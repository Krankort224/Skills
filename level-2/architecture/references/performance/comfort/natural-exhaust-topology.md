# Architectural topology of natural exhaust

Use this method to reserve a complete intended air path and reject broken or
incompatible connections before fixing housing/section/roof geometry. It adds
duct/room/level topology to [air-mode choice](acoustics-and-air.md), not engineering
airflow sizing. A connected graph is necessary for a proposed route; it does not
establish the pressure, flow, pollutant removal, fire or acoustic performance.

## Contents

- [Select the strategy and its boundaries](#select-the-strategy-and-its-boundaries)
- [Construct supply, transfer and extract chains](#construct-supply-transfer-and-extract-chains)
- [Separate paths and test possible reversals](#separate-paths-and-test-possible-reversals)
- [Reserve shafts, top-floor and roof interfaces](#reserve-shafts-top-floor-and-roof-interfaces)
- [Worked two-floor housing chain](#worked-two-floor-housing-chain)
- [Broken transfer, cross-connection and changed floor count](#broken-transfer-cross-connection-and-changed-floor-count)
- [Evidence and related decisions](#evidence-and-related-decisions)

## Select the strategy and its boundaries

Record actual dwelling/room IDs, floor and roof levels, occupancy/operation,
window/door states, outdoor intake/exhaust positions, air-quality/noise/security
conditions, selected system and authority. Distinguish a purely natural stack,
intermittent local fan, continuous mechanical extract, balanced supply/extract
and a mixed alternative. A fan-assisted branch cannot be silently added to a
natural common duct. Natural ventilation is driven by available pressure, not
by the word shaft on a plan; it can weaken or reverse with temperature and wind.

The worked strategy below uses independent passive extract ducts for each
dwelling/room and deliberately avoids inter-dwelling common air ducts. This is
one bounded architectural concept, not a universal prohibition of engineered
shared systems or a claim of compliance with an Approved Document scheme.
Shared collectors, assisted/hybrid stacks or proprietary systems require their
actual system/control/separation and flow evidence before adopting their topology.
House-specific and apartment-block requirements must be selected separately.

Maintain distinct functional paths:

| Path | Architectural commitment / potential failure |
| --- | --- |
| Dwelling general ventilation | Outdoor air reaches occupied rooms, transfers through the dwelling and leaves selected extract rooms; a closed bedroom door or sealed replacement window can break it. |
| Shared lobby/corridor/other communal use | Its own supply/extract/strategy; never assume the protected core is the apartment's transfer duct or that a flat's shaft ventilates the whole building. |
| Cooker hood | A recirculating hood returns air to the kitchen, not outside. An extract hood needs its own actual discharge/system coordination; do not connect its fan/grease path into the natural network by assumption. |
| Garage/service pollution | Separate collection, discharge and intake/compartment interfaces; do not use a residential transfer path or shared return cavity for vehicle fumes. |
| Combustion appliance/flue | Dedicated combustion-air/flue evidence and actual appliance strategy; a ventilation duct is not a chimney and an exhaust fan can change spillage risk even in another room. |

## Construct supply, transfer and extract chains

1. For each occupied room draw outdoor source→actual inlet→occupied room→transfer
   opening/device→internal route→extract room→grille/branch→identified duct→roof
   terminal→outside. Use actual port/door/duct IDs and levels. Outdoor air supplied
   only beside an extract can bypass bedrooms. A room with neither a supply path
   nor an intended downstream path is unresolved even if its window is labelled.
2. Test closed internal doors in the occupied state, not only an open-plan diagram.
   Identify the actual transfer device and free path. Preserve privacy/noise,
   fire/smoke and security functions; do not prescribe an undercut or grille as
   a generic fix to a protected door. Reserve a compatible tested device/path
   with its actual authority/product evidence, or change the operating strategy.
3. Place extract terminals near the pollutant/moisture source without a supplied
   inlet short-circuit; trace each branch to its actual channel. Annotate horizontal
   legs, bends, lining/insulation, openings/supports, condensation/cleaning and
   ceiling depth using [section/services](../../space/vertical/section-and-services.md).
   A line crossing a beam, sealed wall or another home is not an established edge.
4. Make a directed intended-flow graph and trace every required occupied room
   to its own permitted extract/roof destination in every required operating state.
   A node/edge needs a real geometric component and state; a graph edge alone
   cannot create an opening. Record missing physical inputs as unknown, not pass.
5. Retain two separate results: topological continuity and physical/technical
   sufficiency. A complete path still needs engineering pressure/loss/flow,
   terminal/control, fire/acoustic, source-air and actual operation verification.
   A numerical flow result for one room cannot repair another disconnected room.

## Separate paths and test possible reversals

Give every channel an owner, served room/floor, connection list and outlet.
An enclosing shaft can contain several sealed ducts; it is not itself a common
air plenum. Draw the actual partitions/connections and access/penetration
interfaces. Two grille labels on one undivided rectangle do not give independent
paths. Conversely two independent ducts can share a geometric enclosure without
being the same air route; retain their separate occupied space and maintenance.

For the independent-duct strategy, remove outdoor boundary nodes and examine
the **potential bidirectional** interior connection graph as well as the intended
arrows. If one connected air component contains different dwellings, communal
or garage/combustion paths, investigate/reject that unintended join. Ordinary
upward arrows can hide transfer during wind, fan operation or flow reversal.
Do not connect all outside terminals into one generic graph node for this
interior-isolation check: outdoor plume recapture is a separate geometry/air-
quality question. A graph with separated ducts does not prove separated roof
plumes or compliant fire/acoustic construction.

For a proposed shared collector, explicitly replace the independent strategy's
test with the real system's permitted connections, reverse-flow controls,
compartmentation, cleaning and fault-state evidence. Do not infer compliance
from a check valve symbol or assume every floor can join a common duct at the
same point. Identify a missing system decision rather than inventing a collector
detail, satellite-duct height or one-size separation rule.

## Reserve shafts, top-floor and roof interfaces

Overlay plans through every served floor, any bypassed dwelling, ceiling/roof
void and outlet. Keep the same channel ID and actual clear/enclosing dimensions;
deduct enclosing walls, insulation, separation, access and supports explicitly.
At a moved wet room, trace its horizontal branch and any new floor opening.
Do not shift a top-floor shaft without reconnecting the stack below it. Track
inspection/replacement routes, who grants access and which private space is
entered; removing a duct through a bedroom is an architectural consequence.

Draw top-floor extract height and the actual terminal height separately from
the roof/parapet. Its shorter column can have much less buoyancy drive than
the same duct below. For a simple diagnostic of uniform columns,
Δp_stack=gH(ρ_out−ρ_in), before branch/terminal losses and wind. It follows
from the difference of hydrostatic air-column pressures, not a flow-sizing
equation. Add signed inlet-minus-outlet wind pressure only when supplied for
that scenario. H, density and pressure assumptions are not design defaults;
zero/negative or small available drive must not be relabelled as adequate flow.

At roof level coordinate outlets with actual openings/intakes, neighboring mass,
wind exposure, weather/condensation, parapets, drainage/waterproofing, support
and access for inspection/cleaning/replacement. Roof cowls, terminal height and
separation need actual project/system evidence; this method supplies no universal
height or distance. Higher outlets can change roof structure, silhouette and
maintenance. If natural operation cannot meet the required occupied states,
compare an actually designed alternative mode and its plant/duct/control space.

## Worked two-floor housing chain

Original hypothetical continuation of the [section variant unit](../../typologies/housing/section-variants.md#common-fitted-unit-and-regular-section),
not a sized ventilation installation. Two units A/B on FF0 and+3.00 give four
dwelling owners A1/B1/A2/B2. Each has living, bedrooms1/2, hall, kitchen and bath.
The utility is dry service/storage here, not a clothes-drying room; if its use
changes, re-establish extract demand. Roof is+6.00, nominal terminals+7.50,
and kitchen/bath branch inlets+2.50/+5.50. These are supplied study levels.

For every owner h use the intended chains:

`outside:h:inlet → h:living/bed1/bed2 → h:hall → h:kitchen/bath
→ h:extract-K/B → h:branch-K/B → h:duct-K/B → h:roof-K/B → outside:h:out-K/B`.

The slash notation denotes distinct room/branch nodes, not a combined duct.
Each occupied room has its own outdoor inlet and a closed-door transfer to hall.
The hall has transfer to both wet rooms. Each wet room has its own extract,
continuous dedicated duct and roof terminal. Apartment doors to the common core
are closed and are **not** supply/transfer edges. The cooker hood is recirculating
in this example; kitchen general extract remains independently present. Garage,
communal and combustion paths do not join these ducts.

In each unit's1.05 m square shaft enclosure u7.8…8.85,v9.7…10.75 reserve:

| Dedicated channel | u interval | v interval | Intended served room |
| --- | --- | --- | --- |
| Lower-floor K | 8…8.25 | 9.9…10.15 | A1 or B1 kitchen |
| Lower-floor B | 8.4…8.65 | 9.9…10.15 | A1 or B1 bath |
| Upper-floor K | 8…8.25 | 10.3…10.55 | A2 or B2 kitchen |
| Upper-floor B | 8.4…8.65 | 10.3…10.55 | A2 or B2 bath |

These are hypothetical **outside** channel envelopes, with0.15 m between them
and0.20 m perimeter reserve. They are not free air areas, required fire thicknesses
or selected duct sizes. Their outer dimensions must be replaced by actual sized/
constructed channel evidence before fixing the enclosure. No path terminates
inside the surrounding shaft void or opens into the upstairs dwelling it passes.
At each floor the enclosure consumes1.1025 m² of utility, counted once; four
channels do not each claim the same square metre.

Example kitchen branch begins near(u6.8,v9.9), crosses its actual wall at
u7.4…7.6 and continues to the assigned channel at the ceiling reservation;
bath branch reaches the corresponding channel through its north interface.
The actual floor's owner determines the correct channel, not the nearest grille.
Reserve the branch elbows/openings and the required lining/section; they are
not automatically approved penetrations. Utility access is via the kitchen's
0.80 m approach and the portal v10.85…11.75, north of the shaft; its east
service strip remains0.95 m. This requires access within the dwelling. Actual
tool/component reach, cleaning method and compartment details remain checked inputs.

Transform channels and branches with the whole unit in regular/turning/end
variants, and repeat that chosen location across floors. For T's B the lower
kitchen-channel centre moves from(17.475,10.025) to(20.025,−1.875); both roof
and below-floor continuity must follow. Its old terminal is not a new connection.

For a deliberately simplified pressure diagnostic, supply ρ_out=1.25,
ρ_in=1.20 kg/m³ and g=9.81 m/s². Lower inlet-to-outlet height5.0 m gives
2.4525 Pa; upper height2.0 m gives0.981 Pa. No flow or adequacy follows from
either value. A supplied adverse wind difference−3 Pa would make these
−0.5475 and−2.019 Pa respectively before losses: intended upward flow cannot
be assumed, despite a complete graph. Warm-outside/equal-temperature cases,
closed inlets and added fans require their own operating check.

## Broken transfer, cross-connection and changed floor count

Close A2's bedroom2 door in a proposal with no actual transfer provision.
Delete bed2→hall: that room's path ends there although the extract shaft still
reaches the roof. Correction reserves a compatible transfer route/device within
the dwelling, with its actual free-area, acoustic and any fire requirements,
or changes the strategy. Restoring the **physically supported** edge recovers
topological continuity only; an arbitrary grille/door cut is not an approval.
For a geometric candidate where this internal bedroom partition is expressly
non-compartmenting, reserve a continuous sleeve u1…1.25,v7…7.2,
z=FF+2.2…FF+2.35 (A2:5.2…5.35)
between bedroom2 and hall, with both faces open in the tested state. It clears
the floor furniture and supplies a real proposed edge through the0.20 m wall.
Its0.0375 m² geometric opening is not a selected equivalent free area or proven
flow; acoustic/security/control and actual product/authority checks can require
a different/larger path. Do not transfer it to a rated door/wall by analogy.

A wrong connector joining A1's bath duct to B2's branch creates an interior
component containing both homes, visible in the potential-return graph even if
both drawing arrows point up. Remove that connector and retain their separate
continuous ducts, or deliberately select and verify a different shared system.
A shaft enclosure without actual channel separation fails this test as a common
plenum; do not certify it by retaining four labels.

Changed input: a third occupied floor adds two more dedicated channels per unit.
The former2×2 arrangement has four slots, but six are needed. At the same
0.25 m outside size,0.15 m gaps and0.20 m perimeter reserve, a2×3 arrangement
needs1.05×1.45 m. Extending it north from v9.7 to11.15 intersects the former
utility door/action band v10.85…11.75. Rotating to3×2 inside the old utility
would extend east to u9.25, reducing the east service strip to0.55 m<the supplied
0.80 m approach. Both casual area-only fixes fail. Refit/enlarge the actual
utility/shaft and kitchen/door/branch arrangement, choose another established
system, or retain the lower floor count when authorized. Do not shrink a channel
or delete maintenance to claim six fit. Reconcile dwelling area, support/roof and
the top floor's shorter drive after the chosen correction.

One explicit **geometric** third-floor correction is available if its additional
floor/roof and nonbearing-partition changes are authorized. Keep the old four
channel axes and add a third pair in a row to their south; use enclosure
u7.8…8.85,v9.3…10.75. Three row starts v9.5,9.9,10.3 with two0.25 m channels
per row fit its1.05×1.45 boundary. Move the bath/utility partition to
v9.02…9.22: bathroom becomes2.2×1.82=4.004 m²≥the supplied4, utility becomes
2.2×2.58=5.676. The utility's old north portal and east0.95 m approach survive.
The enclosure consumes1.5225 m²,0.42 more than before, leaving4.1535 m² of
utility floor; the repeated unit ledger must deduct that actual shaft area.

The former bathroom solids no longer fit. Refit a walk-in shower at
u8.7…9.6,v8.1…9.0, WC u7.8…8.4,v8.3…9.0 and basin
u9.3…9.8,v7.25…7.75. Replace the inward door with a0.90 m sliding portal
u7.85…8.75 and pocket u8.75…9.65 within v7…7.2. Supplied trial standing
zones WC u7.8…8.4,v7.5…8.3 and shower u8.65…9.25,v7.3…8.1 clear the
other fixtures; no hinged leaf spends that space. This is a coordinate-fit
correction, not accessibility, drainage, waterproofing or product approval.
Recheck kitchen/bath ceiling branches to the actual assigned channels and every
new opening/support. If the third floor moves roof6→9 and outlets7.5→10.5,
its inlet8.5 still has only2 m column while the lower inlet2.5 now has8 m:
graph continuity and more height below do not prove top-floor performance.

## Evidence and related decisions

[Primary source records](../../../sources/housing-and-exhaust.md) distinguish
the selected PSV definition, dwelling supply/transfer/extract, hood and
fire/combustion/maintenance interfaces from jurisdiction-specific prescriptions.
The graph, coordinates, channel/pressure examples and tests are original
synthesis. No current code dimension or engineering performance is supplied.

- Requires — [Actual demand](../../program/demand.md): when room use, occupant/state or system choice changes, update the required paths rather than reuse a label.
- Requires — [Air-mode and acoustic paths](acoustics-and-air.md): choose a credible occupied mode and retain noise/privacy and alternative-air consequences.
- Verified by — [Section/services](../../space/vertical/section-and-services.md#budget-the-section-and-routes): changed branches/shafts must fit support, wall/ceiling and actual removal routes.
- Affects — [Housing section variants](../../typologies/housing/section-variants.md#carry-wet-rooms-shafts-and-ground-through-levels): more channels or moved wet rooms can consume dwelling/core space, change openings and force a new plan/section ledger.
- Affects — [Roof/enclosure](../../construction/structure/roof-and-span.md): changed outlets require actual support, water/thermal continuity, exposure and safe maintenance interfaces.
- Requires — [Requirements](../../requirements.md): for actual ventilation, common-duct, fire/acoustic, combustion, terminal or accessibility conclusions select the project jurisdiction/version and system evidence.
