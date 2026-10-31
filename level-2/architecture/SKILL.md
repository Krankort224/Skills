---
name: architecture
description: Develop, revise, compare, present and review architectural designs through functional programs, spatial planning, composition, styles, materials and bounded analysis. Apply only when explicitly instructed to use architecture. Follow the user's chosen deliverable and format; concepts may be textual. Building/BIM/3D/mesh authoring belongs to a separate modeling task.
---

# Architecture

## Choose the operation

Start at the requested operation. Read its procedure and only the reference sections needed for that decision. Operations are selectable activities, not a compulsory sequence or executor roles. Reuse supplied project information and accepted decisions.

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
| Program, typology, areas, adjacency, circulation | [Program and space](references/program-and-space.md) |
| Organizing idea, proportion, styles and comparison | [Composition and style](references/composition-and-style.md) |
| Envelope, material, daylight/solar/acoustic intent and engineering interfaces | [Performance and coordination](references/performance-and-coordination.md) |
| Source applicability, accessibility, fire and Russian SP/GOST route | [Requirements](references/requirements.md) |
| Parameters, constraints, data quality, alternatives and sensitivity | [Computational design](references/computational-design.md) |
| Requested presentation, optional visual techniques, inspection and precision | [Visual delivery](references/visual-delivery.md) |
| Supported calculators, exact schemas, units and all 14 adoption decisions | [Calculators](references/calculators.md) |
| Pinned source-to-target map and exclusions | [Sources](references/sources.md) |
| Borrowed-material permissions | [Third-party notices](THIRD_PARTY_NOTICES.md) |

Read calculator source only for debugging/modification; its contract and help own normal use. Do not load all source packs or references merely to become familiar with architecture.

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
