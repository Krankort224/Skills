#!/usr/bin/env python3
"""Offline regression tests using independent temporary libraries; never run snippets."""
import copy
import io
import json
import tempfile
import unittest
import zipfile
from contextlib import redirect_stdout, redirect_stderr
from pathlib import Path

import check_library as library
import inspect_dyn as inspector

ROOT = Path(__file__).resolve().parents[1]


def block(ident='sample', group='core', dependencies='none', verification='static'):
    values = dict(id=ident, group=group, status='draft', runtime='Python 2.7 or 3',
                  verification=verification, dependencies=dependencies, mutation='read-only')
    table = '\n'.join('| {} | {} |'.format(k, values[k]) for k in library.FIELDS)
    return '''# Sample\n\n## Contract\n\n| Field | Value |\n| --- | --- |\n%s\n
## Purpose\n\nReturn the input value.\n
## Inputs and outputs\n\nIN[0] is any value. OUT is the same value.\n
## Implementation\n\n```python\nOUT = IN[0]\n```\n
## Adaptation and limits\n\nNo Revit API access.\n
## Verification\n\nSyntax inspected offline; no runtime claim.\n
## Provenance\n\nOriginal test fixture authored for structural validation.\n''' % table


class InspectorTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.graph = json.loads((ROOT / 'assets/examples/graph-contract.dyn').read_text())
        self.path = self.root / 'sample.dyn'
        self.path.write_text(json.dumps(self.graph))

    def tearDown(self):
        self.temp.cleanup()

    def test_fixture_and_exact_single_output(self):
        expected = json.loads((ROOT / 'assets/examples/graph-contract.expected.json').read_text())
        actual = {'graphs': [inspector.summarize(self.graph, 'graph-contract.dyn')]}
        self.assertEqual(expected, actual)
        py = next(n for n in actual['graphs'][0]['nodes'] if n['is_python'])
        self.assertEqual(['IN[0]', 'IN[1]'], [p['name'] for p in py['inputs']])
        self.assertEqual(['OUT'], [p['name'] for p in py['outputs']])
        self.assertNotIn('code', py)
        designscript = {'Id': 'ds', 'ConcreteType': 'Dynamo.Graph.Nodes.CodeBlockNodeModel, DynamoCore',
                        'Code': 'x = 1;', 'Inputs': [], 'Outputs': []}
        self.assertFalse(inspector.summarize({'Nodes': [designscript]})['nodes'][0]['is_python'])
        self.graph['Nodes'][2]['Code'] += '\nOUT[0] = 5\n'
        summary = inspector.summarize(self.graph, code_id='python-contract')
        py = next(n for n in summary['nodes'] if n['is_python'])
        self.assertEqual(1, len(py['outputs']))
        self.assertIn('OUT[0]', py['code'])
        self.assertEqual([], summary['unconnected_ports'])
        self.assertEqual(1, summary['connectors'][1]['target']['port_index'])

    def test_bom_and_invalid_json(self):
        self.path.write_bytes(b'\xef\xbb\xbf' + json.dumps(self.graph).encode())
        self.assertEqual(1, len(inspector.read_graphs(self.path)))
        self.path.write_text('{bad')
        with self.assertRaises(inspector.InspectionError):
            inspector.read_graphs(self.path)
        with redirect_stdout(io.StringIO()), redirect_stderr(io.StringIO()):
            self.assertEqual(1, inspector.main([str(self.path)]))

    def test_bad_structure_and_missing_node_code(self):
        self.path.write_text('{"Nodes": {}}')
        with self.assertRaises(inspector.InspectionError):
            inspector.read_graphs(self.path)
        self.path.write_text(json.dumps(self.graph))
        with redirect_stdout(io.StringIO()), redirect_stderr(io.StringIO()):
            self.assertEqual(1, inspector.main([str(self.path), '--code', 'absent']))

    def test_malformed_dynamo_view_reports_error(self):
        self.graph['View']['Dynamo'] = []
        self.path.write_text(json.dumps(self.graph))
        error = io.StringIO()
        with redirect_stdout(io.StringIO()), redirect_stderr(error):
            self.assertEqual(1, inspector.main([str(self.path)]))
        self.assertIn('View.Dynamo must be a JSON object', json.loads(error.getvalue())['error'])

    def test_wire_diagnostics(self):
        self.graph['Connectors'].append(dict(self.graph['Connectors'][0], Id='duplicate'))
        self.graph['Connectors'].append({'Id': 'broken', 'Start': 'absent', 'End': 'python-in-1'})
        kinds = {d['kind'] for d in inspector.summarize(self.graph)['diagnostics']}
        self.assertTrue({'duplicate_wire', 'multiply_connected_input', 'missing_endpoint'} <= kinds)
        self.graph['Nodes'][2]['Outputs'].append({'Id': 'extra', 'Name': 'OUT[1]'})
        self.assertIn('python_output_count', {d['kind'] for d in inspector.summarize(self.graph)['diagnostics']})

    def test_legacy_wiring_and_unconnected_port(self):
        self.graph['Connectors'][0].update(Start='left', StartIndex=0, End='python-contract', EndIndex=0)
        self.graph['Connectors'].pop(1)
        summary = inspector.summarize(self.graph)
        self.assertEqual('left', summary['connectors'][0]['source']['node_id'])
        self.assertEqual({'right-out', 'python-in-1'}, {p['port_id'] for p in summary['unconnected_ports']})

    def test_archive_collision_resistance_and_safe_extraction(self):
        archive = self.root / 'graphs.zip'
        with zipfile.ZipFile(archive, 'w') as z:
            z.writestr('a/sample.dyn', json.dumps(self.graph))
            z.writestr('b/sample.dyn', json.dumps(self.graph))
        records = inspector.read_graphs(archive)
        files = inspector.extract_graphs(records, self.root / 'out')
        self.assertEqual(4, len(set(files)))
        self.assertEqual(files, inspector.extract_graphs(records, self.root / 'out'))
        Path(files[0]).write_text('unrelated existing data')
        with self.assertRaises(inspector.InspectionError):
            inspector.extract_graphs(records, self.root / 'out')

    def test_archive_traversal_and_empty_archive(self):
        archive = self.root / 'bad.zip'
        for name in ('../escaped.dyn', '/absolute.dyn', 'C:\\evil.dyn', 'a\\..\\evil.dyn'):
            with zipfile.ZipFile(archive, 'w') as z:
                z.writestr(name, json.dumps(self.graph))
            with self.assertRaises(inspector.InspectionError, msg=name):
                inspector.read_graphs(archive)
        with zipfile.ZipFile(archive, 'w') as z:
            z.writestr('empty.txt', 'no graphs')
        with self.assertRaises(inspector.InspectionError):
            inspector.read_graphs(archive)


class LibraryTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        for name in library.REQUIRED:
            path = self.root / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text('# Fixture\n')
        (self.root / 'SKILL.md').write_text('---\nname: example\ndescription: Offline validation fixture\n---\n\n# Fixture\n')
        self.path = self.write_block('sample')

    def tearDown(self):
        self.temp.cleanup()

    def write_block(self, ident, group='core', **kwargs):
        path = self.root / 'assets/blocks' / group / (ident + '.md')
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(block(ident, group, **kwargs))
        return path

    def errors(self):
        return [e['error'] for e in library.validate(self.root)['errors']]

    def test_valid_library_and_catalog(self):
        result = library.validate(self.root)
        self.assertTrue(result['valid'], result['errors'])
        catalog = library.catalog(result['blocks'])
        self.assertIn('[sample](core/sample.md)', catalog)
        self.assertIn('Python 2.7 or 3', catalog)
        (self.root / 'assets/blocks/catalog.md').unlink()
        output = io.StringIO()
        with redirect_stdout(output):
            self.assertEqual(0, library.main([str(self.root), '--catalog']))
        self.assertEqual(catalog + '\n', output.getvalue())

    def test_show_exact_one_block_without_loading_others(self):
        self.write_block('broken').write_bytes(b'\xff')
        output = io.StringIO()
        with redirect_stdout(output):
            self.assertEqual(0, library.main([str(self.root), '--show-block', 'sample']))
        self.assertEqual(self.path.read_text(), output.getvalue())
        with redirect_stdout(io.StringIO()):
            self.assertEqual(1, library.main([str(self.root), '--show-block', '../sample']))

    def test_empty_and_required_files(self):
        self.path.unlink()
        (self.root / 'SKILL.md').unlink()
        errors = self.errors()
        self.assertIn('library contains no blocks', errors)
        self.assertIn('required file missing', errors)

    def test_contract_schema_and_duplicate_fields(self):
        self.path.write_text(block().replace('| id | sample |', '| id | Wrong |\n| id | sample |\n| extra | value |'))
        errors = self.errors()
        self.assertIn('duplicate Contract field: id', errors)
        self.assertIn('unknown Contract field: extra', errors)
        self.path.write_text(block().replace('| group | core |', '| group | invalid |').replace('| runtime | Python 2.7 or 3 |', ''))
        self.assertTrue(any('group must' in e for e in self.errors()))
        self.assertIn('missing or empty Contract field: runtime', self.errors())

    def test_dependencies_and_cycles(self):
        self.write_block('sample', dependencies='absent')
        self.assertIn('unknown dependency: absent', self.errors())
        self.write_block('sample', dependencies='other')
        self.write_block('other', group='views', dependencies='sample')
        self.assertTrue(any('dependency cycle' in e for e in self.errors()))

    def test_syntax_fences_and_placeholder(self):
        self.path.write_text(block().replace('OUT = IN[0]', 'OUT = ('))
        self.assertTrue(any('Python syntax error' in e for e in self.errors()))
        self.path.write_text(block().replace('OUT = IN[0]', 'OUT = f"{IN[0]}"'))
        self.assertTrue(any('Python 3-only syntax' in e for e in self.errors()))
        self.path.write_text(block().replace('## Adaptation', '```python\nOUT = 2\n```\n\n## Adaptation'))
        self.assertTrue(any('exactly one' in e for e in self.errors()))
        self.path.write_text(block().replace('Syntax inspected offline; no runtime claim.', 'TODO verify'))
        self.assertIn('Verification contains an unfinished placeholder', self.errors())

    def test_links_containment_existence_and_anchors(self):
        target = self.root / 'references/runtime.md'
        target.write_text('# Runtime\n\n## Valid heading\n')
        self.path.write_text(block() + '\n[good](../../../references/runtime.md#valid-heading)\n')
        self.assertEqual([], self.errors())
        self.path.write_text(block() + '\n[missing](missing.md)\n[bad](../../../references/runtime.md#absent)\n[escape](../../../../outside.md)\n[ref]: referenced-missing.md\n')
        errors = self.errors()
        self.assertTrue(any('does not exist: missing' in e for e in errors))
        self.assertTrue(any('anchor does not exist' in e for e in errors))
        self.assertTrue(any('escapes skill root' in e for e in errors))
        self.assertTrue(any('referenced-missing.md' in e for e in errors))

    def test_runtime_https_evidence_validation(self):
        valid = 'https://project.example.org/evidence/run-2026-10-08.json?signature=abc'
        self.path.write_text(block(verification='runtime') + '\n')
        original = self.path.read_text()
        self.path.write_text(original.replace('no runtime claim.', 'see [evidence](' + valid + ').'))
        self.assertEqual([], self.errors())
        for target in ('missing-evidence.json', '/etc/hosts', '../../../../outside.json',
                       'http://project.example.org/evidence.json', 'ftp://host/evidence.json',
                       'https:///evidence.json', 'https://[broken/evidence.json',
                       'https://host:bad/evidence.json', 'https://host',
                       'https://host/evidence%ZZ.json', 'https://bad..host/evidence.json'):
            self.path.write_text(original.replace('no runtime claim.', 'see [evidence](' + target + ').'))
            self.assertTrue(any('linked evidence' in e for e in self.errors()), target)

    def test_runtime_evidence_and_frontmatter(self):
        self.write_block('sample', verification='runtime')
        self.assertTrue(any('linked evidence' in e for e in self.errors()))
        self.path.write_text(self.path.read_text().replace('no runtime claim.', 'see [evidence](../../../references/runtime.md).'))
        self.assertEqual([], self.errors())
        (self.root / 'SKILL.md').write_text('---\nname:\ndescription: TODO\n---\n')
        self.assertEqual(2, sum('frontmatter' in e for e in self.errors()))


if __name__ == '__main__':
    unittest.main()
