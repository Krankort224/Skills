# Creation

Input: canonical content and selected design. Output: an editable Word document. Apply the common principles in `../SKILL.md`.

## Structure and select

Identify canonical revisions, audience, sections, assets and required metadata. Inventory content blocks and semantic roles; resolve factual gaps before authoring. For Markdown, read [Markdown input](../references/markdown-input.md) before conversion.

Read all selected preset narrative with `show-preset NAME_OR_MD`. If a live reference needs reusable capture, use borrowing first. Consult design, component or composition sections only for unresolved roles or actual layout structures. Plan reading order, title/cover, section variants, widths, graphics and breaks against the source inventory.

## Author

Read [CLI](../references/toolkit.md#cli) and [limits](../references/toolkit.md#limits):

```sh
python scripts/document_tool.py new --preset NAME_OR_MD --out OUTPUT.docx
```

This creates a styled empty foundation. Use relevant [helper rows](../references/toolkit.md#importable-helpers) and [data contracts](../references/toolkit.md#data-contracts) to populate editable content; implement narrative composition and section variants explicitly. Open a native template directly when preserving its layout is required. Loading parameters alone does not implement the whole design.

## Verify and deliver

Compare the complete content/asset inventory and reading order. Refresh local fields through a capable application. Complete the root verification gate and [visual QA](../references/visual-qa.md), repairing and rerendering as needed. Deliver requested formats with specific limitations; keep accounting and checks outside the final document.
