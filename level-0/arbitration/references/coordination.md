# Coordination and continuation

## Fix the review target and access

Identify the exact immutable revision and confirm the reviewer can read its required artifacts and baseline. A local commit is sufficient when accessible. Publish when that helps execution, review, continuity, or delivery.

Creating commits and pushing changes of the current task to the agreed repository/branch are ordinary execution actions without repeated confirmation, unless user instructions, repository rules, or platform permissions restrict them. This does not automatically authorize merge, deployment, access changes, or unrelated publication.

Review a fixed revision rather than a moving working tree. Unrelated work may continue without altering that target. After relevant changes, identify the new revision, reconcile existing findings, and refresh invalidated verification. Coordinate a single writer for shared artifacts; preserve other participants' work. Separate sessions or subagents may share a filesystem and do not imply technical isolation.

For a denied, pending, or uncertain action, record the exact action/target, reason, completed work, and outcome state. Check an uncertain outcome before retrying. Never route a denied operation through another agent or tool to bypass the restriction; retry only when the governing authorization/retry conditions permit it. Continue unaffected work and report the actual remaining blocker.

## Select category and session arrangement

Use В when one lead can manage bounded assignments and non-author checks. Use Б when persistent implementation/review separation and accompaniment ownership are useful; use А when protocol, navigation and source-management work justify a secretary. A multi-pass Issue must use Б or А, even when each pass is small. Before dispatch or resuming dependent work, replace an invalid В arrangement with Б/А while retaining the current pass, cycle, findings and authorizations. This does not create a new pass or grant permission for new sessions.

Keep the selected arrangement while evidence shows progress toward the agreed criteria, credible checks, and resolution of material findings without recurring regressions. An ordinary repairable defect or a correction checkpoint alone does not justify switching categories or sessions. Model/tree decisions remain with delegation. Categories Б/А need not use multiple user sessions; a reviewer subagent can provide a distinct role in the same execution session.

Consider proposing two independent sessions when a diagnosed limitation of the arrangement compromises quality:

- a material defect persists or recurs despite targeted correction and verification;
- corrections repeatedly introduce regressions;
- review repeatedly misses demonstrable violations or substitutes executor assurances for verification;
- a consequential disagreement survives a bounded factual check.

A severe demonstrated independence failure or essential environment/access limitation may justify an earlier proposal. Diagnose the cause first. Missing requirements, inputs, or permissions need their own remedy; additional sessions do not provide them. Do not assume a different model or session improves quality without a reason tied to the failure.

## Agree a transition

For a category change, state its task-related cause, expected benefit/cost, scope, owners and next checkpoint. The coordinator can make an ordinary assignment change within existing authority; escalate a material tradeoff or additional permission. Do not use a category change to exchange the writer/checker of unfinished result areas. Preserve the multi-pass minimum category and all stage history.

Before launching the second session, present the failed quality criterion, supporting evidence, attempted remedies, expected benefit, coordination cost, and proposed scope and stopping conditions. Obtain user agreement unless prior explicit authorization already covers that transition. Keep the agreement for its stated scope; do not seek it again at each role exchange.

Verify that separate-session launch, access, and reporting are actually available. Disclose missing capabilities and their effect instead of claiming a transition. While agreement is pending, continue useful authorized work in the current arrangement where possible, without launching the second session. If independent review is unavailable, disclose the gap; do not present self-review as independent review.

## Assign areas before editing

Classify by the requested result, not extension or directory:

| Area | Writer in Б | Writer in А | Independent check |
|---|---|---|---|
| Subject result, including requested documentation, skill contracts, tests and settings | Executor | Executor | Subject reviewer |
| Accompanying content: usage explanation, durable limitations and supporting knowledge | Reviewer | Reviewer | Executor read-only or another non-author |
| Navigation: maps, indexes and reading routes | Reviewer | Secretary | Assigned non-author; reviewer may check secretary changes only if uninvolved |
| Protocol records | Named workflow operation owner | Named workflow operation owner; secretary records authorized acceptance and monitors protocol | Non-author checks authored acceptance summaries/records before destructive consolidation |

In В the lead explicitly assigns needed areas and non-author checks without inventing standing roles. In all categories, an author cannot independently approve their changes. A coordinator-authored artifact also needs a non-author check where independent verification is required.

Accompanying documentation is separate from the deliverable. If the task requests a manual or skill adaptation, its normative Markdown is the subject result: the executor writes it. Do not reclassify a reviewed file as accompaniment to let the reviewer fix their own finding. In Б/А the executor may read accompaniment, verify it and supply facts/findings but does not edit it; its owner makes corrections.

For mixed-purpose files, choose one writer before work and route other contributions to that writer. Prefer a file-level boundary. If sequential ownership transfer is necessary, record scope, fixed revision and new writer; serialize edits and preserve independent checking. Splitting a file or transferring custody does not erase authorship or permit a reviewer to implement their own finding in the same stage.

Secretary authority covers navigation/protocol within the assignment, not arbitrary subject content. A knowledge-source restructuring uses context and the applicable restructure operations: establish inventory, agreed map/scope, preserve sources/provenance and verify the migration independently. A role name grants no deletion, download, publication or scope expansion authority.

## Maintain documentation with the stage

At stage dispatch, determine the documentation affected by the agreed result using the project's authoritative sources. Identify the canonical owner, actual update destination, permissions, baseline, stage writer and non-author checker. Consider, where relevant, architecture and technical design, interface/contract definitions, configuration, operating and project instructions, knowledge references, maps, indexes and reading routes. Select by material change, not a mandatory document checklist; record a source-based no-update conclusion when nothing is affected.

During implementation, integration and correction, revisit the impact set when decisions, behavior, file locations or interfaces change. Route each required update to the writer established under [Assign areas before editing](#assign-areas-before-editing): requested/normative subject documentation belongs to the executor; accompaniment belongs to the reviewer in Б/А; navigation belongs to the reviewer in Б or secretary in А; В uses expressly assigned writers and non-author checks. For mixed-purpose sources, retain the agreed file-level owner. Do not let the subject reviewer edit subject documentation under the guise of keeping it current.

Within the authorized scope, update the canonical sources during the same stage, not merely in the handoff or accepted summary. The assigned non-author checks the revised documentation against primary evidence and the final combined result, including material contracts, routes and dependencies. If the result changes after the documentation check, repeat affected documentation and integration checks; if documentation changes after subject review, recheck affected cross-area consistency. An author's assertion or a passing subject-only test does not prove documentation currency.

When a mandatory affected source is inaccessible, outside the permitted write scope or lacks authoritative evidence, do not edit it by assumption. Record the document, mismatch or missing evidence, owner, effect and required authority/remedy; escalate the real decision through the existing process while progressing on separable work. The stage is not ready while a required update or independent check remains unresolved. Optional or unrelated pre-existing documentation debt may be reported separately without expanding the stage or blocking an otherwise sufficient result. Use context for source/update ownership and workflow for applicable Issue acceptance/consolidation; this coordination rule creates neither another documentation lifecycle nor blanket write permission.

## Keep roles within a stage

Identify the stage by its agreed result, scope/boundary and completion criteria. It includes the corrections and rechecks needed to meet those criteria. A new revision, correction cycle, handoff, numbered operation step, participant replacement or restored context does not by itself create a new stage. Do not relabel unfinished correction work to permit a role exchange.

Dot remains arbiter. The executor implements and corrects the subject result; the reviewer independently reviews and rechecks fixed revisions. Keep the reviewer read-only for that area throughout the stage, including its code, tests, subject documentation and settings. They may run checks and create isolated diagnostic examples without changing it. Small fixes and corrections to their own findings still belong to its executor. A separately assigned accompanying area can have the reviewer as writer and another participant as checker; this is not a subject-role exchange.

If an unavailable participant must be replaced under existing recovery authority, preserve the role and transfer its assignment and progress. Replacing the executor does not promote the reviewer to implement their findings; appoint a replacement executor while the reviewer remains reviewer. Apply the same writer/checker separation to accompanying and secretary-owned areas. Preserve the stage, open findings and correction history when replacing any participant.

Exchange roles only after the current stage is complete under the task's existing process and a genuinely different stage begins. Announce the new assignments before editing. A stage is not automatically an Issue major pass; preserve the applicable pass-acceptance rules without adding a separate user-approval gate for every internal stage. A correction cycle within the same stage retains its roles regardless of workflow status changes.

Serialize shared-artifact edits. No session independently signs off its own new changes. Dot receives the complete reviewer report without executor filtering. Between-stage exchanges do not reset findings, history, authority, or acceptance criteria. Earlier authorship can still influence judgment: check against the agreed criteria and source evidence, disclose material independence limits, and arrange a bounded fresh check when justified and authorized.

## Check the combined result

Collect assigned contributions before the workflow execution owner publishes the combined handoff. Identify each area's writer, checker and fixed revision, including accompaniment and navigation. The subject reviewer publishes the complete subject review; other area checks remain separately attributable. Supporting participants do not independently change cycle status or publish competing cycle handoffs.

The coordinator gates readiness on the final combined result: all required areas independently checked, material findings reconciled, required skills applied, permissions in scope and limitations disclosed. A reviewer or secretary's contribution is not accepted merely because that role authored it. Check documentation against primary evidence, not only executor assurances. If the proposed checker would just repeat their own unsupported conclusions, use a bounded fresh source-based check by another non-author.

After a reviewed area changes, fix the new revision and refresh its check and affected dependencies. Preserve still-valid evidence explicitly; do not label an old review as verification of the new combined revision. Route corrections through the existing workflow cycle to the area's writer. In Б/А the subject executor remains read-only for accompanying corrections.

Keep workflow's distinction between readiness, authorized acceptance and closure. The secretary records rather than grants acceptance; independently check the authored summary/record against the actual review, result and authorization before consolidation removes supporting comments. Reuse prior explicit intermediate-acceptance permission for its stated scope without a new prompt at each internal stage. It does not automatically cover final acceptance or Issue closure. Use the existing acceptance/consolidation procedure and its capability-gap handling, not another protocol journal.

## Carry the assignment through handoffs

Carry the following in the existing task handoff, using source pointers for the contract and stating critical requirements directly:

- execution unit/cycle, current stage result/boundary and completion criteria, and operation owner;
- category, each area's writer/checker, workflow operation owners, and authorized session/mode scope;
- explicit required-skill list, source paths/revisions, selected operations/resources, and the instruction to read and apply them;
- baseline and exact result revision/access;
- concrete correction and preserved boundaries;
- documentation impact set, required updates, their canonical owners/writers/checkers, verification evidence, and any unresolved destination or access blocker;
- all open findings, evidence and closure conditions;
- material decisions/permissions, correction history, and next checkpoint.

Preserve these instructions through correction dispatch, further delegation, replacement and continuation. Supplement newly applicable skills under the same source-revision and authority constraints; load their resources progressively. Record sources actually read, task-relevant application/check evidence and gaps separately from the requirements that the recipient must follow. A predecessor's claim of skill use does not replace the next participant's assignment.

## Continue after context loss or transfer

Recover the required-skill assignment and material constraints, read the necessary skill/task sources at their recorded revisions, and record what the receiving participant actually read. Recover live task/Issue state, the current unit/cycle and stage, category and area/operation owners, agreed session scope, baseline/result revisions, open findings, decisions/permissions, correction history, and next action from established records. Check for newer task instructions and changed artifacts before resuming; do not silently change the skill revision. Recheck the multi-pass category constraint without restarting the current cycle.

Do not equate a skill's publication with its automatic loading, or a handoff with evidence that another participant read it. If the procedure or task state is unavailable, identify the gap and continue only supported independent work. Do not reconstruct authority or acceptance from silence, cached memory, or an old summary when the necessary live state is missing.
