# Architecture knowledge design — Issue 10, Stage B

Status: A+B design accepted at `4ad750b7733bd828fb1d99d753e48444387f17e3`; C implements only the mapped pilot, pending its own review. Remaining target paths and D–F work below are still design, not an already migrated corpus. This document builds directly on [Stage A evidence](knowledge-inventory.md). The complete disposition and pilot section map are in [migration-map.md](migration-map.md).

Scope remains `level-2/architecture/**`. A+B added maintenance evidence only. Runtime reading follows the actual skill links, never this maintenance proposal; the calculators and normative authority remain unchanged.

## Contents

- [Design decisions](#design-decisions)
- [Subject hierarchy and ownership](#subject-hierarchy-and-ownership)
- [Knowledge-node completeness and granularity](#knowledge-node-completeness-and-granularity)
- [Internal graph contract](#internal-graph-contract)
- [Progressive reading and entry points](#progressive-reading-and-entry-points)
- [Source locality and evidence retention](#source-locality-and-evidence-retention)
- [Migration and verification design](#migration-and-verification-design)
- [Cross-domain acceptance scenarios](#cross-domain-acceptance-scenarios)
- [Depth increments](#depth-increments)
- [Trade-offs and review decisions](#trade-offs-and-review-decisions)

## Design decisions

1. **One substantive skill, two navigation dimensions.** The eight operations describe the requested activity; subject branches supply architectural knowledge. Neither becomes an executor role or an isolated permission boundary. Architectural reasoning can be used with appropriate modeling, computational, document and other tools.
2. **Hierarchy locates knowledge; links express dependencies.** Every reusable method has one canonical home. Typologies, styles, cases and operations connect to it. The hierarchy does not constrain cross-branch links, and a link does not require loading its entire target subtree.
3. **Decompose by independently answerable questions, not length.** Preserve causal explanation, conditions, alternatives, calculations and corrections. A file containing a coherent mechanism may remain long; a short file consisting only of pointers is not automatically a knowledge node.
4. **Prefer complete local explanation to repeated outside reading.** Retain traceable source evidence without making the source ledger a runtime prerequisite. Removing a URL or replacing it with a source ID does not by itself increase autonomy.
5. **No second graph authority.** Authored Markdown and case data own content and relationships. Any future graph JSON, HTML or report is reproducible derived output, excluded from its own indexing corpus. This issue requires no graph server, external inference, Graphify installation or repository-wide context changes.
6. **Preserve knowledge limits, not capability prohibitions.** A geometric check may not establish glare or capacity, but that does not prohibit using a suitable additional method. Keep method-specific validity and actual missing evidence explicit.

## Subject hierarchy and ownership

The target has eight populated subject branches under `references/`, plus the existing normative module. The proposed names follow actual baseline content. Create a deeper directory only when several independently useful children justify it; do not precreate an empty universal taxonomy.

```text
architecture/
  SKILL.md                         operation entry and shared design principles
  operations/                      existing eight operation contracts
  references/
    index.md                       compact subject discovery and coverage summary
    context/                       urban/site relationships
      urban/
      site/
    program/                       demand, temporal resources, area and allocation
    space/
      planning/                    physical room/floor fit and spatial relationships
      circulation/                 routes, closure and inclusive/emergency interfaces
      vertical/                    levels, cores and stairs
    composition/
      massing/                     parti, solids/voids and section-led form
      facade/                      occupied bays, hierarchy and rhythm
      styles/                      character methods and selected directional profiles
    construction/
      structure/                   support topology and openings
      envelope/                    system families, control paths and junctions
      materials/                   material-specific mechanisms and joints
      existing/                    retained fabric and intervention
    performance/
      comfort/                     light, sound/air and coexisting occupied states
      lifecycle/                   degradation, maintenance and equivalent-function costs
    typologies/                    operating-family applications
    methods/                       comparison, development, representation and completion
    normative/                     existing jurisdiction-aware source records
    requirements.md                existing shared normative applicability owner
    calculators.md                 stable interface to the four bundled tools
  assets/
    studies/                       extracted original cross-domain studies when justified
    styles/                        existing identified-building analyses, kept in place
    compact-fit-study.json         existing exact example data, kept in place
    family-fit-study.json          existing exact example data, kept in place
  sources/                         consolidated non-normative provenance records
  scripts/                         existing tools and proportionate integrity tests
  agents/                          existing loader metadata
  maintenance/                     reviewed design/migration evidence, not runtime routing
  THIRD_PARTY_NOTICES.md            authoritative retained notices
```

This refines the earlier proposal: existing `assets/styles` and the two JSON studies do not move merely to obtain a uniform `cases/` tree. A new `assets/studies/` is justified only for cross-domain progressions extracted from the pilots. Single-method examples stay with their methods. No new top-level `knowledge/`, nested skill or generic process framework is needed.

| Branch | Owns | Important interfaces and distinctions |
| --- | --- | --- |
| Context | Actual urban/site relationships, edges, arrival setting, ground use, topography and phases | Program owns demand; Space owns physically usable journeys; normative rights remain selected evidence, not geometry |
| Program | Activities, concurrent resources, supporting functions, area definitions, adjacency requirements and distribution over time/floors | Room construction belongs to Space; adjacency intent is not a fitted connection; statutory population is not operational demand |
| Space | Occupied geometry, furniture/action envelopes, room/floor fit, movement, closure, levels and stairs | Composition owns experienced/formal order; Construction owns actual support/enclosure mechanisms |
| Composition | Parti, mass/void, sectional expression, hierarchy, facade ordering, material expression and style translation | A facade bay is not a panel manufacturing schedule; material appearance is distinct from degradation and assembly performance |
| Construction | Structural/support concepts, enclosure functions, openings, material-specific joints and existing-fabric intervention | Performance supplies exposure and use consequences; actual calculations and measurements substantiate technical claims |
| Performance | Occupied environmental conditions, control-state compatibility, durability and lifecycle comparisons | General enclosure continuity belongs to Construction; this branch does not repeat complete layer/removal procedures |
| Typologies | Actual use-family operating commitments and specialized spatial consequences | Reuse shared demand, room, access, light and construction methods; no duplicated general checklist per building label |
| Methods | Decision framing, alternative comparison, sensitivity, datums, development/correction, representation and evidence sufficiency | Operations decide what activity is requested; methods explain how a reusable reasoning task is performed |

Named ownership collisions to resolve during migration:

- Keep general room-fit at the method now in `planning-and-section`. Program's provisional capacity example remains a demand-to-space example, with the room-fit dependency explicit; it is not silently replaced by a room-area ratio.
- Keep enclosure control functions and generic component replacement at the current assembly owner. Move the Performance excerpt into that owner without losing its balcony/penetration counterexample; retain exposure/durability as a separate method.
- Distinguish facade generation from elevation consistency. Composition owns occupied-bay order; development owns plan/section/elevation reconciliation; Documentation owns issued-recipient consistency.
- Keep material appearance, degradation mechanism, component-removal sequence and whole maintenance journey distinct and linked.
- Keep bounded-change scope separate from physical repair and final revision closure. They are connected decisions, not three copies of one workflow.

## Knowledge-node completeness and granularity

A node answers a named architectural question with sufficient local reasoning for its declared use. A node may be a file or a stable section within a coherent file. The migration map selects boundaries; it does not mandate one file per heading.

A usable node supplies, in a structure appropriate to the subject:

- the decision, relevant terms and physical/operational mechanism;
- necessary inputs, units, definitions and applicability conditions;
- a constructive method, meaningful alternatives and the circumstances changing the choice;
- relevant quantitative relationships with assumptions and validity, where justified;
- a way to test the result, a recognizable failure and a concrete correction;
- an example or counterexample when it reveals something the procedure alone hides;
- exact links to dependent knowledge and concise provenance.

These are completeness questions, not mandatory repeated headings. A theoretical node may need a careful derivation or several diagrams; a material node may need a failure mechanism and junction sequence. Do not compress them into a generic six-field card. Preserve mathematical reasoning and explanatory distinctions, not only numbered actions.

Split when two questions can be selected independently, have different inputs/validity, recur in different tasks, or have distinct canonical owners. Keep together a mechanism and its necessary caveat, a formula and its units, a worked failure and correction, or a tightly coupled calculation that cannot be interpreted on its own. Splitting a child section is justified only after restoring parent context in the destination.

For example, the daylight node retains distinctions among sky, direct sun, view, privacy and shade states together: removing those distinctions would make its advice misleading. A separately reusable solar-geometry calculation can be linked through the calculator contract. Acoustic paths and ventilation modes initially remain one coupled node because the open/closed-window conflict motivates the choice; isolated future acoustic submethods may be split when they become independently substantive.

The three integrated composition studies and two Performance studies become candidate study assets. Their stated hypothetical inputs, all revisions, arithmetic, remaining unknowns and negative cases travel together. They do not become five isolated success illustrations.

## Internal graph contract

Use ordinary relative Markdown links and meaningful link text. The canonical node identity is its path plus an optional stable heading fragment. No mandatory UUID, YAML sidecar, ontology registry or separately maintained edge database is required.

Four relationship labels are sufficient initially:

| Relation | Meaning | Reading consequence |
| --- | --- | --- |
| Requires | An input definition or method needed to use this decision correctly | Load the relevant portion unless already established in task context; state a condition when only some applications require it |
| Affects | A changed choice can alter another decision | Follow when that physical/operational dependency is present; not an instruction to recursively visit every neighbor |
| Verified by | A specified check can test a particular claim | Read its validity and required inputs; naming a check is not executing it or proving every claim |
| Illustrated by | An authored case demonstrates mechanism, failure or transfer | Optional unless the example is needed to understand the method; a successful case is not universal validation |

Express labels in prose or a small relation list/table next to the relevant reasoning. Examples, shown as syntax only because target files do not exist yet:

```markdown
- Requires — [Area boundary](../../program/area-ledger.md): compare the same measured extent.
- Affects — [Occupied daylight](../../performance/comfort/daylight-view.md): moving the opening changes sky and view paths.
- Verified by — [Clear-room fit](room-fit.md): test actual objects, actions and the uninterrupted route.
- Illustrated by — [Street reading room](../../../assets/studies/street-reading-room.md): coupled height, shade and closed-window correction.
```

Navigation, provenance and normative-authority links remain distinguishable from these knowledge relations. A link to an upstream article is evidence, not a `Requires` edge by default. A legal-source link does not establish compliance. Not every ordinary explanatory link needs a type label; do not manufacture relations simply to increase edge counts.

Keep backlinks only where they help a reader. Direction is meaningful: modifying a duct reservation may affect clear height without every clear-height discussion requiring HVAC sizing. Reciprocal `Affects` links are legitimate. A cycle of unconditional `Requires` links should trigger semantic review for an inseparable coupled method or a missing starting assumption; cycles in the whole subject graph are not inherently defects.

For heading stability, preserve baseline slugs during the pilot where possible. When a heading must change, the accepted migration map must give its old-to-new target and every inbound reference must be rewritten. Do not retain indefinitely duplicated methods as compatibility pages. A temporary index is acceptable only with a defined removal point and no competing content owner.

## Progressive reading and entry points

`SKILL.md` retains operation selection, shared reasoning/evidence principles, tool discovery and a compact subject entry. It stops reproducing the entire subject-question table. `references/index.md` replaces the existing central knowledge map as the single overview of subject homes and material coverage gaps. Domain indexes expose useful questions and distinctions, not a copy of every leaf paragraph.

A known method can be opened directly. For an unfamiliar question, select the operation when needed, then a relevant branch and a leaf. Do not require reading each ancestor, every sibling, the full graph or the provenance ledger. At a leaf, load its complete selected reasoning unit and follow only dependencies material to the current decision.

Use a visited set keyed by path/fragment when tool-supported; otherwise reuse already loaded content explicitly. Read the next linked method because a named input or consequence is unresolved, not because it is adjacent. Stop when the needed decision and relevant checks can be made, preserving material unknowns. No numerical hop limit may truncate a genuine dependency; equally, a cyclic relation must not trigger recursive whole-corpus loading.

Indexes can provide substantive orientation, such as distinguishing demand from fit or facade order from physical panelization, but they do not become new owners of those methods. Operations, normative routes and source-maintenance entry points remain independent selections.

## Source locality and evidence retention

Default preference: author a complete local explanation of reusable knowledge, then cite its provenance once at its canonical source record. Do not send an agent to an external document for a compact mechanism that the skill can fully explain.

Use a consolidated non-normative source layout, populated from existing evidence rather than decorative empty files:

```text
sources/
  index.md                  identities, scope and routes to source records
  upstream-packs.md         two pinned repositories, licenses and exact file/line locators
  library.md                books/course materials, editions, paths, hashes and inspected pages
  precedents.md             identified-object/interpretive evidence and case source IDs
```

The actual content may warrant later splitting by source family; use selective headings before another level. Existing source-only and excluded records remain provenance, not hidden claims of knowledge coverage. The normative module retains its own primary-document URLs and version/applicability contract.

Each record preserves source identity, issuer/author where established, edition/revision/date, stable URL when necessary, exact inspected locator, treatment, local method recipients, rights, and unverified/rejected portions. A pinned upstream repository URL plus an exact path and line range is a useful consolidated locator. The audit still counts distinct cited documents, not merely clickable URLs. Preserve both MIT notices unchanged.

A method points internally to its source record. A case owns its observed/reported/inferred distinctions and the limits of inspected images; the source record owns bibliographic identity and original location. Cross-links replace repeated identity paragraphs. Licenses and notices retain any required attribution even when a URL also exists in the source registry.

Retain necessary external access for current law, changeable product or site data, original visual/archival evidence, and material that cannot be faithfully or lawfully represented locally. Local prose must not pretend that the original has been inspected when it has not. Original explanations of ideas are preferred to copying source prose or images. No new source media is imported under this issue merely to reduce link counts.

Localize a missing method by reading a relevant source within permissions, extracting mechanism/conditions, writing an original complete method, adding an original test/counterexample, recording support and exclusions, and testing without obligatory source retrieval. Do not summarize an entire textbook into superficial bullet points and call the topic complete.

For the six PDFs use Stage A's individual dispositions. In particular, distinguish Barbican's site-management guidance from general architectural method, and treat the CUNY-hosted CMN leaflet as an unresolved hosting/provenance issue until an equivalent primary publication is verified. Removing the mirror without preserving the supported observation is not a successful fix.

Pass E reports before/after values for textual occurrences, clickable occurrences, exact URLs, normalized documents, cited works/source families and genuinely necessary external runtime retrievals. It also reports local-only test outcomes. No arbitrary URL quota or reduction percentage is adopted in B.

## Migration and verification design

Pass C implements only the three-pilot decomposition and necessary inbound-link/checker changes. Other files remain at their baseline homes except exact link rewrites and a narrowly justified shared-owner merge. Pass D implements the approved remaining disposition and graph/navigation checks. Pass E localizes missing knowledge and consolidates provenance. Pass F deepens prioritized actual gaps. Each has its normal review gate after the combined A+B gate.

Preservation is section-level, not just word-count equality. For every moved unit verify its question, definitions, input conditions, equations, units, assumptions, alternatives, failure/correction, example state, provenance and limits. Record deliberate merges with source spans and the resulting owner. Differences in wording are reviewable; unexplained disappearance is not. Negative and conditional results survive alongside positive ones.

Mechanical verification should cover:

- relative targets and fragments, image/data resources, duplicate headings, reference-style links, and links in tables;
- active-node reachability separately from metadata, scripts, tests and maintenance/provenance-only documents;
- path/anchor rewrites, including link-only updates inside normative selection pages;
- one owner for each explicitly mapped shared method, with semantic review rather than a claim that string similarity proves duplication;
- legitimate reciprocal relations and bounded traversal; missing/conditional prerequisites;
- unchanged calculator interfaces and numerical regressions; unchanged source notices and normative record semantics;
- changed-path scope and no caches, downloaded source bodies or unrelated commits.

The current checker hardcodes flat reference names. Update those expectations alongside the pilot, not in advance, and add positive/negative fixtures for the changed behavior. Prefer expected root/operation/domain links and concrete mapped content checks to a permanent giant hardcoded file list. The existing four tools do not become simulations through a navigation refactor.

A graph export is optional. If produced, distinguish literal authored links from inferred relations, preserve source revision/scope, exclude maintenance reports from active knowledge metrics, and make regeneration deterministic. Do not claim that an inferred relationship is an authored prerequisite. No graph tooling is required to review this design.

## Cross-domain acceptance scenarios

These are proposed reproducible evaluation specifications, not completed architectural simulations. All numeric values below are hypothetical study inputs inherited from or constructed for the local examples; none is a legal minimum. Run a scenario using the selected local methods, record the exact loaded paths/sections, reasoning, calculations, unresolved claims and requested result. An evaluator checks the causal result, not merely the presence of keywords.

### K1 — Demand, changeover, room fit and support

Ordinary input: two groups of 20 book one room at 09:00–10:00 and 10:00–11:00; clearing/setup needs 15 minutes; one facilitator also serves another activity 09:30–10:30. Expected reasoning identifies both resource conflicts, offers a later second booking or extra room/staff, and traces waiting/storage and support journeys. It must not conclude that adjacent session times prove sharing.

Conflict variant: times, staff count and room count are fixed. Expected result is a demonstrated incompatibility, not an average occupancy or silently shortened changeover. Changed-condition variant: a second room is available but displaced furniture must pass through an occupied room. Retest spatial support and routes rather than declaring the resource problem solved.

Required graph: demand/timeline → physical room fit → access/closure → area ledger. The distinction between operating demand and statutory population survives.

### K2 — Occupied daylight, noise, air and section

Use the street-reading-room study: floor spacing 3.70 m; upper buildup 0.12 m; structure 0.45 m; services 0.40 m; ceiling 0.05 m; required reading height 2.85 m. Expected geometry: 2.68 m, a 0.17 m shortfall. Moving the main services into a separate band and reserving 0.20 m over reading gives 2.88 m, only a conditional 0.03 m margin.

A 0.70 m canopy at a 3.00 m head under an assumed facade-normal 20-degree sun ray shades approximately 0.255 m vertically; it does not control every low sun condition. Closing noisy-side windows requires an actual alternative air path. Upper/lower shade states must retain the intended occupied light/view/privacy relationships.

Conflict variant: engineering increases the reading-zone reservation beyond its nominal margin. Changed-condition variant: a privacy blind is always closed during use. Expected result revisits fit or light/view claims and dependent choices. It must not claim annual glare, air-change or acoustic compliance from geometry.

Required graph: room/section → daylight/view → acoustic/air modes → enclosure head/junction → maintenance access → verification and actual jurisdiction when relevant.

### K3 — Clear-span hall, services and usable circulation

Use the hall study: 4.20 m floor spacing, 0.12 m buildup, 0.45 m structure, 0.50 m services and 0.05 m ceiling give 3.08 m. A frame column still violates the column-free brief. A 0.85 m provisional long-span depth reduces height to 2.68 m; changing the hall service reservation to 0.12 m gives 3.06 m, conditional on actual edge crossings.

With a hypothetical 1.80 m circulation strip, a 1.00 m swinging leaf leaves 0.80 m and a 0.60 m open cabinet leaves 1.20 m. Expected reasoning relocates swing/maintenance occupation rather than treating arithmetic residuals as code limits. A deeper beam cannot be shortened or pierced without support evidence.

Conflict variant: floor levels and side-bar footprint are fixed. Changed-condition variant: an acoustic buffer is proposed as the air-transfer path. Retest simultaneous circulation, noise and service requirements.

Required graph: support concept → section budget → services path → acoustic buffer → ordinary/maintenance/emergency journeys.

### K4 — Facade order, room use, module and light

Four hypothetical 4 m occupied bays form a 16 m frontage with a nominal 1 m panel grid. A centered 1.6 m opening has jambs 1.2/2.8 m from each bay origin. Compare special panels, finer subdivision and a 2 m opening; the latter aligns nominal jambs but must still satisfy furniture, privacy, support, light and junction needs.

Conflict variant: the 1.6 m opening is fixed. Changed-condition variant: a corner or directional material prevents an apparently repeated panel from being interchangeable. Expected response preserves the program and distinguishes nominal grid, finished opening and fabrication tolerance. A clean elevation is not a manufacturing schedule.

Required graph: occupied-bay composition → room fit → opening envelopes → enclosure junctions → material expression/compatibility.

### K5 — Independent hours and whole boundaries

A foyer and a shared passage both connect to an exhibition area; closing only the foyer door leaves another path open. The evening activity also requires a toilet beyond a locked workshop. Expected response traces every portal and complete support journey, proposes a continuous controlled boundary or changed shared territory, and checks the emergency strategy separately.

Conflict variant: no new door or boundary change is permitted. Changed-condition variant: deliveries use the same evening route. The method must expose an operational incompatibility, not label the room independently accessible because one path exists on paper.

Required graph: program/actors → closure → path/occupied field → typology operations → inclusive/emergency interface.

### K6 — Existing fabric, replacement and continued use

Given a partly surveyed retained wall, an observed finish, an unknown hidden support/control layer and a proposed replacement opening, distinguish observed geometry from inferred capacity. Develop alternatives conditional on the investigation that matters, maintain support/control continuity and trace piece/worker/waste routes during occupied work.

Conflict variant: removal would interrupt the only occupied access route. Changed-condition variant: the replacement unit fits but cannot be installed or removed along the available journey. Expected response revises staging/access or keeps the dependent commitment unresolved. It must not invent concealed condition, a licensed source detail or engineering approval.

Required graph: existing-fabric evidence → opening/support → retained-substrate junction → maintenance journey → phased program/access → requested-use completion.

### K7 — Jurisdiction and knowledge locality

Run an ordinary conceptual version of K2 with jurisdiction unknown. Expected behavior continues independently justified geometric and architectural reasoning while leaving legal thresholds open; it does not default to Russia. Then supply a Russian project location/date/use and require a regulatory conclusion. Expected behavior selects the actual normative records and primary evidence needed for that conclusion, rather than pretending a local paraphrase eliminates live authority verification.

This is the deliberate exception to non-normative local-only evaluation. A successful conceptual local run does not prove legal compliance or current source availability.

## Depth increments

Choose each increment by a named unsolved design question or failed scenario, not by number of sources available. Before adding content, identify the existing owner and the precise missing mechanism, input definition, alternative or verification method.

| Priority | Coherent increment | Evidence that depth increased |
| --- | --- | --- |
| First | Demand → occupied room → route/support → floor/section | K1 and K5 can be resolved under ordinary, fixed-conflict and changed-operation conditions without losing geometry or inventing capacity |
| First | Light/view/privacy/noise/air and their controls | K2 produces a coherent simultaneously usable state, explicit failure behavior and correct limits of geometry |
| Next | Parti, proportion/hierarchy, occupied facade and material/junction expression | K4 yields distinct spatial alternatives, causal trade-offs and a corrected corner/module relationship, not facade adjectives |
| Next | Support/enclosure interfaces and material-system breadth | K3 plus a selected junction/material case carries forces/functions/space and assembly/replacement consequences consistently |
| Next | Existing fabric, typology operations and lifetime intervention | K6 and a selected use-family variation preserve evidence status, independent operation and complete maintenance journeys |
| Following evidence | Underrepresented styles, typologies and specialist subjects | A substantive local method with an original counterexample and verified provenance exists; a new heading or bibliography entry is insufficient |

For every increment, require substantive explanation, applicable inputs, competing choices, a negative case, changed-condition reasoning, cross-domain consequence checks and retained source limits. The review states which question is now covered and what breadth remains unestablished. There is no universal claim of a fully qualified architect, and no forced artificial stopping point based only on token/file count.

## Trade-offs and review decisions

The proposed decision is to migrate the three pilots first, preserve existing identified-case/data paths, centralize duplicated subject discovery, and consolidate provenance only after the content-preserving migration proves useful. This avoids mixing organizational change, source removal and new technical claims in one opaque diff.

The main risks are overfragmentation, loss of parent conditions when extracting a child, duplicated canonical methods, hidden external prerequisites, excessive prerequisite traversal, and creating a source-ID system that merely hides URLs. The section map, conditional relations, local-only scenarios and separate counting metrics address those risks.

A+B requires review of this topology, the pilot destinations/merges and the source-locality contract before C. Later discoveries may justify a revised leaf boundary; record a material deviation before moving dependent content. No required design choice is deferred to an unspecified executor: exact pilot destinations and nonpilot dispositions are provided. Granularity beyond those mapped groups can be refined in a separately reviewed depth increment, not guessed during a mechanical move.
