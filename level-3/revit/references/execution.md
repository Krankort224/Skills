# Execution choices

Choose from the requested deliverable, existing workflow and available capabilities. A model edit, a graph and an installable command have different delivery requirements.

| Concern | Establish |
| --- | --- |
| Language | Python, C# or DesignScript when the task involves textual code |
| Runtime | Python engine/version, CLR bridge, C# compiler and target .NET where relevant |
| Host | Dynamo for Revit, the gateway's in-process executor, or an add-in entry point |
| Access and invocation | MCP call, graph execution or command/event |

MCP exposes tool contracts. Its gateway determines supported execution languages and host capabilities. Dynamo can combine graph nodes, Python, DesignScript and compiled libraries. Read the installed profile and [runtime](runtime.md) before transferring code.

## Choose a route

| Task and context | Route and checks |
| --- | --- |
| Work in a live model with a sufficient typed tool | Read its actual schema, units, selection scope, side effects and result. Verify required postconditions. |
| Need API behavior or atomic verification beyond exposed tools | Use the available custom-code executor. rvt-mcp supports C# in its declared API context. Load [MCP operations](mcp-operations.md). |
| Deliver or maintain a Dynamo workflow | Preserve ports, payloads, bindings and engine/package versions. Load [Dynamo](dynamo.md). |
| Deliver a reusable installed command or application integration | Prepare an add-in with the requested build/deployment contract and target-version API references. |

An existing supported route can already satisfy repeatability. Choose a new deployment mechanism when the deliverable or operating requirements justify it.

## Add-in boundary

A compiled command normally enters through `IExternalCommand`; application startup/shutdown integration uses `IExternalApplication`. Resolve exact interfaces and target .NET from the target SDK. Register the assembly and entry class through a version-appropriate `.addin` manifest. Include required dependencies and a reproducible build. Preparing source and a manifest does not establish installation or successful loading. [Autodesk registration](https://help.autodesk.com/cloudhelp/2026/ENU/Revit-API/files/Revit_API_Developers_Guide/Introduction/Add_In_Integration/Revit_API_Revit_API_Developers_Guide_Introduction_Add_In_Integration_Add_in_Registration_html.html)

For a modeless interface, marshal model work through a supported Revit callback such as `ExternalEvent` and revalidate the document when that callback executes. [Autodesk external events](https://help.autodesk.com/cloudhelp/2026/ENU/Revit-API/files/Revit_API_Developers_Guide/Advanced_Topics/Revit_API_Revit_API_Developers_Guide_Advanced_Topics_External_Events_html.html)

## Transfer between hosts

Recheck document acquisition, input wrappers, units, transaction ownership, failure processing, cancellation and result serialization. Keep pure algorithms independent of those adapters. The C# [checked-model-edit](../assets/blocks/core/checked-model-edit.md) depends on `RvtMcp.Plugin.SafeFailuresPreprocessor`; adapt and verify that dependency for another host. A successful source-profile run provides evidence only for that profile.

For Dynamo language and extension choices, consult its [development overview](https://primer2.dynamobim.org/1_developer_primer_intro/3_developing_for_dynamo). Resolve exact API members through [API contracts](api.md).
