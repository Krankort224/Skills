# Review discovery and execution

These are maintainer checks. Use [trial requests](requests.md), the unchanged fictional [proposal records](proposals.md), and disposable local [file fixtures](prepare_fixture.py). Keep this grading guide, other scenarios and prior answers outside the executor's context.

## Run the comparison

1. Record the exact baseline and candidate revisions. In each native harness (Codex CLI and Hermes), expose one revision at a time through its normal discovery mechanism alongside the ordinary competing skills. Hold model, settings, permissions and starting material constant across that pair, or record the difference.
2. Start a fresh session per quoted request per revision. Supply only the relevant request, its data and the assigned fixture path. Keep the skill name, issue discussion, reference paths and expected results out of prompts. For the procedure handoff, supply the design produced by that revision verbatim to a different executor. Tests and their grading keys are reviewer material; disclose any accidental exposure.
3. Record harness/version, skill revision, exact request and inputs, observable skill and operation reads, actions, output and side effects. Grade discovery, operation and task outcome separately. Hidden load history leaves discovery unknown. Distinguish background host persistence from executor edits. A blocked runtime remains open for that harness. A plan, synthetic session or a mechanically correct result is evidence only of what was observed.
4. For each file trial create a new repository outside the skill-source tree, for example `python3 prepare_fixture.py migration /tmp/unique-new-directory`. Use the `review` mode for the completed handover, and a fresh `migration` fixture for lookup. Capture the initial revision and working diff before the executor starts. The guide, script and fixtures embed no real project contents.

## Grade the requests

**List and assess.** The list returns A–F without starting an investigation. The assessment identifies the following decisions and their evidence. Neither request authorizes edits.

| Record | Evidence and scope of the decision |
| --- | --- |
| A | The operator skipped the existing count check at step 4. Correct the export using that check. |
| B | Repair the export guide's route to the naming guide. The naming rule already covers the case. |
| C | The prefix belongs to each project's delivery specification. The second project needs a different value. |
| D | Cache, header and process state changed together. The cause remains unresolved. A comparison holding input/header and importer conditions fixed could isolate the effect. |
| E | Following v2 exposes an in-scope mismatch. Tag lookup fixes it on reordered input and preserves schedule order on the transfer and previously correct cases. Retain validation and locate the edit in the shared merge operation. Invalid inputs were outside the reported trials. |
| F | The fix corrects quantities yet changes the required order on the second and previously correct third inputs. Withhold this candidate and retain the separately demonstrated gap in v2. |

**Design and handoff.** Grade the supplied procedure and the second executor’s work separately. Look for ownership of each input and release, compatible deliveries, tag uniqueness, missing or unmatched rows, and a way to prepare work while an input is pending. Inspect the procedure for a new mandatory approval even if the executor bypassed it. Record any repair the executor supplied.

| Delivery | Rows or unresolved inputs | Release decision |
| --- | --- | --- |
| 1 | H=12, G=9 | Ready for the authorized preparer to release |
| 2 | H=6, G=4 | Ready |
| 3 | Duplicate H and missing G | Hold for corrected quantities |
| 4 | G=9, H=12 | Ready. Only the schedule order changed from case 1. |
| 5 | The H,G schedule can be prepared. Current quantities are pending. | Hold for the current procurement issue. Previous quantities cannot authorize release. |
| 6 | G=9, H=12, as in case 4 | Hold for the required QA signature. The preparer can finish reconciliation now. |

Score rows and release separately. For cases 1, 2 and 4, distinguish a present decision backed by the executor’s checks from a conditional answer that leaves an unspecified check or record outstanding. Compare case 4 with case 6 to test whether an explicit project control changes only the release decision. A fixed descending sort passes the first three fixtures and fails case 4. Filling a missing sheet from a previous issue fails case 5.

**Numerical and physical evidence.** For the mesh example the successive differences halve from 8 to 4 Pa. First-order extrapolation gives 108 Pa only under a sustained asymptotic trend. Credit diagnosis that scopes the observed mesh dependence and suggests a relevant convergence check, including a finer mesh or verification of solver tolerances. The physical pressure loss requires independent system evidence. For the swapped probes the two pressure differences are 40 and 32 Pa. Swapping reverses the relative offset, giving 36 Pa pressure loss and A-minus-B bias of 4 Pa. Neither absolute bias is identifiable. An engineering answer can finish here.

**Prior work.** Check the [NIST/SEMATECH handbook, section 2.3.3.1.2](https://itl.nist.gov/div898/handbook/mpc/section3/mpc3312.htm). Its test–reference–reference–test sequence cancels common linear drift for equally spaced observations. An arbitrary zero step can leave a bias. Grade the transfer conclusion separately from the search record. Can a colleague locate the decisive passage and identify when and how it was found? Where actions are visible, compare the reported query or direct lookup with the actual one. A suggested query is useful for a future search but does not document the completed lookup. Record any access gap.

**Authorized move.** Compare `release/p04.md` and `history/p04-r6.md` byte-for-byte with the original r7 and r6 Git blobs. Verify the original paths are gone, the two labels in `index.md` resolve to their mapped files, and P-04 and the transmittal IDs survive. Compare `incoming/loose.md`, the existing working edit to `desk.txt`, and the rest of the working tree with their starting states. A request for a plan alone would have a different success condition.

**Review.** Compare the original and migrated commits and the current index. The two drawing moves match `map.txt` and both links work. Both labels offer “Current P-04 plan”; the first opens r6, while the baseline linked r7 as issued and r6 as previous. A recipient can therefore select the earlier revision. Identify the current authority or release record needed if the issue status has since changed. The review should leave the working tree as received.

**Ordinary lookup.** Return `guide/dispatch.md` and its instruction to enter the transmittal ID in the release register. Opening a project guide suffices. Distinguish a lookup from method evaluation.

## Inherited instruction fidelity control

In three separate fresh sessions, give the executor the quoted request below, replacing the bracket with one instruction from the table. Supply only the completed request; preserve the returned rows before grading.

> For unique, matching tag sets, [instruction]. Give the output rows in order for each input. (1) Schedule G,H. Quantity rows H=12,G=9. (2) Schedule H,G. Quantity rows H=6,G=4.

| Instruction | Output 1 | Output 2 |
| --- | --- | --- |
| copy quantities by row position in schedule order | G=12, H=9 | H=6, G=4 |
| look up quantities by tag and emit rows in schedule order | G=9, H=12 | H=6, G=4 |
| look up quantities by tag and emit rows in ascending tag order | G=9, H=12 | G=4, H=6 |

Score fidelity to the supplied instruction separately from the delivery contract, which requires both correct quantities and original schedule order.
