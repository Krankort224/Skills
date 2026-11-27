# MCP session operations

## Target document and execution

- For a live session, list available processes with `revit_list_available_targets` and check the connection with `revit_health`. Pin the intended process and document. Before a write, use `revit_switch_target` with `verify=true` and provide `expectedDocumentId` when known. In the script, recheck the document identifiers required by the project. Account for in-flight calls when switching the connection.
- Use a typed tool when its actual contract covers the operation and required postconditions. Read the contract of any baked tool. Run custom C# through `revit_send_code_to_revit` in a supported API context. Check the script format, imports and dependencies supported by the current tool.
- Check each tool's units. Typed MCP commands may take dimensions in millimeters, while direct Revit API calls use internal units.
- `revit_batch_execute` groups compatible built-in commands. Invoke C# and baked tools separately. Check the failure policy, including `continueOnError`, before relying on atomic execution. Track file side effects separately from document Undo.
- For C#, use the failure handling supported by the current gateway. The imported block depends on `RvtMcp.Plugin.SafeFailuresPreprocessor`. Check native statuses and profile restrictions against the [transaction guidance](transactions.md).
- GUI actions require the applicable user authorization. Commit, save and synchronization each have their own outcomes.

## Invocation boundaries

Group work by operation kind, dependencies and volume. Define the input IDs, action, scope and observable result for each batch. Run each independent batch in a separate invocation that completes its transaction. When control returns, verify the outcome and read the current inputs for the next batch separately.

Successive transactions inside a synchronous C# call can keep Revit busy until the whole script returns. A transaction defines the commit and rollback boundary. An invocation returns control to the host so the caller can verify state before proceeding. End the invocation between independent batches. Keep coupled actions that must succeed or roll back together, such as disconnecting, replacing and reconnecting one component, in one atomic transaction scope.

### Operation types

For other operation types, establish dependencies, impact and verification using the same principles.

| Operation | Boundary and verification |
| --- | --- |
| Load a family or types, including types from a catalog | Use a separate call. After commit, reread the family, types and parameters. Check affected embedded lookup tables and existing instances. |
| Create or duplicate types in a project | Use a call separate from loading and assignment. Confirm new IDs, parameters and effects on existing types. |
| Assign types to instances | Use previously verified types. Group compatible instances that need the same action. Group connector-based categories by size. |
| Change instance or type parameters | Bound the scope of each write. For type parameters, account for all affected instances and dependent values. |
| Create elements or modify geometry and connections | Identify independent components. Keep changes to each connected component atomic and verify its connections to surrounding elements. |
| Create or change parameter bindings | Prepare and verify definitions and bindings before populating values in a separate call. |
| Delete elements or types freed by reassignment | Check usage and dependencies after reassignment. Compare the actual deletion set with the authorized scope in a transaction that can be rolled back. |
| Edit views, sheets, annotations, links or worksets | Separate independent documents, operations and areas of impact. Account for dependents and the cost of updating them. |

Transfers between documents, exports, saves, synchronization and changes to external files each have their own boundaries and receipts. Verify file effects independently of document Undo. See [parameters and units](parameters-and-units.md#shared-parameters-and-definition-files) for shared parameter definitions and files.

### Batch sizing and recovery

For a large operation, test a representative component and a small batch in the current model configuration. A successful pilot can count toward the deliverable. Consider instance counts, shared types, dependencies, loaded links, available memory and Revit responsiveness. Measure execution, regeneration and commit time. Use those measurements to size subsequent batches and reduce their size when costs grow. Set the limit for the current model.

Split a size group into multiple calls as needed while keeping connected components intact. Return a short receipt after each batch with IDs, counts of changed and skipped elements, duration, commit or rollback status and verification results. Check affected elements and their dependents after each batch, then reconcile the full result at the end.

On failure, apply the planned batch rollback and end the call with diagnostics. Confirm recovery with a separate read, then prepare a smaller batch or a corrected plan for a new call. Move recursive splitting, retry attempts and alternative fixes into subsequent calls so their duration and intermediate results remain visible. Carry verified batches forward when resuming.

For a significant delay, report the start time, elapsed time and last verified step. Use the operation status table below while the call is unresolved. If it finishes with a partial or indeterminate outcome, reread the model to establish which changes took effect and which are still outstanding.

## Family reload

Before loading, capture simple data with the exact family name and category, its types and parameters, instance assignments, IDs and `UniqueId` values, geometry and physical connections of the affected instances. Record expected changes and the value preservation policy for `IFamilyLoadOptions`. Choose the `LoadFamily` overload and transaction owner for the target API version. Use the [lookup table guidance](lookup-tables.md) for embedded tables.

Loading can invalidate the previous `Family` object and change its ID. Save identifiers and values before the call and reacquire objects from the document afterward. If the ID changes, find a unique candidate by exact name and category, then check it against the original types and instances. Diagnose ambiguous matches. Require the full match before accepting the reload.

Verify type IDs separately from the family ID, along with instance type assignments, instance `UniqueId` values, parameter values and connector pairs. Compare every identity change with the allowed effects of the operation. On verification failure, apply the planned rollback and check its status. After an error or partial result, reread the document independently to establish what applied and what was restored before choosing a retry or recovery. Record both the native receipt and the model readback.

In a Revit 2022.1 / rvt-mcp 1.2.1 field case on 2026-11-13, reloading changed the family ID and preserved the type and instance IDs, `UniqueId` values, assignments, parameter values and physical connections. Verification by the original ID failed and the gateway returned a partial result. A subsequent read confirmed the new tables and expected calculated values in the model. Why the changes persisted through that error path remains unknown. This case supports verifying actual model state. Its rollback behavior is specific to the observed run.

## In-flight operations

| Signal | Action |
| --- | --- |
| `timed_out_running` | Keep the `operationId`, check `revit_get_operation_status` and wait for the submitted call before the next write. |
| `waiting_for_user` | Report the exact Revit prompt and proceed within current authorization. |
| `completed` with an indeterminate outcome | Check the native receipt and reread the document before deciding whether to retry. |
| Operation record unavailable | Execution state remains unknown. Reconcile available receipts with model state before attempting a retry. |
| Stop requested | Stop submitting new work, send the supported cancellation signal and verify that execution ended and rollback took effect. |

In a long C# call, check cancellation between elements, before a native commit and before assimilating the transaction group. Pass the cancellation check into composed blocks. A native call may be slow to return. Report when it can stop based on the actual execution stage.
