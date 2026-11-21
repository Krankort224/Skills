# Diagnose and recover work

Use when an assignment fails, stalls, loses context or no longer fits its inputs. Apply the [shared contract](../SKILL.md). Recover within the current task and permissions; do not reset accepted decisions, roles, findings or correction history.

## Establish the current state

Identify the task/agent, last material progress, current artifacts and revision, actual checks, open dependencies and whether any process can still change the assigned area. Obtain an interim report where possible. Distinguish launch refusal, active work, completed-but-insufficient output, timeout and confirmed cancellation; a missing report is not proof the worker stopped.

Preserve useful results and evidence before replacing or cancelling work. Do not discard partial output merely because the overall assignment failed, and do not adopt it without checking the requirements it actually supports.

## Diagnose before choosing a remedy

| Cause supported by evidence | Proportionate remedy |
| --- | --- |
| Missing or misunderstood context | Supply the discriminating source/requirement and a bounded continuation |
| Material requirement conflict or decision beyond the worker's authority | Return the decision to its owner; suspend only dependent execution |
| Missing access, tool, permission or modality | Use an authorized capable executor/route if available, or report the exact gap |
| Work too coupled for the decomposition | Reunite dependent decisions or reshape units and checks |
| Insufficient model/executor capability for a well-defined task | Select a suitable allowed alternative through planning |
| Execution error or insufficient verification | Assign the concrete correction/check with a closure criterion |
| Stalled or repetitive progress | Obtain partial results, change the failing conditions, then continue, replace or cancel |

Several causes may coexist. Change only what the diagnosis warrants. A stronger model cannot supply a missing source or authority, and a larger context does not resolve contradictory requirements. Do not require a fixed progression through model tiers, retry counts or tree levels.

## Respect dependencies and active ownership

Inspect whether unfinished siblings supply missing inputs, affect shared artifacts or are needed to establish the cause. Wait for those dependencies, or explicitly replan them, before affected recovery. Independent siblings can continue; their existence alone does not require postponing recovery of another branch.

Before transferring a write scope, establish that its former owner and relevant background work have stopped or finished, with no queued retry or automatic resumption that can write again. A limit-stopped, paused or waiting-to-resume participant can still hold active ownership. Use the exposed lifecycle controls to settle that pending execution and verify the resulting state; a terminal-looking attempt alone may not settle the whole task. If cancellation is unavailable or cannot be confirmed, do not start an overlapping replacement. Continue disjoint work and report the unresolved ownership condition. A cancellation request is not confirmation.

Cancel obsolete or dependency-invalidated work when authorized and technically possible. Preserve a cancellation record with cause and useful results. Handle late reports against their task/input revision; reject or revalidate obsolete conclusions rather than silently merging them into the current result.

The parent can complete the work itself only when it has the capability, authority and required checks. Preserve any assigned non-author review boundary. Escalate an unresolved requirement or ownership decision upward; do not bypass it by relabelling the task, role or stage.

## Continue or replace

Give a replacement the explicit [dispatch package](dispatch.md#prepare-an-accessible-task-package), including required skills and exact pins, scope/permissions, original requirements, preserved decisions, usable progress, checks, failure cause, open findings and next action. State which conditions changed and what observable result would resolve the failure.

Replacements and descendants obey the existing tree/model/runtime restrictions. The main agent approves material tree changes within its authority. An unavailable model does not authorize switching providers, changing configuration or inventing an alias.

On context loss, reconstruct the current task, roles, agent identifiers, dependencies, source/artifact revisions, accepted contributions, permissions and pending work from durable task records and live evidence. Verify material changes before continuing; do not silently restart completed work or treat an old summary as current execution state.

Report the outcome as completed recovery, partial/blocked continuation, or confirmed cancellation with its evidence. Do not claim the original task is complete merely because a replacement launched. Return the recovered contribution to [integration](integrate.md).
