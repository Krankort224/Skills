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
│   │   │   ├── chatgpt.md
│   │   │   └── codex.md
│   │   └── templates/
│   │       ├── issue.md
│   │       ├── execution-comment.md
│   │       ├── handoff-comment.md
│   │       └── accepted-summary.md
│   └── delegation/
│       ├── SKILL.md
│       └── agents/
│           └── openai.yaml
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

#### context

Loads the minimum authoritative repository context required for the current task.

The shared skill contains only general context-loading invariants. A repository-local installation may add:

```text
level-1/context/references/repository.md
```

based on `repository.template.md`.

The local map defines repository scopes, source authority, reading routes, and any non-obvious context boundaries.

#### workflow

Defines the shared GitHub Issue lifecycle for ChatGPT and Codex.

It supports:

- simple Issues, where the whole Issue is one execution/review unit;
- multi-pass Issues, where major passes are implemented and accepted sequentially.

The root skill acts as a lightweight router:

- ChatGPT loads `references/chatgpt.md`;
- Codex loads `references/codex.md`.

Issue bodies are stable contracts. Active implementation instructions, handoffs, review findings, and correction cycles live in comments.

Status flow:

```text
codex-ready → codex-active → codex-review
```

Reusable Issue artifacts are kept in `level-1/workflow/templates/`.

#### delegation

Defines execution planning and subagent orchestration for Codex. It covers deciding whether to delegate, planning the agent tree, passing task-specific context, handling failures, and verifying results.

The model contract has one canonical home in [level-1/delegation/SKILL.md](level-1/delegation/SKILL.md). Root is selected by the user; subagents use the lightweight or main executor defined by that contract.

Root applies `context` before planning. Subagents reuse their parent's task context and apply `context` only when additional repository context is needed; fully specified mechanical work does not require a separate context-loading cycle. The `context` contract remains unchanged.

The tree permits two subagent levels below root. Only lightweight work may be delegated to the second level; failure recovery belongs to the parent. This skill governs execution inside the task and does not replace `workflow` or `context`.

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
