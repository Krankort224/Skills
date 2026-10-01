---
name: delegation
description: Plan Codex execution, choose whether to delegate, and manage agent trees, context, recovery, and verification.
---

# Delegation

Stay within the current task/cycle. Preserve `context`, `workflow`, repository rules, accepted work, and unrelated changes.

## Models

Subagent model registry; update models only here:

| Type | Model |
|---|---|
| light | gpt-6-luna |
| main | gpt-6.1-sol |

Use only registry models for subagents; prevent incompatible inheritance. The light model never spawns agents, even as root. Select by task complexity, not role; use minimum reliable effort. If unavailable, let the parent execute or replan within this contract.

## Planning

User selects root. Root owns planning, coordination, integration, verification, and final delivery.

Root reads Issue/prompt and current instructions, applies `context`, then plans execution. Delegate substantial independent work, context-heavy research, or independent verification when benefits exceed coordination costs. Handle trivial/sequential work directly.

Root is level 0. Default maximum depth: 2. Root may increase depth for justified decomposition.

- Depth 1: light/main.
- Depth D≥2: levels 1…D−1 allow light/main; level D allows only light agents and easy tasks.
- Only main subagents may spawn descendants, within the root-approved tree.

Before spawning, define parents, tasks, models, dependencies, write scopes, and verification. Set concurrency by useful independent work and runtime limits. Announce assignments, models, and reasons. Root approves material tree changes, including depth; announce them without separate user approval within authorized scope.

Check actual tree composition/depth; enforce runtime restrictions where available.

## Context and execution

Each assignment includes goal/scope, decisions, inputs/source pointers, relevant revision, permissions/write scope, constraints, expected result, verification, and any spawning rights. Include critical requirements directly.

Default to task-specific context and `fork_turns=none` where supported. Inherit history only when needed and compatible with the model contract.

Workers reuse supplied context, reading sources directly and applying `context` only for missing task-relevant information. Fully specified mechanical work skips separate context loading, never repository rules. Avoid redundant reading; parents need not pre-read every source.

Never broaden scope. Keep concurrent writes disjoint; serialize shared-file edits. Do useful work while children run; avoid duplication/frequent polling. Reuse agents with matching context.

## Recovery

Diagnose first: context/specification, access/tools/permissions, size/complexity, execution/verification, or stalled progress. Resolve the cause or report a blocker; stronger models do not replace missing inputs/access.

- Failed light at level 1: root stops it and assigns main, transferring requirements, context, usable progress, checks, and failure cause.
- Failed light at level ≥2: parent awaits all other direct-child reports, then attempts completion itself; escalate upward if unsuccessful.
- Failed main: parent replans or completes the work.

Replacements must obey depth/model rules; tree changes require root approval.

Do not wait indefinitely. Track expected duration, new results, and repetitive non-progress. On deadline breach or clear stall, request an interim report, then replan/cancel. Treat cancellation as a report with cause and preserved partial results. Cancel obsolete or dependency-invalidated work. Never retry unchanged conditions.

## Reporting and closure

Return:
`status: done|partial|blocked|error|cancelled; result; files; sources/revision; evidence; checks/results; remaining; cause; next_action`.

Report conclusions and evidence pointers, not full transcripts. Never claim unperformed checks.

Parents verify direct-child scope compliance, material conclusions, changes, and checks without automatically repeating all research. Root verifies the combined result against the user task, including integration.

Checkpoint tree state, accepted results, and pending work for context-loss recovery; do not duplicate canonical project sources.

Before final delivery, account for every agent and finish/cancel outstanding execution. Report the overall result and material limitations.
