# Borrowing formatting

Input: an existing Word DOCX chosen as a design example. Output: one reusable Markdown preset and its neutral rendered preview, with explicit reproduction limits. Use an ASCII lowercase hyphenated library name chosen from the document's design purpose, not personal source content.

## 1. Inspect the example

Read [templates and editing](../references/templates-and-editing.md), [design system](../references/design-system.md) and [preset format](../references/preset-format.md). Run `document_tool.py inspect` and render the source. Inspect representative roles across all source pages, styles and their inheritance, direct formatting, section geometry, theme/fonts, numbering, tables, headers/footers, fields and graphics. Keep the inventory in task-local work.

Distinguish reusable formatting from incidental content and one-off corrections. Identify variants such as cover/body/appendix sections, first/even-page headers, layout tables and numbering sequences. Do not infer a complete design from Normal or the first page alone.

## 2. Extract a draft

Run `document_tool.py extract-preset SOURCE.docx --out DRAFT.md --section INDEX --base technical` with an explicitly selected base (the name here is an example, not a required choice). The helper extracts a bounded subset of section geometry and paragraph-style properties; its output remains a draft with unobserved values and direct-formatting observations. The base supplies identified defaults, not evidence from the source. It does not capture full themes, numbering, multi-section composition, drawings or header/footer bodies.

Review all defaulted and unsupported fields. Investigate effective inherited styles and repeated direct formatting when required. Use [DOCX mechanics](../references/docx-mechanics.md) for package-level evidence. Record source revision/hash, inspected regions and confidence in the preset's provenance without copying factual body text.

## 3. Complete the reusable rules

Put all design information in the one MD: numeric/style parameters, role mappings, section variants, component patterns, composition, adaptation rules, font/asset dependencies and known limits. Use the canonical parameter table for executable settings; use prose/tables for rules requiring layout decisions or specialized code. Mark which values remain deliberate defaults or interpretations. Do not invent captured support for objects the tool cannot reproduce.

Link necessary reusable graphics beside the preset. Keep private source assets and factual source pages out of the shared library. If a required design depends on something unavailable, retain draft status and report the gap.

## 4. Reproduce and verify

Build a neutral demonstration exercising every claimed captured role and section variant, including source-specific structures not covered by the generic example generator. Compare its rendered appearance with the source: typography, spacing, proportions, table treatment, section transitions and header/footer composition. Check exact executable values and editable structure. Read [components](../references/components.md), [composition](../references/page-composition.md) and [visual QA](../references/visual-qa.md) as needed.

Repair the MD or implementation and repeat until the supported design is reproduced. Explicitly narrow the preset's coverage when a feature cannot be captured. Do not use the source's factual text as demonstration content.

## 5. Save the library entry

Set `Status: ready` only after the supported coverage and declared defaults have been reviewed and reproduction checked. Save `assets/presets/<name>.md`, its required assets, and `assets/examples/<name>.png`. Link the preview and any dependency from the MD. Update the skill's library navigation when adding an entry. Persist through the skill's repository workflow; avoid altering an unrelated shared preset.

Report the saved name, supported scope, checks and remaining limits. The original DOCX must not be needed to apply the preset.
