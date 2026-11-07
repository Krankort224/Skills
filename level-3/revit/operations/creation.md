# Creation

## Inputs

Use requested behavior, runtime, representative elements/data, intended scope and project conventions. Resolve unknowns that affect correctness; continue independent work while an answer is pending.

## Procedure

1. Define inputs/outputs, units, parameter scope, missing/ambiguous behavior, iteration caps and acceptance cases. For a graph, specify node IDs, input order/types and the single `OUT` payload shape.
2. Read [runtime](../references/runtime.md) and only required technical references. Locate [blocks](../assets/blocks/catalog.md); read selected complete contracts and dependencies before adapting them.
3. Build read-only discovery and a deterministic plan. Separate project bindings from generic logic. Retain identity and skip reasons; preflight prerequisites before the first write.
4. Implement the smallest coherent change. Declare transaction ownership using [transactions](../references/transactions.md), execution switch, regeneration boundaries and readback. Bound batches and record actual effects, including relevant dependent changes.
5. Inspect the resulting graph with `scripts/inspect_dyn.py`. Check wire endpoints together with the code's `IN[n]` contract: structurally valid wiring may still deliver the wrong payload.
6. Execute meaningful offline checks of critical logic and failure branches. If native access exists and execution is authorized, run a bounded case in the target profile. Verify relevant no-op, ambiguity, failure and rollback behavior.
7. Deliver implementation and evidence. Without native access, provide exact inputs, expected readback and host settings for a bounded native case.

## Result and completion

Provide code/graph, configuration, interface contract, tested examples and verification limits. Complete all checks available in the current environment and state unexecuted native requirements. Compilation or mocks alone do not prove model correctness.
