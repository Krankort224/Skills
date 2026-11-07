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

## Data contracts

The example generator resolves fonts from Fontconfig when available and reports substitutions. Other callers explicitly choose requested settings or a resolved copy; selected templates are never silently rewritten.

`add_text` accepts strings or spans with `text`, `bold`, `italic`, `code` and `link`. List levels are zero-based (0–8); reuse returned concrete numbering IDs for continuation and request a new ID for restarts. Table row lengths must match headers and widths; callers own content and page-fit decisions. `add_figure` preserves raster aspect ratios; `add_omml` accepts native XML, without LaTeX conversion. Fields receive local instructions and optional cached text, with no calculation engine.

## CLI
- show-preset NAME_OR_MD [--section HEADING] [--parameter PATH]: validate the complete MD, then print all narrative by default, excluding Parameters. Repeat either selector for exact sections or typed parameter rows; unknown/ambiguous selections fail. Draft viewing is allowed and visibly labeled; ordinary application still rejects drafts. No writes or asset downloads.
- extract-preset INPUT --base NAME_OR_MD --section INDEX --out DRAFT.md: capture selected section geometry and explicitly defined paragraph-style properties for matching semantic roles. Section index is zero based. Require an explicit base for defaulted fields, write a draft MD, and print extraction diagnostics. Do not overwrite an existing output. Follow the borrowing operation before setting Status: ready.
- inspect INPUT --out JSON: package inventory and validation report; no mutation.
- validate INPUT [--expected-text FILE]: fail on structural errors or missing expected text. Inventory lines are literal text, not Markdown. Repeated equal lines specify required occurrence counts; extra occurrence counts are warnings unless --exact-counts is given.
- new --preset NAME_OR_MD --out DOCX: create a styled empty foundation; refuse existing output paths.
- apply-preset INPUT --preset NAME_OR_MD --out DOCX --restyle: restyle a copy; refuse same-path overwrite and existing outputs; direct formatting remains. It changes named paragraph styles and shared section geometry only. It does not apply narrative rules, remap custom styles, or handle multiple section variants automatically.
- generate_examples.py --out DIR: create four two-page semantic examples and a source chart. Does not render or approve them.
- test_toolkit.py: exercise meaningful integrity and fidelity checks in temporary files, including broken relationship rejection and real list IDs.
- test_preset_view.py: check narrative completeness, exact selections, drafts, invalid inputs and absence of mutation.

## Limits
No renderer is bundled. No generic Markdown parser, full template copier, arbitrary OOXML repair engine or automatic page balancer is promised. SVG/native Office compatibility, complex revision handling and field refresh require specialized task code/tools. Strict shape preservation is not inferred from successful file reopening.

The borrowing extractor does not resolve inherited/theme formatting, absolute line heights, arbitrary/custom style mappings, linked numbering, table styles, columns, header/footer bodies, media or direct overrides. Its observations identify these review needs without transferring source text. Defaults are explicitly listed in the same MD. Draft status remains until the supported capture has been reviewed and visually reproduced.

The loader reads executable settings; implement narrative composition separately after reviewing all narrative with `show-preset`. Parameter-key segments cannot contain dots, backslashes or line breaks; map incompatible roles explicitly. Table pipes are escaped as `\|`; [preset format](preset-format.md) owns serialization and review rules.

Creation, restyling and extraction refuse existing outputs; restyling also refuses same-path overwrite. Inspection/validation reports may replace their specified report path. Verification and rebuild authority follow the root principles.
