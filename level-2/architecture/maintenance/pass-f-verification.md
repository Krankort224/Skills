# Pass F: cross-author transfer and final verification

Status: **execution complete, pending final review and dot acceptance**. Method target is accepted E
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
- [Session2 sun and ground transfer](#session2-sun-and-ground-transfer)
- [Six observed navigation routes](#six-observed-navigation-routes)
- [Coursework matrix reassessment](#coursework-matrix-reassessment)
- [Final verification and limits](#final-verification-and-limits)

## Authorship and actual independence

| Method contribution | Substantive author | Permissible transfer evidence |
| --- | --- | --- |
| A navigation; C sun geometry | Session1 | Session2 checked raw new sun tasks and recorded six navigation walks. |
| B vehicle/service allocation; E volume/exhibition | Session2 | Session1 new F-V/F-T/F-Q/F-X cases below. |
| Original D air topology, rigid transforms and local end-unit refit | Session2 | Session1 F-A/F-S: only unchanged original mechanisms; its edited global R channel coordinate and ground/core are supplied context, not independently certified here. |
| D widened ground/core correction, thresholds, section and its ledgers | Session1 | Session2 F-D-ground. Its original unit/air knowledge is fixed context, not independently certified by its author. |

No new sessions/agents were created. The two existing sessions have already
read/reviewed much of the corpus. These are cross-author changed-input tests,
not a cold-context or blinded user study. Session1 selected its new inputs;
Session2 received only [raw tasks](pass-f-session-2-tasks.md), not expected
results, and returned its complete report through dot. Both must disclose inherited familiarity and any authored interface.
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

At final consolidation Session1 additionally tested a different supplied service
metric: **planning retail floor-credit m²**, with group demands120/80/60,
R1 gross200 minus50 outside commitments=150 available and R2 available120.
A may use R1/R2, B only R1, C only R2; splitting credits is expressly allowed.
A70/50, B80/0, C0/60 closes260 demand against270 available. Removing B's gate
leaves80 unserved despite unchanged aggregate capacity. This is a second
cross-author test of the service-indexed procedure, not part of the earlier
checkpoint freeze. Its assumed planning metric is not statutory retail provision,
operator-confirmed shop capacity or visits/persons: spare school seats cannot
repair a floor-credit deficit. Actual project rates, hours, service metric,
parcel/room fit and authority must be supplied on their own basis.

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

## Session2 sun and ground transfer

Dot delivered the full unfiltered second-session report after its completion.
Its method target was E `2e5515ad960da98bdafefe72f52ade2efc24d580`, task packet
`739a40784bb2f0b1842a740a751bf66d4128c582`. Session2 reports freezing its own
results at2026-11-09 05:10:56 UTC **before** reading the dated matrix; it did not
open Session1 F answers or authored test outputs. It independently tested C and
Session1's D ground correction, while disclosing earlier review familiarity and
authorship of B/E/original D. No mandatory method correction was found.

Reported working evidence, retained on that executor at
`/tmp/issue13-passf-session2/`: `sun_transfer.py`, `sun_results.json`,
`ground_transfer.py`, `navigation.jsonl`, `raw-freeze.md`. The report identifies
56 read events and freeze SHA256
`a93003a2fcc18f13eb4e84812dfec9177d7c9f9ce68b1146a4ca0219676e425a`.
Those working files were not transferred to this executor. The integrated tables
below preserve the complete material results/constructions and their attribution;
Session1 checked arithmetic, interfaces and consistency but does **not** claim to
have re-executed the remote scripts or independently certified its own C/ground.

### F-C: complete events, alternative check and uncertainty

Use the [raw inputs](pass-f-session-2-tasks.md#f-c-sun-task): ENU, latitude52,
declination8, apparent solar time08…16, receivers P/Q and two rotated prisms.
Session2 expressed each local ray component as `a sinH+b cosH+c`, generated all
sign/face-parameter equality events, solved both trigonometric branches and
classified every open event cell by complete slab intersection. Original P had
13/11 cell boundaries for A/B, Q12/12, including window ends. Completeness follows
from this event partition, not a sampling claim.

Its independent geometric construction projects vertices of the portions above
the receiver onto that receiver's horizontal plane and tests the point against
their convex hull. It agreed in every event cell and on1001 additional moments
per combination. Throughout08…16 the sun is in front and above: minimum
s_U0.414505 and n·s0.304487. Contacts block; isolated contacts have zero duration.
All table times are **decimal apparent-solar hours**, rounded to six places,
not HH:MM, civil time or legal insolation credit. Durations used unrounded roots.

| Receiver / option | A blocks | B blocks | Blocked union | Unblocked h | Longest h |
| --- | --- | --- | --- | ---: | ---: |
| P original | 11.552837…13.640734 | 10.254780…11.625363 | 10.254780…13.640734 | 4.614046 | 2.359266 |
| P A lower | none | 10.254780…11.625363 | 10.254780…11.625363 | 6.629416 | 4.374637 |
| P B east | 11.552837…13.640734 | 9.951231…11.241419 | 9.951231…11.241419 + 11.552837…13.640734 | 4.621915 | 2.359266 |
| P both | none | 9.951231…11.241419 | 9.951231…11.241419 | 6.709812 | 4.758581 |
| Q original | 12.718953…14.686324 | 10.807505…12.428175 | 10.807505…12.428175 + 12.718953…14.686324 | 4.411958 | 2.807505 |
| Q A lower | none | 10.807505…12.428175 | 10.807505…12.428175 | 6.379329 | 3.571825 |
| Q B east | 12.718953…14.686324 | 10.416110…12.025023 | 10.416110…12.025023 + 12.718953…14.686324 | 4.423716 | 2.416110 |
| Q both | none | 10.416110…12.025023 | 10.416110…12.025023 | 6.391087 | 3.974977 |

Unblocked intervals are the complement in[8,16]. Original Q has three:
[8,10.807505), (12.428175,12.718953), (14.686324,16]. Active A transitions are
u_max/v_min corner and v_max/z_top edge; B uses u_max/v_max corner and
u_min/z_top edge. Lowering A to4.2 removes its blockage of both points. Moving B
1.2m east adds only28.33s total sun at P/42.33s at Q while **reducing** Q's longest
continuous period by23.48min. It is not an improvement under every criterion.
Height changes reopen program/roof; translation reopens land/neighbours/receivers.

For receiver x±0.08 and B rotation±1 degree, conservative inner/outer prisms use
A half-sizes±0.08 and B±0.14: rotation moves each local coordinate less than
(2+1.4)pi/180<0.06m, plus at most0.08 from relative receiver translation.
Inner prisms are inside every admitted relative solid; outer prisms enclose all.
Original P/B's nominal start10.254780 lies inside the justified transition band
10.190752…10.318587. Before the outer start B definitely does not block; after
the inner start it definitely blocks in this selected neighbourhood. Conservative
unblocked-time enclosures are P4.487265…4.762943h, Q4.180345…4.644360h.
These are enclosures, not exact joint parameter extrema or a global time tolerance.

### F-D-ground: entire paths and changed section

The target is Session1's corrected ground/core, not Session2's original unit/air
method. Exact rational rectangle sweeps of the0.85m square/2.20m-high probe
confirm the five original street-to-apartment/stair/lift/court interface paths.
A changed south opening is0.78m wide, a0.07m deficit. The new support intersects
1.84m² of the old bypass; east remainder0.90m cannot preserve its1.20m width.
Each change and their combined state therefore fail their respective conditions.

Session2 found this permitted correction, without deleting the0.60×4.60 support:

| Element | Corrected coordinates |
| --- | --- |
| South opening | x14.25…15.15, threshold y0…0.2 |
| Support | x14.6…15.2,y7.2…11.8 |
| 1.20m bypass | x14.1…15.3,y0.2…6.6 |
| 2.40m-deep landing | x10.2…14.4,y5.4…7.8 |
| 1.20m-wide B branch | x14.4…15.4,y5.4…6.6 |

All five whole sweeps pass, retaining north passage1.40, equipment interfaces,
private boundaries and thresholds. Support avoids these routes and equipment.
The restored sliding door/pocket x13.35…14.25 and its reserved wall/frame support
remain; new support occupies neither that node nor the north door. Product,
attachment and bearing capacity are unverified project evidence.

Section3−0.30−0.42=2.28m gives0.08 above the probe; services0.52 leave2.18,
a0.02 deficit. Plan rearrangement cannot repair that fixed vertical condition.
Footprint307.2, approach14.4, combined321.6 and two-floor614.4=480+134.4 stay
unchanged. Support occupies2.76m² of existing common reserve (5.52 if repeated),
reducing clear common area without increasing gross. A neighbour fixed at the
former x24 conflicts with the25.6-wide candidate by1.6×12=19.2m²; those fixed
boundaries, both homes and the enlarged core cannot all be retained together.
These checks end at thresholds/equipment interfaces, not movement on the stair,
lift operation or actual street/court levels, rights and external geometry.

## Six observed navigation routes

Session2 started each at `SKILL.md`, choosing operation and subject again.
`overview` means `references/index.md`; subsequent names are the actual reference
files/sections in opening order, not an ideal route reconstructed afterwards.
The reported56 events include selective rereading; they are not a usability score.
First substantive method below means the first subject method after operation/
index selection, not the operation procedure itself.
Session1 checked the named targets and ownership against the fixed corpus. The
complete remote JSONL was not independently read here.

| Task | Actual opening order after SKILL | First substantive method / outcome | Friction and qualification |
| --- | --- | --- | --- |
| N1 upper exhibit | operations/analysis → overview → space/index → space/circulation/access-and-closure → space/planning/room-floor-and-section → construction/structure/frame-and-core | Access/closure; receiving/holding/control/portals/lift/upper landing/hall and independent closed-tenancy access. | No area-ledger detour.3.2×1.8×2.4 is not a complete handler/carrier envelope; mass/orientation/allowances/cabin/door/pit/head/landing and operation remain inputs. |
| N2 moved bathroom | operations/development → overview → space/index → space/planning/room-floor-and-section (levels/core) → space/vertical/stair-section → space/vertical/section-and-services (reuse after F-D) → performance/comfort/natural-exhaust-topology → construction/structure/roof-and-span (thermal boundary/water) | Levels/core; walking profile, branches/shafts through floors, closed doors and roof interfaces. | Re-read the beginning after starting the levels range too late. Air owner is Session2's own D: navigation observation, not its independent air test. |
| N3 population/gate | operations/analysis → overview → program/index → program/demand → context/urban/service-capacity-allocation → context/urban/vehicle-and-parking-geometry → context/urban/quarter-and-public-space (ground/journeys) | Demand; separate units, available places, removed gate edge, reassignment and land. | Returned to actual-journey dependency after vehicle/ground. No actual allocation numbers supplied in this navigation question. B owners are the observer's own. |
| N4 section variants | operations/development → overview → typologies/index → typologies/housing/section-variants → typologies/housing/dwelling-fit → construction/structure/frame-and-core and performance/comfort/natural-exhaust-topology (reuse) | Transformations; whole portals/fronts/wall fit/ledgers/wet/roof consequences. | Original transform/air owners are observer-authored. Independent numeric finding is limited to F-D-ground; F-S is the opposite author's local test. |
| N5 Art Nouveau transfer | operations/concept → overview → composition/index → composition/styles/index → composition/styles/baroque-art-nouveau → composition/styles/precedent-transfer → assets/styles/art-nouveau/casa-batllo/analysis; selective rereads → composition/styles/character-to-decisions → composition/facade/hierarchy-and-rhythm → composition/facade/occupied-bays → composition/massing/section-form | Art Nouveau/Modernisme profile, then real spatial/facade transfer for a changed use. | Extra Baroque reading, recovery of truncated output and two failed guessed filenames rhythm-and-openings.md/character-and-reference.md; correct index links resolved them. These are search/read errors, not broken skill links. |
| N6 brief/provision | operations/brief → requirements → normative/index → program/demand (reuse) → methods/comparison#frame-the-question | Requirements; jurisdiction/version/applicability and decision ownership remain unresolved. | No Russian-module default or current numeric prescription. Preserve both sources/conflict; source access and geometric reasoning do not establish legal applicability. |

N5's concrete contemporary-clinic exploration compared a legible shared entrance
with simple repeated consulting rooms against a flatter facade/deep local waiting
zone. Transfer relates threshold, occupied depth, detail families and real rooms;
a historical image does not prove privacy/light/support. The Casa Batllo case is
selected Catalan Modernisme evidence, not a complete measured plan.
The clinic alternatives establish no healthcare-specific planning or approval.

Comparison with [dated A probes](coverage-and-verification.md#six-task-route-probes),
read only after freezing current results: N1 avoided the former area detour;
N2 reached connected owners directly, with a selective-reading retry; N3/N4 now
reach substantive allocation/vehicle/transform methods where A recorded gaps.
N3 still needed a dependency reread. N5/N6 retain working paths with N5's search
errors explicitly recorded. This is an observed qualitative comparison: no new
global7.6-style score, reconstructed historical transcript or causal speed claim.
Current mixed-author selectors and prior review familiarity preclude a wholly
uninvolved or cold-context navigation test under this two-session arrangement.

## Coursework matrix reassessment

The [historical35 rows](coverage-and-verification.md#historical-35-row-benchmark)
remain immutable dated judgments. Brief identities/read extents are at
[source identity](coverage-and-verification.md#source-identity-and-inspected-extent),
Architecture snapshot `5a0282b0d49792e7688dc2c1f26aca0a8bbcf54d`.
All seven cached files were SHA256/byte-count matched against the freshly fetched
primary manifest in F. Principal KP1–KP4 requirements were re-read, including
KP4's roof/street/court/basement,3–4 flats/core,natural ducts and car-free court.
Graphic-only pages, the differing house-site versions and current legal force
remain unresolved exactly as recorded. KP5 is excluded.

**S** means a sufficient local architectural mechanism in the stated brief-level
scope, with normal project inputs/authority/product evidence still to be supplied;
**P** means a substantive local procedural breadth gap remains. Lack of a selected
site, family, vehicle/product or current governing value is not by itself a skill
gap. No status certifies an actual coursework design or statutory readiness.
The26 previously sufficient rows were reassessed by their primary-brief scope,
preserved complete owners and relevant new task/route evidence; they were not
rerun as26 new CAD/BIM projects or claimed as26 fresh blind trials. Changed rows
below cite their new local mechanism and opposite-author tests explicitly.
These are **executor assessments for review**, not dot's acceptance.

| Row | Historical → current | Mechanism/evidence and exact boundary |
| --- | --- | --- |
| P1 | S → S | Demand/area owners preserved; actual simultaneous activities, support and unknown quantities stay explicit. No chosen pavilion program completed. |
| P2 | S → S | Site/approach/seasonal owners preserved; actual park, retained trees/levels and rights remain inputs. |
| P3 | P → S | Vehicle method and F-V resolve body sweep, entry/column/row/land versus mere counts; site/access owners trace full journeys. Appliance/deployment/authority must be selected separately; the car is not a fire-approval surrogate. |
| P4 | S → S | Object/handler/access owners plus F-X complete wall throats, old-load dispatch and whole-H closure while spine remains. Actual operation/load/support remains unbuilt. |
| P5 | S → S | Core/stair/lift profile owners plus observed N1 provide receiving/landing/pit/head/all-level checks; actual supplier capacity and evacuation evidence remain separate. |
| P6 | S → S | Massing/roof/support and height-budget mechanisms preserved; no member sizing or verified structural capacity. |
| P7 | S → S | F-X new horizontal-model occlusion, alternative interpretation, overview and changed layout; actual crowds/reflection/material visibility still need tests. |
| P8 | S with appendix caveat → S with new independence evidence | Collection-specific exhibition owner and F-X select enclosure/control from a new brief without appendix answers. Historic caveat retained in the dated matrix; actual illumination/fading is unverified. |
| P9 | S → S | Documentation/view/issue and visual-delivery owners preserved; no actual new coursework album rendered. |
| P10 | P → S | Volume owner and F-Q explicit metric, signed solids, varying court exclusion, independent surfaces and changed boundaries. Formal measurement still needs its actual provision, not a hidden universal formula. |
| D1 | S → S | Household/scenario/site/demand mechanisms preserved; no actual family/site chosen here. |
| D2 | S → S | Complete room/actions/use owners preserved; F-S reinforces actual furnishing/door consequences, not a whole new house. |
| D3 | S → S | Stair walking/headroom and floor/attic/roof owners plus observed N2; actual surveyed section/product not executed. |
| D4 | S as coordination → S as coordination | Wet/service/shaft routes and maintainability preserved; F-A adds physical supply/branch/roof effects, separate from MEP sizing. |
| D5 | P → S as architectural topology | Air owner/F-A trace actual inlet, closed-door transfer, extract, channel and roof with missing-supply/reverse/pressure failures. Graph and static drive do not prove flow. |
| D6 | S → S | Wall/roof/functions and junction-continuity methods preserved; no new tested assembly/thermal performance. |
| D7 | S → S | Bounded revision owners preserved; F cases propagate changed geometry to section, program/land and operation rather than rename it. |
| D8 | S as issue method → S as issue method | Area/documentation/completion retained; actual legal area definition and issued project remain dependencies. |
| K1 | S → S | Site/constraints/relationship/requirements owners preserved; no new surveyed base plan or actual site selection. |
| K2 | S with supplied indicators → S with supplied indicators | Demand/metric/ground owners and F-T distinct seats, people, floor and land, once-only reservations; actual rates/denominators remain explicit. |
| K3 | P → S for territorial allocation | General service-indexed allocation owner/F-T give available capacity, eligible entrance chains, cuts/reassignments, indivisible-policy refusal and usable parcels. Additional planning retail m²-credit transfer keeps a separately supplied metric and gate deficit; no seat/area/occupancy conversion or complete retail typology is inferred. |
| K4 | S → S | Quarter hierarchy/mixed addresses/alternatives and massing owners preserved; F-T/C demonstrate consequential ground/height changes, not a whole new quarter. |
| K5 | P → P, vehicle part substantially deepened | F-V and B give actual car/entry/bay/sweep/land mechanisms. A complete cycle-network/street transverse-profile construction and its level/operation checks are not supplied by that car method or demonstrated by these probes. This is residual procedural breadth, not merely absent normative widths. |
| K6 | P → S for architectural journey/vehicle reservation | Quarter whole-journey, inclusive/emergency interfaces and vehicle/service-envelope methods now connect actual paths, crossing/control/standing/working and ground. F-V/T/N3 support the former vehicle gap; selected real appliance, deployment/load/assistance/fire/access approval remains unverified, as required by those owners. |
| K7 | P → S in bounded geometric/architectural scope | Opposite-author F-C proves rotated multi-body point intervals, unions, independent geometry and bounded uncertainty; preserved daylight/court owners address occupied consequences. Fixed-declination prisms/points do not establish actual ephemeris, surface-wide daylight or legal insolation. |
| K8 | S as issue method → S as issue method | Quarter documentation/presentation/indicator mechanisms preserved; no actual full masterplan issue produced. |
| M1 | S with chosen mix → S with chosen mix | Household/mix/dwelling/furniture mechanisms preserved; actual3–4-flat mix still must be supplied and fitted, not certified by the two-home example. |
| M2 | S → S | Existing real regular-unit/core and fitted-room mechanisms preserved; widened-envelope/neighbor inputs remain conditional. |
| M3 | P → S as a transformation mechanism | Original transform/end owner and opposite-author F-S plus the other session's F-D-ground prove nonoverlap/whole portals, refit and ground/section/ledger corrections. Shared D authorship is split and disclosed, not a wholly independent reapproval of all D or a completed actual3–4-flat section. |
| M4 | S as coordination → S as coordination | Core/support/program/ground owners plus F-D-ground and N1/N4 establish interface continuity and section refusal. Basement/roof/concierge/stroller/vestibule and actual equipment requirements still need their real project fit; this probe does not newly certify them. |
| M5 | S architecturally → S architecturally | Structural topology/section/wall-floor owners preserved; no connection/member engineering capacity inferred. |
| M6 | P → S as architectural topology | F-A multi-home channels/roof/functional isolation and changed shaft/utility accounting; actual natural flow, fire/acoustic construction and terminal performance are not proved. |
| M7 | S in reviewed scope → S in reviewed scope | Facade/occupied bay/enclosure owners preserved; F-C supplies selected-point shading and N5 actual precedent/facade lookup. Full daylight/enclosure/current insolation compliance remains separate. |
| M8 | S for planning/operation links → S for those links | Home/court/service owners, F-T land and F-V routes retained; rights, actual servicing and approvals remain project evidence. |
| M9 | S as issue method → S as issue method | Plans/sections/facades/mix/metrics/documentation/completion owners preserved; no actual project issue or new normative approval asserted. |

Bookkeeping only: KP1 now10S/0P, KP2 8/0, KP3 7/1, KP4 9/0; total34S/1P
against historical26S/9P. This is neither an acceptance threshold nor universal
competence. Eight partial rows gain bounded mechanisms; K5 retains the stated
cycle/street-profile breadth gap. P8's separate independence boundary improves
without inventing a tenth historical partial. The six confirmed core topics and
appendix-independent exhibition selection have concrete new-condition evidence;
that does not erase limitations of their deliberately bounded models.

## Final verification and limits

Session1 integrated the other session's complete report, checked its interval/
area/height arithmetic, inequalities, cited file identities and consistency with
the task packet. No new runtime defect or mandatory method correction emerged.
The required next action is final fixed-revision review and dot's explicit
acceptance decision, not another self-acceptance or a new session.

The checkpoint at739a407 already passed48 regressions, checker8 operations/
64 normative records/104 runtime documents and GFM119 files/2504 local links/
161 tables. Final handoff records fresh counts and actual commands at the final
revision; historical numbers above retain their checkpoint identity. All runtime
methods/calculators/tests/normative/source/asset content remains unchanged from E.
Only maintenance evaluation/status/results change; no model, new dependency,
source media or generated graph is installed.

Final integration checks PASS: all48 unit regressions and the targeted19
calculator-contract tests; checker8 operations/64 normative records/104 runtime
documents; independent Pandoc GFM119 Markdown files/2507 local links/164 tables,
no warnings or invalid resources/anchors. All127 other preexisting architecture
and138 outside files are byte-identical to E, including protected runtime,
normative/source and asset resources. The original historical35 rows and frozen
Session2 raw-task packet are unchanged; the new current matrix has35 unique IDs,
34 scoped S/1 P(K5). The final Issue handoff pins these results to its commit.

Limits carried forward: familiar two-session cross-author checks, shared D and
mixed-author navigation; remote raw evidence not re-executed in this executor;
graphic-only brief pages and house-site version conflict; actual site/program/
rights/product and operation; real ephemeris/complex geometry/whole-surface light;
photometry/collection behaviour; MEP/structure/fire/access/measurement approval.
K5's broader cycle/street-profile procedure remains partial. These are explicit
limits, not silently completed designs or a reason to guess current code values.
Pass F is pending review/acceptance; the Issue stays open. No PR, merge or closure.
