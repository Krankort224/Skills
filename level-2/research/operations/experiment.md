# Experiment: design, execution, and evidence

## Establish the current operation

Identify the assigned operation: design, executor preparation, execution, or data verification. A completed plan is not a completed experiment.

## Design the smallest discriminating check

Link check ID to question, claim ID, model version, and prediction. Choose control/baseline, observables, and comparisons. Prespecify confirmatory criteria, analysis, and permissible conclusions before accessing target results; state exploratory goals.

Define variable/fixed factors, confounders, ranges, and comparison limits. Test material interactions; do not default to changing one parameter at a time.

Choose repetitions for the uncertainty. Stochastic checks need consideration of independent realizations and variability; within-run measurements are not independent replicates. Deterministic checks examine numerical parameters and conclusion stability, without arbitrary identical repeats.

Define compute/time budget and stopping conditions. For adaptive series, specify next-point selection and inference limits; never repeat until a desired result appears.

## Prepare reproducible execution

Record applicable code/environment versions, inputs, parameters, initial/boundary conditions, seed/random-draw order, solver settings, precise execution procedure, and metric extraction.

For external handoff, specify configuration, fixed/variable parameters, required data, criteria, and return format. Request comparability information without assuming environment access.

Before large runs, define immutable evidence, required aggregates/control runs, reproducible derivatives, and complete-dataset location outside Git. Follow project storage rules without requiring all large raw files; never revise policy to conceal inconvenient results.

When modifying a working object, follow the project's required dry-run, isolation, and authorization rules. Do not replace a diagnostic run with a write to the working model.

## Execute or hand off the check

Before running, verify plan compliance, inputs, environment, and previous attempts. Reuse comparable results; justify repeats by reproduction, independent verification, or changed conditions.

Link each run ID to configuration, code, and data; record errors, deviations, and stopping reasons. Give corrected reruns separate IDs linked to originals.

For pending or handed-off runs, list expected evidence; never invent future numbers.

## Verify data before interpretation

Establish:

- whether the check used the required configuration;
- whether required results are complete and excluded runs are accounted for;
- whether units, metric definitions, ranges, and processing methods agree;
- whether the control and investigated option are comparable;
- whether an execution failure or numerical artifact explains the effect;
- whether derived numbers and plots can be reproduced from the stated evidence.

Record `execution_status`, `evidence_quality`, and `claim_status` using root definitions. Missing metrics after failure are not zero effects; do not pool incomparable configurations.

Record data and limitations in the adopted document; route substantive conclusions to [interpretation](interpretation.md). Use optional root forms only as needed.
