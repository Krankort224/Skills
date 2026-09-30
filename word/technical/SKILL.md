---
name: word-technical
description: Inspect, edit, repair, or transfer the mechanics of an editable Word DOCX document. Use for preserving or copying styles and templates, sections, numbering, tables, fields, images, headers and footers, document integrity, or other structural Word changes requiring careful OOXML handling.
metadata:
  short-description: Edit Word structure safely
---

# Word technical

Own **DOCX inspection and deterministic mutation**. Preserve content and unrelated formatting. Apply a supplied formatting specification or reference faithfully; leave new aesthetic decisions to `word-design`.

## Route and boundary

- Use this skill when the task is to edit, fix, preserve, or copy Word formatting or structure, including sections, fields, numbering, styles, and headers or footers.
- `word-design` chooses a new visual system; this skill implements its structural operations when required. `markdown-to-word` owns Markdown interpretation and can use these DOCX mechanics. Neither workflow transfers its decisions here.
- Do not turn a repair or format transfer into a redesign, and do not reconstruct the entire document when a targeted edit suffices.

## Workflow

1. **Preflight.** Work on a copy. Inspect the ZIP package and relevant OOXML parts as well as paragraphs and tables. Inventory sections, styles, numbering definitions, relationships, images, hyperlinks, fields, bookmarks, headers, footers, notes, text boxes, content controls, tracked changes, and embedded objects relevant to the requested edit. Locate the exact range and note unsupported or fragile elements before mutation.
2. **Specify the change.** Express what must change separately from *where*: a concrete target and a rule, plus invariants for untouched content. If a reference DOCX is supplied, compare its relevant section settings, named styles, numbering, and header or footer definitions before mapping source roles to target roles. Do not infer a document's semantic roles solely from its direct font formatting when structure contradicts that inference.
3. **Edit deterministically.** Use a DOCX library for supported operations and targeted OOXML edits where the library cannot preserve required structures. Keep section references, field instructions and results, numbering links, content types, and package relationships consistent. Avoid broad XML string replacement or round trips that silently flatten fields, formulas, images, tracked changes, or content controls. Refresh fields only with appropriate tooling and only when needed; never execute external field targets merely to update the document.
4. **Validate.** Reopen the output, check ZIP and XML integrity, relationship targets, expected styles and sections, and the requested properties. Compare the source and output's normalized text, tables, media, hyperlinks, and structural object counts where those were meant to remain stable. Investigate unexplained differences; a successful save is insufficient.
5. Render and inspect affected pages whenever layout may change. Check page breaks, headers and footers, numbering continuity, table overflow, and cross-references. If the environment cannot render or refresh a required field, identify that unverified part rather than claiming completion.

## Quality bar

- A localized change has a localized diff in document behavior; unrelated stories and parts remain intact.
- A reference template or style transfer preserves the target's content and uses the reference only for the requested formatting roles.
- Complex objects found in preflight are preserved, handled explicitly, or identified as a blocker before a destructive edit.
- The result is an editable DOCX whose package and visible layout have been checked to the extent the change requires.
