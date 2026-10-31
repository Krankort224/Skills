# Optimization

## Inputs

Use the accepted baseline, controllable variables, fixed constraints, candidate options and project-specific evaluation criteria. Identify decisions already accepted by the user.

## Procedure

1. Read [computational design](../references/computational-design.md). Define variable ranges, derived values, hard constraints and preference criteria with their source and units.
2. Reject or flag infeasible alternatives before preference scoring. Unknown constraints remain unresolved; do not interpret missing evidence as a pass.
3. Generate or compare a bounded set of architectural options using 2D/numeric representations. Vary meaningful layout, composition, facade, orientation or material decisions without authoring a building/3D/mesh model.
4. Evaluate candidates with the same definitions, assumptions and methods. Use [analysis](analysis.md) for required checks and retain evidence for each result.
5. Explain trade-offs. Do not add unlike units or invent stakeholder weights; use a transparent qualitative or Pareto comparison when preferences are not fixed.
6. Check sensitivity to uncertain inputs and proposed weights where it could change the choice. A few alternatives do not prove a global optimum.
7. Recommend the feasible direction that best matches the stated priorities. Keep unaccepted changes as proposals and preserve the accepted baseline.

## Result

Return variables/constraints, comparable options, feasibility findings, trade-offs and a justified recommendation with uncertainty. Make the decision reversible and traceable to the project brief.
