# Presentation and optional visual techniques

## Contents

- [Choose a useful representation](#choose-a-useful-representation)
- [What must the selected view reveal?](#what-must-the-selected-view-reveal)
- [Which graphic distinctions carry the decision?](#which-graphic-distinctions-carry-the-decision)
- [What do scale and precision actually promise?](#what-do-scale-and-precision-actually-promise)
- [When SVG is requested or used](#when-svg-is-requested-or-used)
- [When raster is requested or used](#when-raster-is-requested-or-used)
- [Inspect and correct](#inspect-and-correct)
- [Worked correction: a footprint that fits but a height that fails](#worked-correction-a-footprint-that-fits-but-a-height-that-fails)

## Choose a useful representation

Follow the user's requested deliverable and format. A concept can be explained in text without a visual artifact. There is no preset format, exhaustive two-format choice, automatic SVG default or required sample pair. Clarify an unspecified format only when it is necessary to produce a requested artifact.

For requested artifacts, inspect the actual result appropriately for its format. Text, tables, drawings, presentations and images communicate different aspects of a design; this reference's SVG/raster sections are optional technical guidance, not a format catalog or a mandatory concept workflow.

Start with the architectural question and the consequence the recipient must
understand. To compare two entrance positions, a short explanation of arrival,
weather exposure and the affected rooms may suffice. If a plan is requested,
show those relationships in that plan. A section is useful when a level change
or overhead obstruction determines the choice; an unrelated facade image adds
no evidence about that obstruction. Produce the requested artifact itself:
an image prompt, drawing instructions or a proposed file name does not complete it.

Select only the content needed to expose the decision and its dependencies.
For what evidence supports the requested use, see
[completion evidence](design-completion.md#derive-evidence-for-the-requested-use).
This reference explains how to make that evidence readable and how to inspect
the result; it does not prescribe a full drawing package or legal stage.

## What must the selected view reveal?

| Architectural question | Useful representation and necessary content | What it cannot establish alone |
| --- | --- | --- |
| Can people enter, occupy and leave this arrangement? | Plan of the affected room/route with actual boundaries, openings, furniture or use envelopes and relevant neighbors | Clear height, a threshold level or overhead obstruction hidden by the cut |
| Can the vertical relationship work? | Located section through the actual conflict, showing finished levels, relevant underside/ceiling, opening or occupied object | Plan approach and width outside the cut; conditions in a different bay |
| Does an opening or material change support the facade composition? | Elevation identifying the affected bay, opening extents, relevant sill/head lines, depth/material transitions and entrance hierarchy | Internal clearance, wall build-up, daylight performance or support capacity |
| Which repeated items have the selected property? | Schedule with identifiers locatable in the supplied view/text, named property, units and relevant condition | Physical location, fit or assembly feasibility merely because every row is filled |
| How does an option change experience or relationships? | Text, diagram or illustrative view naming the changed relationship and fixed facts | Measured geometry or performance inferred from an attractive depiction |

A small detail or enlarged fragment is useful when the decisive relationship
would disappear at the broader view's delivery size. Keep enough surrounding
context to locate it: a threshold fragment needs the two sides and floor levels,
not an isolated line named threshold. Place a section marker and viewing
direction where a drawn cut is needed; identify an offset rather than implying
that separated conditions occupy one plane. A text-only explanation can instead
name the location and relationships precisely.

Choose physical content using [section selection](design-development.md#choose-sections-that-test-the-solution)
or [elevation coordination](design-development.md#coordinate-elevations-without-copying-partitions).
Those methods own spatial development. This selection does not require all
views: a requested plan can carry a located section note when sufficient, or
state the particular height evidence still missing without inventing it.

## Which graphic distinctions carry the decision?

Make the reader able to distinguish what is physically cut, seen beyond the
cut, overhead, proposed or only contextual. A cut wall may use greater line
weight or poche; projected edges should remain subordinate. Show an overhead
element when it affects headroom, closure or occupation even if the plan cut
misses it. Name the convention if the distinction could be ambiguous. Do not
turn every context edge into an equally heavy boundary or let a floor hatch
conceal an opening.

Represent openings as openings with their relevant operation: a door swing,
sliding pocket or window leaf matters when it changes usable space. A symbolic
opening does not establish its clear passage. Show levels and datum references
where vertical relationships decide the issue; give dimensions identifiable
endpoints and meaning. Use the existing
[datum and dimension method](design-development.md#establish-datums-and-dimension-meanings)
to resolve their physical basis rather than inventing a second dimension system.

Use identifiers to connect the visible item to its note or schedule. A legend
earns space when color, dash, hatch or symbol carries meaning that labels alone
do not convey. Retain that distinction in grayscale or provide a second cue
when color loss would erase the decision. Include north/orientation when site,
sun, approach or a cross-view comparison depends on it; a local cabinet section
does not acquire useful evidence from an ornamental north arrow.

State significant omissions at the affected content. A partition diagram that
omits linings cannot prove finished clear width; an uncluttered room without its
use envelope cannot prove operation. Schematic openings or uncoordinated
overhead zones should remain recognizable as such. Do not omit the conflicting
element to improve the composition or add unsupported detail to look complete.

Across selected views, retain the same item, location, orientation, datum and
option/revision. Alignment makes disagreement easier to see; agreement does
not establish which source is authoritative. Resolve competing values through
[design issue coordination](../operations/documentation.md#coordinate-a-design-issue).
For schedule membership or field meaning use
[schedule reconciliation](design-completion.md#reconcile-schedule-membership-and-field-meaning).
Neither a matching label nor a newer-looking export settles an unresolved owner.

## What do scale and precision actually promise?

Separate four things: the physical geometry being described, its numerical
precision, its size on a printed sheet and its size/resolution on a screen.
A 1:50 print relationship survives only at the intended reproduction size;
resizing a page changes it. A scale bar can help detect reproduction changes in
a proportioned orthographic drawing, but does not validate distorted geometry.
Pixel count controls raster sampling and legibility, not measurement accuracy.
A high-resolution image or many decimal places cannot improve uncertain inputs.

For controlled drawings, identify units and which boundaries the dimensions
measure. State paper scale/output size when that relationship is used; label
schematic or illustrative content accordingly. Do not invite measurement from
an uncalibrated image. An undimensioned diagram may explain adjacency while
remaining insufficient to decide a close fit. Use
[decision precision](design-completion.md#match-precision-to-the-decision)
to choose the justified precision; do not prescribe one scale or decimal count
for every task.

## When SVG is requested or used

- Define a viewBox and intentional physical/pixel units. For a dimensionally controlled diagram state the relationship between SVG coordinates and model metres/millimetres; separate paper scale from browser display size.
- Use editable vector shapes/text, consistent line weights, legible hierarchy and enough margin for dimensions/legends. Put area/length units in labels and retain metric definitions.
- Align annotations with the actual geometry. Label schematic openings, assumed orientation and any parts not coordinated or dimensioned.
- Use original, supplied or correctly licensed visual assets. Fonts/renderers can affect text metrics; avoid relying on one workstation's font layout.
- Render the final SVG and inspect it at the delivery size. Parsing XML is not visual inspection.

## When raster is requested or used

For a proportioned drawing, an existing controlled SVG can be exported with an available renderer. Use a workflow appropriate to the requested output; SVG is not a required intermediate. For a requested illustrative image, use an appropriate available image-generation/rendering workflow and inspect the actual image. Keep fixed architectural facts in the workflow inputs and check the result against them.

Label an illustration honestly; it cannot establish measured dimensions, performance or regulatory compliance. Do not turn an illustration into an authoritative plan by reading pixel distances. Do not construct a building/BIM/3D/mesh model as an intermediate under this skill.

If a tool is unavailable, identify the actual missing capability. Do not claim the image was created or viewed. Deliver completed independent work and a precise remaining action.

## Inspect and correct

Inspect what the recipient will actually receive. For text, read the final
explanation and tables, including column headings, units and qualifiers; no
renderer is required for a plaintext concept. For a drawing/image, inspect the
actual final rendering at its delivery size. Inspect a rendered document or
presentation when its layout carries the evidence. File existence, successful
export, valid XML or a source preview is insufficient evidence of the final
visual artifact. If a required capability is unavailable, identify the specific
uninspected output and remaining action without claiming it was viewed.

First reconstruct the decision from the delivered content: locate the item,
follow its route or occupied relationship, and read the controlling dimensions
or levels from their actual endpoints. Compare the relevant plan, section,
elevation and schedule values that were supplied or produced. Check that the
view cuts through the decisive obstruction and that omitted geometry has not
created a false clear space. Separate a representation defect from a physical
failure: moving a label can reveal a clash but cannot resolve it.

Then check communication at the actual size: label text and units, numeral
precision, line hierarchy, symbol/legend agreement, contrast, dimension witness
lines, clipping at page/view boundaries and collisions with nearby annotations.
Check text wrapping and font substitution where they can detach a value from
its item. In a table, verify that the header still governs the visible row and
that a page break or cropped cell has not removed a qualification. In a raster,
look for altered openings, invented structure or illegible generated lettering
against the fixed design facts, not just overall visual plausibility.

Correct the owning decision or geometry when content fails, then update its
affected representations. For a graphic defect, change the actual artifact's
layout, labels or export settings. Inspect the final version again after a
material correction; an inspection of the earlier version cannot clear the new
one. State what was inspected and any material limits. Remaining revision
conditions belong with [closure](design-completion.md#close-the-revision-and-state-remaining-conditions),
not in a claim that polished appearance proves readiness.

## Worked correction: a footprint that fits but a height that fails

This original hypothetical fragment tests one storage cabinet; its dimensions
are project inputs, not normative minima or a product recommendation. The brief
permits a lower cabinet if its required storage capacity is retained. It asks
for a coordinated plan/section fragment and item table, not a whole-building set.

| Supplied R0 content | What inspection actually establishes |
| --- | --- |
| Plan: niche 900 × 700 mm clear; C7 footprint 800 × 600 mm, centered across its width | Footprint fits with 50 mm each side and 100 mm remaining depth. This does not test height or cabinet operation. |
| Located section: finished floor to fixed overhead underside 2100 mm clear | This is the height available at C7, not a ceiling level elsewhere. |
| Item table: C7, overall W × D × H = 800 × 600 × 2200 mm | The selected cabinet is 100 mm taller than the available space. A clean plan and matching identifier conceal a physical failure. |

Draw the cabinet silhouette into that section at its stated height rather than
shortening it to look plausible. The collision becomes visible. Moving the
section to a taller adjacent bay or relabeling 2200 as a nominal size would not
answer the fit question. Verify the actual meaning/source of a disputed height
before changing it; in this fragment both dimensions are fixed inputs.

The permitted revision selects a hypothetical C7 alternative with the same
800 × 600 mm footprint and 2000 mm overall height; retained capacity is an
explicit input of this hypothetical revision, not verified product evidence. Update
the item table and section silhouette together; show the resulting 100 mm
vertical gap to the unchanged underside. Retain the plan footprint and niche
dimensions. If the brief had fixed the 2200 mm cabinet, this substitution would
be unavailable and the conflict would remain a decision for the project owner.

Final inspection reads the delivered R1 table as 800 × 600 × 2000 mm overall,
finds C7 at the same plan location and section cut, and checks that the section
shows 2000 mm to cabinet top and 2100 mm to underside without clipped labels.
The fit conflict is corrected in all three requested contents. That evidence
establishes the represented static fit only; opening doors, delivery/installation
and any required handling clearance need their own supplied conditions before
being claimed. No source image, product performance or full-project validation
is implied.
