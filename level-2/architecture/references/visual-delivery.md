# Presentation and optional visual techniques

## Choose a useful representation

Follow the user's requested deliverable and format. A concept can be explained in text without a visual artifact. There is no preset format, exhaustive two-format choice, automatic SVG default or required sample pair. Clarify an unspecified format only when it is necessary to produce a requested artifact.

For requested artifacts, inspect the actual result appropriately for its format. Text, tables, drawings, presentations and images communicate different aspects of a design; this reference's SVG/raster sections are optional technical guidance, not a format catalog or a mandatory concept workflow.

When a visual is requested, choose views that explain the design decision. A spatial program may benefit from a labeled zoning plan and route diagram; a facade decision may benefit from an elevation and material/rhythm comparison. Keep the chosen presentation consistent with fixed program and geometry.

## When SVG is requested or used

- Define a viewBox and intentional physical/pixel units. For a dimensionally controlled diagram state the relationship between SVG coordinates and model metres/millimetres; separate paper scale from browser display size.
- Use editable vector shapes/text, consistent line weights, legible hierarchy and enough margin for dimensions/legends. Put area/length units in labels and retain metric definitions.
- Align annotations with the actual geometry. Label schematic openings, assumed orientation and any parts not coordinated or dimensioned.
- Use original, supplied or correctly licensed visual assets. Fonts/renderers can affect text metrics; avoid relying on one workstation's font layout.
- Render the final SVG and inspect it at the delivery size. Parsing XML is not visual inspection.

## When raster is requested or used

For a proportioned drawing, an existing controlled SVG can be exported with an available renderer. Use a workflow appropriate to the requested output; SVG is not a required intermediate. For a requested illustrative image, use an appropriate available image-generation/rendering workflow and inspect the actual image. Keep fixed architectural facts in the workflow inputs and check the result against them.

Label an illustration honestly; it cannot establish measured dimensions, performance or regulatory compliance. Do not turn an illustration into an authoritative plan by reading pixel distances. Do not construct a building/BIM/3D/mesh model as an intermediate under this skill.

If a tool is unavailable, identify the actual missing capability. Do not claim the image was created or viewed. Deliver completed independent work and a precise remaining action.

## Inspect and correct

Check overall proportions and numeric labels, functional relationships and routes, orientation/context assumptions, consistency between views and text, readable labels/dimensions/legends, contrast, clipping and collisions. Inspect the actual final version after any material edit. Reconcile a mismatch in the owning geometry/program before polishing its appearance.

## Optional worked example

The optional [pavilion brief](../assets/examples/pavilion-brief.md) defines a synthetic 24 × 18 m area diagram with 432 m² geometric footprint, including a fixed 216 m² hall. Its [SVG](../assets/examples/pavilion-concept.svg) and [PNG](../assets/examples/pavilion-concept.png) express the same constraints; this retained example pair is not an acceptance requirement. Plan geometry uses 30 SVG units per metre; wall allowances and legal-area definitions are unresolved. The elevation is illustrative and not a coordinated specification.

From the repository root, the example can be rendered with an installed Inkscape:

```bash
inkscape level-2/architecture/assets/examples/pavilion-concept.svg --export-filename=level-2/architecture/assets/examples/pavilion-concept.png --export-width=1440
```

The rendering dependency is optional for numerical tools. Inspect the resulting image instead of inferring appearance from a successful command. See the brief for open decisions and the bounded local-revision example.
