# Revit API contracts

The skill owns methods, preconditions, failure interpretation and verification. Exact versioned API contracts come from Autodesk documentation/SDK and the target assemblies. Revit supplies `RevitAPI.dll` for model access and `RevitAPIUI.dll` for UI and entry-point interfaces. [Autodesk API installation](https://help.autodesk.com/cloudhelp/2024/ENU/Revit-API/files/Revit_API_Developers_Guide/Introduction/Getting_Started/Welcome_to_the_Revit_Platform_API/Revit_API_Revit_API_Developers_Guide_Introduction_Getting_Started_Welcome_to_the_Revit_Platform_API_Installation_html.html)

## Resolve an unfamiliar or version-sensitive call

1. Establish the target Revit release/build and selected [runtime](runtime.md). Find the corresponding official API reference or local SDK documentation. Record the source/version for a material compatibility decision.
2. Resolve the owning type, assembly, member, overload, input and return types. Target assembly metadata can confirm presence and signatures. Reflection alone does not establish semantic behavior, supported execution context or successful use in the current document.
3. Read member remarks and exceptions for document kind, view, editability, transaction, regeneration and failure-processing conditions. Check quantities and internal units through [parameters and units](parameters-and-units.md).
4. For Python, distinguish an unavailable member from a CLR binding or conversion failure. Use the declaring-type guidance in [runtime](runtime.md#clr-property-binding-and-inheritance). For C#, check compiler, references and host dependencies.
5. Verify the smallest relevant behavior in the actual profile when native execution is available and in scope. Preserve discrepancies between documented and observed behavior, including exact inputs and outcomes. State the remaining native uncertainty when only source or compile checks are available.

## Follow the subject

| Question | Knowledge route |
| --- | --- |
| Document changes, commit, regeneration and rollback | [Transactions](transactions.md) |
| Element/type identity, parameters and quantities | [Parameters and units](parameters-and-units.md), then selected identity/access blocks |
| Coordinates, linked geometry and physical connections | [Geometry and connectors](geometry-and-connectors.md) |
| View scope, graphics and annotation references | [Annotations and references](annotations-and-references.md) |
| Invocation, API context and language/host adaptation | [Execution](execution.md) and [runtime](runtime.md) |

For another Revit API area, use the same contract-resolution method and load the relevant official source. The library contains selected reusable implementations. New coverage should capture a demonstrated decision or failure mode with its evidence. Full API inventories remain with their versioned owners.
