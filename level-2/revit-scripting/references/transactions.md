# Transactions and receipts

## One owner

| Mode | Boundary |
| --- | --- |
| Native Transaction | No active transaction; helper owns start/commit/rollback |
| Caller-owned native/Dynamo transaction | Helper requires it and must not finish it |
| Native SubTransaction | Bounded isolation within an active transaction; commit remains provisional |
| TransactionGroup | Group of completed native transactions; rollback can undo them |

Declare mode at entry. `doc.IsModifiable` is a prerequisite signal, not permission to close another owner's transaction. Dynamo TransactionManager differs from native Transaction. `ForceCloseTransaction` is not a general rollback primitive and must not dispose of unrelated work.

[transaction-receipt](../assets/blocks/core/transaction-receipt.md) requires genuine native ownership. [reference-level](../assets/blocks/mep/reference-level.md) requires its caller-owned transaction contract.

## Preview and rollback probes

A read-only plan uses no setters, deletion or creation. A rollback probe really mutates and attempts rollback: label it separately, use authorized execution scope and inspect cleanup. Do not call it read-only.

Preflight identity, document/host, bindings, constraints and effects. Track requested/changed/unchanged/skipped/failed separately. Where changes cascade, compare actual effects with allowed scope before completing the transaction.

## Readback and statuses

Reacquire changed elements and verify values/geometry/connectivity against explicit tolerances. Setter success is insufficient. Regenerate at declared boundaries needed for readback/subsequent geometry; avoid unconditional per-item regeneration. A regeneration failure invalidates further model inspection in that attempt and requires the owner's failure path.

Inspect Start, Commit, RollBack and current status. Non-Committed returns do not prove a write. Pending means failure processing is unfinished: suspend further mutation/transactions and preserve the unresolved status for the host's supported lifecycle. Do not force rollback/disposal to bypass Pending. Commit-return and current status may differ with a finalizer.

Failed verification follows the declared rollback policy. Preserve original and cleanup failures. Do not report rolled back if rollback failed/remains pending. A committed SubTransaction still needs outer commit evidence.

## Receipt

Record mode, document/scope, preflight, requested/actual effects, native statuses, readback/tolerances, skips/failures and unresolved cleanup. Record fallback/warnings only when observed.

## Primary evidence

[Transactions](https://help.autodesk.com/cloudhelp/2024/ENU/Revit-API/files/Revit_API_Developers_Guide/Basic_Interaction_with_Revit_Elements/Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Transactions_html.html), [Transaction.Commit](https://help.autodesk.com/cloudhelp/2026/ENU/Revit-API-MainReference/files/html/32714010-7138-f64f-8fde-a310354448e3.htm) and [SubTransaction.Commit](https://help.autodesk.com/cloudhelp/2026/ENU/Revit-API-MainReference/files/html/65a0359a-ef13-e7aa-7d5c-7470fe177848.htm) describe ownership, Pending and outer commitment. Confirm members in the target assembly; these pages are not native verification of our blocks.
