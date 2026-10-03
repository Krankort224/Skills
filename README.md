# Skills

Reusable agent skills for repository work.

This repository is the source of truth for shared skills. Repository-local copies may be adapted where a skill explicitly supports local specialization.

## Structure

```text
Skills/
├── level-1/
│   ├── context/
│   │   ├── SKILL.md
│   │   └── references/
│   │       └── repository.template.md
│   ├── workflow/
│   │   ├── SKILL.md
│   │   ├── references/
│   │   │   ├── definition.md
│   │   │   ├── execution.md
│   │   │   └── acceptance.md
│   │   └── templates/
│   │       ├── issue.md
│   │       ├── execution-comment.md
│   │       ├── handoff-comment.md
│   │       └── accepted-summary.md
│   └── delegation/
│       └── SKILL.md
└── level-2/
    ├── restructure/
    │   ├── SKILL.md
    │   └── operations/
    │       ├── inventory.md
    │       ├── design.md
    │       ├── migration.md
    │       └── review.md
    ├── research/
    │   ├── SKILL.md
    │   ├── operations/
    │   │   ├── question.md
    │   │   ├── literature.md
    │   │   ├── model.md
    │   │   ├── experiment.md
    │   │   └── interpretation.md
    │   └── templates/
    │       ├── evidence-map.template.md
    │       ├── experiment.template.md
    │       └── result.template.md
    └── word/
        ├── SKILL.md
        ├── operations/
        │   ├── borrowing.md
        │   ├── adaptation.md
        │   └── creation.md
        ├── references/
        ├── scripts/
        └── assets/
            ├── examples/
            └── presets/
```

`level-1/` contains shared context and execution-management contracts. `level-2/` contains task-specific skills; `word/` is the self-contained `style-transfer` skill.

Skill levels classify responsibility; they are independent of subagent nesting levels. A level-2 skill may be used directly by root.

## Skills

### Level 1

These skills complement one another without requiring or invoking each other. Select them through the task and applicable instructions:

- [context](level-1/context/SKILL.md) owns source authority and sufficient repository understanding;
- [workflow](level-1/workflow/SKILL.md) owns the Issue contract, cycle lifecycle, and acceptance;
- [delegation](level-1/delegation/SKILL.md) owns execution decomposition, agent assignments, recovery, and integration.

They compose through data: source-backed inputs, task requirements and acceptance criteria, assignments, and results with evidence. The cycle owner turns participant results into the overall handoff. Pass plans define acceptance units; agent trees distribute work within the current task. No fixed skill-call sequence is required.

#### context

Loads the minimum authoritative repository context required for the current task.

The shared skill contains only general context-loading invariants. A repository-local installation may add:

```text
level-1/context/references/repository.md
```

based on `repository.template.md`.

The local map defines repository scopes, knowledge and contract owners, source authority, canonical update destinations, reading routes, and special-source access rules. Ownership boundaries belong in one shared table; contracts remain at their canonical sources. The shared skill resolves these roles and reports material gaps without modifying project knowledge.

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

The model contract has one canonical home in [level-1/delegation/SKILL.md](level-1/delegation/SKILL.md). Root is selected by the user; subagents use the lightweight or main executor defined by that contract.

Root establishes sufficient inputs for decomposition; missing inputs may be gathered directly or through bounded exploration before dependent execution. Assignments carry requirements, decisions, source pointers/revision, and unresolved questions. Workers retrieve missing inputs under applicable project rules; fully specified mechanical work needs no separate context-loading cycle.

The default maximum tree depth is two subagent levels below root; root may increase it for justified decomposition. At the deepest level, when depth is at least two, only lightweight agents and easy tasks are allowed. Intermediate levels may contain main executors. The skill also defines failure diagnosis, stalled-work recovery, and a compact report contract.

### Level 2

#### restructure

Restructures an existing repository or file accumulation without imposing a universal directory layout.

The root routes to four adjacent procedures in `operations/`: inventory, design and migration planning, migration, and review. Start at the requested operation and load only the procedure and missing prerequisites. Common principles and capability/access boundaries stay in `SKILL.md`.

Assign operations by available capabilities and access, independently of Chat, Work, Codex or model. One executor may perform several operations; handoffs preserve evidence, the agreed migration map and prior authorizations. Migration follows the agreed map; review checks both mechanical preservation and whether the structure resolves the stated problems.

Cloud-hosted file contents must not be downloaded, materialized, synchronized, exported, or copied into the local environment without separate, explicit, and unambiguous user authorization.

#### research

[research](level-2/research/SKILL.md) connects a research question, evidence-producing checks, interpretation, and the next iteration. Use it for scientific and engineering investigations, numerical models, and testable investigations of software behavior when explicitly requested.

The lightweight root routes to adjacent procedures in `operations/`: question framing, literature and prior art, model formalization, experiment design/execution, and interpretation. Start at the current phase and load only the required procedures/forms. Root definitions own the independent `execution_status`, `evidence_quality` and `claim_status` vocabularies. Responsibilities follow operations and available capabilities across Chat, Work, and Codex.

Keep exploratory and confirmatory work distinct. Separate implementation correctness, numerical credibility, and correspondence to the investigated system. Preserve negative/inconclusive results and plan deviations; distinguish execution failure from evidence against a hypothesis. Checks and run counts are proportional to the question and uncertainty, with explicit budget and stopping conditions.

Three optional adaptation forms cover evidence mapping, experiment definition, and results. Reuse project documents and storage conventions rather than introducing another directory layout. Source authority, Issue lifecycle, and agent orchestration remain with Level 1 contracts.

#### Word

[style-transfer](level-2/word/SKILL.md) combines the Word lifecycle and a reusable formatting library. Common principles live in `SKILL.md`; three procedures stay together in `operations/`: borrow formatting from a Word example, adapt an existing Word document, and create a new one. Detailed design, composition, DOCX mechanics, toolkit and validation materials remain in `references/` and load as needed.

Each preset is one Markdown file in `assets/presets/` containing all exact parameters and reusable rules. The starting library preserves technical, corporate, minimal and academic designs with their visual examples in `assets/examples/`. There is no parallel JSON preset representation. The Python toolkit reads the typed Markdown table and can extract a bounded draft from a DOCX. Captured drafts identify observed properties and base defaults and require review and visual reproduction before application.

`document_tool.py show-preset` validates the complete preset and prints all narrative rules without the parameter table; repeatable `--section` and `--parameter` options provide exact views after initial review. Execution still loads all settings from the same MD. References load by applicable section, and script sources need reading only for debugging or modification.

Markdown content interpretation is retained inside the creation operation. Tools provide supported building blocks; preserving arbitrary Word layouts, applying narrative composition rules and rendering still require the documented operation and environment capabilities. The former `document-creation` and `markdown-to-word` folders are consolidated into this one autonomous skill.

## Principles

- Keep skills autonomous.
- Keep shared instructions compact.
- Load only the instructions relevant to the active task and execution contour.
- Keep repository-specific knowledge out of shared skills unless the skill explicitly provides an adaptation layer.
- Prefer stable contracts and source-of-truth boundaries over duplicated prose.
- Do not turn skills into copies of project documentation.
- Add supporting references, scripts, or templates only when they materially improve repeated work.

## Repository-local adaptation

Shared skills may be copied into a repository-local skill directory when project-specific adaptation is useful.

For `context`, preserve the shared `SKILL.md` where possible and create a repository-specific `references/repository.md` from the provided template.

For `workflow`, the intent is to keep one common workflow across repositories rather than maintain project-specific variants.

For `restructure`, keep the shared process generic and express project-specific structure decisions in the task itself rather than creating a permanent project-specific fork unless repeated local rules justify one.

For `research`, preserve shared principles and operation procedures, and use the project's existing methodology and artifact locations. Adapt optional forms into completed project documents; source `*.template.*` files stay in Skills. Replace the local skill's adopted-artifacts subsection with links to those documents or a description of the local forms, so integration does not leave broken template links.
