# Editable components

## Title and cover
Use Title for the document's actual title. A compact title block contains title, optional subtitle, then factual metadata. A formal cover may use organization, author, date and version only when provided. Avoid empty hero placeholders and decorative filler. A selected portfolio may begin directly with the person/profile or first project.

## Headings and section transitions
Use actual Heading 1–6 paragraphs. Keep primary project headings outside layout tables where practical for navigation. Use page-break-before on a heading at a genuine new-page transition. On a continuation page, avoid inventing a duplicate semantic heading; use a quiet continuation label only if useful.

## Lists
Use true Word numbering definitions, not literal bullet characters or manually typed 1/2/3. Preserve nesting and intentional restarts. Keep a whole short item together but allow a long item to flow. In dense narrative/project text, list roles may use compact paragraph spacing. Do not distribute one item across unrelated cells.

## Data tables
Use data tables for comparable records. Set deliberate widths: short values narrow, descriptions wide. Align text left; choose numeric alignment deliberately and consistently. Use repeating headers, light borders, preset padding and alternating fills where specified. Use automatic row height; forbid row splitting only for short rows. Allow long rows to split or restructure them instead of creating impossible page-height constraints. Keep header and first row together, but do not keep the entire long table together.

Patterns:
- parameter/value/unit: description wide, value and unit narrow;
- comparison: identical attribute order across options;
- long register: repeating header and stable column widths;
- numerical results: consistent precision, units and alignment.

## Layout tables
Use borderless fixed-width tables when the selected design calls for editorial/portfolio composition. They are layout devices, not data grids. Preserve reading order: left cell top-to-bottom, then right cell. Use one table per region, horizontal merges for full-width rows, no nested tables when an ordinary layout suffices. Give internal gutters explicit padding and zero outer padding where a template requires aligned edges. A cell still needs a paragraph, including after a nested object; remove only proven surplus paragraphs.

## Notes and callouts
Default to a normal Note paragraph with a bold lead-in such as Assumption or Limitation. Use colored or boxed callouts only when supplied design/user preference warrants them. Never rely on warning color alone. Avoid turning ordinary prose into a page of competing panels.

## Images and captions
Use source graphics. Insert inline images at preserved aspect ratio, with width limited to the actual usable cell width and optional maximum height. Do not stretch technical drawings. Keep image and caption together, but let surrounding prose flow independently. Crop only when the task authorizes it and content loss has been assessed. Preserve original assets; conversions go to temporary files.

For SVG: retain native SVG with a compatible raster fallback if the toolchain supports it. If the source SVG embeds a raster image, extracting that exact image is a faithful fallback. Do not pretend raster data has become vector geometry.

## Formulas
Prefer editable OMML. The helper accepts already constructed valid OMML; it is not a LaTeX parser. Use a vetted converter for LaTeX only when available, check resulting math, and preserve equation numbering with fields/bookmarks. A raster fallback requires an explicit limitation and careful sizing; never silently flatten an editable source equation.

## Fields and navigation
Use PAGE/NUMPAGES for page numbers and TOC/SEQ/REF/PAGEREF for navigation where needed. The helper writes fields but cannot certify Word's updated field results. Update using a capable renderer/application and inspect cached results. Preserve bookmark IDs and references. Do not execute DDE, INCLUDETEXT or other external field targets to refresh a document.

## Appendices and wide material
Use explicit section changes for different page geometry; inspect linked headers/footers and page-number restart behavior. Do not rotate the whole document for one wide table. Keep appendix heading, identifier and cross-reference consistent.

