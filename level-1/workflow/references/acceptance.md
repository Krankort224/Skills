# Acceptance

Own result review, authorized acceptance, and completion.

Sections: [Review](#1-review-the-execution-handoff) · [Outcome](#2-review-outcome) · [Acceptance](#3-accept-the-current-execution-unit) · [Consolidation](#4-summarize-and-delete-intermediate-comments) · [Completion](#5-complete-the-issue).

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
- verify the summary and delete the intermediate comments it replaces as specified below;
- verify the overall Result boundary;
- close the Issue only when closure is authorized.

### Multi-pass Issue

When a major pass is accepted:

1. mark its top-level checkbox complete;
2. set its pass status to `accepted`;
3. replace provisional planned decomposition with the actual **Final decomposition**;
4. replace provisional acceptance material with the **Accepted result**;
5. record the **Boundary carried forward**;
6. write one durable accepted summary comment;
7. record the final commit and accepted-summary reference;
8. verify the summary and delete the intermediate comments it replaces as specified below.

The accepted pass section should describe what the pass finally became, not preserve obsolete forecasts.

Do not begin the next major pass until the current one is accepted.

## 4. Summarize and delete intermediate comments

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

For both simple and multi-pass Issues, complete consolidation in this order:

1. Identify the completed unit's intermediate comments, including execution instructions, handoffs, review findings, and correction cycles.
2. Publish the accepted summary, carrying forward all decisions, constraints, unresolved items, and verification evidence needed after consolidation. Use durable evidence references rather than links to comments scheduled for deletion.
3. Read back the published summary and updated Issue body. Verify their coverage against the comments to be removed and repair references to those comments.
4. Delete the intermediate comments replaced by the verified summary. Preserve accepted summaries from other units and comments still needed for active or future work; first carry forward any necessary information from mixed-purpose comments.
5. Fetch the remaining comments and verify that the intended comments were deleted and retained summaries and active-work context remain intact.

Deletion is a required part of consolidation, not optional tidying. Do not leave intermediate comments in place merely because a summary now exists, hide or minimize them as a substitute, or create a parallel transcript/archive to preserve the same clutter. Git retains exact code changes; the summary retains the useful outcome.

If the current environment has no comment-deletion tool, keep the verified summary and record pending cleanup: the completed unit, summary reference, exact comment identifiers to delete, and references or information that must survive. Carry this work into stage 0 of the next pass through its execution dispatch. The pass may remain accepted while cleanup is pending; consolidation remains incomplete until deletion is verified. Bundle stages 0 and 1 in one execution cycle, with no intermediate manual review or separate dispatch.

If deletion fails, report the failure and remaining identifiers rather than claiming success. If there is no next pass, report the outstanding cleanup; do not invent a pass or claim final consolidation is complete.

## 5. Complete the Issue

A simple Issue is eligible for closure when its Result boundary is accepted.

A multi-pass Issue is eligible for closure only when all major passes and the overall Result boundary are accepted.

Before final completion, verify that:

- the final Issue body matches the accepted work;
- all required major-pass checkboxes are accepted, if passes exist;
- durable project-wide knowledge established by the work has been folded into its canonical repository location when needed;
- completed units' intermediate comments have been deleted after verified summaries replaced them;
- temporary implementation chronology has not been copied into canonical knowledge;
- final commits and verification are identifiable.
