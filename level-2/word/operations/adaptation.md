# Adapting an existing Word document

Input: a target Word DOCX and a selected ready preset or reference. Output: a restyled Word document with preserved content and verified pages. Borrow a supplied reference first when reusable formatting is requested or no saved preset exists.

## 1. Inventory the target and select formatting

Read the selected preset completely, [templates and editing](../references/templates-and-editing.md) and [toolkit](../references/toolkit.md). Inspect the target and render its original pages. Inventory content, styles, direct formatting, sections, tables, graphics, formulas, links, fields, revisions and non-body stories relevant to the change. Record protected regions and intended changes outside the output.

Use a new output path. Classify the work as targeted edit, restyle or authorized rebuild. Preserve content and objects unless their change is separately in scope.

## 2. Map roles and resolve conflicts

Map target headings, body, captions, list levels, table types and section variants to the preset's semantic roles. Resolve style names/IDs through inspected definitions rather than matching names blindly. Identify intentional run emphasis and direct formatting that overrides the selected design.

Choose how the preset adapts to current content length, wide tables and graphics. Apply any task override in memory or a temporary MD copy. Load [design system](../references/design-system.md), [components](../references/components.md) and [page composition](../references/page-composition.md) for the affected design decisions.

## 3. Apply supported settings and detailed rules

Use `document_tool.py apply-preset INPUT.docx --preset NAME_OR_MD --out OUTPUT.docx --restyle` only for the helper's supported named styles and shared section geometry. It preserves direct formatting and does not remap arbitrary target styles or apply the preset's narrative composition automatically. Never overwrite all sections' geometry when distinct target/preset section roles need different treatment.

Complete semantic remapping, selective override changes, tables, numbering, header/footer and composition rules with supported helpers or focused task-local OOXML code. Read [DOCX mechanics](../references/docx-mechanics.md) for fragile structures. Preserve existing equations, media and relationships. Report unsupported required transfers instead of silently flattening them.

## 4. Verify and repair

Compare content order and counts, meaningful inline formatting, media, links, bookmarks, equations and protected regions with the original. Explain expected changes such as pagination or selected header styling. Run package validation and source coverage checks, then render and inspect every page using [visual QA](../references/visual-qa.md).

Fix style conflicts, broken navigation and page-fit defects, then rerender. A preserved text inventory alone does not prove safe restyling.

## 5. Deliver

Save the final Word at the requested destination. Report the preset used, any explicit overrides, structural and visual checks, and specific limitations. Do not update the library merely because one target required a local adaptation.
