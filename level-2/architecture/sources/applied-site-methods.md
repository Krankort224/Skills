# Selected primary evidence for applied site methods

These records support [vehicle geometry](../references/context/urban/vehicle-and-parking-geometry.md)
and [territorial service allocation](../references/context/urban/service-capacity-allocation.md).
They are design-mechanism provenance, not a normative catalogue or mandatory
runtime reading. Selected retrieval/inspection date: 2026-11-08. Source media
and temporary text extracts stay outside the repository.

## Manual for Streets 2007

Identity: *Manual for Streets*, first published 2007, Department for Transport
and Communities and Local Government; Thomas Telford Publishing.
[Issuer-hosted PDF](https://assets.publishing.service.gov.uk/media/5a7e0035ed915d74e6223743/pdfmanforstreets.pdf),
146 file pages; SHA-256
`bfda6e5bf2e7c7372dc98ca856f136cb8ef7f5213e688a348396ef09d0c390b4`.

Inspected: copyright leaf (file page 3); selected text 6.8.1–8 (service/waste
vehicle choice, routes and reversing, file pages 76–77), 7.2.6–7 (tracking,
file page 82), 8.3.48–58 (bay/aisle/angle interaction, tracking, underground
interfaces and accessible parking, file pages 111–113). Firecrawl text retrieval
was checked against `pdftotext` for identity/locators. No figure tracing,
full-document visual review or current standards verification is claimed.

Adapted mechanism: choose an actual vehicle/operation, check motion as well as
storage rectangles, and couple bays, aisles, entries and pedestrian space.
Local projections, axle/corner geometry, sampling bound and examples are original
derivations. Excluded: every source dimension, traffic threshold, reversing
limit and old UK-specific normative prescription. No tracking template is copied.

Rights: the inspected leaf states Queen's Printer/Controller of HMSO copyright
2007, separate typographic rights, limited free reproduction purposes and a
permission requirement for other uses. No blanket open licence is inferred.
Only original paraphrase/geometry and bibliographic links are installed; no
source text, diagram, photo, map or logo is redistributed.

## Building Bulletin 103

Identity: Department for Education, *Area guidelines for mainstream schools*,
Building Bulletin 103, cover June 2014.
[Issuer-hosted PDF](https://assets.publishing.service.gov.uk/media/5f23ec238fa8f57acac33720/BB103_Area_Guidelines_for_Mainstream_Schools.pdf),
45 file pages; SHA-256
`7202e761f0f91afc4cba17d7f16b7dab64f190fd7c934cf88ac42ba0add22ce1`.

Inspected: cover/introduction (file pages 1/3), Part B site/category explanation
(file page 35), non-net/supplementary site text (file page 41), copyright/licence
(file page 45). The introduction identifies non-statutory mainstream-school
guidance. Site text distinguishes pupil-usable ground, footprint and access,
and separates children's access from vehicles. No graph/diagram validation.

Adapted mechanism: fit actual activity shapes, footprint, access and support;
distinguish usable outdoor ground from gross land and functional capacity.
Excluded: all numeric formulae, ratios, curriculum assumptions and UK-specific
statutory claims. This source does not establish a universal preschool/retail/
hospital program. Local parcel programs and inputs are explicitly hypothetical.

Rights: Crown copyright 2014; the leaf offers reuse excluding logos under Open
Government Licence v2.0, with separately identified third-party rights requiring
their own permission. Only original synthesis/source links are installed; no
graphic, logo or source text is reproduced.

## Network capacity allocation

Identity: Esri, ArcGIS Pro 3.6 primary documentation,
[Location-allocation analysis layer](https://pro.arcgis.com/en/pro-app/3.6/help/analysis/networks/location-allocation-analysis-layer.htm).
Selected text inspected: Facilities `Capacity`, demand-point definitions and
the complete problem-type table entry `Maximize Capacitated Coverage`, including
cutoffs, all-or-none allocation and non-nearest assignments. This is technical
documentation, not school/admissions authority or an executed GIS model.

Adapted mechanism: distinguish network eligibility from finite supply; nearby
demand can remain unserved when capacity is exhausted. The local conservation,
cut/reassignment procedure and examples are original synthesis. Esri's described
capacitated option assigns a demand point whole; it must not be claimed to run
the local split-seat flow without adapting and verifying data/constraints.
Excluded: proprietary algorithms/code, installation, figures, datasets, defaults
and any claimed solver execution. No redistribution permission for Esri media,
text or software is established here; original explanatory synthesis only.

## Verification and authority limits

Local tests independently construct transformed corners, sample a bounded arc
with declared error allowance, enumerate small allocation cases and reconcile
land. They establish those idealized cases, not empirical driving, actual school
operation or project approval. Existing four calculator contracts remain intact.
Read [requirements](../references/requirements.md) for a real regulatory claim;
source access and numerical success alone cannot supply it.
