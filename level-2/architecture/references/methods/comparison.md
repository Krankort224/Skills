# Computational thinking for design decisions

Use these methods to make bounded architectural choices inspectable. Select the
method needed by the decision; this is not a compulsory sequence or output format.
Apply the decision methods to the available architectural information, whether expressed as descriptions, dimensions, schedules, drawings, models or data. This reference supplies comparison methods, not a bundled solver or a required modeling environment.

## Contents

- [Frame the question](#frame-the-question)
- [Generate controllable alternatives](#generate-controllable-alternatives)
- [Compare options consistently](#compare-options-consistently)
- [Test sensitivity and reproducibility](#test-sensitivity-and-reproducibility)
- [Screen data before translating it into design](#screen-data-before-translating-it-into-design)
- [Check adjacency and access as separate relationships](#check-adjacency-and-access-as-separate-relationships)
- [Evidence and implementation](#evidence-and-implementation)

## Frame the question

**Decision and boundary.** Define what can change and what the comparison must
decide. Entering a parameter in a table does not make it measured, legally binding
or independently adjustable. Use [program and space](../program/demand.md) for the
program and [requirements](../requirements.md) for applicability.

**Inputs.** Use the current brief, accepted baseline, site/program evidence and
stakeholder priorities. Retain source, revision, units and uncertainty for each:

| Role | Meaning | Example |
| --- | --- | --- |
| Fixed | Held constant in this comparison, possibly uncertain | Supplied enclosed area |
| Variable | A controllable choice within a justified domain | East or west entry |
| Derived | Recomputed or reassessed from other inputs | Circulation allowance |
| Missing | Not established; never silently substituted | Service access requirement |

**Procedure.** State the decision, affected interfaces and criteria that could
change the choice. Trace dependencies: if usable area is derived from gross area
and exclusions, do not vary all three independently. Separate verified hard
constraints, unresolved prerequisites and preferences. Classify by actual authority
and applicability, not topic: acoustic separation may be mandatory in one brief
and preferred in another. For a conditional rule, record its trigger and the
evidence needed to establish applicability. Evaluate known hard constraints before
preferences; leave unknown prerequisites **unverified**, rather than passed/failed.
Name the responsible source or decision-maker for each material unresolved input.

**Alternatives and checks.** If fixed requirements conflict, identify the smallest
known conflict and the decision needed to resolve it. Continue unaffected work or
explicit conditional branches. Do not silently relax a requirement or apply a
generic legal hierarchy. Check units, area definitions, valid domains and dependency
direction. A plausible dimensional range does not establish engineering feasibility.
A narrow revision may require only changed inputs and their affected interfaces.

**Worked example.** A hypothetical brief fixes 600 m² enclosed area, 450 m² usable
program and 90 m² services/walls on the same measurement basis. The derived
circulation allowance is 600−450−90=60 m². Option A needs 70 m²: it exceeds the
allowance by 10 m² and is infeasible under those fixed inputs. If 90 m² is only
provisional, A remains conditional pending a defensible revision; an attractive
entrance does not offset the unresolved area conflict.

For a Russian task, include measurement purpose, host/embedded use, work type
and relevant project date among the fixed selection inputs. Resolve them through
[area and capacity selection](../normative/ru/applicability.md#choose-the-area-and-capacity-basis)
and [use and works selection](../normative/ru/applicability.md#classify-use-and-works-before-applying-a-rule).
Keep both the geometric result and any selected statutory metric with their
own definitions. Changing from a room reservation to finished room area, from
an apartment total to a building total, or from operating demand to a prescribed
population is a change of evaluation basis. Recompute affected options under
that basis; it is not an independently adjustable efficiency variable.

For example, option A's “24 m² room” measured before finishes and option B's
23.5 m² finished room cannot establish that A supplies more finished activity
space. Under the hypothetical finishes in the
[boundary correction](../program/area-ledger.md#how-can-areas-be-counted-once-and-compared),
A supplies 23.01 m² and B supplies 23.5 m² on that particular finished-rectangle
basis. The ranking reverses without changing either plan. This supports B only
on the stated geometric criterion; current Russian inclusions/exclusions, room
fit and the actual applicable minimum remain separate inputs. Do not fabricate
a conversion factor or let an unresolved statutory metric receive a passing score.

## Generate controllable alternatives

**Decision and boundary.** Explore different organizing choices before refining
small dimensions. Generate a bounded, explainable set manually; this does not
implement a generator or guarantee complete design-space coverage.

**Inputs.** Use framed constraints, an accepted concept where applicable, controllable
variables, justified domains, evaluation effort and a common comparison basis.
Separate organizational choices (shared hall/distributed circulation), dimensional
choices (bay depth) and presentation choices (color/rendering).

**Procedure.** Select variables that materially affect the decision and explain
their architectural mechanism. Define meaningful levels/categories and dependencies.
Distinguish all combinations of choices from pairing corresponding list entries.
Filter known hard-constraint failures, preserve prerequisite flags and retain
rejection reasons. Give options stable identifiers/revisions and describe what
actually differs. Include the baseline where useful. State which change is expected
to help which criterion and what it might worsen. Reassess after revising an option;
do not attach old results to its new revision.

**Alternatives and checks.** Enumerate a small meaningful domain, or sample a larger
one with explicit gaps and extremes/intermediate cases. Include different organizing
ideas while the concept is open; cosmetic variants do not test spatial alternatives.
Stop adding options when they repeat known trade-offs, or identify the unexplored
area that could still change the decision. Stable scores or repeated similar
options do not establish a global optimum.

**Worked example.** Two permitted entrance sides combined with either a shared hall
or perimeter corridor give four intended combinations, not two paired combinations.
West-entry/shared-hall routes deliveries through public gathering space, failing a
verified separation requirement; reject it. East-entry/shared-hall retains communal
focus. The corridor options offer independent quiet-room access with more circulation.
Keep those three to test communal-space/privacy trade-offs on the same program.

**Optional facade reasoning.** From supplied 2D elevations/schedules, compare an
unaltered rhythm, repeated nominal bays and repetition with explicit exceptions.
Check entry emphasis, opening alignment and departures from composition as well as
type counts. Eight bays at 1.20 m and four at 1.25 m total 14.60 m with two nominal
widths. Twelve at 1.20 m total 14.40 m: the unexplained 0.20 m prevents calling this
equivalent. Retain an exception or revise spacing explicitly. Nominal repetition
alone proves neither shared fabrication tooling, fit, cost savings nor constructability.
Do not import curvature formulas, engineering limits or fabrication tolerances.

## Compare options consistently

**Decision and boundary.** Expose feasible trade-offs and why a direction is
preferred. Scores support judgment; they establish neither overall architectural
quality nor compliance.

**Inputs.** Match program, measurement boundary, evidence date and evaluation method.
Define criterion units or qualitative rubrics, preference direction, uncertainty
and omissions. Name proxies honestly: exterior-wall contact is an opening
opportunity, not daylight performance. Use [calculators](../calculators.md) only within
its exact schemas and limits.

**Procedure.** Show constraint failures and unverified prerequisites first. Compare
eligible options criterion by criterion with raw values and explanations. Define
observable qualitative distinctions, such as quiet-room access through an event
space versus independent access; do not invent precise distances between categories.
One option dominates another only if at least as good on every comparable criterion
and strictly better on one. Call an option **non-dominated within the evaluated
set** when none dominates it; this says nothing about unexplored designs.
Missing evidence cannot establish dominance; uncertain small differences may be ties.
A recommendation of the only currently verified feasible option does not prove
an optimum, even within the evaluated set: unresolved prerequisites or undecided
preferences can change which option is eligible or preferred.

If aggregation helps, disclose stakeholders, weights and normalization. For a
minimizing metric, a declared range L to H gives penalty (x−L)/(H−L); for maximizing,
use (H−x)/(H−L), so lower is consistently preferred. State whether bounds are project
reference values or this set's extrema. Equal bounds have no discriminating scale:
omit that criterion from aggregation and explain. Do not silently clip out-of-range
results. A weighted sum permits compensation between preferences, never a failed
hard constraint. Avoid counting the same benefit twice through correlated metrics.

**Alternatives and checks.** Use raw comparisons, agreed priority order or aspiration
filters when weights lack meaning. Retain raw values even with scores. Check
plausible stakeholder weights and alternate normalization bounds: adding an option
can change candidate-set extrema and the ranking. Preserve omitted qualitative
considerations and unresolved prerequisite flags alongside any preferred direction.

**Worked example.** A has 40 m² circulation and four of six preferred direct links;
B has 50 m² and six links; C has 55 m² and four links, on one common boundary.
A dominates C on these criteria; A and B trade area for links. Declared comparison
bounds 40–60 m² and 0–6 links give penalties A=(0,1/3), B=(1/2,0).
With circulation weight w, A scores (1−w)/3 and B scores w/2: tie at w=0.4.
Above 0.4 A ranks first; below it B ranks first. This exposes preference sensitivity,
but does not justify treating links of different importance as equivalent.

## Test sensitivity and reproducibility

**Decision and boundary.** Find uncertainties that could reverse the choice and
the evidence worth obtaining next. Scenario testing is conditional reasoning,
not a probability forecast or proof of robustness.

**Inputs.** Retain option revisions, input provenance, formulas/rubrics and baseline.
Choose ranges/categories from actual project uncertainty, not a generic percentage.
Distinguish uncertain evidence, controllable choices and stakeholder preferences.

**Procedure.** Change one uncertain independent input at a time, holding the others
constant and recomputing dependent quantities. Record changes in feasibility,
ranking and the qualitative reason for selection. Locate a switch point where
the method supports one and state precision. Then test meaningful combinations
when inputs interact: entry location plus operating hours, or circulation type
plus event use. Avoid impossible combinations of correlated inputs. If new evidence
changes the evaluation method itself, disclose that method revision separately.

**Alternatives and checks.** Use conservative/central/expanded-program scenarios
when evidence cannot justify a continuous range. Report known constraint margins
and separate common risks from option-specific ones. State conditions under which
a preference holds and the evidence needed to resolve it. If all options fail,
revisit the conflict instead of lowering thresholds silently. Keep enough inputs,
dates, definitions, arithmetic, judgments and limitations with the decision for
another reader to repeat it in the project's existing format.

**Worked example.** Hall A provides 120 m² activity space but passage crosses it;
B provides 105 m² with independent access. A supplied event brief requires 100 m²
clear activity space. Reserving 15 m² of A for passage leaves 105 m²: both meet
that area requirement. Concurrent use requiring 25 m² passage leaves A with 95 m²,
failing by 5 m²; B retains 105 m². The interaction is concurrency with access, not
simply hall size. If passage and events never coincide, A remains a candidate;
verify the operating schedule before rejecting it outright.

## Screen data before translating it into design

**Decision and boundary.** Determine what data can support before it changes
program, access or layout. Evidence may support a design hypothesis without
establishing demand, causation, legal boundaries or future behavior. This is not a sensor/GIS deployment.

**Inputs.** Identify owner, collection period/date, location, coverage, sampling
method, definitions, units, processing, permissions and omissions. Distinguish
observations, estimates, inferred proxies and judgments. For spatial evidence,
record CRS, reference/origin, scale and positional accuracy; do not measure
design distances directly from unexamined longitude/latitude coordinates.

**Procedure.** Inspect completeness, duplicates, impossible values, sensor flatlines,
timestamp/time-zone alignment and gaps. Compare periods/locations before combining
data. Check spatial alignment against known references and identify absent features
or populations. Record exclusions/transformations. Preserve missing observations
unless explicit justified imputation suits the question. Check representativeness,
then state observation → interpretation → proposed design response. For each arrow,
identify an alternative explanation and a check capable of refuting it. Use
aggregation appropriate to actual permissions; adopt no generic bin sizes,
retention periods or claimed anonymization guarantees from a design reference.

**Alternatives and checks.** Triangulate with observations, a survey, another source
or a conditional scenario. Obtain better evidence when accuracy is inadequate;
use broader zones instead of false dimensional precision. Wi-Fi devices are not
people, CO₂ alone is not occupancy, mapped paths are not verified access rights,
and old footprints are not surveyed current boundaries. State bias/transfer limits.

**Worked example.** A supplied counter records 80 east-entry and 20 west-entry
passages during an ordinary weekday. Equal observation duration suggests an east
emphasis, but the west gate was closed for half that period. Dividing west counts
by open time assumes constant arrival rate; without hourly data this correction
is unsupported. Retain east-led and west-linked options, obtain open-gate/event
observations, and avoid sizing the west entry on a claim of one-fifth future use.

## Check adjacency and access as separate relationships

**Decision and boundary.** Expose spatial connections, segregation and route
dependencies using a small graph/table. This is bounded topological reasoning
informed by space-syntax concepts, not axial/visibility simulation, human-behavior
prediction, accessible-route verification or egress assessment.

**Inputs.** Name spaces/zones and the tested relationship: shared boundary, direct
door access, visibility, preferred proximity or required separation. Record source
and status. Keep desired relationships separate from each option's actual/proposed
connections; unknown links stay unknown.

**Procedure.** Use one row per unordered pair or a symmetric adjacency matrix,
checking for double counts. Keep required/preferred links distinct; never interpret
a separation instruction as a traversable edge. Build an access graph only from
usable door/passage links under the stated operating condition. Declare direction,
closed/restricted-door handling and vertical links. Count connections or minimum
intervening links by inspection for a small graph; unreachable destinations have
no finite link count. Match nodes, boundary and operating condition across options.
Check the actual 2D arrangement: a graph does not establish dimensions, packing or fit.

**Alternatives and checks.** Examine event/ordinary or staff/public access separately
when links differ. Summarize preferred links with an explicit denominator only if
useful; required failures remain visible. With no preferences the score is not
applicable, not perfect. Degree/link counts alone establish neither privacy,
distance, wayfinding success, congestion nor safety. A visibility graph would
change the representation and evidence required.

**Worked example.** Nodes entrance E, lobby L, hall H and quiet room Q have links
E–L, L–H, H–Q in A and E–L, L–H, L–Q in B. E-to-Q needs three links in A and
two in B. Closing the hall during events makes Q unreachable in A while B keeps
access. That supports B for independent access under that condition. It does not
prove B has a shorter measured route or is quieter: check dimensions, permissions
and acoustic separation independently.

## Evidence and implementation

These methods provide a decision frame, alternative generation and reviewable
comparisons. Use them with the representations and computational workflows
available for the task. For calculations using this skill's bundled tools, follow
the exact [calculator contract](../calculators.md). A numerical result, algorithm or
model alone does not establish engineering sizing, fabrication feasibility or
regulatory compliance; those claims require appropriate inputs and validation.
Distinguish a prepared method, an attempted execution and a verified result.


Provenance and selective reading extents are recorded in [sources](../../sources/upstream-packs.md#comparison-and-data); use the methods here without opening upstream collections.
