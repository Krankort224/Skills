# Geometry and connectors

## Frames

State document and frame for every point/vector: link-local, host, view, paper or raster. Supply origin/axes. Point transforms include translation; vector transforms do not. Resolve the actual link-instance transform; unloaded/failed transform is an error, not identity.

[coordinate-frames](../assets/blocks/core/coordinate-frames.md) projects coordinates and all eight BoundingBoxXYZ corners. Transforming only Min/Max fails for rotations. A projected bbox is an approximation, not proof of visibility, solid intersection or text collision.

Specify model/paper tolerance and scale at conversion boundaries. Crop loops, room boundaries and view range are distinct constraints. [view-domain](../assets/blocks/views/view-domain.md) uses declared loops; do not infer an outer loop from incidental order.

## Topology

Use MEPCurve.ConnectorManager or MEPModel.ConnectorManager. Filter domain and supported physical types. AllRefs can include logical/system references; confirm physical connectivity and exclude self/system edges.

[physical-connectors](../assets/blocks/core/physical-connectors.md) yields physical edges; [bounded-graph](../assets/blocks/core/bounded-graph.md) traverses an immutable snapshot. Report seed/parent/distance, boundaries, cycles, caps and shared ownership rather than scanning the entire model.

Reacquire connectors after movement/creation/regeneration/replacement. Persist snapshot records and owner identity; live connector handles are not durable cross-run identity. Distance/size matches are candidates, not proof of connection.

## Matching

Canonicalize [size signatures](../assets/blocks/mep/connector-size-signature.md) with explicit units/tolerance, preserving shape and unsupported cases.

[positional-resolution](../assets/blocks/mep/positional-resolution.md) requires identity/system/size filters and uniqueness/reservation. Distance does not implement solid overlap or validate fitting orientation; specify additional predicates where required.

Use actual relationships and provenance for [host covers](../assets/blocks/mep/host-cover-map.md) and [nested hierarchy](../assets/blocks/mep/nested-hierarchy.md). A parameter naming a host is reference data, not a physical cover relationship.

## Size groups for connector-based operations

For size-dependent type assignment or resizing, build transaction batches from actual physical connector geometry. Include domain, profile shape and dimensions in declared units and tolerance. Read rectangular width and height in the connector's local axes and preserve their order. For round profiles use diameter derived from `2 * Radius`. Resolve other profiles through their supported API contract. Missing or unsupported dimensions remain explicit unresolved inputs.

For transitions, branches and equipment with multiple ports, include all significant ports and their roles in the signature. Establish port correspondence from topology or a verified family mapping. Preserve ordered rectangular dimensions when matching rotated connections through their coordinate frames. Equal dimensions at one port alone do not establish compatibility of complete elements.

Within each size group, separate incompatible categories, families, target types and operation requirements. Apply the [workload limits](mcp-operations.md#объём-пакета-и-восстановление) to produce bounded calls while keeping connected-node edits atomic. Grouping selects elements through the API and does not require changing the UI selection.

Resolve driving family parameters through the actual family bindings and project configuration. The generic workflow uses connector geometry without prescribing user-defined parameter names. Verify resulting geometry after regeneration when writing a driving parameter or assigning a type.

## Edit boundaries

Before modifying a connected segment, capture both sides of each boundary joint with owner/connector IDs, position, orientation, section and system membership. Include both ends and the distant node of a transition. Assess dependent tags, dimensions and insulation when replacing elements. Identify the segment through continuous physical connections; system names and matching sections help find candidates. Check native connector-system membership separately from project labels. Takeoffs can involve physical `ConnectorType.Curve` connections.

Check available straight length and adjacent geometry. Regeneration can reverse a short segment or replace a fitting. Keep disconnection, insertion/replacement and reconnection of a coupled node in one rollback-capable transaction boundary. Reacquire elements/connectors and verify exact pairs, sections, systems, allowed movement, distant points and branch continuity. Roll back when the result violates planned boundaries.

For preservation operations, record the initial gap and orientation of each physically connected pair along with both connector positions. Verify changes against that baseline and the declared tolerances. Existing connected pairs can have a small geometric gap. Preserving that gap may satisfy the operation without repairing it. Any intended geometric correction needs an explicit scope and postcondition. Do not widen tolerances merely to pass a failed verification. A revised tolerance requires a justified criterion, a revised plan and a fresh check.

For `The Tap must be attached to duct`, resolve the element ID in the warning. An existing takeoff elsewhere on the riser may be affected. Physical connections can survive a geometric attachment error. Inspect the approach axis and placement on the round riser. Expand the repair only within the task's authorized scope, including far joints, insulation and dependents. During a rollback probe compare `DocumentChanged` deletions with the initial inventory.

Select [physical-hvac](../assets/blocks/core/physical-hvac.md) for the C# connector helper, [rectangular-elbow-run](../assets/blocks/mep/rectangular-elbow-run.md) for a checked elbow, [retarget-rectangular-accessory](../assets/blocks/mep/retarget-rectangular-accessory.md) for an existing accessory, or [rectangular-takeoff-to-round-riser](../assets/blocks/mep/rectangular-takeoff-to-round-riser.md) for that bounded takeoff operation. Read each block's profile and coverage before composing it.
