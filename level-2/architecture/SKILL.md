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

Open a known local method or section directly. Otherwise select the relevant subject in the [knowledge and coverage overview](references/index.md), then read one complete method with its conditions, examples and checks. Follow only the dependencies material to this decision; reuse loaded material rather than recursively reading the graph. The overview distinguishes canonical owners, partial coverage and source-only material. A route is not proof of complete architectural competence.

Operations select the requested activity; subject methods supply architectural knowledge. Typologies, styles and cases reuse those methods. Neither every ancestor nor the complete source ledger is a prerequisite. For a whole-design request, synthesize the relevant program, geometry, form, construction and occupied conditions; a local request stays bounded by its affected interfaces.

For normative work, establish the actual jurisdiction through [requirements](references/requirements.md#select-a-jurisdiction-module), then select individual record anchors. Apply [complete selective reading](references/requirements.md#complete-selective-reading): read each chosen record to its boundary and recover truncated output before relying on it. Do not default an unknown jurisdiction to Russia or print entire thematic files as the default retrieval step.

## Tools

From this skill directory:

```bash
python3 scripts/calculators.py --help
python3 scripts/check_skill.py
python3 -m unittest discover -s scripts -p 'test_*.py'
```

The standard-library Python 3 calculators provide explicit JSON-in/JSON-out preliminary area, solar-geometry, glazing-geometry and homogeneous-layer U-value calculations. Read [their contract](references/calculators.md) before selecting a method. No general daylight-factor prediction, thermal-bridge analysis, code compliance or full simulation is implied.

The skill checker guards structure, links, ambiguous headings, runtime reachability
and bounded top-level table continuity. Its graph output is derived diagnostics,
not a reading order, complete Markdown renderer or architectural correctness check.
Inspect a requested artifact in its actual delivered form through Presentation.

## Completion and integration

Deliver the design decision, its reason, requested artifacts, relevant checks and unresolved limits. For revisions, identify changed decisions and their consequences. For comparisons, expose hard-constraint failures before preference rankings.

When sufficiency for an intended issue or a completed revision is the question,
select the relevant [completion method](references/methods/completion.md#derive-evidence-for-the-requested-use).
Deliverability for that stated use does not establish construction readiness,
regulatory approval or reliability for every project. Preserve conditional
conclusions and the exact remaining evidence needed by dependent decisions.

On repository integration, retain internal resources, source revision and notices. Put project adaptations in existing project instructions/data while preserving shared contracts. Source authority, Issue lifecycle and delegation remain with their applicable Level-1 owners.
