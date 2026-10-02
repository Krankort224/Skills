# Minimal style preset

Status: ready

## Purpose

Quiet, neutral documents with simple grayscale tables and a clear hierarchy.

## Semantic roles

Normal is body prose. Title and Subtitle form the opening hierarchy. Metadata holds document context. Heading styles form the section hierarchy. Caption labels figures and tables. Code Block uses a monospace face. Table Text is compact cell content. Note marks qualifications.

## Composition

Use named styles to express meaning; keep headings with their following content. The palette distinguishes primary text, secondary text, table headers, alternating rows, borders, and note backgrounds. Table padding and list indentation belong to the reusable design. Footer parameters style page fields when the author inserts them.

## Adaptation

Borrow this complete file as a starting point. Change the canonical parameter table for the target document, keep semantic roles explicit, and render a representative page before adopting the result. Font substitution changes layout and must be checked. Applying the preset changes section geometry and named paragraph styles; component helpers use the table, list, palette, and footer settings during document creation.

## Dependencies

Requires python-docx and the document toolkit to apply parameters. Fonts must be installed or substituted using the fallback map in the table. No binary template is required. The preview is an illustration; parameters are authoritative.

## Provenance

Migrated without parameter changes from the original authored preset. This preset is not an extraction of a supplied Word reference and makes no institutional compliance claim.

[Preview](../examples/minimal.png)

## Parameters

| Path | Value | Type | Unit |
| --- | --- | --- | --- |
| version | 1 | number | - |
| name | minimal | string | - |
| page.width_mm | 210 | number | mm |
| page.height_mm | 297 | number | mm |
| page.margins_mm.left | 25 | number | mm |
| page.margins_mm.right | 25 | number | mm |
| page.margins_mm.top | 25 | number | mm |
| page.margins_mm.bottom | 25 | number | mm |
| page.header_mm | 10 | number | mm |
| page.footer_mm | 10 | number | mm |
| fonts.body | Arial | string | - |
| fonts.code | Consolas | string | - |
| fonts.fallbacks.Arial | Liberation Sans | string | - |
| fonts.fallbacks.Calibri | Carlito | string | - |
| fonts.fallbacks.Times New Roman | Liberation Serif | string | - |
| fonts.fallbacks.Consolas | Liberation Mono | string | - |
| palette.ink | 000000 | string | - |
| palette.muted | 555555 | string | - |
| palette.accent | 333333 | string | - |
| palette.table_header | F2F2F2 | string | - |
| palette.table_header_text | 000000 | string | - |
| palette.alternating_row | F7F7F7 | string | - |
| palette.border | D9D9D9 | string | - |
| palette.note_background | F3F5F7 | string | - |
| styles.Normal.font | Arial | string | - |
| styles.Normal.size_pt | 11 | number | pt |
| styles.Normal.line_spacing | 1.2 | number | ratio |
| styles.Normal.before_pt | 0 | number | pt |
| styles.Normal.after_pt | 6 | number | pt |
| styles.Normal.color | 000000 | string | - |
| styles.Title.font | Arial | string | - |
| styles.Title.size_pt | 28 | number | pt |
| styles.Title.bold | true | boolean | - |
| styles.Title.before_pt | 0 | number | pt |
| styles.Title.after_pt | 12 | number | pt |
| styles.Title.color | 000000 | string | - |
| styles.Title.keep_with_next | true | boolean | - |
| styles.Subtitle.font | Arial | string | - |
| styles.Subtitle.size_pt | 12 | number | pt |
| styles.Subtitle.before_pt | 0 | number | pt |
| styles.Subtitle.after_pt | 12 | number | pt |
| styles.Subtitle.color | 555555 | string | - |
| styles.Subtitle.keep_with_next | true | boolean | - |
| styles.Caption.font | Arial | string | - |
| styles.Caption.size_pt | 10 | number | pt |
| styles.Caption.before_pt | 4 | number | pt |
| styles.Caption.after_pt | 8 | number | pt |
| styles.Caption.color | 555555 | string | - |
| styles.Metadata.font | Arial | string | - |
| styles.Metadata.size_pt | 10 | number | pt |
| styles.Metadata.before_pt | 0 | number | pt |
| styles.Metadata.after_pt | 4 | number | pt |
| styles.Metadata.color | 555555 | string | - |
| styles.Code Block.font | Consolas | string | - |
| styles.Code Block.size_pt | 10 | number | pt |
| styles.Code Block.line_spacing | 1.05 | number | ratio |
| styles.Code Block.before_pt | 4 | number | pt |
| styles.Code Block.after_pt | 8 | number | pt |
| styles.Code Block.color | 000000 | string | - |
| styles.Table Text.font | Arial | string | - |
| styles.Table Text.size_pt | 10 | number | pt |
| styles.Table Text.line_spacing | 1.1 | number | ratio |
| styles.Table Text.before_pt | 0 | number | pt |
| styles.Table Text.after_pt | 3 | number | pt |
| styles.Table Text.color | 000000 | string | - |
| styles.Note.font | Arial | string | - |
| styles.Note.size_pt | 10.5 | number | pt |
| styles.Note.before_pt | 4 | number | pt |
| styles.Note.after_pt | 8 | number | pt |
| styles.Note.color | 333333 | string | - |
| styles.Heading 1.font | Arial | string | - |
| styles.Heading 1.size_pt | 20 | number | pt |
| styles.Heading 1.bold | true | boolean | - |
| styles.Heading 1.before_pt | 16 | number | pt |
| styles.Heading 1.after_pt | 8 | number | pt |
| styles.Heading 1.color | 000000 | string | - |
| styles.Heading 1.keep_with_next | true | boolean | - |
| styles.Heading 2.font | Arial | string | - |
| styles.Heading 2.size_pt | 14 | number | pt |
| styles.Heading 2.bold | true | boolean | - |
| styles.Heading 2.before_pt | 14 | number | pt |
| styles.Heading 2.after_pt | 7 | number | pt |
| styles.Heading 2.color | 000000 | string | - |
| styles.Heading 2.keep_with_next | true | boolean | - |
| styles.Heading 3.font | Arial | string | - |
| styles.Heading 3.size_pt | 12 | number | pt |
| styles.Heading 3.bold | true | boolean | - |
| styles.Heading 3.before_pt | 12 | number | pt |
| styles.Heading 3.after_pt | 6 | number | pt |
| styles.Heading 3.color | 000000 | string | - |
| styles.Heading 3.keep_with_next | true | boolean | - |
| styles.Heading 4.font | Arial | string | - |
| styles.Heading 4.size_pt | 11 | number | pt |
| styles.Heading 4.bold | true | boolean | - |
| styles.Heading 4.before_pt | 10 | number | pt |
| styles.Heading 4.after_pt | 5 | number | pt |
| styles.Heading 4.color | 000000 | string | - |
| styles.Heading 4.keep_with_next | true | boolean | - |
| styles.Heading 5.font | Arial | string | - |
| styles.Heading 5.size_pt | 11 | number | pt |
| styles.Heading 5.bold | true | boolean | - |
| styles.Heading 5.before_pt | 8 | number | pt |
| styles.Heading 5.after_pt | 4 | number | pt |
| styles.Heading 5.color | 000000 | string | - |
| styles.Heading 5.keep_with_next | true | boolean | - |
| styles.Heading 6.font | Arial | string | - |
| styles.Heading 6.size_pt | 10.5 | number | pt |
| styles.Heading 6.bold | true | boolean | - |
| styles.Heading 6.before_pt | 6 | number | pt |
| styles.Heading 6.after_pt | 3 | number | pt |
| styles.Heading 6.color | 000000 | string | - |
| styles.Heading 6.keep_with_next | true | boolean | - |
| table.padding_mm.top | 2 | number | mm |
| table.padding_mm.bottom | 2 | number | mm |
| table.padding_mm.left | 2.5 | number | mm |
| table.padding_mm.right | 2.5 | number | mm |
| table.border_pt | 0.5 | number | pt |
| table.repeat_header | true | boolean | - |
| list.indent_mm | 8 | number | mm |
| list.hanging_mm | 5 | number | mm |
| list.level_step_mm | 6 | number | mm |
| list.after_pt | 4 | number | pt |
| footer.size_pt | 9 | number | pt |
| footer.color | 666666 | string | - |
