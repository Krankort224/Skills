# Stair section and the walking envelope

Use this method when a proposed flight fits a floor opening but its vertical
connection is unresolved. Use [floor-opening support](../../construction/structure/walls-floors-openings.md#place-a-floor-opening-without-erasing-its-support)
for reactions and [requirements](../../requirements.md) for the applicable dimensional
rules. A study clearance is not a legal minimum; a plan rectangle is not a stair.

## Contents

- [Build and test the walking profile](#build-and-test-the-walking-profile)
- [Repair a conflict by changing the actual section](#repair-a-conflict-by-changing-the-actual-section)
- [Worked conditional section of a return stair](#worked-conditional-section-of-a-return-stair)
- [Source and completion boundary](#source-and-completion-boundary)

## Build and test the walking profile

Fix finished floor levels and distinguish risers, goings, nosings, intermediate
and end landings. Choose a whole riser count; reconcile its actual total rise
with the floor datum rather than leave a fractional last step. Trace the route
from the lower door to the upper door, including its occupied width and turns.
Read the lower flight, return flight and landing at their actual plan positions:
two lines overlapping in one projected section may occupy different y bands.

Build a walking-height profile z(s) along that route, and locate each real
overhead obstruction H(s): floor soffit, opening header, landing edge, beam,
roof framing, lining, duct or fixture. For an explicitly defined vertical study
envelope h, test `H(s)−z(s) ≥ h` at every relevant position. Check both sides of
each step/edge and each piecewise roof segment, not just one midpoint. State
the height-measurement convention; a tread-top study is not an approved
jurisdictional headroom measurement or a complete moving-body envelope.

The support below an upper landing is not an overhead obstruction to a person
standing on that landing. Conversely, an upper-floor beam can obstruct the
lower flight. Subtract the correct build-ups once from their own reference
datum. A beam's total depth and its downstand below a slab are different inputs.
Locate nosing, guard, handrail and installation reservations physically; they
can reduce clear width or intrude into an otherwise passing profile.

Test arrival doors, retained walls and supports on both levels. Do not carry an
upper wall through the opening or declare its weight absent. If headroom/route
depends on removing it, provide a real revised support mechanism and identify
construction sequence and temporary works for engineering development.

## Repair a conflict by changing the actual section

Compare shifting or lengthening the opening to expose the rising profile;
moving the first riser/landing away from a downstand; rotating/reorganizing the
flights; relocating a crossing service; or changing an actually permitted
floor/roof/support datum. Recheck the landing connection and all changed
reactions after each move. Enlarging the hole cannot repair an independently
fixed low roof over the upper arrival. Moving a stair can remove a previously
promised shaft or make the entrance/upper room inaccessible.

For a wall crossing the void, compare routing the stair beside the intact wall,
replacing the affected upper wall with a suitable lightweight organization, or
a developed transfer above the required walking envelope. A beam drawn at
floor level across an intermediate landing defeats the stair even if its plan
supports are plausible. Keep any transfer's loads, posts and foundation path
explicit; raising its outline is not a capacity check.

## Worked conditional section of a return stair

This original hypothetical continuation fixes lower FF0, upper FF+3.30, a
4.00×3.60 m structural void x7…11/y3.2…6.8 and a **study** clearance h2.55 m.
Trial20 equal risers give0.165 each; two10-riser flights have nine0.28 goings,
run2.52, an intermediate landing at+1.65 and upper arrival+3.30. These inputs
are not taken from a source stair table and do not prove a compliant geometry.

In the initial plan both flights ran x7…9.52, lower band y3.3…4.4 and return
band y5.3…6.4, with intermediate landing x9.52…10.62 across those bands. West
end landings were x5.9…7. The wider gap between flights already kept the upper
end landing north of a possible retained wall y4.85…5.15; headroom remained open.

| Position | Walking surface z | Minimum H for this study |
| --- | ---: | ---: |
| First lower tread |0.165|2.715|
| Second lower tread |0.330|2.880|
| Third lower tread |0.495|3.045|
| Ninth lower tread |1.485|4.035|
| Intermediate landing |1.650|4.200|
| First return tread |1.815|4.365|
| Last return tread |3.135|5.685|
| Upper arrival |3.300|5.850|

**Opening edge.** Upper finish0.12 and normal floor depth0.20 give soffit2.98.
If that closed floor extends above the third lower tread, clearance is
2.98−0.495=2.485 and fails. A total-depth0.60 header below structural top3.18
has underside2.58; even the first tread beneath it would have only2.415.
The original first riser exactly at the west frame edge has no positional
margin. Retain the structural hole but compare moving both flights+0.20 in x:
x7.20…9.72, landing x9.72…10.82, end landings extended to x7.20. West frame
x6.70…7.00 is now set back0.20 from the first riser. The upper end extension
is a developed landing-deck projection into the hole, not erased structure.
A trial0.10 east guard reservation ends10.92, inside x11. Actual body/guard/
nosing/connection fit must confirm these reservations.

**Crossing wall.** A possible wall at y5 must not hang unsupported above the
void. Its floor-level beam would obstruct the intermediate landing: underside
3.30 leaves1.65, and a0.60 beam with top3.30 leaves1.05. Compare a raised beam
along y5, underside4.30/top4.90, between actual side posts centered x6.85 and
11.15 with a ground/foundation path. Its0.30 trial width stays in the gap
between flights; at the intermediate landing it gives4.30−1.65=2.65. The upper
wall's affected lower portion must be reorganized to bear on this proposal.
Member/post/foundation capacity and temporary support remain engineering work.
Services0.25 below this beam would reduce clearance to2.40 and fail.

**Unknown roof.** Two possible **required lowest-obstruction profiles**, not
surveyed heights, show what a roof proposal must provide:

- Flat: lowest lining/structure/service surface5.95 over flights and upper
  arrival. Arrival clearance2.65; the separately lower crossing beam still
  controls at the intermediate landing.
- East-descending: with a=7.20, set R5.95 for x≤a, then
  `R(x)=5.95−0.85(x−a)/2.52` to x9.72, and5.10 over the intermediate landing.
  Both ends of every tread must pass the study inequality. This profile gives
  minimum roof clearance2.65 at arrival; the crossing beam remains its own
  lower obstruction in the gap. Reserve roof supports outside these envelopes.

Those profiles already describe the **lowest** obstruction. Hanging a further
0.25 services below them leaves only2.40 at arrival unless the roof rises.
If actual roof clearance above the fixed arrival is below5.85, the fixed
levels and study height are incompatible there; moving the opening alone is
not a solution. The larger flight gap/shift also invalidates any old shaft
reservation it now occupies: relocate and frame that shaft explicitly, then
recount the lost floor area.

## Source and completion boundary

P05 file315/printed9.03,316/9.04 and318/9.06 were visually read for riser/run
reconciliation, landing/door/overhead relationships and paired plan/section
logic. No US/ADA stair/ramp formula, dimension, guard/handrail threshold or
general exit-capacity rule is adopted. The worked geometry is original.
The conditional section resolves specific conflicts; it is not a completed
stair. Actual roof/head profiles, upper-wall loads, structural capacity,
handrails/guards, landing doors, service route and construction sequence must
be verified before calling the stair usable or accepted.
