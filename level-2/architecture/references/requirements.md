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
- [Primary normative sources](#primary-normative-sources)
- [Select a jurisdiction module](#select-a-jurisdiction-module)
- [Selection outcomes](#selection-outcomes)
- [Complete selective reading](#complete-selective-reading)
- [Deliver the open issues](#deliver-the-open-issues)

## Establish applicability

Reuse supplied project location and authority, building use and occupancy, work
type/scope, height and scale, stage and client/authority requirements. Ask only
for missing facts that materially change selection. Record what is known and
what is assumed.
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

## Primary normative sources

Keep normative-document links at the document's official promulgation, the
issuing authority's own publication or its primary official register/operator
record. Assess the publisher's role for that particular document. A government
hostname does not turn a hosted commercial consolidation or another party's
file into a primary publication. Do not retain school mirrors, association
copies, commercial reproductions or arbitrary asset copies as normative links.

An authority's own notice or explanation is primary for that notice only.
Label it as context/discovery and distinguish its statements from the act's
scope, exclusions and status. A primary register card can substantiate its
displayed identity, scope and status metadata without a full-text import.

Source authority and file format are separate. Prefer primary readable digital
text when available. A scanned original can be primary, while searchable text
from a mirror remains secondary. Preserve a correct unavailable primary URL
and its precise evidence limit; do not replace it with a convenient mirror or
silently preserve claims supported only by that mirror. Narrow or leave the
affected field unresolved.

Keep the shared catalog a current-document navigator, without revision
timelines, amendment inventories or predecessor chains. If a project date
requires an older edition or transition, inspect the external primary source
for that decision and store the conclusion with the project owner.

For a discovery record, check the claims actually retained: identity, source,
subject, object/work/territorial conditions, important scope exclusions and
supported edition/status observations. Missing critical identity or scope
evidence remains a catalog limitation. Reading every clause, collecting scans
or independently reconstructing every amendment chain is not a universal
catalog-completion gate. Check detailed provisions, values and the exact
edition/application basis when the design decision requires them. A supplied
project brief can own project requirements; a supplied normative copy still
requires source-authority assessment.

## Select a jurisdiction module

Reuse the project's supplied location and responsible authority. Select the
matching implemented module from the [jurisdiction index](normative/index.md).
Load that module's selection procedure and task routes only when its
jurisdiction matches the project. Regional and municipal selection then follows
the actual project location within that module.

If jurisdiction is unknown, identify the missing location/authority and leave
dependent normative conclusions open while independent design continues. If the
jurisdiction is known but no module is implemented, report that coverage gap
and use its actual primary sources or local expertise for the task. Never
silently substitute another jurisdiction's catalog. Russia is currently the
only implemented module; language, currency and architectural style do not
select it.

## Selection outcomes

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

## Complete selective reading

Select the architectural question and material project conditions before
retrieval. Use the selected [jurisdiction module](normative/index.md)'s task routes to
identify specific record anchors; use thematic contents only for unmatched
questions. A route index is navigation, not a substitute for the owning record
or selected law.

1. Locate the selected heading and the next heading of the same or higher
   level with the available heading/search tool. In a local checkout, for
   example, `rg -n '^## ' <selected-thematic-file>` returns
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
