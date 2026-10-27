# Runtime

## Execution profile

Record Revit major/build, Dynamo version, Python engine/version, host, document kind, view and editability/worksharing state. Record packages/assemblies and how document/selection inputs arrive. Scope evidence to that profile.

Legacy graph sources use Dynamo 2.12.1.8246 with `IronPython2` in Revit 2022 workflows. Python 3 scripts in this skill run offline. Engine labels and Python 3 compilation do not validate IronPython/.NET overloads.

## Host adapters

- Load native/host assemblies at the entry point. Keep block imports inside native helpers so pure logic can run offline.
- Obtain the document through the actual host and pass it explicitly. Do not assume an active UI document in family/background workflows.
- Unwrap Dynamo elements at the boundary; distinguish elements, ElementIds and records. Preserve owning document identity.
- Keep live document access in supported Revit API context. Worker threads may process immutable numeric snapshots; use supported callbacks for native API work.
- Treat linked documents as separately owned/read-only scopes. Bind link instance and linked element; identify unloaded links.

## Compatibility

Use an explicit adapter for a real version difference. Check the target assembly rather than swallowing exceptions and returning valid-looking defaults. Native tests are needed where .NET collections, enum/overload selection and host wrappers affect behavior.

### CLR property binding and inheritance

Treat direct `obj.Property` as dynamic binding, not an authoritative API-contract query. A runtime subclass may hide/override a CLR property or expose a different set of accessors. IronPython/DLR can fail to expose the inherited getter even when that getter remains available on its declaring base type. `hasattr()` and `getattr()` use attribute access too; their failure alone does not prove that the property is absent.

Distinguish confirmed absence in the selected contract, an unresolved direct-access failure, an unavailable getter, a successful null/empty result and a getter/API exception. Do not diagnose a binder failure solely from AttributeError or its message. Preserve stage, exception type/text and actual access path.

Use the bounded [clr-property-access](../assets/blocks/core/clr-property-access.md) adapter. Without a declaring type it attempts direct access once. With a declaring type it selects that property's getter immediately, with no dynamic owner-property read and no fallback to direct access after failure. Confirm absence through the selected contract metadata; a metadata-resolution error is not absence. Do not scan arbitrary base classes or replace all property reads with reflection.

The [IronPython descriptor documentation](https://ironpython.net/documentation/dotnet/dotnet.html) describes `DeclaringType.Property.GetValue(instance)`. For the observed Revit 2022 / Dynamo 2.12 / IronPython 2 case, use:

```python
name = Element.Name.GetValue(element)
```

rather than depending on runtime-class `element.Name` where that declaration conflicts with the inherited getter. [DEC-027 at e15c0cae](https://github.com/Krankort224/Revit-automatization/blob/e15c0caebe8e582119c984eba1cef95e9c736ab3/knowledge/06_DECISIONS.md#dec-027--metadata-имена-элемента-типа-и-семейства-разделяются), in `block0-diversified`, records the original runtime-validated type-name parameter/getter contract. It does not validate the new library adapter. Keep generalized blocks at their actual evidence level; Python 3 CLR descriptor behavior needs separate verification.

Preserve successful None as null and retain its access path; empty text, 0 and False are values. Do not turn failed metadata into empty names and then report a definitive missing/unique type match. [element-identity](../assets/blocks/core/element-identity.md) loads the helper dependency and makes incomplete required candidate metadata indeterminate.

### Version-specific APIs

UnitTypeId/ForgeTypeId and legacy unit enums are not interchangeable values. Isolate ElementId representation differences. Parameter data type/specification is distinct from storage type.

## Evidence boundary

| Capability | Valid conclusion |
| --- | --- |
| JSON/text inspection | Source/graph contracts and recorded metadata |
| Compilation | Syntax in the tested interpreter |
| Pure tests | Algorithm behavior on tested cases |
| Revit mocks | Branch/receipt behavior under mock assumptions |
| Revit run and readback | Native behavior in the stated model/profile/scope |

Without native access, supply a bounded case: inputs, execution switch, preconditions, outputs, affected IDs, commit/rollback criteria and evidence needed. Do not invent runtime logs.

## Primary API source

Use the target version's Autodesk API reference/SDK. The [transaction guide](https://help.autodesk.com/cloudhelp/2024/ENU/Revit-API/files/Revit_API_Developers_Guide/Basic_Interaction_with_Revit_Elements/Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Transactions_html.html) documents API context; its version is not proof of this library's compatibility.
