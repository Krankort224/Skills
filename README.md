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
└── workflow/
    ├── SKILL.md
    ├── references/
    │   ├── chatgpt.md
    │   └── codex.md
    └── templates/
        ├── issue.md
        ├── execution-comment.md
        ├── handoff-comment.md
        └── accepted-summary.md
```

## Skills

### context

Loads the minimum authoritative repository context required for the current task.

The shared skill contains only general context-loading invariants. A repository-local installation may add:

```text
context/references/repository.md
```

based on `repository.template.md`.

The local map defines repository scopes, source authority, reading routes, and any non-obvious context boundaries.

### workflow

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
