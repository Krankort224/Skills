# Completion for the requested architectural use

Use the selected method to decide what the delivered design actually establishes.
Completion depends on the recipient's task, accepted requirements and available
evidence. A stage name, matching identifiers or a polished image cannot establish
that evidence. Keep project facts and decisions in their existing authoritative
locations; these methods require no new register or compulsory document suite.
Example dimensions below are hypothetical design inputs, not standards,
measurement accuracies or construction tolerances.

## Contents

- [Derive evidence for the requested use](#derive-evidence-for-the-requested-use)
- [Reconcile schedule membership and field meaning](#reconcile-schedule-membership-and-field-meaning)
- [Match precision to the decision](#match-precision-to-the-decision)
- [Close the revision and state remaining conditions](#close-the-revision-and-state-remaining-conditions)

## Derive evidence for the requested use

**Decision and inputs.** Determine whether the recipient can make the requested
decision from the proposed result. Use the actual request, intended use/stage,
accepted brief and baseline, available geometry and property evidence, and chosen
format. If a stage label is ambiguous, identify the action it is meant to support:
choosing an arrangement, agreeing a room boundary and its consequences, locating
work from controlled dimensions, or confirming a stated property. These actions
need different evidence even when someone calls all of them “developed design.”

1. Express the intended use as a concrete action and identify the claims on
   which it depends. “Compare two consultation-room arrangements” depends on
   their activity fit, independent access and relevant privacy/separation
   consequences. “Set out the accepted wall” also depends on a controlled wall
   location, measurement faces, datum and resolved thickness. Do not infer those
   additional facts from a convincing option narrative.
2. For each consequential claim, reconstruct its physical mechanism. A room's
   independence needs its own usable connection, not merely a second room name.
   A separation needs a continuous boundary and treatment of openings and the
   ceiling zone, not merely a finish hatch. Identify the smallest evidence that
   would reveal a failure of that mechanism. Use the actual project information;
   explanatory text can state relationships, while a requested controlled plan
   must express the positions and dimension basis it is intended to communicate.
3. Test the weakest dependency before adding presentation detail. Ask what
   plausible condition, still compatible with the supplied information, would
   reverse the claimed conclusion. If the unknown partition thickness could
   erase the activity envelope, it is a fit dependency. If only paint color is
   undecided, it need not prevent an arrangement comparison. Resolve the former,
   bound it as a study assumption, or narrow the conclusion explicitly.
4. Choose information that distinguishes the live alternatives. A plan can
   expose route and furniture conflicts; a section or precise textual junction
   explanation can expose a separation stopping at a shared ceiling. Select a
   cut through the actual uncertainty using
   [section selection](design-development.md#choose-sections-that-test-the-solution).
   When a view is needed, use [visual delivery](visual-delivery.md#choose-a-useful-representation)
   for its information and inspection. Additional views that repeat an already
   demonstrated fact do not repair a missing dependency.
5. Compare the evidence with the whole requested result. If the task requests a
   revised arrangement, perform the permitted spatial correction; merely stating
   the defect is insufficient. If a critical input cannot be resolved, complete
   the independent design work and state the exact claim and use still blocked.
   Change the delivered conclusion to match the evidence; do not silently lower
   the brief to fit the available material.

**Worked failure and correction.** A user requests a textual study of replacing
one meeting room with two independently accessed consultation rooms, preserving
the enclosing bay and its two windows. The first explanation says “divide the
room equally; both have daylight and acoustic privacy.” It neither locates the
partition relative to the windows nor explains access or the ceiling boundary.
Those omissions affect the claimed arrangement; the absence of an illustration
does not cause the failure.

Use the hypothetical [R2 geometry](design-development.md#propagate-a-changed-client-constraint):
the new partition occupies the solid interval between the fixed openings; each
finished room is 2.175 × 4.350 m and accepts the supplied 2.100 × 4.000 m activity
envelope. Give each a door from the shared route and describe the door/furniture
approach together. Explain that the separation continues through the ceiling
zone and identify the termination and penetrations whose performance remains
unverified. Revise the conclusion to “the stated activity envelopes fit under
these design inputs and each room retains an opening; each has a proposed direct
door to the shared route, with door/furniture approaches still to be checked;
daylight adequacy and the acoustic property are unverified.” The envelope and
opening decisions are developed; the independent-access conclusion remains
conditional until its actual operating geometry is checked. A textual study
can express those relationships and limits. A room with a window has neither proven daylight
adequacy nor proven privacy simply because the schedule calls it consultation.

If the request instead requires a dimensionally controlled setting-out plan,
that text is insufficient. Supply the requested location/datum/dimension content
and resolve or explicitly withhold dependent setting-out decisions. The choice
between a provisional comparison and a committed location trades early decision
speed against dependency resolution; it never changes an unknown into a fact.

**Critical checks and limits.** Trace every promise in the delivered conclusion
to actual evidence and check that the result still answers the user's request.
A concept may be complete for an arrangement comparison while a requested
property confirmation remains incomplete. Legal stage/scope claims require the
actual jurisdiction and applicable evidence through
[requirements](requirements.md#select-a-jurisdiction-module); unknown location
does not default to any jurisdiction. This method establishes adequacy for a
specified use, not universal project completeness or legal approval.

## Reconcile schedule membership and field meaning

**Decision and inputs.** Make a requested schedule describe the actual selected
revision without omitted, duplicated or semantically substituted items. Use the
accepted geometry and identities, the relevant existing schedule/notes, field
definitions, selected alternatives and source status. Read only the schedules
affected by the change. Use
[issued-item coordination](../operations/documentation.md#coordinate-a-design-issue)
for reconciling a decision across outputs; the method here resolves membership
and meaning within the affected scheduled information.

1. Establish what a row represents before comparing counts: a physical room,
   door occurrence, shared door type, finish face, assembly or alternative.
   Establish each critical field's boundary, units and conditions. “Width” may
   mean a leaf, rough opening or clear passage; “area” may mean finished room
   floor or a reservation including walls. Equal numbers with different meanings
   do not agree. Keep different physical measures in separate defined fields
   or notes rather than forcing them into one convenient number.
2. Trace the change from old membership to new membership. For a split, retire
   the old room from the active room total and introduce each resulting room
   once. For a merge, retire the contributing rooms and introduce the combined
   room once, accounting for any retained obstruction or changed wall allocation.
   For a relocation, retain the occurrence identity when it is the same item
   under project conventions and change its location/relationships. Do not reuse
   a retired identity in a way that makes historical and current meanings
   indistinguishable. Preserve history through existing project conventions;
   historical rows must not remain counted as active work.
3. Separate type from occurrence. A shared type can describe common construction
   while each occurrence has its own location, handing, adjoining rooms and
   local approach. Two openings using one type are two occurrences, not one
   door. A type table is not an additional collection of physical doors. If one
   occurrence needs a different property, choose an explicit local exception or
   a different type according to the project's conventions; silently editing the
   shared type would also change every other recipient.
4. Recompute dependent values from the selected geometry and original metric
   basis. Use [area accounting](program/area-ledger.md#how-can-areas-be-counted-once-and-compared)
   for floor/room allocations and
   [architectural takeoff](operation-and-lifecycle.md#count-the-architectural-work)
   for face/return/piece/installed/procurement scope. Check membership and totals
   independently: a duplicated row and a missing row can cancel numerically.
   Label a subtotal with missing values as partial; an unknown is not zero.
   Exclude unselected alternatives from active totals while preserving their
   stated comparison role if they are still requested.
5. Read material/property fields as claims. An appearance intention, a selected
   product, a required property and evidence that an actual assembly achieves
   that property have different meanings. State the property, conditions and
   evidence status where it matters. A product choice cannot verify an assembly
   whose substrate, joints, penetrations or installation differ from its evidence.
   Keep unknown availability, quantities or properties explicit rather than
   filling the cells to make the table look complete.

**Worked split and field correction.** In the hypothetical R2 revision the old
meeting-room allocation is 19.575 m². A stale room schedule lists that room
alongside two new rooms of 9.46125 m² each. Its active room subtotal becomes
38.4975 m² for space that has only one former allocation. Retire the old room
from active membership. The two finished rooms total 18.9225 m²; account for the
new 0.6525 m² partition reservation in its proper category, so the same spatial
boundary still reconciles to 19.575 m². Do not enlarge either room's reported
clear area to absorb the wall. This consumes the area owner's basis, rather
than inventing a new statutory metric.

The two new route doors may share a type, but each needs its own occurrence and
correct room relationship. If the type's supplied 1.000 m is a leaf width while
the occurrence schedule labels it “clear passage,” correct the field meaning;
frame, open position and hardware geometry are still needed to establish clear
passage. Do not resize the accepted opening merely to make two unlike fields
equal. If a former door is removed, retire it; if it is reused, show its current
location once. The type row is not a third installed door.

A finish note “timber appearance” on the new separator also cannot populate an
“acoustic rating verified” field. Keep the finish intent, the separation's
performance requirement and the unverified assembly evidence distinct. If a
later verified build-up changes thickness, return to the physical room fit and
then update dependent schedule values. Correcting a claim in a table does not
perform that spatial revision.

**Alternatives, checks and limits.** A type with explicit local exceptions can
avoid unnecessary type proliferation, but makes occurrence-level reading more
important; a separate type makes a consequential difference more visible but
must not imply a different product without evidence. Use existing conventions
and the recipient's actual decision. Check both directions: every active physical
recipient appears with the right meaning, and every active scheduled occurrence
has a physical recipient. Inspect the final rendered table or actual text after
editing. Correct arithmetic and matching tags establish neither usable geometry
nor a tested property, purchasable quantity, price or product availability.

## Match precision to the decision

**Decision and inputs.** Report dimensions, areas and properties at a resolution
that supports the actual decision without overstating their basis. Use original
input status, measurement endpoints/datums, units, calculation relationships and
the decision's limiting condition. Distinguish supplied survey measurement,
accepted design allocation, calculation, provisional reservation and illustrative
proportion. More displayed digits do not improve the weakest input.

1. Recover what the number means and where it comes from. A finished-face width
   calculated from assumed linings remains conditional on those linings. A
   nominal component designation cannot replace a measured clear dimension.
   Consume [datum and dimension meanings](design-development.md#establish-datums-and-dimension-meanings)
   rather than assigning new endpoints during presentation.
2. Identify the decision threshold or relationship that must remain visible:
   positive clear fit, closing dimension chain, acceptable area basis, or a
   comparison whose ranking might reverse. Retain the unrounded calculation for
   this check. Choose display rounding only after assessing its consequence;
   calculate totals from underlying values, and explain a relevant rounding
   discrepancy rather than altering an input to force displayed sums to close.
3. Test uncertainty where it can reverse the result. Use source-supported bounds
   or explicitly identified study alternatives, never an invented error margin.
   If the input is only unknown, say which missing face/build-up/measurement
   prevents the conclusion. A study can expose the maximum total build-up that
   would fit; it cannot assert that the eventual assembly will stay inside it.
4. When the intended use becomes more committed, obtain the newly necessary
   evidence before promoting the claim. A wall reservation used to compare
   arrangements needs actual thickness/location evidence before it supports
   finished-clear setting out. Recalculate affected fit if that evidence changes
   the reservation. Adding decimals to the former value is no transition in
   knowledge.

**Worked rounding failure and correction.** Suppose a client has supplied a
2.300 m minimum clear width for an activity, and a hypothetical dimension chain
leaves 2.295 m. Displayed to two decimals, both read 2.30 m; a summary claiming
“fits at 2.30 m” conceals a 0.005 m shortfall under those inputs. Keep the
unrounded comparison and report the failed fit. If geometry is permitted to
change, move the responsible boundary enough to provide the required clear
width and recalculate the neighboring room; if it is fixed, compare another
arrangement or request an authorized requirement/boundary change. Do not borrow
space from an accepted route or describe the discrepancy as within tolerance.
No construction or measurement tolerance was provided by this arithmetic.

If the available 2.295 m itself comes from an unverified lining assumption,
there are two separate results: that trial's arithmetic fails, and the actual
finished width remains unknown. A later survey or verified build-up may change
the trial, but an unknown cannot be used as a positive clearance. Conversely,
an exact calculation of 9.46125 m² from R2's hypothetical rectangular inputs
does not claim surveyed area accuracy to five decimal places. An explanatory
schedule may show 9.46 m² with its design basis while retaining underlying
values for reconciliation. Two displayed 9.46 m² rooms sum to 18.92 m²; that
rounded presentation must not replace the underlying 18.9225 m² when reconciling
the wall allocation or testing a close limit.

**Alternatives, checks and limits.** Early reservations allow useful comparison
without pretending to know a selected assembly; resolving the assembly first
reduces dependent uncertainty but may constrain options prematurely. State
which choice serves the requested use. Check dimensions and totals at their
original precision, then read the rounded output as the recipient will. Use
explicit source tolerances only within their stated scope. Unknown survey
accuracy, product variation or installation allowance remains unknown; no
generic tolerance, universal significant-digit rule or illustration-based
measurement follows from this method.

## Close the revision and state remaining conditions

**Decision and inputs.** Decide whether the final delivered revision supports its
stated use after the last consequential edit. Use the accepted baseline, actual
change, final requested outputs, evidence from performed checks and unresolved
dependencies. For spatial revision use
[physical correction and propagation](design-development.md#turn-critique-into-a-spatial-correction);
for cross-output reconciliation use
[coordinate a design issue](../operations/documentation.md#coordinate-a-design-issue).
This method evaluates their final consequences; it does not replace either owner.

1. Find what the final change invalidates. A relocated opening can invalidate
   approach and furniture checks even if its width stays fixed. A thicker wall
   can invalidate a room fit and quantity without moving the external boundary.
   Select and rerun the affected earlier checks against the new geometry and
   actual operating conditions. Successful checks on the superseded revision
   remain history, not evidence for the changed interface.
2. Reconstruct the requested result from its delivered form. Start as the
   recipient would: follow the described arrival/door/activity sequence, the
   dimension/level relationship, or the scheduled room/material recipient.
   Include the local open/closed and occupied conditions relevant to the claim.
   Check that the final wording and any final artifact expose the same decision
   and limitations. Inspect requested artifacts after the last material edit;
   an earlier inspection or the author's change description cannot establish
   what the final recipient sees.
3. Judge each unresolved item by its consequence. A known conflict with a fixed
   requirement blocks claiming that requested fit. Missing critical evidence
   blocks its dependent claim even if no failure is yet demonstrated. An
   explicit assumption may support a conditional study when the intended use
   allows it, its physical failure threshold is visible and the recipient is
   not being asked to rely on the unknown as established. Independent later
   work can remain open when it cannot invalidate the current decision. Do not
   relabel a critical missing fact as later work just to finish the package.
4. Resolve or expose the consequential choice. Offer architectural alternatives
   that change the cause, with the cost to room fit, access, external exposure,
   expression or maintenance made explicit. If authority to change a fixed
   requirement is absent, preserve it and state the incompatible facts. Continue
   independent results. Rank open items by what they prevent and by how much
   rework their late resolution could cause, rather than assigning an unexplained
   generic severity score.
5. Deliver the achieved decision and reason, actual changed content, performed
   checks and remaining conditions in the requested form. For each material
   condition, name the missing fact/decision, its existing owner where known,
   affected physical interface and consequence before the result can serve the
   more committed use. “Specialist review required” alone identifies neither
   the dependency nor what the architecture currently reserves.

**Worked closed-revision failure and correction.** In R2, the two room envelopes
fit and each room has a proposed direct door to the shared route. Independent
access remains conditional on checking door operation, furniture and approaches.
A final explanation still says the new separation provides acoustic privacy,
while its only junction information
ends at a common suspended ceiling. Matching room tags and a reconciled area
total cannot close that physical dependency. Correct the architectural intent
by continuing the separating boundary through the ceiling zone to its stated
termination and identifying penetrations and access closures. Revise the affected
ceiling/access arrangement if the new wall interrupts it. Then remove the
unsupported performance conclusion: the boundary continuity is developed, but
the actual assembly/junction property remains unverified. The spatial study can
explain the proposed two-room arrangement with that access condition explicit;
a requested verification of acoustic performance is still incomplete.

If obtaining the relevant assembly evidence requires a thicker partition,
recheck both rooms, the window-pier termination and door approaches before
calling that revised fit complete. A different build-up may preserve room width
but change cost, appearance or attachment; a relocated partition may improve
one room while reducing the other or striking an opening. These consequences
need actual project evidence and permitted geometry, not invented product data.

The R2 counterexample is a different outcome: two required 2.300 m clear widths
plus the 0.150 m partition need 4.750 m inside a fixed 4.500 m width. That is a
demonstrated 0.250 m incompatibility. A conditional acoustic note cannot cure
it. Compare another arrangement or obtain an authorized boundary/brief change;
do not deliver a claim that the stated two-room requirement fits. A decorative
finish color left open may be independent of this fit, but a finish thickness
on which the clearance depends is not.

**Critical checks and limits.** Read the final conclusion against the actual
revision and each material unresolved item: does a promise still rely on an
unknown, superseded geometry or an unperformed check? State completed correction,
conditional study and remaining action distinctly. If a requested artifact or
critical tool capability was unavailable, identify the actual missing result;
a prompt or plan to make it is not that result. This readiness judgment is for
the requested architectural use. It confers neither Issue acceptance nor legal,
construction, product or engineering approval, and it predicts no guaranteed
outcome on a future project.
