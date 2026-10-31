# Community pavilion — synthetic concept brief

This fictional exhibition and community pavilion demonstrates an editable 2D concept diagram and a raster rendering of that same diagram. It is not an actual project. The SVG is the editable source; the PNG is an exported view. These are two example capabilities, not a requirement to deliver both formats for future tasks: use the format the user chooses.

## Fixed decisions

- The external schematic footprint is a rectangle, 24 m east–west by 18 m north–south: 432 m² of geometric area. Dimensions and room rectangles share a scale of 30 SVG units per metre in the plan.
- Using metres from the northwest corner, with x east and y south, the allocation is:

| Space | x range | y range | Geometric area |
| --- | --- | --- | ---: |
| Exhibition hall | 0–12 m | 0–18 m | 216 m² |
| Gallery / circulation spine | 12–16 m | 0–18 m | 72 m² |
| East lobby | 16–24 m | 0–6 m | 48 m² |
| Café / social | 16–24 m | 6–12 m | 48 m² |
| Support | 16–24 m | 12–15 m | 24 m² |
| Sanitary | 16–24 m | 15–18 m | 24 m² |
| **Total** | | | **432 m²** |

- Arrival is through the east lobby, with a conceptual path via the spine into the hall. Each program cell has a separate opening onto the spine. Openings and route indicate relationships, not verified door widths or a detailed layout.
- The elevation suggests a low, contemporary pavilion with glazing, warm timber accents and a restrained light and charcoal palette. It is an illustrative composition, not a coordinated construction elevation.

## Assumptions and open questions

North is assumed to be up on the plan for illustration; no actual site, climate, survey, topography, client or jurisdiction is specified. Areas are rectangular diagram areas, with no allowance for walls, columns or other construction, and are not a legal area calculation. The project requires confirmation of site orientation, uses and occupancy, structural system and grid, building height, facade and material details, local area definitions, jurisdictional requirements, fire and life safety, and accessibility. None has been verified, and the diagram makes no compliance claim. This is a concept area diagram, not for construction.

For an optional local revision, shift the east entry within the lobby's east edge and adjust the conceptual arrival line while preserving the footprint and all room rectangles. Check that the entry remains in the lobby and that the route still connects lobby, spine and hall.

## Rendering and visual check

The SVG is hand-authored with editable vector shapes and text, a 1440 × 1000 viewBox, and locally available DejaVu Sans with a sans-serif fallback. From the repository root, render with Inkscape:

```sh
inkscape level-2/architecture/assets/examples/pavilion-concept.svg --export-filename=level-2/architecture/assets/examples/pavilion-concept.png --export-width=1440
```

The exported 1440 × 1000 PNG was visually inspected for label legibility, boundaries, openings, arrival path, dimensions and clipping. The geometry is intentionally schematic: line widths and openings are graphic conventions, the elevation is not dimensioned or coordinated in detail, and different installed fonts or renderers can alter text metrics. For any revision, re-export and inspect the result at delivery size.
