# Multi-building shadows and direct-sun intervals

Use this method to compare actual obstruction geometry and direct-sun periods at
selected receivers. [Daylight/view](daylight-view.md) owns occupied lighting,
sky/view and control choices; [the solar calculator](../../calculators.md#solar)
owns its four-input preliminary position/shadow contract. This method adds
occlusion and time-interval construction, not an illuminance or compliance engine.

## Contents

- [Define receivers, solids and time](#define-receivers-solids-and-time)
- [Construct the shadow and test one ray](#construct-the-shadow-and-test-one-ray)
- [Find complete intervals for a declared solar model](#find-complete-intervals-for-a-declared-solar-model)
- [Combine buildings and bound the result](#combine-buildings-and-bound-the-result)
- [Worked two-building comparison](#worked-two-building-comparison)
- [Change height, position and resolution](#change-height-position-and-resolution)
- [Propagate the architectural decision](#propagate-the-architectural-decision)
- [Source boundary and related decisions](#source-boundary-and-related-decisions)

## Define receivers, solids and time

Record these inputs with source, date, units and uncertainty before calculating:

| Input | Definition and consequence |
| --- | --- |
| Coordinate frame | Local east E, north N, up U; metre coordinates and one vertical datum. State true/grid/project-north relation. A drawing's up direction is not automatically true north. |
| Receivers | Identify each site/activity point or actual window point P=(E,N,U). Give facade outward unit normal n when front-face sun is required. One point is not the whole window, facade or court. Use several declared samples or a complete surface test for a spatial claim. |
| Obstructions | Actual opaque solids: footprint, orientation, base/top levels and relevant roof, parapet, balcony/reveal geometry. Keep existing/proposed/uncertain parts identifiable. Empty bounding-box volume is not automatically opaque. |
| Solar/date/time source | Latitude, selected date(s), supplied declination or checked position series, horizon/refraction/disk convention, reference meridian/UTC offset/daylight-saving and conversion evidence. Unknown civil-to-solar conversion prevents a clock-time result. |
| Evaluation domain | Requested time window and occupied/seasonal question; receiver/front-face eligibility; boundary-contact convention; numeric and geometry/time uncertainty. No generic statutory test date, duration, minimum altitude or sample interval is supplied. |

The complete interval construction below is bounded to fixed points and finite
unions of **vertical rectangular prisms**, each permitted its own horizontal
yaw, and a fixed-declination geometric solar model. Require finite positive
prism dimensions, a receiver strictly outside every closed obstruction, and
−90°<latitude<90°. For a true L-shaped mass use its actual nonoverlapping pieces;
for sloped/curved/porous roofs, terrain or trees use actual suitable geometry and
verified ray intersection. A solid enclosing box gives a conservative obstruction
screen only: its predicted blockage need not exist in the real empty portions.
A ray missing a verified enclosing box also misses the enclosed solid; a hit
requires the real geometry before claiming actual shade.

A window's host cannot be one solid box containing the receiver and its opening.
Represent the actual opaque sides/reveals/shades without filling the aperture.
Do not solve self-intersection by an unexplained offset or by deleting all host
shading. Resolve a coincident/inside point or use a documented boundary method
before relying on its result. The ideal sun here is a point at infinite distance;
clouds, transmission, diffuse sky, reflections and the solar disk are excluded.

## Construct the shadow and test one ray

For supplied altitude α and north-clockwise azimuth A, the direction **toward**
the sun is s=(cosα sinA, cosα cosA, sinα). Use consistent degree/radian conversion.
Trace P+λs with λ>0, not P−λs. U-component ≤0 is outside geometric above-horizon
eligibility. A facade point additionally needs n·s>0; sun behind the facade is
not an obstruction-caused interval. At zenith a vector remains usable even when
azimuth is undefined. Near the horizon retain the declared precision limit.

For a horizontal receiver plane at z_p, project each obstruction vertex Q at or
above that plane away from the sun:

`Q_shadow=(Q_E−(Q_U−z_p)s_E/s_U, Q_N−(Q_U−z_p)s_N/s_U, z_p)`.

For a convex solid clipped above the plane, the convex hull of the projected
vertices is its ideal shadow polygon. Clip at the plane first if the solid
crosses it; do not project below-plane volume as an obstruction above the receiver.
Union the polygons of separate bodies instead of summing overlapping areas.
At another receiver height, reclip/reproject: a ground diagram cannot establish
a window's exposure. For a nonhorizontal facade, intersect its actual plane or
test the selected points directly; the horizontal projection is not that facade.

For a prism rotated θ counterclockwise from east, with horizontal origin O,
transform the ray into its own axes:

`p_x=cosθ(P_E−O_E)+sinθ(P_N−O_N)`;
`p_y=−sinθ(P_E−O_E)+cosθ(P_N−O_N)`; `p_z=P_U`;
`s_x=cosθ s_E+sinθ s_N`; `s_y=−sinθ s_E+cosθ s_N`; `s_z=s_U`.

Its local bounds are [l_i,u_i] for i=x,y,z. Intersect three parameter intervals:

1. Start λ_near=0, λ_far=+∞. If s_i=0 and p_i is outside [l_i,u_i], the ray
   misses. If it is inside, that slab imposes no parameter restriction; do not
   divide by zero or replace a small direction by zero without a justified bound.
2. Otherwise compute `(l_i−p_i)/s_i` and `(u_i−p_i)/s_i`, order them, then take
   max with λ_near and min with λ_far. An empty interval is a miss.
3. After all three slabs, λ_near≤λ_far and λ_far>0 means a closed-solid hit.
   Retain the body and hit location. Exact tangency counts as a blocked contact
   under this conservative convention; isolated instants have zero duration.
   A contact within uncertain geometry is a borderline result, not robust shade.

This supplies a checkable 3D result with a named cause. Closest hit is useful for
diagnosis, but any hit blocks the ideal ray. Removing the first building can
leave another behind it; retain all contributors when testing a correction.

## Find complete intervals for a declared solar model

Do not declare a whole interval clear from two clear endpoints. A narrow shadow
can pass between them. A status-changing bracket can be refined, but bisection
alone neither discovers all transitions nor proves that a bracket contains only
one. Use a complete event construction for the supported model below, or a
separately justified temporal enclosure for the actual model.

For latitude φ, **supplied constant** declination δ and local apparent solar
time h, use H=15°(h−12), with:

`s_E=−cosδ sinH`;
`s_N=cosφ sinδ−sinφ cosδ cosH`;
`s_U=sinφ sinδ+cosφ cosδ cosH`.

These match the existing calculator's spherical geometry and north-clockwise
azimuth convention. The calculator still accepts one instant, apparent solar
time and a supplied declination; it does **not** calculate date/clock conversion,
receiver height or occlusion. Its numerical horizon/undefined-azimuth guards
are not new physical tolerances. Check a vector directly at zenith and leave
the unresolved near-horizon band explicit.

With φ and δ fixed, every world/local component has form
`a sinH+b cosH+c`. Rotating a prism or forming n·s preserves that form.
For each point/prism pair generate candidate events in the chosen window:

- s_U=0 and, when relevant, n·s=0: eligibility changes;
- each local s_i=0: slab direction/sign changes;
- for **every pair of different axes** i,j and every choice of one boundary
  on each axis, let d_i=boundary_i−p_i and d_j=boundary_j−p_j; solve
  `d_i s_j−d_j s_i=0`. These are equality events of face-intersection parameters,
  including edges a ray may graze. Do not select only the intuitively nearest face.

Each equation is A sinH+B cosH+C=0. With R=hypot(A,B)>0 and β=atan2(B,A),
solve sin(H+β)=−C/R: both branches `asin(−C/R)−β+2πk` and
`π−asin(−C/R)−β+2πk`, retaining only roots inside the window. If |C|>R there
is no real root; if R=0, the equation is either an identity or has no roots.
An identity needs no isolated event because the tied order persists. Handle
near-identities/tangencies with explicit numeric/geometry uncertainty rather
than silently clamping an unreliable root or deleting a short interval.

Add the window ends, sort events and test a midpoint of **every** open cell with
the full slab and eligibility tests. Within a cell all component signs and
face-parameter orders are fixed, so hit status cannot change there. This is why
the event list, rather than a chosen coarse time step, establishes completeness
for these prisms and this solar model. Classify boundary contacts separately;
zero-duration contacts do not add hours. Split midnight/wrapped windows by date
and use their actual inputs; do not carry yesterday's declination into a new day.

The construction is exact in its declared mathematical model, **not an accuracy
claim for the real sun/date or a survey**. Declination varies, refraction/disk and
geometry/time inputs can move transitions. With a varying-declination ephemeris,
complex solids or moving controls, use that actual model with verified event
search/enclosures; this fixed-δ event proof does not automatically transfer.
A denser sample alone is evidence at those samples, not completeness between them.

## Combine buildings and bound the result

Build eligible intervals E where the geometric sun is above the horizon and,
for a facade claim, in front. Keep night/back-face periods distinct from building
blockage. For each body retain its blocked subset B_j of E. Sort the blocked
intervals by start and merge overlaps/touching boundaries once. Direct sun is
`D=E \ union(B_j)`. Record both the total duration and individual continuous
intervals; neither maximum continuous duration nor fragmented legal credit is
determined by a sum alone. Apply any actual aggregation/exclusion rule only after
selecting its jurisdiction/version, receiver and test-date basis.

Choose a reporting time tolerance ε_t for the decision, not as an assumed solar
accuracy. Re-evaluate each analytic candidate and the ray on both sides; retain
an enclosing transition band if the root, geometry or solar input is uncertain.
Close roots/tangent cases need their whole uncertainty bands, not a rounded
single event. For the supported event model numerical refinement can narrow a
root band; it cannot remove uncertain survey heights or declination/time choice.

Keep a definitely-blocked set B_def and a possibly-blocked set B_pos across the
justified uncertainty enclosure: B_def is blocked for every admissible realization,
and B_pos encloses every possible blockage. Similarly E_def is always eligible
and E_pos encloses all possibly eligible times. A
conservative direct-sun lower set is E_def\B_pos; an upper set is
E_pos\B_def. For the nominal case with known eligibility and m isolated boundary
bands of width at most w, the unclassified duration is at most m w, after union
and clipping. Do not count overlapping uncertainty bands twice. If completeness
of the event set/enclosure is unproved, this duration-error bound is unproved too.
Varying a few corners of an arbitrary uncertainty box is not a guaranteed bound;
provide a valid enclosure or report nominal results and the missing robustness.

For a picture at a selected instant, label sun input, coordinates, receiver plane
and actual solid approximation. For intervals, give the date/model/time basis,
receiver, obstruction IDs, eligible/blocked/direct spans, transition precision
and missing evidence. A rendered shadow picture is not an interval calculation.

## Worked two-building comparison

All dimensions/time choices are original hypothetical inputs. Select φ=45°,
δ=0°, apparent solar window 06:00–18:00 and a low receiver P=(0,0,1) m with a
south-facing normal (0,−1,0). This is a geometric equinox-style model, not a
selected statutory test date or clock-time conversion. Opaque prisms are:

| Body | East interval, m | North interval, m | Base/top, m |
| --- | --- | --- | --- |
| A | 4…8 | −6…−4 | 0…9 |
| B | 2…6 | −8…−6 | 0…11 |

For this special model s_N/s_U=−1 and q=s_E/s_U=−√2 tanH. Along a ray whose
vertical rise from P is v, N=−v and E=qv. A's north slab gives v=4…6 and its
top does not further restrict it: a hit needs 2/3≤q≤2. B similarly gives
v=6…8 and 1/4≤q≤1. Solving these endpoints independently of a 3D ray routine:

| Quantity | Apparent solar decimal hours | Duration, h |
| --- | --- | ---: |
| A blocked | 8.3509593122…10.3173732120 | 1.9664138998 |
| B blocked | 9.6490406878…11.3316674759 | 1.6826267880 |
| Overlap | 9.6490406878…10.3173732120 | 0.6683325241 |
| Blocked union | 8.3509593122…11.3316674759 | 2.9807081637 |

Adding the two blocked durations would overstate blockage by 0.6683325241 h.
Within the geometric 12 h eligibility window, direct sun is
06:00…8.3509593122 and 11.3316674759…18:00, total 9.0192918363 h. Displaying
ten decimals permits arithmetic reproduction, not a ten-decimal observational
accuracy claim. State any chosen display rounding and uncertainty separately.

## Change height, position and resolution

At P=(0,0,6), A's north slab would require z=10…12>9 and B would require
z=12…14>11. Neither blocks: the high receiver has the full eligible window.
Do not reuse the ground/low-window result for that point or credit its exposure
to all lower windows. Retest actual front-face eligibility on a changed facade.

Lower B's top to8 m while retaining P_z=1. Its allowed rise becomes6…7, hence
2/7≤q≤1. B's end moves to11.2385497561; the blocked union shortens by
0.0931177198 h (about5.59 min), leaving direct sun to start earlier. Reducing
height changes an actual interval, not merely a shadow's graphic length.

Alternatively move B to east bounds−6…−2 with its other bounds unchanged.
Its blockage moves to12.6683325241…14.3509593122. A's earlier interval remains;
the gap between them is now direct sun. Recalculate interval union and continuous
spans; do not keep the old early/late classification after moving the body.

The original B end is11:19:54.003 in this model, only about6 seconds before an
11:20 grid mark. Samples at11:15 and11:20 establish only a5-minute transition
bracket. If those are the sole observations, do not report a second-accurate
time or credit the entire bracket. The event construction locates the model root;
with an explicitly justified ±1 s numerical band its unresolved width is2 s.
That chosen band excludes neither survey nor sun/time uncertainty. Samples at
08:00 and11:30 are both clear yet miss the entire intermediate blocked union,
demonstrating why equal endpoint status cannot certify an interval.

## Propagate the architectural decision

Compare alternatives at the same receivers, date/time basis and uncertainty.
Lowering/moving A or B, opening a gap or changing a court width can redistribute
light among several windows and outdoor uses. Recheck all material recipients,
not only the point that improves. An upper-floor benefit cannot compensate for
a required lower-floor failure unless the actual brief/authority permits it.

Carry changed footprint/height into the [quarter land balance](../../context/urban/quarter-and-public-space.md#reconcile-ground-use-without-double-counting),
housing floor/population assumptions, [service reservations](../../context/urban/service-capacity-allocation.md)
and [vehicle/servicing ground](../../context/urban/vehicle-and-parking-geometry.md)
when those consequences exist. Carry changed opening/shade/roof geometry into
[occupied daylight and control](daylight-view.md) and its actual construction/
maintenance interfaces. Retain a failed alternative if fixing its shade would
violate a fixed height/program/land constraint; identify the authorized decision
needed instead of silently shrinking the building or deleting a receiver.

## Source boundary and related decisions

[Primary source records](../../../sources/solar-occlusion.md) identify selected
ray/slab and solar evidence, rights and excluded content. The event partition,
interval accounting, examples and corrections are original synthesis. The four
calculator implementations/contracts remain unchanged; `test_sun_intervals.py`
contains bounded verification constructions, not a new supported solar/GIS engine.

- Requires — [Requirements](../../requirements.md): when a date, receiver, duration, fragmented credit or compliance conclusion depends on authority, select actual jurisdiction/version and detailed provisions; the geometry supplies none by default.
- Requires — [Site inputs](../../context/site/site-and-context.md#translate-climate-and-parcel-inputs-into-site-moves): when true orientation, neighboring solids, terrain or datums are unresolved, establish their evidence or keep alternatives conditional.
- Affects — [Daylight, view and occupied control](daylight-view.md#separate-sun-sky-view-and-control): changed obstruction/direct-sun intervals reopen the relevant opening/view/control choices, not an automatic illuminance prediction.
- Affects — [Quarter ground and activities](../../context/urban/quarter-and-public-space.md): when moving/reshaping a body or court displaces land/use, reconcile those reservations and affected receivers rather than treating the improved ray as the whole design.
