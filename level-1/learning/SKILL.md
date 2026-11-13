---
name: learning
description: Deepen skills from significant evidence during actual use. Every agent keeps this learning contract in view; start a concrete improvement cycle only for a demonstrated gap or a useful, transferable solution within the current task's permissions.
---

# Learning

Improve the method that produced an outcome when evidence warrants it. Notice meaningful corrections, uncommon successful solutions, failures and missing branches during the task. Routine successful use needs no learning report, additional analysis, file, evaluator or skill change. Reading this Level-1 contract starts none of those actions.

## Decide whether to proceed

For a significant signal, read [evidence and scope](references/evidence-and-scope.md). Compare the episode with the method actually used, its source revision, task requirements and available evidence. Diagnose before generalizing:

| Finding | Next action |
| --- | --- |
| Existing instructions already cover the case; execution departed from them | Correct execution within the task; no skill change for that error alone. |
| Missing context/access, a navigation gap, or a project-specific fact | Resolve or report the gap at its owner; do not turn it into a universal method rule. |
| Evidence identifies a reusable method gap or a transferable successful technique | Prepare a bounded refinement candidate at the owning method. One well-supported exceptional case can suffice. |
| Cause, source, scope or outcome is materially uncertain | Obtain the discriminating evidence if authorized, or defer the candidate with the named gap. |

Mixed causes are possible. A navigation repair can itself be reusable, but that requires evidence about the route; it does not prove the underlying method is deficient. Frequency, user silence and model confidence establish neither generality nor acceptance.

## Bound the candidate

Before editing, state the hypothesis and expected gain, evidence, applicability/exclusions, canonical owner and proposed destination, protected behavior, and verification plan. Choose the smallest coherent improvement: an operation, diagnostic branch, reference, example, tool or test; change the root only when the shared contract needs it. Without write authority, return the proposal on the existing task surface.

Plan checks of behavior produced by the method: the original case, a transfer or boundary case, and affected regressions. Distinguish planned checks from actual results and static/mechanical checks from agent behavior and target-runtime evidence. A tested candidate still carries the scope and limitations of those checks.

Use the applicable task process to correct and recheck, roll back only candidate changes while preserving unrelated work, accept under existing authority, or defer with named missing evidence. Readiness, publication and a successful check do not supply user acceptance; do not add a new approval ceremony where the task already authorizes the action.

## Select the operation

Start at the current action; reuse sufficient existing evidence rather than requiring a fixed sequence or loading every procedure:

| Current need | Operation |
| --- | --- |
| Capture the meaningful episode and decide whether more investigation is warranted | [observe](operations/observe.md) |
| Diagnose the mechanism, cause and transfer boundary | [generalize](operations/generalize.md) |
| Locate and prepare the smallest authorized candidate change | [refine](operations/refine.md) |
| Check candidate behavior and the evidence supporting its claims | [verify](operations/verify.md) |
| Decide correction, rollback, acceptance or deferral | [consolidate](operations/consolidate.md) |

Use [placement](references/placement.md) for owner/resource selection and the optional [improvement form](templates/improvement.template.md) when the current task format is insufficient. They supply no new authority or mandatory artifact.

Select [evaluation](references/evaluation.md) for check design or material version comparisons; the optional [scenario form](templates/scenario.template.md) helps specify a check without creating a new evaluation system.

## Preserve owners and load selectively

Use `context` for source authority, project understanding and knowledge destinations; `workflow` for an applicable Issue lifecycle and acceptance; `delegation` for agent allocation and recovery; assigned `arbitration` for coordination and adjudication. Supply evidence to these owners without duplicating their procedures or changing their permissions. Learning does not create an Issue, spawn an agent, install a tool or broaden a task.

Keep transient candidates and evidence in the existing task's work surface. Integrate accepted reusable knowledge at its canonical method owner; keep local facts in project-owned knowledge. Do not create a central observation archive, copy private transcripts, or duplicate accepted Issue summaries.

Load the [decision cases](tests/scenarios.md), [refinement cases](tests/refinement-cases.md) or [evaluation cases](tests/evaluation-cases.md) for the corresponding checks, and the [source/adaptation record](references/sources.md) for provenance questions. None is required for uneventful use. This skill implies no hooks, background observer, confidence database or automatic mutation/promotion.
