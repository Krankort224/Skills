# Acceptance

Own result review, authorized acceptance, and completion.

## 1. Review the execution handoff

When the Issue is in `codex-review`, review the result against the current execution unit.

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

## 2. Review outcome

If the current execution unit is not acceptable, report concrete findings in an Issue comment. Preserve the contract body and accepted parts. Prepare correction dispatch through the definition operation.

If review passes, report that result. Without explicit acceptance authorization, leave the unit unaccepted and the Issue in `codex-review`.

## 3. Accept the current execution unit

After the required review succeeds and acceptance is authorized, use `../templates/accepted-summary.md` for the durable accepted summary.

### Simple Issue

When the whole Issue is accepted:

- reconcile the body with the final accepted result if needed;
- write one durable accepted summary comment;
- verify the overall Result boundary;
- close the Issue only when closure is authorized.

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

## 4. Accepted summary

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

## 5. Complete the Issue

A simple Issue is eligible for closure when its Result boundary is accepted.

A multi-pass Issue is eligible for closure only when all major passes and the overall Result boundary are accepted.

Before final completion, verify that:

- the final Issue body matches the accepted work;
- all required major-pass checkboxes are accepted, if passes exist;
- durable project-wide knowledge established by the work has been folded into its canonical repository location when needed;
- temporary implementation chronology remains in Issue/Git history rather than being copied into canonical knowledge;
- final commits and verification are identifiable.
