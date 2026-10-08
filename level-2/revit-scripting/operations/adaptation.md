# Adaptation

## Inputs

Use the authoritative script/graph revision, requested change, runtime and representative input/output or log. Preserve immutable examples; edit the intended project copy.

## Procedure

1. Identify entry point, collaborators, schemas and transaction owner. Inspect graph wiring and embedded code. Establish requested behavior and interfaces callers rely on.
2. Capture the smallest baseline distinguishing current from requested behavior. Read the relevant [error pattern](../references/error-patterns.md) if a failure motivates the patch.
3. Locate [blocks](../assets/blocks/catalog.md) and read complete selected contracts. Check runtime, scopes, conversions and exceptions before replacement; a generalized helper is not automatically a drop-in substitute.
4. Patch the owning layer. Update affected consumers for an agreed schema change; otherwise preserve the interface. Synchronize schema/version markers and use an explicit legacy adapter rather than guessed indices or parameter scopes.
5. Check new behavior and affected baseline/failure cases. Inspect changed wires and payload types. For writes, verify values, geometry or connectivity in the declared native transaction and roll back failed verification.
6. Compare actual effects with requested scope. Record cascades, fallbacks and skipped items; distinguish partial success from a completed batch. Apply [transaction](../references/transactions.md) cleanup and evidence rules.

## Result and completion

Deliver a bounded patch, interface/configuration changes, before/after example and checks performed. Verify the requested behavior and affected compatibility cases to the available evidence level; state remaining native checks.
