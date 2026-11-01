# Analysis

## Inputs

Use the design question, geometry/data, defined units/metrics, applicable sources and the decision the result should inform. Inspect missing/invalid inputs before choosing a method.

## Procedure

1. Define the comparison or acceptance question, outputs needed and useful accuracy. Choose a qualitative check, bounded calculator or justified external analysis rather than defaulting to the most complex method.
2. Read [performance and coordination](../references/performance-and-coordination.md), [computational design](../references/computational-design.md) or the [calculator contract](../references/calculators.md), as applicable.
3. Record input values, source/revision, unit and metric definitions, method assumptions and supported cases. Explicitly distinguish project targets from applicable normative requirements.
4. Run only a method whose prerequisites are met. Validate nonfinite/impossible inputs and ambiguous units. Preserve failed runs as failures; do not replace unavailable external execution with fabricated numeric results.
5. Check known bounds, independent identities or sensitivity appropriate to the question. Explain whether data/method uncertainty can change the design decision.
6. Interpret the actual result in architectural terms. Glazing ratios do not establish daylight performance; homogeneous U-value does not include junctions; apparent solar geometry does not supply climate/radiation or civil time.
7. For a code-related conclusion, follow [requirements](../references/requirements.md) and verify applicability separately. For Russia, use the relevant [catalog records](../references/normative-catalog.md), then the actual selected provisions and amendments; document currency, selection and design verification are separate questions. A calculator does not decide compliance.

## Result

Report question, method, inputs/units/assumptions, execution status, usable results, interpretation and limitations. If execution is unavailable, provide a prepared bounded check and exact missing capability/data.
