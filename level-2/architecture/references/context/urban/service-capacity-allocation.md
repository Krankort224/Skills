# Territorial service capacity and residential groups

Use this method to decide which residential groups can actually use a selected
school, preschool or other finite public service, and what its land/route choice
changes. [Demand](../../program/demand.md) owns activity/population inputs;
[quarter ground balance](quarter-and-public-space.md#reconcile-ground-use-without-double-counting)
owns physical land. Enough seats in aggregate is a necessary arithmetic check,
not evidence that each group is served.

## Contents

- [Define demand and capacity on the same basis](#define-demand-and-capacity-on-the-same-basis)
- [Build actual route eligibility](#build-actual-route-eligibility)
- [Allocate without double credit](#allocate-without-double-credit)
- [Fit the facility parcel and recount the quarter](#fit-the-facility-parcel-and-recount-the-quarter)
- [Derive a floor and site reservation for education](#derive-a-floor-and-site-reservation-for-education)
- [Worked seat surplus with an unserved group](#worked-seat-surplus-with-an-unserved-group)
- [Changed access, parcel or population](#changed-access-parcel-or-population)
- [Source boundary and related decisions](#source-boundary-and-related-decisions)

## Define demand and capacity on the same basis

Choose the study date/phase, residential groups and actual entrances, population
source and uncertainty, service types/age cohorts, operating periods, admissions
or entitlement basis and project jurisdiction. Keep pupils, preschool places,
retail floor area and visits per day as different units. A service circle does
not grant an admissions right. A building labelled school supplies no verified
capacity, opening date or available place.

For each group i and service k record demand d_ik. Prefer known cohort/operating
data. If an authorized planning rate q_ik is used, show its source, denominator,
date and rounding: for example ceil(P_i q_ik) persons, not a fractional place.
Sum groups on the selected basis; rounding a combined population can differ
from rounding separate indivisible groups. Do not infer a legal rate from a
coursework parameter or assume the same age structure in every group.

For each facility j and service k retain the actual or provisional capacity
C_jk, established metric and evidence, existing/outside commitments E_jk,
other exclusive reservations R_jk, opening/availability and operator. Available
capacity A_jk=C_jk−E_jk−R_jk must be nonnegative. Check reservation identities:
an existing pupil already included in E must not be subtracted again in R.
Unknown outside commitments make availability unknown, not equal to gross C.
One 40-place facility used by two quarters remains 40 places in its shared ledger.

Distinguish operator-confirmed capacity, an architectural candidate fitted to a
supplied program, and a future commitment. Do not use a future facility for an
earlier occupied phase. Different age cohorts, rooms, shifts and staffing are
not fungible unless the actual program and authority permit the conversion.

## Build actual route eligibility

Use [continuous journeys](quarter-and-public-space.md#keep-public-private-and-service-journeys-continuous)
for each group entrance → paths/crossings/control points → actual facility gate
→ destination. Retain links, lengths or travel times, levels, mode, opening
hours, barriers, crossing rights and the user's ability to traverse them. Build
a small explicit network for the question: shared nodes connect only where a
real crossing/entrance exists. A bridge without a usable approach, fenced school
edge or locked garden is not a network edge. Split a large residential group
when its entrances or access conditions differ.

Compute route distance as the sum along the verified eligible chain, or time as
the sum of travel plus declared waits; do not compare a time cutoff to metres.
For each i,j,k mark eligibility e_ijk=1 only when the service type/age/phase,
actual access and selected distance/time/admissions conditions hold. Record why
an edge is excluded. Unchecked conditions yield **unknown**, not eligible or
proven impossible. A strict result can use only confirmed edges; a separate
conditional scenario may expose which unknown edge would change it.

Use actual selected authority for any catchment, accessibility, road-crossing
or admissions requirement. Geometric proximity, operator eligibility and legal
compliance are separate axes. Test a gate closure, seasonal interruption or
changed crossing by removing the real edge and recalculating the chain; moving
a circle on a plan is not a revised route. Keep child/visitor access distinct
from delivery, parking and emergency movement.

## Allocate without double credit

Let x_ijk be places reserved for group i at facility j for service k. On the
same period/phase and unit basis require:

- x_ijk≥0, and x_ijk=0 on excluded edges;
- sum_j x_ijk=d_ik for a fully served group; otherwise record residual
  u_ik=d_ik−sum_j x_ijk≥0;
- sum_i x_ijk≤A_jk for each facility/service.

Record a group-by-facility allocation table and both row/column totals, not just
the chosen nearest facility. Individual children/seats are integer units. A
group may be split only where its operating/admissions assumptions permit it;
otherwise allocate it whole and disclose the extra constraint. Different
services get separate allocations. Shared rooms/staff/time also need the
[resource timeline](../../program/shared-use.md), not independent reuse of one
capacity in simultaneous tables.

For a small case assign groups with only one eligible facility first, then
test flexible groups. A failed greedy choice is not proof of infeasibility:
try moving a flexible reservation along an alternative eligible edge, freeing
its former place for a constrained group. Continue such augmenting reassignments
or enumerate the bounded choices. For divisible demand this is a capacity-flow
problem (source→groups with d, eligible group→facility edges, facilities→sink
with A); a full flow certifies the stated arithmetic allocation only. Whole-group
requirements need integer group assignments and cannot be certified by a split
flow. A larger actual network may use a suitable solver with those constraints;
no solver or GIS installation is necessary for the local procedure.

Diagnose a capacity cut: for any set G of groups, compare its total demand with
the total available capacity of its union of eligible facilities N(G). If
sum_G d > sum_N(G) A, the deficit cannot be cured by reordering allocations.
Total quarter capacity can still exceed total demand. This subset condition
characterizes feasibility for the divisible network with established edges;
whole-group and shared-resource constraints can cause further failures.

Correct the responsible variable: secure a real new eligible connection,
redistribute existing flexible reservations, add genuinely available capacity,
choose another facility parcel, change phase or reduce the authorized demand.
Do not double-book outside seats, invent an entrance, relax a cutoff or count
the same shared facility again. Recompute the table after every change.

## Fit the facility parcel and recount the quarter

For every credited new/expanded facility, fit a supplied service-specific program:
building footprint and floor assumption, required usable outdoor/activity
rectangles, setbacks/buffers, accessible entrance, standing/collection, waste,
service/fire interfaces and retained land. Record which input owns each size
or capacity claim. Gross parcel area minus footprint is not automatically usable
play area; slopes, easements, fragments, safety separation and incompatible
simultaneous use can remove it. Check shapes and clear dimensions, not just sums.
If the brief supplies places or population only, [derive the floor and site
reservation](#derive-a-floor-and-site-reservation-for-education) before crediting
a footprint.

Reuse [vehicle geometry](vehicle-and-parking-geometry.md) for actual parking,
delivery/turning and operating zones. A school's loading bay cannot also supply
its peak-arrival play/entrance area without a verified operation change. Off-site
outdoor provision needs its own capacity/right, real route and operating plan.
One physical outdoor piece is counted once even if permitted successive
activities use it; separate functional credits from physical ground accounting.

Put each footprint, outdoor piece, route and support reservation in the canonical
quarter ledger with a stable ID. Carry capacities and affected housing floor/
population assumptions alongside it, without adding floor m² to land m². A new
facility may displace housing or a court; a path can consume planted ground;
retaining the old population can then require another site. Conversely a lower
population changes service and parking demand and the actual housing program,
not just an indicator printed in a table. Test each occupied phase independently.

## Derive a floor and site reservation for education

Translate the offered places into groups present at the same time and the rooms
and staff that serve them. In addition to classrooms or group rooms, identify
shared activity and specialist spaces and the staff, storage, dining, rest,
sanitary or service provision the actual brief calls for. Use the
[activity program](../../program/demand.md) and [learning clusters](../../typologies/learning.md)
for those relationships, and [shared-use timelines](../../program/shared-use.md)
to check whether the same rooms, equipment and staff can serve the proposed
schedule.

Use the [area ledger](../../program/area-ledger.md) to assign spaces, support,
circulation, cores and walls to actual levels on a stated boundary. Establish
the footprint from the arrangement of those levels. Check usable room depth
and frontage, core fit and links to arrival, service and outdoor use. Reserve
the outdoor activity and its support separately in the ground ledger and test
them through [outdoor play and sport](quarter-and-public-space.md#fit-outdoor-play-and-sport).

**Illustrative allocation.** A hypothetical center offers 120 places in four
groups of 30. Four 60 m² group rooms, 80 m² of shared activity and staff/service
support, and 100 m² of shared circulation, cores and walls total 420 m² on the
study's enclosed floor-area basis. Assign two rooms, 40 m² of support and
50 m² of circulation, cores and walls to each level. Two stacked 21 × 10 m
plates give 210 m² per level and a single 210 m² footprint. A separate 30 × 20 m
yard reserves 600 m² of ground. These inputs illustrate a provisional
allocation. Confirm the support inventory, rooms and entrances, and fit the
actual teaching and outdoor schedules before relying on this capacity.

## Worked seat surplus with an unserved group

All numbers and a 500 m walking cutoff are declared hypothetical project inputs,
not demographic or statutory defaults. Three groups require school places
A=70, B=60, C=50 and preschool places A=25, B=20, C=15. Splitting group B's
individual seats is permitted in this study; each child still gets one place.

School S1 has gross 100, 20 verified outside commitments, hence 80 available;
S2 has 120, 20 outside, hence 100 available. Preschool T1 and T2 each have
40 gross and 10 outside, hence 30 available. School supply/demand is 180/180;
preschool is 60/60. No outside reservation is credited twice.

| Group | School S1 route, m | School S2 route, m | School demand |
| --- | ---: | ---: | ---: |
| A | 350 | 720 | 70 |
| B | 650 | 420 | 60 |
| C | 760 | 300 | 50 |

These are measured hypothetical network chains, not radial distances. B→S1's
650 m detour is caused by a closed garden; its 230 m detour segment cannot be
silently replaced by a drawn shortcut. A can use only S1; B and C only S2.
The subset {B,C} needs 110 places but its only eligible facility supplies 100:
10 unserved while S1 has 10 unused places. Giving B S1's remaining ten places
would violate eligibility; reporting 180 available seats conceals the failure.

The preschool routes are independently confirmed: A→T1 only, C→T2 only, B→both.
Allocation T1: A25+B5=30; T2: B15+C15=30 works. Spare preschool provision cannot
repair the school deficit. If B must attend one preschool as an indivisible
20-person group, that particular split is forbidden and each facility lacks
room after its constrained group: report infeasibility on that changed basis.

One correction obtains a public bypass outside the closed garden, with actual
rights, entry and crossings. Its 60 m segment replaces the 230 m detour:
B→S1 becomes 650−230+60=480 m, now eligible. Reserve the disjoint 60×2=120 m²
path as a trial clear reservation, not a code width. Revised schools:

| Group | S1 allocation | S2 allocation | Residual |
| --- | ---: | ---: | ---: |
| A | 70 | 0 | 0 |
| B | 10 | 50 | 0 |
| C | 0 | 50 | 0 |
| Facility total / available | 80 / 80 | 100 / 100 | 0 |

Suppose each school's supplied candidate program fits an 80×60=4,800 m² parcel:
building x=0…60,y=0…20 (1,200); outdoor field x=0…65,y=20…60 (2,600);
access/service x=60…80,y=0…20 plus x=65…80,y=20…40 (700);
landscape x=65…80,y=40…60 (300). These four nonoverlapping categories tile
the parcel. Actual separations, activity fit and the offered capacity remain
project evidence, not conclusions from m²/person. The example supplies this
program as a checked architectural candidate, not an operating approval.

For each preschool a separate supplied candidate program tiles a 40×30=1,200 m²
parcel: building 30×10=300, outdoor 30×20=600, access 10×20=200, landscape
10×10=100; arrange the latter two in the remaining 10×30 side band. This is
a different program/unit, not school seats scaled into preschool provision.

In a 20,000 m² quarter, two school parcels consume 9,600 and two preschool
parcels 2,400. Housing footprints 4,800, other paths/service 1,600, public
space 600 and planted reserve 1,000 close the same boundary. The bypass changes
paths/service to 1,720 and planting to 880; the total stays 20,000. Do not add
the bypass again inside school parcels or remove housing population merely
because the path consumes planting. School-parcel internal ground is already
inside the 9,600, not a second quarter-level footprint/play total.

## Changed access, parcel or population

If the bypass closes at school arrival, remove that edge: B→S1 returns to
650 m and the ten-place failure returns. Proposed future opening cannot serve
today's phase. Another actual facility/connection, an authorized capacity change
or lower demand is required.

If S2 is offered a 30×160 m parcel instead, equal 4,800 m² area does not fit the
supplied 65×40 m outdoor rectangle in either axis-aligned orientation. Its
capacity is no longer a fitted architectural candidate; leave it uncredited
until a permitted program/parcel correction is demonstrated. A rotated/freeform
solution needs its own containment proof, not equal area. Moving delivery ground
into the field cannot recover its required clear shape.

Alternatively, without the bypass, assume B's authorized planning model is
d_school=ceil(0.10 P_B), with P_B=600. A and C remain fixed. The S2 bottleneck
allows B at most 50 school places, so P_B≤500 under that model: a reduction of
100 residents. Reconcile the actual dwelling mix/floor program before adopting
it. If B's preschool model is ceil(P_B/30), its demand changes from 20 to 17;
recalculate preschool reservations and parking on their own bases. The reduced
population does not automatically release a school parcel or legal entitlement.

## Source boundary and related decisions

[BB103](../../../sources/applied-site-methods.md#building-bulletin-103) supports
the distinction between usable school outdoor ground, footprint and access;
[Esri's primary documentation](../../../sources/applied-site-methods.md#network-capacity-allocation)
distinguishes network eligibility and finite capacity. This local conservation,
cut/reassignment procedure, parcel construction and examples are original
synthesis. The split-seat flow here is explicitly different from Esri's documented
whole-demand-point capacitated option. No GIS execution, dataset or admissions
policy is inferred. No source formula, school-area standard or catchment number
is imported; normative selection remains separate. The educational floor and
site example uses original study inputs. Its local provenance is recorded under
[recovered local methods](../../../sources/index.md#recovered-local-methods).

- Requires — [Demand](../../program/demand.md): when demographic/type/period inputs are unresolved, retain scenarios rather than inventing a service rate.
- Verified by — [Actual quarter journeys](quarter-and-public-space.md#keep-public-private-and-service-journeys-continuous): check every relied-on entrance, closure, crossing, level and right, separately from reserved places.
- Verified by — [Outdoor play and sport](quarter-and-public-space.md#fit-outdoor-play-and-sport): when a facility relies on play or sport provision, fit each operating zone and actual access under the stated timetable.
- Verified by — [Vehicle/parking geometry](vehicle-and-parking-geometry.md): when a facility parcel includes delivery, collection or parking, test actual motion and standing/handler space.
- Affects — [Quarter ground](quarter-and-public-space.md#reconcile-ground-use-without-double-counting): changes to facilities or routes displace named physical reservations once and may reopen the housing/population balance.
- Requires — [Shared-use timeline](../../program/shared-use.md): when capacity depends on shared rooms, staff or outdoor operation, test concurrency and changeover before claiming availability.
- Requires — [Requirements](../../requirements.md): when claiming legal provision, catchment, accessibility or admissions applicability, check the actual authority/version and project conditions.
