# Operation and lifecycle

Use these methods when an architectural choice changes operation, access,
maintenance or replacement over time. They develop a bounded assembly or space,
not a whole-building estimate or maintenance specification. The existing
[maintenance and durability](performance/lifecycle/durability.md#durability-and-maintenance-of-materials)
method owns exposure and material selection; [compatibility and replaceability](envelope-and-assemblies.md#compatibility-movement-and-replaceability)
owns the component removal sequence. Select them when exposure or removal is
part of the current decision, then carry the affected operation and consequences
through the matching method below. Use
[consistent comparison](computational-design.md#compare-options-consistently) and
[sensitivity](computational-design.md#test-sensitivity-and-reproducibility) for
eligibility and decision rules; the cost exercise here supplies inputs to them.

## Contents

- [Trace a complete maintenance journey](#trace-a-complete-maintenance-journey)
- [Design for intervention over time](#design-for-intervention-over-time)
- [Count the architectural work](#count-the-architectural-work)
- [Compare equivalent function over time](#compare-equivalent-function-over-time)

## Trace a complete maintenance journey

**Decision and inputs.** Test whether inspection, cleaning, local repair and a
plausible replacement can actually occur while the surrounding place operates.
Select one component and task, its location and access face, likely tools and
piece size from available product or operator information, the existing routes,
occupancy schedule and permitted temporary working area. Distinguish known
conditions from proposed reservations and unknown operator requirements. A
maintenance hatch or a reachable fixing alone does not demonstrate a journey.

**Procedure.** Follow the worker, equipment, removed piece, waste and replacement
from arrival to return to service. Draw plan and section at the bottlenecks:

1. Arrival, unloading and transfer: identify the external approach, vehicle or
   lifting position if needed, entry, turns, thresholds and vertical transfer.
   Does the largest actual piece pass in its required orientation? Reserve space
   for handling and protected storage of both old and new pieces, not just a
   nominal clear width. Check whether the route depends on land or spaces not
   controlled by the operator.
2. Establish a work zone: show approach and working faces, opening/swing and
   extraction path, equipment setup and exclusion or protection zone. Identify
   who and what is displaced, including public movement and neighboring activities.
   Determine when the space is available, who grants access, and where work
   supplies and waste can wait. A direct path may still be unusable during the
   only operating window.
3. Perform the selected operation using the existing removal sequence. Trace
   observation and cleaning of the actual failure point, not merely the visible
   finish. For replacement, track the full piece through the tightest turn, support
   interfaces and closures. Identify services or control layers interrupted and
   how they are restored; reserve any temporary protection or support as an
   explicit specialist-designed dependency, not an assumed capacity.
4. Remove waste and reinstate: allow cleaning, compatible closure and restoration,
   inspection/testing appropriate to the actual system, and return of users and
   equipment. Record the affected duration as an input or unknown, including
   preparation and reinstatement. A task is incomplete while its protective
   layer or ordinary route remains out of service.

**Alternatives and checks.** Compare an accessible service side, movable furniture,
a separately approached recess, a different component module or scheduled
closure. Each spends area, changes appearance or affects operations. Test the
ordinary condition and the maintenance condition on the same plan: a temporary
route must reach its destination and coexist with the work zone. Identify a
fallback when the only route is blocked and who is responsible for confirming
its availability. Inclusive access, fire and safety requirements and actual
handling methods require project-specific verification; a sketch does not prove
them. Where no feasible temporary operation is established, mark the option
unresolved and change its layout rather than counting downtime as zero.

**Example — concealed drain.** A roof outlet can be seen from a hatch but its
strainer cannot be withdrawn under a fixed guard. A cleaning crew would also
block the sole terrace approach while setting equipment beside the hatch. Move
the guard or outlet and create a distinct work bay, then trace strainer removal,
debris handling and reinstatement while retaining a separately verified route.
If that bay cannot fit, compare a different outlet position or a planned terrace
closure with an agreed temporary arrangement. The change is an access hypothesis;
roof drainage and guard design still need specialist confirmation.

## Design for intervention over time

**Decision and inputs.** Consider how the exposure, use and assembly make a
particular intervention likely or difficult. Identify water paths, abrasion,
cleaning chemicals, sun, movement, trapped moisture, corrosion contacts and
inspection visibility as relevant to the actual detail. Establish what is
known about the products and operator resources. An observed vulnerable
interface is a reason to investigate, not a predicted failure date.

**Procedure.** Map each consequential layer or piece to its function, exposure,
observable condition, means of cleaning or repair and dependencies. Compare:

- retain and clean or adjust where condition and performance allow;
- repair a localized defect while preserving sound surrounding material;
- replace a sacrificial piece, seal or finish independently;
- replace a larger assembly only when local intervention cannot restore the
  required function or cannot be executed reliably.

For each path, show the **product piece** actually supplied and removed, not
just the damaged area: dimensions, weight/handling information where available,
fixing access, direction of removal and clearance at its destination. Identify
adjacent pieces disturbed, matching and compatibility needs, and access to the
substrate. A small defect can require a large piece or several neighbors to come
out. Confirm an available replacement or repair method; assumed future spare
parts and undocumented reuse are not evidence.

Trace the shared support and closure before choosing a repair boundary. If one
rail, bracket or common seal secures several panels, removing one may disturb
others, expose a control layer or leave neighboring pieces unsupported. Preserve
their support and protective functions through a separately designed temporary
condition; do not prescribe its sizing. A detachable cover or independent
retainer may reduce disruption but adds fixings, thickness, joints and interfaces
to maintain. Reusing sound material requires condition assessment, safe removal,
handling, storage, compatibility and reinstallation; count losses and any
rework. Compare wholesale replacement if those prerequisites cannot be met.

**Example — damaged entrance lining.** Repeated contact damages one lower
lining panel. A local patch retains more material but may leave an unmatched finish
and cannot conceal persistent moisture from a leaking threshold. A separate
replaceable base panel allows local renewal, but its shared rail and adjoining
water-control closure must remain supported and continuous during work. Correct
the water path, provide an independently accessible base fixing and carry the
replacement panel through the entrance work-zone test. If matching stock or a
compatible closure is unverified, report those conditions; do not assume a
repair interval or that a modular panel is automatically more durable.

## Count the architectural work

**Decision and inputs.** Quantify a bounded architectural change so that useful
geometry, unavoidable pieces and operation consequences are visible before unit
rates are known. Use a stated drawing revision and measured inside/outside faces,
units, opening treatment, system build-up, module and cutting rules. Record
uncertain dimensions and unmeasured details separately.

**Procedure.** Set a common functional/output and performance boundary before
measuring options: for example the same enclosed opening, required weather and
access function, and period of use. Count each distinct layer, backing, support,
closure and associated access work needed to deliver that boundary. Keep field
area, perimeter/returns, joint length, piece count and discrete components in
their own units. For a rectangular field, net face area = width × height minus
openings counted on that face; add measured reveals and returns separately.
Avoid subtracting the same opening twice or counting an overlapping support twice.
Record whether quantities refer to installed work, procurement or waste.

For modular work, lay out whole pieces against corners, openings, joint widths
and orientation; count the cut pieces actually needed, including whether an
offcut can physically and acceptably be reused. Calculate procurement in supplier
stock units from that cutting/layout and documented damage/spare allowances;
installed cut-piece count need not equal purchased whole-piece count. Do not
equate net area with purchased area. Count disturbed adjacent pieces, replacement closure,
access setup, waste removal and temporary works for each event. Distinguish
reusable removed material from waste only after the recovery path is established.
Show a range or a separate unknown for unmeasured edges and layout; do not hide
it in a generic waste percentage.

**Example — quantity before price.** A hypothetical 6 m × 3 m field has a
2 m × 1 m opening: net face area is 16 m²; a 0.2 m deep reveal around all four
sides adds 1.2 m², if the design actually lines all four. Two hypothetical module
layouts must cover the same 17.2 m² of finish; neither procurement quantity
follows until layout and cuts are drawn. A repair may remove a whole module
and adjacent closure even when the damaged patch is smaller. If rates and
service evidence are unavailable, the geometry still identifies a possible
reduction in cuts or access disruption, but cannot establish which option costs
less over time.

## Compare equivalent function over time

**Decision and inputs.** Compare the same output, required performance and
physical boundary across the same declared analysis period and operating
conditions. Include differences in enabling support, protective closure,
maintenance access and any additional work necessary to achieve equivalent
function. Define currency and price date, quantities, rates, taxes or exclusions,
operation assumptions and treatment of residual value. Obtain event timing and
cost data from the project/operator and suppliers or mark them unknown. A
product's nominal life is not automatically its assembly's service life.

**Procedure.** Build an event ledger for each option: initial supply and
installation; inspection/cleaning; repair and replacement; access, protection,
handling, disposal or recovery; temporary operation or loss of use; and end-of-
period treatment where within the agreed boundary. Each event combines its own
quantity × unit rate plus event-specific fixed costs. Count repeated events
individually at their assumed dates, including replacement waste and affected
neighboring work. Avoid adding the same access setup twice if tasks truly share
one visit, or assuming sharing where schedules or access differ. If temporary
loss has no agreed monetary value, show its duration and affected function
alongside costs rather than assigning zero.

For a simple undiscounted scenario, total cost is initial cost plus the sum of
all event costs less any supported residual credit. For a discounted comparison,
use a project-agreed real or nominal rate consistent with the price basis and
sum each dated net cost divided by `(1 + r)^t`; state the time origin, rate,
period and residual treatment. Use finite inputs with `r > -1`, and nonnegative
`t` in the same period units as the rate. Do not add costs in mixed price bases or imply
that an environmental inventory follows from money. A separate impact comparison
needs compatible source data, units and system boundaries for each relevant stage.

**Break-even and uncertainty.** In a hypothetical project scenario, suppose A
has an initial cost `I_A` greater than B by `D`, but each of `n` matched service
events saves `S` relative to B, including access and temporary-use costs. With
no discounting or other differences, A breaks even at `n × S = D`; A is lower
only above that threshold. For illustration only, if `D = 12` cost units and
`S = 3` per event, the tie is four events; three events favor B and five favor A.
These symbols and event counts are hypothetical, not prices, intervals or material
life. When event timing, event scope or costs differ, use the dated ledger instead
of this shortcut. Test plausible project-supported ranges and correlated cases:
access setup and closure duration may change together, and a failed component
may trigger adjacent work. Identify the input at which the preference changes.

**Checks and limits.** Show feasibility and unverified prerequisites before
ranking. If event frequency, scope, price or downtime is missing and could reverse
the result, retain the alternatives and state what evidence would resolve the
choice. Quantity and spatial improvements can still be identified without a cost
ranking. Do not infer service life, costs, carbon or a universal material winner
from a source example. Confirm system performance, actual condition, handling,
operational requirements and specialist design before implementation.
