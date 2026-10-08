# Views, annotations and references

## Domains and layout

Resolve target view, frame, scale, crop/domain and supported operation. Avoid implicit active-view changes. [view-domain](../assets/blocks/views/view-domain.md) uses explicit 2D loops/even-odd membership; callers extract/tessellate native boundaries.

Separate planner and native executor. Plans own candidates, geometry/references, placement and tolerances. Execution reports actual references/coordinates, skips and fallbacks. Successful alternatives do not validate intended geometry.

Bboxes/raster occupancy are estimates. They do not establish exact visible contours or text/leader collision freedom. Use native/visual readback for the actual acceptance criterion.

## Native references

Prefer actual element/geometry references. Enable Options.ComputeReferences when extraction needs references; preserve document/element/link provenance.

Stable strings are model/geometry-bound serialized references. Parse in the correct document and resolve owner/link; parsing alone does not prove dimension/tag suitability. [stable-reference-preflight](../assets/blocks/views/stable-reference-preflight.md) adds a caller-supplied suitability check.

Run-local DREF-style IDs are payload lookup keys, not ElementIds/stable strings. Do not generalize constructed RVTLINK/LINEAR suffixes into a universal resolver. Isolate any version-specific path and verify actual native results.

Reject stale, missing, cross-document or unsupported references before creation. Coplanarity, alignment, view geometry and constraints may still cause native failure; capture it in transaction/readback evidence.

## Overrides

[graphic-overrides](../assets/blocks/views/graphic-overrides.md) prepares surface foreground colors from explicit mappings, preserving unrelated existing settings. It validates drafting solid fill and view support; it does not reset arbitrary overrides.

IDs/baselines are document/view scoped. Cache within that scope. Reset only owned fields/records or restore a captured baseline under an explicit conflict policy.

Stored override readback does not guarantee visible color where filters/templates/materials/display settings intervene. Inspect rendered appearance if that is the acceptance criterion.
