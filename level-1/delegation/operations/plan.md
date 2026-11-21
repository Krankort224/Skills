# Plan execution and assignments

Use before decomposing or materially changing an execution plan. Apply the [shared contract](../SKILL.md). Produce a sufficient plan on the current task surface, not a mandatory extra planning artifact.

## Establish the work and available means

Identify the intended result, current execution unit, relevant source revision, preserved decisions, owners, allowed changes and completion evidence. Distinguish unknown inputs from decisions already delegated to the executor. Resolve material missing inputs directly or through bounded exploration before dependent work; a fully specified mechanical task needs no extra exploration cycle.

Check only the environment facts needed for this assignment:

- whether child tasks can actually be created and whether they may be used here;
- whether a child's model is selectable per launch, chosen through configured routes, fixed, inherited or unknown;
- what context, tools, source access and writable locations the child will receive;
- whether children can create descendants, and available depth/concurrency limits;
- how completion, partial results, continuation and cancellation are exposed.

Use observed tool contracts and current configuration, with an applicable runtime reference as supporting guidance. Do not equate a provider's catalog with a configured pool, infer access from the parent's access, or require a full environment audit for a simple task. If a needed fact is unknown, bound the assignment to established capabilities or resolve that fact before dependent execution.

## Choose useful units

Compare direct execution with delegation using the task's uncertainty, coupling, context volume, benefit of independent checking and expected cost of instructions, duplicated reading, integration and retries. More agents do not automatically reduce elapsed time or improve evidence.

Select units that have identifiable inputs, a coherent output, clear ownership and a usable check. Mark dependencies between units; run only ready independent units concurrently. Keep closely coupled decisions with an owner who can see the necessary evidence. Do not separate work merely by file count or by labels such as research/execution/review.

For each planned unit establish its parent, goal, inputs/source pin, dependencies, executor/model choice where selectable, write scope, expected output, checker and spawning rights. The main agent approves material changes to its tree within existing task authority; this is not a new user approval ceremony. Announce assignments, their model or route when known, and the reason for the choice. Announce material tree changes, including a changed depth limit, even when no new assignment is created. Keep these updates concise and distinguish an unknown effective model from a requested one.

## Select an executor

1. Derive the requirements: tools, source access, modality, context size, uncertainty, interdependence and judgment. Distinguish a hard requirement from a preference.
2. Intersect available choices with user/project allowlists and assignment permissions. Preserve a fixed or inherited model when that is the supported route; do not request an unavailable override.
3. Apply a relevant model table within its declared scope. The [OpenAI pool](../references/models/openai.md) supplies that pool's recommendations; other authorized pools need not adopt its identifiers or tiers.
4. Choose a sufficiently capable allowed executor with proportionate effort and coordination cost. Effort names and model aliases are runtime-specific. A cheaper model that needs repeated repair may be a poor choice; stronger judgment does not repair missing tools or facts.
5. If the preferred option is unavailable, select an allowed adequate alternative, reframe the work, or let the parent execute when it can meet the requirements. Keep a genuine capability or required-check gap explicit.

Research, implementation, verification and coordination may each require different levels of judgment in different tasks. Do not classify an unfamiliar model by its brand or assume that a tier measured for one workload applies to another. Preserve the user's main-agent choice; needing another capability does not authorize changing that agent or configuring another provider.

## Bound the tree and writes

Count the main agent as depth 0. Retain a default maximum depth of 2 unless the existing task or runtime imposes a tighter limit. The main agent may approve a different plan for justified decomposition within actual runtime and user limits. Never silently raise a technical or user-imposed limit.

Grant descendant dispatch only when the participant is assigned that responsibility, the runtime supports it, the proposed descendants fit the approved tree and remaining capacity, and permissions are preserved. With no grant, the worker returns a need for delegation to its parent. Model tiers do not grant this right. A high-capability executor may be a leaf at any allowed depth.

Set concurrency from ready independent work and actual available capacity, accounting for active participants. Do not hardcode a session-specific slot count into the method. Check the actual tree when it is observable; disclose an unverifiable material limit rather than claiming enforcement.

Establish one active writer per shared artifact/area. Separate tasks by write scope or serialize them. Use only an already authorized isolation mechanism; a separate context or worktree does not authorize a new branch or merge. If independence is required for a check, preserve a non-author checker and give it raw evidence and criteria rather than the author's desired conclusion.

Dispatch through [dispatch](dispatch.md). If decomposition depends on missing evidence, assign only the bounded exploration that can resolve it, then revise the dependent plan.
