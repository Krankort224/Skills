# Optimization

## Inputs

Use the accepted baseline, controllable variables, fixed constraints, candidate options and project-specific evaluation criteria. Identify decisions already accepted by the user.

## Procedure

1. Use the [decision frame](../references/computational-design.md#frame-the-question) and [alternative generation](../references/computational-design.md#generate-controllable-alternatives) to establish fixed/variable/derived inputs, hard constraints, unknown prerequisites and preference criteria with their sources and units.
2. Reject or flag infeasible alternatives before preference scoring. Unknown constraints remain unresolved; do not interpret missing evidence as a pass.
3. Generate or compare a bounded set of architectural options using 2D/numeric representations. Vary meaningful layout, composition, facade, orientation or material decisions without authoring a building/3D/mesh model.
4. Evaluate candidates with the same definitions, assumptions and methods. Use [analysis](analysis.md) for required checks and retain evidence for each result.
5. Apply [consistent comparison](../references/computational-design.md#compare-options-consistently). Explain trade-offs, avoid adding unlike units or inventing stakeholder weights, and distinguish non-dominated options from a stakeholder preference.
6. Use [sensitivity and reproducibility](../references/computational-design.md#test-sensitivity-and-reproducibility) when uncertainty or weights can change the recommendation. Check meaningful interacting assumptions; a few alternatives do not prove a global optimum.
7. Recommend the feasible direction that best matches the stated priorities. Keep unaccepted changes as proposals and preserve the accepted baseline.

## Result

Return variables/constraints, comparable options, feasibility findings, trade-offs and a justified recommendation with uncertainty. Make the decision reversible and traceable to the project brief.
