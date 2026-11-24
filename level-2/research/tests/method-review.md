# Evaluating working methods

Use these checks when evaluating changes to the skill. The worksheet trials in [the proposal records](proposals.md) are synthetic givens. They supply inputs for a decision and do not constitute observations of a live harness.

## Selection

In Hermes and Codex CLI, use the same skill revision and ordinary discovery settings. Start a fresh session for each request. Supply the text of the proposal records and one of the following questions, without a source path, skill hint, issue discussion, grading notes or previous answer.

1. “List the proposals”
2. “Which of these proposals, if any, justify changing a shared skill, and why?”

Record the harness and version, skill revision, prompt, answer and observed tool actions. Grade the answer and any visible skill selection separately. An acceptable answer with unavailable load history leaves selection unknown. Disclose access to grading material if it occurred. Check for attempted edits within the task and distinguish them from background persistence by the host. An unavailable native run remains open for that harness.

The first answer should list A–F without investigating or editing them. For the second, judge the decisions by their supporting evidence:

| Record | What the evidence supports |
| --- | --- |
| A | Follow step 4 and correct the export. The episode supplies no reason to repeat the existing instruction. |
| B | Correct the broken route at the export guide. The naming guide already covers this case. |
| C | Keep the prefix in each project's delivery specification. The other project's requirement rules out the proposed universal value. |
| D | The cause remains unresolved. A useful check would compare cache state with the same input/header and importer conditions. The recollection supplies no such comparison. |
| E | Propose the tag lookup at the shared merge operation, retaining schedule order and validation. The first row exposes the failure despite following v2. The second tests transfer and the third protects already-correct behavior. No supplied trial exercised invalid tag sets. |
| F | The original quantity mismatch is fixed, but the aligned B,A schedule is reordered. The second schedule also loses its order. Withhold this version and retain the independently demonstrated gap in v2. |

## Applying the instructions

To observe execution as well as interpretation, give an executor the following request in three fresh sessions. Replace the bracketed sentence each time with one instruction from the table. Supply only the completed request. Record the executor's outputs before comparing them with the expected results.

> For unique, matching tag sets, [instruction]. Give the output rows in order for each input. (1) Schedule G,H. Quantity rows H=12,G=9. (2) Schedule H,G. Quantity rows H=6,G=4.

| Instruction | Expected output 1 | Expected output 2 |
| --- | --- | --- |
| copy quantities by row position in schedule order | G=12, H=9 | H=6, G=4 |
| look up quantities by tag and emit rows in schedule order | G=9, H=12 | H=6, G=4 |
| look up quantities by tag and emit rows in ascending tag order | G=9, H=12 | G=4, H=6 |

The delivery contract requires both the quantity for each tag and the original schedule order. Score fidelity to the supplied instruction separately from meeting the delivery contract. Running a lookup script alone cannot show whether an agent followed a written instruction.

## Ordinary engineering use

In a fresh session, supply only this question:

> In a steady air duct, probe A at the upstream tap read 150 Pa and probe B at the downstream tap read 110 Pa. With flow held fixed, the probes were exchanged. B read 146 Pa upstream and A read 114 Pa downstream. Assuming constant additive probe offsets, estimate the pressure drop. Does either probe's absolute offset follow from this test?

The two differences are 40 Pa and 32 Pa. Exchanging probes reverses the offset difference, giving a pressure drop of 36 Pa and an A-minus-B offset of 4 Pa. Neither absolute offset is identifiable. The response should address the engineering question without introducing a skill review.
