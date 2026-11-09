# Building volume: boundary, solids and reconciliation

Use this method for building volume (строительный объём), not merely a sum of
floor areas. [Area accounting](area-ledger.md) retains its own definitions;
[floor/roof organization](../space/planning/room-floor-and-section.md#reconcile-upper-floors-tall-rooms-and-roofs)
owns occupied levels and voids. The original examples below measure geometry,
not a jurisdiction's building-volume provision.

## Contents

- [Select the requested volume](#select-the-requested-volume)
- [Construct mutually exclusive solids](#construct-mutually-exclusive-solids)
- [Prism and clear-space counterexample](#prism-and-clear-space-counterexample)
- [Mixed roof, wing, basement and open court](#mixed-roof-wing-basement-and-open-court)
- [Change the height or boundary](#change-the-height-or-boundary)
- [Evidence and related decisions](#evidence-and-related-decisions)

## Select the requested volume

Record the purpose, metric name, authority/version, units, datum and exact
measurement faces before calculating. Keep these three questions separate:

| Quantity | Boundary to establish | What cannot be inferred |
| --- | --- | --- |
| Geometric external envelope | Actual selected outer faces, base and roof surfaces, enclosed versus open parts | Neither usable room air nor a statutory total follows from this solid |
| Space/air volume | Finished room faces, soffits, actual internal obstructions, relevant openings and connected spaces | External walls, roof voids, slabs and shafts are not all usable room air; geometric air volume alone does not size ventilation |
| Formally defined building volume | Applicable purpose/jurisdiction/source, edition, above/below datum, inclusions and exceptions | A familiar label, BIM property or textbook rule is not the applicable measurement instruction |

For a formal result, read the selected provision through
[requirements](../requirements.md#primary-normative-sources); for a confirmed
Russian public building follow the [СП118 owner](../normative/ru/building-typologies.md#sp-118-13330-2022)
and its current primary text. This method supplies no unseen clause or numeric
exception. If that evidence is unavailable, report a named geometric subtotal
and leave the formal figure unresolved. Do not rename it as compliant volume.

List treatment of attics, open courts, double-height rooms, balconies/canopies,
plant enclosures, external stairs, projections, recesses and below-ground parts.
Use the actual definition for each; no universal inclusion list is assumed.
Thermal/conditioned boundaries may follow a ceiling rather than the outer roof.
An internal floor void can change floor area without removing outer envelope;
an open-to-sky notch changes the solid itself. Changing the reporting datum can
reclassify an unchanged solid without changing its total.

## Construct mutually exclusive solids

1. Freeze coordinated plan, section and elevation dimensions in metres. State
   whether faces include finishes, slabs and roof build-up; a roof's outer top
   and a room soffit are different surfaces. Unknown build-up is unresolved.
2. Partition at changes of footprint, base, roof slope, height and exclusion.
   Give each piece an ID and coordinate footprint, bottom/top functions and
   metric role. Interiors of added solids must be disjoint. Touching at a face
   adds no volume. If starting from overlapping masses, partition or explicitly
   subtract their intersection, not just a shared line on the plan.
3. For a constant-height prism use V=A×h. A constant-width wing with a planar
   single slope uses footprint×(end height1+end height2)/2. A gable cap with
   triangular section uses span×rise/2×ridge length. These averages require
   the declared linear section; two endpoint heights do not determine a curved
   or stepped roof. For a planar height over a triangular footprint, its mean
   is the three vertex heights divided by3. Triangulate without overlap.
4. More generally integrate actual sectional area: V=integral A(z) dz, or
   integrate top minus bottom over the plan. Split at all geometry changes;
   subtract a court through its actual varying height, not at one convenient
   storey height. Clip a sloping grade against the solids before reporting an
   above/below split. A bounding box is only a bound, not measured volume.
5. Sum signed components once. Reconcile an independent section/slice construction
   with the piece ledger and the actual plan/elevations. Show units and rounding
   after reconciliation. A mesh/software total needs its closed, correctly
   oriented surfaces, exclusions and tolerance checked against those boundaries.

Repeat occupied headroom, roof/drainage/support and site checks when geometry
changes; volume conservation does not preserve spatial usefulness. A tall room
does not gain another floor merely because its height equals two floor intervals.

## Prism and clear-space counterexample

An original hypothetical external prism x0…10,y0…8,z0…6 is480m³. A mezzanine
inside it does not change that outer volume. Deleting the mezzanine changes
floor area but retains480m³; summing only its remaining80m² floor×3m would
incorrectly report240m³. A changed6.5m outer height instead gives520m³.

If a separate clear-space study explicitly gives finished inside faces
x0.2…9.8,y0.2…7.8,z0.25…5.75 with no other internal obstruction, that space
is9.6×7.6×5.5=401.28m³. Do not apply this ratio to another building or deduct
its shell again from the already internal boundary. Actual internal floors,
equipment and service/ceiling zones need their own assigned treatment.

## Mixed roof, wing, basement and open court

This independent study selects the external geometric envelope, includes its
declared outer build-up within the coordinates and splits at z0. It excludes
an open-to-sky court above z0, but retains a basement beneath its lid at z0.
No roof/parapet/canopy beyond the listed faces is supplied or credited.

| Piece | Coordinates / selected section | Signed volume m³ |
| --- | --- | ---: |
| Main body M | x0…12,y0…8,z0…6 | +576 |
| Gable over M | eaves z6 at y0/8, ridge z8 at y4, length12 | +96 |
| Wing W | x12…18,y0…8, base0, outer roof rises linearly z4→6 from x12→18 | +240 |
| Basement B | x0…12,y0…8,z−3…0, including beneath court | +288 |
| Open court C | x4…8,y2…6, from z0 through M's actual roof | −120 |

M and W share only x12, not volume; B touches the above-ground pieces at z0.
The main roof is z_top(y)=8−0.5×abs(y−4). Over the court its average is7.5m,
so subtract16×7.5=120, not16×6 or16×8. Above0 is576+96+240−120=792;
below0 is288; **total1080m³**. The18×8×11 bounding box is1584, overstating
the selected solid by504. A single average building height hides those causes.

An independent horizontal-slice check gives main remaining body80×6=480;
main roof bands z6…7 and7…8 contribute56 and16. Wing bands z0…4 and4…6
contribute192 and48. Thus480+56+16+192+48=792 above0 again. For the first
roof band let t=z−6: area=80−48t,0≤t≤1; for the second it is64−32t,1≤t≤2.
The wing upper band's area is48−24(z−4). These functions come from the actual
intersected footprints, including the court, not a second copy of the ledger.

## Change the height or boundary

Change one input at a time unless a combined option is explicitly selected:

- Raise M's ridge8→9 with eaves unchanged. The whole cap gains48m³, but the
  open court exclusion also gains12. Net gain36: above828, below288, total1116.
  Retest structure, roof/build-up, outer form, shadow and occupied height.
- Lower only B's base−3→−3.5. Its96m² footprint gains48: total1128. Reopen
  excavation, water/support, access and services; do not count that increase
  as additional occupied floor area.
- Enclose the court flush to the originally defined roof faces. Restore120
  to the selected outer envelope: total1200, even if no intermediate floors
  are added. Its daylight/air/fire/thermal and drainage conditions change.
- Report the unchanged original solid above/below horizontal z0.5 instead of0.
  The128m² included plate between0 and0.5 reclassifies64: above728, below352,
  total1080. This is a reporting-plane experiment, not a legal basement test.

## Evidence and related decisions

[Source selection and read limits](../../sources/volume-and-exhibition.md) record
the primary mathematical check and the unselected formal-definition boundary.
Coordinates, partitions, examples and checks here are original synthesis.

- Requires — [Area ledger](area-ledger.md): keep floor, clear-room, ground and volume quantities distinct; use the same actual geometry without converting one metric implicitly.
- Verified by — [Floors, tall rooms and roofs](../space/planning/room-floor-and-section.md#reconcile-upper-floors-tall-rooms-and-roofs): reconcile floor edges, voids, roof underside and actual occupied headroom.
- Affects — [Roof and span](../construction/structure/roof-and-span.md#choose-where-the-thermal-boundary-follows-the-roof): a changed outer roof/conditioned boundary reopens support, build-up, water and maintenance, even when the arithmetic closes.
- Affects — [Ground and basement](../construction/structure/ground-and-basement.md#decide-what-actually-needs-to-be-below-ground): changed lower bounds need the actual ground/water/access proposal.
- Affects — [Multi-building sun](../performance/comfort/multi-building-sun.md): changed enclosing solids can change actual neighbor occlusion; equal volume does not preserve shadows.
