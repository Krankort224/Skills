# Смена типа подключённого прямоугольного клапана

[Contract](#contract) · [Purpose](#purpose) · [Inputs and outputs](#inputs-and-outputs) · [Implementation](#implementation) · [Adaptation and limits](#adaptation-and-limits) · [Verification](#verification) · [Provenance](#provenance)

## Contract

| Field | Value |
| --- | --- |
| id | retarget-rectangular-accessory |
| group | mep |
| status | reviewed |
| language | csharp |
| runtime | Revit 2022.1 / rvt-mcp / C# |
| verification | runtime |
| dependencies | physical-hvac |
| mutation | document-write |

## Purpose

Меняет тип существующего экземпляра внутри одного семейства. Сохраняет исходное сечение и физические связи на обоих концах. Для семейства, которое меняет размер при подключении, есть режим временного разъединения с восстановлением тех же стыков.

## Inputs and outputs

ID экземпляра и загруженного типа, ожидаемые ширина и высота, линейный и угловой допуски, точные имена двух параметров экземпляра. Ширина, высота и линейный допуск передаются во внутренних единицах Revit, угловой допуск в радианах. Исходный клапан и обе ответные стороны должны совпасть по порядку B×H.

## Implementation

```csharp
public sealed class RectangularAccessoryRetarget
{
    private sealed class Joint
    {
        public int Port;
        public ElementId PeerOwner;
        public int PeerPort;
        public XYZ Origin;
        public XYZ Direction;
        public XYZ PeerOrigin;
        public XYZ PeerDirection;
        public ElementId System;
        public ElementId PeerSystem;
    }

    private readonly Document document;
    private readonly ElementId instanceId;
    private readonly string instanceUniqueId;
    private readonly ElementId oldType;
    private readonly ElementId newType;
    private readonly double width;
    private readonly double height;
    private readonly double tolerance;
    private readonly double angularTolerance;
    private readonly Joint[] joints;

    private RectangularAccessoryRetarget(
        Document doc, FamilyInstance instance, FamilySymbol target, double width, double height,
        double tolerance, double angularTolerance, Joint[] joints)
    {
        document = doc;
        instanceId = instance.Id;
        instanceUniqueId = instance.UniqueId;
        oldType = instance.GetTypeId();
        newType = target.Id;
        this.width = width;
        this.height = height;
        this.tolerance = tolerance;
        this.angularTolerance = angularTolerance;
        this.joints = joints;
    }

    public static RectangularAccessoryRetarget Capture(
        Document doc, ElementId instanceId, ElementId targetTypeId, double width, double height,
        double tolerance, double angularTolerance)
    {
        var instance = doc.GetElement(instanceId) as FamilyInstance;
        var target = doc.GetElement(targetTypeId) as FamilySymbol;
        if (instance == null || target == null || instance.Symbol.Family.Id != target.Family.Id
            || instance.GetTypeId() == target.Id
            || instance.Category.Id.IntegerValue != (int)BuiltInCategory.OST_DuctAccessory)
            throw new ArgumentException("Expected a different type in the same duct-accessory family.");
        if (!(width > 0) || !(height > 0) || !(tolerance > 0) || !(angularTolerance > 0))
            throw new ArgumentException("Dimensions and tolerances must be positive.");

        var ports = PhysicalHvac.Ports(instance);
        if (ports.Length != 2)
            throw new InvalidOperationException("Expected exactly two physical HVAC ports.");
        var joints = ports.Select(port =>
        {
            var peer = PhysicalHvac.Peers(port).Single();
            if (!PhysicalHvac.RectangularSection(port, width, height, tolerance)
                || !PhysicalHvac.RectangularSection(peer, width, height, tolerance))
                throw new InvalidOperationException("The planned section must match both sides of the existing joint.");
            return new Joint
            {
                Port = port.Id,
                PeerOwner = peer.Owner.Id,
                PeerPort = peer.Id,
                Origin = port.Origin,
                Direction = port.CoordinateSystem.BasisZ,
                PeerOrigin = peer.Origin,
                PeerDirection = peer.CoordinateSystem.BasisZ,
                System = port.MEPSystem?.Id ?? ElementId.InvalidElementId,
                PeerSystem = peer.MEPSystem?.Id ?? ElementId.InvalidElementId
            };
        }).ToArray();
        return new RectangularAccessoryRetarget(doc, instance, target, width, height, tolerance, angularTolerance, joints);
    }

    public void Apply(
        string widthParameter, string heightParameter,
        bool temporarilyDisconnect, Action checkCancellation)
    {
        if (!document.IsModifiable)
            throw new InvalidOperationException("Retarget the accessory inside the caller's transaction.");
        if (string.IsNullOrWhiteSpace(widthParameter) || string.IsNullOrWhiteSpace(heightParameter)
            || widthParameter == heightParameter)
            throw new ArgumentException("Specify the distinct instance dimension parameters.");

        var instance = ResolveInstance();
        if (instance.GetTypeId() != oldType)
            throw new InvalidOperationException("The instance type changed after preflight.");
        VerifyJoints();

        checkCancellation?.Invoke();
        if (temporarilyDisconnect)
        {
            foreach (var joint in joints)
            {
                checkCancellation?.Invoke();
                Port(joint).DisconnectFrom(Peer(joint));
            }
        }

        var replacement = ResolveInstance().ChangeTypeId(newType);
        if (replacement != ElementId.InvalidElementId && replacement != instanceId)
            throw new InvalidOperationException("Revit replaced the accessory instance.");
        document.Regenerate();
        checkCancellation?.Invoke();

        instance = ResolveInstance();
        SetLength(instance, widthParameter, width);
        SetLength(instance, heightParameter, height);
        document.Regenerate();

        if (temporarilyDisconnect)
        {
            foreach (var joint in joints)
            {
                checkCancellation?.Invoke();
                var port = Port(joint);
                var peer = Peer(joint);
                if (!PhysicalHvac.RectangularSection(port, width, height, tolerance)
                    || !PhysicalHvac.RectangularSection(peer, width, height, tolerance)
                    || port.Origin.DistanceTo(peer.Origin) > tolerance)
                    throw new InvalidOperationException("Original connection cannot be restored at the planned section.");
                if (!port.IsConnectedTo(peer))
                    port.ConnectTo(peer);
            }
        }
    }

    public void Verify()
    {
        if (ResolveInstance().GetTypeId() != newType)
            throw new InvalidOperationException("Revit did not retain the requested accessory type.");
        VerifyJoints();
    }

    public void VerifyRollback()
    {
        if (ResolveInstance().GetTypeId() != oldType)
            throw new InvalidOperationException("The original type was not restored.");
        VerifyJoints();
    }

    private void VerifyJoints()
    {
        var instance = ResolveInstance();
        if (PhysicalHvac.Ports(instance).Length != joints.Length)
            throw new InvalidOperationException("The number of accessory ports changed.");

        foreach (var joint in joints)
        {
            var port = Port(joint);
            var peer = Peer(joint);
            var attached = PhysicalHvac.Peers(port).Single();
            if (attached.Owner.Id != joint.PeerOwner || attached.Id != joint.PeerPort
                || !PhysicalHvac.RectangularSection(port, width, height, tolerance)
                || !PhysicalHvac.RectangularSection(peer, width, height, tolerance)
                || port.Origin.DistanceTo(joint.Origin) > tolerance
                || peer.Origin.DistanceTo(joint.PeerOrigin) > tolerance
                || port.CoordinateSystem.BasisZ.AngleTo(joint.Direction) > angularTolerance
                || peer.CoordinateSystem.BasisZ.AngleTo(joint.PeerDirection) > angularTolerance
                || (port.MEPSystem?.Id ?? ElementId.InvalidElementId) != joint.System
                || (peer.MEPSystem?.Id ?? ElementId.InvalidElementId) != joint.PeerSystem)
                throw new InvalidOperationException("The original accessory joint changed at port " + joint.Port + ".");
        }
    }

    private FamilyInstance ResolveInstance()
    {
        var instance = document.GetElement(instanceId) as FamilyInstance;
        if (instance == null || instance.UniqueId != instanceUniqueId)
            throw new InvalidOperationException("The original accessory instance is unavailable.");
        return instance;
    }

    private Connector Port(Joint joint) => PhysicalHvac.Resolve(document, instanceId, joint.Port);

    private Connector Peer(Joint joint) => PhysicalHvac.Resolve(document, joint.PeerOwner, joint.PeerPort);

    private static void SetLength(FamilyInstance instance, string parameterName, double value)
    {
        var parameter = instance.GetParameters(parameterName).Single();
        if (parameter.IsReadOnly || parameter.StorageType != StorageType.Double
            || (parameter.Definition.GetDataType() != SpecTypeId.Length
                && parameter.Definition.GetDataType() != SpecTypeId.DuctSize))
            throw new InvalidOperationException("Expected a writable instance length or duct size: " + parameterName);
        parameter.Set(value);
        if (Math.Abs(parameter.AsDouble() - value) > 1e-8)
            throw new InvalidOperationException("Revit did not retain the instance dimension: " + parameterName);
    }
}
```

## Adaptation and limits

Сними план через `Capture`. Выполни `Apply` в транзакции и `Verify` после нативного коммита дочерней транзакции. Для dry-run проверь `VerifyRollback`. Проектные проверки владения, зависимых элементов, системных расходов и инвентаря соседней сети добавляет вызывающая операция.

## Verification

Режим с временным разъединением в стенде 800×300, с одним экземпляром и двумя воздуховодами. Пройден отказ при перестановке B и H. Поведение без разъединения и другие семейства проверяются отдельной пробой.

[Свидетельство прогона](../../../evidence/revit-2022-mcp-smoke.json)

## Provenance

Imported from the local `revit-mcp` skill on 2026-11-12, source path `assets/blocks/mep/retarget-rectangular-accessory.md`. Original block ID `mcp-retarget-rectangular-accessory`. Original Markdown SHA-256 `ae539229e0fd75fe22042f0af703a9bca30458ebf851da8918beac8ecb85bc8b`.

The implementation fence is preserved. The recorded native [evidence](../../../evidence/revit-2022-mcp-smoke.json) identifies its source hash, host and coverage. Contract/headings were normalized for the shared library; this import performs no new native validation.
