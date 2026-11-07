# Scoped stable-reference preflight

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
| id | stable-reference-preflight |
| group | views |
| status | reviewed |
| runtime | Revit 2022 API context; Python 2.7 or 3 syntax |
| verification | offline |
| dependencies | none |
| mutation | read-only |

## Purpose

Resolve an actual serialized stable reference in its declared host document, including linked ownership, and require a caller-owned suitability check before annotation creation.

## Inputs and outputs

`preflight_stable_reference(doc, stable, suitability)` parses a nonempty actual stable string. A required callback receives the resolved context and returns `{"ok": bool, "reason": text}`. Result has `status`, `reason` and, after successful resolution, native host/reference/owner/link fields. READY means the callback accepted the context; it is not proof that a native dimension/tag will be created. INVALID and UNSUITABLE never write.

## Implementation

```python
def preflight_stable_reference(doc, stable, suitability):
    from Autodesk.Revit.DB import ElementId, Reference, RevitLinkInstance
    try:
        string_types = (basestring,)
    except NameError:
        string_types = (str,)
    if not isinstance(stable, string_types) or not stable.strip():
        return {"status": "INVALID", "reason": "Empty or nonstring stable reference"}
    if not callable(suitability):
        raise ValueError("A suitability callback is required")
    try:
        reference = Reference.ParseFromStableRepresentation(doc, stable)
        host_owner = doc.GetElement(reference.ElementId)
        if host_owner is None or host_owner.Document != doc:
            raise ValueError("Host owner is missing or outside the supplied document")
        context = {"host_document": doc, "stable": stable, "reference": reference,
                   "host_owner": host_owner, "link_instance": None,
                   "owner_document": doc, "owner": host_owner,
                   "owner_reference": reference, "link_transform": None}
        if reference.LinkedElementId != ElementId.InvalidElementId:
            if not isinstance(host_owner, RevitLinkInstance):
                raise ValueError("Linked reference host is not a RevitLinkInstance")
            linked_doc = host_owner.GetLinkDocument()
            if linked_doc is None:
                raise ValueError("Referenced link is unloaded")
            owner = linked_doc.GetElement(reference.LinkedElementId)
            if owner is None or owner.Document != linked_doc:
                raise ValueError("Linked owner is missing")
            transform = host_owner.GetTotalTransform()
            if transform is None:
                raise ValueError("Link transform is unavailable")
            linked_ref = reference.CreateReferenceInLink()
            if linked_ref is None or linked_ref.ElementId != owner.Id:
                raise ValueError("Linked reference conversion did not resolve its owner")
            context.update({"link_instance": host_owner, "owner_document": linked_doc,
                            "owner": owner, "owner_reference": linked_ref,
                            "link_transform": transform})
    except Exception as exc:
        return {"status": "INVALID", "reason": str(exc)}
    try:
        verdict = suitability(context)
        if not isinstance(verdict, dict) or type(verdict.get("ok")) is not bool:
            raise ValueError("Suitability must return an explicit Boolean ok field")
        if not isinstance(verdict.get("reason"), string_types) or not verdict["reason"]:
            raise ValueError("Suitability must provide a reason")
    except Exception as exc:
        context.update({"status": "UNSUITABLE", "reason": str(exc)})
        return context
    context.update({"status": "READY" if verdict["ok"] else "UNSUITABLE",
                    "reason": verdict["reason"]})
    return context
```

## Adaptation and limits

Input must come with the correct document/model identity; parsing cannot detect every cross-model collision. The callback must remain read-only and check intended geometry type, actual referenced geometry, target view, alignment/coplanarity and task tolerances. Retrieve geometry using owner_reference in owner_document and transform linked points/vectors explicitly. Nested linked references require a separate adapter. Native objects are operation-local; reacquire after relevant model changes. No undocumented stable-string construction, suffix repair or dimension creation is included.

## Verification

`scripts/test_view_blocks.py` loads this fence with native mocks and checks host/linked resolution, unloaded/missing owners, missing transform, invalid parse, malformed suitability and explicit rejection. Native reference stability, geometry suitability and annotation creation are unverified.

## Provenance

Adapted from [Revit automatization Block 3](https://github.com/Krankort224/revit-automatization/blob/f6b4a4301ef70187780150acf44f6e5140a6c339/src/block_3/block_3_current.py), function `parse_reference_stable`, and [Core reference extraction](https://github.com/Krankort224/revit-automatization/blob/f6b4a4301ef70187780150acf44f6e5140a6c339/src/block_0_core/block_0_core_current.py). Replaced implicit doc/global fallback with scoped resolution, actual linked ownership and a mandatory caller-owned suitability verdict.

[Autodesk Reference API](https://help.autodesk.com/cloudhelp/2026/ENU/Revit-API-MainReference/files/html/d28155ae-817b-1f31-9c3f-c9c6a28acc0d.htm) documents LinkedElementId and CreateReferenceInLink; confirm target assembly behavior in a native case.
