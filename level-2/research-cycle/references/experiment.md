# Experiment: design, execution, and evidence

## Establish the current operation

Distinguish designing a check, preparing instructions for an executor, running it, and verifying the resulting data. Perform only the assigned operation; a completed plan is not a completed experiment.

## Design the smallest discriminating check

Connect the check to the question, model version, and prediction. Choose a control or baseline, observable quantities, and necessary comparisons. For confirmatory work, record conditions for conclusions, criteria, and the analysis method before accessing the target result; for exploratory work, state the exploration goal.

Define what varies and what remains fixed, material confounders, parameter ranges, and comparison limitations. If factor interactions matter, provide for testing them; do not automatically reduce the task to changing one parameter at a time.

Choose repetition counts according to the uncertainty involved. For stochastic work, consider independent realizations and variability; repeated measurements within one run are not independent replicates. For a deterministic calculation, check numerical parameters and conclusion stability rather than requiring an arbitrary number of identical runs.

Define the compute/time budget and stopping conditions. For an adaptive series, explain the rule for selecting the next point and the limits of inference; do not repeat a check until the desired result appears.

## Prepare reproducible execution

Record applicable code and environment versions, inputs, parameters, initial/boundary conditions, seed and order of random draws, solver settings, command or other precise execution procedure, and method of obtaining metrics.

For handoff to an external analyst, specify the configuration, fixed and variable parameters, required data, criteria, and return format. Without assuming access to their environment, request the information needed to verify comparability.

Before a large run, define the evidence policy: what remains immutable, which aggregates and control runs are needed, what can be reproduced, and how to locate a complete dataset outside Git. Follow project storage rules; do not automatically require keeping all large raw files. Do not change the policy after an inconvenient result to conceal it.

When modifying a working object, follow the project's required dry-run, isolation, and authorization rules. Do not replace a diagnostic run with a write to the working model.

## Execute or hand off the check

Before running, verify compliance with the plan, input availability, environment conditions, and the existence of relevant previous attempts. Reuse a comparable result; repeat it for reproduction, independent verification, or changed conditions with an explained purpose.

Assign a stable identifier to each run; connect it to configuration, code, and data. Preserve material errors, deviations, and stopping reasons. Separate a corrected rerun from the original attempt.

If a run has not occurred or has been assigned to the user/an external executor, state this explicitly and list the expected evidence. Do not fill future numbers with assumptions.

## Verify data before interpretation

Establish:

- whether the check used the required configuration;
- whether required results are complete and excluded runs are accounted for;
- whether units, metric definitions, ranges, and processing methods agree;
- whether the control and investigated option are comparable;
- whether an execution failure or numerical artifact explains the effect;
- whether derived numbers and plots can be reproduced from the stated evidence.

Separate execution status, data credibility, and hypothesis support. A missing metric after failure is not a zero effect. Do not combine incomparable configurations into one estimate.

Record data and limitations; use the interpretation reference in the root skill for substantive conclusions. For a durable definition and result, use the corresponding root-skill forms within the adopted project document.
