---
name: workflow
description: Manage GitHub Issue definition, execution, review, and acceptance. Apply only to a specific Issue or an explicit request to create one; route by operation across Chat, Work, and Codex.
metadata:
  short-description: Run the Issue workflow
---

# Workflow

## Applicability and authority

Apply only when the current task concerns a specific Issue or the user directly requests creating one. Otherwise, continue the user's task without this lifecycle or its operation references. An Issue mentioned elsewhere in the conversation does not bind the current task to it.

Create an Issue, accept an Issue or major pass, or close an Issue only on direct, unambiguous user instruction. A review request, passing checks, or silence does not authorize acceptance or closure.

## Task contract

Use GitHub Issues as stable task contracts and comments as the active work surface.

An Issue may be either:

- **simple** — the whole Issue is one execution/review unit;
- **multi-pass** — major passes are accepted sequentially.

Do not introduce passes unless they materially improve control of a larger task.

Status flow: `codex-ready → codex-active → codex-review`.

Designate one responsible owner per operation and cycle. Apply dispatch, Issue-status, and cycle-level publication instructions only to that owner. Supporting participants execute assignments within the owner's dispatched cycle and return results to the owner.

While the current execution unit is active, keep its contract stable. Implementation instructions, handoffs, review findings, and correction cycles belong in comments. Rewrite accepted contract material only after acceptance.

## Operations

Select by the current requested operation, independently of interface or model. Load only its reference:

- **Definition** — Issue contract, execution/correction instructions, dispatch: [definition](references/definition.md).
- **Execution** — implementation, verification, handoff: [execution](references/execution.md).
- **Acceptance** — result review, authorized acceptance, completion: [acceptance](references/acceptance.md).

Use templates from `templates/` for Issue artifacts. Load other operation references only when the task moves to those operations or explicitly concerns inspecting or revising this workflow.

## Continuation

When switching or branching between Chat, Work, and Codex, preserve the current task, execution unit, cycle, instructions, and prior explicit authorizations. Verify the live Issue body, status, and relevant comments before continuing Issue operations. Report inaccessible state rather than assuming it from conversation history.

Switching or branching does not create a new cycle, expand authority, or authorize acceptance. Continue an active cycle without repeating dispatch; follow the current requested operation.

## Artifact roles

Use these roles without replacing repository-specific context:

- canonical project knowledge — durable project-wide rules and architecture;
- Issue body — stable scope and accepted contract;
- active Issue comments — current implementation/review workspace;
- accepted summary — compact durable record of an accepted Issue or pass;
- Git history — exact change history.

Do not turn the Issue body into a diary.
