# Два прямоугольных воздуховода с отводом

[Contract](#contract) · [Purpose](#purpose) · [Inputs and outputs](#inputs-and-outputs) · [Implementation](#implementation) · [Adaptation and limits](#adaptation-and-limits) · [Verification](#verification) · [Provenance](#provenance)

## Contract

| Field | Value |
| --- | --- |
| id | rectangular-elbow-run |
| group | mep |
| status | reviewed |
| language | csharp |
| runtime | Revit 2022.1 / rvt-mcp / C# |
| verification | runtime |
| dependencies | physical-hvac |
| mutation | document-write |

## Purpose

Строит два участка одинакового сечения по трём точкам и соединяет их штатным отводом. Возвращает ID двух воздуховодов и фитинга.

## Inputs and outputs

ID типа системы, прямоугольного типа воздуховода и уровня в проверенном документе. Тип воздуховода должен иметь подходящее правило трассировки для отвода. Точки, размеры и допуск передаются во внутренних единицах Revit.

## Implementation

```csharp
public sealed class RectangularElbowRun
{
    public readonly ElementId FirstDuct;
    public readonly ElementId SecondDuct;
    public readonly ElementId Elbow;

    private readonly ElementId systemType;
    private readonly ElementId ductType;
    private readonly ElementId level;

    private RectangularElbowRun(ElementId firstDuct, ElementId secondDuct, ElementId elbow,
        ElementId systemType, ElementId ductType, ElementId level)
    {
        FirstDuct = firstDuct;
        SecondDuct = secondDuct;
        Elbow = elbow;
        this.systemType = systemType;
        this.ductType = ductType;
        this.level = level;
    }

    public static RectangularElbowRun Create(
        Document doc, ElementId systemTypeId, ElementId ductTypeId, ElementId levelId,
        XYZ start, XYZ corner, XYZ end, double width, double height, double tolerance)
    {
        if (!doc.IsModifiable)
            throw new InvalidOperationException("Create the run inside the caller's transaction.");
        var systemType = doc.GetElement(systemTypeId) as MechanicalSystemType;
        var ductType = doc.GetElement(ductTypeId) as DuctType;
        var level = doc.GetElement(levelId) as Level;
        if (systemType == null || ductType == null || level == null || ductType.Shape != ConnectorProfileType.Rectangular)
            throw new ArgumentException("Resolve a rectangular duct type, system type and level in the target document.");
        if (!(width > 0) || !(height > 0) || !(tolerance > 0)
            || start.DistanceTo(corner) <= doc.Application.ShortCurveTolerance
            || end.DistanceTo(corner) <= doc.Application.ShortCurveTolerance)
            throw new ArgumentException("Invalid dimensions, tolerance or duct segment lengths.");

        var first = Duct.Create(doc, systemType.Id, ductType.Id, level.Id, start, corner);
        var second = Duct.Create(doc, systemType.Id, ductType.Id, level.Id, corner, end);
        foreach (var duct in new[] { first, second })
        {
            SetDimension(duct, BuiltInParameter.RBS_CURVE_WIDTH_PARAM, width);
            SetDimension(duct, BuiltInParameter.RBS_CURVE_HEIGHT_PARAM, height);
        }

        doc.Regenerate();
        var firstEnd = PhysicalHvac.AtEnd(first, corner, tolerance);
        var secondEnd = PhysicalHvac.AtEnd(second, corner, tolerance);
        var elbow = doc.Create.NewElbowFitting(firstEnd, secondEnd);
        if (elbow == null)
            throw new InvalidOperationException("Revit did not create the requested elbow.");
        return new RectangularElbowRun(first.Id, second.Id, elbow.Id, systemType.Id, ductType.Id, level.Id);
    }

    public void Verify(Document doc, XYZ start, XYZ end, double width, double height, double tolerance)
    {
        var first = doc.GetElement(FirstDuct) as Duct;
        var second = doc.GetElement(SecondDuct) as Duct;
        var elbow = doc.GetElement(Elbow) as FamilyInstance;
        var fitting = elbow?.MEPModel as MechanicalFitting;
        if (first == null || second == null || fitting == null || fitting.PartType != PartType.Elbow)
            throw new InvalidOperationException("Expected two ducts and a native elbow.");

        foreach (var duct in new[] { first, second })
        {
            if (duct.GetTypeId() != ductType || duct.ReferenceLevel?.Id != level
                || duct.get_Parameter(BuiltInParameter.RBS_DUCT_SYSTEM_TYPE_PARAM)?.AsElementId() != systemType)
                throw new InvalidOperationException("Duct type, reference level or system type changed.");
        }

        var firstFree = PhysicalHvac.AtEnd(first, start, tolerance);
        var secondFree = PhysicalHvac.AtEnd(second, end, tolerance);
        var elbowPorts = PhysicalHvac.Ports(elbow);
        var allPorts = PhysicalHvac.Ports(first).Concat(PhysicalHvac.Ports(second)).Concat(elbowPorts);
        if (PhysicalHvac.Peers(firstFree).Length != 0 || PhysicalHvac.Peers(secondFree).Length != 0
            || elbowPorts.Length != 2 || !allPorts.All(port => PhysicalHvac.RectangularSection(port, width, height, tolerance)))
            throw new InvalidOperationException("Unexpected exterior connection or rectangular section.");

        var peerOwners = elbowPorts.Select(port => PhysicalHvac.Peers(port).Single().Owner.Id);
        if (!new HashSet<ElementId>(peerOwners).SetEquals(new[] { FirstDuct, SecondDuct }))
            throw new InvalidOperationException("Elbow is not connected directly to both planned ducts.");
    }

    private static void SetDimension(Duct duct, BuiltInParameter parameter, double value)
    {
        var item = duct.get_Parameter(parameter);
        if (item == null || item.IsReadOnly || item.StorageType != StorageType.Double)
            throw new InvalidOperationException("Missing writable duct dimension: " + parameter);
        item.Set(value);
    }
}
```

## Adaptation and limits

Вызови `Create` внутри транзакции и `Verify` после нативного коммита дочерней транзакции. `Verify` сверяет типы, уровень, сечение, свободные внешние концы и обе физические связи отвода. Длины сегментов могут измениться на величину подрезки при установке фитинга.

## Verification

Два поворота на 90° с разными направлениями, высотами и сечениями 400×250 и 500×300. Для других углов и правил трассировки нужен отдельный прогон.

[Свидетельство прогона](../../../evidence/revit-2022-mcp-smoke.json)

## Provenance

Imported from the local `revit-mcp` skill on 2026-11-12, source path `assets/blocks/mep/rectangular-elbow-run.md`. Original block ID `mcp-rectangular-elbow-run`. Original Markdown SHA-256 `5de6249468a9eae803cce9c9986ce3f4b5262a9f0651f65b860c5fbfefa4f727`.

The implementation fence is preserved. The recorded native [evidence](../../../evidence/revit-2022-mcp-smoke.json) identifies its source hash, host and coverage. Contract/headings were normalized for the shared library; this import performs no new native validation.
