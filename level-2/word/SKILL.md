---
name: style-transfer
description: Borrow formatting from an existing Word DOCX into a reusable Markdown preset, apply a saved preset to another Word document, or create a new editable Word document. Use for capturing visual examples, extending the preset library, restyling existing documents, and creating reports, portfolios, proposals, or academic documents with verified layout.
---

# Style transfer

Own the complete Word lifecycle and the reusable formatting library. Capture a good Word example once, save its reusable design in one Markdown preset, and reproduce it in other documents. Keep shared layout principles here, operation procedures in `operations/`, implementation details in `references/`, and formatting data in `assets/presets/`.

## Select an operation

| Requested result | Operation | Read |
| --- | --- | --- |
| Save an existing Word document's formatting for reuse | Borrowing | [Borrowing](operations/borrowing.md) |
| Apply saved formatting or a supplied visual reference to an existing Word document | Adaptation; borrow first if no reusable preset exists | [Adaptation](operations/adaptation.md) |
| Build a new Word document from supplied content | Creation | [Creation](operations/creation.md) |

Start at the requested operation. Chain operations only when the task needs it. Read the selected operation and only the supporting materials relevant to its objects and risks. Keep all operations within this skill.

## Common principles

### Content and authority

- Use canonical sources for facts and a reference document for design. Preserve wording, order, meaning, uncertainty, units and required repetitions during formatting. Rewrite or condense only when the task authorizes it. Do not copy sample facts, contacts or placeholder text from a design source into a target.
- Inventory source content, assets and relevant objects before mutation. Keep the source-to-output map outside the final document. Formatting may change pagination; an example's page count is not a limit on current content.
- Apply precedence: explicit user constraint → selected reference/preset → supplied brand → unselected library defaults → component defaults. A selected layout may legitimately omit a cover or TOC or use borderless layout tables.
- Preserve unrelated content and package parts. Use a targeted edit, restyle or rebuild according to the requested change; rebuild only when required and authorized. Keep comments, revisions, fields, formulas, drawings and other stories intact unless their change is in scope.

### Semantic and editable structure

- Use real Title, Subtitle, Heading and named body/component styles. Match styles by semantic role and inspected definitions; a style's name or size alone does not prove its role. Keep heading depth consistent with the actual outline.
- Use true Word numbering with deliberate nesting, continuation and restarts. Use editable tables, working hyperlink relationships, valid fields/bookmarks and native OMML formulas. The bundled OMML helper inserts supplied math; it does not parse LaTeX.
- Treat named styles as the baseline. Preserve meaningful direct formatting such as emphasis and special glyphs; remove only overrides known to contradict the requested restyle. Do not replace whole paragraph/cell text when child markup must survive.
- Keep unsupported content visible or preserve its native object and report the precise limitation. Never silently rasterize editable math, drop unsupported Markdown, or present a partial conversion as lossless.

### Typography and composition

- Check font availability and Cyrillic, mathematical and special glyphs. Apply substitutions in a task-local configuration and report material differences. Do not rewrite a shared preset to suit one environment.
- Compute usable space from actual section geometry, margins, headers/footers and cell padding. Preserve image aspect ratios and legibility. Use source graphics and inspect cropping before any authorized crop.
- Keep headings with following content and figures with captions. Allow long paragraphs, lists and tables to flow. Use repeating table headers, deliberate widths and automatic row height. Use layout tables only when the chosen design warrants them and verify reading order.
- Repair spacing, widths, breaks and block distribution before shrinking type. Keep all required content. Use whitespace to separate meaningful groups; avoid clipping, collisions, stranded headings and accidental blank pages.
- Make deliberate section transitions and check linked headers/footers and page-number continuity. Use fields for navigation and numbering; refresh them only with a capable application and without executing external instructions.

### Reusable formatting

- Store all information about one preset in one `assets/presets/<name>.md`: exact parameters, semantic mappings, composition, adaptation rules, dependencies, provenance and limitations. Do not keep a parallel JSON/YAML representation or a separate prose passport.
- Store a neutral visual render in `assets/examples/<name>.png` and link it from the preset. Keep any necessary logo or image dependencies in `assets/presets/<name>-assets/`; reference them from that same MD. Do not require the original Word document for reuse.
- Separate observed rules, derived choices, explicit defaults and unsupported features during borrowing. A draft is not an approved reproduction. Verify a new preset before marking it ready; do not silently fill gaps and call them captured design.
- Keep original examples and shared presets unchanged for a one-document override. Save a new preset only when creating or updating reusable formatting is part of the task. Use design-only data and neutral demonstration content in the shared library.

### Verification and delivery

- Reopen and validate the final DOCX package, relationships, numbering and relevant object counts. Compare source coverage, assets and protected regions according to the operation. Investigate every unexplained loss or duplicate.
- Render and inspect every latest page at full resolution; a contact sheet is only navigation. Correct defects and rerender after layout changes. Verify factual fidelity, package integrity, field results and appearance separately.
- If a required check is unavailable or a feature cannot be reproduced, report the concrete limitation and partial status. A successful save, structural PASS or extraction command does not certify visual quality.
- Save outputs at the project's designated or user-requested destination. Keep build scripts, inventories and render intermediates temporary unless required. Deliver only requested formats, with concise checks and limitations outside the document.

## Library and tools

The starting library contains [technical](assets/presets/technical.md), [corporate](assets/presets/corporate.md), [minimal](assets/presets/minimal.md) and [academic](assets/presets/academic.md). Their linked previews show authored defaults, not regulatory compliance or exact-font equivalence. Read the chosen MD as the sole source for its values and rules.

Use the environment-owned Python runtime where available, otherwise the project environment with Python 3.10+, `python-docx`, `lxml` and `Pillow`. Do not install globally or fetch dependencies silently. Locate rendering through available environment capabilities rather than a hard-coded installation path.

Use `scripts/document_tool.py` for inspection, draft extraction, styled foundations, conservative restyling and package validation. Use `scripts/document_tools.py` for supported authoring helpers and focused OOXML changes where needed. Read [toolkit](references/toolkit.md) before using an API; its documented limits apply to all operations. Commands are building blocks, not completion certificates.

## Supporting materials

| Material | Read when |
| --- | --- |
| [Preset format](references/preset-format.md) | Writing, reviewing or extending a Markdown preset |
| [Design system](references/design-system.md) | Mapping roles, selecting formatting or resolving fonts/themes |
| [Components](references/components.md) | Authoring or adapting lists, tables, graphics, formulas or navigation |
| [Page composition](references/page-composition.md) | Planning dense pages, portfolios, wide material or repairing pagination |
| [Templates and editing](references/templates-and-editing.md) | Capturing a reference or changing an existing document |
| [DOCX mechanics](references/docx-mechanics.md) | Editing sections, styles, numbering, fields, relationships or fragile objects |
| [Visual QA](references/visual-qa.md) | Rendering, checking a candidate preset or reviewing final pages |
| [Toolkit](references/toolkit.md) | Executing commands, authoring helpers or evaluating tool support |
| [Markdown input](references/markdown-input.md) | Creating a Word document from Markdown content |
| [Sources](references/sources.md) | Checking provenance or external technical authorities |
