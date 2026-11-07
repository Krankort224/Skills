# Adaptation

Input: an existing Word document and selected formatting. Output: a restyled editable document. Apply the common principles in `../SKILL.md`.

## Inspect and map

Read all preset narrative with `show-preset NAME_OR_MD`. Inspect the relevant editing sections in [templates/editing](../references/templates-and-editing.md), then inventory/render the target, including objects, other stories, protected regions and direct formatting. Choose targeted editing, restyling or an authorized necessary rebuild; write a new output path.

Map semantic roles, numbering, table types and sections by inspected definitions, not names alone. Separate intentional emphasis from conflicting overrides. Read component/composition sections only for actual elements, content-length constraints or wide objects requiring decisions.

## Apply

Read [CLI](../references/toolkit.md#cli) and [limits](../references/toolkit.md#limits):

```sh
python scripts/document_tool.py apply-preset INPUT.docx --preset NAME_OR_MD --out OUTPUT.docx --restyle
```

This changes named paragraph styles and shared section geometry only. For differing section variants, apply geometry selectively instead. Implement narrative rules and custom style mappings explicitly with supported helpers or focused OOXML edits; read the corresponding mechanics sections. Preserve meaningful inline overrides and task-local configuration. A one-document adaptation does not update the library.

## Verify and deliver

Compare source order, coverage/counts, inline markup, media, links, anchors, equations and protected regions; explain material pagination changes. Complete the root verification gate and [visual QA](../references/visual-qa.md), repairing and rerendering as needed. Deliver requested formats and report the applied preset, overrides and specific limitations.
