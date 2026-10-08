# Resolve records by position and explicit semantics

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
| id | positional-resolution |
| group | mep |
| status | reviewed |
| runtime | Python 2.7 or 3; Revit record extraction caller-owned |
| verification | offline |
| dependencies | none |
| mutation | read-only |

## Purpose

Resolve serialized targets to live candidate records using coordinate distance and explicit semantic filters. Do not use saved ElementId as matching authority.

## Inputs and outputs

Records require `point_mm` (three coordinates). Candidates require unique `id`; targets use optional `key` and provenance fields. Exact `identity_fields` default to `family,type,system`; each target must contain these unless caller explicitly supplies a different field list. Optional `size_mm` is compared componentwise. Output is FOUND, NOT_FOUND, AMBIGUOUS, OCCUPIED or INVALID_TARGET with candidate evidence. `resolve_positions` enforces one-to-one occupancy in explicit target order and preserves its caller-owned occupied set.

## Implementation

```python
import math


def position_values(values, count=None):
    result = [float(v) for v in values]
    if count is not None and len(result) != count:
        raise ValueError('Unexpected coordinate/dimension count')
    if any(math.isnan(v) or math.isinf(v) for v in result):
        raise ValueError('Nonfinite geometry')
    return result


def resolve_position(target, candidates, occupied=None, tolerance_mm=5.0,
                     identity_fields=('family', 'type', 'system'),
                     size_tolerance_mm=0.1):
    if (tolerance_mm < 0 or size_tolerance_mm < 0 or
            any(math.isnan(float(v)) or math.isinf(float(v))
                for v in (tolerance_mm, size_tolerance_mm))):
        raise ValueError('Invalid matching tolerance')
    try:
        expected = position_values(target['point_mm'], 3)
        for field in identity_fields:
            if field not in target or target[field] is None:
                raise ValueError('Missing expected identity: %s' % field)
        size = position_values(target['size_mm']) if 'size_mm' in target else None
        if size is not None and (not size or min(size) <= 0):
            raise ValueError('Invalid target size')
    except Exception as error:
        return {'status': 'INVALID_TARGET', 'error': str(error), 'candidates': []}
    occupied = set(occupied or [])
    matches, invalid = [], []
    seen = set()
    for candidate in candidates:
        try:
            ident = candidate['id']
            if ident is None:
                raise ValueError('Missing candidate ID')
            if any(field not in candidate or candidate[field] is None for field in identity_fields):
                raise ValueError('Missing candidate identity')
            if ident in seen:
                raise ValueError('Duplicate candidate ID')
            seen.add(ident)
            point = position_values(candidate['point_mm'], 3)
            if any(candidate.get(field) != target[field] for field in identity_fields):
                continue
            if size is not None:
                actual_size = position_values(candidate['size_mm'], len(size))
                if any(v <= 0 for v in actual_size):
                    raise ValueError('Invalid candidate size')
                if any(abs(a-b) > size_tolerance_mm for a,b in zip(size, actual_size)):
                    continue
            distance = math.sqrt(sum((a-b)**2 for a,b in zip(expected, point)))
            if distance <= tolerance_mm:
                matches.append({'id': ident, 'distance_mm': distance,
                                'occupied': ident in occupied})
        except Exception as error:
            invalid.append({'id': candidate.get('id'), 'error': str(error)})
    available = [row for row in matches if not row['occupied']]
    status = ('AMBIGUOUS' if len(available) > 1 else 'FOUND' if available else
              'OCCUPIED' if matches else 'NOT_FOUND')
    result = {'status': status, 'method': 'POINT_DISTANCE_AND_EXACT_FILTERS',
              'candidates': matches, 'invalid_candidates': invalid}
    # Invalid records can hide a second match: uniqueness is unverified.
    if invalid:
        result['status'] = 'INVALID_CANDIDATES'
    elif status == 'FOUND':
        result['id'] = available[0]['id']
    return result


def resolve_positions(targets, candidates, occupied=None, **options):
    candidates = list(candidates)
    reserved = set(occupied or [])
    results = []
    for index, target in enumerate(targets):
        result = resolve_position(target, candidates, reserved, **options)
        result['key'] = target.get('key', index)
        if result['status'] == 'FOUND':
            reserved.add(result['id'])
        results.append(result)
    return {'results': results, 'occupied_ids': sorted(reserved)}
```

## Adaptation and limits

Use the same host-coordinate datum and unit for targets/candidates. Identity/system normalization belongs to the caller and must be symmetric. Round diameter versus rectangle dimensions must use compatible explicit size signatures. Any malformed candidate makes the entire supplied index unsafe and returns INVALID_CANDIDATES, even if another record matches. This conservative rule prevents false uniqueness claims from partial data. Ambiguity is rejected even if one candidate is slightly nearer; do not silently choose it. IDs identify current candidates and occupancy only; target ElementId/provenance fields are ignored. This block performs distance matching only: no solid intersection, bounding box cube or native identity checks are implied. Does not write Revit or mutate caller records.

## Verification

Executed `python scripts/test_mep_blocks.py`: 31 tests passed across the five exact Markdown implementation fences (2026-10-08, CPython 3.12). Tests cover pure algorithms and mocked API success/error/rollback; they do not establish native Revit behavior or source runtime inheritance. IronPython 2.7 syntax compatibility is intentional but not executed in this environment.

## Provenance

[CFD-modeling geometry resolver](https://github.com/Krankort224/CFD-modeling/blob/6f6ff37416a4145313737cb9c23a311d3e8ebedb/tools/py/10_VRU_Place.py), pin `6f6ff37416a4145313737cb9c23a311d3e8ebedb`: `candidate_current_report`, `find_current_grille_geometrically`. Generalized the geometry-only identity principle into pure point-distance matching. Does not copy `20.resolve_record`'s solid-overlap algorithm or claim its behavior.
