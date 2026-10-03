---
name: restructure
description: Use when explicitly asked for restructure. Inventory an existing repository or file accumulation, design its minimal target structure, migrate an agreed map, or review the result while preserving provenance, current state and important data.
---

# Restructure

Reduce ambiguity and future work cost. Derive organization from actual contents, ownership, lifecycle boundaries and project needs; do not impose a universal tree.

## Operation routing

Start at the requested operation. Load only its procedure and prerequisites needed to resolve a material gap; reuse current evidence instead of repeating completed work.

| Operation | Input | Result | Procedure |
| --- | --- | --- | --- |
| Inventory | Defined scope and accessible physical state | Observations, evidence and unresolved roles | [Inventory](operations/inventory.md) |
| Design | Sufficient current inventory and project constraints | Minimal target, naming rules and migration map | [Design](operations/design.md) |
| Migration | Agreed target/map and execution authority | Applied changes and before/after evidence | [Migration](operations/migration.md) |
| Review | Baseline, agreed map and actual result | Findings, deviations and remaining decisions | [Review](operations/review.md) |

## Common principles

- Inventory before changing organization. Separate observed facts, suspected relationships, structural decisions, execution and review.
- Classify by lifecycle and ownership. Add categories only for practical differences; avoid symmetry, empty future architecture and arbitrary placement of uncertain items.
- Change organization by default, not content or project architecture. Identify additional content changes separately; perform them only within authorized scope.
- Preserve provenance, accepted history, immutable sources, external identifiers and unrelated user changes. Never delete potentially valuable material because its role is unclear.
- Preserve explicit unresolved cases and prior decisions. A completed local operation need not resolve the whole accumulation.
- Follow project source authority, storage and update destinations. Level 1 contracts retain responsibility for Issue lifecycle, assignments and publication; restructuring establishes no competing process.

## Capabilities and continuation

Assign each operation by available access and capability, independently of interface or model. One executor may perform several operations. Without direct access, request a scoped inventory or execution report; do not assume remembered filenames describe current state or claim inaccessible checks occurred.

Carry scope, source revision/inventory, agreed target/map, existing authorizations, evidence and unresolved items across handoffs. Interface changes do not restart the work or grant new authority. Do not silently redesign during migration; suspend affected work for material unresolved decisions. An agreed map may already supply execution authority; avoid asking again solely because the executor changed.

## Cloud-file boundary

Local download, materialization, synchronization, export or copying of cloud-file contents requires separate, explicit, unambiguous user authorization for that action. Restructuring or inventory requests do not provide it. Without authorization, inspect only listings and metadata exposed without downloading contents. Do not bypass this boundary through another tool or temporary directory; report content-access dependencies.

## Completion

Report the performed operation, evidence/checks, deviations, unresolved or blocked items, and justified next action. Use existing project records; retain concise before/after records for large or valuable accumulations without mandating extra files. Judge success by lower ambiguity, clearer current-state ownership, preserved provenance and lower future work cost, not visual neatness. Review does not itself authorize project acceptance.
