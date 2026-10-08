# Block catalog

Derived from block contracts by `scripts/check_library.py --catalog`.

## core

| Block | Status | Runtime | Verification | Dependencies | Mutation |
| --- | --- | --- | --- | --- | --- |
| [bounded-graph](core/bounded-graph.md) | reviewed | Python 2.7 or 3 | offline | none | read-only |
| [coordinate-frames](core/coordinate-frames.md) | reviewed | Python 2.7 or 3; Revit 2022 for link adapter | offline | none | read-only |
| [element-identity](core/element-identity.md) | reviewed | Revit 2022 / Dynamo 2.12 / IronPython 2.7; Python 3 with compatible Revit host | offline | none | read-only |
| [parameter-access](core/parameter-access.md) | reviewed | Revit 2022 / Dynamo 2.12 / IronPython 2.7; Python 3 with compatible Revit host | offline | none | document-write |
| [physical-connectors](core/physical-connectors.md) | reviewed | Revit 2022 / Dynamo 2.12 / IronPython 2.7; Python 3 with compatible Revit host | offline | none | read-only |
| [table-payload](core/table-payload.md) | reviewed | Python 2.7 or 3 | offline | none | read-only |
| [transaction-receipt](core/transaction-receipt.md) | reviewed | Revit 2022 / Dynamo 2.12 / IronPython 2.7; Python 3 with compatible Revit host | offline | none | document-write |

## mep

| Block | Status | Runtime | Verification | Dependencies | Mutation |
| --- | --- | --- | --- | --- | --- |
| [connector-size-signature](mep/connector-size-signature.md) | reviewed | Revit 2022 / Dynamo 2.12 / IronPython 2.7; pure helpers Python 2.7 or 3 | offline | none | read-only |
| [host-cover-map](mep/host-cover-map.md) | reviewed | Revit 2022 / Dynamo 2.12 / IronPython 2.7; pure helpers Python 2.7 or 3 | offline | none | read-only |
| [nested-hierarchy](mep/nested-hierarchy.md) | reviewed | Revit 2022 / Dynamo 2.12 / IronPython 2.7; pure helpers Python 2.7 or 3 | offline | none | read-only |
| [positional-resolution](mep/positional-resolution.md) | reviewed | Python 2.7 or 3; Revit record extraction caller-owned | offline | none | read-only |
| [reference-level](mep/reference-level.md) | reviewed | Revit 2022 / Dynamo 2.12 / IronPython 2.7; pure helpers Python 2.7 or 3 | offline | none | document-write |

## views

| Block | Status | Runtime | Verification | Dependencies | Mutation |
| --- | --- | --- | --- | --- | --- |
| [graphic-overrides](views/graphic-overrides.md) | reviewed | Revit 2022 API context; Python 2.7 or 3 syntax | offline | none | read-only |
| [stable-reference-preflight](views/stable-reference-preflight.md) | reviewed | Revit 2022 API context; Python 2.7 or 3 syntax | offline | none | read-only |
| [view-domain](views/view-domain.md) | reviewed | Python 2.7 or 3; caller supplies view-local coordinates | offline | none | read-only |

