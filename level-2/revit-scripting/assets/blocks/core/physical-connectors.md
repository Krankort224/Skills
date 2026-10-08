# Verified physical HVAC connectors

## Contents

- [Contract](#contract)
- [Purpose](#purpose)
- [Inputs and outputs](#inputs-and-outputs)
- [Implementation](#implementation)
- [Adaptation and limits](#adaptation-and-limits)
- [Verification](#verification)
- [Provenance](#provenance)

## Contract

| Field | Value |
|---|---|
| id | physical-connectors |
| group | core |
| status | reviewed |
| runtime | Revit 2022 / Dynamo 2.12 / IronPython 2.7; Python 3 with compatible Revit host |
| verification | offline |
| dependencies | none |
| mutation | read-only |

## Purpose

Extract HVAC ports and actual physical edges from MEPCurve or family MEPModel connectors. AllRefs alone is not evidence of physical connection.

## Inputs and outputs

`physical_hvac_graph(elements, document_key, api=None)` returns `ports`, `edges`, and `warnings`. Input elements belong to one explicit document namespace. Ports contain owner/connector IDs, origin, direction, shape, dimensions and connection state. Edges identify both endpoint ports, always carry `physical_is_connected_to` provenance, and may reach owners outside the supplied collection; boundary filtering belongs to the graph caller.

## Implementation

```python
# -*- coding: utf-8 -*-
def physical_hvac_graph(elements, document_key, api=None):
    if api is None:
        import Autodesk.Revit.DB as api
    if not document_key:
        raise ValueError('document_key is required')
    elements = list(elements)
    source_document = elements[0].Document if elements else None
    if elements and source_document is None:
        raise ValueError('Actual source Document is required')
    if any(element.Document != source_document for element in elements):
        raise ValueError('Supplied elements must share one actual Document')
    ports, edges, warnings = {}, {}, []
    allowed = [getattr(api.ConnectorType, name, None)
               for name in ('End', 'Curve', 'Physical')]
    allowed = [value for value in allowed if value is not None]
    def eid(value):
        if hasattr(value, 'Value'):
            return int(value.Value)
        if hasattr(value, 'IntegerValue'):
            return int(value.IntegerValue)
        raise ValueError('Native ID has no Value or IntegerValue')
    def xyz(value):
        return (float(value.X), float(value.Y), float(value.Z))
    def physical(connector):
        try:
            return (connector.Domain == api.Domain.DomainHvac and
                    connector.ConnectorType in allowed and
                    not isinstance(connector.Owner, api.MEPSystem))
        except Exception as error:
            warnings.append('connector-filter-read: %s' % error)
            return False
    def port(connector):
        owner = connector.Owner
        if owner.Document != source_document:
            raise ValueError('Reference owner belongs to another document')
        owner_id = eid(owner.Id)
        connector_id = int(connector.Id)
        if owner_id < 0 or connector_id < 0:
            raise ValueError('Port identity unavailable')
        key = '%s:%s:%s' % (document_key, owner_id, connector_id)
        if key not in ports:
            row = {'id': key, 'owner_id': owner_id,
                   'connector_id': connector_id,
                   'origin': xyz(connector.Origin),
                   'domain': str(connector.Domain),
                   'connector_type': str(connector.ConnectorType),
                   'is_connected': bool(connector.IsConnected)}
            for name in ('Shape', 'Radius', 'Width', 'Height'):
                try:
                    raw = getattr(connector, name)
                    row[name.lower()] = (str(raw) if name == 'Shape'
                                         else float(raw))
                except Exception:
                    row[name.lower()] = None
            try:
                row['direction'] = xyz(connector.CoordinateSystem.BasisZ)
            except Exception:
                row['direction'] = None
            ports[key] = row
        return key
    for element in elements:
        try:
            manager = getattr(element, 'ConnectorManager', None)
            if manager is None:
                model = getattr(element, 'MEPModel', None)
                manager = getattr(model, 'ConnectorManager', None)
            if manager is None:
                warnings.append('no_connector_manager: %s' % eid(element.Id))
                continue
            for connector in manager.Connectors:
                if not physical(connector):
                    continue
                source = port(connector)
                for other in connector.AllRefs:
                    if not physical(other):
                        continue
                    if eid(other.Owner.Id) == eid(element.Id):
                        continue
                    if (not connector.IsConnectedTo(other) or
                            not other.IsConnectedTo(connector)):
                        continue
                    target = port(other)
                    pair = tuple(sorted((source, target)))
                    edges[pair] = {'id': '|'.join(pair),
                                   'from': pair[0], 'to': pair[1],
                                   'directed': False,
                                   'provenance': 'physical_is_connected_to'}
        except Exception as error:
            warnings.append('connector_read: %s' % error)
    return {'ports': [ports[key] for key in sorted(ports)],
            'edges': [edges[key] for key in sorted(edges)],
            'warnings': warnings}
```

## Adaptation and limits

Port dimensions and origins use native internal units. Preserve document namespace when merging outputs. Connector IDs are element-scoped; do not infer persistent topology after model edits. This block does not inspect linked models or infer connections from proximity. Read failures produce explicit warnings and may yield a partial graph, so callers requiring completeness must reject warnings. API injection is for tests.

## Verification

Native validation pending. Offline mocks cover MEPCurve and family managers, DomainHvac exclusion, logical/system refs, unconnected AllRefs, reciprocal IsConnectedTo verification, edge deduplication, port metadata, partial-read warnings, throwing Domain reads with explicit partial-graph warnings, actual mixed-document rejection and 64-bit IDs without eager legacy access. They do not prove native connector enumeration or regenerated connection states.

## Provenance

Adapted from [Revit Core at f6b4a430](https://github.com/Krankort224/Revit-automatization/blob/f6b4a4301ef70187780150acf44f6e5140a6c339/src/block_0_core/block_0_core_current.py), `connector_manager_of`, `connectors_of`, `connector_refs`, `build_system_graph_layer`; and [CFD parameter fill at 6f6ff374](https://github.com/Krankort224/CFD-modeling/blob/6f6ff37416a4145313737cb9c23a311d3e8ebedb/tools/py/20_VRU_FillParameters.py), `connector_manager`, `physical_hvac_connectors`. Added exact domain/type exclusions and verified reciprocal physical edges; removed proximity and implicit global documents.
