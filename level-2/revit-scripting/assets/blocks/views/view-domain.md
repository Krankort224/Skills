# Explicit view-domain membership

## Contents

- [Contract](#contract)
- [Purpose](#purpose)
- [Inputs and outputs](#inputs-and-outputs)
- [Implementation](#implementation)
- [Adaptation and limits](#adaptation-and-limits)
- [Verification](#verification)
- [Provenance](#provenance)

## Contract

| Field | Value |
| --- | --- |
| id | view-domain |
| group | views |
| status | reviewed |
| runtime | Python 2.7 or 3; caller supplies view-local coordinates |
| verification | offline |
| dependencies | none |
| mutation | read-only |

## Purpose

Classify a point against explicit polygon loops using an even-odd rule, including holes and disjoint regions, without assuming collection order or an implicit world/view frame.

## Inputs and outputs

`classify_view_domain(point, loops, tolerance, boundary="include", max_vertices=4096)` accepts finite 2D numeric tuples in one declared unit/frame. Loops have at least three distinct noncollinear vertices; an optional repeated closing vertex is removed. Result contains `state` (INSIDE/OUTSIDE/BOUNDARY), `inside`, and boundary loop indices. Invalid/budget-exceeding input raises ValueError.

## Implementation

```python
import math


def classify_view_domain(point, loops, tolerance, boundary="include",
                         max_vertices=4096):
    def number(value):
        if isinstance(value, bool):
            raise ValueError("Boolean is not a coordinate")
        value = float(value)
        if math.isnan(value) or math.isinf(value):
            raise ValueError("Nonfinite coordinate or tolerance")
        return value

    def xy(value):
        if len(value) != 2:
            raise ValueError("Expected a 2D point")
        return (number(value[0]), number(value[1]))

    p = xy(point)
    tol = number(tolerance)
    if tol < 0 or boundary not in ("include", "exclude"):
        raise ValueError("Invalid tolerance or boundary rule")
    if isinstance(max_vertices, bool) or int(max_vertices) != max_vertices:
        raise ValueError("Vertex budget must be an integer")
    if max_vertices < 3 or not loops:
        raise ValueError("Empty domain or invalid vertex budget")
    polygons, count = [], 0
    for loop in loops:
        if len(loop) > max_vertices + 1:
            raise ValueError("Domain vertex budget exceeded")
        poly = [xy(v) for v in loop]
        if len(poly) > 1 and poly[0] == poly[-1]:
            poly.pop()
        count += len(poly)
        if count > max_vertices:
            raise ValueError("Domain vertex budget exceeded")
        if len(poly) < 3 or len(set(poly)) != len(poly):
            raise ValueError("Degenerate or repeated polygon vertices")
        area2 = sum(a[0] * b[1] - b[0] * a[1]
                    for a, b in zip(poly, poly[1:] + poly[:1]))
        if area2 == 0:
            raise ValueError("Zero signed-area polygon")
        polygons.append(poly)

    def distance2(a, b):
        dx, dy = b[0] - a[0], b[1] - a[1]
        length2 = dx * dx + dy * dy
        t = ((p[0] - a[0]) * dx + (p[1] - a[1]) * dy) / length2
        t = max(0.0, min(1.0, t))
        return (p[0] - a[0] - t * dx) ** 2 + (p[1] - a[1] - t * dy) ** 2

    parity, on = False, []
    for index, poly in enumerate(polygons):
        hit = False
        for a, b in zip(poly, poly[1:] + poly[:1]):
            if distance2(a, b) <= tol * tol:
                hit = True
            if (a[1] > p[1]) != (b[1] > p[1]):
                crossing_x = a[0] + (p[1] - a[1]) * (b[0] - a[0]) / (b[1] - a[1])
                if p[0] < crossing_x:
                    parity = not parity
        if hit:
            on.append(index)
    state = "BOUNDARY" if on else ("INSIDE" if parity else "OUTSIDE")
    return {"state": state, "inside": boundary == "include" if on else parity,
            "boundary_loops": on}
```

## Adaptation and limits

Caller extracts/tessellates simple native loops and projects them into the explicit view frame. Self-intersections and intersecting/overlapping loops are outside this contract; this is membership, not polygon repair or solid overlap. The even-odd rule handles containment holes independently of winding. Boundary tolerance applies to every loop, including hole boundaries. Z range, visibility, crop activation, paper scale and annotation collision checks are separate.

## Verification

`scripts/test_view_blocks.py` loads this fence and checks hole/disjoint membership, winding/order independence, boundary policy, closing vertices, malformed/nonfinite input and vertex limits. Pure offline tests; no native crop extraction or rendered visibility verification.

## Provenance

Adapted from [Revit automatization Core](https://github.com/Krankort224/revit-automatization/blob/f6b4a4301ef70187780150acf44f6e5140a6c339/src/block_0_core/block_0_core_current.py), functions `point_in_single_poly_2d`, `point_in_room_loops_2d`, `dist_2d_point_segment`. Removed implicit world XYZ, globals and view-range coupling; added explicit frame input, validation, budget and boundary receipt. Original source runtime evidence is not transferred.
