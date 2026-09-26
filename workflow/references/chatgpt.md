# ChatGPT Contour

Own task definition, execution dispatch, review, acceptance, and progression between major passes.

## 1. Define the Issue

When creating or substantially restructuring an Issue, make the body a stable contract rather than a work log.

Include only what is useful across the whole implementation cycle:

- **Goal** — the finished result of the whole Issue;
- **Result boundary** — high-level Definition of Done;
- **Inherited baseline** — accepted foundations that must not be silently redesigned;
- **Scope / Out of scope**;
- **Pass plan** — major passes only;
- for each pass:
  - purpose;
  - planned decomposition when useful;
  - initial boundary;
  - acceptance target.

The top-level checklist contains only major passes. A checked item means the whole pass has been accepted.

The first unchecked major pass is the current pass.

Planned sub-passes are forecasts, not promises. Do not continuously rewrite the Issue body when they split, merge, disappear, or change during execution.

## 2. Prepare the current pass for execution

Before sending work to Codex:

- select only the current major pass;
- read the current Issue body and relevant active comments;
- determine the concrete instruction for the next execution cycle;
- preserve the pass boundary and inherited baseline;
- do not silently introduce a new architectural or product decision;
- define what evidence will be sufficient for review.

If the task is contradictory, materially underspecified, or requires a new decision outside the accepted contract, resolve that in Chat before dispatch rather than asking Codex to improvise.

When the execution instruction is ready, set the Issue to `codex-ready`.

### Execution recommendation to the user

After preparing the task and setting `codex-ready`, report the execution recommendation **in Chat**, separately from the Issue content.

Use:

- **Environment:** the execution surface, such as local Codex, cloud/Work, or another explicitly available environment;
- **Model:** the recommended model;
- **Reasoning:** the recommended reasoning level;
- **Why:** one short explanation tied to the actual task.

Example:

```text
Issue prepared and moved to codex-ready.

Execution recommendation:
- Environment: local Codex
- Model: Terra
- Reasoning: High
- Why: implementation and regression work across several related modules.
```

Do **not** add this recommendation to the Issue body or GitHub comments unless the user explicitly asks for it there.

Treat the recommendation as advice to the user, not part of the task contract.

## 3. Review Codex handoff

When Codex moves the Issue to `codex-review`, review the result against the current pass contract.

Check:

1. the original pass purpose and boundary;
2. acceptance target;
3. actual commits and diff;
4. reported tests, runtime checks, or other evidence;
5. project contracts and accepted decisions;
6. unintended or out-of-scope changes;
7. limitations, risks, and unverified claims.

Inspect the evidence needed to verify material claims rather than relying only on the handoff summary.

Review defects-first: identify incorrect behavior, missing acceptance criteria, regressions, unsupported claims, or scope violations before discussing stylistic improvements.

Do not redefine the task to fit the implementation that happened.

## 4. Correction cycle

If the pass is not acceptable:

- state the concrete review findings in an Issue comment;
- specify the correction needed for the current pass;
- keep the Issue body unchanged;
- preserve accepted parts of the current implementation unless they genuinely need revision;
- set the Issue back to `codex-ready`.

Then report a fresh execution recommendation to the user in Chat. The recommended environment, model, or reasoning level may differ from the previous cycle.

Repeat:

`instruction → Codex handoff → ChatGPT review → correction`

as many times as necessary.

## 5. Accept the pass

When the major pass is accepted as a whole:

1. mark its top-level checkbox complete;
2. set its pass status to `accepted`;
3. replace the provisional planned decomposition with the actual **Final decomposition**;
4. replace provisional acceptance material with the **Accepted result**;
5. record the **Boundary carried forward**;
6. record the final commit and canonical pass-summary reference;
7. write one durable accepted-pass summary comment;
8. remove or supersede working-comment clutter only according to the repository's supported cleanup method.

The accepted pass section should describe what the pass finally became, not preserve obsolete forecasts.

## 6. Accepted-pass summary

Preserve only durable information that remains useful after the implementation conversation is over.

Include when relevant:

- problems found;
- root causes;
- corrections and accepted decisions;
- rejected approaches that should not be casually reintroduced;
- final verification;
- final commit;
- accepted baseline.

Omit empty sections.

Do not turn the summary into a chronological replay of the active comments.

## 7. Progress to the next pass

Do not begin the next major pass until the current one is accepted.

After acceptance, the next unchecked major pass becomes current.

Prepare its concrete execution instruction and repeat the dispatch process.

## 8. Complete the Issue

The Issue is complete only when all major passes and the overall result boundary are accepted.

Before final completion, verify that:

- all top-level pass checkboxes are accepted;
- the final Issue body matches the actual accepted work;
- durable project-wide knowledge established by the work has been folded into its canonical repository location when needed;
- temporary implementation chronology remains in Issue/Git history rather than being copied into canonical knowledge;
- final commits and verification are identifiable.

## Source-of-truth roles during execution

Use this hierarchy by role, not as a substitute for repository-specific context:

- canonical project knowledge — durable project-wide rules and architecture;
- Issue body — scope, pass map, and accepted pass contracts;
- active Issue comments — current implementation/review workspace;
- accepted pass summary — compact durable record of the accepted pass;
- Git history — exact change history.

Do not turn the Issue body into a diary.
