# Adjudicating findings

## Establish the claim

For each material finding, record in the existing review work surface:

`ID; requirement/source; observed deviation; consequence; evidence + reviewed revision; decision + grounds; closure condition`.

Use a stable identifier through corrections. Separate observation from inference and an unperformed check from a failed check. Evidence can be a reproducible behavior, inspected artifact, authoritative contract, or required verification result. An executor's assurance alone does not establish compliance.

## Choose a disposition

| Decision | Basis | Next action |
|---|---|---|
| Correct | Supported contract violation, regression, or missing required result | Specify the bounded change and evidence needed to close it. |
| Investigate | Consequential claim with insufficient or conflicting evidence | Define one discriminating check, its inputs, evidence target, and stopping condition. |
| Reject with grounds | Authoritative evidence contradicts the claim, or the requested change is an unsupported preference | Retain the evidence and reason; do not dismiss a substantive claim on confidence alone. |
| Propose separately | Useful improvement outside the agreement | Offer it without adding an Issue, changing its order, or blocking an otherwise sufficient result. |
| Escalate | Resolution requires a user-owned decision, material compromise, or authority/capability unavailable after bounded diagnosis | Present concrete options, consequences, evidence, and a recommendation. |

The executor may explain or challenge a finding; the reviewer may respond with evidence. If disagreement remains, dot decides what evidence resolves it or identifies the decision outside its authority. Do not substitute repeated argument or another agent's vote for that evidence. Preserve uncertainty when no decisive check is available.

A serious possible defect with incomplete evidence calls for investigation or a disclosed blocker, not automatic rejection or acceptance. Treat a missing mandatory check as an evidence gap even when the implementation looks plausible.

## Dispatch and resolve corrections

Combine compatible corrections into one actionable package. Preserve accepted behavior and unrelated work. Specify closure conditions by behavior or evidence, leaving implementation choices free where the contract permits.

At the new revision, inspect the corrected behavior and affected dependencies. A fix can create a regression elsewhere; a finding is not closed merely because a line changed or an executor marked it done. Identify what prior verification remains applicable and rerun checks invalidated by the changes.

Keep materially unresolved findings open. Record a reasoned rejection or verified correction as a disposition rather than silently dropping it. Only propose a new goal, weaker criterion, or material compromise to the user; do not redefine success to match the existing implementation.

## Examples of judgment

- A reviewer demands a framework replacement but identifies no violated requirement: reject the blocking demand or propose the improvement separately.
- An executor reports success while a required runtime check was not run: obtain the check or disclose the evidence gap; do not report a pass.
- A reviewer alleges that four records were lost, but a source-backed comparison at the reviewed revision accounts for all records: reject with that evidence.
- Two correction cycles failed because checks used a stale fixture; the correct fixture is available and an authorized fix is clear: reassess, change the check, and continue. The cycle count alone is not a user decision.
- A correction resolves one criterion by removing another agreed behavior: require a compatible correction or present the real tradeoff to the user.

## Checkpoint outcome

At each progress reassessment, summarize the unresolved requirement, new evidence/progress, diagnosed cause, changed approach, and next observable checkpoint. Distinguish an ordinary fix from a limitation of the review arrangement. Changing modes does not cure an unclear specification or absent permission. Stop repeating a remedy that is not producing evidence or progress; retain useful partial results when blocked.
