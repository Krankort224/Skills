# Definition

Own Issue definition and execution dispatch.

## 1. Define the Issue

Make the Issue body a stable contract rather than a work log.

Use `../templates/issue.md` as the default structure.

The common contract contains:

- **Goal** — finished result;
- **Result boundary** — Definition of Done;
- **Inherited baseline** — accepted foundations that must not be silently redesigned;
- **Scope / Out of scope**.

Choose the execution shape deliberately.

### Simple Issue

Use a simple Issue when the work can be implemented and reviewed as one coherent unit.

Do not add a Pass plan or Passes section merely for formality.

The whole Issue is the current execution unit.

### Multi-pass Issue

Use major passes when the Issue contains several coherent results that should be implemented and accepted sequentially.

Add:

- **Pass plan** — major passes only;
- for each pass:
  - purpose;
  - planned decomposition when useful;
  - initial boundary;
  - acceptance target.

The top-level checklist contains only major passes. A checked item means the whole pass has been accepted.

The first unchecked major pass is the current execution unit.

Planned sub-passes are forecasts, not promises. Do not continuously rewrite the Issue body when they split, merge, disappear, or change during execution.

## 2. Prepare execution

Before dispatching execution:

- identify the current execution unit: the whole Issue for a simple Issue, or the first unaccepted major pass for a multi-pass Issue;
- read the Issue body and relevant active comments;
- determine the concrete instruction for the next execution cycle;
- preserve the current boundary and inherited baseline;
- do not silently introduce a new architectural or product decision;
- define what evidence will be sufficient for review.

Use `../templates/execution-comment.md` for the execution or correction comment.

If the task is contradictory, materially underspecified, or requires a new decision outside the accepted contract, resolve that with the user before dispatch rather than asking the executor to improvise.

For correction cycles, use the latest review findings to specify concrete corrections. Keep the contract body unchanged and preserve accepted parts unless they need correction.

When the execution or correction instruction is ready, publish it and set the Issue to `codex-ready`. Do not dispatch the next major pass before the current one is accepted.

### Execution recommendation to the user

After each initial or correction dispatch to `codex-ready`, report the execution recommendation **in the conversation**, separately from the Issue and GitHub comments.

Include:

- **Environment**;
- **Model**;
- **Reasoning**;
- **Why** — one short explanation tied to the actual task.

Do not add this recommendation to GitHub unless the user explicitly asks.

Treat it as advice to the user, not part of the task contract.
