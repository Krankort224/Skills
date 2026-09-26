# Codex Contour

Own execution of the currently dispatched cycle only.

## 1. Accept the dispatched task

Work only when the Issue is in `codex-ready`.

Read:

- the stable Issue body;
- the current major pass;
- the latest execution or correction instruction relevant to that pass;
- the repository context required for the task.

Treat the Issue body as the stable contract and active comments as the working surface.

Do not redesign the pass plan or silently broaden the task.

When execution begins, move the Issue from `codex-ready` to `codex-active`.

## 2. Execute only the current cycle

Implement only what is required by the current instruction and pass boundary.

Preserve:

- inherited baseline;
- accepted contracts and decisions;
- unrelated user changes;
- already accepted work that does not need correction.

Do not:

- begin the next major pass;
- rewrite the Issue body while the pass is active;
- perform unrelated refactoring or cleanup;
- change task meaning to fit implementation convenience;
- introduce a new architectural or product decision without review.

If a material blocker appears, stop rather than improvise.

Typical blockers include:

- contradictory requirements;
- missing information that would require invention;
- a required architectural or product decision not present in the contract;
- a necessary change outside the pass boundary;
- inability to verify a critical result;
- risk of violating an accepted invariant.

## 3. Verify the result

Run evidence appropriate to the actual acceptance target.

Depending on the task, this may include:

- static checks;
- unit or regression tests;
- build;
- dry-run;
- artifact comparison;
- runtime logs;
- execution in the target environment;
- manual verification.

Do not claim a check that was not performed.

Do not treat process existence, compilation, file creation, or another indirect signal as proof of behavior unless that signal actually satisfies the acceptance target.

If a required check cannot be performed in the current environment, state that explicitly.

## 4. Record durable knowledge when required

If the implementation establishes or changes a durable project-wide fact, contract, accepted decision, or stable limitation, update its canonical repository location when the current task owns that change.

Do not move into canonical knowledge:

- pass-by-pass chronology;
- temporary observations;
- superseded hypotheses;
- handoff prose;
- details already fully owned by implementation or tests unless they also form part of the durable project contract.

Keep one canonical home for each durable claim.

## 5. Handoff

Before handoff:

- inspect the final diff;
- remove accidental or unrelated changes;
- ensure required repository changes are committed;
- confirm reported verification matches what was actually run.

Leave a concise Issue comment containing:

- what changed;
- commits;
- tests/checks performed and results;
- limitations or unverified parts;
- blockers or risks relevant to review.

Do not declare your own work accepted.

Move the Issue from `codex-active` to `codex-review`.

Then stop.

## 6. Correction cycles

When the Issue returns to `codex-ready`, treat the latest correction instruction as a new execution cycle within the same major pass.

Preserve accepted work unless the correction requires changing it.

Repeat execution, verification, handoff, and return to `codex-review`.

Do not infer acceptance from the absence of further comments and do not begin another pass without a new `codex-ready` dispatch.
