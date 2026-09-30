# Toolkit contract

## Dependencies and execution
Use Python 3.10+ with python-docx, lxml and Pillow. Prefer the environment-owned runtime. These helpers are original source; they do not vendor an external Word framework.

## Importable helpers
Import document_tools from this directory using a task-local Python import path.

| API | Behavior |
| --- | --- |
| load_preset(name_or_path) | Read validated JSON design settings; four names supported |
| resolve_fonts(config, available_fonts=None) | Resolve a copied preset against supplied font names or Fontconfig; return effective settings and substitutions |
| apply_preset(doc, config, geometry=True) | Set named paragraph styles and optionally geometry |
| add_text(parent, text_or_spans, style) | Add editable text; spans accept text/bold/italic/code/link |
| add_list(parent, text, level, ordered, num_id) | Add real nine-level numbering; return paragraph and concrete ID |
| add_data_table(doc, headers, rows, widths_mm, config) | Create a fixed-width editable table with repeating header |
| add_layout_table(doc, widths_mm, gutter_mm) | Create a borderless composition grid; caller owns page-fit decisions |
| add_figure(parent, path, width_mm, max_height_mm, alt) | Insert inline raster image, preserved aspect ratio and width limits |
| add_field(paragraph, instruction, cached) | Insert supported local Word field; no update engine |
| add_omml(paragraph, xml) | Insert native supplied OMML; no LaTeX parsing |
| package_report(path) | Inspect/validate ZIP/XML/relationships and inventory structures |
| body_text(path) | Extract body paragraph text including table/text-box stories |
| source_coverage(path, expected_lines) | Check normalized text-line presence and expected occurrence counts |

Selected templates can be opened with Document(template); do not apply_preset unless a restyle is authorized. add_layout_table is deliberately available for portfolio designs but should not turn ordinary reports into cell-based prose.

The example generator resolves fonts from the local inventory when Fontconfig is available and prints substitutions. Other callers explicitly choose whether to use the requested settings or a resolved copy. Never silently resolve or replace fonts in a selected template.

## CLI
- inspect INPUT --out JSON: package inventory and validation report; no mutation.
- validate INPUT [--expected-text FILE]: fail on structural errors or missing expected text. Inventory lines are literal text, not Markdown. Repeated equal lines specify required occurrence counts; extra occurrence counts are warnings unless --exact-counts is given.
- new --preset NAME --out DOCX: create a styled empty foundation.
- apply-preset INPUT --preset NAME --out DOCX --restyle: restyle a copy; refuse same-path overwrite; direct formatting remains.
- generate_examples.py --out DIR: create four two-page semantic examples and a source chart. Does not render or approve them.
- test_toolkit.py: exercise meaningful integrity and fidelity checks in temporary files, including broken relationship rejection and real list IDs.

## Limits
No renderer is bundled. No generic Markdown parser, full template copier, arbitrary OOXML repair engine or automatic page balancer is promised. SVG/native Office compatibility, complex revision handling and field refresh require specialized task code/tools. Strict shape preservation is not inferred from successful file reopening.

## Output safety
Write new paths by default. The CLI refuses replacing its input. Validate after authoring and after focused OOXML changes. Rebuilds require a source inventory and explicit task authority; tool convenience is not permission to discard existing bodies.
