# Skills

Reusable agent skills for repository work.

This repository is the source of truth for shared skills. Projects can read its universal methods and resources directly while keeping their context and valid adaptations locally. Existing repository-local copies remain supported where explicitly chosen. The [Skills project map](level-1/context/references/repository.md) explains this repository's components, knowledge owners and reading routes; it is project knowledge, separate from the reusable [context template](level-1/context/references/repository.template.md).

## Structure

```text
Skills/
├── level-0/
│   └── arbitration/
├── level-1/
│   ├── context/
│   ├── workflow/
│   └── delegation/
├── level-2/
│   ├── architecture/
│   └── methodology/
└── level-3/
    ├── revit/
    ├── word/
    └── project-space/
```

Each skill owns its `SKILL.md` and supporting resources. [AGENTS.md](AGENTS.md#usage) owns selection rules: Level 0 is for dot or an assigned equivalent; Level 1 applies to every agent; Level 2 supplies semantically selected general/domain expertise; Level 3 supplies expertise for an established software context and operation. `word/` retains the `style-transfer` skill identifier.

Skill levels classify responsibility, not complexity, instruction priority or subagent depth. Level 2 and Level 3 may be used directly by root or workers and may compose. Operation-specific loading remains progressive. The [migration and adoption map](#migration-and-adoption) records changed paths, preserved identities and adoption checks. The prospective `mep` skill is not created by this migration.

## Repository skills

### Level 0

[Arbitration](level-0/arbitration/SKILL.md) keeps the user's goal with the arbiter and routes subject work to a bounded internal worker or an independently addressable owner. Its [two tools](level-0/arbitration/references/tools.md) resolve the Skills revision at reading time and review each exact outgoing assignment at dispatch time. The arbiter [adjudicates findings](level-0/arbitration/references/adjudicate.md) and [assesses readiness](level-0/arbitration/references/assess-readiness.md). A specialist assigned a direct task may execute it.

The [Codex dot arrangement](level-0/arbitration/references/codex-dot.md) defines В/Б/А, area writers and checkers, and changes of session or role. A permitted internal reviewer can check a fixed revision in the same user session. The [Hermes arrangement](level-0/arbitration/references/hermes.md) describes direct specialist intake and factual consultations between independently addressable participants under their existing grants.

### Level 1

Every agent reads these root contracts. They complement one another without requiring or invoking each other; load their supporting procedures only for applicable operations:

- [context](level-1/context/SKILL.md) owns source authority and sufficient repository understanding;
- [workflow](level-1/workflow/SKILL.md) owns the Issue contract, cycle lifecycle, and acceptance;
- [delegation](level-1/delegation/SKILL.md) owns selection, assignment, recovery and verification of internal subagents.

They compose through data: source-backed inputs, task requirements and acceptance criteria, assignments, and results with evidence. The cycle owner turns participant results into the overall handoff. Pass plans define acceptance units; agent trees distribute work within the current task. No fixed skill-call sequence is required.

#### context

Reads project purpose, component relationships and authoritative sources, and maintains or reviews project context references when requested. The sole [context entry point](level-1/context/SKILL.md) routes to read, maintain and review; ordinary loading/reading/review does not change files or install tools.

An adopted project uses a completed `skills/context/references/repository.md` explaining its purpose, scopes, component roles/interactions, knowledge owners, constraints and reading routes. Create it from the shared source template when available; preserve local adaptations and keep source templates in Skills. The map routes to canonical owners without duplicating their whole documents. Missing maps/graphs allow direct-source investigation.

Map-based initialization/refresh and read-only review are supported. The artifact-only `references/graphify/` skeleton reserves the derived JSON/HTML/report location without fabricated output. Selected graph work uses supporting [build](level-1/context/operations/graphify/build.md), [maintenance](level-1/context/operations/graphify/maintain.md), [read](level-1/context/operations/graphify/read.md) and [export](level-1/context/operations/graphify/export.md) methods. Their [technical profile and references](level-1/context/tools/graphify.md) own preparation, native recipes, schemas, APIs and compatibility evidence.

The tested Linux CPython 3.12 Python/Markdown lane supports fresh structural/active-agent mixed staging, conservative semantic reuse, cold-checkout recovery, coherent Git-commit trio publication and bounded native investigation. Changed inputs rebuild the full structural baseline; unchanged inputs/profile can retain exact output bytes. Optional presentation/interchange/cross-repository views preserve explicit source, direction, format and ownership limits. Actual Windows/Work host pilots and independent end-to-end integration remain [Issue #9](https://github.com/Krankort224/Skills/issues/9) gates. Graph methods add no entry point, Issue lifecycle or Operations-hub dependency.

#### workflow

Defines the shared GitHub Issue lifecycle by operation, independently of Chat, Work, or Codex. Applies to work on a specific Issue or a direct request to create one; ordinary work without an Issue does not use this lifecycle.

It supports:

- simple Issues, where the whole Issue is one execution/review unit;
- multi-pass Issues, where major passes are implemented and accepted sequentially.

The root skill acts as a lightweight router:

- definition loads `references/definition.md`;
- execution loads `references/execution.md`;
- acceptance, including result review, loads `references/acceptance.md`.

Issue bodies are stable contracts. Active implementation instructions, handoffs, review findings, and correction cycles live in comments. Creation, acceptance, and closure require direct, unambiguous user instruction; review alone does not authorize acceptance. Continuing in another interface preserves the task and prior authorizations without restarting an active cycle.

Status flow:

```text
codex-ready → codex-active → codex-review
```

Canonical Issue artifact schemas are kept in `level-1/workflow/templates/`; operation references define their use. Definition establishes inherited contracts and change boundaries; execution uses established canonical destinations; accepted summaries record task outcomes and point to project-wide knowledge at its owner.

#### delegation

[Delegation](level-1/delegation/SKILL.md) helps a parent decide whether to do the work directly, use deterministic code or assign a bounded contribution to an internal child. The parent owns the promised result. [Dispatch](level-1/delegation/operations/dispatch.md#prepare-an-accessible-task-package) packages the inputs, authority and expected evidence. [Collect](level-1/delegation/operations/collect.md) checks the returned work, resolves failures and settles outstanding writers.

[Model selection](level-1/delegation/references/model-selection.md) starts from the reasoning and access required. A task or project can select a map such as the [OpenAI pool](level-1/delegation/references/models/openai.md). Otherwise the agent assesses the permitted choices on the available evidence. The maintained [Codex](level-1/delegation/references/runtimes/codex.md) and [Hermes](level-1/delegation/references/runtimes/hermes.md) references describe their own controls. An unfamiliar host can use its exposed schema. [Decision scenarios](level-1/delegation/tests/scenarios.md) cover the portable behavior.

### Level 2

#### methodology

[Methodology](level-2/methodology/SKILL.md) has two entries. [Investigate](level-2/methodology/operations/investigate.md) helps explain a discrepancy, assess prior work, design or evaluate a working procedure, or interpret existing observations. [Organize](level-2/methodology/operations/organize.md) helps inventory existing material, design its organization, execute an agreed map, or review the outcome. Select the operation by the requested result. A completed experiment or an agreed migration map can be the starting point.

For detailed investigations, the [model](level-2/methodology/references/models.md) and [experiment](level-2/methodology/references/experiments.md) references cover verification and reproducible evidence. Method evaluation can use observations from ordinary work, including a pending proposal or memory. A request to list those records needs only the list. Maintainers can use the [discovery and execution checks](level-2/methodology/tests/method-review.md) to compare revisions.

#### architecture

[architecture](level-2/architecture/SKILL.md) develops, revises, compares, presents and reviews architectural design. A compact root routes to eight selectable operations: brief, concept, development, analysis, optimization, presentation, documentation and review. Local knowledge covers activity-based programming and shared-resource timelines, room/plan/section families, multi-building public-space/phase relationships, selected learning/library/short-stay and shared-domestic methods, site and outdoor relationships, massing and facade composition, envelope systems/junctions, environmental and structural/services interfaces, and critique through concrete spatial revision. Conditional strategies and worked progressions support design without retrieving the upstream skill collections; their exact provenance stays in the source map. Comparison methods and visual delivery support those architectural decisions. An optional question/coverage map groups quarter/urban context, site, building, spaces and systems/assemblies, with shared owners and explicit partial knowledge; direct common-question routes remain available without reading the whole map. A selectively loaded Russian normative catalog adds federal/work-stage, territory/local/special-condition, typology, fire/accessibility and sanitary/environmental/interface routes. Records retain official evidence, applicability triggers, edition/status observations and explicit verification gaps; document discovery does not establish design compliance.

Selected style profiles and authored building analyses add evidence-led classification and adaptation to another brief; general methods stay in references, while examples live in `assets/styles/<style>/<building>/` with inspected-source and reproduction limits. Requested-use completion methods add evidence sufficiency, schedule membership/meaning, decision precision and final revision closure; expanded representation methods connect each selected view to the decision and inspection it supports.

The user chooses the deliverable and format for each task. A concept may be textual when no artifact is requested; any requested artifact is produced and inspected appropriately. The skill has no automatic SVG default or mandatory SVG/raster pair. Its architectural reasoning can inform drawings, 3D and BIM work alongside other skills and tools when relevant to the task; it does not limit the agent's available workflows.

Four bounded Python tools support preliminary area, apparent-solar geometry, glazing-geometry and homogeneous-layer U-value comparisons. They use explicit inputs/units and make no compliance or full-simulation claim. The source map accounts for both pinned upstream packs, all fourteen calculator decisions and retained MIT notices. Jurisdiction/source applicability, assumptions, numerical results and design judgments stay distinguishable.

### Level 3

#### Word

[style-transfer](level-3/word/SKILL.md) combines the Word lifecycle and a reusable formatting library. Common principles live in `SKILL.md`; three procedures stay together in `operations/`: borrow formatting from a Word example, adapt an existing Word document, and create a new one. Detailed design, composition, DOCX mechanics, toolkit and validation materials remain in `references/` and load as needed.

Each preset is one Markdown file in `assets/presets/` containing all exact parameters and reusable rules. The starting library preserves technical, corporate, minimal and academic designs with their visual examples in `assets/examples/`. There is no parallel JSON preset representation. The Python toolkit reads the typed Markdown table and can extract a bounded draft from a DOCX. Captured drafts identify observed properties and base defaults and require review and visual reproduction before application.

`document_tool.py show-preset` validates the complete preset and prints all narrative rules without the parameter table; repeatable `--section` and `--parameter` options provide exact views after initial review. Execution loads all parameters from the same MD. References load by applicable section, and script sources need reading only for debugging or modification.

Markdown content interpretation is retained inside the creation operation. Tools provide supported building blocks; preserving arbitrary Word layouts, applying narrative composition rules and rendering still require the documented operation and environment capabilities. The former `document-creation` and `markdown-to-word` folders are consolidated into this one autonomous skill.

#### project-space

[project-space](level-3/project-space/SKILL.md) manages supported Project-space operations through files: workspace inspection, employee/access configuration, project properties, topics, task agreement/execution/review, material import and UNC references, replacement/deletion and task links. References cover causal replay, immutable publication and coordinated task/material drafts; an importable Windows helper supplies file transport without an MCP server or new application CLI. Product authorization and unsupported-operation boundaries remain in force. Select it for an established Project-space operation; live deployment and employee data stay outside skill sources.

#### revit

[revit](level-3/revit/SKILL.md) inspects and modifies models, creates/adapts/diagnoses automation and extracts reusable logical blocks. Five task-based procedures load only relevant knowledge. [Execution](level-3/revit/references/execution.md) distinguishes language, runtime, host and invocation through MCP, Dynamo or add-ins. [API contracts](level-3/revit/references/api.md) routes exact versioned questions to target documentation/SDK and assemblies. Engineering requirements can come from project sources or complementary domain skills.

Each logical block has one canonical Markdown file containing its contract, Python or C# implementation, limits, verification and provenance. The derived catalog navigates core, MEP and view helpers by language and runtime. Python tests load canonical fences. Five C# blocks retain imported native evidence for Revit 2022.1 / rvt-mcp 1.2.1, with source hashes and an accompanying smoke harness. Other hosts and changed implementations require their own verification.

Standard-library Python 3 tools inspect `.dyn`/ZIP metadata, validate block contracts/dependencies/links and Python syntax, and verify or compose C# smoke sources. The library validator does not compile C#. Native runs require the documented host, transaction ownership, fixtures and readback. The skill's methods remain usable beyond the current block inventory.

## Third-party skills

The [repository skills](#repository-skills) above are maintained in this Git tree. The following external skills are part of the broader working toolset but are installed separately; the connection method is documented here instead of copying or linking upstream source code.

| Skill | Source | Connection method | Coverage |
| --- | --- | --- | --- |
| **Ponytail** | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | **ChatGPT plugin** (`engineering-suite-ponytail`): install and enable Ponytail through **Settings → Plugins** or the chat sidebar. No Git submodule or repository-local skill installation is required. | Minimal implementation and simplification; code review and repository audits for over-engineering; technical-debt ledger and impact/help views. |

The Ponytail plugin bundles `ponytail`, `ponytail-review`, `ponytail-audit`, `ponytail-debt`, `ponytail-gain`, `ponytail-help`, and `code-simplification`. Its entry point and bundled instructions are supplied by the plugin. Availability is specific to the connected environment and must be checked independently for ChatGPT, Codex, or other agents; cloning this repository does not install or activate the plugin.

## Principles

- Describe each skill by the knowledge and methods it supplies, not by actions, formats, tools or other skills that it forbids an agent to use.
- Combine compatible skill knowledge within the user's task, subject to applicable activation, authorization and tool contracts. A method's evidence limits are not general prohibitions on the agent.
- Keep skills autonomous.
- Keep shared instructions compact.
- Load only the instructions relevant to the active task and execution contour.
- Keep repository-specific knowledge out of shared skills unless the skill explicitly provides an adaptation layer.
- Prefer stable contracts and source-of-truth boundaries over duplicated prose.
- Do not turn skills into copies of project documentation.
- Add supporting references, scripts, or templates only when they materially improve repeated work.

## Migration and adoption

Issue #9 Pass A migrated the source hierarchy from baseline `c11000bae812d9a87b366f44fa6d5706a5915a4a`; the migration implementation is `bf4415eabbc9a9d7f3f8a129d9637a7af1cfffe6`. [AGENTS.md](AGENTS.md#usage) owns the active skill-selection policy; this map records path and identifier compatibility only.

| Previous source | Current source | Skill identifier |
| --- | --- | --- |
| `level-2/revit-scripting/` | `level-3/revit/` | `revit-scripting` → `revit` |
| `level-2/word/` | `level-3/word/` | `style-transfer` unchanged |
| `level-2/project-space/` | `level-3/project-space/` | `project-space` unchanged |

The former `level-1/learning` was retired. Its [last Level-1 contract](https://github.com/Krankort224/Skills/blob/dc835ea066f8907df62ca6e519dc31231f2778b4/level-1/learning/SKILL.md) remains available for historical pins. Method evaluation now has a [direct entry in methodology](level-2/methodology/operations/investigate.md#design-or-evaluate-a-working-method).

#### Adopting methodology

The Level-2 `research` and `restructure` identifiers are retired. Their last separate [research](https://github.com/Krankort224/Skills/tree/ad1c823f1611319a6b17b2758a5f85630da6472c/level-2/research) and [restructure](https://github.com/Krankort224/Skills/tree/ad1c823f1611319a6b17b2758a5f85630da6472c/level-2/restructure) trees remain available at that revision. When adopting the newer shared source, replace those two active entries with `level-2/methodology/SKILL.md` and update operation references as follows.

| Former operation under `level-2/` | Current destination |
| --- | --- |
| `research/operations/question.md` | [Diagnose a discrepancy](level-2/methodology/operations/investigate.md#diagnose-a-discrepancy) or [design or evaluate a working method](level-2/methodology/operations/investigate.md#design-or-evaluate-a-working-method) |
| `research/operations/literature.md` | [Compare prior work](level-2/methodology/operations/investigate.md#compare-prior-work) |
| `research/operations/model.md` | [Models](level-2/methodology/references/models.md) |
| `research/operations/experiment.md` | [Experiments](level-2/methodology/references/experiments.md) |
| `research/operations/interpretation.md` | [Interpret existing evidence](level-2/methodology/operations/investigate.md#interpret-existing-evidence) |
| `restructure/operations/inventory.md` | [Inventory existing material](level-2/methodology/operations/organize.md#inventory-existing-material) |
| `restructure/operations/design.md` | [Design the structure](level-2/methodology/operations/organize.md#design-the-structure) |
| `restructure/operations/migration.md` | [Execute an agreed migration](level-2/methodology/operations/organize.md#execute-an-agreed-migration) |
| `restructure/operations/review.md` | [Review an existing result](level-2/methodology/operations/organize.md#review-an-existing-result) |

The three optional forms retain their names under `methodology/templates/`. The [evidence record](level-2/methodology/references/experiments.md#evidence-record) now owns the status vocabulary. Preserve existing records, completed forms, local adaptations and revision provenance during adoption.

#### Other source migrations

The arbitration and delegation reorganization starts at `e43d96842c1a11e134d1b77da92d78f595d2bbb6`. Apply the following paths relative to the named skill in either the source hierarchy or a flattened installation. Preserve the original pin for historical observations.

| Skill | Previous entry | Current destination |
| --- | --- | --- |
| Arbitration | `references/coordination.md` | [Shared assignments and return](level-0/arbitration/SKILL.md), [Codex dot organization](level-0/arbitration/references/codex-dot.md), [readiness checks](level-0/arbitration/references/assess-readiness.md) |
| Arbitration | `references/adjudication.md` | [Adjudicate](level-0/arbitration/references/adjudicate.md) |
| Arbitration | `tests/scenarios.md` | [Common cases](level-0/arbitration/tests/common.md), [Codex dot](level-0/arbitration/tests/codex-dot.md), [Hermes](level-0/arbitration/tests/hermes.md) |
| Delegation | `operations/plan.md` | [Direct work or child](level-1/delegation/SKILL.md), [selection](level-1/delegation/references/model-selection.md), [assignment and tree limits](level-1/delegation/operations/dispatch.md) |
| Delegation | `operations/recover.md`, `operations/integrate.md` | [Collect, recover and verify](level-1/delegation/operations/collect.md). The [dispatch package anchor](level-1/delegation/operations/dispatch.md#prepare-an-accessible-task-package) remains available. |
| Delegation | `references/runtimes/openai-collaboration.md` | [Historical evidence at its original revision](https://github.com/Krankort224/Skills/blob/e43d96842c1a11e134d1b77da92d78f595d2bbb6/level-1/delegation/references/runtimes/openai-collaboration.md). Select the current [Codex reference](level-1/delegation/references/runtimes/codex.md) when its documented surface applies. |
| Delegation | `references/runtimes/kimi-code.md` | [Retained Kimi source](level-1/delegation/references/runtimes/kimi-code.md). The current portable contract also covers hosts outside its maintained Codex and Hermes routes. |

The 2026-11-12 Revit consolidation starts from shared revision `9ff140d622f93f2a7b23356cbc4ebab878259467` and the local `revit-mcp` skill. Shared Revit owns the merged methods. MCP session guidance moves to `revit/references/mcp-operations.md`; modeling, connection boundaries and promotion rules move to the corresponding operation/subject owners. Five C# block paths remain relative to the skill root and their old `mcp-` IDs become filename-based IDs, recorded in each block's provenance with the original Markdown hash. Implementation hashes and native evidence are preserved. Full project field logs remain local. A local `revit-mcp` entry may route to this shared source at an identified revision; preserve existing inbound links during adoption.

At the time of the source-level migration, `architecture`, `research` and `restructure` stayed at Level 2. See [Adopting methodology](#adopting-methodology) for their subsequent catalog change. Level-0 arbitration and the three Level-1 skills retain their paths. Resources, scripts, examples and operation references move with their complete skill subtrees; source reclassification does not change their behavior.

For an explicitly chosen local-copy installation, place skills directly under the destination `skills/` (without the source `level-*` hierarchy). Shared use instead follows the source and project-reference routes below. Update active paths and Revit invocation names, preserve local customizations and original source revision/provenance, and keep already-published historical pins unchanged. Do not implicitly migrate downstream repositories. Original `*.template.*` files stay in this shared source; the adopted project keeps completed local versions.

Selection checks distinguish ordinary roots from assigned arbitration, workers from delegated operations, Level-2 domain work from established Level-3 software operations, combined architecture/Revit work, an incidental software mention from an actual software task, and Issue-free work from an Issue lifecycle. The reviewed examples and execution evidence remain in [Issue #9](https://github.com/Krankort224/Skills/issues/9); they are static contract checks, not model-behavior or native-host tests.

## Shared use across projects

A project's `AGENTS.md` identifies this repository, the applicable skill paths, its local context entry/map and any project-owned adaptations. Every agent reads the Level-1 roots, then only applicable operations; Level 0 remains an assigned arbitration role. Selection and composition stay owned by [AGENTS.md](AGENTS.md#usage), and model choices stay in delegation. A project constraint or explicit user instruction is not erased by switching the source of a method.

Read shared files with an already authorized GitHub connector or an identified local checkout. Resolve `main` to a commit for the current task, or use an explicitly adopted pin, and load all dependent resources at that revision. Record the actual revision in the task evidence and the project's existing provenance record when adopting it. Do not change the active task's revision merely because upstream moved. Shared changes can be read by subsequent tasks without distributing independent procedure copies.

A remote skill's relative links refer to its source directory at that commit. The target map and its links remain target-owned. A local context `SKILL.md` can be a short router to the shared context method plus its own `references/repository.md`; it adds project facts/adaptations rather than another implementation of context. Keep other valid adaptations at existing project owners and explicitly route to them before using a generic procedure. Source templates remain here; adapt them to completed project files.

For tools, identify a compatible shared tool directory and pass the target root separately. Reading a script via a connector does not prove it is executable on that host. Respect each project's access restrictions, including an established no-network route; report missing required access instead of claiming the transition works. No native skill registration, user-wide instruction installation, plugin, background update or new service is implied by these links.

## Repository-local adaptation

Shared skills may be copied into a repository-local skill directory when project-specific adaptation is useful. Keep them directly under the destination `skills/`, without the source level hierarchy; retain provenance and local adaptations.

For `context`, preserve the shared `SKILL.md` where possible. Use the source `references/repository.template.md` to create the destination's `references/repository.md` from that project's authoritative sources. Keep the template in Skills; exclude the populated Skills map and generated `references/graphify/` artifacts from transfer. Existing destination maps and graphs are project-owned: preserve them during skill updates, then refresh only when requested through context maintain. Each requested graph build selects that repository's own sources and scope; copying the Skills graph does not initialize a destination graph. A shared skill used from outside the target repository must locate the target's map rather than defaulting to its own adjacent map.

For `workflow`, the intent is to keep one common workflow across repositories rather than maintain project-specific variants.

For `methodology`, keep project-specific conventions, agreed directory structures and evidence at their project owners. When adopting a local copy, preserve the shared procedures, adapt optional forms into completed project documents, and update the skill's optional-form links to those documents or describe the local evidence location.

For `revit`, keep runtime profiles, project parameter/family bindings, paths, tolerances and native evidence locations in the project's existing configuration/instructions. Preserve shared block contracts and record the adopted source revision; project-specific pipeline state remains with its owner.

For `architecture`, preserve shared operations and evidence requirements. Keep the project brief, source applicability, area definitions, dimensions, accepted decisions and requested deliverable/format in existing project-owned material; retain source revision and license notices when transferring the skill.
