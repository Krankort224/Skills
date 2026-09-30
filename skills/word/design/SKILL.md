---
name: word-design
description: Design or restyle the visual presentation of a Word DOCX document. Use for requests to make a report polished, corporate, technical, academic, or minimal; improve typography, page layout, tables, title pages, callouts, and header or footer appearance while preserving content and structure.
metadata:
  short-description: Design Word document layouts
---

# Word design

Own the **visual choices** in an editable Word document. Preserve its meaning, reading order, data, links, fields, and semantic structure unless the user explicitly requests a content change.

## Route and boundary

- Use this skill for the appearance of an existing DOCX or the design phase of a newly created one.
- For Markdown input, first use `markdown-to-word` to transfer content and structure; apply the chosen design to the resulting DOCX.
- For inspection, repair, style or template transfer, section and field mechanics, follow `word-technical`. Its mechanical rules can support this skill without deciding the design.
- Do not parse Markdown, repair corrupt OOXML, replace document content to simplify layout, or invent data, branding, or a corporate identity.

## Workflow

1. Inspect the document and any supplied brand guide or reference. Identify heading levels, tables, images, captions, callouts, sections, page numbers, headers, footers, and repeated patterns. Record the existing page size and any fixed constraints.
2. Choose one restrained visual direction from the request or context. If unspecified, use a neutral technical default. Treat the directions below as starting points, not mandatory values:

   | Direction | Typical treatment |
   | --- | --- |
   | Minimal | Generous spacing, clear hierarchy, almost monochrome |
   | Technical | Dense but legible tables, numbered headings, precise captions |
   | Corporate | Consistent accent color, branded title and table headers |
   | Academic | Conservative typography, clear citations and figure numbering |

3. Define one coherent system before editing: page geometry and content width; body, heading, caption, code, and table styles; type sizes and spacing; a limited palette; table borders, fills, and cell padding; title and callout treatment; header, footer, and page-number placement. Use available fonts. Apply choices through named Word styles and theme settings where feasible, rather than styling every run independently.
4. Apply the system consistently. Preserve real headings and list numbering. Keep table headings readable, repeat header rows where useful, and avoid splitting short labels or isolated headings across pages. Use section breaks only when needed for a genuine layout change. Insert dynamic page-number fields rather than typed page numbers.
5. Render every page after the change and inspect cover, normal pages, dense tables, figures, page transitions, and the last page. Correct clipping, widows, accidental blanks, inconsistent spacing, low contrast, displaced captions, and header or footer collisions. Repeat until the rendered layout is coherent.
6. Verify that text, table values, links, images, and structural elements survived. Deliver the editable DOCX and briefly state the chosen direction and any remaining layout limitation.

## Quality bar

- The same role uses the same named style throughout the document.
- Page geometry and table widths fit the page; contrast, spacing, and heading hierarchy remain legible in the rendered pages.
- Brand colors or logos appear only when supplied or explicitly authorized.
- The visual result is checked as pages, not inferred from successful DOCX generation alone.
