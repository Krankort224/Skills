# Parameters and units

## Identity and scope

Use built-in identifiers for built-in semantics, GUIDs for shared bindings, or exact configured names for custom bindings. Reject duplicate name matches. Localized built-in display names are not stable identifiers.

Declare instance/type scope. Resolve type identity deliberately; type writes may affect all its instances and belong in mutation scope. Avoid implicit instance-to-type fallback.

Use [element-identity](../assets/blocks/core/element-identity.md) and [parameter-access](../assets/blocks/core/parameter-access.md). A familiar family-name substring does not establish parameter behavior; require known project mappings.

## Representation and quantity

StorageType is separate from quantity/specification. A Double can be length, flow, angle, area or dimensionless. Record the specification and external/internal units.

Use target-version conversion APIs; reject unavailable/failed conversions rather than returning the original input. Define tolerances in the comparison unit.

Compute with typed access. AsValueString is for presentation; SetValueString needs an explicit host locale/format contract. Parse external numbers with declared decimal/thousands conventions and reject ambiguity.

ElementId parameters can contain sentinels/references. Resolve semantics and owning document rather than treating them as ordinary integer quantities.

## Writing

Check binding, scope, storage/specification, writability and transaction mode. Distinguish unchanged/changed/absent/unsupported/failed. Verify using typed readback and tolerance; propagate failed verification to the transaction owner.

For coupled family parameters, verify resulting geometry/connectors. Do not identify an unknown binding by a coincidentally equal current value. Keep parameter maps, names and supported family behavior in project configuration.
