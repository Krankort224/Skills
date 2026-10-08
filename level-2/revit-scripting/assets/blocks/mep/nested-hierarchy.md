# Trace nested family hierarchy

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
| id | nested-hierarchy |
| group | mep |
| status | reviewed |
| runtime | Revit 2022 / Dynamo 2.12 / IronPython 2.7; pure helpers Python 2.7 or 3 |
| verification | offline |
| dependencies | none |
| mutation | read-only |

## Purpose

Trace explicit roots without unbounded global scans. Retain multiple-parent evidence, per-root reachability, cycles, unavailable elements and traversal limits.

## Inputs and outputs

`trace_nested` accepts root IDs, lookup/children callbacks, positive node/depth limits and optional explicit parent-child edges. `revit_nested` accepts root elements and optional finite `super_scope` elements whose `SuperComponent` links supplement API child lists. Return records, edges with source, cycle paths and issues; `complete=False` means errors or limits prevented a complete trace.

## Implementation

```python
def nested_id(value):
    value = getattr(value, 'Id', value)
    return int(getattr(value, 'IntegerValue', value))


def trace_nested(root_ids, resolve, children, extra_edges=None,
                 max_nodes=1000, max_depth=20):
    if max_nodes < 1 or max_depth < 1:
        raise ValueError('Traversal limits must be positive')
    roots = sorted(set(nested_id(x) for x in root_ids))
    extra = {}
    for parent, child in extra_edges or []:
        extra.setdefault(nested_id(parent), set()).add(nested_id(child))
    records, edges, issues, cycles = {}, {}, [], []
    visited = set()
    stack = [(root, root, None, 0, ()) for root in reversed(roots)]
    while stack:
        ident, root, parent, depth, ancestry = stack.pop()
        if ident in ancestry:
            cycles.append(list(ancestry) + [ident])
            continue
        if (root, ident) in visited:
            continue
        if depth > max_depth:
            issues.append({'id': ident, 'root': root, 'status': 'DEPTH_LIMIT'})
            continue
        if ident not in records and len(records) >= max_nodes:
            issues.append({'id': ident, 'root': root, 'status': 'NODE_LIMIT'})
            continue
        visited.add((root, ident))
        row = records.setdefault(ident, {'id': ident, 'roots': set(),
                                         'parents': set(), 'available': False})
        row['roots'].add(root)
        if parent is not None:
            row['parents'].add(parent)
        try:
            element = resolve(ident)
            if element is None:
                raise ValueError('Element unavailable')
            row['available'] = True
            direct = set(nested_id(x) for x in children(element))
        except Exception as error:
            issues.append({'id': ident, 'root': root, 'status': 'API_ERROR',
                           'error': str(error)})
            direct = set()
        all_children = direct | extra.get(ident, set())
        for child in sorted(all_children, reverse=True):
            key = (ident, child)
            sources = edges.setdefault(key, set())
            if child in direct:
                sources.add('GetSubComponentIds')
            if child in extra.get(ident, set()):
                sources.add('SuperComponent_SCOPE')
            # Record a second parent even when this root already visited child.
            if child in records:
                records[child]['parents'].add(ident)
            stack.append((child, root, ident, depth + 1, ancestry + (ident,)))
    for row in records.values():
        row['roots'] = sorted(row['roots'])
        row['parents'] = sorted(row['parents'])
        row['multiple_parents'] = len(row['parents']) > 1
    return {'records': [records[i] for i in sorted(records)],
            'edges': [{'parent': p, 'child': c, 'sources': sorted(edges[(p,c)])}
                      for p,c in sorted(edges)],
            'cycles': cycles, 'issues': issues, 'complete': not issues and not cycles}


def revit_nested(doc, roots, super_scope=None, max_nodes=1000, max_depth=20):
    from Autodesk.Revit import DB
    extra, scan_errors = [], []
    for index, element in enumerate(super_scope or []):
        if index >= max_nodes:
            raise ValueError('Explicit SuperComponent scope exceeds max_nodes')
        try:
            parent = element.SuperComponent
            if parent is not None:
                extra.append((nested_id(parent), nested_id(element)))
        except Exception as error:
            scan_errors.append({'id': nested_id(element), 'status': 'SUPER_ERROR',
                                'error': str(error)})
    result = trace_nested(roots, lambda i: doc.GetElement(DB.ElementId(i)),
                          lambda e: e.GetSubComponentIds(), extra,
                          max_nodes, max_depth)
    result['issues'].extend(scan_errors)
    result['complete'] = result['complete'] and not scan_errors
    return result
```

## Adaptation and limits

Only elements reachable from roots are returned. Supplemental parent scanning is explicit and bounded; never collect all FamilyInstances implicitly. Multiple parents describe conflicting evidence, not a valid tree to silently collapse. Cycle edges remain visible. Root/parent IDs are document-local provenance. Does not promote nested devices into independent terminals or change selection/pinned state.

## Verification

Executed `python scripts/test_mep_blocks.py`: 31 tests passed across the five exact Markdown implementation fences (2026-10-08, CPython 3.12). Tests cover pure algorithms and mocked API success/error/rollback; they do not establish native Revit behavior or source runtime inheritance. IronPython 2.7 syntax compatibility is intentional but not executed in this environment.

## Provenance

[CFD-modeling graph](https://github.com/Krankort224/CFD-modeling/blob/6f6ff37416a4145313737cb9c23a311d3e8ebedb/tools/dyn/00_CFD_ModelSnapshot.dyn), pin `6f6ff37416a4145313737cb9c23a311d3e8ebedb`: embedded `collect_recursive_subcomponent_ids`, `split_top_level_family_instances`. Adapted into bounded iterative traversal with per-root and multiple-parent provenance; optional explicit SuperComponent scope replaces global scanning.

Uploaded scripts archive SHA256 `6caa68eb49c6e9cec087eb4b280336d0d8300df9635c4ad719bea1240472b20e`: graph `KOV_Запись имени системы и группирование.dyn`, node `4dbd9fcaa3634fa3b5e8783dec06617b`, `walk_subcomponents_from`, `add_edge`. Removed global family scanning and project parameter writes; preserved edge provenance.
