---
name: workflow
description: Run repository work through the shared GitHub Issue lifecycle, loading only the instructions for the active ChatGPT or Codex execution contour.
metadata:
  short-description: Run the Issue workflow
---

# Workflow

Use GitHub Issues as stable task contracts and comments as the active work surface.

An Issue may be either:

- **simple** — the whole Issue is one execution/review unit;
- **multi-pass** — the Issue is split into major passes that are accepted sequentially.

Do not introduce passes unless they materially improve control of a larger task.

Issue status flows through:

`codex-ready → codex-active → codex-review`

While the current execution unit is active, keep its contract stable. Implementation instructions, handoffs, review findings, and correction cycles belong in comments. Rewrite accepted contract material only after acceptance.

Load only the instructions for the active contour:

- ChatGPT: read `references/chatgpt.md`.
- Codex: read `references/codex.md`.

Use templates from `templates/` when creating Issue workflow artifacts.

Do not load the other contour unless the current task explicitly requires inspecting or revising the workflow itself.
