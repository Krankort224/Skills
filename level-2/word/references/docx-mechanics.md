# DOCX mechanics

## Package and relationships
DOCX is an OPC ZIP package. Internal relationship targets resolve relative to the owning part, not the archive root; package relationships resolve from root. Check that targets exist, relationship IDs used by XML resolve in their owning .rels file, required parts exist and content types cover parts. External hyperlinks may be legitimate: preserve them without fetching their target.

The provided validator parses XML with external-entity resolution disabled, rejects duplicate ZIP names and missing internal relationship targets, and checks reference IDs. It does not implement the complete ECMA schema or certify arbitrary embedded objects.

## Styles
Use paragraph styles for semantic roles and character spans/styles for emphasis. Set ascii/hAnsi/eastAsia/cs font attributes where necessary. Direct formatting outranks style properties; changing Normal alone does not restyle all runs. Do not remove a run's complete rPr to change one property.

## Sections
The final sectPr belongs to the body; earlier sectPr belongs to a paragraph's pPr. Preserve page size, margins, orientation, start type, header/footer references and page numbering. Linked headers/footers may belong to another section; unlink deliberately before replacing them. Check first-page and odd/even settings after edits.

## Numbering
A true list uses numPr with numId/ilvl, a concrete num definition and an abstractNum. Ensure both IDs exist. Use distinct concrete IDs for intentional restarts; retain one across continuation paragraphs. The helper creates explicit nine-level definitions for bullet or decimal lists. It does not repair arbitrary imported numbering.

## Tables
Set tblGrid and cell widths consistently, fixed layout when requested, padding in twips and repeating header flags. Use automatic row height. CantSplit is suitable only for rows fitting a page. Merged cells share XML; do not iterate them as if they were distinct logical cells when checking duplicates. Table layout cannot be validated solely from widths: render it.

## Images
Resolve embedded image relationships and maintain width/height proportions. Inline drawings are easier to predict than floating anchors. Do not convert anchors globally: wrapping/positioning may be intentional. SVG requires an Office-compatible extension and a bitmap fallback for older readers. Alt text should describe the actual visual or its task-relevant role, not a fabricated conclusion.

## Fields, bookmarks and equations
Preserve fldChar begin/separate/end and instruction text. Avoid stale cached values; update with Word or a suitable renderer when needed. Never refresh external instructions blindly. Keep SEQ/REF/PAGEREF references consistent with bookmark names/IDs. OMML is editable native math; image rendering is not equivalent.

The field helper allows local PAGE, NUMPAGES, TOC, SEQ, REF and PAGEREF instructions only. It marks fields dirty but does not update them. The OMML helper accepts oMath/oMathPara roots and does not interpret LaTeX.

## Revisions and other stories
Body text is not the entire document. Headers/footers, notes, comments, text boxes and revision markup may contain text. Inventory their presence before editing. Paragraph objects from a high-level library may omit revision-wrapped content. Preserve or handle it explicitly, never infer absence.

## Source-aware validation
Use an exact text inventory when all content should be retained. A no-loss comparison must account for expected title/label changes and deliberate duplication. A substring check alone cannot prove correct order or uniqueness. For structured source assembly maintain item-level destination counts, then verify XML text and visual reading order.

## Unsupported operations
The bundled code is a reusable core, not a full Word replacement. It does not provide arbitrary tracked-change/comment editing, full style/template merging, LaTeX conversion, automatic layout balancing, authoritative field refresh or ECMA-schema validation. Use environment-specialized tools and revalidate if those operations are requested.


