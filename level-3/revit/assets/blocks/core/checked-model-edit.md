# Проверяемая запись и откат

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

Выполняет одну операцию с дочерней транзакцией и проверкой внутри группы. При dry-run дочерняя транзакция проходит нативный commit, затем группа откатывается и вызывается отдельная сверка исходного состояния.

## Inputs and outputs

Проверенный документ, имя операции, режим, действия для записи и проверки. Передай `verifyRollback` для dry-run. `checkCancellation` проверяет сигнал отмены и выбрасывает исключение. Для длинного действия вызывай его также между элементами.

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

Перед вызовом документ должен быть доступен для записи и вне транзакции. Колбэки относятся к одному документу. Для внешних файлов, сохранения и синхронизации нужен отдельный контракт. После успешной записи выполняй независимое чтение.



The implementation requires `RvtMcp.Plugin.SafeFailuresPreprocessor`. Its recorded run covers that gateway profile. Adapt and verify failure handling before using another host. Native Pending failure processing requires the host lifecycle described in [transactions](../../../references/transactions.md); the recorded smoke cases do not establish Pending handling.

## Verification

Успешный коммит, откат dry-run, откат после сбоя проверки и отмена перед коммитом.

[Свидетельство прогона](../../../evidence/revit-2022-mcp-smoke.json)

## Provenance

Imported from the local `revit-mcp` skill on 2026-11-12, source path `assets/blocks/core/checked-model-edit.md`. Original block ID `mcp-checked-model-edit`. Original Markdown SHA-256 `9a9c655f0d5354bfee19aff1c379e7eda34c311a49f1a2adc4a1aec162c87ed4`.

The implementation fence is preserved. The recorded native [evidence](../../../evidence/revit-2022-mcp-smoke.json) identifies its source hash, host and coverage. Contract/headings were normalized for the shared library; this import performs no new native validation.
