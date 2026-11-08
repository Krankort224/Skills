# Panel, joint and occupied-opening budget

Use this method when a repeated elevation must fit actual components around an
accepted occupied opening. It owns that coupled dimensional budget; [occupied
bays](occupied-bays.md) owns the elevation's order, and [coordination pitch](../../construction/structure/frame-and-core.md#separate-coordination-pitch-component-and-occupied-clearance)
owns the distinction between axes, component outlines and occupied clear faces.
Do not replace a fixed opening or borrow its operating space to regularize panels.

## Contents

- [Define the protected opening and dimensional chain](#define-the-protected-opening-and-dimensional-chain)
- [Test installation error and service movement separately](#test-installation-error-and-service-movement-separately)
- [Compare repairs at the actual interface](#compare-repairs-at-the-actual-interface)
- [Worked failure and conditional correction](#worked-failure-and-conditional-correction)
- [Retest a changed opening](#retest-a-changed-opening)
- [Carry the budget through the junction](#carry-the-budget-through-the-junction)
- [Source and completion boundary](#source-and-completion-boundary)

## Define the protected opening and dimensional chain

Record one datum, units, measured end/corner faces and their uncertainty. Keep the
required occupied aperture distinct from frame outside, rough opening, reveal,
support and fixing zones. Establish a protected opening reservation that contains
those interfaces and the accepted opening/control operation. Record which faces
are fixed, which may change, and who can authorize a change. An opaque trim over
glass can preserve the frame outline while reducing the usable view/light aperture.

Split the facade at each protected opening, corner or other fixed interface.
For each resulting opaque strip, list the actual sequence from end to jamb:
end interval, panel outlines, internal joints, closure component and jamb interval.
Count each physical interval once; a shared joint is not two full gaps. Record
whether a dimension is a visible face, cut outline, overlap or concealed fixing
zone. Sum on one plane and direction; a folded return is not its projected width.

For a strip of length `S` with one adjustable internal gap `g`, write
`g = S − e − k − Σp`, where `e` and `k` are the assigned end and jamb intervals
and `Σp` includes every actual panel/closure width. For several joints use their
explicit sum and positions first; the same total gap can hide a locally closed
joint. A positive residual is not permission to distribute it arbitrarily.

## Test installation error and service movement separately

Use project/supplier inputs or stated study assumptions for component deviations,
survey/setting uncertainty, adjustment travel and the admissible service gap.
Retain their source/status and included effects. Installation uncertainty concerns
where the completed pieces start; service movement concerns how they subsequently
approach or separate. Do not infer either from a material name or count the same
deformation in both allowances. Missing bounds leave the dependent fit unresolved.

For nominal dimensions, calculate `g0 = S0 − e0 − k0 − Σp0`. With independent
signed bounds but no justified correlation, use the conservative sum
`U = uS + ue + uk + Σup`. Then `g_inst` lies in `[g0 − U, g0 + U]`.
This is a bounded dimensional check, not a statistical tolerance prediction.
Use a different interval calculation when actual one-sided bounds are supplied.

Let supplied movement allowances be closure `C ≥ 0` and opening `O ≥ 0`, and the
admissible service gap be `[rmin, rmax]`. Require both
`g0 − U − C ≥ rmin` and `g0 + U + O ≤ rmax`.
Equivalently the nominal gap must lie in `[rmin + U + C, rmax − U − O]`.
An empty interval means that changing nominal panel widths alone cannot solve
the stated uncertainty/movement conflict. Do not select only the favorable signs.
For correlated movements or several restraints, obtain the actual relative-motion
bounds and test each joint; do not assume movement divides equally among them.

## Compare repairs at the actual interface

| Alternative | Constructive change and consequence | Condition before retaining it |
| --- | --- | --- |
| Retain repeated panel sizes and revise joint/end arrangement | A different closure, independent opening surround or qualified joint system can decouple the visual rhythm from the frame. It changes joint count, depth, support and sometimes the apparent opening. | Rebuild every local interval and confirm the actual adjustment/movement bounds. A wider visible seam does not establish a wider permitted service gap or concealed overlap. |
| Retain opening and interface reservations; fit a closure component | Keep the repeated field where useful and determine the last component from the measured strip and actual preceding pieces. This introduces a special size/hand and a later dimensional commitment. | Establish measurable faces, cut/installation sequence, achievable residual error and permitted closure range. A label “cut to fit” supplies none of those inputs. |

Compare corner/end appearance, aperture loss, supplier/component families, access
and replacement as well as the sum. A repair requiring another party's change
remains conditional until that change is established. Prefer neither alternative
solely because it has fewer nominal panel types or a more regular elevation.

For a fitted closure, establish the measurement state: retained frame/end faces,
support setting and actual preceding components must be identifiable before its
size is committed. Select the intended installed gap, subtract the measured
component/interface chain, then include measurement, cutting and later setting changes
in the remaining error bound. Check that bound and the closure's smallest/largest
outline before repeating the arrangement. A nominal design dimension cannot
substitute for an unavailable face measurement.

## Worked failure and conditional correction

All following dimensions, bounds and permitted ranges are original hypothetical
project inputs, not product capabilities, material properties or recommendations.
On a nominal 4800 mm frontage protect an opening reservation from x=1700 to
x=3100; its already tested occupied aperture, frame and controls remain inside
that reservation. Each opaque strip is nominally 1700 mm. Test both independently.
For one strip retain actual end/jamb intervals `e=10`, `k=16`, with their setting
already resolved for this study; strip uncertainty is ±2 mm and each panel's
width deviation ±1 mm. The selected service-gap range is 8–18 mm, with relative
closure/opening allowances `C=3`, `O=2`. Actual projects must establish these inputs.

**First failure.** Two nominal 840 mm panels, a 12 mm joint and the end/jamb
intervals need `10 + 840 + 12 + 840 + 16 = 1718 mm`: 18 mm too much. Moving a
jamb 18 mm into the protected opening would spend accepted aperture/interface
space. The panel rhythm is the variable to repair under this boundary.

**Nominal repair still fails.** Two 831 mm panels give `g0=12` and an exact
1700 mm nominal total. But `U=2+1+1=4`: the service gap can reach
`12−4−3=5 mm`, below 8 mm. Indeed the permitted nominal-gap interval is
`[8+4+3, 18−4−2]=[15,12]`, which is empty. Redrawing a wider nominal joint or
shrinking both panels cannot make all the supplied bounds compatible.

**Closure alternative.** Retain one nominal 831 mm field panel and target a
14 mm installed joint. Determine the closure from the measured strip and actual
field panel: `p_closure = S − 10 − 16 − 14 − p_field`, nominally 829 mm.
The proposed project reservation permits closure widths 800–860 mm, subject to
actual edge/fixing/removal checks. To retain this option, its measurement, cutting
and setting arrangement must establish a combined residual gap error no greater
than ±1 mm, including unresolved measurement error. This requires a revised,
verified measurement/setting proposal; the original ±2 mm survey uncertainty
cannot simply be relabeled ±1 mm. Known dimensional variation changes the closure
size; remaining error governs the gap. No workshop capability is claimed.
Under that condition `g_inst=13–15`, so service gaps stay within
`[13−3, 15+2]=[10,17] mm`, inside 8–18 mm. Allowing for ±2 mm strip variation,
±1 mm field-panel variation and that final ±1 mm residual, closure widths are
825–833 mm. They fit the study reservation; support and assembly remain unverified.
If the residual error cannot be established, retain the failure and compare the
different joint/end arrangement rather than silently assigning tighter tolerances.
This checks the named internal joint; end/jamb movement and interface capacities
still need their own selected checks.

## Retest a changed opening

Suppose an authorized revision widens the protected reservation to x=1650–3150,
leaving each opaque strip nominally 1650 mm. The former field/closure convention
now needs a nominal closure `1650−10−16−14−831=779 mm`, below the selected 800 mm
reservation. The former conditional result no longer applies. One alternative
is a new 780 mm field component with nominal closure 830 mm; under the same
stated bounds its closure range is 826–834 mm. It retains the joint budget but
changes a component family and the elevation's order. Compare a revised surround
instead, and recheck the newly authorized aperture, privacy, light and controls;
do not pull its jamb back simply to reuse the original panel schedule.

## Carry the budget through the junction

Check the chosen edge in plan and section through the [opening junction](../../construction/envelope/assemblies.md#opening-head-jamb-and-sill)
and [compatibility/removal method](../../construction/envelope/assemblies.md#compatibility-movement-and-replaceability).
Place real supports, adjustment and restraint points, seals, flashings, insulation
and drainage exits without consuming the protected aperture or fixing the very
joint intended to move. A cladding gap is not automatically an air/water seal or
fire separation. Keep attachment and replacement access, including the actual
panel extraction direction and neighboring pieces. For a displaced frame, return
to the [opening's support/use](../../construction/structure/walls-floors-openings.md#develop-a-wall-opening-as-support-and-use)
and [occupied light/view/control](../../performance/comfort/daylight-view.md) checks.
Use [material expression](../material-expression.md) for joint/grain/handedness
choices; matching widths do not make differently edged or oriented panels identical.

## Source and completion boundary

This is original dimensional synthesis extending the linked local owners; no
fresh source inspection, material coefficient or supplier performance is claimed.
Report fixed faces, dimensional chain, signed bounds, failed extreme, retained
alternative and its dependencies in the requested representation. Hand arithmetic,
a spreadsheet, code or a drawing can carry the same explicit budget; inspect the
actual result and preserve its units and assumptions. This method establishes
conditional dimensional compatibility, not a fabrication schedule, connection
design, tested movement capacity, weather performance or regulatory approval.
