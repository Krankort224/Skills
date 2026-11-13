# Parameters and units

## Identity and scope

Use built-in identifiers for built-in semantics, GUIDs for shared bindings, or exact configured names for custom bindings. Reject duplicate name matches. Localized built-in display names are not stable identifiers.

Declare instance/type scope. Resolve type identity deliberately; type writes may affect all its instances and belong in mutation scope. Avoid implicit instance-to-type fallback.

Use [element-identity](../assets/blocks/core/element-identity.md) and [parameter-access](../assets/blocks/core/parameter-access.md). A familiar family-name substring does not establish parameter behavior; require known project mappings.

## Built-in parameter reference

Use the stable identifier with `Element.get_Parameter(BuiltInParameter)` in the appropriate instance or type context. Check presence, storage type, quantity/specification and writability on the actual element. Extend this starter list as new categories and operations require it, following [API contract resolution](api.md).

| Purpose | BuiltInParameter | Initial applicability |
| --- | --- | --- |
| Reference to an element's type | `ELEM_TYPE_PARAM` | Elements exposing a type reference. Use `GetTypeId()` for type resolution and `ChangeTypeId(...)` for assignment. |
| Type name | `SYMBOL_NAME_PARAM` | Applicable element types. |
| Duct width and height | `RBS_CURVE_WIDTH_PARAM`, `RBS_CURVE_HEIGHT_PARAM` | Duct curves with applicable profiles. |
| Duct diameter | `RBS_CURVE_DIAMETER_PARAM` | Round duct curves. |
| Pipe diameter | `RBS_PIPE_DIAMETER_PARAM` | Applicable pipe curves. |
| System name and classification | `RBS_SYSTEM_NAME_PARAM`, `RBS_SYSTEM_CLASSIFICATION_PARAM` | MEP elements exposing these system properties. Verify physical system membership through connector/system APIs. |

Identifiers and descriptions were checked against Autodesk's Revit 2022 `RevitAPI.xml`. This establishes reference availability in that release. Verify applicability and behavior in the target release and document. Availability on curves does not establish availability on fittings, accessories or equipment. Use [connector geometry](geometry-and-connectors.md#size-groups-for-connector-based-operations) for physical connection sizes and resolve each family's driving parameters separately.

## Shared parameters and definition files

A shared parameter's GUID establishes its identity. Resolve values with `Element.get_Parameter(Guid)` in the declared instance/type context and project definitions with `SharedParameterElement.Lookup(doc, guid)` where applicable. Record same-name/different-GUID and same-GUID/incompatible-definition conflicts before dependent writes. Ordinary project or family parameters require their own verified identity and scope.

The shared parameter definition file (ФОП, файл общих параметров) stores external definitions and definition groups. The document stores its imported definitions, bindings and element values. Existing document values can be read without the original file. Editing the file does not automatically migrate definitions already loaded into projects or families.

1. Resolve the authoritative file for the task from project or organization configuration. Check the configured `Application.SharedParametersFilename` and open it through `Application.OpenSharedParameterFile()`. Treat a missing file or conflicting definition as a concrete gap for dependent definition work. Continue independent document reads.
2. Compare the required GUID, name, data specification and definition attributes with the existing file and document. Reuse the established GUID. Creating a definition without an explicit GUID generates a new identity, so replacement or renaming requires a deliberate migration plan covering values and dependencies.
3. For project bindings, inspect `Document.ParameterBindings`, `InstanceBinding` versus `TypeBinding`, categories and the parameter's UI group. Keep the file's definition group distinct from the UI group. When adding categories, retain existing categories and the binding kind unless the task changes them. Use the target-version `Insert`/`ReInsert` contract and check its result. Capture existing values and dependencies before a binding replacement or scope change and verify their preservation or intended migration afterward.
4. For family definitions, use `FamilyManager`. Verify GUID, instance/type scope, specification, formulas, associations and values across affected family types. Plan the effects of reloading the family into its owning project and verify them separately.
5. Treat file changes as a separate persistence operation within the authorized scope. Record the original file state and a restoration method before writing. Document transaction rollback cannot restore file contents. For a temporary switch of `Application.SharedParametersFilename`, retain its original value and restore it in `finally`. A permanent switch belongs to the task's explicit configuration scope.
6. After committing definition or binding changes, independently reread identity, specification, scope, categories and control values before the next value-writing batch. Report file changes, document commits and family reloads with their own outcomes.

The GUID, file-access and binding members above were checked against Autodesk's Revit 2022 API reference. Resolve overloads, specification/group identifiers and family replacement semantics for the target release through [API contracts](api.md). Keep the chosen file path, parameter GUIDs and family mappings in project configuration.

## Representation and quantity

StorageType is separate from quantity/specification. A Double can be length, flow, angle, area or dimensionless. Record the specification and external/internal units.

Use target-version conversion APIs; reject unavailable/failed conversions rather than returning the original input. Define tolerances in the comparison unit.

Compute with typed access. AsValueString is for presentation; SetValueString needs an explicit host locale/format contract. Parse external numbers with declared decimal/thousands conventions and reject ambiguity.

ElementId parameters can contain sentinels/references. Resolve semantics and owning document rather than treating them as ordinary integer quantities.

## Writing

Check binding, scope, storage/specification, writability and transaction mode. Distinguish unchanged/changed/absent/unsupported/failed. Verify using typed readback and tolerance; propagate failed verification to the transaction owner.

For coupled family parameters, verify resulting geometry/connectors. Do not identify an unknown binding by a coincidentally equal current value. Keep parameter maps, names and supported family behavior in project configuration.
