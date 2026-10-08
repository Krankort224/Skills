# Preserving graphic override preparation

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
| id | graphic-overrides |
| group | views |
| status | reviewed |
| runtime | Revit 2022 API context; Python 2.7 or 3 syntax |
| verification | offline |
| dependencies | none |
| mutation | read-only |

## Purpose

Prepare surface foreground color overrides from explicit host element/color records while retaining each element's unrelated per-view settings. Preparation performs no document write.

## Inputs and outputs

`prepare_graphic_overrides(doc, view, records)` takes native ElementIds and RGB integer triples in records `{"element_id": id, "rgb": (r,g,b)}`. All records must resolve uniquely in the supplied document. Returns native document/view scope, drafting solid-fill ID and entries containing element ID, RGB, baseline and desired OverrideGraphicSettings. These native objects are operation-local, not JSON or durable state. Empty input returns an empty plan. Invalid scope, RGB, duplicates, missing elements or solid fill raise ValueError.

## Implementation

```python
def prepare_graphic_overrides(doc, view, records):
    from Autodesk.Revit.DB import (Color, ElementId, FillPatternElement,
                                   FillPatternTarget, FilteredElementCollector,
                                   OverrideGraphicSettings)

    def id_key(value):
        return int(value.Value if hasattr(value, "Value") else value.IntegerValue)

    if view.Document != doc or doc.IsFamilyDocument or view.IsTemplate:
        raise ValueError("Expected a project view in the supplied document")
    if not view.AreGraphicsOverridesAllowed():
        raise ValueError("View does not support graphic overrides")
    rows, seen = [], set()
    for record in records:
        eid, rgb = record["element_id"], record["rgb"]
        if not isinstance(eid, ElementId) or eid == ElementId.InvalidElementId:
            raise ValueError("Expected a native host ElementId")
        key = id_key(eid)
        if key in seen:
            raise ValueError("Duplicate element override")
        if len(rgb) != 3:
            raise ValueError("RGB requires three integer channels")
        channels = []
        for value in rgb:
            if isinstance(value, bool) or int(value) != value or not 0 <= value <= 255:
                raise ValueError("Invalid RGB channel")
            channels.append(int(value))
        element = doc.GetElement(eid)
        if element is None or element.Document != doc:
            raise ValueError("Missing host element")
        seen.add(key)
        rows.append((eid, tuple(channels)))
    if not rows:
        return {"document": doc, "view_id": view.Id, "solid_fill_id": None, "entries": []}
    fills = []
    for element in FilteredElementCollector(doc).OfClass(FillPatternElement):
        pattern = element.GetFillPattern()
        if pattern.IsSolidFill and pattern.Target == FillPatternTarget.Drafting:
            fills.append(element.Id)
    if not fills:
        raise ValueError("Drafting solid fill is unavailable")
    solid_id = min(fills, key=id_key)
    entries = []
    for eid, rgb in rows:
        baseline = view.GetElementOverrides(eid)
        desired = OverrideGraphicSettings(baseline)
        desired.SetSurfaceForegroundPatternId(solid_id)
        desired.SetSurfaceForegroundPatternColor(Color(*rgb))
        desired.SetSurfaceForegroundPatternVisible(True)
        entries.append({"element_id": eid, "rgb": rgb,
                        "baseline": baseline, "desired": desired})
    return {"document": doc, "view_id": view.Id,
            "solid_fill_id": solid_id, "entries": entries}
```

## Adaptation and limits

Call immediately before a caller-owned transaction applies SetElementOverrides; rebuild stale plans so newer settings are preserved. The caller owns transaction/readback/rollback and must verify the three changed surface foreground fields. In-memory OGS setters do not modify the document. No reset or cut/line/background override is implied. Apply only to host elements; linked graphics need a separate contract. The default color-to-category/parameter mapping belongs to the project. Stored override values do not prove rendered appearance.

## Verification

`scripts/test_view_blocks.py` runs this fence with explicit Revit mocks, checking drafting/model fill filtering, preservation of line/cut/background settings, invalid colors, duplicate/missing IDs, unsupported views and empty input. Tests verify that the mock document never receives SetElementOverrides. Native drafting fill discovery and actual appearance remain unverified.

## Provenance

Adapted from immutable archive SHA256 `6caa68eb49c6e9cec087eb4b280336d0d8300df9635c4ad719bea1240472b20e`, graph 04 (EI coloring), Python node `57edd7f801f84b6aba8295f8c7b03384`, functions `get_solid_fill_pattern_id` and `make_ogs`. Removed project family-name selection, swallowed API exceptions, old API fallbacks and blanket override reset. Added exact host scope and baseline-copy preservation.

Primary member semantics: [OverrideGraphicSettings](https://help.autodesk.com/cloudhelp/2026/ENU/Revit-API-MainReference/files/html/eb2bd6b6-b7b2-5452-2070-2dbadb9e068a.htm) and [SetElementOverrides](https://help.autodesk.com/cloudhelp/2026/ENU/Revit-API-MainReference/files/html/a6f1ced3-1f1c-dd42-c0ca-f15f301d1cad.htm). These reference pages do not validate the target runtime.
