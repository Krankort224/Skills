#!/usr/bin/env python3
"""Inspect Dynamo JSON without evaluating node code. Python 3 standard library only."""
import argparse
import hashlib
import json
import re
import sys
import zipfile
from collections import Counter
from pathlib import Path, PurePosixPath


class InspectionError(ValueError):
    pass


def safe_member(name):
    """Reject ambiguous or escaping ZIP names, including Windows spellings."""
    normalized = name.replace('\\', '/')
    p = PurePosixPath(normalized)
    if p.is_absolute() or '..' in p.parts or re.match(r'^[A-Za-z]:', normalized):
        raise InspectionError('unsafe ZIP member: ' + name)
    return normalized


def read_graphs(path):
    path = Path(path)
    if zipfile.is_zipfile(path):
        with zipfile.ZipFile(path) as archive:
            members = archive.infolist()
            for entry in members:
                safe_member(entry.filename)
                if (entry.external_attr >> 16) & 0o170000 == 0o120000:
                    raise InspectionError('ZIP symlink is not supported: ' + entry.filename)
            names = [e.filename for e in members if e.filename.lower().endswith('.dyn')]
            if len(names) != len(set(names)):
                raise InspectionError('duplicate ZIP graph member names')
            sources = [(n, archive.read(n)) for n in sorted(names)]
    elif path.suffix.lower() == '.dyn':
        sources = [(path.name, path.read_bytes())]
    else:
        raise InspectionError('input must be a .dyn file or ZIP archive')
    if not sources:
        raise InspectionError('archive contains no .dyn graphs')
    result = []
    for name, raw in sources:
        try:
            graph = json.loads(raw.decode('utf-8-sig'))
        except (UnicodeError, ValueError) as exc:
            raise InspectionError('{}: invalid UTF-8 JSON: {}'.format(name, exc)) from exc
        if not isinstance(graph, dict) or not isinstance(graph.get('Nodes'), list):
            raise InspectionError(name + ': expected a JSON object with Nodes array')
        if not isinstance(graph.get('Connectors', []), list):
            raise InspectionError(name + ': Connectors must be an array')
        result.append((name, raw, graph))
    return result


def summarize(graph, source='graph.dyn', code_id=None):
    nodes, port_map, node_map, diagnostics = [], {}, {}, []
    for node in graph['Nodes']:
        if not isinstance(node, dict) or not isinstance(node.get('Id'), str):
            raise InspectionError(source + ': each node requires a string Id')
        nid = node['Id']
        if nid in node_map:
            diagnostics.append({'kind': 'duplicate_node_id', 'node_id': nid})
        entry = {'id': nid, 'name': node.get('Name', node.get('NodeType', '')),
                 'type': node.get('ConcreteType', node.get('NodeType', '')),
                 'engine': node.get('Engine'), 'inputs': [], 'outputs': []}
        is_python = 'Python' in str(entry['type']) or 'Python' in str(node.get('NodeType', ''))
        entry['is_python'] = is_python
        for key, direction in [('Inputs', 'inputs'), ('Outputs', 'outputs')]:
            ports = node.get(key, [])
            if not isinstance(ports, list):
                raise InspectionError(source + ': node port lists must be arrays')
            for index, port in enumerate(ports):
                if not isinstance(port, dict) or not isinstance(port.get('Id'), str):
                    raise InspectionError(source + ': each port requires a string Id')
                item = {'id': port['Id'], 'name': port.get('Name', ''), 'index': index}
                entry[direction].append(item)
                endpoint = {'node_id': nid, 'port_id': item['id'],
                            'port_name': item['name'], 'port_index': index,
                            'direction': direction}
                if item['id'] in port_map:
                    diagnostics.append({'kind': 'duplicate_port_id', 'port_id': item['id']})
                port_map[item['id']] = endpoint
        if is_python and len(entry['outputs']) != 1:
            diagnostics.append({'kind': 'python_output_count', 'node_id': nid,
                                'expected': 1, 'actual': len(entry['outputs'])})
        if code_id == nid:
            entry['code'] = node.get('Code', '')
        nodes.append(entry)
        node_map[nid] = entry

    def endpoint(connector, key, direction):
        ident = connector.get(key)
        if ident in port_map:
            return dict(port_map[ident])
        index = connector.get(key + 'Index', connector.get(key + 'Port', 0))
        if ident in node_map and isinstance(index, int):
            ports = node_map[ident][direction]
            if 0 <= index < len(ports):
                return dict(port_map[ports[index]['id']])
        return {'node_id': ident if ident in node_map else None,
                'port_id': ident, 'port_index': index, 'missing': True}

    connectors, counts, seen = [], Counter(), set()
    for conn in graph.get('Connectors', []):
        if not isinstance(conn, dict):
            raise InspectionError(source + ': connectors must be objects')
        start, end = endpoint(conn, 'Start', 'outputs'), endpoint(conn, 'End', 'inputs')
        cid = conn.get('Id')
        connectors.append({'id': cid, 'source': start, 'target': end})
        for side, point, direction in [('source', start, 'outputs'), ('target', end, 'inputs')]:
            if point.get('missing'):
                diagnostics.append({'kind': 'missing_endpoint', 'connector_id': cid,
                                    'side': side, 'endpoint_id': point['port_id']})
            elif point['direction'] != direction:
                diagnostics.append({'kind': 'wrong_port_direction', 'connector_id': cid,
                                    'side': side, 'port_id': point['port_id']})
            else:
                counts[point['port_id']] += 1
        pair = (start['port_id'], start['port_index'], end['port_id'], end['port_index'])
        if pair in seen:
            diagnostics.append({'kind': 'duplicate_wire', 'connector_id': cid})
        seen.add(pair)
    unconnected = []
    for pid, point in port_map.items():
        if counts[pid] == 0:
            unconnected.append(dict(point))
        elif point['direction'] == 'inputs' and counts[pid] > 1:
            diagnostics.append({'kind': 'multiply_connected_input', 'port_id': pid,
                                'connection_count': counts[pid]})
    view = graph.get('View', {})
    if not isinstance(view, dict):
        raise InspectionError(source + ': View must be a JSON object')
    dynamo = view.get('Dynamo', {})
    if not isinstance(dynamo, dict):
        raise InspectionError(source + ': View.Dynamo must be a JSON object')
    return {'source': source, 'name': graph.get('Name'), 'uuid': graph.get('Uuid'),
            'dynamo_version': dynamo.get('Version'),
            'engines': sorted({n['engine'] for n in nodes if n['engine']}),
            'graph_inputs': graph.get('Inputs', []), 'graph_outputs': graph.get('Outputs', []),
            'nodes': nodes, 'connectors': connectors, 'unconnected_ports': unconnected,
            'diagnostics': diagnostics}


def extract_graphs(records, destination):
    """Write only inspected graphs and their code; no archive paths are reused."""
    dest = Path(destination)
    dest.mkdir(parents=True, exist_ok=True)
    written = []
    for name, raw, graph in records:
        stem = re.sub(r'[^A-Za-z0-9_-]+', '_', Path(name).stem)[:60] or 'graph'
        tag = hashlib.sha256(name.encode('utf-8')).hexdigest()[:16]
        prefix = stem + '-' + tag
        files = [(prefix + '.dyn', raw)]
        for index, node in enumerate(graph['Nodes']):
            if 'Code' in node and ('Python' in str(node.get('ConcreteType', '')) or
                                   'Python' in str(node.get('NodeType', ''))):
                nid = str(node.get('Id', index))
                node_tag = hashlib.sha256(nid.encode('utf-8')).hexdigest()[:16]
                files.append((prefix + '-{}-{}.py'.format(index, node_tag),
                              node['Code'].encode('utf-8')))
        for filename, content in files:
            target = dest / filename
            if target.is_symlink():
                raise InspectionError('refusing extraction into symlink: ' + str(target))
            if target.exists() and target.read_bytes() != content:
                raise InspectionError('refusing to overwrite different content: ' + str(target))
            target.write_bytes(content)
            written.append(str(target))
    return written


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('input')
    parser.add_argument('--code', metavar='NODE_ID', help='include this node code in JSON')
    parser.add_argument('--extract', metavar='DIR', help='extract inspected graphs and Python text')
    args = parser.parse_args(argv)
    try:
        records = read_graphs(args.input)
        graphs = [summarize(g, name, args.code) for name, _, g in records]
        if args.code and not any(any(n['id'] == args.code for n in g['nodes']) for g in graphs):
            raise InspectionError('node ID not found: ' + args.code)
        result = {'graphs': graphs}
        if args.extract:
            result['extracted_files'] = extract_graphs(records, args.extract)
        print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
        return 0
    except (OSError, ValueError, TypeError, zipfile.BadZipFile, KeyError) as exc:
        print(json.dumps({'error': str(exc)}, ensure_ascii=False), file=sys.stderr)
        return 1


if __name__ == '__main__':
    sys.exit(main())
