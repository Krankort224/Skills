# Verified model edits and rollback

[Contract](#contract) · [Purpose](#purpose) · [Inputs and outputs](#inputs-and-outputs) · [Implementation](#implementation) · [Adaptation and limits](#adaptation-and-limits) · [Verification](#verification) · [Provenance](#provenance)

## Contract

| Field | Value |
| --- | --- |
| id | checked-model-edit |
| group | core |
| status | reviewed |
| language | csharp |
| runtime | Revit 2022.1 / rvt-mcp / C# |
| verification | runtime |
| dependencies | none |
| mutation | document-write |

## Purpose

Runs one operation in a child transaction and verifies it inside a transaction group. In a dry run, the child transaction commits natively, then the group rolls back and a separate check verifies the original state.

## Inputs and outputs

Supply a verified document, operation name, mode, and callbacks for writing and verification. Pass `verifyRollback` for a dry run. `checkCancellation` checks the cancellation signal and throws an exception when cancellation is requested. In a long operation, call it between elements as well.

## Implementation

```csharp
public sealed class ModelEditReceipt
{
    public readonly bool DryRun;
    public readonly TransactionStatus Transaction;
    public readonly TransactionStatus Group;

    public ModelEditReceipt(bool dryRun, TransactionStatus transaction, TransactionStatus group)
    {
        DryRun = dryRun;
        Transaction = transaction;
        Group = group;
    }
}

public static class CheckedModelEdit
{
    public static ModelEditReceipt Run(
        Document doc,
        string label,
        bool dryRun,
        Action mutate,
        Action verify,
        Action verifyRollback,
        Action checkCancellation)
    {
        if (doc == null || doc.IsReadOnly || doc.IsModifiable)
            throw new InvalidOperationException("A writable document outside a transaction is required.");
        if (string.IsNullOrWhiteSpace(label) || mutate == null || verify == null)
            throw new ArgumentException("A label, mutation and post-commit verification are required.");
        if (dryRun && verifyRollback == null)
            throw new ArgumentException("Provide a rollback readback for the dry run.");

        checkCancellation?.Invoke();
        using (var group = new TransactionGroup(doc, label))
        using (var transaction = new Transaction(doc, label))
        {
            Require(group.Start(), TransactionStatus.Started, "start transaction group");
            try
            {
                Require(transaction.Start(), TransactionStatus.Started, "start transaction");
                var options = transaction.GetFailureHandlingOptions();
                options.SetFailuresPreprocessor(new RvtMcp.Plugin.SafeFailuresPreprocessor());
                options.SetClearAfterRollback(true);
                transaction.SetFailureHandlingOptions(options);

                mutate();
                checkCancellation?.Invoke();
                var nativeStatus = transaction.Commit();
                Require(nativeStatus, TransactionStatus.Committed, "commit child transaction");

                verify();
                checkCancellation?.Invoke();
                var groupStatus = dryRun ? group.RollBack() : group.Assimilate();
                Require(groupStatus, dryRun ? TransactionStatus.RolledBack : TransactionStatus.Committed,
                    dryRun ? "roll back dry run" : "commit verified group");
                if (dryRun)
                    verifyRollback();
                return new ModelEditReceipt(dryRun, nativeStatus, groupStatus);
            }
            catch
            {
                if (transaction.GetStatus() == TransactionStatus.Started)
                    Require(transaction.RollBack(), TransactionStatus.RolledBack, "roll back child transaction");
                if (group.GetStatus() == TransactionStatus.Started)
                    Require(group.RollBack(), TransactionStatus.RolledBack, "roll back group");
                throw;
            }
        }
    }

    private static void Require(TransactionStatus actual, TransactionStatus expected, string operation)
    {
        if (actual != expected)
            throw new InvalidOperationException(operation + " returned " + actual + " instead of " + expected + ".");
    }
}
```

## Adaptation and limits

Call with a writable document outside an open transaction. Keep all callbacks scoped to that document. External files, saving and synchronization require separate contracts. Read the document independently after a successful write.



The implementation requires `RvtMcp.Plugin.SafeFailuresPreprocessor`. Its recorded run covers that gateway profile. Adapt and verify failure handling before using another host. Native Pending failure processing requires the host lifecycle described in [transactions](../../../references/transactions.md); the recorded smoke cases do not establish Pending handling.

## Verification

The native run verified a successful commit, dry-run rollback, rollback after a failed check and cancellation before commit.

[Native run evidence](../../../evidence/revit-2022-mcp-smoke.json)

## Provenance

Imported from the local `revit-mcp` skill on 2026-11-12, source path `assets/blocks/core/checked-model-edit.md`. Original block ID `mcp-checked-model-edit`. Original Markdown SHA-256 `9a9c655f0d5354bfee19aff1c379e7eda34c311a49f1a2adc4a1aec162c87ed4`.

The implementation fence is preserved. The recorded native [evidence](../../../evidence/revit-2022-mcp-smoke.json) identifies its source hash, host and coverage. Contract/headings were normalized for the shared library; this import performs no new native validation.
