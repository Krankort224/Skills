# Occupied daylight, view and control

## Contents

- [Daylight, view and occupied comfort](#daylight-view-and-occupied-comfort)
- [Generate room and section schemes](#generate-room-and-section-schemes)
- [Separate sun, sky, view and control](#separate-sun-sky-view-and-control)
- [Construct a finite-canopy ray check](#construct-a-finite-canopy-ray-check)
- [Test a finite canopy with bounded input uncertainty](#test-a-finite-canopy-with-bounded-input-uncertainty)
- [Fit Russian room conditions without merging their tests](#fit-russian-room-conditions-without-merging-their-tests)
- [Provenance and use limits](#provenance-and-use-limits)
- [Related decisions](#related-decisions)

Use this method to generate, test and revise the spatial solution. Proposed architectural reservations do not establish loads, member/equipment sizes, physical performance, technical safety or compliance; obtain the project-specific evidence needed for those claims. Select [requirements](../../requirements.md) for the actual jurisdiction. Example dimensions are hypothetical inputs, not standard sizes or certified performance; no environmental simulation is claimed.

## Daylight, view and occupied comfort

Start with an occupied position and activity, rather than a glazing percentage.
Record orientation and hemisphere, neighboring heights/distances, room depth,
window sill/head, reveals, ceiling level, furniture and eye/task positions. Use
actual occupied periods, climate and privacy needs. A tall neighbor may remove
sky even where there is plenty of glass; a deep reveal can protect from sun and
rain while further restricting that sky.

### Generate room and section schemes

| Scheme | Spatial reason to try it | Consequence to test and possible revision |
| --- | --- | --- |
| Shallow perimeter room with punched windows | Direct view and sky access can serve a defined band of activity; opaque piers provide storage, support and privacy | Check rear positions separately. Move low-occupancy storage inward, raise the window head where the section permits, or shorten room depth; widening glass below the task does little to remove an obstruction above it |
| Room lit from two sides | Different sky directions can reduce dependence on one bright facade and allow a quieter opening | Check glare from both directions, cross-views and supports at the corner. Retain a pier or column when removing it would create an unjustified transfer |
| High daylight opening plus lower view opening | Separate access to sky from seated views/privacy; each band can have a different shade | High glass alone provides no seated view. Keep a usable view band, inspect overhead glare and make upper controls reachable or maintainable |
| Roof monitor or clerestory over a deep/top-floor room | Brings sky to the interior without giving every activity street exposure | Select its orientation from actual sun paths, not a universal north-facing rule. A glowing roof opening, direct sun patch, rain noise, roof structure, drainage and cleaning may defeat the intent; use an opaque baffle or indirect ceiling wash where appropriate |
| Courtyard or light slot with rooms around it | Adds a second edge to a deep building and can separate noisy street frontage from quieter use | Lower levels may still see little sky. Test opposing heights, court width, overlooking and sound reflection; enlarge/reposition the void or reduce depth instead of counting it as guaranteed daylight |
| Reflecting shelf or bright upper ceiling | May redistribute admitted light while controlling the near-window band | A shelf also blocks sky/view and needs cleaning. A beam, bulkhead or dark ceiling can interrupt the route; coordinate the section before retaining it |

A view must be tested from actual seated and standing positions, including users
at different heights. A narrow high slot is not equivalent to an outward view.
Place desks so the window is to the side where this suits the use: a window
behind the screen can reflect in it; a bright window behind the subject can
impair face recognition. Neither arrangement is universally preferable without
the activity and sightline.

### Separate sun, sky, view and control

In plan and section trace: (a) visible sky from front and rear positions,
(b) sightlines out and in, and (c) representative sun rays at occupied times.
For a simple geometric ray test, state the assumed sun direction/angle and the
shading dimensions; account for oblique sun and finite device width in plan as
well as section. This is a geometric test, not a daylight, glare or thermal
prediction. Do not turn a window-head rule of thumb into proof of illumination.

A horizontal overhang can intercept high sun while leaving some lower views;
low sun near the facade normal may pass below it. A fin can intercept oblique
sun yet block a desired oblique view and can do little against sun normal to the
opening. Adjustable external shades intercept sun before it reaches the glass
but require wind, ice, cleaning and repair provisions. Internal blinds can help
with visual control but should not be credited with the same solar-heat control.
Darker glass can reduce transmitted light along with glare and still leave a
bright source; it does not replace examining the occupied view.

Test controls both deployed and retracted. If one blind closes the entire facade
for privacy, its nominal daylight/view benefit may disappear during occupation.
Consider independently controlled upper/lower bands, selective translucent
privacy areas, a screened retreat or relocating an activity. Preserve electric
lighting provision for occupied periods and positions that daylight may not
serve. Specify the next question precisely: for example, annual glare at the
western reading desks with the chosen shade states, rather than “check daylight.”
Use [calculators](../../calculators.md) only within their documented scope.

### Construct a finite-canopy ray check

A facade-normal section alone cannot decide whether an oblique ray misses a
finite side edge. This original coordinate construction checks one supplied
direction and one point on the glazing, without requiring an external source
pack or claiming annual daylight/glare performance.

Place the facade at `x = 0`, exterior at positive x, lateral position along y
and height along z. Model a thin horizontal rectangular canopy at `z = h`,
spanning `0 ≤ x ≤ D` and `y_left ≤ y ≤ y_right`. The tested facade point is
`(0, y_p, z_p)`, below the canopy. Use consistent metres for all lengths.
Supply solar altitude `alpha` above the horizon and signed horizontal angle
`gamma` from the outward facade normal, positive toward increasing y; use degrees consistently when evaluating
trigonometry. This front-face construction assumes `0 < alpha < 90°` and
`abs(gamma) < 90°`. It does not infer sun position from a city, civil time or date.

Trace from the point toward the sun. A vertical rise `h − z_p` intersects the
canopy plane at:

- `x_hit = (h − z_p) × cos(gamma) / tan(alpha)`;
- `y_hit = y_p + (h − z_p) × sin(gamma) / tan(alpha)`.

The idealized canopy blocks that ray only if both coordinates lie inside its
actual rectangle. This follows from the ray's vertical, facade-normal and
lateral components; it is not a device efficacy factor. For infinite width the
vertical shadow drop at the outer edge is `D × tan(alpha) / cos(gamma)`, reducing
to `D × tan(alpha)` for a facade-normal ray. Finite width must still be checked.

**Failure and correction.** With hypothetical `h = 3.00`, `D = 0.70`, canopy
width `y = −0.60…+0.60`, tested point `(0, 0, 2.60)`, altitude `20°` and
horizontal angle `60°`, the hit is approximately `(0.549, 0.952, 3.00)`.
It lies within the depth but beyond the side edge. An infinitely wide/profile
section predicts shading at that height, while the supplied finite canopy does
not block this ray. Widening the rectangle to `y = −1.00…+1.00` blocks this one
point/direction in the model; adding projection depth alone does not repair the
side miss. Retest other glazing points, direction signs and occupied periods.

A moved/lowered/widened shade changes views, sky access, privacy, support and
maintenance. For sloping, thick, perforated or irregular devices, test the real
faces/openings rather than treating the rectangle as their equivalent. A blocked
glazing-point ray is not a room illuminance, glare, thermal, safety or legal
result; an occupant claim also needs the actual opening, inside/neighboring
obstructions and deployed control state. Keep uncertainty in the supplied angles
and geometry explicit.

#### Test a finite canopy with bounded input uncertainty

**Decision and inputs.** Does the selected ray-interception claim survive the
supplied dimensional and angular bounds, or only the nominal values? This
original geometric method extends the [point/ray construction](#construct-a-finite-canopy-ray-check).
It checks an ideal thin horizontal rectangle and a bounded family of glazing
points/directions, not annual sun, a probability of comfort or a product size.
Record the datum, units, source and meaning of each bound: measured uncertainty,
installation reservation, selected point range or supplied direction range.
An unknown is not a zero allowance. Do not invent a tolerance or derive actual
sun directions from this method.

Use finite, ordered intervals `h_lo…h_hi`, `z_lo…z_hi`, `y_lo…y_hi` for canopy height, tested
point height and lateral point position; use degrees for `alpha_lo…alpha_hi`
and signed `gamma_lo…gamma_hi` in the preceding coordinate convention. First
require `h_lo > z_hi`, `0 < alpha_lo ≤ alpha_hi < 90°` and
`−90° < gamma_lo ≤ gamma_hi < 90°`. All lengths are metres. If a bound leaves
that below-canopy/front-face domain, this construction cannot certify the whole
range; separate the relevant physical cases and use their actual ray/face
intersections. Do not clamp the angles to make a result pass.

**Construct an enclosing hit range.** Treat the stated inputs as independently
variable for this calculation unless their joint constraints are established:

1. Subtract the height intervals in opposite order:
   `Delta_lo = h_lo − z_hi`, `Delta_hi = h_hi − z_lo`.
   For independent `h = 3.00 ± 0.02` and `z_p = 2.60 ± 0.02`, the rise is
   `0.36…0.44`, not `0.38…0.42`. A shared datum error could correlate the two
   heights; retain such evidence rather than assuming either cancellation or
   independent worst errors.
2. Let `r = Delta / tan(alpha)`, the horizontal distance from the point to its
   canopy-plane intersection. Since positive cotangent decreases with altitude,
   `r_lo = Delta_lo / tan(alpha_hi)` and
   `r_hi = Delta_hi / tan(alpha_lo)`.
3. Obtain `c_lo` and `c_hi`, the minimum and maximum of `cos(gamma)` over the
   supplied range. In this front-face domain the minimum is at an endpoint;
   the maximum is `1` if the range includes `0°`, otherwise the larger endpoint
   cosine. Then `x_min = r_lo × c_lo`, `x_max = r_hi × c_hi`.
   Endpoint-only checking is insufficient when the range crosses the normal:
   for `gamma = −20…+20°`, the largest x occurs at `0°`, not at either end.
4. Sine increases throughout this domain, so set
   `s_lo = sin(gamma_lo)`, `s_hi = sin(gamma_hi)`. Form the four products
   `r_lo × s_lo`, `r_lo × s_hi`, `r_hi × s_lo`, `r_hi × s_hi` and take their
   minimum `q_lo` and maximum `q_hi`. The lateral bounds are
   `y_min = y_lo + q_lo`, `y_max = y_hi + q_hi`.
   This product check retains the sign when rays come from either side or the
   range crosses zero; always pairing the largest r with the smallest signed
   sine does not give both extrema.

These extrema enclose every hit in the independent input box; x and y extrema
need not belong to the same ray. Do not combine their tuples into a fictional
single worst sun position. A rectangular box can be conservative when altitude,
horizontal angle, point position or measured heights are correlated. If a
negative margin matters, identify its realizing input tuple and establish
whether that tuple is actually allowed. A narrower joint range needs evidence,
not deletion of an inconvenient endpoint. Sampling can expose a missed case
but cannot prove an unsampled continuous range safe.

**Judge the claim on guaranteed geometry.** For a fixed rectangle require
`0 ≤ x_min`, `x_max ≤ D`, `y_left ≤ y_min` and `y_max ≤ y_right`.
If its edge positions are also bounded, use the rectangle common to all allowed
positions: the smallest projection D, largest left-edge coordinate and smallest
right-edge coordinate; if no common rectangle exists, no guarantee follows
from this enclosure test. Report depth margin `D − x_max`, left margin
`y_min − y_left` and right margin `y_right − y_max` on that guaranteed geometry.
All must be nonnegative for every boxed ray to be intercepted in this ideal
model. Equality is contact with an ideal edge, with no spare geometric margin.
A negative margin defeats that guarantee; show a permitted miss before calling
the actual project constraints incompatible.

**Original hypothetical stress and correction.** Keep `h = 3.00 ± 0.02`,
`z_p = 2.60 ± 0.02`, `y_p = −0.05…+0.05`, `alpha = 18…22°` and
`gamma = 55…65°`, with independent bounds. A fixed `D = 0.70`,
`y_left = −1.00`, `y_right = +1.00` blocks the nominal 20°/60° ray at
`(0.5495, 0.9518)`, but the full calculation gives
`r = 0.8910…1.3542`, `x = 0.3766…0.7767` and `y = 0.6799…1.2773`.
Depth and right margins are approximately `−0.0767` and `−0.2773`.
The depth maximum uses `h = 3.02`, `z_p = 2.58`, `alpha = 18°`,
`gamma = 55°`; the lateral maximum instead uses `gamma = 65°` and
`y_p = +0.05`. Both are allowed misses under these independent study inputs.

If a changed rectangle is permitted, trial `D = 0.80`, `y = −1.30…+1.30`.
Its depth/right margins are only about `0.0233/0.0227 m`; it intercepts the
selected bounded ray family, before any additional unrepresented uncertainty.
This is a conditional geometric alternative, not automatic shade sizing or
supplier/structural confirmation. If projection and width are fixed at the
smaller values and the whole stated family must be blocked, retain the conflict.
Compare an authorized geometry change, another independently usable control,
or a genuinely permitted activity/position change and retest its new inputs;
do not silently enlarge the canopy or narrow the required directions.

**Changed use and competing consequences.** Moving the tested band down to
`z_p = 2.50 ± 0.02` with the other bounds retained increases the maxima to
about `x = 0.9533`, `y = 1.5562`, so even the trial enlarged rectangle fails.
The previous pass was neither a whole-opening nor an occupied-task result.
Larger shades can cost sky/view and change head/support and cleaning space;
test their [opening junction and attachment](../../construction/envelope/assemblies.md#opening-head-jamb-and-sill)
and [complete replacement journey](../lifecycle/intervention-and-cost.md#trace-a-complete-maintenance-journey).
Use [coexisting occupied states](operating-states.md#develop-states-that-can-actually-coexist)
for the actual control consequence. If a retractable option must stow in wind,
its deployed rectangle supplies no interception in that state. If privacy closes
the required view band, neither a larger canopy nor this ray calculation restores
the view. Compare a compatible independent control or another suitable task
position, retaining the actual light/view/privacy and air/noise requirements.
Record unavailable modes and missing evidence through that existing state
method; no glare, illuminance, thermal, structural or legal result follows here.

### Fit Russian room conditions without merging their tests

For a confirmed Russian project, select the actual room activity and occupation
before assigning its facade. Use [SP 52](../../normative/ru/environment-and-interfaces.md#sp-52-13330-2016)
for the relevant lighting question, [SP 51](../../normative/ru/environment-and-interfaces.md#sp-51-13330-2011)
for noise and the [sanitary environmental-factor record](../../normative/ru/environment-and-interfaces.md#sanpin-1-2-3685-21)
for the affected room-specific conditions. Their records do not supply a
verified numerical target. Keep a room's lighting/КЕО question separate from
whether an insolation provision applies to that room or its host use. Direct
sun duration, available diffuse sky, glare, outlook and privacy answer different
questions; a sun ray drawn through a window cannot pass them all.

| Actual trigger | Spatial response to develop | Retest before retaining it |
| --- | --- | --- |
| Quiet sustained work at a noisy street | Compare a shallower street room with a quieter-side room; put storage/service depth on the more exposed edge where compatible | The quieter side still needs usable sky/openings; closed street windows need an actual alternative air path. Do not exchange a noise conflict for an unserved deep occupied room |
| Residential host with public use or production below/beside it | Separate sensitive sleeping/quiet positions from deliveries, impact, plant and evening events in plan and section | Check receiver/use and occupied time independently of the tenant label. A quiet office proposal and a noisy workshop are different inputs even within the same shell |
| Required privacy at an occupied window | Test offset sightlines, selective screening and independently controlled upper light/lower view bands | Inspect the actual occupied shade state and neighboring windows. Screening that removes useful sky may require shallower rooms, a different facade allocation or a different activity |
| Café, workplace or children's activity replaces generic public occupation | Refit food/staff/visitor/waste routes, wet support and occupied room positions to the actual operation | Read the selected current activity-specific sanitary provisions and project dates before treating the generic room as sufficient; new occupancy can change more than furniture count |

For the last row use the matching [catering](../../normative/ru/environment-and-interfaces.md#sanpin-2-3-2-4-4282-26),
[workplace](../../normative/ru/environment-and-interfaces.md#sp-2-2-4285-26) or
[children's activity](../../normative/ru/environment-and-interfaces.md#sp-2-4-2-4283-26)
record. Their primary-text gaps remain unresolved; no sanitary occupancy,
permitted use, glazing percentage, insolation duration or noise limit is inferred
here. Keep the useful plan alternatives while the specific missing provision is
resolved, and replace only the affected alternative when the evidence changes.

## Provenance and use limits

The operative reasoning is local; external reading is not a runtime prerequisite. [Pinned readings, adaptations and exclusions](../../../sources/upstream-packs.md#performance-and-coordination) retain the source identity, inspected extent and limitations. Use [requirements](../../requirements.md) for jurisdiction-specific applicability.

## Related decisions

- Requires — [Planning and section](../../space/planning/room-floor-and-section.md#construct-a-room-that-can-be-used): identify actual occupied positions and room/opening geometry.
- Verified by — [Multi-building direct-sun intervals](multi-building-sun.md): when neighboring volumes determine a selected point's direct sun, test actual solids, receiver height, time basis and blocked-interval union. This geometric check does not verify illuminance, glare or statutory insolation.
- Affects — [Acoustic paths and air modes](acoustics-and-air.md): opening/blind/shade states must coexist with noise and air needs.
- Verified by — [Envelope and assemblies](../../construction/envelope/assemblies.md#develop-four-connected-junctions): test the head, shade/control and enclosure interfaces.
- Illustrated by — [Street reading room](../../../assets/studies/street-reading-room.md): keep failed low-sun geometry, revised services and conditional margins.
