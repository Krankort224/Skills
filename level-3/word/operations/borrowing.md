# Borrowing

Input: a Word reference whose design should be reusable. Output: one Markdown preset, required reusable assets and a neutral visual preview. Apply the common principles in `../SKILL.md`; use a lowercase ASCII hyphenated preset name.

## Inspect

Read [preset format](../references/preset-format.md) and the inspection section of [templates/editing](../references/templates-and-editing.md). Inspect the package and render all source pages. Identify semantic roles, inherited/direct formatting, section geometry, themes/fonts, numbering, tables, headers/footers, fields and graphics. Separate repeatable design from exceptional decoration and factual content. Identify cover/body/appendix and first/even-page variants.

## Capture

Read [CLI](../references/toolkit.md#cli) and [limits](../references/toolkit.md#limits). Select an explicit fallback baseline and section:

```sh
python scripts/document_tool.py extract-preset INPUT.docx --base technical --section 0 --out DRAFT.md
```

Review observed/defaulted paths and direct-formatting diagnostics. Resolve inheritance, custom mappings and unsupported features using only relevant mechanics/design sections. Complete semantic roles, composition, section variants, adaptation, dependencies, provenance/source revision or hash, and coverage limits in the same MD. Distinguish defaults from observations; extraction is a starting draft.

Link required reusable graphics from `<name>-assets/`. Missing required dependencies keep the preset draft. Exclude factual source text.

## Reproduce and review

Build a neutral sample covering every claimed role and section variant. Consult component/composition sections for actual unusual structures. Compare rendered typography, spacing, proportions, tables, transitions, headers/footers and exact settings with the reference. Check editability and [visual QA](../references/visual-qa.md). Repair and repeat, or narrow the declared supported scope. Source pages are inspection material; the library preview contains neutral content.

## Save

Mark `Status: ready` only after review and successful reproduction. Save `assets/presets/<name>.md`, linked dependencies and `assets/examples/<name>.png`; update library navigation when needed and persist through the source repository workflow. Report verified scope and remaining limitations. The original DOCX must not be needed for application.
