# ChatGPT Contour

Own task definition, execution dispatch, review, acceptance, and progression.

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

Before sending work to Codex:

- identify the current execution unit: the whole Issue for a simple Issue, or the first unaccepted major pass for a multi-pass Issue;
- read the Issue body and relevant active comments;
- determine the concrete instruction for the next execution cycle;
- preserve the current boundary and inherited baseline;
- do not silently introduce a new architectural or product decision;
- define what evidence will be sufficient for review.

Use `../templates/execution-comment.md` for the execution or correction comment.

If the task is contradictory, materially underspecified, or requires a new decision outside the accepted contract, resolve that in Chat before dispatch rather than asking Codex to improvise.

When the execution instruction is ready, set the Issue to `codex-ready`.

### Execution recommendation to the user

After preparing the task and setting `codex-ready`, report the execution recommendation **in Chat**, separately from the Issue and GitHub comments.

Include:

- **Environment**;
- **Model**;
- **Reasoning**;
- **Why** — one short explanation tied to the actual task.

Do not add this recommendation to GitHub unless the user explicitly asks.

Treat it as advice to the user, not part of the task contract.

## 3. Review Codex handoff

When Codex moves the Issue to `codex-review`, review the result against the current execution unit.

Check:

1. purpose, scope, and boundary;
2. acceptance target or Result boundary;
3. actual commits and diff;
4. reported tests, runtime checks, or other evidence;
5. project contracts and accepted decisions;
6. unintended or out-of-scope changes;
7. limitations, risks, and unverified claims.

Inspect evidence needed to verify material claims rather than relying only on the handoff summary.

Review defects-first: identify incorrect behavior, missing acceptance criteria, regressions, unsupported claims, or scope violations before stylistic improvements.

Do not redefine the task to fit the implementation that happened.

## 4. Correction cycle

If the current execution unit is not acceptable:

- state concrete review findings in an Issue comment;
- specify the required correction;
- keep the contract body unchanged;
- preserve accepted parts unless they genuinely need revision;
- set the Issue back to `codex-ready`.

Then report a fresh execution recommendation to the user in Chat. Environment, model, or reasoning may differ from the previous cycle.

Repeat:

`instruction → Codex handoff → ChatGPT review → correction`

as many times as necessary.

## 5. Accept the current execution unit

Use `../templates/accepted-summary.md` for the durable accepted summary.

### Simple Issue

When the whole Issue is accepted:

- reconcile the body with the final accepted result if needed;
- write one durable accepted summary comment;
- verify the overall Result boundary;
- complete the Issue.

### Multi-pass Issue

When a major pass is accepted:

1. mark its top-level checkbox complete;
2. set its pass status to `accepted`;
3. replace provisional planned decomposition with the actual **Final decomposition**;
4. replace provisional acceptance material with the **Accepted result**;
5. record the **Boundary carried forward**;
6. record the final commit and accepted-summary reference;
7. write one durable accepted summary comment;
8. clean up working-comment clutter only according to the repository's supported cleanup method.

The accepted pass section should describe what the pass finally became, not preserve obsolete forecasts.

Do not begin the next major pass until the current one is accepted.

## 6. Accepted summary

Preserve only information that remains useful after the implementation conversation is over.

Include when relevant:

- problems found;
- root causes;
- corrections and accepted decisions;
- rejected approaches that should not be casually reintroduced;
- final verification;
- final commit;
- accepted baseline.

Omit empty sections.

Do not turn the summary into a chronological replay of active comments.

## 7. Complete the Issue

A simple Issue is complete when its Result boundary is accepted.

A multi-pass Issue is complete only when all major passes and the overall Result boundary are accepted.

Before final completion, verify that:

- the final Issue body matches the accepted work;
- all required major-pass checkboxes are accepted, if passes exist;
- durable project-wide knowledge established by the work has been folded into its canonical repository location when needed;
- temporary implementation chronology remains in Issue/Git history rather than being copied into canonical knowledge;
- final commits and verification are identifiable.

## Source-of-truth roles during execution

Use these roles without replacing repository-specific context:

- canonical project knowledge — durable project-wide rules and architecture;
- Issue body — stable scope and accepted contract;
- active Issue comments — current implementation/review workspace;
- accepted summary — compact durable record of an accepted Issue or pass;
- Git history — exact change history.

Do not turn the Issue body into a diary.
