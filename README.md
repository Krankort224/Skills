# Skills

Reusable agent skills for repository work.

This repository is the source of truth for shared skills. Repository-local copies may be adapted where a skill explicitly supports local specialization.

## Structure

```text
Skills/
├── context/
│   ├── SKILL.md
│   └── references/
│       └── repository.template.md
├── workflow/
│   ├── SKILL.md
│   ├── references/
│   │   ├── chatgpt.md
│   │   └── codex.md
│   └── templates/
│       ├── issue.md
│       ├── execution-comment.md
│       ├── handoff-comment.md
│       └── accepted-summary.md
├── restructure/
│   ├── SKILL.md
│   └── references/
│       ├── chatgpt.md
│       └── codex.md
└── word/
    ├── design/
    │   └── SKILL.md
    ├── technical/
    │   └── SKILL.md
    └── markdown-to-word/
        └── SKILL.md
```

## Skills

### Level 1

#### context

Loads the minimum authoritative repository context required for the current task.

The shared skill contains only general context-loading invariants. A repository-local installation may add:

```text
context/references/repository.md
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

Reusable Issue artifacts are kept in `workflow/templates/`.

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

### Word

Three independent skills live under `word/`:

- `design` chooses and applies the visual system for a Word document;
- `technical` inspects and changes DOCX structure while preserving unrelated content and formatting;
- `markdown-to-word` converts Markdown semantics into an editable DOCX with minimal styling.

For Markdown that also needs visual polish, use `markdown-to-word` first and `design` second. Either skill can follow `technical` for low-level DOCX operations without handing over its own design or conversion decisions.

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
