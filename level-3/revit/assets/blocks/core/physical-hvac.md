# Physical HVAC connectors

[Contract](#contract) · [Purpose](#purpose) · [Inputs and outputs](#inputs-and-outputs) · [Implementation](#implementation) · [Adaptation and limits](#adaptation-and-limits) · [Verification](#verification) · [Provenance](#provenance)

## Contract

| Field | Value |
| --- | --- |
| id | physical-hvac |
| group | core |
| status | reviewed |
| language | csharp |
| runtime | Revit 2022.1 / rvt-mcp / C# |
| verification | runtime |
| dependencies | none |
| mutation | read-only |

## Purpose

Resolves physical connectors on ducts and family instances, connected pairs, end connectors by point and rectangular cross-sections.

## Inputs and outputs

Supply a live element or the owner and connector IDs in a verified document. Coordinates, dimensions and linear tolerance use Revit internal units. A point lookup requires exactly one end within tolerance.

## Implementation

```csharp
public static class PhysicalHvac
{
    public static Connector[] Ports(Element element)
    {
        var manager = element is MEPCurve curve
            ? curve.ConnectorManager
            : (element as FamilyInstance)?.MEPModel?.ConnectorManager;
        return manager == null
            ? new Connector[0]
            : manager.Connectors.Cast<Connector>().Where(IsPhysical).OrderBy(port => port.Id).ToArray();
    }

    public static Connector[] Peers(Connector port)
    {
        return port.AllRefs.Cast<Connector>()
            .Where(peer => peer.Owner.Id != port.Owner.Id && IsPhysical(peer) && port.IsConnectedTo(peer))
            .OrderBy(peer => peer.Owner.Id.IntegerValue)
            .ThenBy(peer => peer.Id)
            .ToArray();
    }

    public static Connector AtEnd(Element element, XYZ point, double tolerance)
    {
        return Ports(element)
            .Where(port => port.ConnectorType == ConnectorType.End && port.Origin.DistanceTo(point) <= tolerance)
            .Single();
    }

    public static Connector Resolve(Document doc, ElementId owner, int portId)
    {
        var element = doc.GetElement(owner);
        if (element == null)
            throw new InvalidOperationException("Connector owner disappeared: " + owner.IntegerValue);
        return Ports(element).Single(port => port.Id == portId);
    }

    public static bool RectangularSection(Connector port, double width, double height, double tolerance)
    {
        return port.Shape == ConnectorProfileType.Rectangular
            && Math.Abs(port.Width - width) <= tolerance
            && Math.Abs(port.Height - height) <= tolerance;
    }

    private static bool IsPhysical(Connector port)
    {
        return port.Domain == Domain.DomainHvac
            && (port.ConnectorType == ConnectorType.End
                || port.ConnectorType == ConnectorType.Curve
                || port.ConnectorType == ConnectorType.Physical);
    }
}
```

## Adaptation and limits

After `Regenerate`, a type change or reconnection, resolve the connector again by owner and connector ID. Record both endpoint identities for topology. `Ports` accepts physical `Curve` connections. The evidence verifies `End` connections and preservation of an existing `Curve` connection in the takeoff scenario.

## Verification

Used when creating an elbow and restoring both connections of a damper.

[Native run evidence](../../../evidence/revit-2022-mcp-smoke.json)

## Provenance

Imported from the local `revit-mcp` skill on 2026-11-12, source path `assets/blocks/core/physical-hvac.md`. Original block ID `mcp-physical-hvac`. Original Markdown SHA-256 `087eac342e9ef095941dea2fa82af38c7a2fb5b64505dfcb7ef9bd5281fc7a77`.

The implementation fence is preserved. The recorded native [evidence](../../../evidence/revit-2022-mcp-smoke.json) identifies its source hash, host and coverage. Contract/headings were normalized for the shared library; this import performs no new native validation.
