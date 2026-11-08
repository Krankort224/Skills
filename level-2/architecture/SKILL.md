---
name: architecture
description: Architectural design knowledge and methods for developing, revising, comparing, presenting and reviewing spaces and buildings through programs, spatial planning, composition, styles, materials, and evidence-based analysis. Apply these methods to the user's chosen task, format and available workflow.
---

# Architecture

## Contents

- [Choose the operation](#choose-the-operation)
- [Shared design contract](#shared-design-contract)
- [Load knowledge by question](#load-knowledge-by-question)
- [Tools](#tools)
- [Completion and integration](#completion-and-integration)

## Choose the operation

Start at the requested operation. Read its procedure and only the reference sections needed for that decision. Operations are selectable activities, not a compulsory sequence or executor roles. Reuse supplied project information and accepted decisions.

Develop solutions with the local knowledge below. Upstream collections are provenance for skill maintenance, not runtime dependencies. When a brief asks for a whole design, synthesize program, plan and section, form/material intent and interfaces together; for a bounded request, work only on the affected decisions.

| Request | Procedure | Result |
| --- | --- | --- |
| Establish or clarify the design task | [Brief](operations/brief.md) | Actionable program, relationships, constraints and open decisions |
| Explore an organizing architectural idea | [Concept](operations/concept.md) | Meaningful alternatives and a reasoned direction |
| Refine a selected solution | [Development](operations/development.md) | Coordinated spatial, facade and material decisions |
| Check a quantitative or qualitative question | [Analysis](operations/analysis.md) | Inputs, method, results, interpretation and limits |
| Compare controllable alternatives | [Optimization](operations/optimization.md) | Feasible options and explicit trade-offs |
| Present the design in the requested form | [Presentation](operations/presentation.md) | Requested presentation, with appropriate inspection of any artifact |
| Explain and hand off the design | [Documentation](operations/documentation.md) | Coordinated narrative, schedules and drawing/content requirements |
| Assess a design against its brief/evidence | [Review](operations/review.md) | Prioritized findings and concrete corrections |

For a local revision, identify the accepted baseline, requested change and affected interfaces. Preserve decisions outside that boundary and check consequences without restarting the whole design cycle. Select additional operations only when the requested result requires them.

## Shared design contract

- Architecture contributes methods for purpose, program, composition, spatial organization, stylistic direction, facade/material intent and evaluation of design alternatives. Apply them through the representations, models, data and tools relevant to the task.
- Separate source-backed normative requirements, project requirements, provisional assumptions, performed calculation results and design judgments. Retain their source, units, applicability and uncertainty. An attractive image or successful tool exit does not prove a design decision correct.
- Keep project facts, dimensions, site/software profiles, source selections and accepted decisions in the project's existing authoritative material. Reuse its structure; do not create a second project/process framework.
- Establish jurisdiction and applicable source versions explicitly. Unknown jurisdiction allows independent design exploration, with normative conclusions left open. Do not infer location from language/currency or apply foreign-code defaults. Use [requirements](references/requirements.md) for applicability checks.
- Define area/occupancy/performance metrics before comparing them. Geometric area, GFA/GIA/NIA and local legal area definitions are not interchangeable. Record conversion assumptions and reject ambiguous units or incompatible definitions.
- Describe styles through composition, proportion, spatial character, material/facade treatment and contextual fit. Verified named architects, identified buildings and relevant history may explain those mechanisms and their adaptation. Do not substitute biography/name lists, unsupported classifications or copied designs for architectural reasoning.
- Identify contradictions between fixed requirements before claiming a feasible solution. Show the incompatible constraints, continue independent work and identify the decision needed to proceed; do not silently relax a requirement.
- Follow the user's chosen deliverable and format for the current task. A concept request may be answered in text when no artifact is requested. Do not impose an image/file, a preset format or an automatic SVG default. Produce and appropriately inspect any requested artifact; clarify an unspecified format only when necessary to complete that deliverable. Identify diagrammatic, dimensionally controlled and illustrative content honestly.
- Choose checks proportional to uncertainty and stage. Distinguish a prepared method, an attempted execution and usable results. Report unavailable tools, invalid inputs or failed runs without inventing results.

## Load knowledge by question

Use the direct common-question routes below when the method is known. If the
request spans domains or its home is unclear, select only the relevant section
of the [knowledge/coverage map](references/knowledge-map.md):
[quarter/urban context](references/knowledge-map.md#quarter-and-urban-context),
[site](references/knowledge-map.md#site), [building](references/knowledge-map.md#building),
[spaces](references/knowledge-map.md#spaces), [systems/assemblies](references/knowledge-map.md#systems-and-assemblies)
or [cross-cutting methods](references/knowledge-map.md#cross-cutting-methods).
The map declares bounded methods, partial coverage and shared owners; it is not
a required whole-file read or a second design entry point. Typologies and styles
connect to those homes rather than duplicating their procedures. A route alone
does not establish complete competency in its subject.

| Question | Reference |
| --- | --- |
| Activities, concurrent demand and room program | [Program demand](references/program/demand.md#what-activities-and-capacity-must-the-program-accommodate) |
| Conflicting brief statements, shared staff or changeover between bookings | [Conditional demand](references/program/demand.md#turn-an-incomplete-brief-into-testable-demand), [resource timeline](references/program/shared-use.md#test-shared-use-as-an-occupancy-and-resource-timeline) |
| Room fit, plan families, floors and cores | [Planning and section](references/planning-and-section.md) |
| Furnished family/compact dwelling, door use or gross-to-clear deductions | [Dwelling fit](references/dwelling-fit.md#test-a-dwelling-through-its-actual-use) |
| Bearing walls, floor direction, stair/shaft voids or window operation | [Wall/floor organization](references/wall-floor-and-opening.md#make-wall-roles-and-floor-direction-agree), [floor openings](references/wall-floor-and-opening.md#place-a-floor-opening-without-erasing-its-support), [wall openings](references/wall-floor-and-opening.md#develop-a-wall-opening-as-support-and-use) |
| Stair opening fits in plan but headroom or upper arrival is unresolved | [Walking profile and section](references/stair-section.md#build-and-test-the-walking-profile) |
| Area boundary, allowances and double counting | [Area accounting](references/program/area-ledger.md#how-can-areas-be-counted-once-and-compared) |
| Adjacency, access and people/goods routes | [Relationships](references/program/relationships.md#which-relationships-must-the-plan-satisfy), [movement](references/space/circulation/access-and-closure.md#how-do-people-and-goods-move-through-access-zones) |
| Spaces inside, overlapping, beside or linked to each other; a route that crosses an activity | [Spatial relationships](references/spatial-composition.md#choose-how-spaces-meet), [path relationship](references/spatial-composition.md#place-movement-beside-through-or-into-a-space) |
| Floors, adaptability or a bounded layout change | [Vertical organization](references/program/floors-and-change.md#how-should-the-program-occupy-floors-and-adapt-over-time), [local revision](references/methods/bounded-revision.md#how-should-a-bounded-revision-or-comparison-be-judged) |
| Site, arrival and meaningfully different concepts | [Context](references/context/site/arrival-and-setting.md#how-should-the-design-respond-to-site-and-arrival), [partis](references/composition/massing/parti.md#how-can-different-partis-be-generated-and-compared) |
| Urban edges, outdoor rooms, approach or sloping ground | [Site and context](references/site-and-context.md) |
| Several plots/buildings, public-space hierarchy, independent phases or seasonal ground use | [Quarter and public space](references/quarter-and-public-space.md) |
| Housing mix, apartment aspects, gallery/landing choice or home-to-court journeys | [Dwelling/access family](references/housing-and-court.md#choose-a-dwelling-and-access-family-together), [court and servicing](references/housing-and-court.md#connect-home-court-and-servicing) |
| Learning clusters, public libraries, short-stay accommodation or mixed operators | [Use-family selection](references/building-use-families.md#select-a-family-by-its-operating-commitments), then the matching Contents method; [shared interface](references/building-use-families.md#combine-families-at-an-explicit-interface) when uses meet |
| Existing fabric, incomplete survey or retain/repair/replace choices | [Conditional commitments](references/existing-building-adaptation.md#turn-partial-survey-into-conditional-commitments), [intervention choice](references/existing-building-adaptation.md#choose-retain-repair-or-replace-against-the-changed-use) |
| Old/new substrate, control-layer transition or occupied work | [Retained-substrate interface](references/existing-building-adaptation.md#connect-replacement-work-to-the-actual-retained-substrate), [occupied states](references/existing-building-adaptation.md#test-occupied-work-as-a-succession-of-usable-states) |
| Mass/void, hierarchy, style or material expression | [Composition questions](references/composition/index.md) |
| Named style, architect or building; transfer to another brief | [Direction/case selector](references/style-directions.md#select-by-the-design-question), [evidence before classification](references/style-and-precedent-methods.md#read-an-object-before-classifying-it), [mechanism transfer](references/style-and-precedent-methods.md#transfer-a-mechanism-into-a-changed-brief) |
| Light, view, noise and ventilation trade-offs | [Daylight](references/performance/comfort/daylight-view.md#daylight-view-and-occupied-comfort), [acoustic paths](references/performance/comfort/acoustics-and-air.md#acoustic-paths-and-ventilation-choices) |
| Simultaneous environmental demands, partial closure, usable controls or failed equipment | [Coexisting occupied states](references/environmental-operating-modes.md#develop-states-that-can-actually-coexist), [changeover and failure](references/environmental-operating-modes.md#make-changeover-usable-and-failure-explicit) |
| Envelope junctions, durability or engineering space | [Continuity](references/envelope-and-assemblies.md#climate-exposure-and-envelope-continuity), [maintenance](references/performance/lifecycle/durability.md#durability-and-maintenance-of-materials), [reservations](references/space/vertical/section-and-services.md#budget-the-section-and-routes) |
| Envelope system selection and assembly/junction intent | [Envelope and assemblies](references/envelope-and-assemblies.md) |
| Clear-span roof or arch/tie/ridge choices | [Spanning mechanism](references/roof-and-span.md#choose-a-spanning-mechanism-and-its-boundaries), [ridge support](references/roof-and-span.md#distinguish-a-ridge-board-from-a-supported-ridge) |
| Roof insulation boundary or drainage conflicts | [Thermal boundary](references/roof-and-span.md#choose-where-the-thermal-boundary-follows-the-roof), [roof water](references/roof-and-span.md#resolve-roof-water-in-plan-and-at-the-junction) |
| Basement, raised floor, buried interface or excavation beside existing support | [Underground program](references/ground-and-basement.md#decide-what-actually-needs-to-be-below-ground), [neighboring ground](references/ground-and-basement.md#map-neighboring-ground-and-construction-dependencies), [buried control functions](references/ground-and-basement.md#keep-support-soil-retention-and-water-control-distinct) |
| Directional frame action, open ground story or grid/component/joint dimensions | [Frame and stability](references/frame-and-core.md#choose-frame-and-stability-action-with-the-plan), [physical coordination](references/frame-and-core.md#separate-coordination-pitch-component-and-occupied-clearance) |
| Shaft versus cabin/landing, lift head/pit or machinery and independent core access | [Equipment envelope](references/frame-and-core.md#fit-vertical-equipment-and-maintenance-with-the-core), [continuous core journey](references/frame-and-core.md#carry-core-routes-and-support-through-every-level) |
| Timber bearing, hanger, stacked/flush roof depth or visible joint | [Support topology](references/timber-and-joints.md#choose-support-topology-and-visible-expression-together), [assembly and replacement](references/timber-and-joints.md#reserve-assembly-and-replacement-access) |
| Timber/glazing or masonry movement; exposed timber end/base | [Differential movement](references/timber-and-joints.md#coordinate-grain-and-differential-movement), [weathering and bases](references/timber-and-joints.md#keep-exposed-ends-and-bases-able-to-shed-water-and-dry) |
| Maintenance journey, intervention quantities or equivalent-function cost over time | [Complete maintenance journey](references/operation-and-lifecycle.md#trace-a-complete-maintenance-journey), [architectural takeoff](references/operation-and-lifecycle.md#count-the-architectural-work), [dated event comparison](references/operation-and-lifecycle.md#compare-equivalent-function-over-time) |
| Inclusive journeys and everyday/emergency spatial conflicts | [Spatial coordination](references/space/circulation/inclusive-and-emergency-interfaces.md#inclusive-use-and-fire-spatial-coordination) |
| Source applicability, accessibility, fire and jurisdiction selection | [Requirements](references/requirements.md) |
| Normative source selection for the project's actual jurisdiction | [Jurisdiction modules](references/normative/index.md), selected through [requirements](references/requirements.md#select-a-jurisdiction-module); for confirmed Russia, [conditional design adaptations](references/normative/ru/applicability.md#choose-the-area-and-capacity-basis) |
| Fixed/variable inputs, constraints and comparison | [Decision frame](references/computational-design.md#frame-the-question), [consistent comparison](references/computational-design.md#compare-options-consistently) |
| Uncertainty, data or a misleading spatial proxy | [Sensitivity](references/computational-design.md#test-sensitivity-and-reproducibility), [data screening](references/computational-design.md#screen-data-before-translating-it-into-design), [access graph](references/computational-design.md#check-adjacency-and-access-as-separate-relationships) |
| Reconcile a design decision across requested outputs | [Design issue coordination](operations/documentation.md#coordinate-a-design-issue) |
| Sufficient evidence for the requested issue, schedule changes, precision or final readiness | [Requested-use adequacy](references/design-completion.md#derive-evidence-for-the-requested-use), [schedule meaning](references/design-completion.md#reconcile-schedule-membership-and-field-meaning), [precision](references/design-completion.md#match-precision-to-the-decision), [revision closure](references/design-completion.md#close-the-revision-and-state-remaining-conditions) |
| Develop plan/section/elevation, diagnose and redesign a weak proposal | [Design development](references/design-development.md) |
| Requested presentation, optional visual techniques, inspection and precision | [Visual delivery](references/visual-delivery.md) |
| Supported calculators, exact schemas, units and all 14 adoption decisions | [Calculators](references/calculators.md) |
| Pinned source-to-target map and exclusions | [Sources](references/sources.md) |
| Borrowed-material permissions | [Third-party notices](THIRD_PARTY_NOTICES.md) |

For general methods, use the reference Contents or current heading inventory to
select the question. Read the selected method through its next peer heading,
including assumptions, procedure, checks, example and source limits; recover
truncated output before relying on it. Do not load every method for a bounded
change. Read calculator source only for debugging/modification; its contract and help own normal use. Do not load all source packs or references merely to become familiar with architecture.

For normative source work, select the project's jurisdiction module through
[requirements](references/requirements.md#select-a-jurisdiction-module), then use
its matching task route to select individual record anchors. Apply [complete selective reading](references/requirements.md#complete-selective-reading): retrieve each selected record to its boundary and recover any truncated output before relying on it. Do not print entire thematic files as the default retrieval step.

## Tools

From this skill directory:

```bash
python3 scripts/calculators.py --help
python3 scripts/check_skill.py
python3 -m unittest discover -s scripts -p 'test_*.py'
```

The standard-library Python 3 calculators provide explicit JSON-in/JSON-out preliminary area, solar-geometry, glazing-geometry and homogeneous-layer U-value calculations. Read [their contract](references/calculators.md) before selecting a method. No general daylight-factor prediction, thermal-bridge analysis, code compliance or full simulation is implied.

The skill checker guards structure, links and bounded top-level table continuity;
it is not a complete Markdown renderer or an architectural correctness check.
Inspect a requested artifact in its actual delivered form through Presentation.

## Completion and integration

Deliver the design decision, its reason, requested artifacts, relevant checks and unresolved limits. For revisions, identify changed decisions and their consequences. For comparisons, expose hard-constraint failures before preference rankings.

When sufficiency for an intended issue or a completed revision is the question,
select the relevant [completion method](references/design-completion.md#derive-evidence-for-the-requested-use).
Deliverability for that stated use does not establish construction readiness,
regulatory approval or reliability for every project. Preserve conditional
conclusions and the exact remaining evidence needed by dependent decisions.

On repository integration, retain internal resources, source revision and notices. Put project adaptations in existing project instructions/data while preserving shared contracts. Source authority, Issue lifecycle and delegation remain with their applicable Level-1 owners.
