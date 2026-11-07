# Markdown as creation input

Read this reference only when creating Word from Markdown. It owns Markdown interpretation inside style-transfer; it does not define a separate skill or formatting library.

## Inventory and parser

Identify the intended Markdown dialect and extensions. Inventory headings, mixed/nested lists and restarts, tables, links/anchors, inline/block images, quotes, code, tasks, footnotes, raw HTML, mathematical expressions and custom fenced blocks. Resolve local assets relative to the source document.

Use a real parser/token tree or an available conversion backend with demonstrated support for the selected dialect. Do not parse arbitrary Markdown with a collection of regular expressions. Check the actual installed backend/version; Python DOCX helpers do not supply a Markdown or LaTeX parser. Do not silently install a missing backend.

## Semantic mapping

Map parsed headings to real Word headings; lists to numbering with correct levels/start/continuation; tables to editable cells; links to relationships/bookmarks; graphics to correctly sized embedded assets; quotes/code to named styles; inline emphasis to spans. Preserve multi-block list items and cell formatting. Represent task state with supported editable controls or visible checkbox text and report which representation was used.

For math, use a vetted backend producing native OMML, either directly or through validated intermediate formats. Distinguish literal currency/escaped dollars from math according to the chosen dialect. Check equations in XML and render; unsupported TeX remains visible and flagged at its source location. No silent image replacement or missing formula is acceptable.

## Unsupported content

Do not infer raw HTML, Mermaid or merged-table support from general Markdown support. Convert with a supported method or preserve visible source with a precise exception. When a diagram becomes an image, retain its source outside the DOCX if required and state that its internals are not editable Word objects. Record unresolved assets, lost attributes and unsupported extensions by source location.

## Verify

Compare source and output text/order, heading levels, list starts/nesting, table rows/cells, links/anchors, notes, images and math. Inspect representative complex structures and all rendered pages. Apply the selected preset through the creation operation after semantic conversion; the converted document is not complete until its content, structure and layout have been checked.
