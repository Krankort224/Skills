# Correct insulation worksets through their hosts

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
| id | insulation-workset |
| group | mep |
| status | reviewed |
| runtime | Revit 2022 / Dynamo / IronPython 2.7; Python 3 with compatible Revit host |
| verification | offline |
| dependencies | none |
| mutation | document-write |

## Purpose

Correct a mismatched insulation workset when the insulation's own workset parameter is read-only. Temporarily set the host to the insulation's current workset, regenerate the whole batch once, restore the host's original workset, then verify both after native Commit. A regeneration after creation alone did not correct this source case.

## Inputs and outputs

Pass explicit native `DuctInsulation` or `PipeInsulation` elements from one document to `plan_insulation_worksets(doc, insulations)`. Planning is read-only and preserves document, host/cover identities, original worksets, type and thickness. Duplicate cover IDs are deduplicated; different temporary worksets for one host are rejected. The plan is session-bound, not a serializable interchange format.

`stage_insulation_worksets(doc, plan, execute=False)` defaults to preview. Execution requires a caller-owned active native Transaction; it owns only a batch SubTransaction. `STAGED_PENDING_COMMIT` means hosts were restored and the SubTransaction committed, not that insulation worksets have propagated. Failure receipts require the caller's declared rollback policy; unresolved states retain the transaction handle. The helper never creates/deletes insulation, changes active worksets, finishes the outer transaction, or touches matching hosts.

Keep a caller-owned native TransactionGroup open around the outer Transaction. After stage success, Commit the Transaction and pass its actual return/current statuses to `verify_insulation_worksets`. Assimilate the group only after `VERIFIED_AFTER_COMMIT`; roll the group back on failed readback. Stop mutation on Pending/unknown statuses. Record native statuses, warnings and rollback evidence in the owning pipeline. Do not plug this sequence into a wrapper that verifies dependent worksets before outer Commit or adds another regeneration.

## Implementation

```python
def iw_api(api):
    if api is None:
        from Autodesk.Revit import DB
        from Autodesk.Revit.DB.Mechanical import DuctInsulation
        from Autodesk.Revit.DB.Plumbing import PipeInsulation
        class NativeApi(object):
            pass
        adapter = NativeApi()
        for name in ('ElementId', 'SubTransaction', 'TransactionStatus',
                     'BuiltInParameter', 'StorageType'):
            setattr(adapter, name, getattr(DB, name))
        adapter.DuctInsulation = DuctInsulation
        adapter.PipeInsulation = PipeInsulation
        return adapter
    return api


def iw_id(value):
    return int(getattr(value, 'Id', value).IntegerValue)


def iw_same_document(left, right):
    try:
        return bool(left.Equals(right))
    except AttributeError:
        return left is right


def plan_insulation_worksets(doc, insulations, api=None):
    api = iw_api(api)
    if doc is None or doc.IsFamilyDocument:
        raise ValueError('Project document required')
    rows, targets, seen = [], {}, set()
    for cover in insulations:
        if not isinstance(cover, (api.DuctInsulation, api.PipeInsulation)):
            raise ValueError('Explicit duct/pipe insulation scope required')
        if not iw_same_document(cover.Document, doc):
            raise ValueError('Insulation belongs to another document')
        ident = iw_id(cover)
        if ident in seen:
            continue
        seen.add(ident)
        host = doc.GetElement(cover.HostElementId)
        if host is None or not iw_same_document(host.Document, doc):
            raise ValueError('Insulation host unavailable or foreign')
        original, current = iw_id(host.WorksetId), iw_id(cover.WorksetId)
        row = {'insulation_id': ident, 'insulation_uid': str(cover.UniqueId),
               'host_id': iw_id(host), 'host_uid': str(host.UniqueId),
               'host_workset_id': original, 'insulation_workset_id': current,
               'type_id': iw_id(cover.GetTypeId()),
               'thickness_ft': float(cover.Thickness)}
        rows.append(row)
        if doc.IsWorkshared and current != original:
            if iw_id(host) in targets and targets[iw_id(host)]['temporary'] != current:
                raise ValueError('One host requires different temporary worksets')
            targets[iw_id(host)] = {'host_id': iw_id(host),
                                    'original': original, 'temporary': current}
    return {'_document': doc, 'rows': rows,
            'hosts': [targets[i] for i in sorted(targets)],
            'workshared': bool(doc.IsWorkshared)}


def iw_set_host(host, target, api):
    parameter = host.get_Parameter(api.BuiltInParameter.ELEM_PARTITION_PARAM)
    if (parameter is None or parameter.IsReadOnly or
            parameter.StorageType != api.StorageType.Integer):
        raise ValueError('Writable Integer host workset parameter required')
    if not parameter.Set(target) or iw_id(host.WorksetId) != target:
        raise ValueError('Host workset write/readback failed')


def stage_insulation_worksets(doc, plan, execute=False, api=None):
    api = iw_api(api)
    receipt = {'status': 'DRY_RUN', 'plan': plan,
               'outer_commit_required': False, 'start_status': None,
               'commit_status': None, 'current_status': None,
               'rollback_status': None}
    if not iw_same_document(doc, plan.get('_document')):
        raise ValueError('Plan belongs to another document')
    if not execute:
        return receipt
    covers = [doc.GetElement(api.ElementId(r['insulation_id']))
              for r in plan['rows']]
    current = plan_insulation_worksets(doc, covers, api)
    if (current['rows'] != plan['rows'] or current['hosts'] != plan['hosts'] or
            current['workshared'] != plan['workshared']):
        raise ValueError('Insulation/host identity or original state changed')
    if not plan['hosts']:
        receipt['status'] = 'NO_CHANGE'
        return receipt
    if not doc.IsModifiable or doc.IsReadOnly:
        raise ValueError('Caller-owned writable native Transaction required')
    tx = api.SubTransaction(doc)
    try:
        start = tx.Start(); receipt['start_status'] = str(start)
        if start != api.TransactionStatus.Started:
            raise ValueError('Batch SubTransaction did not start')
        for item in plan['hosts']:
            host = doc.GetElement(api.ElementId(item['host_id']))
            iw_set_host(host, item['temporary'], api)
        doc.Regenerate()
        for item in plan['hosts']:
            host = doc.GetElement(api.ElementId(item['host_id']))
            iw_set_host(host, item['original'], api)
        commit = tx.Commit(); receipt['commit_status'] = str(commit)
        state = tx.GetStatus(); receipt['current_status'] = str(state)
        if (commit != api.TransactionStatus.Committed or
                state != api.TransactionStatus.Committed):
            raise ValueError('Batch SubTransaction commit not confirmed')
        receipt.update(status='STAGED_PENDING_COMMIT', outer_commit_required=True)
    except Exception as error:
        receipt['error'] = str(error)
        try:
            state = tx.GetStatus()
            if state == api.TransactionStatus.Started:
                rollback = tx.RollBack()
                receipt['rollback_status'] = str(rollback)
                state = tx.GetStatus()
            receipt['current_status'] = str(state)
            receipt['status'] = ('ROLLED_BACK' if state == api.TransactionStatus.RolledBack
                                 else 'ROLLBACK_UNCONFIRMED')
        except Exception as cleanup_error:
            receipt.update(status='ROLLBACK_FAILED', rollback_error=str(cleanup_error))
    finally:
        try:
            state = tx.GetStatus()
            if state in (api.TransactionStatus.Uninitialized,
                         api.TransactionStatus.Committed, api.TransactionStatus.RolledBack):
                tx.Dispose()
            else:
                receipt['transaction_handle'] = tx
                receipt['owner_action_required'] = True
        except Exception as cleanup_error:
            receipt['transaction_handle'] = tx
            receipt['owner_action_required'] = True
            receipt['cleanup_error'] = str(cleanup_error)
    return receipt


def verify_insulation_worksets(doc, receipt, commit_status, current_status, api=None):
    api = iw_api(api)
    result = {'status': 'OUTER_COMMIT_UNCONFIRMED', 'ok': False, 'rows': []}
    if (receipt.get('status') != 'STAGED_PENDING_COMMIT' or doc.IsModifiable or
            commit_status != api.TransactionStatus.Committed or
            current_status != api.TransactionStatus.Committed):
        return result
    plan = receipt['plan']
    if not iw_same_document(doc, plan.get('_document')):
        result['status'] = 'DOCUMENT_MISMATCH'
        return result
    errors = []
    for expected in plan['rows']:
        row = {'insulation_id': expected['insulation_id'],
               'host_id': expected['host_id'], 'ok': False}
        try:
            cover = doc.GetElement(api.ElementId(expected['insulation_id']))
            host = doc.GetElement(api.ElementId(expected['host_id']))
            if cover is None or host is None:
                raise ValueError('Insulation or host disappeared')
            row.update(actual_host_workset_id=iw_id(host.WorksetId),
                       actual_insulation_workset_id=iw_id(cover.WorksetId))
            if (str(cover.UniqueId) != expected['insulation_uid'] or
                    str(host.UniqueId) != expected['host_uid'] or
                    iw_id(cover.HostElementId) != expected['host_id'] or
                    iw_id(cover.GetTypeId()) != expected['type_id'] or
                    abs(float(cover.Thickness)-expected['thickness_ft']) > 1e-9 or
                    iw_id(host.WorksetId) != expected['host_workset_id'] or
                    iw_id(cover.WorksetId) != expected['host_workset_id']):
                raise ValueError('Postcommit identity/type/thickness/workset mismatch')
            row['ok'] = True
        except Exception as error:
            row['error'] = str(error); errors.append(row)
        result['rows'].append(row)
    result.update(status='COMMITTED_READBACK_FAILED' if errors else 'VERIFIED_AFTER_COMMIT',
                  ok=not errors, group_rollback_required=bool(errors))
    return result
```

## Adaptation and limits

Preserve the order: create/select explicit covers, inspect actual worksets, switch only mismatched hosts, regenerate once, restore original hosts, native Commit, then verify dependent covers before group Assimilate. The host's restored parameter value does not prove the insulation has updated before outer Commit. Failure during regeneration invalidates further model inspection; use the transaction owner's native cleanup path. Do not add per-element regeneration or attempt to write a read-only insulation parameter.

This changes hosts temporarily and may refresh other dependents on those hosts. Inventory/check them in the owning pipeline when their original state must be preserved; the helper cannot establish unchanged connectivity, geometry, other covers or warning history. Resolve worksharing/host editability and group constraints for the actual model. The batch is atomic at its SubTransaction; the caller decides whether to abort the outer operation or remove its newly created covers after a confirmed rollback. Pipe insulation is supported by the original DLL scope and this API adapter, but has no native validation here. No linked documents, lining, orphan cleanup, system-name rules, family names, type selection or log paths are inherited from the source.

## Verification

The generalized fence has offline verification only. On 2026-10-13, `python scripts/test_insulation_workset.py` passed 22 [targeted tests](../../../scripts/test_insulation_workset.py); full skill discovery passed 93 tests. Tests execute the fence directly with mock native transactions, including the default Mechanical/Plumbing namespace adapter, mismatch-only writes, multiple hosts with one regeneration, original-host restoration, matching covers without writes, readonly/rejected setters, stale/foreign plans, outer-commit gating, postcommit propagation failure, rollback failures and unchanged type/thickness/identity. Library validation and Python 2 grammar checks passed; IronPython and the exact extracted helper still require native execution.

The source integration `Insulate_DP_DV_VZ_v3` ran in Revit 2022 on 2026-10-13. [Native log](https://chatgpt.com/api/library/files/libfile_187d6a80643c81918f7e5d47903f41de/download), filename `Insulate_DP_DV_VZ_20261013_183159_622000.txt`, SHA256 `1369bb84ede56ee2421b184ba14fbf8084101a74c12cddfc4ca08124b58985f8`: 1292 duct-insulation worksets corrected, all hosts restored and all covers read back after `Committed / Committed`; 1052 and 240 hosts in two different original worksets. Thirteen tap-attachment warnings were recorded; connectivity was not verified. The script targets Dynamo/IronPython 2.7, but the log does not record the engine or Dynamo version. This validates the integrated batch mechanism in that profile, not every generalized adapter/pipe/failure path.

## Provenance

[Uploaded FixInsulationCommand.zip](https://chatgpt.com/api/library/files/libfile_ace437b822c88191b4f16b133b624360/download), SHA256 `8d4f6a784feb6b3af869058880f9077c8df4f6d2bc6986f31dc9bf55bd9a91ee`: `Plugins.UtilsHKLS.dll`, versions 1.0.0.0 and 1.0.0.1, `Plugins._Template.FixInsulationCommand.Execute`. Both method bodies have the same IL sequence: host Set to cover workset, Regenerate, host Set to original. DLL references are RevitAPI/RevitAPIUI 22.0.0.0. Removed full-model collectors, orphan deletion, per-cover regeneration and unchecked setters/commit.

[Integrated Python source](https://chatgpt.com/api/library/files/libfile_cb09506b2c3881919fe41846b24429eb/download), Library version 2, SHA256 `fc1335d8ef872eb34b756e34d64a43adc30592df70085554a820ab2a681573af`: `Insulate_DP_DV_VZ.py`, `check_created_batch`, `set_host_workset`, postcommit `verify_insulation`. Extracted the correction only; replaced creation/log schemas with explicit session-bound plans, a caller-owned outer transaction contract, batch SubTransaction and independent postcommit readback. Keep complete sources/logs with their owners; the links/hashes above identify evidence rather than duplicate it.
