# Map actual MEP insulation and lining

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
| id | host-cover-map |
| group | mep |
| status | reviewed |
| runtime | Revit 2022 / Dynamo 2.12 / IronPython 2.7; pure helpers Python 2.7 or 3 |
| verification | offline |
| dependencies | none |
| mutation | read-only |

## Purpose

Map actual insulation/lining elements to hosts and hosts to actual covers. Keep a missing type-reference parameter separate from absence of a physical cover.

## Inputs and outputs

Pass a document and explicit host elements. Optional `cover_elements` is an explicit, possibly incomplete scope; omit it to collect only InsulationLiningBase elements. Output contains `host_to_covers`, `cover_to_host`, and issues. `references` is optional caller-provided diagnostic data and never establishes cover existence. IDs belong to this document only; the native collector rejects hosts and covers from other documents.

## Implementation

```python
def cover_id(value):
    value = getattr(value, 'Id', value)
    return int(getattr(value, 'IntegerValue', value))


def cover_maps(hosts, covers, resolve, references=None, complete_scope=False):
    references = references or {}
    by_host = {}
    reverse = {}
    issues = []
    for host in hosts:
        ident = cover_id(host)
        by_host[ident] = {'cover_ids': [], 'actual_status': 'UNKNOWN_SCOPE',
                          'reference': references.get(ident, 'NOT_INSPECTED')}
    seen = set()
    for cover in covers:
        ident = cover_id(cover)
        if ident in seen:
            continue
        seen.add(ident)
        try:
            host_id = cover_id(cover.HostElementId)
            if host_id <= 0:
                raise ValueError('Invalid HostElementId')
            host = resolve(host_id)
            if host is None:
                raise ValueError('Host element unavailable')
            reverse[ident] = host_id
            if host_id in by_host:
                by_host[host_id]['cover_ids'].append(ident)
        except Exception as error:
            reverse[ident] = None
            issues.append({'cover_id': ident, 'status': 'UNRESOLVED_HOST',
                           'error': str(error)})
    for row in by_host.values():
        row['cover_ids'].sort()
        row['actual_status'] = ('PRESENT' if row['cover_ids'] else
                                'ABSENT' if complete_scope and not issues else
                                'UNKNOWN_SCOPE')
    return {'host_to_covers': by_host, 'cover_to_host': reverse,
            'issues': issues, 'complete_scope': bool(complete_scope)}


def collect_host_covers(doc, hosts, cover_elements=None, references=None):
    from Autodesk.Revit import DB
    hosts = list(hosts)
    def same_document(element):
        try:
            return bool(element.Document.Equals(doc))
        except AttributeError:
            return element.Document is doc
    if any(not same_document(host) for host in hosts):
        raise ValueError("Host belongs to another document")
    complete = cover_elements is None
    if complete:
        cover_elements = list(DB.FilteredElementCollector(doc).OfClass(
            DB.InsulationLiningBase).WhereElementIsNotElementType())
    else:
        cover_elements = list(cover_elements)
    if any(not same_document(cover) for cover in cover_elements):
        raise ValueError("Cover belongs to another document")
    invalid = [cover_id(e) for e in cover_elements
               if not isinstance(e, DB.InsulationLiningBase)]
    if invalid:
        raise ValueError('Scope contains non-cover elements: %s' % invalid)
    return cover_maps(hosts, cover_elements,
                      lambda ident: doc.GetElement(DB.ElementId(ident)),
                      references, complete)
```

## Adaptation and limits

Use physical `HostElementId` as authority, not a host's insulation/lining type-name or thickness reference. Explicit partial cover scopes cannot prove absence. A failed cover resolution conservatively prevents absence claims. Does not inspect linked documents or infer covers from solids. No selection, view, pinned state, parameters or document changes.

## Verification

Executed `python scripts/test_mep_blocks.py`: 31 tests passed across the five exact Markdown implementation fences (2026-10-08, CPython 3.12). Tests cover pure algorithms and mocked API success/error/rollback; they do not establish native Revit behavior or source runtime inheritance. IronPython 2.7 syntax compatibility is intentional but not executed in this environment.

## Provenance

[CFD-modeling source](https://github.com/Krankort224/CFD-modeling/blob/6f6ff37416a4145313737cb9c23a311d3e8ebedb/tools/py/_grille_branch_pilot.py), pin `6f6ff37416a4145313737cb9c23a311d3e8ebedb`: `Executor.preflight`, insulation inventory and `HostElementId` checks. Adapted into a bidirectional read-only map; removed project IDs, EI60 assumptions and writes.

Uploaded scripts archive SHA256 `6caa68eb49c6e9cec087eb4b280336d0d8300df9635c4ad719bea1240472b20e`: graph `KOV_Сборка спецификации воздуховодов.dyn`, node `5caea6a62c774f7eae803f60686b9f19`, `get_host_of_cover`, `add_cover`, `cover_row`. Kept physical cover authority; replaced global document variables and reference-based assumptions with explicit scope and diagnostics.
