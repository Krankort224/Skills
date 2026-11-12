# Block catalog

Derived from block contracts by `scripts/check_library.py --catalog`.
C# snippets are not compiled or syntax-checked offline.

## core

| Block | Language | Status | Runtime | Verification | Dependencies | Mutation |
| --- | --- | --- | --- | --- | --- | --- |
| [bounded-graph](core/bounded-graph.md) | python | reviewed | Python 2.7 or 3 | offline | none | read-only |
| [checked-model-edit](core/checked-model-edit.md) | csharp | reviewed | Revit 2022.1 / rvt-mcp / C# | runtime | none | document-write |
| [clr-property-access](core/clr-property-access.md) | python | reviewed | Revit 2022 / Dynamo 2.12 / IronPython 2.7; Python 3 CLR requires separate verification | offline | none | read-only |
| [coordinate-frames](core/coordinate-frames.md) | python | reviewed | Python 2.7 or 3; Revit 2022 for link adapter | offline | none | read-only |
| [element-identity](core/element-identity.md) | python | reviewed | Revit 2022 / Dynamo 2.12 / IronPython 2.7; Python 3 CLR requires separate verification | offline | clr-property-access | read-only |
| [parameter-access](core/parameter-access.md) | python | reviewed | Revit 2022 / Dynamo 2.12 / IronPython 2.7; Python 3 with compatible Revit host | offline | none | document-write |
| [physical-connectors](core/physical-connectors.md) | python | reviewed | Revit 2022 / Dynamo 2.12 / IronPython 2.7; Python 3 with compatible Revit host | offline | none | read-only |
| [physical-hvac](core/physical-hvac.md) | csharp | reviewed | Revit 2022.1 / rvt-mcp / C# | runtime | none | read-only |
| [table-payload](core/table-payload.md) | python | reviewed | Python 2.7 or 3 | offline | none | read-only |
| [transaction-receipt](core/transaction-receipt.md) | python | reviewed | Revit 2022 / Dynamo 2.12 / IronPython 2.7; Python 3 with compatible Revit host | offline | none | document-write |

## mep

| Block | Language | Status | Runtime | Verification | Dependencies | Mutation |
| --- | --- | --- | --- | --- | --- | --- |
| [connector-size-signature](mep/connector-size-signature.md) | python | reviewed | Revit 2022 / Dynamo 2.12 / IronPython 2.7; pure helpers Python 2.7 or 3 | offline | none | read-only |
| [host-cover-map](mep/host-cover-map.md) | python | reviewed | Revit 2022 / Dynamo 2.12 / IronPython 2.7; pure helpers Python 2.7 or 3 | offline | none | read-only |
| [insulation-workset](mep/insulation-workset.md) | python | reviewed | Revit 2022 / Dynamo / IronPython 2.7; Python 3 with compatible Revit host | offline | none | document-write |
| [nested-hierarchy](mep/nested-hierarchy.md) | python | reviewed | Revit 2022 / Dynamo 2.12 / IronPython 2.7; pure helpers Python 2.7 or 3 | offline | none | read-only |
| [positional-resolution](mep/positional-resolution.md) | python | reviewed | Python 2.7 or 3; Revit record extraction caller-owned | offline | none | read-only |
| [rectangular-elbow-run](mep/rectangular-elbow-run.md) | csharp | reviewed | Revit 2022.1 / rvt-mcp / C# | runtime | physical-hvac | document-write |
| [rectangular-takeoff-to-round-riser](mep/rectangular-takeoff-to-round-riser.md) | csharp | reviewed | Revit 2022.1 / rvt-mcp / C# | runtime | physical-hvac, checked-model-edit | document-write |
| [reference-level](mep/reference-level.md) | python | reviewed | Revit 2022 / Dynamo 2.12 / IronPython 2.7; pure helpers Python 2.7 or 3 | offline | none | document-write |
| [retarget-rectangular-accessory](mep/retarget-rectangular-accessory.md) | csharp | reviewed | Revit 2022.1 / rvt-mcp / C# | runtime | physical-hvac | document-write |

## views

| Block | Language | Status | Runtime | Verification | Dependencies | Mutation |
| --- | --- | --- | --- | --- | --- | --- |
| [graphic-overrides](views/graphic-overrides.md) | python | reviewed | Revit 2022 API context; Python 2.7 or 3 syntax | offline | none | read-only |
| [stable-reference-preflight](views/stable-reference-preflight.md) | python | reviewed | Revit 2022 API context; Python 2.7 or 3 syntax | offline | none | read-only |
| [view-domain](views/view-domain.md) | python | reviewed | Python 2.7 or 3; caller supplies view-local coordinates | offline | none | read-only |

