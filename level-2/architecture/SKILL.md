---
name: architecture
description: Develop, revise, compare, present and review architectural designs through functional programs, spatial planning, composition, styles, materials and bounded analysis. Apply only when explicitly instructed to use architecture. Follow the user's chosen deliverable and format; concepts may be textual. Building/BIM/3D/mesh authoring belongs to a separate modeling task.
---

# Architecture

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

- Architecture owns purpose, program, composition, spatial organization, stylistic direction, facade/material intent and evaluation of design alternatives. Use numbers and 2D representations to support those decisions.
- Separate source-backed normative requirements, project requirements, provisional assumptions, performed calculation results and design judgments. Retain their source, units, applicability and uncertainty. An attractive image or successful tool exit does not prove a design decision correct.
- Keep project facts, dimensions, site/software profiles, source selections and accepted decisions in the project's existing authoritative material. Reuse its structure; do not create a second project/process framework.
- Establish jurisdiction and applicable source versions explicitly. Unknown jurisdiction allows independent design exploration, with normative conclusions left open. Do not infer location from language/currency or apply foreign-code defaults. Use [requirements](references/requirements.md) for applicability checks.
- Define area/occupancy/performance metrics before comparing them. Geometric area, GFA/GIA/NIA and local legal area definitions are not interchangeable. Record conversion assumptions and reject ambiguous units or incompatible definitions.
- Describe styles by composition, proportion, spatial character, material/facade treatment and contextual fit. Use no biographies, historical surveys or person-centered routing.
- Identify contradictions between fixed requirements before claiming a feasible solution. Show the incompatible constraints, continue independent work and identify the decision needed to proceed; do not silently relax a requirement.
- Follow the user's chosen deliverable and format for the current task. A concept request may be answered in text when no artifact is requested. Do not impose an image/file, a preset format or an automatic SVG default. Produce and appropriately inspect any requested artifact; clarify an unspecified format only when necessary to complete that deliverable. Identify diagrammatic, dimensionally controlled and illustrative content honestly.
- Choose checks proportional to uncertainty and stage. Distinguish a prepared method, an attempted execution and usable results. Report unavailable tools, invalid inputs or failed runs without inventing results.

## Design and modeling boundary

Do not create/edit a building, BIM, 3D or mesh model, implement Revit/Dynamo/Grasshopper workflows, or activate a modeling MCP through this skill. Architectural coordination may reserve spaces, state interfaces and compare design intent in 2D. It does not size engineering systems or establish a building model.

For a later explicit modeling task, hand off the accepted geometry/dimensions, program, coordinate/orientation assumptions, materials, decisions and unresolved interfaces. Modeling belongs to `revit-scripting` under its own explicit invocation and execution contract; do not automatically invoke another Level-2 skill. A raster illustration is not a measured model.

## Load knowledge by question

| Question | Reference |
| --- | --- |
| Activities, concurrent demand and room program | [Program demand](references/program-and-space.md#what-activities-and-capacity-must-the-program-accommodate) |
| Room fit, plan families, floors and cores | [Planning and section](references/planning-and-section.md) |
| Area boundary, allowances and double counting | [Area accounting](references/program-and-space.md#how-can-areas-be-counted-once-and-compared) |
| Adjacency, access and people/goods routes | [Relationships](references/program-and-space.md#which-relationships-must-the-plan-satisfy), [movement](references/program-and-space.md#how-do-people-and-goods-move-through-access-zones) |
| Floors, adaptability or a bounded layout change | [Vertical organization](references/program-and-space.md#how-should-the-program-occupy-floors-and-adapt-over-time), [local revision](references/program-and-space.md#how-should-a-bounded-revision-or-comparison-be-judged) |
| Site, arrival and meaningfully different concepts | [Context](references/composition-and-style.md#how-should-the-design-respond-to-site-and-arrival), [partis](references/composition-and-style.md#how-can-different-partis-be-generated-and-compared) |
| Urban edges, outdoor rooms, approach or sloping ground | [Site and context](references/site-and-context.md) |
| Mass/void, hierarchy, style or material expression | [Massing](references/composition-and-style.md#how-should-mass-and-void-organize-the-site-and-rooms), then the matching composition Contents question |
| Light, view, noise and ventilation trade-offs | [Daylight](references/performance-and-coordination.md#daylight-view-and-occupied-comfort), [acoustic paths](references/performance-and-coordination.md#acoustic-paths-and-ventilation-choices) |
| Envelope junctions, durability or engineering space | [Continuity](references/performance-and-coordination.md#climate-exposure-and-envelope-continuity), [maintenance](references/performance-and-coordination.md#durability-and-maintenance-of-materials), [reservations](references/performance-and-coordination.md#structure-and-services-reservations) |
| Envelope system selection and assembly/junction intent | [Envelope and assemblies](references/envelope-and-assemblies.md) |
| Inclusive journeys and everyday/emergency spatial conflicts | [Spatial coordination](references/performance-and-coordination.md#inclusive-use-and-fire-spatial-coordination) |
| Source applicability, accessibility, fire and jurisdiction selection | [Requirements](references/requirements.md) |
| Normative source selection for the project's actual jurisdiction | [Jurisdiction modules](references/normative/index.md), selected through [requirements](references/requirements.md#select-a-jurisdiction-module); for confirmed Russia, [conditional design adaptations](references/normative/ru/applicability.md#choose-the-area-and-capacity-basis) |
| Fixed/variable inputs, constraints and comparison | [Decision frame](references/computational-design.md#frame-the-question), [consistent comparison](references/computational-design.md#compare-options-consistently) |
| Uncertainty, data or a misleading spatial proxy | [Sensitivity](references/computational-design.md#test-sensitivity-and-reproducibility), [data screening](references/computational-design.md#screen-data-before-translating-it-into-design), [access graph](references/computational-design.md#check-adjacency-and-access-as-separate-relationships) |
| Reconcile a design decision across requested outputs | [Design issue coordination](operations/documentation.md#coordinate-a-design-issue) |
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

## Completion and integration

Deliver the design decision, its reason, requested artifacts, relevant checks and unresolved limits. For revisions, identify changed decisions and their consequences. For comparisons, expose hard-constraint failures before preference rankings.

On repository integration, retain internal resources, source revision and notices. Put project adaptations in existing project instructions/data while preserving shared contracts. Source authority, Issue lifecycle and delegation remain with their applicable Level-1 owners.
