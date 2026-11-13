# Proportional evaluation

Use for designing a selected check or comparing material method versions. The [verify operation](../operations/verify.md) owns the minimal original/transfer/regression gate; this reference supplies check design and interpretation details, not a stand-alone evaluator or mandatory directory layout.

## Match the evidence to the claim

| Evidence | Can support | Does not establish alone |
| --- | --- | --- |
| Static/source inspection | Metadata, routes, definitions, syntax and identifiable source-level properties | Behavior of an agent following instructions, native effects, artifact fidelity or causal improvement |
| Mechanical fixture or implementation test | Actual input/output/error behavior of the exercised implementation and fixture/profile | Generalization of prose instructions, excluded inputs or an unexercised target host |
| Agent application | Actual method use, output/actions and criterion-specific behavior in the supplied context | Cold-context independence, causality or reliability beyond the observed trials |
| Target-runtime/domain inspection | The observed artifact, host transaction/readback, rendering or other checked domain behavior | Other versions/profiles, regulatory conclusions or unchecked side effects |

One check can supply several evidence types, but name exactly which observations support each claim. The runtime executing a Python mock is not the native runtime it mocks. Source pins and logs identify evidence; they do not make it authoritative for another subject. Use existing context/domain ownership decisions.

## Specify a useful check

Use raw inputs and observable criteria. For example, a record-association change must retain correct ID membership, order, quantities and rejected invalid inputs; a response saying “preserved order” is not a checker. Include a boundary that could expose the mechanism's limits and affected protected cases, not only demonstrations chosen because they pass.

Choose the checker by the question: deterministic comparison/schema/invariants for precise properties, a grounded rubric for open-ended outputs, applicable native readback or human judgment for properties requiring them. Establish ambiguous rubric decisions through the existing reviewer/arbiter rather than averaging opinions. No checker type is universally sufficient.

Pin the method/artifact, task, data, rubric/checker version, runtime/profile and relevant tools/permissions. Note assumptions, exclusions, expected evidence, execution budget/stopping condition when relevant, and what an unavailable check leaves unresolved. The optional [scenario form](../templates/scenario.template.md) is an adaptation starting point; a few lines in the existing task record can suffice.

Keep actual outcomes separate from the plan. If the checker or fixture is defective, record that and repair/rerun the affected comparison within authority; do not silently discard a negative result. A candidate's own assertions or an author's rubric-aware demonstration are evidence to inspect, not independent verification by themselves.

## Compare material versions

Expand evaluation when scope or coupling makes the minimal set insufficient: changed root selection, multiple interacting operations, new input classes, critical protected behavior or a runtime/profile transition. Choose cases by affected mechanisms and risks; avoid imposing a fixed suite or run count on every task.

1. Fix baseline and candidate revisions, intended gain, protected behavior and comparison criteria before execution. Identify which task authority permits the runs; use existing allocation/model/coordination decisions instead of introducing an evaluation agent sequence.
2. Use comparable task inputs, source evidence, tools/profile/access, execution limits and grading rules. If a condition intentionally changes, isolate and label it; do not attribute the difference solely to the method. A missing baseline or inaccessible runtime leaves that comparison claim unresolved, though separable checks may still support narrower claims.
3. Include the original trigger, meaningfully varied transfer/boundary inputs and affected successful/error paths. Keep expected answers and author explanations out of a fresh executor's initial task. Separate raw tasks from grading material; disclose prior authorship, visible rubric, context/history reuse and other dependence.
4. Inspect actual outputs and consequential actions for each fixed version. Record per-case differences, regressions, unavailable/invalid runs and relevant resource effects. If a model or environment varies, report that confound; stochastic behavior may warrant controlled repeats when justified, not invented trials.
5. Judge the stated improvement together with protected behavior. An original-case gain does not outweigh an unresolved required regression. A smaller claim can be proposed explicitly when evidence supports it; it cannot silently replace the agreed acceptance criterion.

A list of selected cases is not a sampled success rate. Do not call one successful attempt on each of several different cases pass@k or pass^k. Such reliability claims need defined task population, comparable repeated trials, trial count/protocol and uncertainty appropriate to the estimator. Prefer exact observed outcomes and limitations when those conditions are absent; confidence labels, votes, file counts and user silence are not substitutes.

Keep the comparison and outcome in the existing task/review record, with durable source pointers where needed. Do not copy run history into a central learning ledger. Route correction, withdrawal, acceptance or named deferral through [consolidate](../operations/consolidate.md).
