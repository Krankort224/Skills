---
name: workflow
description: Run repository work through the shared GitHub Issue lifecycle, loading only the instructions for the active ChatGPT or Codex execution contour.
metadata:
  short-description: Run the Issue workflow
---

# Workflow

Use GitHub Issues as stable task contracts and comments as the active work surface.

Work on one major pass at a time.

Issue status flows through:

`codex-ready → codex-active → codex-review`

The Issue body remains stable while a pass is active. Implementation instructions, handoffs, review findings, and correction cycles belong in comments. Rewrite the pass section only after the pass is accepted.

Load only the instructions for the active contour:

- ChatGPT: read `references/chatgpt.md`.
- Codex: read `references/codex.md`.

Do not load the other contour unless the current task explicitly requires inspecting or revising the workflow itself.
