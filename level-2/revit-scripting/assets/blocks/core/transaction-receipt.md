# Native transaction with verification receipt

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
| id | transaction-receipt |
| group | core |
| status | reviewed |
| runtime | Revit 2022 / Dynamo 2.12 / IronPython 2.7; Python 3 with compatible Revit host |
| verification | offline |
| dependencies | none |
| mutation | document-write |

## Purpose

Coordinate preflight, native writes, readback verification and commit as one explicit operation. Return an honest receipt for dry runs, committed changes, rollbacks and host failures; do not use ForceCloseTransaction as a rollback mechanism.

## Inputs and outputs

`transaction_receipt(doc, name, preflight, write, verify, dry_run=True, api=None)` requires no existing external document transaction (`doc.IsModifiable` must be false). Pure `preflight(doc)` returns a dict with `ok=True` and optional planned metadata. `write(doc, plan)` executes inside a native transaction and returns a result; `verify(doc, result)` must return exactly True after readback. A dry run calls only preflight, never write or verify. Receipt contains status, committed, dry_run, plan, result, error and native start/commit/current/rollback statuses. Callback failures are reported and rollback is attempted.

## Implementation

```python
# -*- coding: utf-8 -*-
def transaction_receipt(doc, name, preflight, write, verify,
                        dry_run=True, api=None):
    if api is None:
        import Autodesk.Revit.DB as api
    receipt = {'status': 'preflight_failed', 'committed': False,
               'dry_run': bool(dry_run), 'plan': None, 'result': None,
               'error': None, 'rollback_status': None,
               'start_status': None, 'commit_status': None,
               'current_status': None}
    if doc is None or not name:
        raise ValueError('Document and transaction name required')
    if doc.IsModifiable:
        receipt.update({'status': 'external_transaction_active',
                        'error': 'Native transaction ownership unavailable'})
        return receipt
    if getattr(doc, 'IsReadOnly', False):
        receipt.update({'status': 'document_read_only',
                        'error': 'Document cannot be modified'})
        return receipt
    try:
        plan = preflight(doc)
        if not isinstance(plan, dict) or plan.get('ok') is not True:
            receipt['plan'] = plan
            receipt['error'] = 'Preflight did not return ok=True'
            return receipt
        receipt['plan'] = plan
    except Exception as error:
        receipt['error'] = str(error)
        return receipt
    if dry_run:
        receipt['status'] = 'dry_run_ready'
        return receipt
    if not callable(write) or not callable(verify):
        receipt['error'] = 'Write and verification callbacks required'
        return receipt
    transaction = None
    try:
        if doc.IsModifiable:
            raise ValueError('Preflight changed transaction ownership')
        transaction = api.Transaction(doc, name)
        start = transaction.Start()
        receipt['start_status'] = str(start)
        receipt['current_status'] = str(transaction.GetStatus())
        if start != api.TransactionStatus.Started:
            raise ValueError('Transaction did not start: %s' % start)
        options = transaction.GetFailureHandlingOptions()
        options.SetClearAfterRollback(True)
        transaction.SetFailureHandlingOptions(options)
        result = write(doc, plan)
        receipt['result'] = result
        doc.Regenerate()
        if verify(doc, result) is not True:
            raise ValueError('Readback verification failed')
        commit = transaction.Commit()
        receipt['commit_status'] = str(commit)
        current = transaction.GetStatus()
        receipt['current_status'] = str(current)
        if (commit != api.TransactionStatus.Committed or
                current != api.TransactionStatus.Committed):
            raise ValueError('Commit did not succeed: %s' % commit)
        receipt.update({'status': 'committed', 'committed': True})
    except Exception as error:
        receipt['error'] = str(error)
        if transaction is None:
            receipt['status'] = 'transaction_failed'
        else:
            try:
                current = transaction.GetStatus()
                receipt['current_status'] = str(current)
                if current == api.TransactionStatus.RolledBack:
                    rollback = current
                elif current == api.TransactionStatus.Started:
                    rollback = transaction.RollBack()
                else:
                    rollback = current
                receipt['rollback_status'] = str(rollback)
                current = transaction.GetStatus()
                receipt['current_status'] = str(current)
                if (rollback == api.TransactionStatus.RolledBack and
                        current == api.TransactionStatus.RolledBack):
                    receipt['status'] = 'rolled_back'
                else:
                    receipt['status'] = 'rollback_unconfirmed'
                    receipt['unresolved_transaction'] = transaction
                    if current == api.TransactionStatus.Pending:
                        receipt['pending_transaction'] = transaction
            except Exception as rollback_error:
                receipt['status'] = 'rollback_failed'
                receipt['rollback_status'] = str(rollback_error)
                receipt['unresolved_transaction'] = transaction
    finally:
        if transaction is not None and 'unresolved_transaction' not in receipt:
            try:
                transaction.Dispose()
            except Exception as dispose_error:
                receipt['dispose_error'] = str(dispose_error)
    return receipt
```

## Adaptation and limits

Preflight must be read-only; the wrapper cannot sandbox arbitrary callbacks. Consumers must verify actual written values and treat only `committed` as confirmed success; other statuses require inspection of native statuses before assuming rollback. A Pending native commit cannot always be synchronously rolled back: `rollback_unconfirmed` explicitly reports that host failure-processing state instead of claiming rollback. The receipt retains `pending_transaction` without RollBack or Dispose; the host owns completion and callers must stop further writes until it resolves. Compare both Commit return status and GetStatus because finalizers can change the current status. Failed or incomplete rollbacks retain `unresolved_transaction` without disposing an active or unknown native state. Result IDs from rolled-back attempts are telemetry, not surviving model elements. Native API mocks do not replace Dynamo transaction ownership checks. No `TransactionManager.ForceCloseTransaction` is used.

## Verification

Native validation pending. Offline tests cover dry run with zero write/verify calls, rejected preflight, existing external transaction, successful commit, write failure, readback failure with rollback, commit failure/automatic rollback and pending rollback-unconfirmed status, failed/unfinished rollback retention, native status capture and commit/current status disagreement. Native failure dialog, Pending lifecycle and worksharing behavior need host validation.

## Provenance

Adapted from [CFD parameter fill at 6f6ff374](https://github.com/Krankort224/CFD-modeling/blob/6f6ff37416a4145313737cb9c23a311d3e8ebedb/tools/py/20_VRU_FillParameters.py), native `Transaction.Start`/write/readback/`Commit` loop; and [Revit dimension executor at f6b4a430](https://github.com/Krankort224/Revit-automatization/blob/f6b4a4301ef70187780150acf44f6e5140a6c339/src/block_3/block_3_current.py), transaction execution loop and `validate_created_dimension`. Replaced project writes with callbacks, moved preflight before transaction, disallowed external transaction ownership and added honest failed verification/commit receipts.
