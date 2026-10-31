# Computational thinking for design decisions

Use structured comparisons to make architectural choices inspectable. This is
an aid to design judgment, not a modeling or optimization implementation. For
eligible numerical estimates see [calculators](calculators.md); for design inputs
see [program and space](program-and-space.md).

## Frame the question

State the decision and alternatives, for example whether two arrangements
better balance required adjacency, usable area and daylight opportunity. Identify
stakeholders and decisions the comparison must support. Keep the scope small
enough for its inputs and evaluation methods to be explained and reviewed.

## Define inputs and relationships

- List fixed inputs with source and confidence: site, program, access and known
  constraints. A fixed input may still be uncertain; record that uncertainty.
- List independent choices that vary between options: for example plan
  arrangement, orientation, entrance position or number of rooms.
- List derived outputs and their calculation or judgment method: areas,
  adjacency satisfaction, qualitative daylight exposure and estimated cost if
  a defensible basis is supplied. Distinguish measured from inferred values.
- Classify verified requirements as constraints, client preferences as goals,
  and unresolved requirements as open questions. Do not turn an assumption
  into a legal constraint merely by entering it in a table.
- Set units, ranges and input provenance before comparing; reject inconsistent,
  missing or out-of-date data, or flag the resulting limitation explicitly.

## Compare options consistently

Use the same boundary, program and assumptions across options. Name the option,
its parameter values and revision, method, output units, missing information,
and the criteria used. Include a simple table and drawings where useful. Avoid
false numerical precision and do not combine unlike measurements into a score
without explaining normalization, weights, stakeholders and omissions.

Describe conflicts rather than hide them in one ranking: an option can improve
adjacency while reducing privacy or increasing exposed facade. A calculation
is conditional on its inputs and method; a qualitative judgment needs its
rationale. Mark infeasible or unverified options and state why. The choice
remains a design decision, with client and specialist involvement as needed.

## Test sensitivity and reproducibility

Change one uncertain input at a time over a plausible, explicitly stated range,
recalculate or reassess consistently, and show whether the preference changes.
Where interactions matter, also test meaningful combinations. Sensitivity is
not a probability forecast and cannot compensate for missing evidence.

Keep the input data, source dates, definitions, formulas where applicable,
assumptions, option identifiers and revisions, output table and limitations
together so another person can repeat the comparison. Identify which results
are approximate and which require simulation or specialist verification.

## Boundary and handoff

Use descriptive parameters and 2D diagrams here. Do not author building, BIM,
3D or mesh models, or implement a tool-specific parametric workflow. When a
model is later explicitly requested, provide the selected concept, dimensions,
coordinate and unit assumptions, source data, revision, unresolved issues and
required checks as a handoff for the separately requested workflow.
