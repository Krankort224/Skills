# Vehicle routes and parking geometry

Use this method to decide whether a selected parking/servicing arrangement can
actually be reached and used. Demand belongs to [program](../../program/demand.md);
physical land belongs to the [quarter ledger](quarter-and-public-space.md#reconcile-ground-use-without-double-counting).
Neither a counted stall nor an automobile centreline establishes a usable place.

## Contents

- [Define the vehicle and the claim](#define-the-vehicle-and-the-claim)
- [Construct the parking module](#construct-the-parking-module)
- [Construct and verify a movement](#construct-and-verify-a-movement)
- [Carry the route through servicing and section](#carry-the-route-through-servicing-and-section)
- [Worked parking failure and correction](#worked-parking-failure-and-correction)
- [Changed vehicle and entry](#changed-vehicle-and-entry)
- [Source boundary and related decisions](#source-boundary-and-related-decisions)

## Define the vehicle and the claim

Retain the demand source, date, units, operating period and reserved users. Keep
resident, visitor, accessible/transfer, delivery, waste and emergency demands
distinct. Only combine their physical places when their actual times, controls
and alternative provision permit it; an available dwelling space is not
automatically visitor capacity. Determine required provision and dimensions
through [requirements](../../requirements.md), not a foreign parking diagram.

For every consequential vehicle retain a dated manufacturer/operator drawing or
an explicitly selected design template: overall length/width/height including
mirrors and equipment; effective wheelbase L; front/rear overhang f/r; steering
or turning-envelope definition; approach/departure/breakover geometry where
relevant; operational clearances and uncertainties. Body radius, wheel radius
and kerb-to-kerb/wall-to-wall turning circles are different quantities. Ask what
the supplied radius measures before drawing a curve. Keep wheel tracks,
body/mirror sweep and working/person zones as separate envelopes.

The construction below is bounded to a rigid, planar, low-speed vehicle with
parallel effective axles, no slip and an effective bicycle steering angle.
It does not model articulated trailers, rear-steered/multi-axle behaviour,
dynamic cornering, tyre scrub, visibility, queue throughput, load-bearing ground
or safe operation. Use a checked vehicle-specific template or suitable verified
tracking tool for those cases; inspect its vehicle, steering/speed/reversing
settings, clearance and output extent. A passenger-car pass says nothing about
a refuse vehicle, fire appliance or accessible unloading operation.

## Construct the parking module

1. Draw the actual clear site/basement polygon, walls, columns, kerbs, trees,
   protected footpaths, doors, equipment and unavailable land. Identify whether
   dimensions run to markings, finished faces or a structural grid. Reserve
   actual door opening/transfer, wheel stops, pedestrian arrival and maintenance
   zones; do not count them inside a generic vehicle rectangle without evidence.
2. Choose orientation and operating direction with the entry, pedestrian edge,
   support grid and exit. At angle θ to the aisle, let b be the rectangular bay
   width normal to its long axis and l its length. For 0 < θ ≤ 90°, a parallel
   row has normal depth D = l sin θ + b cos θ and repeat pitch p = b/sin θ.
   Its end projection q = l cos θ + b sin θ gives row length
   B_row = (n−1)p + q. Thus n = 0 if usable length B < q; otherwise
   n = 1 + floor((B−q)/p). These are rectangle-projection identities, not
   permission to use a particular bay or aisle size. Draw the actual vertices
   and end wedges; a bounding rectangle is reserved ground, not extra stalls.
3. At 90°, D=l and B_row=nb. A facing double row with clear aisle a reserves
   depth 2l+a, before edge paths, wall/column offsets, ramps and end manoeuvres.
   For angled rows use 2D+a only when both physical rows and end conditions fit.
   Parallel parking requires its actual insertion/exit movement and end space;
   it is not the θ→0 limit of the angled-row formula.
4. Select trial a, end buffers and entry width, then test movements below.
   Wider stalls can reduce manoeuvre demand; a nominal aisle width alone cannot
   decide this trade. Test the end and obstructed bays as well as a middle bay,
   with adjacent spaces occupied. Count inaccessible/obstructed stalls as failed,
   and separate geometrically usable places from provision still awaiting rules.
5. Record the union of parking, aisle, aprons, ramp, protected walking and loading
   pieces in the ground ledger. Assign each physical piece once. A manoeuvre
   overlay is not an extra area; simultaneous incompatible use of that piece is
   a conflict. Recheck demand after a column or transfer zone removes a place.

## Construct and verify a movement

Use metres and a common plan datum. At rear-axle midpoint (x,y), heading ψ,
place the body rectangle with local coordinates u ∈ [−r,L+f],
v ∈ [−w/2,w/2]. Transform every corner by
X=x+u cos ψ−v sin ψ, Y=y+u sin ψ+v cos ψ. Add separately supplied mirrors,
equipment and clearance c; c is a study/project input, never a statutory default.

For an effective maximum steering angle δ, rear-axle radius
R_min=L/tan δ. Use R≥R_min and a tangent-connected path. A left quarter-turn
starting at (x0,y0), heading east, has
x=x0+R sin t, y=y0+R(1−cos t), ψ=t, 0≤t≤π/2.
Reverse and right turns need their correct direction/heading; do not rotate an
independent rectangle at a corner or teleport its axle to a second centreline.

For a constant left circle with R>w/2, the body's enclosing outer radius is
R_out=sqrt(max(r,L+f)²+(R+w/2)²); its inner radius is R−w/2 when the
rectangle spans the rear axle. These radial limits screen an annular passage,
not the full entry/exit or steering transition of a finite turn. Front overhang
can hit an outer column while the rear-wheel track clears the inner kerb.

1. Trace entrance → aisle → manoeuvre → parked/working position → departure
   through the actual exit. Include any reverse or multi-point sequence, its
   holding area, supervision and concurrent users; geometric reversibility
   alone is not operational permission. Reversing along the same rigid path
   recovers the same body sweep, but still needs a separate conflict check.
2. Test the union of transformed body polygons against every obstacle and the
   available polygon. A straight constant-heading segment is checked exactly
   by extruding its body along the segment. An endpoint-only check misses a
   collision between endpoints. Offset obstacles or the body by the chosen c.
3. For a bounded sampled curve, retain each interval's maximum axle travel Δs
   and heading change Δψ in radians. Let ρ be the farthest body point from the
   axle. Relative to the preceding sampled pose, every intermediate body point
   moves at most ε = Δs + ρ|Δψ|: translation is bounded by travelled distance,
   rotation by radius times angle. Require sampled separation **greater than
   c+ε**, including from unavailable boundaries. An actual sampled intersection
   fails; no intersection without this margin is unresolved, not a pass.
   Refine the intervals or use an exact sweep. This bound assumes the stated
   path and monotone/bounded turn within each interval; endpoints alone cannot
   bound an unrecorded excursion. Geometric/input uncertainty is additional.
4. Show the critical pose, minimum margin and input/path used. A collision
   rejects that path; it does not prove no possible path exists. Compare wider
   bays/aisles, a different entry, reduced count, changed support, another
   actually available vehicle or servicing location. Recheck the entire route
   and all affected reservations after the change.

## Carry the route through servicing and section

At delivery/waste standing positions draw the stopped body plus tail-lift,
door/container operation, handler, receiving/temporary holding and onward object
route. Trace the load to its destination using [object/handler fit](../../space/planning/room-floor-and-section.md#construct-a-room-that-can-be-used).
Standing in the only through lane or on a school entrance is a concurrent-state
failure even if a vehicle can drive there. A small collection vehicle is an
alternative only with the operator's actual collection/frequency arrangements.

Trace an independent protected walking/transfer route from parking and external
approach to actual entrances. Locate crossings and sight obstructions, doors,
queues and vehicle overhang at kerbs; a painted footpath inside the sweep is
not separation. Test arrivals during delivery and closed gates. Fire access
needs its selected appliance/strategy, required clearances and ground/load/
deployment evidence; ordinary geometric access neither approves nor replaces it.

For basement/ramp choices, carry clear swept width around columns/walls and
the complete vehicle height through portals, services, overhead doors and turns.
Draw the actual longitudinal vehicle underside/wheel contact profile through
each slope transition, and test grounding, overhang and head clearance; an
average ramp gradient is insufficient. Reserve transition lengths, holding
before the gate, pedestrian/evacuation routes, drainage, foundation and service
interfaces. Ventilation, fire strategy, ramp traction, structure and equipment
need their actual engineering evidence. If those inputs are absent, reserve
alternatives and keep the dependent result open; this method supplies no default
ramp slope, headroom, drainage or fire width.

## Worked parking failure and correction

All values below are original hypothetical study inputs. The brief permits an
unroofed alternative, asks for 20 ordinary car places, and separately resolves
accessible provision. Select body w=1.8, L=2.6, f=0.9, r=1.1 (length 4.6 m),
effective δ_max=35° and clearance c=0.20 m. Choose l=5.2, a=6.0 and through
connections at both aisle ends; reserve a full-depth 6 m apron at each end.
The example's rectangle includes all assumed vehicle projections; no extra
mirror/equipment protrusion is supplied. These dimensions are not published
parking standards.

With b=2.5 and 26.4 m row length, arithmetic gives ten places per row: 20.
Depth is 16.4 m; with both end aprons the reserved rectangle is
(26.4+12)×16.4 = 629.76 m². Bottom bays occupy y=0…5.2, aisle y=5.2…11.2,
upper bays y=11.2…16.4. The assumed adjacent upper cars occupy y=11.5…16.1.

For an interior upper target with centre x_j, approach east at rear axle
(x_j−4,7.8), turn left at R=4, then move north 0.8 m to rear axle
(x_j,12.6). The final body reaches y=11.5…16.1. Steering is
atan(2.6/4)=33.02°≤35°, so this is an admissible idealized path. But during
the turn its front-right corner protrudes east of x_j by
sqrt(3.5²+4.9²)−4 = 2.0216 m, at y=11.8. A car in the next 2.5 m bay starts
only 2.5−0.9=1.6 m east of x_j: actual overlap, despite all 20 counted boxes.
A proposed canopy column x=9…9.4, y=7.6…8.0 also blocks the straight aisle
approach to a farther bay. Removing one counted bay would not remove that column.

A geometric correction uses b=3.3 and an unroofed option, removing the proposed
canopy column and its construction intent. Ten bays now need 33 m row length;
with aprons the module is 45×16.4=738 m², an increase of 108.24 m². The same
car/path has 3.3−0.9−2.0216=0.3784 m minimum horizontal clearance to the
adjacent parked car, exceeding c. Translation across bays and reflection to the
opposite row preserve the construction; the free end aprons contain the end
approaches, with separate through entry/exit rather than an untested U-turn.
The final parked body has 0.30 m longitudinal margins. Reverse departure
retraces the tested sweep, then follows the aisle to the onward exit.

This is a vehicle-geometry success for the declared paths and occupied cars,
not approval of door use, public reversing, queue operation or accessible/fire
provision. If row length remains 26.4 m, the wider layout has only 16 candidate
places; the unmet four places must be reported, not hidden by the same total.
If the canopy/column is fixed, the unroofed correction is unavailable: change
the actual path/layout or retain the failure. Moving a structural column without
its support decision is not a geometric remedy.

For the land consequence, take a 10,000 m² boundary with a declared 2,200 m²
unallocated planted piece. Reserving the corrected 738 m² module, a separate
45×1.8=81 m² protected edge path and a separate 60 m² service connector leaves
1,321 m² of that planted piece. The connector is counted once, not again as
service land plus circulation. Any overlap between its swept/working use and
the protected path still needs correction; arithmetic cannot resolve it.

## Changed vehicle and entry

An operator substitutes w=2.0, L=3.5, f=1.0, r=1.2 at the same steering limit.
Length becomes 5.7>5.2 m and R_min=3.5/tan35°≈4.999>4 m. Both the parked
fit and old turn fail. At a new R=5 m, the front outer radius is
sqrt(4.5²+6²)=7.5 m; recheck neighbours, aprons and the whole approach with
new depth rather than preserving 20 nominal places. A supported smaller vehicle,
another collection point or land/program change is a real decision.

For the original car a straight gate spanning y=6.5…9.1 admits the centred
approach at y=7.8 with c=0.20. Moving that approach to y=8.8 gives body top
9.7>9.1 even before c. Re-centre the route where possible or change the gate/
entry and retest the connection to the turn; a translated end arrow is not a
new continuous path. Both changes reopen ground, supports and operator inputs.

## Source boundary and related decisions

Selected primary reading is [Manual for Streets 2007](../../../sources/applied-site-methods.md#manual-for-streets-2007).
The module projections, axle/corner construction, sampling bound and hypothetical
failures are original derivations. No source dimension table, diagram or tracking
software is installed. The four supported calculators are unchanged; these
constructions are not a new general vehicle simulator.

- Requires — [Demand](../../program/demand.md): when provision/users/time basis is unresolved, establish it before counting places.
- Requires — [Actual journeys](quarter-and-public-space.md#keep-public-private-and-service-journeys-continuous): when a path crosses controlled plots, resolve its operating chain and rights.
- Affects — [Ground balance](quarter-and-public-space.md#reconcile-ground-use-without-double-counting): count changed bays, aprons, ramps, service and walking pieces once.
- Affects — [Territorial service allocation](service-capacity-allocation.md#fit-the-facility-parcel-and-recount-the-quarter): when manoeuvres/loading compete with a school or childcare parcel, refit capacity and access rather than spending its play area twice.
- Verified by — [Object/occupied-state fit](../../space/planning/occupied-state-fit.md): when delivery continues indoors or shares operation/holding space, test those actual objects and states separately.
- Requires — [Requirements](../../requirements.md): for actual provision, accessible/fire/technical or jurisdiction-dependent conclusions, establish their own authority and evidence.
