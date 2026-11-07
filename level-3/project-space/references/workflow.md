# Projects, topics and task workflow

Read `docs/task-workflow.md`, task-relevant `docs/access-control.md` and the current `core/domain.rs` reducer. Then use [Publication and replay](publication.md). This mapping describes supported actions; it does not introduce new transitions or managerial overrides.

## Project and topic actions

| Result | Event and payload | Context |
| --- | --- | --- |
| Rename an existing project | `project.updated`: `{title}` | Project stream; project management and actual participation checks |
| Add/change participants or rights | Mutable registry transaction | [Configuration](configuration.md); no new access-grant events |
| Create a topic | `topic.created`: `{topic_id,title,status}` | New topic ID and stream, null own base; dependency on project creation |
| Rename a topic | `topic.updated`: `{topic_id,title}` | Current topic head |
| Set manual topic status | `topic.status_set`: `{topic_id,status}` | `active`, `waiting` or `completed`; independent of task statuses |

Topic changes require `topic.manage` or applicable inherited rights and current command-time domain membership checks. Never add participation/privileges as a side effect of a rename. New topics default to `active` when the request supplies no different status. `updated_at` is derived from accepted topic/task/material events, not an editable file timestamp.

Ordinary production project creation is currently disabled by `DenyNewProjects`, independently of Root and registry grants. For explicitly requested initial deployment use `docs/deployment.md` and its bounded operator plan. Do not bootstrap a second project, temporarily grant creation, patch authorization, or fabricate `project.created` to work around this gate. Topic/project deletion, archive, moving entities between projects/topics and reopening completed tasks are not defined current operations; preserve the data and state that limitation when requested.

## Task content and deadlines

Resolve a unique existing topic and a registered project participant as assignee. Current actor becomes the creator; creation time is automatic. `title` is required and nonblank. `description` is a string and may be empty/multiline. Every content version contains the complete title, description and deadline, including unchanged fields.

Deadline forms are closed objects:

- No deadline: `{"kind":"none"}`.
- Date precision: `{"kind":"date","value":"YYYY-MM-DD"}`; preserve the calendar date.
- Exact time: `{"kind":"instant","value":"...Z"}`; convert an explicitly understood local date/time to UTC. Clarify an ambiguous timezone rather than guessing.

Preserve an existing deadline unless the user changes/removes it. Do not invent a date, turn date-only into midnight UTC, or substitute `null`/omission. Read legacy content without truncating or rewriting old events.

## Task action mapping

All payloads below also include the stable `task_id`. Use the task stream, accepted task base and current project authorization head/snapshot. `proposal_event_id` and `submission_event_id` name the **current accepted** proposal/submission of this same task; they are not arbitrary event IDs or necessarily the task head.

| User intent | Type and other payload fields | Required state / actor |
| --- | --- | --- |
| Assign a new task | `task.created`: `topic_id,assignee_sid,title,description,deadline,initial_artifacts: []` | New task ID/null own base; creator is actual participating actor. Other assignee → `proposed`; self → `in_progress` |
| Accept a proposal | `task.proposal_accepted`: `proposal_event_id` | `proposed`, current recipient |
| Reject a proposal | `task.proposal_rejected`: `proposal_event_id` | `proposed`, current recipient; becomes `rejected` |
| Propose changed wording/deadline | `task.proposal_revised`: `proposal_event_id,title,description,deadline` | `proposed`, current recipient; at least one content/deadline value changes; other party becomes recipient |
| Cancel after rejection | `task.cancelled` | `rejected`, creator; becomes `cancelled` |
| Reassign after rejection | `task.reassigned`: `assignee_sid,title,description,deadline` | `rejected`, creator; different current project participant; same task ID/history |
| Submit work for review | `task.result_submitted`: `result_artifact_ids: []` | `in_progress`, assignee of a non-self task; becomes `in_review` |
| Accept the submitted result | `task.result_accepted`: `submission_event_id` | `in_review`, creator; becomes `completed` |
| Return work for revision | `task.rework_requested`: `submission_event_id,deadline` | `in_review`, creator; becomes `in_progress`; preserve deadline unless changed |
| Edit a self-task | `task.self_updated`: `title,description,deadline` | `in_progress`, creator=assignee=actor; actual content change |
| Complete a self-task | `task.self_completed`: `result_artifact_ids: []` | `in_progress`, creator=assignee=actor; becomes `completed` |

Normal participants can create tasks without a special creation privilege. Both current actor and assignee must satisfy current membership/domain checks for the command. Management/Root does not replace the creator/assignee/recipient relationships. Removing an assignee does not authorize silently reassigning or impersonating them.

Do not convert an ordinary request to change an accepted non-self task into `self_updated`, rewrite its creation event, invent a message event or silently create a different task. Explain the supported workflow boundary if no accepted transition expresses the request. Reassignment after rejection preserves creation time and history; reassignment to the creator becomes an in-progress self-task.

Materials remain the topic library plus task links. No result-file selection, intermediate/final container movement or required attachment is part of submission/completion. An accepted non-self obligation cannot be silently rewritten during review.

## Combined task and material operations

For a new task with files/references, inspect `initial_task_creation.rs` and material `StagedDraftMaterial`/draft handling before writing. Validate and stage the complete immutable plan **before** publishing the task. Allocate the operation, task, workflow and material IDs once. New `task.created` still uses `initial_artifacts: []`; its materials are registered/reused and linked through the sealed initial-task draft after the exact workflow anchor is accepted. Preserve task publication if some later material steps fail; report which materials/links remain and retry the same operation.

For a proposal revision with material changes, validate the current recipient, expected task/proposal heads and changed content; seal material source bytes/references, expectations and shared-impact confirmation before the revision event. Publish exactly that `task.proposal_revised`, then use the sealed draft anchored to it. The initiating actor's limited proposal-form rights do not become general material-edit rights after the recipient changes.

Read the [material coordinated-draft procedure](materials.md#coordinated-task-drafts) for exact journal shapes and checks. Reuse an available verified coordinator or implement/test its current staged plan and fingerprint behavior; do not replace the compound action with ordinary creator `register`/`link` events that would be unauthorized. If a step cannot proceed, return an accurate partial outcome and preserve its durable plan, rather than deleting the task or restarting with new IDs.

## Workspace reporting

Build project/topic/task views from accepted state, then overlay current registry membership and applicable view rights. Filter my tasks by actual creator/assignee relationships; show a self-task once under executing, not twice. Distinguish proposals awaiting me, proposals awaiting someone else, executing work, review, rejection and terminal states. Show the current proposal version/recipient and pending recovery/conflict separately. For deadline/workload reports use stored precision and the user's timezone; timestamps do not set causality.
