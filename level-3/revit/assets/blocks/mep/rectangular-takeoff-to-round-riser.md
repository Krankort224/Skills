# Прямоугольная врезка в круглый стояк

[Contract](#contract) · [Purpose](#purpose) · [Inputs and outputs](#inputs-and-outputs) · [Implementation](#implementation) · [Adaptation and limits](#adaptation-and-limits) · [Verification](#verification) · [Provenance](#provenance)

## Contract

| Field | Value |
| --- | --- |
| id | rectangular-takeoff-to-round-riser |
| group | mep |
| status | reviewed |
| language | csharp |
| runtime | Revit 2022.1 / rvt-mcp / C# |
| verification | runtime |
| dependencies | physical-hvac, checked-model-edit |
| mutation | document-write |

## Purpose

Создаёт прямоугольную врезку на круглом стояке через `NewTakeoffFitting`. Выбранный тип должен быть загружен. Если Revit создаёт другой тип того же семейства, блок назначает выбранный тип и проверяет результат.

## Inputs and outputs

ID двух прямолинейных воздуховодов, ID свободного прямоугольного коннектора горизонтальной ветки, ID ожидаемого типа врезки, линейный допуск во внутренних единицах Revit и угловой допуск в радианах. Ось подхода должна попадать в ось вертикального стояка внутри его прямого участка. Воздуховоды должны иметь один тип системы. Принадлежность ветки и стояка к одной проектной системе проверь при составлении плана.

## Implementation

```csharp
public sealed class RectangularTakeoffToRoundRiser
{
    private sealed class PortState
    {
        public readonly int Id;
        public readonly ConnectorType Kind;
        public readonly ConnectorProfileType Shape;
        public readonly XYZ Origin;
        public readonly XYZ Direction;
        public readonly XYZ WidthAxis;
        public readonly double Width;
        public readonly double Height;
        public readonly double Radius;
        public readonly Tuple<int, int>[] Links;

        public PortState(Connector port)
        {
            Id = port.Id;
            Kind = port.ConnectorType;
            Shape = port.Shape;
            Origin = port.Origin;
            Direction = port.CoordinateSystem.BasisZ;
            if (Shape == ConnectorProfileType.Rectangular)
            {
                WidthAxis = port.CoordinateSystem.BasisX;
                Width = port.Width;
                Height = port.Height;
            }
            if (Shape == ConnectorProfileType.Round)
                Radius = port.Radius;
            Links = ReadLinks(port);
        }

        private static Tuple<int, int>[] ReadLinks(Connector port)
        {
            return PhysicalHvac.Peers(port).Select(peer => Tuple.Create(peer.Owner.Id.IntegerValue, peer.Id)).ToArray();
        }

        public void Check(Connector port, double linear, double cosine, bool allowNewConnection)
        {
            Require(port.ConnectorType == Kind && port.Shape == Shape
                && (Shape != ConnectorProfileType.Rectangular || (PhysicalHvac.RectangularSection(port, Width, Height, linear)
                    && Math.Abs(port.CoordinateSystem.BasisX.DotProduct(WidthAxis)) >= cosine))
                && (Shape != ConnectorProfileType.Round || Math.Abs(port.Radius - Radius) <= linear)
                && port.CoordinateSystem.BasisZ.DotProduct(Direction) >= cosine,
                "Changed connector type, section or direction: " + port.Owner.Id + "/" + Id);

            var displacement = port.Origin - Origin;
            Require((allowNewConnection ? displacement.CrossProduct(Direction) : displacement).GetLength() <= linear,
                "Connector moved outside the planned axis or fixed point: " + port.Owner.Id + "/" + Id);
            if (!allowNewConnection)
                Require(ReadLinks(port).SequenceEqual(Links), "Existing connection changed: " + port.Owner.Id + "/" + Id);
        }
    }

    private sealed class DuctState
    {
        public readonly ElementId Id;
        public readonly PortState[] Ports;
        private readonly ElementId type;
        private readonly ElementId system;
        private readonly ElementId level;
        private readonly WorksetId workset;

        public DuctState(Duct duct)
        {
            Id = duct.Id;
            type = duct.GetTypeId();
            system = SystemType(duct);
            level = duct.ReferenceLevel?.Id;
            workset = duct.WorksetId;
            Ports = PhysicalHvac.Ports(duct).Select(port => new PortState(port)).ToArray();
        }

        public Duct Check(Document doc, double linear, double cosine, int freeEnd, int addedPorts)
        {
            var duct = doc.GetElement(Id) as Duct;
            Require(duct != null && duct.GetTypeId() == type && SystemType(duct) == system
                && duct.ReferenceLevel?.Id == level && duct.WorksetId.IntegerValue == workset.IntegerValue,
                "Duct type, system type, level or workset changed: " + Id);
            Require(PhysicalHvac.Ports(duct).Length == Ports.Length + addedPorts, "Unexpected port count: " + Id);
            foreach (var port in Ports)
                port.Check(PhysicalHvac.Resolve(doc, Id, port.Id), linear, cosine, port.Id == freeEnd);
            return duct;
        }
    }

    private readonly Document doc;
    private readonly DuctState branch;
    private readonly DuctState riser;
    private readonly int endId;
    private readonly ElementId symbolId;
    private readonly XYZ hit;
    private readonly double linear;
    private readonly double cosine;
    public ElementId FittingId { get; private set; } = ElementId.InvalidElementId;

    private RectangularTakeoffToRoundRiser(
        Document doc, Duct branch, int endId, Duct riser, ElementId symbolId, XYZ hit, double linear, double cosine)
    {
        this.doc = doc;
        this.branch = new DuctState(branch);
        this.riser = new DuctState(riser);
        this.endId = endId;
        this.symbolId = symbolId;
        this.hit = hit;
        this.linear = linear;
        this.cosine = cosine;
    }

    public static RectangularTakeoffToRoundRiser Capture(Document doc, ElementId branchId, int endId,
        ElementId riserId, ElementId symbolId, double linear, double angular)
    {
        Require(doc != null && !doc.IsModifiable, "Capture requires a document outside a transaction.");
        Require(linear > 0 && !double.IsInfinity(linear) && angular > 0 && angular < Math.PI / 2,
            "Positive finite tolerances are required.");
        var branch = doc.GetElement(branchId) as Duct;
        var riser = doc.GetElement(riserId) as Duct;
        var symbol = doc.GetElement(symbolId) as FamilySymbol;
        Require(branch != null && riser != null && branch.Id != riser.Id && symbol != null
            && symbol.Category?.Id.IntegerValue == (int)BuiltInCategory.OST_DuctFitting,
            "Two different ducts and a loaded duct fitting type are required.");
        Require(SystemType(branch) != ElementId.InvalidElementId && SystemType(branch) == SystemType(riser),
            "Duct systems are incompatible.");
        Require(!branch.Pinned && !riser.Pinned && branch.GroupId == ElementId.InvalidElementId
            && riser.GroupId == ElementId.InvalidElementId, "Ducts must be unpinned and outside model groups.");

        var branchLine = (branch.Location as LocationCurve)?.Curve as Line;
        var riserLine = (riser.Location as LocationCurve)?.Curve as Line;
        var cosine = Math.Cos(angular);
        Require(branchLine != null && riserLine != null && Math.Abs(branchLine.Direction.Z) <= Math.Sin(angular)
            && Math.Abs(riserLine.Direction.Z) >= cosine, "Expected a straight horizontal branch and vertical riser.");

        var end = PhysicalHvac.Resolve(doc, branchId, endId);
        Require(end.ConnectorType == ConnectorType.End && end.Shape == ConnectorProfileType.Rectangular && !end.IsConnected,
            "The selected branch port must be an open rectangular end.");
        var riserEnds = PhysicalHvac.Ports(riser).Where(p => p.ConnectorType == ConnectorType.End).ToArray();
        Require(riserEnds.Length == 2 && riserEnds.All(p => p.Shape == ConnectorProfileType.Round),
            "Expected two round riser ends.");

        var start = riserLine.GetEndPoint(0);
        var station = (end.Origin - start).DotProduct(riserLine.Direction);
        var hit = start + riserLine.Direction.Multiply(station);
        var approach = hit - end.Origin;
        var facing = end.CoordinateSystem.BasisZ;
        Require(station > linear && station < riserLine.Length - linear
            && approach.DotProduct(facing) > linear && approach.CrossProduct(facing).GetLength() <= linear,
            "The open branch end must face the interior of the riser axis.");
        return new RectangularTakeoffToRoundRiser(doc, branch, endId, riser, symbolId, hit, linear, cosine);
    }

    public void Apply()
    {
        Require(doc.IsModifiable, "Apply requires a caller-owned transaction.");
        VerifyRollback();
        var fitting = doc.Create.NewTakeoffFitting(PhysicalHvac.Resolve(doc, branch.Id, endId), (Duct)doc.GetElement(riser.Id));
        doc.Regenerate();
        FittingId = fitting.Id;
        if (fitting.GetTypeId() != symbolId)
        {
            var symbol = (FamilySymbol)doc.GetElement(symbolId);
            Require(fitting.Symbol.Family.Id == symbol.Family.Id, "Routing selected a different fitting family.");
            var replacement = fitting.ChangeTypeId(symbolId);
            if (replacement != ElementId.InvalidElementId)
                FittingId = replacement;
        }
        doc.Regenerate();
    }

    public void Verify()
    {
        var duct = branch.Check(doc, linear, cosine, endId, 0);
        riser.Check(doc, linear, cosine, -1, 1);
        Require((duct.Location as LocationCurve)?.Curve is Line line && line.Length > linear, "Branch length is invalid.");
        var fitting = doc.GetElement(FittingId) as FamilyInstance;
        Require(fitting != null && fitting.GetTypeId() == symbolId, "Expected takeoff type was not created.");

        var end = PhysicalHvac.Resolve(doc, branch.Id, endId);
        var neighbors = PhysicalHvac.Peers(end);
        Require(neighbors.Length == 1 && neighbors[0].Owner.Id == FittingId, "The branch does not connect to the takeoff.");
        var branchSide = neighbors[0];
        var branchFrame = end.CoordinateSystem;
        var fittingFrame = branchSide.CoordinateSystem;
        var axesMatch = Math.Abs(branchFrame.BasisX.DotProduct(fittingFrame.BasisX)) >= cosine
            && Math.Abs(branchFrame.BasisY.DotProduct(fittingFrame.BasisY)) >= cosine;
        var axesCross = Math.Abs(branchFrame.BasisX.DotProduct(fittingFrame.BasisY)) >= cosine
            && Math.Abs(branchFrame.BasisY.DotProduct(fittingFrame.BasisX)) >= cosine;
        var sameSection = (axesMatch && PhysicalHvac.RectangularSection(branchSide, end.Width, end.Height, linear))
            || (axesCross && PhysicalHvac.RectangularSection(branchSide, end.Height, end.Width, linear));
        Require(sameSection && branchSide.Origin.DistanceTo(end.Origin) <= linear
            && fittingFrame.BasisZ.DotProduct(branchFrame.BasisZ) <= -cosine,
            "Branch and takeoff ports do not match.");
        var ports = PhysicalHvac.Ports(fitting);
        Require(ports.Length == 2 && ports.All(p => PhysicalHvac.Peers(p).Length == 1),
            "Expected a two-port takeoff with two physical links.");
        var host = PhysicalHvac.Peers(ports.Single(p => p.Id != branchSide.Id))[0];
        Require(host.Owner.Id == riser.Id && host.ConnectorType == ConnectorType.Curve && host.Origin.DistanceTo(hit) <= linear,
            "The takeoff does not connect to the planned riser station.");
    }

    public void VerifyRollback()
    {
        branch.Check(doc, linear, cosine, -1, 0);
        riser.Check(doc, linear, cosine, -1, 0);
        Require(FittingId == ElementId.InvalidElementId || doc.GetElement(FittingId) == null,
            "The takeoff already exists or survived rollback.");
    }

    private static ElementId SystemType(Duct duct)
    {
        return duct.get_Parameter(BuiltInParameter.RBS_DUCT_SYSTEM_TYPE_PARAM)?.AsElementId() ?? ElementId.InvalidElementId;
    }

    private static void Require(bool valid, string message)
    {
        if (!valid) throw new InvalidOperationException(message);
    }
}
```

## Adaptation and limits

Сними план через `Capture`. В `CheckedModelEdit` передай `Apply`, `Verify` и для пробного прогона `VerifyRollback`. После записи повтори `Verify` отдельным чтением документа. Прямой участок ветки может удлиниться или укоротиться вдоль своей оси. При сохранённых связях блок сверяет ID обоих коннекторов, положение, направление и сечения. При стыковке с фитингом размеры сверяются по физическим осям портов. Границы по зависимым элементам и автоматические изменения Revit проверяет вызывающая операция.

**Диагностика.** Если нативный коммит выдаёт предупреждение о врезке, проверь элемент по ID предупреждения и геометрию его подхода. [Границы изменений](../../../references/geometry-and-connectors.md#edit-boundaries)

## Verification

Revit 2022.1, ветка 250×180 и стояк Ø400. Сохранены существующая врезка и дальний стык. Пройдены выбор другого типа того же семейства, отказ для занятого коннектора, пробный коммит с откатом и откат после ошибки итоговой проверки.

[Свидетельство прогона](../../../evidence/revit-2022-mcp-smoke.json)

## Provenance

Imported from the local `revit-mcp` skill on 2026-11-12, source path `assets/blocks/mep/rectangular-takeoff-to-round-riser.md`. Original block ID `mcp-rectangular-takeoff-to-round-riser`. Original Markdown SHA-256 `11b1fa0947208d0c3e9921fa891209e14031b29a5cc81ab81b7d0a65a21bdfac`.

The implementation fence is preserved. The recorded native [evidence](../../../evidence/revit-2022-mcp-smoke.json) identifies its source hash, host and coverage. Contract/headings were normalized for the shared library; this import performs no new native validation.
