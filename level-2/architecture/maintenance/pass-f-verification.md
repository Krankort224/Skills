# Pass F: cross-author transfer and final verification

Status: **in progress**, not accepted. Method target is accepted E
`2e5515ad960da98bdafefe72f52ade2efc24d580`; acceptance-only recording commit
`6f6bde9e14ffcf4becbd920fe7026fcc7c136e1d` changes no method.
[Issue13](https://github.com/Krankort224/Skills/issues/13) owns the contract;
[E acceptance](https://github.com/Krankort224/Skills/issues/13#issuecomment-6729101605)
and [F dispatch](https://github.com/Krankort224/Skills/issues/13#issuecomment-6729162661)
own authorization/roles. Dot arbitrates. This maintenance evidence is not a
runtime index, whole-project design or automatic coverage score.

## Contents

- [Authorship and actual independence](#authorship-and-actual-independence)
- [Session1 vehicle and territorial allocation](#session1-vehicle-and-territorial-allocation)
- [Session1 original D mechanisms](#session1-original-d-mechanisms)
- [Session1 volume and exhibition](#session1-volume-and-exhibition)
- [Coursework matrix worklist](#coursework-matrix-worklist)
- [Remaining evaluation and checks](#remaining-evaluation-and-checks)

## Authorship and actual independence

| Method contribution | Substantive author | Permissible transfer evidence |
| --- | --- | --- |
| A navigation; C sun geometry | Session1 | Session2 checks raw new sun tasks and records six navigation walks. |
| B vehicle/service allocation; E volume/exhibition | Session2 | Session1 new F-V/F-T/F-Q/F-X cases below. |
| Original D air topology, rigid transforms and local end-unit refit | Session2 | Session1 F-A/F-S: only unchanged original mechanisms; its edited global R channel coordinate and ground/core are supplied context, not independently certified here. |
| D widened ground/core correction, thresholds, section and its ledgers | Session1 | Session2 F-D-ground. Its original unit/air knowledge is fixed context, not independently certified by its author. |

No new sessions/agents were created. The two existing sessions have already
read/reviewed much of the corpus. These are cross-author changed-input tests,
not a cold-context or blinded user study. Session1 selected its new inputs;
Session2 receives only [raw tasks](pass-f-session-2-tasks.md), not expected
results. Both must disclose inherited familiarity and any authored interface.
Current B/D/E navigation additions have shared authorship: actual route walks
are usability observations; do not label an observer's own selector independent.
The complete D document has no wholly uninvolved third reviewer in this mode.

Session1's one-off standard-library checker is outside the repository at
`/tmp/issue13-F-session1.py`; command:
`PYTHONDONTWRITEBYTECODE=1 python3 /tmp/issue13-F-session1.py`.
It imports no authored skill test helpers. The inputs, calculations and limits
below allow independent reconstruction; the Issue checkpoint records exact
revision/command results. No one-off log/script is installed as a runtime tool.

## Session1 vehicle and territorial allocation

### F-V: changed vehicle, angle, entry and land

Owner used: [vehicle geometry](../references/context/urban/vehicle-and-parking-geometry.md).
Supplied rigid low-speed vehicle: L3.05/front1.05/rear1.20/width2.05m;
rear-axle R4.80; maximum effective steer34 degrees; required clearance0.22.
Approach east at rear axle(x_j−4.8,8.7), turn left90 degrees then move north0.8
so final axle is(x_j,14.3). Adjacent upper bodies span y13.1…18.4, lower bodies
0.3…5.6. Test upper neighbours at x_j±pitch and the lower row. Bays are5.9m
deep with6.9m aisle; through aprons6m at both ends. Test pitches3.45/3.80,
eight bays in each row. All values are study inputs, not parking standards.

Independent vertex/segment polygon distances give minimum separation0.101754704
at3.45 (fails0.22) and0.451754704 at3.80. With1800 curve intervals,
`epsilon=(R+rho)*pi/(2*1800)=0.007876831`, so the corrected continuous lower
bound is0.443877874>0.22. Required steering32.432557 degrees fits34;31 does
not admit this path. All sampled corner coordinates with that bound fit the
module/end aprons; the final straight translation is checked separately.
This validates the declared route, not every possible route or real operation.

Entry clear interval y7.4…10 contains the straight body with0.275m edge margins;
changing it to7.8…10.4 obstructs its lower edge y7.675. A proposed canopy column
x11.2…11.6,y8.3…8.8 intersects the exact straight extrusion. An expressly
permitted unroofed alternative removes that proposed canopy/column; retaining
it requires another actual route. Reducing the stall count alone does not fix it.

Reserved module land changes740.52→792.88m², +52.36. As a **separate** angled
rectangle construction (not the tested90-degree driving path), l5.9/b3.2,
angle55 degrees in30m yields actual row spans29.444260 for seven bays and
33.350738 for eight: seven fit, eight do not. Angled rows still need their own
vehicle movement/aisle/end check.

### F-T: new service graph, gate, whole groups and parcel

Owner used: [allocation](../references/context/urban/service-capacity-allocation.md).
One service/cohort/phase; supplied demands A27/B24/C21/D18/E15. Available places
X40=(46−6 outside), Y35=(43−8), Z35=(40−5), each reservation counted once.
Initially A/B reach only X; C only Y; D Y/Z; E only Z. Total110 exceeds105,
but subset A+B requires51 against X40:11-place deficit. An integer augmenting
flow construction confirms only94 can be assigned.

A newly available, admitted route B→Y has complete declared segments
70+260+90+40=460m under the supplied500m condition; its gate/crossing/phase
are assumed established for this hypothetical case. A full allocation becomes:

| Group | X | Y | Z | Total |
| --- | ---: | ---: | ---: | ---: |
| A | 27 | 0 | 0 | 27 |
| B | 13 | 11 | 0 | 24 |
| C | 0 | 21 | 0 | 21 |
| D | 0 | 3 | 15 | 18 |
| E | 0 | 0 | 15 | 15 |
| Used | 40 | 35 | 30 | 105 |

Closing that real gate removes the edge and restores the11 deficit. If whole
residential groups must remain indivisible, exhaustive eligible assignments
remain infeasible: A forces B off X, but B24+C21 then exceed Y35. A split flow
is not that operating policy's proof. Without the new edge, fixed A27 leaves13
for B; under the separately supplied rate ceil(0.075 P_B), maximum P_B=173
(174 needs14). Reducing demand must also revise housing/parking, not only a table.

A100×70m parcel can contain the supplied40×25 building x5…45,y5…30 and
45×30 clear field x50…95,y5…35. An equal-area20×350 parcel cannot contain that
field even after rotation (minimum projected width30>20). This is shape evidence,
not a facility capacity or complete servicing approval. In a20000m² quarter,
6000 building+7000 facility+4200 parking+2800 remaining ground closes. A150m²
new bypass leaves2650 remaining. Applying F-V's additional52.36 in the same
ledger makes parking4252.36/remaining2597.64; sum stays20000. No seat capacity
is inferred from these areas.

## Session1 original D mechanisms

### F-A: missing supply, communal join, more channels and top floor

Owner used: [air topology](../references/performance/comfort/natural-exhaust-topology.md).
Six homes A1…A3/B1…B3 each have independent kitchen/bath ducts, three occupied
rooms, hall and actual outside endpoints. Put B3's inlet only into its hall,
removing its bedroom1 supply while leaving bed1→hall→extract→outside.
Directed reachability rejects the outside-to-bedroom chain despite its intact
exhaust path. Proposed correction reserves an exterior inlet u8.8…9.1,v0…0.2,
z=FF+2…FF+2.2 in that bedroom, clear of its supplied window u6.3…7.5. This
geometric opening is not selected free area, flow or approved wall construction.

A wrong A2 bath-duct→communal-core connection joins different functional owners
in the potential bidirectional graph after outdoor boundaries are removed.
Removing that actual connector restores the selected independent strategy's
isolation. Outside plume recapture and engineered shared systems remain separate.

Fresh outside channel0.30m, gap0.12 and perimeter0.18 give a six-channel2×3
enclosure1.08×1.50. At u7.8…8.88,v9.25…10.75 it stays inside the accepted
third-floor utility, leaves0.92m east strip and the north door at10.85 clear;
channel starts u7.98/8.40 and v9.43/9.85/10.27. Its1.62m² deduction is0.0975
more than the former six-channel enclosure, leaving4.056m² utility. These are
outside envelopes, not fire separations or duct sizing.

With terminal9.6, inlet2.4/8.4, densities1.24/1.19, g9.81 and signed wind−1Pa,
available ideal static pressure is+2.5316 below and−0.4114 at top, before losses.
Even repaired topology and a fitted shaft do not prove upward top-floor flow.
No part of this test independently passes Session1's ground/core correction.

### F-S: original rigid transform and local thicker end unit

Owner used: [original section procedure](../references/typologies/housing/section-variants.md).
Treat the accepted global unit/core coordinates as fixed supplied input; the
independent target is Session2's unchanged transform and local end-room method.
Rotate R's B clockwise120 degrees about(15.6,6), retaining the core. Exact
polygon clipping gives19.756016m² overlap with A and42.464529 with core. Portal
endpoints become approximately(15.210289,6.225)/(15.989711,5.775): no whole
portal shares an orthogonal core boundary. That rigid proposal fails; this is
not proof that no redesigned120-degree housing group can exist.

For a separately changed end wall0.72m, the unchanged living room is23.368<24.
A permitted0.15m nonbearing living/bedroom1 partition shift gives living24.058,
bedroom1 16.790 and bedroom2 16.008m², preserving supplied minima. Bed2 at
u1.35…2.95 retains0.60 side actions u0.75…1.35/u2.95…3.55 and foot action
v7.6…8.2; wardrobe u0.75…3.95 retains its original v/action extents. Separate
foot/side actions clear the original door sweep u3…3.9,v7.2…8.1; bedroom1 and
living furniture/door coordinates remain inside their changed rooms. The ledger
is98.496 clear+14.672 perimeter+6.832 partitions=120; after shaft97.3935.
The global ground correction is not certified by its own author through this
local calculation. The coursework's actual3–4 flats/core, selected program,
site and roof/ground obligations are not completed by a two-household study.

## Session1 volume and exhibition

### F-Q: another asymmetric roof/court/wing/basement

Owner used: [volume](../references/program/building-volume.md). Supplied external
geometric solid: main x0…10,y0…8, base0,eaves5,ridge7 at y3; planar slopes to
eaves y0/8. Wing x10…15,y0…8, base0, roof3→6 along x. Basement under the whole
main footprint z−2.4…0, including under court. Court x2…5,y1…5 is open above0.
No extra projection or legal inclusion is assumed.

Independent exact signed-tetrahedron sums over outward-oriented planar faces
give main480+wing180−court77.6+basement192=774.4m³; above582.4/below192.
Ridge7→8 gives805.6; basement base−2.9 gives814.4; equal-area court y0…4
gives777.6. Report plane+0.6 gives517.6/256.8, total774.4. A separately selected
boundary following a z5 ceiling over the main body instead of its outer roof
gives712, not finished air volume or a statutory quantity. Changing a measurement
boundary is not an energy/ventilation or legal result.

### F-X: new collection, sightline, operating light and large replacement

Owner used: [exhibition](../references/typologies/exhibition.md), without a
coursework appendix. New hypothetical brief: fragile horizontal model plus a
robust indoor machine and bright interpretation. Supplied model top0.95,
front detail at(3,7.2), eyes at(3,5.5), z1.15/1.60; opaque front rim y6.7 rises
to1.30. Actual sightlines at the rim are1.008824/1.141176: both blocked.
A permitted lower opaque edge0.95 with no opaque upper rail clears these rays;
glazing/reflection, other details and sensory usability still need evidence.
Offer an identified reproduction/description, not a silently substituted original.

New lender inputs: instantaneous35lux, viewing30lux, episode36×24=864h,
budget9000lux-hours, separately permitted preparation12h×75lux=900. Eight hours
view/day gives10692 (fails); six gives8676. Closed leakage2→5lux changes six
hours to10620; maximum151.2 viewing hours permits4.2h/day, and4h/day gives8820.
An intense100lux local patch violates the35 cap regardless of short exposure.
These results select a separately controllable opaque original room and actual
object-plane spill/closed/fault verification while the robust hall/spine remain
open. They do not predict fading or establish those actual illuminances.

Fresh layout: outer14×10m, clear ceiling5.5, south spine y0.2…2; G west of
x6…6.2 partition, H x6.2…13.8,y2…9.8. Main south entrance x6.2…7.8 crosses
y0…0.2, with a separately assumed12m² approach x6…8,y−6…0. G's sliding
portal x2.4…3.6 crosses partition y2…2.2. Original robust load's complete handler
3.0×3.4m,height3.5 traverses east x14 portal y3…6.8,height3.6, from(16,5) to
(10,5): sweep x8.5…17.5,y3.3…6.7. Apron x14…18,y2.8…7 is16.8m².

Changed body3.2×3.0×3.9 has complete handler3.6×4.2,height4.1. Original portal
fails width/height. A permitted opening y2.7…7.2,height4.3 and apron
x14…18.5,y2.5…7.4 (22.05m²) allow translation(16,4.95)→(10,4.95): sweep
x8.2…17.8,y2.85…7.05. Additional service land5.25m² is explicit; spine is
clear. Close H's entire south opening/receiving portal and dispatch the old load
before the new arrival. Brighter interpretation bay x6.5…8,y7.5…9.2 stays out
of this sweep; its path and safe lighting need the actual occupied-state checks.

For the supplied overview intent≤60 degrees horizontal/≤45 upward (not a
standard), old centre(10,8.5) fails. Move to(10,9.3), field x9.5…10.5,
y8.8…9.8. Distance to body face6.45 is2.85m: span58.620014, upward
43.976970/38.904138 at eyes1.15/1.60. This is nominal point geometry, not
crowd visibility, ergonomic acceptance, actual handling or a construction design.
If an earlier30-degree upward target is retained instead, the seated eye needs
4.763140m while the fixed layout offers2.85: report that incompatibility rather
than treating the separately supplied45-degree intent as an authorized relaxation.
Rational interval-union coverage additionally verifies both complete handling
sweeps and14 continuous1m square-probe public segments to the model and both
overview positions, through the actual entrance/G portal. The selected public
paths avoid the changed machine body. H replacement closure remains a separate
operating state from these display-time paths; the spine/G approach stays outside
the handling sweep. Probe size is a supplied diagnostic, not an access standard.

## Coursework matrix worklist

The [historical35 rows](coverage-and-verification.md#historical-35-row-benchmark)
remain immutable dated judgments. Actual brief identities and selective reading
remain at [source identity](coverage-and-verification.md#source-identity-and-inspected-extent).
All seven cached files were SHA256-recomputed and matched the primary pinned
migration manifest again; F re-read principal KP1–KP4 requirement text, including
KP4's roof/ground/3–4-flat/natural-duct clauses. Graphic-only source pages were
not newly inspected. No coursework or normative source is edited or imported.

This is a worklist, **not the final current-coverage matrix**. Proposed changes
need the other session's sun/ground/navigation report, the original whole-row
scope and final regression consolidation. Unknown project inputs and unrun
models remain separate from local-method coverage. KP5 remains excluded.

| Row | Historical | Actual F evidence available / remaining consolidation |
| --- | --- | --- |
| P1 | Sufficient | Original demand/area owner preserved; retain its supplied-input scope in final audit. |
| P2 | Sufficient | Site/approach/seasonal owners preserved; actual park/site remains an input. |
| P3 | Partial | F-V new vehicle/entry/row/land evidence; separate real fire/operation inputs and broader route scope. |
| P4 | Sufficient | F-X replacement and closure supplement the preserved object/handler/access chain; whole project logistics unbuilt. |
| P5 | Sufficient | Lift/core/section owners preserved; N1 route pending, actual supplier/egress evidence still separate. |
| P6 | Sufficient | Massing/roof/support owners preserved; no member-sizing claim. |
| P7 | Sufficient | F-X new model ray, overview, alternative representation and changed layout; inspect original viewing scope. |
| P8 | Sufficient with independence caveat | F-X independently selects collection control from new inputs without the appendix; historic caveat remains historical. Actual lighting unmeasured. |
| P9 | Sufficient | Documentation/view/issue owners preserved; no new coursework album rendered. |
| P10 | Partial | F-Q new metric/roof/court/basement changes; formal measurement authority remains an actual project input. |
| D1 | Sufficient | Household/site/demand owners preserved; actual household and chosen site still needed. |
| D2 | Sufficient | Occupied-use owners preserved; F-S furniture actions are supplemental, not a full new house. |
| D3 | Sufficient | Stair/section/attic owners preserved; N2 pending, actual headroom/model not tested here. |
| D4 | Sufficient | Wet/service/shaft owners preserved; F-A adds air-interface consequences. |
| D5 | Partial | F-A real supply/closed-door/extract/roof chains, fault and changed channels; no flow approval. |
| D6 | Sufficient | Wall/roof/function-junction owners preserved, no new thermal/assembly performance. |
| D7 | Sufficient | Bounded revision mechanisms preserved; cross-domain consequences recorded in new probes. |
| D8 | Sufficient | Metrics/documentation/completion preserved; legal area definition unresolved if not selected. |
| K1 | Sufficient | Site/constraints methods preserved; original location/base drawings not issued here. |
| K2 | Sufficient with supplied indicators | F-T separate demand/capacity and once-only land; actual demographic and denominators stay explicit. |
| K3 | Partial | F-T constrained subset, real-gate scenario, integer allocation, whole-group refusal and parcel shape; non-educational service breadth must not be silently inferred. |
| K4 | Sufficient | Quarter/public network/massing alternatives preserved; no new entire quarter model. |
| K5 | Partial | F-V car/entry/55-degree bay geometry improves its vehicle part; full cycle links/street cross-sections/ramp breadth not demonstrated by this car test. |
| K6 | Partial | Vehicle and separate journey mechanisms preserved; actual appliance/deployment/fire strategy not established. Reassess whole-row architectural scope explicitly. |
| K7 | Partial | Session2 F-C and actual N3 routes pending; first session must not self-certify its own C. |
| K8 | Sufficient | Quarter documentation/visual/indicator methods preserved; no full coursework issue generated. |
| M1 | Sufficient with chosen mix | Dwelling/mix/furniture methods preserved; no full chosen3–4-flat program is completed here. |
| M2 | Sufficient | Existing actual regular-unit/core mechanisms preserved; correction inputs remain conditional. |
| M3 | Partial | F-S original transform/end-unit evidence available; Session2 corrected-ground transfer pending. Shared D authorship disclosed. |
| M4 | Sufficient as coordination | Session2 ground/interface test pending; original roof/basement/stair/product requirements remain separate. |
| M5 | Sufficient architecturally | Structural topology/section methods preserved; member/connection capacity remains engineering evidence. |
| M6 | Partial | F-A multi-home/channel/roof/functional separation checks; actual natural flow/fire/acoustic approval excluded. |
| M7 | Sufficient in reviewed scope | Facade/room/enclosure preserved; sun-dependent claims wait for F-C. |
| M8 | Sufficient for links | F-T land and F-V movements supplement court/ground owners; complete servicing/rights not established. |
| M9 | Sufficient as issue method | Documentation/metrics/mix/completion preserved; final whole-row audit still pending. |

## Remaining evaluation and checks

Await dot's delivery of the complete second-session report from the
[solution-withheld packet](pass-f-session-2-tasks.md). Then resolve verified
findings, finalize all35 current statuses with exact evidence/limits, record the
six **actual** navigation walks and comparison, and perform final fixed-revision
checks. Do not mechanically upgrade all historical partial rows or invent an
aggregate completeness score.

Session1's checkpoint checks PASS: skill checker8 operations/64 normative records/
104 runtime documents; all48 unchanged unit regressions; independent Pandoc GFM
119 Markdown files/2504 local links/161 tables, no warnings or missing/escaping
targets/anchors. All127 other preexisting architecture and138 outside files are
byte-identical to accepted E, including every method, operation, calculator,
test, normative/source record and asset. The original35 historical rows are
exactly preserved; the new worklist has35 distinct matching IDs. Only maintenance
evidence and raw tasks change. The separate one-off checker and seven pinned
brief-identity checks also PASS. The Issue checkpoint identifies the actual
commit and command results; these checks do not replace the outstanding tasks.
Pass F and the overall Issue remain open; no self-acceptance, PR or merge.
