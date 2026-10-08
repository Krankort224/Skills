# Bounded graph traversal with shared ownership

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
| id | bounded-graph |
| group | core |
| status | reviewed |
| runtime | Python 2.7 or 3 |
| verification | offline |
| dependencies | none |
| mutation | read-only |

## Purpose

Traverse a supplied graph without turning it into a tree. Preserve cycles, shared ownership and original edge provenance while applying explicit stop/exclude boundaries and finite budgets.

## Inputs and outputs

`bounded_graph(edges, seeds, boundary=None, max_nodes=1000, max_edges=2000, max_visits=10000)` accepts unique edge IDs with `from`, `to`, `provenance`, optional `directed`; `seeds` maps owner IDs to seed lists. `boundary(node, owner)` returns `expand`, `stop` or `exclude`; default is expand. Returns accepted nodes/edges, ownership lists, excluded boundary events, visit count and explicit truncation reasons. Identifiers must be hashable. Budgets are global across owners, not depth limits.

## Implementation

```python
# -*- coding: utf-8 -*-
def bounded_graph(edges, seeds, boundary=None, max_nodes=1000,
                  max_edges=2000, max_visits=10000):
    from collections import deque
    for cap in (max_nodes, max_edges, max_visits):
        if isinstance(cap, bool) or int(cap) != cap or cap < 0:
            raise ValueError('Caps must be nonnegative integers')
    adjacency, edge_by_id = {}, {}
    for raw in edges:
        edge = dict(raw)
        if not all(key in edge for key in ('id', 'from', 'to', 'provenance')):
            raise ValueError('Missing edge identity or provenance')
        if not isinstance(edge['directed'] if 'directed' in edge else False,
                          bool):
            raise ValueError('directed must be Boolean')
        if not edge['provenance']:
            raise ValueError('Explicit provenance required')
        key = edge['id']
        if key in edge_by_id:
            raise ValueError('Duplicate edge ID')
        edge_by_id[key] = edge
        adjacency.setdefault(edge['from'], []).append((edge['to'], key))
        if not edge.get('directed', False):
            adjacency.setdefault(edge['to'], []).append((edge['from'], key))
    nodes, accepted_edges, ownership = set(), set(), {}
    seen, queued, queue = set(), set(), deque()
    exclusions, reasons, visits = [], set(), 0
    for owner in sorted(seeds, key=lambda item: repr(item)):
        for node in seeds[owner]:
            state = (owner, node)
            if state not in queued:
                queue.append(state)
                queued.add(state)
    policy = boundary or (lambda node, owner: 'expand')
    while queue:
        if visits >= max_visits:
            reasons.add('max_visits')
            break
        owner, node = queue.popleft()
        state = (owner, node)
        if state in seen:
            continue
        seen.add(state)
        visits += 1
        action = policy(node, owner)
        if action not in ('expand', 'stop', 'exclude'):
            raise ValueError('Unknown boundary action')
        if action == 'exclude':
            exclusions.append({'owner': owner, 'node': node})
            continue
        if node not in nodes and len(nodes) >= max_nodes:
            reasons.add('max_nodes')
            continue
        nodes.add(node)
        ownership.setdefault(node, set()).add(owner)
        if action == 'stop':
            continue
        for target, edge_id in adjacency.get(node, []):
            target_action = policy(target, owner)
            if target_action not in ('expand', 'stop', 'exclude'):
                raise ValueError('Unknown boundary action')
            if target_action == 'exclude':
                exclusions.append({'owner': owner, 'node': target})
                continue
            if target not in nodes and len(nodes) >= max_nodes:
                reasons.add('max_nodes')
                continue
            if edge_id not in accepted_edges and len(accepted_edges) >= max_edges:
                reasons.add('max_edges')
                continue
            nodes.add(target)
            accepted_edges.add(edge_id)
            target_state = (owner, target)
            if target_state not in queued:
                queue.append(target_state)
                queued.add(target_state)
    ordered_nodes = sorted(nodes, key=lambda item: repr(item))
    return {'nodes': ordered_nodes,
            'edges': [edge_by_id[key] for key in
                      sorted(accepted_edges, key=lambda item: repr(item))],
            'ownership': dict((node, sorted(ownership.get(node, set()),
                                           key=lambda item: repr(item)))
                              for node in ordered_nodes),
            'excluded': exclusions, 'visits': visits,
            'truncated': bool(reasons), 'limit_reasons': sorted(reasons)}
```

## Adaptation and limits

Boundary callbacks must be pure and deterministic; they can be called more than once. Ownership describes completed visits, so nodes admitted immediately before a visit cap may have empty ownership; `truncated=True` requires caller review. Stop nodes are included but not expanded for that owner. Input allocation is not capped: reject oversized source graphs before calling if memory is constrained. Proximity provenance remains proximity, never physical. No Revit dependencies or implied connection inference.

## Verification

Offline cases test cycles, shared nodes with multiple owners, stop/exclude policy, directed edges, all three caps, malformed provenance and duplicate IDs. No native Revit run is claimed or needed for this pure traversal; integration with model-specific graph extraction remains pending.

## Provenance

Generalized from [Revit Core at f6b4a430](https://github.com/Krankort224/Revit-automatization/blob/f6b4a4301ef70187780150acf44f6e5140a6c339/src/block_0_core/block_0_core_current.py), `build_system_graph_layer`, `SystemGraphDsu`, `build_node_proximity_graph`. Traversal is a new bounded BFS adaptation rather than a verbatim DSU extraction; explicit per-owner visited states preserve shared ownership and supplied provenance.
