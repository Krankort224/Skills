# Creating a Word document

Input: canonical content and any chosen preset, reference or explicit design constraints. Output: an editable Word document with complete content, deliberate composition and verified pages.

## 1. Ground and structure content

Identify canonical source revisions, audience, intended use, required sections, graphics and factual metadata. Create a task-local source inventory and destination map. Resolve contradictions and missing required facts before drafting claims. Use source wording unless rewriting is authorized.

For Markdown input, read [Markdown input](../references/markdown-input.md) and inventory its dialect and extensions before conversion. Preserve its semantic structure; format and verify the resulting DOCX within this operation.

## 2. Resolve design

Read a selected preset completely. If a live Word reference is the design authority, inspect it and use [borrowing](borrowing.md) when a reusable capture is required. Without a selected reference, choose an existing preset from the content's purpose or use deliberate task-local settings. Read [design system](../references/design-system.md) and [components](../references/components.md); load [composition](../references/page-composition.md) for dense, wide or editorial material.

Plan semantic roles, reading order, cover/title choice, section variants, table widths, image sizes and genuine page transitions. Resolve fonts without editing shared settings. Template example text is not source content.

## 3. Author

Read [toolkit](../references/toolkit.md). `document_tool.py new --preset NAME_OR_MD --out OUTPUT.docx` creates a styled foundation, not a finished document. Use importable helpers to insert actual text, native lists, editable tables, figures, fields and validated OMML. Use [DOCX mechanics](../references/docx-mechanics.md) where focused package changes are needed.

Apply both the preset's executable parameters and its narrative composition/component rules. A generic helper cannot implement every saved layout. Build variants explicitly and account for every canonical content block. Open an existing template as a foundation only when retaining its native layout is part of the chosen route.

## 4. Validate and compose final pages

Reopen the DOCX, run package validation, and compare expected content/order/counts and selected assets. Update supported local fields using a capable application where necessary. Render and inspect every page using [visual QA](../references/visual-qa.md). Repair layout and repeat after changes.

Check source coverage separately from appearance. Preserve the intended reading order, formula editability and internal navigation. Record unavailable checks and unsupported features as limitations.

## 5. Deliver

Save at the requested destination and return only requested formats. Report checks and limitations concisely. Keep neutral demonstrations, build scripts and inventories outside the final document and temporary unless persistence is required.
