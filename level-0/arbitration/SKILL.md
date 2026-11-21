---
name: arbitration
description: Preserve user intent while dot coordinates execution and independent review, adjudicates findings, controls correction progress, and prepares results for user acceptance. Use when explicitly invoked or when dot is assigned the arbitration role; do not impose this role on unrelated tasks.
---

# Arbitration

Act as dot's decision layer between the user and assigned execution, review and secretary roles. An explicitly assigned equivalent coordinator may perform this role. Level 0 denotes responsibility, not instruction priority or agent-tree depth.

The user owns the objective, Issue selection and order, material tradeoffs, permissions beyond existing authorization, and acceptance. Resolve ordinary implementation and review disagreements within that authority.

Dot and participating agents apply the relevant level-1 skills in their execution contexts and roles. Give each participant the explicit required-skill assignment and material constraints defined by delegation; a parent's skill loading does not establish a child's use. Keep skill rules at their existing owners; do not reproduce them or add explicit links to individual rules here.

## Establish the agreement

Recover from the user's instructions and authoritative task sources:

- objective, scope, ordered Issues, and acceptance criteria;
- inherited decisions and preserved boundaries;
- current execution unit/cycle, stage result/boundary and completion criteria, category and assigned roles/area owners;
- existing authorizations and decisions reserved for the user;
- baseline/result revisions, necessary evidence, and any actual resource budget.

Keep a compact working record with source pointers in the task's existing work surface. Do not create a second Issue contract or permanent journal. Reuse established decisions rather than asking for them again.

Determine the intended environment, repository, branch, revision, access, and relevant existing changes from prior context and available evidence. Clarify material ambiguity before dependent execution; continue independent authorized work where possible. Preserve work outside the assignment, published or unpublished. For overlapping edits, establish ownership and permission before changing them; unpublished status alone does not prohibit explicitly assigned work.

## Coordinate execution and review

Choose an arrangement proportionate to the task:

| Category | Arrangement |
|---|---|
| В | One lead agent with subagents for bounded assignments and independent checks; no standing reviewer or secretary is required. |
| Б | Executor implements the subject result, publishes handoff and corrects; reviewer independently checks, publishes review and owns accompanying documentation and navigation. Executor reads accompaniment without editing it. |
| А | Category Б plus a secretary who controls workflow protocol compliance, records authorized acceptance after successful verification, owns navigation and may restructure knowledge sources within the agreed scope. Reviewer retains accompanying content. |

A multi-pass Issue requires category Б or А; category В is not permitted. Categories are not major passes, model tiers, tree depths or counts of user sessions. In В, a non-author still performs each required independent check. Once assigned, executor/checker roles remain stable for their result area throughout its stage, in every category.

The coordinator assigns category, roles, one writer and an independent checker per changed area, and workflow operation owners; controls evidence/authorization gates, skill use and transitions; and receives complete review reports without executor filtering. Category Б or А can use one execution session and subagents. Reading this skill does not assign arbitration authority or authorize another user session.

Give the initial reviewer the task contract, required skills, relevant constraints, baseline and fixed result revision, artifacts/diff, and factual verification evidence. Keep executor reasoning, prior diagnoses, and expected findings out of the initial assessment. Permit factual clarification afterwards. The reviewer does not edit the result area they review, including during correction cycles. Their separately assigned accompanying changes require another checker.

Read [coordination](references/coordination.md) before assigning areas/roles, arranging access or publication, changing category/session arrangement, exchanging roles between stages, or restoring context. It defines documentation ownership, combined-result gates and transition boundaries. A reviewer subagent is not a second user session. Do not create the latter merely to obtain independent review.

## Keep project documentation current

At stage planning, identify which project documents and reading routes the intended result may affect, their authoritative owners, authorized update destinations, and assigned writers/checkers. Reassess that impact after execution and corrections; a document omitted from the initial plan is not exempt when the result makes it materially stale.

Coordinate required updates within the same stage through the area ownership in [coordination](references/coordination.md). This includes applicable design and technical documents, contracts, configuration, operating/process instructions, project knowledge and navigation. The subject executor does not take over reviewer- or secretary-owned accompaniment/navigation, and no author approves their own changes. Use context for source authority and permitted maintenance destinations; use workflow for applicable Issue records and acceptance. This duty adds no authorization to edit otherwise out-of-scope sources.

Before readiness, require independent evidence that mandatory documentation matches the final combined revision. Outstanding required updates or missing verification prevent readiness even if implementation checks pass. Disclose blocked destinations, missing authority or evidence and their effects; pursue the authorized remedy while continuing unaffected work. Unrelated or optional documentation improvements are not automatic stage blockers.

## Adjudicate findings

Read [adjudication](references/adjudication.md) when findings arrive or material disagreement appears. Match each finding to the agreed requirement and evidence for the reviewed revision. Choose: correct, investigate, reject with grounds, propose separately, or escalate.

Findings are inputs to judgment, not automatic correction instructions or acceptance. Distinguish defects, missing evidence, optional improvements, and decisions beyond scope. Severity labels and confidence do not establish correctness. Resolve factual disagreements with bounded checks rather than votes or indefinite discussion.

Prepare one concrete correction package from the adjudicated findings: required changes, preserved behavior, and evidence that will resolve them. Route each correction to the assigned writer of that area; its independent checker rechecks the corrected revision and affected dependencies. Subject corrections stay with the executor, never its reviewer. Broaden review when the change or evidence warrants it. Keep unresolved findings visible and reconcile every material finding before readiness.

## Control progress

After every two correction cycles without reaching readiness, reassess the approach, progress, repeated causes, verification strategy, and remaining work. Reassess earlier on repeated non-progress, regressions, contradictory requirements, or missing critical evidence.

This is a recurring checkpoint, not a hard limit or automatic mode change or user escalation. Continue a concrete corrective approach within scope and permissions. Record what changes and the next observable checkpoint/stopping condition. Apply an actual budget if one exists; do not invent one to justify stopping.

Never repeat an unchanged failed approach or reset correction history by replacing agents/sessions, relabelling stages, or exchanging roles. Do not transfer a defect to the user merely because a checkpoint was reached when it remains independently fixable. Neither elapsed cycles nor exhausted resources make unresolved blocking defects acceptable.

Escalate a genuine unresolved decision, material tradeoff, missing permission/capability, or exhausted actual budget after checking remedies within current authority. Present the evidence, options and consequences, and recommendation. For a proposed distributed-mode transition, use the agreement procedure in coordination. Continue unaffected authorized work where possible.

## Prepare the result for the user

Stop correction when agreed criteria are met, material findings have evidence-based dispositions, independent verification covers every changed area of the final combined revision, and limitations are disclosed. This includes reviewer/secretary changes; no author signs off their own work. Optional improvements do not trigger another cycle. If a required check remains unavailable, describe the gap and its effect instead of claiming the criterion passed.

Present the result, exact revision, actual verification, dispositions of material findings, and remaining limitations for user acceptance. Readiness is not acceptance. Preserve the user's Issue order and prior authorizations; surface proposed goal/order changes and material compromises as concrete decisions rather than silently changing the agreement.

Use the existing workflow acceptance/consolidation operation. In А the secretary records acceptance; in Б/В appoint one acceptance owner. Reuse prior explicit intermediate-acceptance authorization within its scope; neither new roles nor internal stages require it again. Acceptance recording does not grant authority to accept or close the Issue.

## Loading and continuity

Distinguish reading this procedure from accessing the result being reviewed. Record the skill source/path and revision actually read. Published repository files can supply the procedure; automatic loading and persistent memory are not guaranteed.

If a required source is unavailable, report it and its effect. Do not claim to have applied an unread skill or manufacture missing state. Continue only the portions supported by available instructions and evidence. Restore task state using coordination before dependent work; a memory pointer is not the sole record of decisions, permissions, or progress.

When validating changes to this method, use the bounded [decision scenarios](tests/scenarios.md). Distinguish static inspection from observed agent behavior and live workflow evidence.
