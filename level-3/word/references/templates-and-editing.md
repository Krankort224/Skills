# Templates and existing documents

## Inspect before selecting an edit route
Render the selected template. Inventory page geometry, styles, headers/footers, all content stories, fields, numbering, tables, drawing types, bookmarks and revisions. Identify direct formatting that contributes to the reference's identity.

Choose:
- targeted edit: preserve layout and unaffected parts;
- restyle: preserve content, change an agreed visual system;
- rebuild: recreate body composition only when explicitly required/authorized, retaining selected design conventions.

A rebuild is not a routine repair strategy. Text replacement through paragraph.text/cell.text clears child markup and may lose fields, links, math, drawings or run emphasis.

## Facts versus design
Use the current canonical source for facts and the template for presentation. Template text may be stale. Read layout selectors and compare them with current source headings; fail on an unmatched selector rather than treating it as an empty block. Map all source items, including items beyond a template's old slice limits. Check repeated items across pages.

A template can contain actual content instead of placeholders. Refresh every relevant occurrence: profile, role, contacts, project descriptions, labels and dates. Do not fabricate a new section simply to fill a gap.

## Reuse styles safely
Open the template as the foundation when making a template-based derivative. Preserve style names and IDs, page geometry and relevant header/footer relationships. Remove old body elements only for a permitted whole-body rebuild, preserving final sectPr and checking section-local properties. Do not strip direct formatting globally.

Copying styles from a different file is not equivalent to transferring all design. Theme, numbering, relationships, section settings and linked header/footer parts can affect it. For complex merges use a capable composer or focused package mutation, not copy-paste of unrelated XML parts.

## Content mapping
Maintain a task-local content map:
- canonical source file/revision;
- section/item identifier;
- destination role/page/region;
- expected repetitions or deliberate exclusions;
- asset path and usage.

Store this outside the final document. For repository-based sources, keep their canonical files unchanged unless the task includes source editing. Resolve contradictions before inventing facts.

## Preserve complex structures
Treat track changes, comments, content controls, embedded objects, text boxes and linked objects as fragile. The provided helper inventories these but does not implement arbitrary repair. Use specialized tooling for the requested object, or report the specific blocking limitation.

Never accept revisions, remove comments or execute macros/external fields simply to make the file easier to process.

## Verify according to route
Targeted edit: compare unaffected text, media, links, stories and object counts.
Restyle: compare content and objects; expect pagination changes.
Rebuild: compare full source inventory, selected assets and template design constraints; count changes are expected but must be explained.

Reopen, validate and render. Field refresh and page layout must be verified separately from ZIP/XML integrity.


