# Render and verify

## Render contract
Use the available documents skill renderer when supplied by the environment. Select its path from the environment/skill catalog, not a hard-coded installation path in this reusable skill. Otherwise render with native Word or LibreOffice through a task-local isolated workflow. Use the environment-owned runtime when available.

A renderer may temporarily use PDF internally to produce PNGs. Do not deliver that intermediate or turn it into a separate requested format. If the user prohibits even temporary PDF conversion, select another permitted rendering route.

## Inspect all latest pages
Follow the root render/review gate. Record final page count and reviewed scope outside the artifact.

Check:
- first-page purpose, title and metadata;
- heading ladder and actual navigation roles;
- type size, Cyrillic and special glyphs;
- text/cell clipping, overlaps, collisions and overly dense columns;
- whitespace and unintended blank pages;
- table header repetition, widths, borders, padding and row continuation;
- image proportions, legibility, captions and correct source selection;
- page-number continuity, fields and appendix transitions;
- last-page composition and accidental leftovers.

## Content gate
Compare canonical items and intended destination counts. Search for stale contacts, outdated template claims, missing sections and unresolved placeholders. Check facts separately from design. Do not insert uncertainty notes into the final document merely because the build had a missing source; report unresolved issues to the user.

## Structural gate
Run document_tool.py validate; reopen with python-docx. Investigate relationship, numbering and media warnings. Compare source media hashes when images must remain unchanged. Check bookmarks, links and equations for requested preservation.

## Library sample verification
Generate examples with generate_examples.py, validate each, then render and inspect every page. The same semantic sample should exercise title, multiple headings, nested real lists, a data table, a figure/caption, local page fields, native math and a continuation page. Values are explicitly demo data, not source facts.

These examples exercise those supported components, not all possible Word features. Run focused tests when introducing new code, failures or unsupported structures. When borrowing a new design, add a neutral source-specific sample for every claimed component and section variant; a four-preset smoke test does not verify the new capture.

## Template application test
Use a real selected template with current authoritative content. Check source coverage and structures absent from generic demos. Record transferable defects through the project's existing workflow and update reusable guidance/tools when appropriate.
