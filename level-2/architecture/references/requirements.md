# Requirements and jurisdiction

Identify potentially relevant obligations early and verify them against the
actual project. Design exploration can proceed with unknown jurisdiction, but
requirements remain unverified and no compliance conclusion follows. Do not
infer country or jurisdiction from language, currency or style; do not apply IBC,
Eurocode or any other code as a default.

## Contents

- [Establish applicability](#establish-applicability)
- [Accessibility and inclusive use](#accessibility-and-inclusive-use)
- [Fire and life safety](#fire-and-life-safety)
- [Russia-specific source selection](#russia-specific-source-selection)
- [Complete selective reading](#complete-selective-reading)
- [Deliver the open issues](#deliver-the-open-issues)

## Establish applicability

Ask for project location and authority, building use and occupancy, new build or
alteration, scope, height and scale, project stage, and any client or authority
requirements already supplied. Record what is known and what is assumed.
Confirm applicable law, adopted code edition, amendments, effective dates,
transitional provisions, use classification and any approvals with the relevant
authority and qualified local professionals. Private standards or client targets
may supplement, but do not automatically replace, legal requirements.

For each proposed requirement record:

| Field | Record |
| --- | --- |
| Source | Issuing body, title, edition/date, stable link or supplied document |
| Applicability | Jurisdiction, adoption, amendments, project conditions, verifier |
| Provision | Exact section, relevant scope, exceptions and interpretation |
| Design response | Location on plan, input, assumption, evidence and issue owner |
| Status | Confirmed, pending, not applicable with reason, or conflicting |

Quote only what is needed and check original authoritative sources; a secondary
summary or upstream reference is a lead, not a substitute for the adopted text.
If a document is unavailable or its application is uncertain, identify the
missing source or expert decision and keep the requirement open.

## Accessibility and inclusive use

Explore step-free arrival and movement, usable entrances and doors, vertical
connections, maneuvering, sanitary facilities, signage and sensory needs.
Identify relevant user journeys including arrival, use and exit, and their
potential barriers. Actual dimensions, facilities and exceptions require the
applicable provisions and project-specific interpretation; do not use generic
figures as universal minima. Engage users and an accessibility specialist where
appropriate. Inclusive intent alone is not a compliance determination.

## Fire and life safety

Identify occupancy and fire strategy assumptions, routes to safety, exit
locations, compartment boundaries, vertical connections, access for responders
and interfaces with structure and services. Check potential conflicts early:
open stairs, atria, facade openings, locked doors and mixed uses can affect the
strategy. Travel distances, capacity, ratings, separation and systems depend on
applicable rules and the project; do not assign generic thresholds or conclude
that a sketch is safe or compliant. Obtain authority and fire specialist review.

## Russia-specific source selection

When Russia is confirmed, select the matching question/condition from
[task-to-record routes](normative-routes.md), then use its specific record links.
The [catalog](normative-catalog.md) owns coverage and discovery-source limits.
The catalog's Russian adaptation target does
not assign Russia to every future task. Do not read every record for a local
decision.

1. Establish the actual subject: address/municipality and parcel, host and
   embedded uses, users, work classification, height/depth/scale, existing
   conditions, design stage and relevant project dates. Distinguish premises
   alteration, reconstruction and capital repair; a user's word “renovation”
   alone does not settle the legal classification. Retain fixed project facts
   and identify only missing conditions material to selection.
2. Select the relevant [work/stage](normative-routes.md#work-and-timing) record;
   then screen territory, typology, fire/accessibility, sanitary/environmental
   and engineering-interface branches against the actual task. Include
   adjacent documents where a changed entrance, use, envelope or route affects
   them. Check both the host building and an embedded function.
3. Read each candidate record completely using [selective reading](#complete-selective-reading), including its scope, exclusions and verification limits.
   Follow the linked official text/register to the relevant provision and
   necessary amendments, replacement and commencement evidence. A registry
   abstract supports discovery, not every detailed rule. An active badge,
   search excerpt or agency-hosted old commercial text cannot establish a
   current provision. Keep inconsistent status/replacement fields unresolved.
4. Establish the application basis for the selected provision and project
   date: direct legal/sanitary/fire obligation, a documented technical safety
   route, or a project/contract requirement. The post-2024 construction
   requirements mechanism, fire mechanism and any historical transitions need
   separate checks in the federal record. Do not classify a whole SP/GOST as
   universally mandatory or voluntary from its title, registration or an old
   list. Do not infer that a missing registry search result removes a statutory
   duty. An alternative substantiation route needs an actual justified project
   decision, not a shortcut around a constraint.
5. Select the edition for the actual work/stage/date and scope of intervention.
   Compare any transition provisions, approved baseline and establishing acts.
   A newer edition does not automatically replace the project's justified
   basis; an old supplied standard does not freeze the applicable requirements.
   Retrieve the missing authoritative evidence before resolving a conflict.
6. Assign a selection outcome below and identify the source fragment, factual
   trigger, edition/date condition and remaining question. Store the result in
   the existing project's requirements/source record, with its design response
   and owner. Keep shared discovery metadata in the catalog; do not create a
   parallel project-fact store.

| Selection outcome | Required reasoning |
| --- | --- |
| Applicable | Relevant scope/conditions and selected provision/edition/basis established for the stated decision; name the actual evidence. This is source selection, not a claim the design complies. |
| Potential | Scope is plausibly triggered, but a named project fact or provision check is missing. State what would decide the selection. |
| Not applicable | Cite a checked scope exclusion or absent trigger and the actual project fact; topical mismatch alone is insufficient where the host/adjacent use may still trigger it. |
| Unresolved | Currency, legal basis, contradiction, source access or interpretation prevents a reliable decision. Name the missing text/decision rather than supply a default value. |

A record's partial verification and a project's selection outcome are different
axes. A checked registry scope can identify a potential document while detailed
application remains unresolved. Absence of an unknown height, fire class or site
zone is not proof of absence of its requirements. Continue independent design
work with explicit assumptions while retaining dependent conclusions as open.

### Apply the route to a bounded change

For a relocated entrance in an existing apartment building, first retain the
accepted layout and identify whether the change affects common property,
load-bearing elements, façade, access, evacuation or an embedded public use.
Check the housing/work-classification route and local/heritage conditions;
screen residential/public typology and fire/accessibility together. If the
municipality, scope of intervention or approvals are unknown, select potential
sources and leave their affected provisions unresolved. Do not silently treat
the task as either new construction or harmless interior decoration.

## Complete selective reading

Select the architectural question and material project conditions before
retrieval. Use the [route index](normative-routes.md) to identify specific
record anchors; use thematic contents only for unmatched questions. The route
index is navigation, not a substitute for the owning record or selected law.

1. Locate the selected heading and the next heading of the same or higher
   level with the available heading/search tool. In a local checkout, for
   example, `rg -n '^## ' references/normative/building-typologies.md` returns
   current record boundaries without printing the file. Do not reuse line
   numbers from an older revision.
2. Retrieve from the selected heading through the line before the next
   peer/parent heading, or through EOF for the last section. Use bounded line
   ranges/section reads supported by the tool. Batch only the complete selected
   records that the tool can actually return. A link to a thematic file does
   not mean to print the entire file or every related group.
3. Inspect the returned content and truncation metadata. Each normative record
   must be visible through its end, including **Identity**, **Authority**,
   **Scope**, **Edition/status**, **Application basis**, **Related** and
   **Verification**. Read all conditions/exceptions and any text after those
   fields within the record. A successful fetch, stored tool variable, arbitrary
   character prefix or output ending inside a field is not a complete read.
4. If output is truncated or a boundary/field is missing, recover before using
   the claim: request a smaller known section/range or increase the return
   capacity enough for that complete extent. A long record can be read in
   contiguous bounded parts with its start/end and every part accounted for.
   Do not silently substitute the visible prefix or mark unread material as
   reviewed. If retrieval cannot be completed, label that record unread or
   partial and keep its dependent conclusion unresolved.
5. Follow a related record or external provision when the actual decision or
   a critical condition requires it. Inspect the selected authoritative scope,
   provision, exclusions and changes at similarly known boundaries. Stop when
   the decision has sufficient evidence; do not load the remaining corpus for
   completeness alone.

When reporting source selection, identify the records/provisions actually read
and any incomplete retrieval that limits the result. Distinguish complete
reading of a local catalog record from checking its cited external texts and
from establishing its application to the project.

## Deliver the open issues

Separate confirmed requirements from aspirations, assumptions and potential
checks. Assign the unresolved question, responsible party and next decision date.
A conceptual drawing, area estimate, or checklist is not a regulatory approval.
See [program and space](program-and-space.md) and
[performance and coordination](performance-and-coordination.md).
