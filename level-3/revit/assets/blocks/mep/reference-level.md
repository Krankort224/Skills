# Change reference level while preserving absolute height

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
| id | reference-level |
| group | mep |
| status | reviewed |
| runtime | Revit 2022 / Dynamo 2.12 / IronPython 2.7; pure helpers Python 2.7 or 3 |
| verification | offline |
| dependencies | none |
| mutation | document-write |

## Purpose

Plan a reference-level change from absolute insertion height. Optionally execute one element atomically, rejecting changed height, level, identity or pinned state.

## Inputs and outputs

`plan_reference_level` takes an element, explicit levels and a caller-supplied `compatible(element)` predicate for an already-tested family/host combination. Levels are sorted by actual `Elevation`; select highest level at or below Z, clamping below lowest. Output is READY/NO_CHANGE/SKIP with original XYZ, old/new IDs and new internal-foot offset. Plans retain a native document handle and ProjectInformation UID: they are session-bound, not JSON artifacts. Different documents and foreign level scopes are rejected. `execute_reference_level` defaults `execute=False`; a write requires the caller's existing active Transaction. Native SubTransaction attempts per-element rollback on failed checks and reports whether restoration is confirmed; caller controls unresolved transaction states and outer commit/Undo. Optional `api` enables offline mocks only.

## Implementation

```python
import math


def level_id(value):
    value = getattr(value, 'Id', value)
    return int(getattr(value, 'IntegerValue', value))


def choose_reference_level(z_ft, levels):
    z_ft = float(z_ft)
    if math.isnan(z_ft) or math.isinf(z_ft):
        raise ValueError('Nonfinite absolute elevation')
    rows = sorted([(float(level.Elevation), level_id(level), level)
                   for level in levels], key=lambda row: (row[0], row[1]))
    if not rows or any(math.isnan(r[0]) or math.isinf(r[0]) for r in rows):
        raise ValueError('Explicit finite levels required')
    if len(set(r[0] for r in rows)) != len(rows):
        raise ValueError('Coincident levels require caller disambiguation')
    selected = rows[0]
    for row in rows:
        if row[0] <= z_ft:
            selected = row
    return selected[2], z_ft - selected[0]


def reference_api(api):
    if api is None:
        from Autodesk.Revit import DB
        return DB
    return api


def reference_parameters(element, api):
    level = element.get_Parameter(api.BuiltInParameter.FAMILY_LEVEL_PARAM)
    offset = element.get_Parameter(api.BuiltInParameter.INSTANCE_ELEVATION_PARAM)
    if (level is None or offset is None or level.IsReadOnly or offset.IsReadOnly or
            str(level.StorageType) != 'ElementId' or str(offset.StorageType) != 'Double'):
        raise ValueError('Writable level ElementId and offset Double required')
    return level, offset


def reference_xyz(element):
    point = element.Location.Point
    values = [float(point.X), float(point.Y), float(point.Z)]
    if any(math.isnan(v) or math.isinf(v) for v in values):
        raise ValueError('Nonfinite insertion point')
    return values


def reference_same_document(left, right):
    try:
        return bool(left.Equals(right))
    except AttributeError:
        return left is right


def plan_reference_level(element, levels, compatible, api=None):
    api = reference_api(api)
    try:
        if not isinstance(element, api.FamilyInstance) or not compatible(element):
            return {'status': 'SKIP_INCOMPATIBLE'}
        if element.Pinned:
            return {'status': 'SKIP_PINNED'}
        if level_id(element.GroupId) != -1:
            return {'status': 'SKIP_GROUPED'}
        document = element.Document
        levels = list(levels)
        if any(not reference_same_document(level.Document, document) for level in levels):
            raise ValueError("Level belongs to another document")
        xyz = reference_xyz(element)
        level_param, offset_param = reference_parameters(element, api)
        current = level_id(level_param.AsElementId())
        target, offset = choose_reference_level(xyz[2], list(levels))
        return {'status': 'NO_CHANGE' if current == level_id(target) else 'READY',
                '_document': document,
                'document_uid': str(document.ProjectInformation.UniqueId),
                'element_id': level_id(element), 'unique_id': str(element.UniqueId),
                'old_level_id': current, 'new_level_id': level_id(target),
                'new_level_elevation_ft': float(target.Elevation),
                'original_xyz_ft': xyz, 'new_offset_ft': offset}
    except Exception as error:
        return {'status': 'SKIP_ERROR', 'error': str(error)}


def execute_reference_level(doc, plan, compatible, execute=False,
                            tolerance_mm=0.1, api=None):
    if not execute:
        return {'status': 'DRY_RUN', 'plan': plan}
    if plan.get('status') != 'READY':
        return {'status': 'SKIPPED', 'reason': plan.get('status')}
    if tolerance_mm < 0 or math.isnan(tolerance_mm) or math.isinf(tolerance_mm):
        raise ValueError('Invalid height tolerance')
    if not doc.IsModifiable:
        raise ValueError('Caller must own an active native Transaction')
    if (not reference_same_document(doc, plan.get('_document')) or
            str(doc.ProjectInformation.UniqueId) != plan.get('document_uid')):
        return {'status': 'DOCUMENT_MISMATCH'}
    api = reference_api(api)
    tx = api.SubTransaction(doc)
    receipt = {'start_status': None, 'commit_status': None,
               'current_status': None, 'rollback_status': None}

    def current_status():
        try:
            state = tx.GetStatus()
            receipt['current_status'] = str(state)
            return state
        except Exception as error:
            receipt['status_query_error'] = str(error)
            receipt['current_status'] = None
            return None

    try:
        start = tx.Start(); receipt['start_status'] = str(start)
        if start != api.TransactionStatus.Started or current_status() != api.TransactionStatus.Started:
            raise ValueError('SubTransaction did not start')
        element = doc.GetElement(api.ElementId(plan['element_id']))
        if element is None or str(element.UniqueId) != plan['unique_id']:
            raise ValueError('Element identity changed')
        if not isinstance(element, api.FamilyInstance) or not compatible(element):
            raise ValueError('Family/host compatibility changed')
        if element.Pinned or level_id(element.GroupId) != -1:
            raise ValueError('Element became pinned/grouped')
        if abs(reference_xyz(element)[2]-plan['original_xyz_ft'][2])*304.8 > tolerance_mm:
            raise ValueError('Original absolute Z changed before write')
        level, offset = reference_parameters(element, api)
        if level_id(level.AsElementId()) != plan['old_level_id']:
            raise ValueError('Original level changed before write')
        target = doc.GetElement(api.ElementId(plan['new_level_id']))
        if target is None or not isinstance(target, api.Level):
            raise ValueError('Target level unavailable')
        if abs(float(target.Elevation)-plan['new_level_elevation_ft'])*304.8 > tolerance_mm:
            raise ValueError('Target elevation changed')
        if not level.Set(target.Id):
            raise ValueError('Level Set rejected')
        if not offset.Set(plan['original_xyz_ft'][2]-float(target.Elevation)):
            raise ValueError('Offset Set rejected')
        doc.Regenerate()
        element = doc.GetElement(api.ElementId(plan['element_id']))
        level, offset = reference_parameters(element, api)
        if (str(element.UniqueId) != plan['unique_id'] or
                level_id(level.AsElementId()) != plan['new_level_id'] or
                abs(reference_xyz(element)[2]-plan['original_xyz_ft'][2])*304.8 > tolerance_mm or
                element.Pinned):
            raise ValueError('Postwrite identity/level/Z/state verification failed')
        commit = tx.Commit(); receipt['commit_status'] = str(commit)
        state = current_status()
        if commit == api.TransactionStatus.Pending or state == api.TransactionStatus.Pending:
            receipt['status'] = 'TRANSACTION_PENDING'
        elif commit == api.TransactionStatus.Committed and state == api.TransactionStatus.Committed:
            receipt.update(status='STAGED_VERIFIED', element_id=plan['element_id'],
                           outer_commit_required=True)
        else:
            raise ValueError('SubTransaction commit not confirmed')
    except Exception as error:
        receipt['error'] = str(error)
        state = current_status()
        if state == api.TransactionStatus.RolledBack:
            receipt['status'] = 'ROLLED_BACK'
        elif state == api.TransactionStatus.Pending:
            receipt['status'] = 'TRANSACTION_PENDING'
        elif state == api.TransactionStatus.Started:
            try:
                rollback = tx.RollBack(); receipt['rollback_status'] = str(rollback)
                state = current_status()
                receipt['status'] = ('ROLLED_BACK' if state == api.TransactionStatus.RolledBack
                                     else 'ROLLBACK_UNCONFIRMED')
            except Exception as rollback_error:
                receipt['rollback_error'] = str(rollback_error)
                current_status()
                receipt['status'] = 'ROLLBACK_FAILED'
        else:
            receipt['status'] = ('ROLLBACK_UNCONFIRMED' if state is None else
                                 'TRANSACTION_FAILED')
    state = current_status()
    if state in (api.TransactionStatus.Committed, api.TransactionStatus.RolledBack,
                  api.TransactionStatus.Uninitialized):
        try:
            tx.Dispose(); receipt['disposed'] = True
        except Exception as error:
            receipt['dispose_error'] = str(error)
    else:
        receipt['transaction_handle'] = tx
        receipt['owner_action_required'] = True
    return receipt
```

## Adaptation and limits

The compatibility predicate is mandatory and must establish that this family's actual host/placement supports both writable parameters; parameter availability alone is insufficient. Do not use for face/work-plane/two-level families, curves, linked elements or families where changing the reference rehosts geometry without a tested adapter. Do not unpin. Caller handles worksharing preflight and outer transaction failures. Receipts retain native start/commit/current/rollback statuses. Only confirmed RolledBack state permits ROLLED_BACK. Pending, active or unknown states retain `transaction_handle` without disposal; the owner must resolve them before further document access. ROLLBACK_FAILED and ROLLBACK_UNCONFIRMED never imply restored state. `STAGED_VERIFIED` is not a committed-document receipt; recheck after outer commit. Absolute Z is measured from Location.Point, not merely reconstructed from the parameters being changed. No numbered level-name prefixes or project elevation constants. Selection/view state is untouched.

## Verification

Executed `python scripts/test_mep_blocks.py`: 31 tests passed across the five exact Markdown implementation fences (2026-10-08, CPython 3.12). Tests cover pure algorithms and mocked API success/error/rollback; they do not establish native Revit behavior or source runtime inheritance. IronPython 2.7 syntax compatibility is intentional but not executed in this environment.

## Provenance

[CFD-modeling level lookup](https://github.com/Krankort224/CFD-modeling/blob/6f6ff37416a4145313737cb9c23a311d3e8ebedb/tools/py/10_VRU_Place.py), pin `6f6ff37416a4145313737cb9c23a311d3e8ebedb`: `choose_level_for_z`, `get_location_point`, `move_location_to`; native transaction/readback principle in `20_VRU_FillParameters.py`. Reimplemented reference-level planning/execution, removing project-level names and imposing per-element rollback. This is new adaptation code, not a claim that those source functions perform reference-level changes.

Uploaded scripts archive SHA256 `6caa68eb49c6e9cec087eb4b280336d0d8300df9635c4ad719bea1240472b20e`: graph `KOV_Назначение референсных уровней.dyn`, node `73de7a14eb344cbf89ecad16b6c12c8b`, `get_level_parameter`, `get_offset_parameter`, `get_absolute_z`, `choose_target_level`. Retained absolute-Z/offset principle; removed numbered level prefixes, added explicit compatible-host predicate, stale-plan checks and native per-element rollback.
