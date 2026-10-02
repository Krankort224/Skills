# Toolkit contract

## Dependencies and execution
Use the runtime/dependency rules in `../SKILL.md`. These helpers are original source; they do not vendor an external Word framework. `preset_markdown.py` parses the canonical parameter table without a Markdown-engine dependency; `extract_preset.py` creates a bounded borrowing draft.

## Importable helpers
Import document_tools from this directory using a task-local Python import path.

| API | Behavior |
| --- | --- |
| load_preset(name_or_path, allow_draft=False) | Read validated single-file Markdown settings by library name or MD path; reject drafts by default |
| resolve_fonts(config, available_fonts=None) | Resolve a copied preset against supplied font names or Fontconfig; return effective settings and substitutions |
| apply_preset(doc, config, geometry=True) | Set named paragraph styles and optionally geometry |
| add_text(parent, text_or_spans, style) | Add editable text; spans accept text/bold/italic/code/link |
| add_list(parent, text, level=0, ordered=False, num_id=None, config=None) | Add real nine-level numbering; return paragraph and concrete ID |
| add_data_table(doc, headers, rows, widths_mm, config) | Create a fixed-width editable table with repeating header |
| add_layout_table(doc, widths_mm, gutter_mm) | Create a borderless composition grid; caller owns page-fit decisions |
| add_figure(parent, path, width_mm, max_height_mm, alt) | Insert inline raster image, preserved aspect ratio and width limits |
| add_field(paragraph, instruction, cached) | Insert supported local Word field; no update engine |
| add_omml(paragraph, xml) | Insert native supplied OMML; no LaTeX parsing |
| package_report(path) | Inspect/validate ZIP/XML/relationships and inventory structures |
| body_text(path) | Extract body paragraph text including table/text-box stories |
| source_coverage(path, expected_lines) | Check normalized text-line presence and expected occurrence counts |

Selected templates can be opened with Document(template); do not apply_preset unless a restyle is authorized. add_layout_table is deliberately available for portfolio designs but should not turn ordinary reports into cell-based prose.

Package counts cover the main document, headers, footers, notes and comments; `story_counts` preserves each part's separate inventory. Both simple and complex fields are counted. Source coverage intentionally checks the main document only, so a duplicate fact in a footer cannot hide missing body content.

The example generator resolves fonts from the local inventory when Fontconfig is available and prints substitutions. Other callers explicitly choose whether to use the requested settings or a resolved copy. Never silently resolve or replace fonts in a selected template.

## CLI
- extract-preset INPUT --base NAME_OR_MD --section INDEX --out DRAFT.md: capture selected section geometry and explicitly defined paragraph-style properties for matching semantic roles. Section index is zero based. Require an explicit base for defaulted fields, write a draft MD, and print extraction diagnostics. Do not overwrite an existing output. Follow the borrowing operation before setting Status: ready.
- inspect INPUT --out JSON: package inventory and validation report; no mutation.
- validate INPUT [--expected-text FILE]: fail on structural errors or missing expected text. Inventory lines are literal text, not Markdown. Repeated equal lines specify required occurrence counts; extra occurrence counts are warnings unless --exact-counts is given.
- new --preset NAME_OR_MD --out DOCX: create a styled empty foundation; refuse existing output paths.
- apply-preset INPUT --preset NAME_OR_MD --out DOCX --restyle: restyle a copy; refuse same-path overwrite and existing outputs; direct formatting remains. It changes named paragraph styles and shared section geometry only. It does not apply narrative rules, remap custom styles, or handle multiple section variants automatically.
- generate_examples.py --out DIR: create four two-page semantic examples and a source chart. Does not render or approve them.
- test_toolkit.py: exercise meaningful integrity and fidelity checks in temporary files, including broken relationship rejection and real list IDs.

## Limits
No renderer is bundled. No generic Markdown parser, full template copier, arbitrary OOXML repair engine or automatic page balancer is promised. SVG/native Office compatibility, complex revision handling and field refresh require specialized task code/tools. Strict shape preservation is not inferred from successful file reopening.

The borrowing extractor does not resolve inherited/theme formatting, absolute line heights, arbitrary/custom style mappings, linked numbering, table styles, columns, header/footer bodies, media or direct overrides. Its observations identify these review needs without transferring source text. Defaults are explicitly listed in the same MD. Draft status remains until the supported capture has been reviewed and visually reproduced.

The Markdown loader reads executable settings, not narrative composition. Read the whole preset in the operation and implement those rules separately. Parameter-key segments cannot contain dots, backslashes or line breaks; rename/map such roles explicitly. Table pipes are escaped as `\|`. Read [preset format](preset-format.md) for file ownership, status and schema.

## Output safety
Write new paths by default. The CLI refuses replacing its input. Validate after authoring and after focused OOXML changes. Rebuilds require a source inventory and explicit task authority; tool convenience is not permission to discard existing bodies.
