# Fit an occupied room across changing states

Use this method when an area total or an empty-room sketch passes but simultaneous
use, a changed arrangement or moving objects may fail. The general
[room-construction method](room-floor-and-section.md#construct-a-room-that-can-be-used)
owns activity/furniture selection; this method makes its state-dependent geometric
test explicit. Reuse the actual project boundary, objects and operating evidence.

## Contents

- [Define the geometry and the state](#define-the-geometry-and-the-state)
- [Test containment, overlap and a complete move](#test-containment-overlap-and-a-complete-move)
- [Correct an L-shaped studio without borrowing area](#correct-an-l-shaped-studio-without-borrowing-area)
- [Retest time, fixed constraints and a changed load](#retest-time-fixed-constraints-and-a-changed-load)
- [Evidence, related decisions and limits](#evidence-related-decisions-and-limits)

## Define the geometry and the state

Record a common origin, axes, units, level and measurement boundary. Distinguish
the inside-face shell from usable floor after columns, walls and fixed equipment.
Represent a rectilinear shell as a union of nonoverlapping rectangles or a large
rectangle minus explicit notches. A bounding rectangle or equal-area substitute
cannot establish containment in an L-shaped room. Inclined/curved boundaries and
changed object orientation need their actual geometry; use suitable model or
drawing tools when useful, without treating this elementary test as their limit.
Use finite ordered coordinate bounds, positive envelope dimensions and finite
nonnegative allowances; reject invalid inputs rather than clipping a failed fit.

For each relevant state record:

| Input | What must remain distinct |
| --- | --- |
| Fixed objects | Solid footprints and projections that remain when an activity stops; assumed concealment or an inactive machine does not remove them |
| Activity | Actual furniture, people and action envelope, including the needed uninterrupted field; do not infer seating capacity from its area |
| Operation | Cabinet/door/leaf, operator and assistance envelope while used, separately from the parked solid |
| Movement | Protected route and complete object-plus-handler transit; arrival, use, reset and maintenance can require different occupied states |
| Uncertainty | Supplied survey, component and handling allowances with direction and basis; an unknown allowance stays unresolved |
| Resources | Required room, people, equipment, storage and unavailable/reset periods, linked to the actual booking and authority to change it |

Envelopes can share a physical place only when their uses genuinely cannot
coincide and the transition is feasible. A swept envelope is not a new physical
piece of floor: [count the floor once](../../program/area-ledger.md), then overlay
its state-specific demands. Do not add already included chair or handling space
a second time. Retain height, support, sightline, opening and environmental checks
separately; passing a floor test does not settle them.

## Test containment, overlap and a complete move

1. Place the actual active setting, not its area label. Verify the entire shape
   lies inside the shell and outside every relevant notch/obstruction. For an
   orthogonal setting, intersect it with each excluded rectangle rather than
   checking its centre or four bounding-shell corners alone.
2. For rectangles A and B, positive overlap requires both
   `min(A.x_max,B.x_max) > max(A.x_min,B.x_min)` and the analogous y inequality.
   Its area is the product of those two positive interval lengths. Check each
   simultaneous activity/operation against the protected route and its neighbors.
   Mere touching has zero overlap area but zero separation; it is acceptable only
   on the stated geometric basis, with required movement/clearance already included.
3. Where a supplied independent positional allowance is e on each side, expand
   the tested envelope from `[x0,x1] × [y0,y1]` to
   `[x0−e,x1+e] × [y0−e,y1+e]` before testing. Use directional allowances when
   appropriate; do not invent e or apply it twice to an already reserved envelope.
   Correlated measured positions may warrant a less conservative explicit model.
4. For a fixed-orientation rectangular handling envelope w × d translating
   along one straight segment from centre `(xa,ya)` to `(xb,yb)`, an axis-parallel
   segment sweeps exactly
   `[min(xa,xb)−w/2,max(xa,xb)+w/2] × [min(ya,yb)−d/2,max(ya,yb)+d/2]`.
   Check each segment and its junction, all intervening obstacles, and both ends.
   A diagonal segment's bounding rectangle is only a conservative enclosure.
   Rotating the load, changing the handler's position, slopes and thresholds need
   their actual continuous sweep/handling method; clear endpoints do not prove it.
5. If a neighbor must move first, locate it and its handler in a real holding
   place and test that complete move too. If a path enters an occupied activity,
   reserve an authorized vacant period or provide another physical path. State
   the correction and retest the same demand, not a conveniently smaller one.

## Correct an L-shaped studio without borrowing area

This is an original hypothetical open-studio study in metres, not a clearance,
capacity or product prescription. The inside-face floor boundary is
`[0,8] × [0,6]` minus notch `[5,8] × [4,6]`: **42 m² before deducting the
interior column**. No internal partition is assumed in this supplied model.
Unlisted real walls, door swings or equipment would require another test.

| Item | Initial arrangement | Correction being tested |
| --- | --- | --- |
| Fixed column | `[2.9,3.3] × [2.3,2.7]`, area0.16 | Unchanged; its support is not removed to make the activity fit |
| Protected through-route P | `[0,8] × [0,1.2]`, area9.60 | Unchanged; waiting or reset cannot appropriate it |
| Required uninterrupted activity field A | `[1.2,5.2] × [1.4,4.4]`, 4×3=12 | `[0.8,4.8] × [2.9,5.9]`, same dimensions and declared activity |
| Complete cabinet-use envelope W | `[6,7.8] × [0.6,2.6]`, area3.60 | `[6,7.8] × [1.5,3.5]`; relocation is permitted only if its actual body, connections and use can follow |
| Connector B from P into A | `[0.8,1.8] × [1.2,2.9]`, width1.00 | `[0.8,2.1] × [1.2,2.9]`, width1.30, area2.21 |

Here A is an unfurnished practice field; the supplied transfer state has no other
parked object inside it. A furnished activity needs its actual objects plotted
in every state: a session ending does not make tables or stored loads disappear.

The initial A overlaps the notch by `0.2×0.4=0.08 m²` and the column by
`0.4×0.4=0.16 m²`. Neither defect is repaired by calling A a12m² room.
Initial W occupies `1.8×0.6=1.08 m²` of P during cabinet use. The revised A
avoids both excluded regions; revised W leaves P clear. Test the actual occupied
furniture behind A and the cabinet's full supplied working envelope, rather than
interpreting a reserved rectangle as a complete furnishing design.

Suppose the operator supplies a **fixed-orientation 1.10×1.00 m object-plus-handler
envelope**, permits the required translations and reserves0.05m on each side.
The tested envelope is1.20×1.10m. It cannot pass the initial1.00m connector.
For the corrected layout, move its centre from `(7.2,0.6)` to `(1.45,0.6)`,
then to `(1.45,3.45)`. The reserved horizontal sweep is
`[0.85,7.80] × [0.05,1.15]`, inside P. The vertical sweep is
`[0.85,2.05] × [0.05,4.00]`, contained in P, B and the vacant A, clear of the
column and corrected W. The supplied handling procedure—not the two arrows—must
justify retaining orientation. These are floor-envelope results; turning,
threshold, vertical/load or human capability not supplied here remains unresolved.

The revised same-boundary ledger closes:
`9.60 P + 2.21 B + 12.00 A + 3.60 W + 0.16 column + 14.43 residual = 42.00 m²`.
These are disjoint allocated pieces in this state; W includes its physical body
and use, so its cupboard is not deducted again. The residual is not additional
certified capacity, net legal area or a promise that another activity fits.

## Retest time, fixed constraints and a changed load

**Ordinary transition.** A ends at10:00, B starts at10:15, and the operator supplies
a15-minute reset with the required person/equipment available throughout.
The path above enters A, so that interval must actually be vacant; an incoming
group needs its own waiting/support place outside P. The geometry makes this
selected transition a candidate, not proof of its duration or staffing.

**Fixed conflict.** If the cabinet cannot move and P must remain available during
cabinet use, their1.08m² overlap remains incompatible. Change the permitted
arrangement/operation or report that conflict; leftover area does not resolve it.
Separately, if the sole reset worker is unavailable until10:20, the earliest
supplied15-minute reset ends10:35. The10:15 booking cannot be retained merely
because the physical path fits. Use the [resource timeline](../../program/shared-use.md)
to obtain an authorized staffing or booking correction rather than average demand.

**Changed load.** A replacement handling envelope1.30×1.00m plus the same supplied
allowances needs1.40×1.10m, failing B's1.30m width under the stated procedure.
A conditional B width1.50m, `[0.8,2.3] × [1.2,2.9]`, avoids the supplied column
and reconnects to A; its area2.55m² reduces residual to14.09m². Retest the actual
new sweeps, receiving/storage state and neighbors before retaining it. If B is
fixed, choose an evidenced different load/handling or physical approach; do not
grant rotation, a smaller allowance or safe occupation without evidence.

## Evidence, related decisions and limits

This orthogonal containment/sweep derivation and studio are original dimensional
synthesis extending the existing local room-fit mechanism, with no new book,
image or upstream reading. [Original synthesis](../../../sources/index.md#original-local-synthesis)
distinguishes it from retained bibliographic evidence. All quantities above are
supplied hypothetical inputs. The method rejects modeled conflicts and develops
conditional alternatives; it does not prove accessibility, fire safety, ergonomics,
structural capacity or a complete building's usable population.

- Requires — [Demand and room envelope](../../program/capacity-and-room-demand.md): obtain the actual activity and included action/handling space.
- Requires — [Area boundary](../../program/area-ledger.md): keep the same measured extent and count each piece once.
- Affects — [Complete closure and support journeys](../circulation/access-and-closure.md): local fit must survive the actual doors, hours and shared destinations.
- Verified by — [Section and services](../vertical/section-and-services.md): a valid floor envelope can still lack headroom or intersect equipment/support.
- Verified by — [Occupied environmental states](../../performance/comfort/operating-states.md): a new seat, route or cabinet location changes controls, view, air and privacy.
