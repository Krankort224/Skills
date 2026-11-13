# Evidence and scope

Use this decision contract when a meaningful episode could justify improving a skill. Stop at no change when no method gap remains; it is a valid learning outcome.

## Establish what happened

Identify only what the decision needs:

- The task, intended result and applicable constraints, with source pointers.
- The skill/operation and exact revision actually read; distinguish the prescribed method from actions actually taken.
- Relevant inputs, conditions and observed output/error or successful result. Separate source facts, observations, interpretations and unperformed checks.
- A plausible cause, competing explanations, and the evidence that distinguishes them.

Reuse artifacts, checks and task records already available. Do not harvest a whole transcript or record every tool call. A correction identifies a signal, not necessarily a reusable rule; an uncommon success needs evidence of what worked and under which conditions. Do not present a synthetic example or a source's claimed result as a runtime you observed.

If material evidence is missing, name the smallest useful check and its access/runtime needs. Perform it only within existing authority. If unavailable, report the missing evidence and its consequence; do not invent a cause or replace an unavailable native test with a claim of success.

## Diagnose the cause and owner

Use the established `context` decisions for owners and source authority. These categories guide diagnosis rather than creating mutually exclusive labels:

| Cause | Discriminating question | Supported disposition |
| --- | --- | --- |
| Execution error | Did the agent omit, misapply or contradict an adequate applicable instruction? | Correct the task execution. A method edit needs separate evidence that the instruction itself needs improvement. |
| Context/access gap | Was a necessary fact, source, permission, input or runtime absent, stale or unread? | Retrieve/verify it or report the gap. Missing access is not proof of a method defect. |
| Navigation gap | Was the necessary knowledge adequate but unreachable, misrouted or undiscoverable on the applicable path? | Propose a bounded correction to the owning route if evidenced and authorized; retain adequate method content. |
| Project-specific fact | Is this a local constraint, source binding, accepted choice or configuration rather than a transferable method? | Keep it at the existing project owner through an authorized update or proposal. Do not generalize its value or paths. |
| Reusable method gap | Does following the applicable method still fail, omit a necessary branch or miss a demonstrably useful technique under identifiable conditions? | Prepare a candidate at the method owner, with scope, exclusions and behavioral checks. |

For example, a missing environment profile can explain a failure while a broken route to the profile explains why it was missed. Resolve both at their owners without concluding that the API method is wrong. If the current skill already contains the useful technique, finding it late is not evidence for duplicating it elsewhere.

## Justify the scope

A candidate needs a causal account: **under these conditions, this method change should produce this improvement while preserving these behaviors**. Identify the conditions that made the episode informative and the cases where the proposed change would be wrong or unnecessary.

One validated exceptional input can expose a missing branch in a method that promises to handle that input class. It can support a narrow candidate before use in another project. Do not demand an arbitrary occurrence count or claim all-project validity from that case. Conversely, repeating a local convention across several repositories does not make it universal.

Separate the transferable procedure from local values, paths, preferences and permissions. An observed project rule stays local unless evidence supports a distinct reusable abstraction. Verify applicability at its owner; neither recency nor a generic label such as “best practice” establishes it.

Evidence is sufficient **for the proposed decision**, not for every later claim. An input/output counterexample and source inspection may justify trying a candidate; they do not establish the candidate's improvement, transfer or native-runtime correctness. A successful workaround alone does not prove its suspected cause. Record the missing discriminating evidence when alternatives materially affect the refinement.

## Candidate, result and acceptance

Before substantive refinement, make the proposal reviewable on the existing task surface:

`hypothesis/expected gain; source evidence + method revision; applicability/exclusions; owner/destination; protected behavior; planned original + transfer/boundary + affected-regression checks; current authority and missing evidence`.

This is a compact decision record, not a mandatory new file or second Issue contract. Use the existing task format where available. If the proposed destination is not writable under current authorization, return the proposal rather than writing elsewhere to bypass that boundary.

Keep the following distinctions visible without introducing a second task lifecycle:

| Evidence/authority available | What may be claimed |
| --- | --- |
| No significant new signal or an adequate method was merely misapplied | No skill change is warranted by this episode. Correcting execution can still be necessary. |
| Supported candidate, no authority to change its owner | Proposal only; identify the owner, intended check and needed authority. |
| Plausible candidate, unresolved material cause/scope/check | Deferred pending named evidence or capability; neither failed nor verified by assumption. |
| Candidate exercised against identified cases | Tested candidate, with actual outputs, failures and coverage limits; not accepted merely because tested. |
| Candidate fails the required behavior or regresses protected behavior | Correct and recheck, or roll back its changes. Preserve unrelated edits and earlier evidence. |
| Required evidence supports readiness | Present under the task's existing acceptance authority; do not infer acceptance or create extra approval gates. |

Acceptance belongs to the governing task process. For an Issue, use `workflow`; where arbitration is assigned, send findings and evidence to that arbiter. After authorized acceptance, integrate the reusable method at its canonical owner and retain outcome/provenance through established records. Keep transient rejected hypotheses out of shared roots. Reuse existing accepted summaries rather than copying them into a learning ledger.
