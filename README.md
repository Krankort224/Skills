# Skills

Reusable agent skills for repository work.

This repository is the source of truth for shared skills. Repository-local copies may be adapted where a skill explicitly supports local specialization.

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
│   ├── research/
│   ├── restructure/
│   └── ponytail/   # pinned upstream gitlink; reference only
└── level-3/
    ├── revit/
    ├── word/
    └── project-space/
```

Each skill owns its `SKILL.md` and supporting resources. [AGENTS.md](AGENTS.md#usage) owns selection rules: Level 0 is for dot or an assigned equivalent; Level 1 applies to every agent; Level 2 supplies semantically selected general/domain expertise; Level 3 supplies expertise for an established software context and operation. `word/` retains the `style-transfer` skill identifier.

Skill levels classify responsibility, not complexity, instruction priority or subagent depth. Level 2 and Level 3 may be used directly by root or workers and may compose. Operation-specific loading remains progressive. The [migration and adoption map](#migration-and-adoption) records changed paths, preserved identities and adoption checks. The prospective `mep` skill is not created by this migration.

## Skills

### Level 0

[arbitration](level-0/arbitration/SKILL.md) supports dot's arbitration role, or an explicitly assigned equivalent, between the user, execution, and independent review. Supporting references cover adjudication and coordination; published availability does not guarantee automatic loading. An ordinary root agent does not acquire this role from its tree position.

### Level 1

Every agent reads these root contracts. They complement one another without requiring or invoking each other; load their supporting procedures only for applicable operations:

- [context](level-1/context/SKILL.md) owns source authority and sufficient repository understanding;
- [workflow](level-1/workflow/SKILL.md) owns the Issue contract, cycle lifecycle, and acceptance;
- [delegation](level-1/delegation/SKILL.md) owns execution decomposition, agent assignments, recovery, and integration.

They compose through data: source-backed inputs, task requirements and acceptance criteria, assignments, and results with evidence. The cycle owner turns participant results into the overall handoff. Pass plans define acceptance units; agent trees distribute work within the current task. No fixed skill-call sequence is required.

#### context

Reads project purpose, component relationships and authoritative sources, and maintains or reviews project context references when requested. The sole [context entry point](level-1/context/SKILL.md) routes to read, maintain and review; ordinary loading/reading/review does not change files or install tools.

An adopted project uses a completed `skills/context/references/repository.md` explaining its purpose, scopes, component roles/interactions, knowledge owners, constraints and reading routes. Create it from the shared source template when available; preserve local adaptations and keep source templates in Skills. The map routes to canonical owners without duplicating their whole documents. Missing maps/graphs allow direct-source investigation.

Map-based initialization/refresh and read-only review are supported. The artifact-only `references/graphify/` skeleton reserves the derived JSON/HTML/report location without fabricated output. [Graphify's audited profile](level-1/context/tools/graphify.md) records B's source/feasibility evidence; graph construction, genuine subscription semantic extraction, portable graph maintenance/publication and host pilots remain later [Issue #9](https://github.com/Krankort224/Skills/issues/9) gates. There is no Operations-hub dependency.

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

Defines execution planning and subagent orchestration for Codex. It covers deciding whether to delegate, planning the agent tree, passing task-specific context, handling failures, and verifying results.

The model contract has one canonical home in [level-1/delegation/SKILL.md](level-1/delegation/SKILL.md). Root is selected by the user; subagent selection follows that contract's task-complexity criteria.

Root establishes sufficient inputs for decomposition; missing inputs may be gathered directly or through bounded exploration before dependent execution. Assignments carry requirements, decisions, source pointers/revision, and unresolved questions. Workers retrieve missing inputs under applicable project rules; fully specified mechanical work needs no separate context-loading cycle.

Tree depth, allowed model tiers at each level, and spawning rights are defined by the skill. It also defines failure diagnosis, stalled-work recovery, and a compact report contract.

### Level 2

#### ponytail — external reference

[ponytail](level-2/ponytail) is a pinned Git submodule linking to [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail), not an adopted skill. Its source is available for deliberate inspection; no installation, hooks, agent policy or personality is enabled through this link.

#### restructure

Restructures an existing repository or file accumulation without imposing a universal directory layout.

The root routes to four adjacent procedures in `operations/`: inventory, design and migration planning, migration, and review. Start at the requested operation and load only the procedure and missing prerequisites. Common principles and capability/access boundaries stay in `SKILL.md`.

Assign operations by available capabilities and access, independently of Chat, Work, Codex or model. One executor may perform several operations; handoffs preserve evidence, the agreed migration map and prior authorizations. Migration follows the agreed map; review checks both mechanical preservation and whether the structure resolves the stated problems.

Cloud-hosted file contents must not be downloaded, materialized, synchronized, exported, or copied into the local environment without separate, explicit, and unambiguous user authorization.

#### research

[research](level-2/research/SKILL.md) connects a research question, evidence-producing checks, interpretation, and the next iteration. Use it when the task calls for scientific and engineering investigations, numerical models, or testable investigations of software behavior.

The lightweight root routes to adjacent procedures in `operations/`: question framing, literature and prior art, model formalization, experiment design/execution, and interpretation. Start at the current phase and load only the required procedures/forms. Root definitions own the independent `execution_status`, `evidence_quality` and `claim_status` vocabularies. Responsibilities follow operations and available capabilities across Chat, Work, and Codex.

Keep exploratory and confirmatory work distinct. Separate implementation correctness, numerical credibility, and correspondence to the investigated system. Preserve negative/inconclusive results and plan deviations; distinguish execution failure from evidence against a hypothesis. Checks and run counts are proportional to the question and uncertainty, with explicit budget and stopping conditions.

Three optional adaptation forms cover evidence mapping, experiment definition, and results. Reuse project documents and storage conventions rather than introducing another directory layout. Source authority, Issue lifecycle, and agent orchestration remain with Level 1 contracts.

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

[revit](level-3/revit/SKILL.md) creates, adapts and diagnoses Revit/Dynamo scripts, and extracts reusable logical blocks from source examples. The root routes to four adjacent procedures in `operations/`; runtime, Dynamo, transactions, parameters/units, geometry/connectors, annotations/references and error patterns load from `references/` as needed. The rename preserves current coverage; it does not claim newly implemented Revit capabilities.

Each logical block has one canonical Markdown file containing its contract, Python implementation, limits, verification and pinned provenance. The derived catalog navigates core, MEP and view helpers. Offline tests load those implementation fences directly. The initial library is reviewed with offline checks; native Revit behavior remains a separate verification requirement.

Two standard-library Python 3 tools inspect `.dyn`/ZIP metadata, ports and wires without executing embedded code, and validate block contracts, dependencies, syntax and local links. Script/graph creation and native document writes still require the documented runtime, transaction ownership and readback contract.

## External references

The [Ponytail gitlink](level-2/ponytail) on Level 2 points to the official upstream repository at the pinned revision `96608e078b2d5ea607c5c3b8b5a54d1c1fba6846`. It is a reference for deliberate consultation, not an installed skill or plugin; its instructions and hooks are not adopted automatically.

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

`architecture`, `research` and `restructure` remain Level 2. Level-0 arbitration and the three Level-1 skills retain their paths. Resources, scripts, examples and operation references move with their complete skill subtrees; source reclassification does not change their behavior.

For adoption into another repository, install skills directly under its own `skills/` (without the source `level-*` hierarchy). Update active paths and Revit invocation names, preserve local customizations and original source revision/provenance, and keep already-published historical pins unchanged. Do not implicitly migrate downstream repositories. Original `*.template.*` files stay in this shared source; the adopted project keeps completed local versions.

Selection checks distinguish ordinary roots from assigned arbitration, workers from delegated operations, Level-2 domain work from established Level-3 software operations, combined architecture/Revit work, an incidental software mention from an actual software task, and Issue-free work from an Issue lifecycle. The reviewed examples and execution evidence remain in [Issue #9](https://github.com/Krankort224/Skills/issues/9); they are static contract checks, not model-behavior or native-host tests.

## Repository-local adaptation

Shared skills may be copied into a repository-local skill directory when project-specific adaptation is useful. Keep them directly under the destination `skills/`, without the source level hierarchy; retain provenance and local adaptations.

For `context`, preserve the shared `SKILL.md` where possible and create a repository-specific `references/repository.md` from the provided template.

For `workflow`, the intent is to keep one common workflow across repositories rather than maintain project-specific variants.

For `restructure`, keep the shared process generic and express project-specific structure decisions in the task itself rather than creating a permanent project-specific fork unless repeated local rules justify one.

For `research`, preserve shared principles and operation procedures, and use the project's existing methodology and artifact locations. Adapt optional forms into completed project documents; source `*.template.*` files stay in Skills. Replace the local skill's adopted-artifacts subsection with links to those documents or a description of the local forms, so integration does not leave broken template links.

For `revit`, keep runtime profiles, project parameter/family bindings, paths, tolerances and native evidence locations in the project's existing configuration/instructions. Preserve shared block contracts and record the adopted source revision; project-specific pipeline state remains with its owner.

For `architecture`, preserve shared operations and evidence requirements. Keep the project brief, source applicability, area definitions, dimensions, accepted decisions and requested deliverable/format in existing project-owned material; retain source revision and license notices when transferring the skill.
