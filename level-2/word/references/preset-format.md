# Single-file Markdown presets

Store each design in `assets/presets/<name>.md`. The MD is the sole source for exact parameters and human-readable rules. Use the same basename for its neutral render in `assets/examples/`. Do not keep parallel JSON/YAML data or introduce `.template.` files for active library presets.

## Sections

- Title and `Status: ready` or `Status: draft`.
- Purpose: intended document types, character and supported scope.
- Parameters: the one canonical typed parameter table.
- Semantic roles: mapping source/target roles to styles, sections and components.
- Composition: title/cover, reading order, page/section variants, graphics and navigation.
- Adaptation: permitted variations and treatment of different content lengths.
- Dependencies: fonts, reusable assets and specialized tooling.
- Provenance and limitations: authored or captured origin, source revision/hash when applicable, observations/defaults, verified coverage and unsupported elements.
- Preview link, for example `[Preview](../examples/technical.png)`.

Keep all reusable knowledge about this preset here. References describe generic mechanics; they do not own individual preset values.

## Canonical parameter table

Under the exact heading `## Parameters`, use `Path | Value | Type | Unit`. Paths reconstruct the existing version-1 nested configuration. Types are `string`, `number` and `boolean`; booleans are lowercase `true`/`false`. Numeric values are finite decimal values. Units are `mm`, `pt`, `ratio` or `-` as appropriate. Do not add numeric copies of these settings to narrative sections.

```markdown
## Parameters

| Path | Value | Type | Unit |
| --- | --- | --- | --- |
| version | 1 | number | - |
| name | example | string | - |
| page.width_mm | 210 | number | mm |
| styles.Heading 1.size_pt | 18 | number | pt |
| styles.Heading 1.bold | true | boolean | - |
```

This is a partial syntax example, not a loadable preset. Use a complete existing preset as the baseline; retain every required parameter. Separate path segments with dots; a segment cannot contain a dot, backslash or line break, so map incompatible style names to a supported role. Escape a table pipe as `\|`, a string backslash as `\\`, and string line breaks as `\n`/`\r`. The loader rejects malformed, duplicate and conflicting fields instead of guessing.

The executable table configures the supported helper subset: page geometry, fonts/fallbacks, palette, named paragraph styles, data-table treatment, list geometry and footer treatment. Document multi-section variants, nonstandard components and instructions beyond that subset in the same file. Implement and verify them in the operation; successfully loading the table does not mean those narrative rules were automatically applied.

## Capture status and review

The extraction command produces a draft. Label observed fields, inherited/defaulted values and direct-formatting observations; investigate gaps against rendered source pages. A base preset is an explicit source of fallback values, not evidence that those values occurred in the example. Keep the observation report and coverage limits in this same MD, without factual body text.

Before marking ready, complete semantic/composition rules, review all fallback choices, reproduce a neutral sample and inspect the supported coverage. Preserve limitations even after readiness. A preset may be ready for a declared subset of the source's design; disclose that subset. Normal load/application must reject a draft.

## Evolution

Keep one canonical table per preset. Make single-document overrides in memory or a temporary MD copy. When saving a reusable change, update its rules and regenerate the preview if appearance changes. Record source/provenance and limitations in the same MD. Required binary assets can be linked from an adjacent `<name>-assets/` directory; the source DOCX is not a runtime dependency.
