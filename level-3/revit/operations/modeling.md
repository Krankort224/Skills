# Modeling and inspection

## Establish the result

Identify the target document, requested observations or changes, element/view scope and acceptance criteria. Take dimensions, flows, names and tolerances from project sources. Use complementary domain expertise when the engineering decision requires it. Select the available [execution route](../references/execution.md).

Read-only inspection returns bounded observations, element identities and unresolved cases. It can finish at that point. A rollback probe invokes real writes and belongs to an authorized mutation scope.

## Discover and plan

For an inspection request, collect only the observations needed for the answer and report their scope. The change-plan steps below apply when model edits are requested.

1. Resolve inputs in their owning document. Inspect types, levels, parameter bindings, geometry and editability/worksharing state. Preserve ambiguity and exclusions. Changing a type can affect instances beyond the selection; inventory those effects before choosing an instance edit, a shared type edit or a separate type.
2. Form a deterministic plan containing affected IDs, operations, boundary conditions, units, tolerances and expected readback. For MEP use actual connector geometry after regeneration and preserve rectangular width/height order. Follow [parameters](../references/parameters-and-units.md) and [connection boundaries](../references/geometry-and-connectors.md#edit-boundaries).
3. Select useful [blocks](../assets/blocks/catalog.md) by contract, language, runtime and evidence. Read their declared dependencies. Declare the transaction owner and any host adapter. For elbows and transitions, inspect the selected type's routing preferences and verify the geometry actually produced by Revit. Loaded family/type assignment and type-catalog loading have distinct preconditions and effects; verify newly loaded types before installation.
4. Compare the plan with fresh model state immediately before writing. Replan changed inputs and resolve outstanding operations before dispatching another mutation. MCP-specific call boundaries and receipts belong to [MCP operations](../references/mcp-operations.md).

For embedded lookup-table changes, follow [lookup tables](../references/lookup-tables.md) to export the loaded data, establish complete configuration keys and validate calculated values. Before a family reload, define its [identity and readback checks](../references/mcp-operations.md#перезагрузка-семейства).

## Apply and verify

Use [transactions](../references/transactions.md) to keep coupled edits and their checks within a rollback-capable boundary. For a rollback probe, verify actual postconditions and restoration of the starting state. Apply the same plan after rechecking its prerequisites.

Reacquire affected elements and connectors after regeneration or replacement. Check types, sections, levels, physical connector pairs, system membership and preserved external connections. Compare intended terminal flow values separately from calculated `Connector.Flow`. Include dependent annotations, insulation and unexpected additions/deletions when relevant to the affected scope.

For example, replacing a duct segment with two branches requires fixed boundary joints, new segment axes, sections, types and fittings in the plan. Verification covers both continuous branch paths, distant unaffected segments and specified flows.

After commit, read the target model independently of the write result. Report requested and actual effects, exceptions, native statuses, readback and unresolved outcomes. Keep commit, file save and synchronization statuses distinct and use existing project locations for operational logs.
