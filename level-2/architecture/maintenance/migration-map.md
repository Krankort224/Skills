# Architecture migration map — Issue 10, Stage B

Status: proposed, not executed or accepted. This map accounts for the 67 files at `d260c6cb845734f9fe2e7a86bc1ca97cc1f46e72`. It does not authorize an executor to skip the combined A+B review or to begin later passes automatically.

All paths are relative to `level-2/architecture/`. Future paths are code literals, not live links. Existing content remains at its baseline locations during A+B. See [inventory](knowledge-inventory.md) and [target design](knowledge-design.md).

## Contents

- [Actions and stage boundaries](#actions-and-stage-boundaries)
- [Complete file disposition](#complete-file-disposition)
- [Pilot section map](#pilot-section-map)
- [Shared owners and content preservation](#shared-owners-and-content-preservation)
- [Inbound references and atomic changes](#inbound-references-and-atomic-changes)
- [Source and case migration](#source-and-case-migration)
- [Execution order and acceptance evidence](#execution-order-and-acceptance-evidence)

## Actions and stage boundaries

`Keep` preserves the path and method; later exact internal-link rewrites do not imply permission to change its claims. `Move` relocates the complete method with its examples and limits. `Split` maps named substantive sections to owners. `Merge` reconciles overlapping knowledge into an existing owner while preserving unique reasoning. `Replace navigation` replaces a redundant index, not its underlying knowledge. No baseline item has an unexplained deletion or an unresolved destination.

C implements the three pilot decompositions and the necessary link-only, shared-owner and checker adjustments. D implements the remaining approved paths and navigation. E consolidates source provenance and addresses demonstrated local-knowledge gaps. F develops reviewed depth increments. A+B changes only the three maintenance documents, none of the 67 baseline files.

Moves of a multi-method document initially preserve section-level nodes. This deliberately avoids pretending that every nonpilot method was deeply re-audited during A. Further splitting requires a demonstrated independent question, preserved conditions and an updated reviewed map; a directory move alone is not counted as increased knowledge depth.

## Complete file disposition

| Baseline file | Disposition and destination | Stage and preservation |
| --- | --- | --- |
| `SKILL.md` | Keep path; retarget pilot links in C; compact subject entry in D | Preserve eight operations, compositional capability principle, evidence and deliverable rules |
| `THIRD_PARTY_NOTICES.md` | Keep; retarget consolidated provenance links in E | Preserve full required license/attribution text and distinctions for unlicensed source media |
| `agents/openai.yaml` | Keep | Preserve name, invocation policy and loader metadata |
| `assets/compact-fit-study.json` | Keep | Preserve exact example geometry/data |
| `assets/family-fit-study.json` | Keep | Preserve exact example geometry/data |
| `assets/styles/art-nouveau/casa-batllo/analysis.md` | Keep | Rewrite internal links in D; source-ID consolidation in E without losing inspected/uninspected distinctions |
| `assets/styles/baroque/san-carlo-alle-quattro-fontane/analysis.md` | Keep | Same case-preservation contract |
| `assets/styles/brutalism/barbican/analysis.md` | Keep | Same; retain site-guidance and non-survey limitations |
| `assets/styles/classical/pantheon/analysis.md` | Keep | Same; preserve attribution uncertainty |
| `assets/styles/gothic/chartres-cathedral/analysis.md` | Keep | Same; inaccessible plans must not become inspected evidence |
| `assets/styles/modernism/villa-savoye/analysis.md` | Keep | Same; preserve mirror status and rejected chronology until verified replacement |
| `assets/styles/organic/fallingwater/analysis.md` | Keep | Same; preserve original-versus-later-intervention distinctions |
| `assets/styles/renaissance/villa-rotonda/analysis.md` | Keep | Same; published plate is not silently relabeled as as-built survey |
| `operations/analysis.md` | Keep; retarget selected methods | C/D, operation meaning unchanged |
| `operations/brief.md` | Keep; retarget selected methods | C/D, operation meaning unchanged |
| `operations/concept.md` | Keep; retarget selected methods | C/D, operation meaning unchanged |
| `operations/development.md` | Keep; retarget selected methods | C/D, operation meaning unchanged |
| `operations/documentation.md` | Keep; retarget selected methods | C/D; keep issued-decision reconciliation owned here |
| `operations/optimization.md` | Keep; retarget selected methods | C/D, operation meaning unchanged |
| `operations/presentation.md` | Keep; retarget selected methods | C/D; no forced representation format |
| `operations/review.md` | Keep; retarget selected methods | C/D, operation meaning unchanged |
| `references/building-use-families.md` | Split into `references/typologies/index.md`, `housing/shared-domestic.md`, `learning.md`, `libraries.md`, `short-stay.md`, `mixed-use.md` under that branch | D; family selection in index, each complete family in its leaf, shared-interface method and mixed-use correction together in `mixed-use.md`; source conditions follow each affected leaf |
| `references/calculators.md` | Keep path and exact supported interface | C/D links only; E may consolidate provenance, not change four tool schemas or 14 adoption decisions |
| `references/composition-and-style.md` | Split by pilot map | C; no knowledge-only redirect copy after inbound links are repaired |
| `references/computational-design.md` | Move to `references/methods/comparison.md` | D; preserve each question, alternative generation, sensitivity, data and access-graph examples |
| `references/design-completion.md` | Move to `references/methods/completion.md` | D; keep sufficiency, schedule semantics, precision and closure independently addressable |
| `references/design-development.md` | Move to `references/methods/design-development.md` | D; preserve coordinated R0/R1/R2 reasoning and requested-change propagation |
| `references/dwelling-fit.md` | Move to `references/typologies/housing/dwelling-fit.md` | D; preserve both worked cases and links to unchanged exact JSON data |
| `references/envelope-and-assemblies.md` | Merge pilot enclosure-continuity material into existing control-function owner in C; move complete result to `references/construction/envelope/assemblies.md` in D | Preserve functions, climate/use conditions, four junctions, replacement logic and unique balcony/penetration reasoning |
| `references/environmental-operating-modes.md` | Move to `references/performance/comfort/operating-states.md` | D; keep coupled-state example, controls, changeover and failure conditions together |
| `references/existing-building-adaptation.md` | Move to `references/construction/existing/adaptation.md` | D; preserve survey uncertainty, retain/repair/replace, substrate and occupied-stage methods |
| `references/frame-and-core.md` | Move to `references/construction/structure/frame-and-core.md` | D; retain support/core/equipment dependencies and section-level direct entry |
| `references/ground-and-basement.md` | Move to `references/construction/structure/ground-and-basement.md` | D; preserve program, neighbor/support, buried-water distinctions and conditional example |
| `references/housing-and-court.md` | Move to `references/typologies/housing/access-and-court.md` | D; no general movement-method duplication |
| `references/knowledge-map.md` | Replace navigation with `references/index.md` and populated branch indexes | D; preserve coverage gaps and ownership distinctions, not two parallel complete catalogues |
| `references/normative/index.md` | Keep | Preserve jurisdiction selection and implemented-module identity |
| `references/normative/ru/applicability.md` | Keep; exact changed internal targets only | C/D; preserve legal facts, applicability mechanisms, verification limits and external URLs |
| `references/normative/ru/building-typologies.md` | Keep | Normative content unchanged; link-only repairs if actually affected |
| `references/normative/ru/environment-and-interfaces.md` | Keep | Same normative-preservation rule |
| `references/normative/ru/federal-framework.md` | Keep | Same normative-preservation rule |
| `references/normative/ru/fire-and-accessibility.md` | Keep | Same normative-preservation rule |
| `references/normative/ru/index.md` | Keep | Same normative-preservation rule |
| `references/normative/ru/routes.md` | Keep | Same normative-preservation rule |
| `references/normative/ru/territory-and-special-conditions.md` | Keep | Same normative-preservation rule |
| `references/operation-and-lifecycle.md` | Move to `references/performance/lifecycle/intervention-and-cost.md` | D; keep complete maintenance journeys, intervention, quantities and event-comparison methods |
| `references/performance-and-coordination.md` | Split and narrowly merge by pilot map | C; preserve all failed/revised conditions and numerical meanings |
| `references/planning-and-section.md` | Move complete method family to `references/space/planning/room-floor-and-section.md` | D; retain general room-fit ownership, nested clear-area example, floor/section methods and all coupled studies; no automatic extra split |
| `references/program-and-space.md` | Split by pilot map | C; keep operating-demand versus normative-population distinction |
| `references/quarter-and-public-space.md` | Move to `references/context/urban/quarter-and-public-space.md` | D; preserve open-space, address, ground, journey, phase and seasonal methods as addressable sections |
| `references/requirements.md` | Keep path | Shared legal applicability and selective reading remain stable |
| `references/roof-and-span.md` | Move to `references/construction/structure/roof-and-span.md` | D; preserve separate support, restraint, thermal-boundary and roof-water questions, with cross-links to enclosure |
| `references/site-and-context.md` | Move to `references/context/site/site-and-context.md` | D; physical edge/topography mechanisms remain distinct from the pilot's translation of site cues into a parti |
| `references/sources.md` | Split provenance into `sources/index.md`, `sources/upstream-packs.md`, `sources/library.md`, `sources/precedents.md` | E; source identities/read extents/adaptation and exclusions survive; normative-evidence explanation links to existing normative owners |
| `references/spatial-composition.md` | Move to `references/space/planning/spatial-relationships.md` | D; keep containment/overlap/linking-space/path/sequence mechanisms and correction example |
| `references/stair-section.md` | Move to `references/space/vertical/stair-section.md` | D; walking profile, repair and full conditional return-stair example remain together |
| `references/style-and-precedent-methods.md` | Move to `references/composition/styles/precedent-transfer.md` | D; retain evidence-first classification and changed-brief transfer |
| `references/style-baroque-and-art-nouveau.md` | Move to `references/composition/styles/baroque-art-nouveau.md` | D; preserve distinct profiles, variations, comparison and evidence limits |
| `references/style-classical-gothic-renaissance.md` | Move to `references/composition/styles/classical-gothic-renaissance.md` | D; preserve each profile as an independently linked section |
| `references/style-directions.md` | Move/adapt to `references/composition/styles/index.md` | D; one selector, declared perimeter and case routes, not a second root |
| `references/style-modern-organic-and-brutalist.md` | Move to `references/composition/styles/modern-organic-brutalist.md` | D; preserve breadth caveats and exact case relationships |
| `references/timber-and-joints.md` | Move to `references/construction/materials/timber-and-joints.md` | D; preserve grain, wetting, support/fastener access, temporary support and terrace variants |
| `references/visual-delivery.md` | Move to `references/methods/visual-delivery.md` | D; retain optional formats, precision and actual inspection, without a format mandate |
| `references/wall-floor-and-opening.md` | Move to `references/construction/structure/walls-floors-openings.md` | D; preserve support roles, floor voids, opening envelopes, material movement and worked correction |
| `scripts/calculators.py` | Keep | Implementation and four interfaces unchanged |
| `scripts/check_skill.py` | Keep; update affected path expectations and add focused graph/link checks | C/D, not A+B; no false complete-renderer or architecture-quality claim |
| `scripts/test_calculators.py` | Keep | Preserve numerical/invalid-input regressions |
| `scripts/test_check_skill.py` | Keep; extend for accepted path/link behavior | C/D, not A+B; negative fixtures must fail for the intended reason |

## Pilot section map

The source ranges below are inclusive lines at the pinned baseline. Headings are exact baseline titles. A parent row and its child rows intentionally overlap in ownership but not in content accounting: the parent row covers only its stated line span; every child has its own span. Preserve heading slugs where possible. All ranges from the start to the end of each pilot are accounted for, including introductions and navigation.

### Program and space

Source: `references/program-and-space.md`, 478 lines.

| Source lines and heading | Destination | Treatment |
| --- | --- | --- |
| 1–12 — title, purpose, shared context and source limits | Each selected Program/Space leaf as relevant | Carry essential input/example conditions; common principles remain in root, not verbatim repeated boilerplate |
| 13–21 — Contents | Program and affected branch navigation | Rebuild from actual leaves; old TOC is not substantive method content |
| 22–52 — What activities and capacity must the program accommodate? | `references/program/demand.md` | Preserve complete activity/concurrency decision and inputs |
| 53–70 — Turn an incomplete brief into testable demand | `references/program/demand.md` | Keep as child method with source/status/conflict logic |
| 71–112 — Test shared use as an occupancy and resource timeline | `references/program/shared-use.md` | Separate full method and 09:00–11:00 worked conflict, including changeover, staff, waiting/storage and area caveats |
| 113–134 — Infer the missing program from the use | `references/program/support-program.md` | Preserve use-pattern table, mechanisms and object-based storage derivation |
| 135–197 — Derive a provisional capacity and room envelope | `references/program/capacity-and-room-demand.md` | Preserve demand/physical-envelope connection, six-table example, peak scenarios and host/activity normative distinctions; link to general room-fit owner |
| 198–267 — How can areas be counted once and compared? | `references/program/area-ledger.md` | Preserve metric definitions, counting procedure, Russian metric distinctions and finish-area correction |
| 268–291 — Connect the ledger to geometry | `references/program/area-ledger.md` | Keep with ledger; voids, residuals and geometric fit do not become separate superficial card |
| 292–322 — Which relationships must the plan satisfy? | `references/program/relationships.md` | Preserve relationship meanings and conflict treatment |
| 323–342 — Turn relationships into an organizing scheme | `references/program/relationships.md` | Keep as constructive child; connect to plan families and parti without duplicating them |
| 343–382 — How do people and goods move through access zones? | `references/space/circulation/access-and-closure.md` | Preserve actors, timing, flows, queues, sightlines and route alternatives |
| 383–409 — Make a closed zone a complete boundary | `references/space/circulation/access-and-closure.md` | Keep complete boundary and after-hours support example with the journey method |
| 410–451 — How should the program occupy floors and adapt over time? | `references/program/floors-and-change.md` | Preserve allocation, vertical interfaces, housing/future-state and phase conditions |
| 452–478 — How should a bounded revision or comparison be judged? | `references/methods/bounded-revision.md` | Preserve accepted baseline, affected-neighbor propagation, hard constraints and low-disruption alternatives |

### Composition and style

Source: `references/composition-and-style.md`, 649 lines.

| Source lines and heading | Destination | Treatment |
| --- | --- | --- |
| 1–8 — title and shared program/performance/requirements context | Selected leaves | Preserve required dependencies without forcing all references to load |
| 9–20 — Contents | Composition branch navigation | Rebuild from actual target owners |
| 21–65 — How should the design respond to site and arrival? | `references/context/site/arrival-and-setting.md` | Own selection of consequential site cues and their translation into a parti; physical edge/topography methods stay at the existing site owner |
| 66–95 — How can different partis be generated and compared? | `references/composition/massing/parti.md` | Preserve alternative-generation and discriminating comparison method |
| 96–137 — Organizational types are working hypotheses | `references/composition/massing/parti.md` | Keep seven-family mechanisms, failures, hybrid conditions and worked choice with parent method |
| 138–170 — How should mass and void organize the site and rooms? | `references/composition/massing/mass-and-void.md` | Preserve equal-assumption comparison and occupied void testing |
| 171–214 — What the massing operations change | `references/composition/massing/mass-and-void.md` | Keep add/carve/step/split mechanisms, effects, example and physical-performance caveats |
| 215–244 — How can section generate form? | `references/composition/massing/section-form.md` | Preserve strategy table and mutual plan/section consequences |
| 245–275 — How can scale, hierarchy and rhythm support the idea? | `references/composition/facade/hierarchy-and-rhythm.md` | Preserve use-grounded prominence, person/building/context scales, exceptions and test |
| 276–324 — Derive an elevation from occupied bays | `references/composition/facade/occupied-bays.md` | Full opening-order table, corner/end behavior, nominal panel distinctions and fabrication-evidence limits; restore necessary parent inputs |
| 325–371 — How can a requested style become design decisions? | `references/composition/styles/character-to-decisions.md` | Preserve experiential traits, alternatives, evidence and changed-brief transfer links |
| 372–387 — Coherent character can be produced by different traits | `references/composition/styles/character-to-decisions.md` | Keep trait table and tensions with the method |
| 388–434 — How should materials express and support the design? | `references/composition/material-expression.md` | Preserve complete role/appearance/assembly choice, alternatives and junction check |
| 435–473 — Material and tectonic vocabulary | `references/composition/material-expression.md` | Keep actual/apparent role, unit/joint/grain/weathering distinctions; link to durability and assembly owners |
| 474–481 — Worked progressions and common hypothetical-study conditions | The three study assets below | Carry this essential qualifier into each extracted study; they are not legal minima or source designs |
| 482–529 — A corner community building: public presence and a quiet garden | `assets/studies/corner-community-building.md` | Preserve L/compact geometry, independent-use failure, revised gallery and all remaining inputs |
| 530–591 — A sloping library: shared reading, quiet work and an ordered facade | `assets/studies/sloping-library.md` | Preserve level/sill failure, revised allocation, module mismatch and all conditional interfaces |
| 592–641 — Two Russian reading pavilions: climate and use change the edge | `assets/studies/reading-pavilions.md` | Preserve both study contexts, comparison table and unknown parcel/current-design-parameter conditions; not a city-wide rule |
| 642–649 — Method sources | Internal provenance pointers in receiving methods/studies | Preserve adapted/rejected/source-limit meaning; exact source records remain in `references/sources.md` until E |

### Performance and coordination

Source: `references/performance-and-coordination.md`, 481 lines.

| Source lines and heading | Destination | Treatment |
| --- | --- | --- |
| 1–15 — title, scope and hypothetical-input conditions | Selected methods and both study assets | Retain evidence limits as method conditions, not new restrictions on the agent's tools or expertise |
| 16–28 — Contents | Relevant branch navigation | Rebuild from actual owners |
| 29–37 — Daylight, view and occupied comfort | `references/performance/comfort/daylight-view.md` | Preserve occupied-position input frame |
| 38–55 — Generate room and section schemes | `references/performance/comfort/daylight-view.md` | Keep complete schemes/conflicts table with parent |
| 56–82 — Separate sun, sky, view and control | `references/performance/comfort/daylight-view.md` | Keep distinctions, finite/oblique shading, deployed/retracted control and next-check meaning |
| 83–109 — Fit Russian room conditions without merging their tests | `references/performance/comfort/daylight-view.md` | Preserve conditional applicability and unresolved numerical/primary-text limits; normative record content is not imported |
| 110–118 — Acoustic paths and ventilation choices | `references/performance/comfort/acoustics-and-air.md` | Preserve source/path/receiver and distinct sound mechanisms |
| 119–136 — Make a spatial response to each path | `references/performance/comfort/acoustics-and-air.md` | Keep response/failure table and room-acoustics qualifications |
| 137–156 — Choose a credible operating mode | `references/performance/comfort/acoustics-and-air.md` | Keep natural/mechanical/mixed mode, complete air path and control-state dependency with acoustic method |
| 157–186 — Climate, exposure and envelope continuity | Existing `references/envelope-and-assemblies.md`, control-function method | Merge in C into `#assign-control-functions-before-drawing-layer-order`, using a clearly named child section for interface tracing; retain climate/use dependency and unique balcony/penetration example. Whole owner moves in D |
| 187–222 — Durability and maintenance of materials | `references/performance/lifecycle/durability.md` | Keep exposure mechanisms, table, functional comparison basis and distinct assembly-removal/whole-journey links |
| 223–224 — Structure and services reservations heading | Two receiving methods below | Retain conceptual-reservation context; no empty heading-only target |
| 225–251 — Choose support logic with the plan | `references/construction/structure/support-concepts.md` | Preserve comparative support-family table and continuous support/stability inputs; detailed frame/roof mechanisms remain at their owners |
| 252–294 — Budget the section and routes | `references/space/vertical/section-and-services.md` | Preserve full clear-height equation and inclusion definitions, overlap/crossing alternatives, distribution and replacement paths |
| 295–334 — Inclusive use and fire spatial coordination | `references/space/circulation/inclusive-and-emergency-interfaces.md` | Preserve real ordinary/maintenance/emergency journey conflicts and project-specific strategy conditions |
| 335–399 — Worked progression: street reading room | `assets/studies/street-reading-room.md` | Preserve all starting inputs, failed height and shading tests, revisions, small margins and remaining checks |
| 400–465 — Worked progression: hall overlaid with services | `assets/studies/hall-services.md` | Preserve column/height coupled failure, revised routing, door/cabinet occupation, arithmetic and conditional result |
| 466–476 — Communicate decisions and uncertainty | `references/methods/bounded-revision.md`, child `Communicate conditions and remaining decisions` | Merge complementary reservation/evidence reasoning into the bounded-revision method; do not create an eleven-line pseudo-skill |
| 477–481 — Method sources | Internal provenance pointers in receiving methods/studies | Preserve local-method versus source-provenance distinction and exact support links |

## Shared owners and content preservation

The only planned substantive shared-owner merge in C outside the three pilots is the enclosure-continuity material into the existing assembly reference. The existing owner already explains rain/drainage, air, thermal and vapor/drying functions, climate/use reversals and connected junctions. Preserve the pilot's interface tracing and balcony alternatives rather than duplicate the same control-function procedure in a new Performance leaf. Its destination can initially be a named child under the existing control-function heading, so existing inbound targets remain stable.

Other overlap is handled by exact cross-links and explicit distinction, not opportunistic deletion. The general room-fit method remains in `planning-and-section` during C. Program's capacity example must retain its demand/concurrency role. Material expression keeps sensory/tectonic decisions; durability keeps exposure mechanisms; generic removal stays in assemblies; the whole worker/piece/waste journey stays in lifecycle. Support-concept comparison does not replace detailed frame, roof or timber reasoning.

For each extracted leaf, preserve the method-specific inputs and qualifications that were previously inherited from a parent heading or document introduction. A short reminder of essential conditions is allowed; a copied competing procedure is not. All numerical study inputs must remain explicitly hypothetical. Do not transfer historical drawings, source images or project data merely because their case text moves.

The source span ledger is the preservation authority for C. A reviewer should be able to select any line range above and find its retained reasoning at the destination. Tables, formulas, negative cases and caveats count as content. Navigation may be regenerated; deleting a caveat as repetitive requires semantic review rather than a mechanical word-count argument.

## Inbound references and atomic changes

The exact inbound sets below were measured at the baseline, excluding each pilot's own TOC. A source file can link to several different pilot sections, so a filename replacement alone is insufficient. Resolve each original target fragment through the section map and make the link relative to its new source location.

### Program inbound set — 20 files

```text
SKILL.md
operations/brief.md
operations/development.md
operations/documentation.md
references/building-use-families.md
references/composition-and-style.md
references/computational-design.md
references/design-completion.md
references/design-development.md
references/existing-building-adaptation.md
references/frame-and-core.md
references/knowledge-map.md
references/normative/ru/applicability.md
references/performance-and-coordination.md
references/planning-and-section.md
references/quarter-and-public-space.md
references/requirements.md
references/sources.md
references/spatial-composition.md
references/style-and-precedent-methods.md
```

### Composition inbound set — 11 files

```text
SKILL.md
operations/concept.md
operations/optimization.md
operations/presentation.md
references/knowledge-map.md
references/normative/ru/applicability.md
references/performance-and-coordination.md
references/program-and-space.md
references/site-and-context.md
references/sources.md
references/style-and-precedent-methods.md
```

### Performance inbound set — 19 files

```text
SKILL.md
operations/analysis.md
operations/concept.md
operations/development.md
operations/documentation.md
references/building-use-families.md
references/composition-and-style.md
references/design-development.md
references/envelope-and-assemblies.md
references/housing-and-court.md
references/knowledge-map.md
references/normative/ru/applicability.md
references/operation-and-lifecycle.md
references/program-and-space.md
references/quarter-and-public-space.md
references/requirements.md
references/site-and-context.md
references/sources.md
references/wall-floor-and-opening.md
```

For whole-file links without a fragment, inspect the surrounding question. Replace with the relevant leaf or a useful branch index; do not send every old link to one generic index. For an intentionally multi-question reference, use more than one precise target only when its context needs them.

C must also update the checker's required-reference expectations for the three removed flat pilot files. Do not edit the issue-wide root README to make this happen; the task is skill-scoped. Preserve the fixed normative record count and content except necessary local-link destination strings. A changed fragment is not authorization to refresh legal status or reorder laws.

The final C snapshot is atomic at the repository-tree level: new owners, rewritten inbound links, source-map recipients, affected tests and removal of superseded pilot bodies agree. There is no published intermediate state where both old and new copies claim ownership or references point to absent files. D similarly updates links relative to every newly moved source file, not only links targeting it.

## Source and case migration

Until E, `references/sources.md` stays the provenance owner; C/D only rewrite its local recipient links. Its upstream pins, inspected ranges, bibliographic metadata, exclusions, unread status and history do not disappear because a method was split.

In E, map existing source sections as follows:

| Existing source section | Proposed owner | Preserve |
| --- | --- | --- |
| Pinned sources and reading boundary | `sources/index.md` plus `sources/upstream-packs.md` | A/C identities, exact revisions, treatment vocabulary and narrow-reading limits |
| Program; Composition; Performance; Comparison/data; Documentation coordination | `sources/upstream-packs.md` | Every inspected file/section/line locator, adaptation decision and exact local recipient; source IDs reduce repeated URLs, not cited-document accounting |
| Excluded and unresolved material | Corresponding source-family record | Reasons, unread portions and rejected prescriptions; do not turn them into a generic runtime ban |
| Architecture library and all seven continuation subsections | `sources/library.md` | Catalog revision, title/edition/rights, source paths/hashes, actual file/printed pages, source-specific exceptions and stated unreviewed content |
| Styles and identified objects | `sources/precedents.md` with internal links from unchanged case paths | Primary object/interpretive evidence, exact observations, unavailable media, later alterations and source permissions |
| Russian normative evidence | Short pointer to existing `references/requirements.md` and normative module | Current primary-source and jurisdiction contract; no duplicate normative registry |

Five newly extracted study assets retain all supplied assumptions and revisions, with links back to their operative methods. The existing eight identified-building cases stay where they are. The two JSON dwelling studies stay byte-identical. A method-specific example does not move to `assets/studies/` unless independent reuse actually warrants the separation.

The five study assets are `corner-community-building.md`, `sloping-library.md`, `reading-pavilions.md`, `street-reading-room.md`, and `hall-services.md`. No image, source PDF or tracing is added. Their names and paths are concrete C targets; domain/index pages should link to them only where they illuminate an actual mechanism.

## Execution order and acceptance evidence

1. After A+B acceptance, confirm the branch head and compare architecture-only changes against the pinned baseline. Preserve unrelated inherited repository content; do not merge other ongoing work merely to update this skill.
2. For C, extract complete pilot units according to the line ledger, restore essential parent conditions and perform the two named merges: enclosure tracing into the existing assembly owner, and uncertainty communication into the new bounded-revision owner.
3. Add only indexes needed for these populated leaves. Keep direct known-method entry. Update each inbound fragment, source recipient, moved-study link and checker expectation together; remove superseded pilot bodies once no active dependency remains.
4. Run structural and unit checks, inspect the exact diff, and reconcile every pilot source span. Recalculate the existing study arithmetic and preserve the negative/conditional results. Exercise selected K1–K5 routes from the design as actual local-only method tests; record what was loaded and why the result is supported.
5. Hand C off once with section-level evidence. Do not silently begin D. After D acceptance, perform source-localization E and selected depth increments F under their reviewed boundaries.

A successful migration demonstrates content preservation and better question-to-method access. It does not establish improved architectural competence until the substantive tests show it. A successful A+B package supplies this implementable map and its evidence; it does not claim that these future paths, links or method tests already exist or have passed.
