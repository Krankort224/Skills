# Canonical connector size signatures

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
| id | connector-size-signature |
| group | mep |
| status | reviewed |
| runtime | Revit 2022 / Dynamo 2.12 / IronPython 2.7; pure helpers Python 2.7 or 3 |
| verification | offline |
| dependencies | none |
| mutation | read-only |

## Purpose

Produce round/rectangular connector sizes in millimetres with deterministic orientation, tolerance deduplication and area ordering.

## Inputs and outputs

`size_signatures` consumes records with `shape` (`Round` or `Rectangular`), `diameter_mm` or `width_mm`/`height_mm`, optional `id`, `logical`, `domain`. Output includes unique signatures with contributing IDs, area and rejected-record reasons. `connector_size_records` adapts a single live element. Configure logical exclusion, allowed domains and rectangle axis preservation.

## Implementation

```python
import math


def size_finite(value):
    value = float(value)
    if math.isnan(value) or math.isinf(value) or value <= 0:
        raise ValueError('Dimension must be finite and positive')
    return value


def size_signatures(records, tolerance_mm=0.1, preserve_axes=False,
                    exclude_logical=True, allowed_domains=None):
    if tolerance_mm < 0 or math.isnan(tolerance_mm) or math.isinf(tolerance_mm):
        raise ValueError('Invalid dimension tolerance')
    accepted, rejected = [], []
    for index, record in enumerate(records):
        ident = record.get('id', index)
        try:
            if exclude_logical and record.get('logical', False):
                raise ValueError('LOGICAL_EXCLUDED')
            if allowed_domains is not None and record.get('domain') not in allowed_domains:
                raise ValueError('DOMAIN_EXCLUDED')
            shape = record.get('shape')
            if shape == 'Round':
                dims = [size_finite(record['diameter_mm'])]
                area = math.pi * dims[0] * dims[0] / 4.0
            elif shape == 'Rectangular':
                dims = [size_finite(record['width_mm']), size_finite(record['height_mm'])]
                if not preserve_axes:
                    dims.sort(reverse=True)
                area = dims[0] * dims[1]
            else:
                raise ValueError('UNSUPPORTED_SHAPE: %s' % shape)
            accepted.append({'shape': shape, 'dimensions_mm': dims,
                             'area_mm2': area, 'connector_ids': [ident]})
        except Exception as error:
            rejected.append({'id': ident, 'reason': str(error)})
    accepted.sort(key=lambda r: (r['area_mm2'], r['shape'], r['dimensions_mm']))
    unique = []
    for row in accepted:
        match = next((prior for prior in unique
                      if prior['shape'] == row['shape'] and all(
                          abs(a-b) <= tolerance_mm for a,b in zip(
                              prior['dimensions_mm'], row['dimensions_mm']))), None)
        if match is None:
            unique.append(row)
        else:
            match['connector_ids'].extend(row['connector_ids'])
    return {'signatures': unique, 'rejected': rejected,
            'rectangle_orientation': 'AXIS_PRESERVED' if preserve_axes else 'LARGE_SMALL',
            'tolerance_mm': tolerance_mm}


def connector_size_records(element):
    manager = getattr(element, 'ConnectorManager', None)
    if manager is None:
        model = getattr(element, 'MEPModel', None)
        manager = getattr(model, 'ConnectorManager', None)
    if manager is None:
        return {'records': [], 'issues': ['NO_CONNECTOR_MANAGER']}
    records, issues = [], []
    for index, connector in enumerate(manager.Connectors):
        try:
            shape = str(connector.Shape)
            row = {'id': int(connector.Id), 'shape': shape,
                   'logical': str(connector.ConnectorType) == 'Logical',
                   'domain': str(connector.Domain)}
            if shape == 'Round':
                row['diameter_mm'] = float(connector.Radius) * 2 * 304.8
            elif shape == 'Rectangular':
                row['width_mm'] = float(connector.Width) * 304.8
                row['height_mm'] = float(connector.Height) * 304.8
            records.append(row)
        except Exception as error:
            issues.append({'index': index, 'error': str(error)})
    return {'records': records, 'issues': issues}
```

## Adaptation and limits

Default rectangle signature is larger-side/smaller-side, independent of roll; set `preserve_axes=True` when width/height meaning matters. Dimensions remain measured floats, not nominal type labels. Tolerance uses deterministic representative matching, not transitive clustering: A≈B and B≈C need not merge A with C. Oval/undefined shapes are explicitly rejected; adding oval support requires defining major/minor semantics. Logical exclusion defaults on. Configure `allowed_domains=['DomainHvac']` for HVAC only. Reacquire live connectors after regeneration. No connector writes.

## Verification

Executed `python scripts/test_mep_blocks.py`: 31 tests passed across the five exact Markdown implementation fences (2026-10-08, CPython 3.12). Tests cover pure algorithms and mocked API success/error/rollback; they do not establish native Revit behavior or source runtime inheritance. IronPython 2.7 syntax compatibility is intentional but not executed in this environment.

## Provenance

[CFD-modeling helpers](https://github.com/Krankort224/CFD-modeling/blob/6f6ff37416a4145313737cb9c23a311d3e8ebedb/tools/py/10_VRU_Place.py), pin `6f6ff37416a4145313737cb9c23a311d3e8ebedb`: `connector_manager`, `physical_hvac_connectors`, `connector_dimensions_mm`. Adapted as read-only record adapter plus pure signatures; removed family-specific primary-port selection and size writes.

Uploaded scripts archive SHA256 `6caa68eb49c6e9cec087eb4b280336d0d8300df9635c4ad719bea1240472b20e`: graph `KOV_Сборка спецификации воздуховодов.dyn`, size node `b6c1ee8881064d69b388405aa402f375`, `conn_dims_ft`, `conn_area_ft2`, `normalize_rect`, `build_size_from_connectors`. Added deterministic float-tolerance deduplication, explicit logical/domain policy and unsupported-shape reporting.
