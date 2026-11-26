---
name: arbitration
description: Keep the user's goal across sessions, choose an owner for subject work, review each outgoing assignment, adjudicate findings and assess readiness. Use for Codex dot or an assigned arbiter, and for independently addressed specialist contributions.
---

# Arbitration

Start from the user's actual task and the authority already granted. The user retains the objective, ordering, material tradeoffs, additional permissions and acceptance unless a specific decision was explicitly assigned. Reading this method grants no coordination mandate, write authority or access. A person or agent receiving a direct task may own that task without acquiring authority over a wider project.

## Start an arbiter turn

When the user requires this skill each turn, resolve the current commit of `Krankort224/Skills` immediately before reading it, even in a continuing session. Use an available equivalent system reader or the verified [bundled reader](scripts/read_skill.py). On first use without a known reader, resolve `refs/heads/main` through Git or an authorized GitHub connector, then read `level-0/arbitration/SKILL.md` at that exact commit. A preloaded manifest can locate the package. Verify the bytes used before applying it. Take dependent documents and scripts for the same reading from the same commit. At a later fresh reading, resolve again; preserve any version the user explicitly required.

Keep the original user request and its source, later user amendments in order, allowed effects, promised result, acceptance criteria and outstanding owners recoverable. A worker's summary can report progress. Return to the user's words before assigning new work. Read only the evidence needed for a routing, correction or readiness decision.

## Choose the owner

The arbiter owns context across sessions, decisions within its grant and the return to the user. Give subject execution, tool-heavy investigation, authoring, subject checks and corrections to a worker. The arbiter can recover sources, check its assignments, contact owners, inspect compact evidence and report or stop work.

An internal child suffices when a single bounded assignment can return a checkable result inside this session, the child has the inputs and access, and compact evidence lets the arbiter judge completion without taking over the execution history. For example, a child can identify the rows explaining a discrepancy even in a large table. Use an existing authorized, independently addressable specialist or minion when dependent stages, later intake, corrections or resumption need a continuing owner. A one-line fix in that owner's ongoing work stays with them. Preserve required non-author checks in either arrangement. If the necessary owner is unavailable, report the affected work and continue separable coordination within existing grants.

## Review each outgoing assignment

Before issuing work as arbiter to **either** a minion or an internal child, use the available equivalent system tool or the [bundled assignment reviewer](scripts/review_assignment.py). This also applies to review requests, corrections and instructions to resume or extend work. Reading status, collecting a finished result, replying to the user and stopping a writer do not assign work. Dispatch alone never triggers a skill freshness lookup.

1. Present the original user text, subsequent user amendments, the intended recipient and the exact proposed instruction. Use the original source or a verified copy after a handoff. A missing source keeps dependent work pending.
2. Inspect that packet. Explain which requested outcome the contribution serves, the result/evidence to return, and whether the proposed effects and criteria fit the user's grant. Decide `send` or `revise`. On drift, withhold the draft, correct it and repeat the review; involve the user only for a genuinely reserved decision.
3. Send only the reviewed assignment to its reviewed recipient after confirmation. Keep the other material inside the arbiter's context unless the worker needs it and may receive it. Recheck a changed packet and each separate work order. The tool binds the comparison to its inputs; the arbiter owns semantic judgment and the actual send. If neither implementation is available, name the blocked assignment.

See [tool invocation and availability](references/tools.md) for the standalone and system interfaces.

## Select the route

| Current need | Route |
| --- | --- |
| Receive, assign, continue or collect a bounded contribution | Apply the assignment and continuation contract below. |
| Organize work as Codex dot | [Codex dot](references/codex-dot.md), including category, stage roles and session decisions when relevant. |
| Receive or coordinate work as a Hermes specialist | [Hermes](references/hermes.md), including peer consultation within existing grants. |
| Resolve a finding or a material disagreement | [Adjudicate](references/adjudicate.md). |
| Decide whether an agreed result is ready or identify its unmet gate | [Assess readiness](references/assess-readiness.md). |

Select by the participant arrangement actually in use. An independently addressable participant has a usable request and return route of its own. A child managed inside someone else's execution context is an implementation detail of that participant's contribution. Its owner supplies the result and remains accountable for its effects. A permitted internal child may supply independent checking when its authorship, inputs, access and evidence support that check.

## Make and receive a bounded assignment

Confirm the objective, authoritative task sources, live state, permissions, preserved decisions and any actual budget relevant to the request. A recipient assigned execution may complete its own contribution directly. The arbiter chooses the owner as above. Prefer a direct authorized route over an extra relay.

Supply the recipient with what they need for the work:

- Requester, accountable owner of the overall result, contribution owner and named owner of any reserved decision.
- Outcome and sufficiency criteria, current boundary and dependencies, material constraints and decisions to preserve.
- Relevant context, accessible authoritative inputs and their exact revisions, expected artifact or fixed result revision and who needs access. State any task-required method, its pinned source and selected resources with an explicit instruction to read and apply them. Preserve those instructions when handing work onward.
- Permitted effects such as reading, editing a named area, contacting a particular party, publishing or spending. Verify both access and authority. Technical reachability, a role label or the ability to ask someone does not add a grant.
- Checker when required, evidence to return, and the return point or checkpoint. Give an independent checker the agreed criteria, raw artifacts and factual observations. Keep author diagnoses and expected findings out of the initial request. Clarify facts after the independent assessment when needed.

An assignment transfers responsibility for its contribution. The overall owner retains integration, the promise to the requester, and actions reserved to that owner. Keep one active writer per changed area and serialize shared writes. Respect source and effect restrictions when forwarding. If authority or capabilities are missing, identify the affected action and pursue separable authorized work.

Return the usable result or partial result, its fixed identity and source pointers, actual checks and limitations, any outstanding writer or decision, and the next action. Distinguish what a recipient was instructed to use from what they actually read, applied and verified. Capture the compact record on the existing task surface when others need it to continue.

## Recover an interrupted assignment

Recover the live task, latest applicable instructions and exact method/source revisions from accessible authoritative records. Check for newer decisions or changed artifacts before dependent work. Recover the current unit and scope, owners, open findings and correction history, prior grants, active or queued work, and next checkpoint. Confirm what is readable in the receiving context. Publication, an old summary and a memory pointer alone cannot establish live state, method use or authority. Preserve the current unit, history and scope. Report missing state and continue supported independent work.

Before retrying an interrupted or uncertain action, determine what landed and what may still run. Preserve useful partial work. A timed-out, disconnected or paused writer may still write through a queued retry, background work or automatic resumption. Before transferring overlapping write scope or relying on that area as settled, obtain evidence that the previous writer completed, was stopped with confirmation or can no longer affect the area through an authorized arrangement. For a denied action, record the affected target and reason. Retry only within its authorization and through a permitted route. Keep an unresolved writer visible as a blocker for dependent work. Replace an unavailable participant only within existing authority and keep the writer and checker responsibilities separate.

When maintaining the source checkout, use its [common](tests/common.md), [Codex dot](tests/codex-dot.md) and [Hermes](tests/hermes.md) decision cases as applicable.
