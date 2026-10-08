# Dynamo contracts

## Inspection

Run `scripts/inspect_dyn.py` on a graph or ZIP. It distinguishes Python from DesignScript CodeBlock nodes and reports versions/engines, node/port identities, connectors, unconnected ports and bad/multiple wires. A clean structural report does not establish payload compatibility.

Use `--code NODE_ID` for relevant Python and `--extract DIR` for explicit extraction. Embedded code never executes. Preserve the immutable source. Extraction rejects unsafe ZIP paths and separates colliding filenames.

## Ports and payloads

A Dynamo Python node has one output port carrying `OUT`. `OUT[4]` in a schema identifies a list member, not a fifth graph port. The inspector resolves native port-ID and legacy node-ID/index endpoints; compare them with actual `IN[n]` usage.

Specify input index, type, rank/cardinality, units and execution polarity. `execute=True` and `dry_run=True` request opposite behavior; do not infer polarity from a node label.

Use named fields/table headers. [table-payload](../assets/blocks/core/table-payload.md) validates a table or `[report, table]` against required columns; do not opportunistically accept a nested list.

For multi-node pipelines, publish a schema/version marker and producer-to-consumer field map. Check required fields before calculation/writes. Keep intentional legacy compatibility in one adapter; reject other shapes rather than guessing indices.

## Diagnostic evidence

Record graph revision, node ID/engine, producer/consumer port identities, raw shape and first failing field. CodeBlock expressions may wrap lists, change rank or units; inspect those producers too. Display names and canvas placement are navigation aids.

When editing embedded code, preserve IDs, relevant port/view metadata and unrelated graph state. Reinspect the final graph and compare requested nodes/wires. Graph execution may trigger other active write nodes, even if the edited helper is read-only.

## Example

The synthetic [graph](../assets/examples/graph-contract.dyn) and [expected JSON](../assets/examples/graph-contract.expected.json) illustrate offline wiring inspection and one structured Python output. They contain no native execution evidence.
