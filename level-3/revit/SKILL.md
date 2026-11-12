---
name: revit
description: Inspect and modify Revit models, develop and diagnose Revit automation, and reuse verified API methods. Use for established Revit tasks involving model elements, parameters, geometry, MEP connections, views or annotations through available MCP tools, Dynamo or add-ins.
---

# Revit

## Operations

Select the requested operation and load only its procedure plus missing prerequisites. Preserve the task and prior authorizations across interfaces and executors.

This skill owns Revit representation, API use, execution and verification. Project sources and complementary domain skills can supply engineering requirements, calculations and acceptance criteria. Resolve only the expertise the task needs; another skill is optional. The current block inventory does not limit the skill's knowledge scope.

| Request | Procedure | Result |
| --- | --- | --- |
| Inspect or change a model | [Modeling](operations/modeling.md) | Scoped observations or verified model changes |
| Write a script, graph or add-in | [Creation](operations/creation.md) | Implementation with explicit input, mutation and verification contracts |
| Change existing behavior | [Adaptation](operations/adaptation.md) | Bounded patch preserving agreed interfaces |
| Explain a failure | [Diagnostics](operations/diagnostics.md) | Source-backed finding, reproduction and correction path |
| Extract reusable logic | [Borrowing](operations/borrowing.md) | Canonical block with provenance and checks |

## Shared contract

- Establish the target document, Revit version/build, available capabilities and selected execution profile. Record language, engine/compiler, host and dependencies when relevant. Follow [execution](references/execution.md) when choosing a route and [API contracts](references/api.md) when resolving an unfamiliar or version-sensitive member.
- Define inputs, units, outputs, missing/ambiguous cases, ownership and mutation scope before implementation. Keep project family names, parameter maps, paths and tolerances in explicit task/project configuration.
- Separate read-only discovery, planning and document writes. A preview must not invoke a write callback. Use the task's concrete mutation scope and existing authorization; resolve only genuinely missing decisions needed for execution.
- Use supported Revit API context and a declared transaction owner. Record native statuses, readback, rollback and unexpected effects. An attempted write, setter return or subtransaction commit does not prove a verified document commit.
- Preserve identity and provenance through matching/traversal. Report boundaries, caps, exclusions and shared ownership. Reject unresolved ambiguity rather than silently broadening a selection.
- Separate logic tests, mocked API checks and actual Revit runs. State the tested profile and evidence for each claim. Legacy runtime success does not validate a generalized replacement.
- When native execution is unavailable, deliver inspectable code, available checks and a precise native verification case. Do not simulate a successful Revit run.

## Load technical detail by need

| Need | Reference |
| --- | --- |
| Choosing typed tools, scripts, graphs or add-ins | [Execution](references/execution.md) |
| Exact API members, SDK and version evidence | [API contracts](references/api.md) |
| Host, compatibility, offline boundary | [Runtime](references/runtime.md) |
| MCP target binding, call boundaries and unresolved operations | [MCP operations](references/mcp-operations.md) |
| Python ports, wires, payloads, graph inspection | [Dynamo](references/dynamo.md) |
| Transaction ownership, readback, regeneration | [Transactions](references/transactions.md) |
| Parameter identity, scope, data types, units | [Parameters and units](references/parameters-and-units.md) |
| Frames, link transforms, physical topology | [Geometry and connectors](references/geometry-and-connectors.md) |
| View domains, overrides, native references | [Annotations and references](references/annotations-and-references.md) |
| Symptom-led checks | [Error patterns](references/error-patterns.md) |

## Reuse the block library

Start with the derived [catalog](assets/blocks/catalog.md). Select by behavior, language, runtime and evidence, then read the complete chosen block and its dependencies. Load only selected blocks. Each implementation has one canonical `python` or `csharp` fence. Host dependencies remain explicit when adapting code between MCP, Dynamo and add-ins.

Each block owns purpose, inputs/outputs, implementation, limits, verification and provenance. Its Contract table owns `id`, `group`, `status`, `runtime`, `verification`, `dependencies` and `mutation`. New blocks declare `language`; older contracts infer it from the implementation fence. A `draft` needs review before use; `reviewed` means its recorded review/checks passed.

| Verification | Evidence |
| --- | --- |
| `static` | Syntax/contracts reviewed; behavior not executed |
| `offline` | Logic or mocks executed outside Revit; native behavior remains unverified |
| `runtime` | Linked evidence from this block in a stated Revit/host/model profile |

The library combines Python helpers and C# model-editing blocks in subject groups. Imported C# evidence covers the recorded Revit 2022.1 / rvt-mcp profile. Transfer and hash verification preserve that evidence; execution in a new host requires its own checks.

## Local tools and examples

Run Python 3 tools from the skill directory. They use the standard library and require no Revit. Read tool source only for debugging or changes.

```bash
python3 scripts/inspect_dyn.py path/to/graph.dyn
python3 scripts/inspect_dyn.py path/to/scripts.zip
python3 scripts/inspect_dyn.py path/to/graph.dyn --code NODE_ID
python3 scripts/inspect_dyn.py path/to/scripts.zip --extract path/to/output
python3 scripts/check_library.py --show-block parameter-access
python3 scripts/check_library.py
python3 scripts/check_library.py --catalog
python3 scripts/compose_smoke.py
python3 -m unittest discover -s scripts -p 'test_*.py'
```

The inspector reports versions, engines, node/port identities, wires and diagnostics without executing embedded code. Code/extraction are opt-in. The validator checks contracts, dependencies, local links and Python syntax. C# compilation requires its target compiler and assemblies. `--show-block` reads one complete block. `--catalog` derives navigation; update [catalog.md](assets/blocks/catalog.md) after library changes. The smoke composer checks C# source hashes against imported evidence; see [native checks](references/native-smoke.md) for fixture preparation and execution.

Use the synthetic [graph](assets/examples/graph-contract.dyn) and [expected inspection](assets/examples/graph-contract.expected.json) for graph-contract examples. Unit tests execute Markdown fences directly, avoiding a second implementation source.

## Delivery and local adaptation

Report changed behavior, artifacts, checks that ran and remaining native uncertainty. For document writes, include requested/actual scope, native commit/rollback status and readback. Attach the smallest useful raw case.

Preserve shared contracts on integration. Record the adopted source revision and configure local runtime, parameter/family bindings and evidence locations in the project's existing instructions/configuration. Project logs and unresolved pipeline state stay with their owners. Source authority, Issue lifecycle and agent orchestration remain with their applicable contracts.
