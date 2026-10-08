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
