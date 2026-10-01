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
    │   └── references/
    │       ├── chatgpt.md
    │       └── codex.md
    └── word/
        ├── document-creation/
        │   ├── SKILL.md
        │   ├── references/
        │   ├── scripts/
        │   └── assets/
        └── markdown-to-word/
            └── SKILL.md
```

`level-1/` contains shared context and execution-management contracts. `level-2/` contains task-specific skills, with domain groups such as `word/` preserved where useful.

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

The skill uses an alternating two-contour process:

```text
Codex inventory
    ↓
ChatGPT semantic analysis and target structure
    ↓
Codex migration and validation
    ↓
ChatGPT review
```

Codex owns direct filesystem discovery and mechanical migration. ChatGPT owns semantic classification, target-structure design, migration planning, and final structural review.

Cloud-hosted file contents must not be downloaded, materialized, synchronized, exported, or copied into the local environment without separate, explicit, and unambiguous user authorization.

#### Word

Two level-2 skills live under `level-2/word/`:

- `document-creation` owns the complete Word lifecycle: source analysis, structure, visual design, template adaptation, deterministic creation/editing, package checks, rendering, and visual correction;
- `markdown-to-word` converts Markdown semantics into an editable DOCX with minimal styling.

`document-creation` includes four machine-readable presets (technical, corporate, minimal, academic), component and layout guides, tested Python helpers, and reproducible visual examples. A user-selected template takes priority over presets.

For Markdown input, `markdown-to-word` owns semantic interpretation; `document-creation` provides the Word authoring and verification lifecycle. The Markdown skill's capability redesign is deferred.

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
