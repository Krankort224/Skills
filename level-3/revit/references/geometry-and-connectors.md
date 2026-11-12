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

## Edit boundaries

Before modifying a connected segment, capture both sides of each boundary joint with owner/connector IDs, position, orientation, section and system membership. Include both ends and the distant node of a transition. Assess dependent tags, dimensions and insulation when replacing elements. Identify the segment through continuous physical connections; system names and matching sections help find candidates. Check native connector-system membership separately from project labels. Takeoffs can involve physical `ConnectorType.Curve` connections.

Check available straight length and adjacent geometry. Regeneration can reverse a short segment or replace a fitting. Keep disconnection, insertion/replacement and reconnection of a coupled node in one rollback-capable transaction boundary. Reacquire elements/connectors and verify exact pairs, sections, systems, allowed movement, distant points and branch continuity. Roll back when the result violates planned boundaries.

For `The Tap must be attached to duct`, resolve the element ID in the warning. An existing takeoff elsewhere on the riser may be affected. Physical connections can survive a geometric attachment error. Inspect the approach axis and placement on the round riser. Expand the repair only within the task's authorized scope, including far joints, insulation and dependents. During a rollback probe compare `DocumentChanged` deletions with the initial inventory.

Select [physical-hvac](../assets/blocks/core/physical-hvac.md) for the C# connector helper, [rectangular-elbow-run](../assets/blocks/mep/rectangular-elbow-run.md) for a checked elbow, [retarget-rectangular-accessory](../assets/blocks/mep/retarget-rectangular-accessory.md) for an existing accessory, or [rectangular-takeoff-to-round-riser](../assets/blocks/mep/rectangular-takeoff-to-round-riser.md) for that bounded takeoff operation. Read each block's profile and coverage before composing it.
