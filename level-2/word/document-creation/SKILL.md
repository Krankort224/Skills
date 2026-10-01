---
name: document-creation
description: Create, complete, restyle, edit, or repair editable Word DOCX documents through the full lifecycle of source analysis, document structure, visual design, deterministic authoring, template adaptation, content and package validation, page rendering, and visual correction. Use for reports, portfolios, proposals, academic documents, and existing Word files; preserve facts and respect supplied templates.
---

# Document creation

Deliver an editable, factually faithful Word document whose actual pages have been inspected. Own both visual choices and their implementation. Do not treat a successful save or a longer checklist as proof of quality.

## Choose a route

| Input and task | Route | Read |
| --- | --- | --- |
| Content without a design source | Structure content, select a preset, build | [Design system](references/design-system.md), [components](references/components.md) |
| Selected DOCX template or visual reference | Inspect first; use its styles, geometry and composition before presets | [Templates and existing documents](references/templates-and-editing.md) |
| Existing document needing a local edit | Inventory affected stories and objects; make a targeted change | [DOCX mechanics](references/docx-mechanics.md) |
| Whole-document restyling | Preserve content, approve a visual direction from the request, change named styles and components | [Design system](references/design-system.md), [composition](references/page-composition.md) |
| Markdown input | Read the current conversion skill for Markdown semantics; use this skill for the resulting DOCX lifecycle | `../markdown-to-word/SKILL.md` |

Do not require a preset when a user has chosen a template. A portfolio may legitimately use editable borderless layout tables, different typography, and no cover or TOC. Do not impose report conventions on it.

## Complete the lifecycle

1. **Ground content.** Identify canonical text, graphics, accepted template, repository instructions and intended audience. Record the source revision and a content inventory outside the deliverable. A template is a design source, not an authority for current facts. Detect stale selectors, outdated contact details, missing sections and unreferenced source blocks before authoring. Do not invent claims or change canonical source facts silently.
2. **Inspect.** Run `scripts/document_tool.py inspect INPUT.docx --out inventory.json` for an existing file. Render a supplied template before changing it. Inspect styles, page geometry, body and other stories, numbering, fields, relationships, text boxes, tables, images and revision markup relevant to the task. Classify the edit as targeted, restyle or explicitly authorized rebuild.
3. **Plan structure and composition.** Map each source block to a semantic role and intended location. Set reading order, heading levels, image roles, table widths and page transitions. Keep content references separate from design settings. Load [page composition](references/page-composition.md) for dense material, landscape sections or split project pages.
4. **Choose and resolve design.** Apply precedence: explicit user constraint → selected template/layout → supplied brand guide → preset → local component default. Use [preset files](assets/presets/) as the numeric source of truth. Override them in a task configuration rather than editing shared values for one document. Check font availability and preserve Cyrillic, math and special glyphs.
5. **Author deterministically.** Use `python-docx` with [document_tools.py](scripts/document_tools.py) for supported operations and focused OOXML patches where needed. Keep real headings, true numbering, editable tables and native formulas. Use existing template styles when selected. Preserve unrelated parts; do not flatten fields, revisions or drawings by replacing whole paragraphs indiscriminately.
6. **Validate content and structure.** Run `document_tool.py validate OUTPUT.docx`. Supply `--expected-text inventory.txt` when exact source coverage matters. Compare media, hyperlinks and structural counts with the source according to the chosen edit route. Resolve every unexplained loss or duplicate. The validator reports structural errors and warnings; it cannot certify factual correctness or page appearance.
7. **Render and inspect every page.** Use the environment's documents renderer (`render_docx.py`) or an explicitly selected native Word/LibreOffice rendering workflow. Inspect full-resolution page images, not only a contact sheet. Apply [visual QA](references/visual-qa.md), fix defects and rerender after each layout change. If rendering is unavailable, report the specific limitation; do not claim visual verification.
8. **Deliver and persist.** Save the final DOCX in the project's designated export location or the user-requested destination. Keep build scripts, renders and content inventories in temporary work unless the project requires otherwise. Record source revision, checks and limitations in the Issue or handoff. Deliver only requested formats; render intermediates are not additional deliverables.

## Use the toolkit

Use the environment-owned Python runtime where provided; otherwise use a project environment with `python-docx`, `lxml` and `Pillow`. Do not install globally or fetch dependencies silently. Commands below use `python` as a placeholder for that interpreter.

```bash
python scripts/document_tool.py new --preset technical --out report.docx
python scripts/document_tool.py inspect reference.docx --out reference-inventory.json
python scripts/document_tool.py apply-preset input.docx --preset minimal --out styled.docx --restyle
python scripts/document_tool.py validate result.docx --expected-text source-inventory.txt
python scripts/generate_examples.py --out /temporary/examples
python scripts/test_toolkit.py
```

`new` creates the styled foundation, not a finished report. `apply-preset` changes named styles and geometry without stripping direct formatting or repairing arbitrary objects. Never invoke it on a selected template unless restyling was requested. Import the helpers for full authoring; read [toolkit contract](references/toolkit.md) for APIs and limits.

## Quality gates

- Every required source block is accounted for, and content is editable.
- Visual roles use named styles; explicit component exceptions are deliberate.
- Selected template identity survives, including legitimate layout tables and source-image proportions.
- Package, relationships, numbering and relevant objects remain valid.
- All latest rendered pages have been reviewed; no clipping, unintended blanks, collisions, missing glyphs, stranded headings or unreadable technical graphics remain.
- Do not shrink text or discard content merely to fit a template's old page count.

## Supporting materials

- [Design system](references/design-system.md): four presets, style roles, overrides and fonts.
- [Components](references/components.md): covers, tables, figures, notes, lists, formulas and navigation.
- [Composition](references/page-composition.md): page archetypes and concrete repair decisions.
- [Templates and editing](references/templates-and-editing.md): source/style mapping and safe mutation.
- [DOCX mechanics](references/docx-mechanics.md): sections, styles, numbering, fields, relationships and fragile objects.
- [Visual QA](references/visual-qa.md): render loop and measurable review checks.
- [Toolkit](references/toolkit.md): executable APIs, supported operations and tests.
- [Sources](references/sources.md): external inspiration and provenance.
