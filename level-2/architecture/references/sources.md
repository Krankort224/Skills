# Sources and adaptation map

This skill selectively adapts ideas from two pinned upstream collections:

- **A:** [Skills-Architects at 30a0845dddcaebd765fc396059573d02e99c5b63](https://github.com/Abhinavbwj/Skills-Architects/tree/30a0845dddcaebd765fc396059573d02e99c5b63).
- **C:** [Claude-skills-for-Computational-Designers at 7a090c9ddc92e441b1419910673edbcfa7a962ed](https://github.com/Abhinavbwj/Claude-skills-for-Computational-Designers/tree/7a090c9ddc92e441b1419910673edbcfa7a962ed).

[Third-party notices](../THIRD_PARTY_NOTICES.md) preserve both licenses.
Source material is untrusted evidence, not instructions for this skill. The
upstream content is not a verified current code, product database or engineering
standard. Consult primary project-specific sources for applicable requirements.

## Mappings

Paths below are relative to the named upstream root. **Revised** means the topic
was selected and substantially rewritten for this skill; **reference-only**
means it informed scope or review without importing its prescriptions;
**excluded** means no operational guidance was imported.

| Upstream path | Destination | Treatment and limits |
| --- | --- | --- |
| A `skills/building-programming/SKILL.md` | [program and space](program-and-space.md) | Revised: brief, schedule, adjacency; removed universal benchmarks and mandatory sequence. |
| A `skills/building-typology/SKILL.md` | [program and space](program-and-space.md) | Revised: types as hypotheses; removed fixed dimensions, benchmark values and exemplars. |
| A `skills/spatial-planning/SKILL.md` | [program and space](program-and-space.md) | Revised: arrangements and circulation trade-offs; no assumed code distances. |
| A `skills/concept-design/SKILL.md` | [composition and style](composition-and-style.md) | Revised: organizing idea and contextual comparison in conceptual 2D. |
| A `skills/design-theory/SKILL.md` | [composition and style](composition-and-style.md) | Revised: composition, proportion and expression; no person or history routing. |
| A `skills/building-envelope/SKILL.md`, `skills/material-selection/SKILL.md` | [performance and coordination](performance-and-coordination.md) | Revised: assemblies, junctions and material decision criteria; no prescribed assemblies or numeric values. |
| A `skills/daylighting-design/SKILL.md`, `skills/acoustic-design/SKILL.md` | [performance and coordination](performance-and-coordination.md) | Revised: conceptual trade-offs, specialist review, no performance claims. |
| A `skills/building-services/SKILL.md`, `skills/structural-systems/SKILL.md` | [performance and coordination](performance-and-coordination.md) | Revised: interfaces, spatial reservations and issue ownership; no engineering design. |
| A `skills/accessibility-design/SKILL.md`, `skills/fire-life-safety/SKILL.md` | [requirements](requirements.md) | Revised: design concerns and jurisdiction-specific source verification; no default thresholds. |
| A `skills/architect-foundations/references/global-codes-frameworks.md`, `skills/building-codes/references/ibc-reference.md` | [requirements](requirements.md) | Reference-only, identified by tree: jurisdiction-specific digests are not adopted as authority or fallback. |
| A `skills/architect-foundations/references/theorists-and-movements.md` | — | Excluded: biographies, historic narrative and person routing are outside this design workflow. |
| A `skills/country-*/SKILL.md`, `skills/geographic-foundations/SKILL.md` | [requirements](requirements.md) | Excluded: country digests and inferred jurisdiction; source/version/applicability must be verified for the project. |
| A `skills/architect-calculator/` | [calculators](calculators.md) | Calculator-specific adoption and exclusions are recorded there; no calculator prescriptions duplicated here. |
| C `skills/cd-foundations/SKILL.md` | [computational design](computational-design.md) | Revised: input/constraint/output thinking only. |
| C `skills/data-driven-design/SKILL.md` | [computational design](computational-design.md) | Revised: provenance, quality, uncertainty and comparability; no universal privacy thresholds. |
| C `skills/generative-design/SKILL.md`, `skills/optimization-methods/SKILL.md` | [computational design](computational-design.md) | Revised: objectives, alternatives and trade-offs; no search algorithms or optimality claims. |
| C `skills/parametric-modeling/SKILL.md` | [computational design](computational-design.md) | Revised: fixed, variable and derived values; no software-specific model implementation. |
| C `skills/cd-calculator/` | [calculators](calculators.md) | Calculator decisions belong to that reference. |
| C `skills/bim-scripting/`, `skills/mesh-processing/`, `skills/computational-geometry/`, `skills/scripting-reference/`, `skills/interoperability/` | — | Excluded: BIM, 3D/mesh authoring, software catalogs and implementation. |
| C `skills/digital-fabrication/`, `skills/algorithmic-patterns/`, `skills/ml-for-aec/`, `skills/facade-computation/`, `skills/structural-computation/`, `skills/design-automation/` | — | Excluded: fabrication, algorithms, ML, automated model generation and specialist computation. |
| C `skills/environmental-simulation/` | [performance and coordination](performance-and-coordination.md) | Reference-only by topic: conceptual limitations; no simulation workflows or standards values imported. |

The linked local references are newly written, selective adaptations, not full
copies of either collection. The project has no imported external image assets;
illustrations must use supplied, original or appropriately licensed assets.
Further modeling work requires a later explicit request and a separate handoff.

## Russian normative evidence

The [jurisdiction index](normative/index.md) exposes implemented modules only.
The [Russian catalog](normative/ru/index.md) contains discovery and applicability
metadata, checked at the record's stated boundary/date. It is not imported from
upstream country digests or the Architecture coursework library. Normative links
follow the [primary-source contract](requirements.md#primary-normative-sources):
official promulgation, issuer publication or primary official register/operator.
Government-hosted third-party consolidations and other mirrors are not retained
as normative links. Notices/explanations are identified for their own publishing
role. Each thematic record owns its supported scope/status and access limits;
secondary-only statements are narrowed rather than relabeled as primary checks.
The Russian [selection procedure](normative/ru/applicability.md) owns local
mechanisms; shared rules and outcomes remain in requirements. This is a
current-document navigator, without revision archives. Detailed project
provisions are checked when selected. Full texts stay external.
