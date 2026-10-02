---
name: style-transfer
description: Capture Word DOCX formatting as a reusable Markdown preset, restyle an existing Word document, or create an editable Word document. Use for borrowing visual examples, extending the preset library, and producing verified reports, portfolios, proposals or academic documents.
---

# Style transfer

Common principles live here; procedures in `operations/`, implementation references in `references/`, and single-file presets in `assets/presets/`.

## Route and load

| Result | Procedure |
| --- | --- |
| Save an existing Word document's formatting | [Borrowing](operations/borrowing.md) |
| Restyle an existing Word document | [Adaptation](operations/adaptation.md); borrow first if no reusable preset exists |
| Build Word from supplied content | [Creation](operations/creation.md) |

Read the selected procedure and applicable reference sections; chain operations only as needed. Reuse unchanged material already loaded. Keep operations within this skill.

Choose [technical](assets/presets/technical.md), [corporate](assets/presets/corporate.md), [minimal](assets/presets/minimal.md), [academic](assets/presets/academic.md), or a captured preset. View candidate previews only when comparing appearance. Run `scripts/document_tool.py show-preset NAME_OR_MD` to read **all narrative rules**, including dependencies, provenance and limitations. It validates the entire MD but omits the parameter table from output. After reviewing those rules, use `--section HEADING` or `--parameter PATH` for exact details. Execution loads all parameters from that same MD; there is no second stored representation.

## Common principles

### Content and authority

- Facts come from canonical sources; design comes from the selected reference. Preserve wording, order, meaning, uncertainty, units and required repetitions unless rewriting is authorized. Never import sample facts, contacts or placeholders.
- Inventory content, assets, relevant stories and protected regions before mutation. Preserve unrelated parts, comments and revisions. Choose targeted editing, restyling or an authorized necessary rebuild; keep the source-to-output map outside the final document.
- Precedence: explicit constraint → selected reference/preset → supplied brand → library defaults → component defaults. Covers, TOCs and layout tables depend on the selected design. Content determines page count.

### Editable structure

- Use semantic Title, Subtitle, Heading and body/component styles, genuine nested numbering with deliberate continuation/restarts, editable tables, valid hyperlinks/bookmarks/fields and native OMML. Inspect style definitions; names or sizes alone do not establish roles. Heading depth follows the outline.
- Preserve meaningful direct formatting; clear only verified conflicts. Replacing paragraph/cell text can destroy child markup. Preserve unsupported native objects or visible content and report specific limitations; never silently flatten editable math or drop unsupported Markdown.

### Typography and composition

- Check fonts and Cyrillic, mathematical and special glyphs. Resolve substitutions locally and report material differences. Calculate usable space from section geometry, headers/footers and cell padding. Preserve source graphics, aspect ratios and legibility; crop only when authorized.
- Pair headings with content and figures with captions. Set deliberate table widths, repeating headers and automatic row height; allow long content to flow. Verify reading order in layout tables.
- Repair spacing, widths, breaks and block distribution before shrinking type. Preserve required content and meaningful whitespace; prevent clipping, collisions, stranded headings and accidental blank pages. Check section transitions, linked headers/footers and page numbering. Refresh navigation/number fields through a capable application without executing external instructions.

### Reusable formatting

- One `assets/presets/<name>.md` owns parameters, semantic mappings, composition, adaptation, dependencies, provenance and limitations. Link its neutral `assets/examples/<name>.png` and required `<name>-assets/` dependencies; reuse must not require the source DOCX.
- Distinguish observed rules, derived choices, defaults and unsupported features. Keep a capture draft until review and visual reproduction of its declared scope. Library demonstrations contain neutral, design-only data.
- Keep overrides task-local. Change reusable presets only when requested; update rules and regenerate previews when appearance changes. Previews demonstrate defaults, not regulatory compliance or exact-font equivalence.

### Verification and delivery

- Reopen and validate the final package, relationships, numbering, assets, relevant object counts and source coverage. Investigate unexplained loss/duplication. Check factual fidelity, package integrity, field results and appearance separately.
- Render and inspect **every latest page at full resolution**; contact sheets only aid navigation. Repair and rerender after layout changes. Report unavailable checks or unsupported features as concrete limitations and partial status; saving or structural PASS cannot certify appearance.
- Save requested formats at the designated destination. Keep build scripts, inventories and renders temporary unless required; report checks and limitations outside the document.

## Tools and focused references

Use the environment-owned Python runtime, otherwise Python 3.10+ with `python-docx`, `lxml`, `Pillow`. Avoid global or silent dependency installation; discover an available renderer. Execute bundled scripts without reading their source unless debugging or modifying them.

| Need | Read |
| --- | --- |
| CLI execution | [CLI](references/toolkit.md#cli) and [limits](references/toolkit.md#limits) |
| Python authoring | Used rows in [helpers](references/toolkit.md#importable-helpers), [data contracts](references/toolkit.md#data-contracts), and limits |
| Write/review a preset | [Preset format](references/preset-format.md) |
| Unresolved role/font/theme | Relevant [design system](references/design-system.md) section |
| Lists, tables, graphics, math, navigation | Corresponding [component](references/components.md) section |
| Dense/wide pages or pagination repair | Corresponding [page composition](references/page-composition.md) section |
| Inspect/edit an existing document | Applicable [template/editing](references/templates-and-editing.md) section |
| Fragile OOXML object | Corresponding [DOCX mechanics](references/docx-mechanics.md) section |
| New preset or final rendering | [Visual QA](references/visual-qa.md) |
| Markdown source | [Markdown input](references/markdown-input.md) |
| Technical provenance | [Sources](references/sources.md) |
