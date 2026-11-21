---
name: delegation
description: Plan execution, assign work to available agents, pass task context, recover interrupted work, and verify combined results across models and execution environments. Every agent reads this contract; use its operations only for the current assignment.
---

# Delegation

Distribute work within the current task and applicable permissions. Preserve accepted results, unrelated changes and the user's choice of the main agent. Reading this contract does not start an agent tree, Issue lifecycle, installation or publication.

## Shared contract

- Distinguish the **assignment/role**, **model suitability**, **runtime capability**, and **permission**. A model name or tier proves neither tool access nor spawning rights. A tool being available does not expand the assignment.
- Delegate when independent work, context reduction or required verification justifies the coordination and checking cost. Perform small or tightly sequential work directly. If delegation is unavailable, continue work the current executor can complete with the task's required checks; disclose any remaining capability or mandatory independent-review gap.
- The main agent owns its execution plan, integration and final delivery within the assigned process. An ordinary root is at **depth 0**, not automatically an arbitration role. Preserve established area writers/checkers and operation owners.
- Give every participant an explicit goal, source/revision, constraints, permissions, expected result and checks. Enumerate required skills, exact source pins, selected operations/resources and the instruction to **read and apply** them. A parent's reading or inherited conversation does not establish a worker's use.
- Preserve these instructions, role boundaries, useful progress and open findings through continuation, replacement and descendant assignments. Supply critical requirements directly and source pointers the recipient can actually access.
- Assign spawning rights and tree limits explicitly. Check actual runtime capacity and applicable restrictions before dispatch. Keep concurrent writes disjoint; serialize shared-file changes. Context isolation does not imply filesystem isolation.
- Diagnose failures before changing executors. Stronger models do not supply missing inputs, tools or permissions. Do not repeat a failed attempt under unchanged conditions.
- Check direct-child outputs against their assignments and evidence; check combined coverage and integration before final delivery. Self-check is not independent review where a non-author check is required. Account for every launched participant and outstanding execution.

## Select the operation

Start at the current action and reuse sufficient existing evidence; these are not mandatory sequential phases.

| Current need | Operation |
| --- | --- |
| Decide how to execute, decompose work, select executors and bound the tree | [plan](operations/plan.md) |
| Prepare an assignment, start or continue work, and follow progress | [dispatch](operations/dispatch.md) |
| Diagnose a failure or stall, replace an executor, replan or cancel | [recover](operations/recover.md) |
| Check contributions, combine results and finish execution | [integrate](operations/integrate.md) |

## Load only applicable references

For model selection, use the actual authorized candidate set and the matching reference when available. The [OpenAI pool](references/models/openai.md) owns that pool's concrete mappings and selection policy. It is not a universal provider catalog. A missing model table does not prohibit an otherwise authorized executor or justify inventing a model ranking.

For interface-specific actions, select a profile by the tools and environment actually present:

- [OpenAI collaboration interface](references/runtimes/openai-collaboration.md): the named agent-management surface, not all OpenAI products.
- [Kimi Code CLI](references/runtimes/kimi-code.md): configured subagent types and model routing.
- [Hermes Agent](references/runtimes/hermes.md): default delegation and configured strategy variants.

Check each profile's scope and evidence status. Live tool schemas, observed configuration and applicable permissions govern an actual invocation; documentation or a stale profile cannot grant a missing feature. An unfamiliar environment can use these operations through its exposed tools without a prewritten adapter. Report material unknowns and continue supported work. Do not install or reconfigure an environment merely to match a reference.

## Result and continuity

Use this compact return contract, with only assignment-relevant detail:

`status: done|partial|blocked|error|cancelled; result; files/artifacts; sources/revision; evidence; checks/results; remaining; cause; next_action`.

Identify skills/revisions actually read, evidence of their material application, and missing sources or unperformed steps. An acknowledgement alone is not compliance evidence. Return conclusions and source pointers rather than full transcripts.

Checkpoint accepted contributions, active agent/task identifiers, dependencies, owners and pending work on the existing task surface when continuity requires it. Keep canonical knowledge with its owner. Context owns source authority; workflow owns applicable Issue lifecycle and acceptance; assigned arbitration owns coordination/adjudication; learning owns evidence-based method improvement. Delegation adds none of those roles or permissions.

Use [decision scenarios](tests/scenarios.md) when checking changes to this method. They are evaluation material, not a checklist to run on every task.
