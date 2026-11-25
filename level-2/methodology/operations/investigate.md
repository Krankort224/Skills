# Investigate

Start with the decision the user needs and the evidence already available. A completed run can be interpreted immediately. Frame a new check only for an uncertainty that could change the answer.

## Diagnose a discrepancy

Describe the observed result, the expected result, and the conditions under which the difference occurs. Separate requirements from the means assumed to satisfy them. For a new question, identify the system, the unknown and what would count as a sufficient answer. Exploration can identify promising explanations. Confirmation requires a prediction and criteria set before examining the target result.

Compare the failing case with a comparable working case or a known reference. Trace where their inputs, measurements, assumptions or actions first diverge. For each plausible explanation, identify an observable consequence and an outcome that would count against it. Select the smallest check for which the explanations predict different outcomes. If they predict the same result, identify the missing observation. For an engineering choice, checking a stated operating criterion can suffice.

For a calculation that changes with step size, fix the model and inputs, vary the numerical setting, and examine whether the quantity of interest stabilizes. Whether that quantity describes the physical system is a separate question with its own evidence. For solver details or a model revision, use [model checks](../references/models.md). For a controlled test or handoff, use [experiment design](../references/experiments.md).

## Compare prior work

State what the comparison must settle, such as whether an earlier measurement supports a claim or supplies a useful control. Search by mechanism and conditions as well as by project terminology. Choose the depth that the decision requires. Verify consequential claims in the original publication, documentation, data or implementation.

For each material analogue, identify what was measured or proved, how, under which conditions, and which difference could alter the result here. Distinguish proofs, simulations, physical observations and authors’ interpretations. A source can supply a useful method even if its data cannot settle the target claim. Report disagreements, search scope and access gaps. When coverage matters or someone will repeat the search, record the date, where you looked, the queries or direct lookup path you actually used, and the decisive passage. Bound novelty claims to that coverage. Stop when further searching is unlikely to change the decision or the agreed budget is exhausted.

## Design or evaluate a working method

1. **Define the job.** Identify the executor, inputs and arrival times, required output, and who owns each fact and decision. For each required check, say what evidence satisfies it. Use a status the task or authoritative source already supplies. Seek fresh confirmation only when the status is missing, conflicting, or the governing rule requires it. Bind release authority to the project role and label any proposed extra approval as optional.
2. **Choose how to perform it.** Compare viable approaches, including current practice. Identify the difference in outcome, cost or prerequisites that changes the choice. Write the ordinary case so the executor can complete it with the supplied evidence. For a readiness decision, put the verdict at the point the deciding checks pass. For example, “Mark it ready when the checks pass. The authorized person can then issue it and record the transmittal.” Put a record or signature before the verdict when the governing rule makes it a condition. For each hold, name the unmet condition, who can resolve it and which work can continue.
3. **Try to break the choice.** Walk a fully valid input through the draft, including its intake steps. If it stops for paperwork, a second person or reconfirmation, identify the rule or unresolved fact that requires that stop. Remove unsupported stops from the delivered procedure. Check the motivating case, a transfer case that distinguishes the intended rule from a plausible shortcut, and any consequential missing input or previously correct behavior at risk. Where feasible, have another executor try the draft on fresh inputs. Inspect the actual output and decision to proceed or hold, and record which cases ran.
4. **Give the decision and its limits.** Deliver the usable procedure or the smallest justified edit at the owner of the rule. Retaining the current method is a valid result. If the choice still depends on an unknown, name the observation that would settle it. An analysis request ends with the recommendation.

When the starting evidence is a memory, proposal or unusual success, recover the version of the instruction, the action taken, and the result. An adequate step may have been skipped or made hard to find by a broken link. A permission, missing input or project convention can explain an episode. Inspect these possibilities before proposing a shared change. Report separately what failed in the original method and how the candidate performed. One documented counterexample can invalidate a universal guarantee while the proposed repair still needs testing.

## Interpret existing evidence

Recover the question, prediction, definitions and criteria that applied to the actual run. Inspect the inputs, units, source version, comparison conditions and deviations that could change the conclusion. Preserve the original evidence and identify hypotheses developed after inspecting it.

Report what was executed, how usable its evidence is, and which claim it supports or contradicts under the tested conditions. A failed run can leave the claim open. Quantify variability where relevant and distinguish practical effect from statistical uncertainty. Link the result to the specific measurement, log, proof or comparison. A change in one metric can leave competing mechanisms unresolved. For formal check records and reproducible runs use the [evidence record](../references/experiments.md#evidence-record).

Finish with the scoped conclusion and its limit. If another check is worthwhile, explain which remaining decision it enables. Keep a result, its interpretation, and any authorized change to the method or project separately identifiable.
