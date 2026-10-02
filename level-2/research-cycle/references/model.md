# Model formalization and verification

## Establish the model's role

Determine what the model represents and which question it serves. Distinguish an abstract mathematical model, a physical model, an engineering calculation, and a model of software behavior. A more detailed implementation does not automatically become more credible.

Use the current project baseline. State proposed changes separately; do not silently replace the accepted model.

## Make assumptions explicit

Record applicable elements:

- variables, parameters, units, and notation;
- geometry, topology, domains, and relationships;
- equations, algorithms, or state-transition rules;
- initial and boundary conditions, inputs, and excitations;
- included and excluded processes;
- applicability range and missing information;
- the relationship between internal state and measured quantities.

For software, states, input contracts, transitions, and observable outputs may replace physical equations. Explicitly omit what is not applicable; do not invent physical meanings for technical parameters.

## Separate verification levels

| Level | Question being checked | Possible methods |
| --- | --- | --- |
| Formal correctness | Are definitions, relationships, and constraints consistent? | Dimensions, ranges, limiting cases, invariants, analytical implications |
| Implementation correctness | Does the code implement the accepted model? | Control cases, comparison with an analytical solution, transition and invariant checks |
| Numerical credibility | Does the calculation method determine the result? | Convergence with step/mesh, tolerances and horizon, method comparisons, stability diagnostics |
| Correspondence to the system | Is the model sufficient for conclusions about the investigated object? | Comparable measurements, an external benchmark, physically justified parameters and limitations |

Choose checks according to the risk of the particular conclusion. Passing implementation tests does not prove a physical mechanism; missing external data limits conclusions to the model level.

## Distinguish physical and technical factors

Separate model parameters from solver settings, stopping criteria, floating-point effects, and technical limits. Determine whether the claimed effect depends on discretization, a threshold, clamping, or resampling.

If stabilization changes an equation or the admissible state space, treat it as a model change. If it implements an unchanged contract, explain its numerical meaning and check its influence. Do not introduce a “fix” merely because the current result is inconvenient.

## Choose sufficient rigor

Use a simple model for the accessible question. Move to a more rigorous solver, greater detail, or a physical prototype when the effect to test, material parameters, observable signature, and grounds for considering the previous level insufficient are defined.

Do not demand physical confirmation of abstract research, but do not transfer its result to a physical system without the corresponding justification.

Preserve the model or its change at the project-defined owner; record the version used and material differences in the experiment. Do not create a second full model description merely to satisfy a form.
