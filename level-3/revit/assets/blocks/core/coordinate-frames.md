# Explicit view frames and linked bounding boxes

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
|---|---|
| id | coordinate-frames |
| group | core |
| status | reviewed |
| runtime | Python 2.7 or 3; Revit 2022 for link adapter |
| verification | offline |
| dependencies | none |
| mutation | read-only |

## Purpose

Project points and vectors using an explicit origin/right/up frame. Convert all eight bounding-box corners through bbox and link transforms, reporting missing transforms rather than assuming identity.

## Inputs and outputs

`coordinate_frame(origin, right, up, tolerance=1e-9)` validates an orthogonal basis and returns immutable tuple values. `frame_point`, `frame_vector`, `frame_world` convert three-component tuples. `linked_bbox_corners(link, bbox, api=None)` returns `ok` with eight host tuples or `error` with reason. Link transforms come from `GetTotalTransform`; bbox.Transform is applied first. No implicit document or view.

## Implementation

```python
# -*- coding: utf-8 -*-
def _frame_xyz(value):
    import math
    try:
        parts = (value.X, value.Y, value.Z)
    except AttributeError:
        parts = tuple(value)
    if len(parts) != 3:
        raise ValueError('Expected three coordinates')
    parts = tuple(float(item) for item in parts)
    if any(math.isnan(item) or math.isinf(item) for item in parts):
        raise ValueError('Nonfinite coordinate')
    return parts


def _frame_dot(a, b):
    return sum(a[index] * b[index] for index in range(3))


def _frame_normalize(value, tolerance):
    import math
    value = _frame_xyz(value)
    length = math.sqrt(_frame_dot(value, value))
    if length <= tolerance:
        raise ValueError('Degenerate basis')
    return tuple(item / length for item in value)


def coordinate_frame(origin, right, up, tolerance=1e-9):
    if tolerance <= 0 or tolerance >= 1:
        raise ValueError('Invalid tolerance')
    right = _frame_normalize(right, tolerance)
    up = _frame_normalize(up, tolerance)
    if abs(_frame_dot(right, up)) > tolerance:
        raise ValueError('Frame basis must be orthogonal')
    normal = (right[1] * up[2] - right[2] * up[1],
              right[2] * up[0] - right[0] * up[2],
              right[0] * up[1] - right[1] * up[0])
    return {'origin': _frame_xyz(origin), 'right': right, 'up': up,
            'normal': _frame_normalize(normal, tolerance)}


def frame_vector(frame, vector):
    vector = _frame_xyz(vector)
    return tuple(_frame_dot(vector, frame[name])
                 for name in ('right', 'up', 'normal'))


def frame_point(frame, point):
    point = _frame_xyz(point)
    relative = tuple(point[index] - frame['origin'][index]
                     for index in range(3))
    return frame_vector(frame, relative)


def frame_world(frame, local, is_vector=False):
    local = _frame_xyz(local)
    base = (0.0, 0.0, 0.0) if is_vector else frame['origin']
    axes = (frame['right'], frame['up'], frame['normal'])
    return tuple(base[index] + sum(local[axis] * axes[axis][index]
                                  for axis in range(3))
                 for index in range(3))


def linked_bbox_corners(link, bbox, api=None):
    if api is None:
        import Autodesk.Revit.DB as api
    try:
        if link is None or bbox is None:
            raise ValueError('Link and bounding box required')
        link_transform = link.GetTotalTransform()
        bbox_transform = bbox.Transform
        if link_transform is None or bbox_transform is None:
            raise ValueError('Transform unavailable')
        low, high = _frame_xyz(bbox.Min), _frame_xyz(bbox.Max)
        if any(low[index] > high[index] for index in range(3)):
            raise ValueError('Invalid bounding box bounds')
        points = []
        for x in (low[0], high[0]):
            for y in (low[1], high[1]):
                for z in (low[2], high[2]):
                    local = api.XYZ(x, y, z)
                    linked = bbox_transform.OfPoint(local)
                    points.append(_frame_xyz(link_transform.OfPoint(linked)))
        return {'status': 'ok', 'corners': points, 'error': None}
    except Exception as error:
        return {'status': 'error', 'corners': None, 'error': str(error)}
```

## Adaptation and limits

All values stay in caller/native length units; this block does not multiply by view scale or convert to millimeters. Projection retains signed normal distance, so callers can apply plane tolerances explicitly. It rejects skew/degenerate frames rather than silently orthogonalizing them. Bbox transformation encloses geometry only as far as the source bbox does; it is not solid intersection. Identity is accepted only when actually supplied by the API, never as an error fallback.

## Verification

Offline cases cover rotated and translated frame round trips, vector translation independence, orthogonality rejection, eight-corner bbox transformation order and unavailable/throwing transforms. Native link transform and mirrored-link validation remain pending.

## Provenance

Adapted from [CFD snapshot graph at 6f6ff374](https://github.com/Krankort224/CFD-modeling/blob/6f6ff37416a4145313737cb9c23a311d3e8ebedb/tools/dyn/00_CFD_ModelSnapshot.dyn), embedded functions `project_uv_ft`, `bbox_corners`, `element_bbox_host_corners`; and [Revit Core at f6b4a430](https://github.com/Krankort224/Revit-automatization/blob/f6b4a4301ef70187780150acf44f6e5140a6c339/src/block_0_core/block_0_core_current.py), `point_view_xy`, `transform_bb_to_points`, `get_total_transform_safe`. Added explicit origin and validation; removed silent identity fallback. Embedded snapshot copies are derived analysis files, not alternate repository source paths.
