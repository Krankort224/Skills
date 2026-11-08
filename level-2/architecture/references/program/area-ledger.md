# Area boundary and ledger

## Contents

- [How can areas be counted once and compared?](#how-can-areas-be-counted-once-and-compared)
- [Connect the ledger to geometry](#connect-the-ledger-to-geometry)
- [Provenance and use limits](#provenance-and-use-limits)
- [Related decisions](#related-decisions)

Select this method for its question; reuse accepted project facts and decisions. Numerical examples are hypothetical, not area standards. Apply [requirements](../requirements.md) only to the actual jurisdiction and use; demand does not establish physical fit or compliance.

## How can areas be counted once and compared?

**Decision and boundary.** Establish a consistent area basis and expose missing
allowances before using a total for a fit or option comparison. Define the
measurement boundary, units and inclusions. GFA, GIA and NIA depend on their
measurement conventions and are not interchangeable local legal categories.
When a formal metric is needed, identify the governing published method and
version. Do not silently convert one into a statutory area.

1. Give each physical space a stable ID, activity, quantity, capacity, unit area
   and total, source or assumption, confidence, and special relationships. For
   known values, total = quantity × unit area, with area in the same units.
   An unknown area stays blank or is an explicitly labeled working allowance
   agreed for the study; it is not a standard.
2. Assign each physical area once to a defined category. Identify whether room
   circulation is already included in each unit area; distinguish it from shared
   corridors, lobbies, stairs, lifts, plant, shafts and structural elements.
   A shared room appears once as a physical area even when several user groups
   use it. Note its allocations separately without summing them again.
3. Add only mutually exclusive components inside the chosen boundary. If a
   combined core allowance already includes a lobby or shaft, do not add that
   component again. If using a factor instead of explicit components, state its
   denominator and precisely what it covers; do not add covered items separately.
4. Show a subtotal of known areas and list missing components. A range is useful
   only if its assumptions and endpoints are clear. A ratio can check a defined
   relationship, but cannot turn an incomplete schedule into a measured total.
5. For floor fit, compare the assigned area plus uncovered circulation and core
   components with available area on the *same* boundary. A positive arithmetic
   remainder does not prove the shape, access or structure works; test those
   spatially. See [calculators](../calculators.md) for calculation scope.

Cross-check the total independently by use and by assigned floor. Those two
sums must agree before the remainder is used for a decision. Correct an arithmetic
discrepancy rather than carrying one total in the introduction and another in
the floor ledger. For required clear room areas use
[clear-area construction](../space/planning/room-floor-and-section.md#construct-a-clear-area-fit-with-explicit-wall-reservations)
to test walls and shared movement explicitly.

For Russia, choose the measurement **purpose** before translating the ledger.
Keep the study's room/plate boundary alongside the selected Russian metric;
do not replace GFA/GIA/NIA labels with Russian words and preserve their totals.
Use the [local measurement selection](../normative/ru/applicability.md#choose-the-area-and-capacity-basis)
and the relevant [СП 54](../normative/ru/building-typologies.md#sp-54-13330-2022),
[СП 55](../normative/ru/building-typologies.md#sp-55-13330-2016) or
[СП 118](../normative/ru/building-typologies.md#sp-118-13330-2022) owner.

| Decision being made | Preserve in the architectural ledger | Establish before a formal Russian total |
| --- | --- | --- |
| Fit furniture or an activity inside a room | Finished clear shape, obstructions and uninterrupted activity envelope | Selected room measurement rule and treatment of its special parts; a room reservation including walls is not that measurement |
| Fit the program on a floor | Actual floor boundary, rooms, walls, shafts, shared routes and residual, each counted once | Applicable floor/building definition and treatment of voids, stairs and external parts; a plate remainder is not automatically usable room area |
| Report a dwelling/apartment area | Each room and auxiliary space, with balconies/loggias/terraces identified separately | Purpose of the figure: design, housing-law area or cadastral measurement; use the selected definition rather than a generic net/gross factor |
| Compare public-building totals | Room schedule and separate circulation, engineering and external-space components | Which of общая, полезная or расчетная площадь is actually requested and its current inclusions/exclusions; these labels are not synonyms |

**Boundary correction.** A supplied 6.000 × 4.000 m room block is 24.000 m²
between its stated unfinished faces. With a hypothetical 0.050 m finish on each
face, its finished rectangle is 5.900 × 3.900 = 23.010 m². Before: 24.000 m² is
credited against a client requirement for 24.000 m² finished room area. After:
credit 23.010 m² and show the 0.990 m² shortfall. If the 4.000 m unfinished depth
is fixed, a 24.000 m² finished rectangle would need unfinished width
24/3.900 + 0.100 ≈ 6.254 m; retain that as a conditional enlargement or change
the permitted arrangement. Do not take the extra width from an accepted route.
The arithmetic is geometric, with hypothetical finishes. A formal Russian room
area remains unresolved until its current measurement provision is selected;
neither this example nor a successful area calculator supplies that provision.

**Small check.** Two rooms at 20 m² each plus one shared room at 30 m² total
70 m² of listed rooms. If a 10 m² lobby is included in the core allowance, adding
it again as circulation overstates the total by 10 m². If the core area is
unknown, 70 m² is a partial subtotal, not the building total.

### Connect the ledger to geometry

At early blocking stage use reservation polygons, not a falsely precise net
schedule. A room block can contain its enclosing partitions and local furniture
access; call it a reservation until those are drawn. Give every piece of floor
one owner. Subtract voids at the level where there is no floor, not at every
level beneath a roof opening. Count an open terrace or external gallery on its
own stated basis, without mixing it into enclosed usable area. Sloping ceilings
need both footprint and usable-height information; a rectangular footprint alone
can conceal unusable occupation.

For a rectangle, area = width × depth; for an L-shape, sum two nonoverlapping
rectangles or subtract the missing corner from the enclosing rectangle. Track
core, shared movement, room reservations, separately drawn structure/partitions
and residual area so their sum equals the same measured floor boundary. A tiny
triangular remainder beside a core may be geometrically real but unable to house
any activity. Keep it residual instead of crediting it as a missing room.

If a schedule is larger than the available plate, no rearrangement can fix that
arithmetic. If it is smaller but still does not fit, look for deficient frontage,
wrong proportions, disconnected remnants, excessive route depth or fixed
obstructions. Revise the responsible variable rather than shrinking all rooms
uniformly. See the [worked ledgers](../space/planning/room-floor-and-section.md#worked-design-progressions).

## Provenance and use limits

The operative reasoning is local; external reading is not a runtime prerequisite. [Pinned readings, adaptations and exclusions](../../sources/upstream-packs.md#program-and-space) retain the source identity, inspected extent and limitations. Use [requirements](../requirements.md) for jurisdiction-specific applicability.

## Related decisions

- Verified by — [Planning and section](../space/planning/room-floor-and-section.md#construct-a-room-that-can-be-used): check wall, door and finished-room geometry rather than treating a subtotal as a fitted plan.
- Affects — [Capacity and room demand](capacity-and-room-demand.md): recheck actual capacity when the measured boundary changes.
