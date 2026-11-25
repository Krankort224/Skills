# Investigate

Start with the decision the user needs and the evidence already available. A completed run can be interpreted immediately. Frame a new check only for an uncertainty that could change the answer.

## Diagnose a discrepancy

Describe the observed result, the expected result, and the conditions under which the difference occurs. Separate requirements from the means assumed to satisfy them. For a new question, identify the system, the unknown and what would count as a sufficient answer. Exploration can identify promising explanations. Confirmation requires a prediction and criteria set before examining the target result.

Compare the failing case with a comparable working case or a known reference. Trace where their inputs, measurements, assumptions or actions first diverge. For each plausible explanation, identify an observable consequence and an outcome that would count against it. Select the smallest check for which the explanations predict different outcomes. If they predict the same result, identify the missing observation. For an engineering choice, checking a stated operating criterion can suffice.

For a calculation that changes with step size, fix the model and inputs, vary the numerical setting, and examine whether the quantity of interest stabilizes. Whether that quantity describes the physical system is a separate question with its own evidence. For solver details or a model revision, use [model checks](../references/models.md). For a controlled test or handoff, use [experiment design](../references/experiments.md).

## Compare prior work

State what the comparison must settle, such as whether an earlier measurement supports a claim or supplies a useful control. Search by mechanism and conditions as well as by project terminology. Choose the depth that the decision requires. Verify consequential claims in the original publication, documentation, data or implementation.

For each material analogue, identify what was measured or proved, how, under which conditions, and which difference could alter the result here. Distinguish proofs, simulations, physical observations and authors’ interpretations. A source can supply a useful method even if its data cannot settle the target claim. Report disagreements, relevant search scope and access gaps. Bound any novelty statement to the sources and search performed. Stop when further searching is unlikely to change the decision or the agreed budget is exhausted.

## Design or evaluate a working method

1. **Define the job.** Identify who will use the procedure, which inputs they receive and when, the source that owns each critical decision, and the required output. Specify constraints that a successful change must preserve. Use the project’s existing release criteria and authority. If an additional approval would be valuable, present it as a proposed change and explain the need.
2. **Choose how to perform it.** Compare viable approaches, including the current practice when it exists. Identify the difference in outcome, cost or prerequisites that would change the choice. Describe the selected sequence in terms another executor can follow. Specify what to do with missing, late or ambiguous inputs, which independent work can proceed, and when the output is ready to use.
3. **Try to break the choice.** Define observable success and failure before checking. Exercise the motivating case, a different input that tests transfer, and a case that already works when a revision puts it at risk. For a reusable procedure, have another executor apply the instructions to fresh inputs when feasible. Inspect the resulting work against the required output. Record which checks were actually run.
4. **Give the decision and its limits.** Deliver the usable procedure or the smallest justified edit at the owner of the rule. Retaining the current method is a valid result. If the choice still depends on an unknown, name the observation that would settle it. An analysis request ends with the recommendation.

When the starting evidence is a memory, proposal or unusual success, recover the version of the instruction, the action taken, and the result. An adequate step may have been skipped or made hard to find by a broken link. A permission, missing input or project convention can explain an episode. Inspect these possibilities before proposing a shared change. Report separately what failed in the original method and how the candidate performed. One documented counterexample can invalidate a universal guarantee while the proposed repair still needs testing.

## Interpret existing evidence

Recover the question, prediction, definitions and criteria that applied to the actual run. Inspect the inputs, units, source version, comparison conditions and deviations that could change the conclusion. Preserve the original evidence and identify hypotheses developed after inspecting it.

Report what was executed, how usable its evidence is, and which claim it supports or contradicts under the tested conditions. A failed run can leave the claim open. Quantify variability where relevant and distinguish practical effect from statistical uncertainty. Link the result to the specific measurement, log, proof or comparison. A change in one metric can leave competing mechanisms unresolved. For formal check records and reproducible runs use the [evidence record](../references/experiments.md#evidence-record).

Finish with the scoped conclusion and its limit. If another check is worthwhile, explain which remaining decision it enables. Keep a result, its interpretation, and any authorized change to the method or project separately identifiable.
