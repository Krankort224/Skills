---
name: markdown-to-word
description: Convert or copy Markdown (.md) into an editable Word DOCX while preserving semantic structure. Use for Markdown-to-Word exports with headings, nested lists, tables, links, images, quotes, code, task lists, and mathematical expressions; optionally map to an existing Word template without redesigning it.
metadata:
  short-description: Convert Markdown into editable Word
---

# Markdown to Word

Own the **translation of Markdown semantics** into an editable DOCX. Keep the Markdown source authoritative and preserve its order, wording, and meaningful structure. Add only the formatting needed to represent those roles in Word.

## Route and boundary

- Use this skill for Markdown to DOCX conversion. For Word authoring, design, and final verification, follow `document-creation` while retaining ownership of Markdown interpretation.
- Apply an optional supplied Word template's existing styles; do not redesign them. For delicate OOXML, fields, numbering, or template mechanics, follow `document-creation` without transferring Markdown interpretation to it.
- Do not treat raw HTML or unsupported extensions as plain text silently. Do not rasterize formulas or replace missing images with placeholders without telling the user.

## Workflow

1. Inspect the Markdown and local assets. Identify its flavor and extensions, heading levels, mixed and nested lists, tables, links, images, task markers, code fences, quotations, footnotes, and inline or display math. Resolve relative image paths against the source file. Check the converter's actual feature support before choosing it; use a Markdown parser with a token tree rather than regex substitutions for nested constructs.
2. If a template is supplied, inspect its paragraph, character, table, and numbering styles. Map each Markdown role to a compatible named Word style. Keep template geometry, theme, and branding; use a plain, readable default style set if no template exists. Reject missing or incompatible style mappings before conversion.
3. Convert headings to real Heading 1–6 paragraphs; list items to actual Word list numbering with correct level and restart; tables to editable cells; links to hyperlink relationships; local images to embedded media with alt text where available; quotes and code to distinct named styles. Preserve inline emphasis and literal code. Represent task markers as editable checkboxes when supported, or as explicit textual boxes and report the substitution.
4. Handle `$...$` and `$$...$$` only when they are intended as math in the chosen Markdown flavor. Prefer a validated LaTeX → MathML → OMML route for Word-native editable equations; inspect the resulting math nodes and rendered expressions. If conversion of a formula fails or is unavailable, keep the source expression visible and flag the affected location. Never silently replace it with an image or omit it.
5. Detect unsupported structures with source locations, including raw HTML, complex merged tables, or unresolved assets. Fix the conversion method if feasible; otherwise report a precise limitation. Preserve the original Markdown and do not claim a lossless conversion when a feature was downgraded.
6. Reopen the DOCX, inspect semantic counts and representative complex elements against the Markdown, and render the document. Check nested numbering, hyperlinks, images, code spacing, table overflow, task markers, and equations in the resulting pages. Deliver the editable DOCX and any explicit conversion exceptions.

## Quality bar

- Document structure uses named Word styles and native elements where available, not only visual imitation.
- Text, ordering, links, and local assets match the Markdown; conversion exceptions are visible and traceable to source positions.
- A supplied template remains the style authority. Any later visual improvement belongs to `document-creation`.
