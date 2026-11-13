# Verify the candidate's behavior

Use after refinement or when an existing candidate needs evidence. Reuse the task's candidate hypothesis, scope, protected behavior and check plan; do not repeat earlier operations to fill a sequence. Apply [evaluation](../references/evaluation.md) when check design or a material comparison needs detail.

## Fix the claim and inputs

Identify the baseline, exact candidate revision/artifact and relevant runtime/profile. Record which method the executor actually reads, supplied task/input, expected observations and the source of those expectations. Keep required checks distinct from optional exploration. A changed candidate or material input invalidates evidence about the affected behavior; identify which earlier checks remain applicable.

Use the existing task format or adapt the optional [scenario form](../templates/scenario.template.md). For each check, establish the question, input/conditions, expected behavior, checker/rubric, execution capability and stopping condition before inspecting the candidate's answer. Do not weaken a criterion or replace a difficult case after seeing failure.

## Run the minimal behavioral gate

Select the smallest set that covers:

| Check | What it must establish |
| --- | --- |
| Original trigger | The candidate resolves the demonstrated gap or reproduces the useful technique under its stated conditions. Compare baseline behavior when needed to establish the improvement. |
| Transfer or boundary | A mechanism-preserving change still works, or a stated exclusion produces the intended rejection/deferral rather than an unsupported result. Do not merely rename the original example. |
| Affected regressions | Previously supported behaviors and accepted constraints exposed to the change remain intact, including relevant invalid-input/failure paths and adaptations. Explain when no behavior is affected instead of inventing an unrelated suite. |

Check the behavior produced by using the method. For agent instructions, supply an actual task and raw artifacts with the skill, inspect the result and consequential actions, and grade against the task criteria. Merely finding preferred words in a response or links in the skill does not test that behavior. Keep expected answers, author diagnosis and proposed fixes out of the executor's initial input where independence matters. Disclose author application, prior authorship and context leakage.

For a tool change, execute meaningful input/output/error cases in its relevant runtime. A mock can exercise the mocked contract; it cannot establish native host/store side effects. If an architectural, document or other domain method produces an artifact, inspect the properties its claim requires through the applicable domain method. Source inspection, compilation, receipts and file existence establish only the properties actually checked.

Run only authorized checks. Do not launch agents, install tools, change external data or publish merely because a scenario would benefit from them. Use existing delegation/coordination decisions for independent checks; if access or a required environment is missing, retain that evidence gap and continue separable checks.

## Interpret the observations

Record each actual output/error and the checker used, with evidence level and version. Separate:

- **Observed failure:** the candidate produced behavior contradicting a required criterion. Passing another check does not cancel it.
- **Observed support:** the executed check supports its specific criterion and scope, not untested cases or a reliability claim.
- **Unestablished result:** not run, unavailable capability, inconclusive evidence, or a checker/execution failure that prevents interpretation. Diagnose a repairable checker failure and rerun; do not count it as success or automatically attribute it to the candidate.

Keep simultaneous conclusions: a known regression remains a failure even if another required native check is unavailable. Do not hide the failure under an overall “unverified” label, or turn partial support into overall readiness. A correct original example with a failed protected case is not ready.

For a broad change to scope, root routing, interacting branches or runtime behavior, select the proportional expanded comparison in [evaluation](../references/evaluation.md#compare-material-versions). Otherwise stop when required evidence is sufficient; optional improvements do not require unlimited evaluation.

Return the fixed target, actual results, failed criteria, unavailable checks and their consequences, retained earlier evidence and invalidated checks. Use [consolidate](consolidate.md) for the next decision. Verification supplies evidence, not acceptance or a new task lifecycle.
