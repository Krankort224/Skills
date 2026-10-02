# Model formalization and verification

## Establish the model's role

Identify represented system and question. Distinguish mathematical, physical, engineering, and software-behavior models; implementation detail alone adds no credibility.

Identify baseline version and proposed changes separately.

## Make assumptions explicit

Record applicable elements:

- variables, parameters, units, and notation;
- geometry, topology, domains, and relationships;
- equations, algorithms, or state-transition rules;
- initial and boundary conditions, inputs, and excitations;
- included and excluded processes;
- applicability range and missing information;
- the relationship between internal state and measured quantities.

For software, states, input contracts, transitions, and outputs may replace physical equations. Mark inapplicable elements; do not invent physical meanings for technical parameters.

## Separate verification levels

| Level | Question being checked | Possible methods |
| --- | --- | --- |
| Formal correctness | Are definitions, relationships, and constraints consistent? | Dimensions, ranges, limiting cases, invariants, analytical implications |
| Implementation correctness | Does the code implement the accepted model? | Control cases, comparison with an analytical solution, transition and invariant checks |
| Numerical credibility | Does the calculation method determine the result? | Convergence with step/mesh, tolerances and horizon, method comparisons, stability diagnostics |
| Correspondence to the system | Is the model sufficient for conclusions about the investigated object? | Comparable measurements, an external benchmark, physically justified parameters and limitations |

Select checks by conclusion risk. Implementation tests do not prove physical mechanisms; absent external data limits conclusions to the model level.

## Distinguish physical and technical factors

Separate model parameters from solver settings, stopping criteria, floating-point effects, and technical limits. Check effect dependence on discretization, thresholds, clamping, or resampling.

Stabilization changing equations/admissible states is a model change. Implementing an unchanged contract requires explaining numerical meaning and checking influence; inconvenience does not justify a fix.

## Choose sufficient rigor

Use a simple model for the accessible question. Escalate solver, detail, or physical prototype once effect, material parameters, observable signature, and grounds for previous-level insufficiency are defined.

Do not demand physical confirmation of abstract research, but do not transfer its result to a physical system without the corresponding justification.

Preserve model/change at the project owner; link its version and material differences to check IDs without duplicating a full description for a form.
