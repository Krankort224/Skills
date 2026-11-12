public class DuctFixture
{
    internal static void Need(bool ok, string message)
    {
        if (!ok) throw new InvalidOperationException(message);
    }
    internal static int[] Inventory(Document doc)
    {
        return new FilteredElementCollector(doc).WhereElementIsNotElementType()
            .Where(e => e.Category != null && (e.Category.Id.IntegerValue == (int)BuiltInCategory.OST_DuctCurves
              || e.Category.Id.IntegerValue == (int)BuiltInCategory.OST_DuctFitting))
            .Select(e => e.Id.IntegerValue).OrderBy(id => id).ToArray();
    }

    internal static string DocumentKey(Document doc)
    {
        return doc == null ? "" : doc.Title + "|" + doc.PathName + "|" + doc.ProjectInformation?.UniqueId;
    }

    public static object Run(UIApplication app)
    {
        var active = DocumentKey(app.ActiveUIDocument?.Document);
        var doc = app.Application.NewProjectDocument(McpSkillFixture.DuctTemplate);
        try
        {
            Need(DocumentKey(doc) != active, "Scratch document must differ from the active project.");
            var level = new FilteredElementCollector(doc).OfClass(typeof(Level)).Cast<Level>().First();
            var system = new FilteredElementCollector(doc).OfClass(typeof(MechanicalSystemType)).Cast<MechanicalSystemType>()
                .First(x => x.SystemClassification == MEPSystemClassification.SupplyAir);
            var type = new FilteredElementCollector(doc).OfClass(typeof(DuctType)).Cast<DuctType>()
                .First(x => x.Shape == ConnectorProfileType.Rectangular
                    && x.RoutingPreferenceManager.GetNumberOfRules(RoutingPreferenceRuleGroupType.Elbows) > 0);
            var initial = Inventory(doc);
            var z = level.Elevation + 10;
            var tol = 0.1 / 304.8;
            var a = new XYZ(0, 0, z);
            var b = new XYZ(15, 0, z);
            var c = new XYZ(15, 15, z);
            RectangularElbowRun run = null;
            var dry = CheckedModelEdit.Run(doc, "Disposable dry run", true,
                () => run = RectangularElbowRun.Create(doc, system.Id, type.Id, level.Id, a, b, c, 400.0/304.8, 250.0/304.8, tol),
                () => run.Verify(doc, a, c, 400.0/304.8, 250.0/304.8, tol),
                () => Need(Inventory(doc).SequenceEqual(initial), "Dry run did not restore initial inventory."),
                null);

            var failed = false;
            try
            {
                CheckedModelEdit.Run(doc, "Forced verification failure", false,
                    () => run = RectangularElbowRun.Create(doc, system.Id, type.Id, level.Id, a, b, c, 400.0/304.8, 250.0/304.8, tol),
                    () => { throw new InvalidOperationException("forced verification failure"); }, null, null);
            }
            catch (InvalidOperationException e) when (e.Message == "forced verification failure")
            {
                failed = true;
            }
            Need(failed && Inventory(doc).SequenceEqual(initial), "Verification failure left changes.");

            var cancelled = false;
            var cancelChecks = 0;
            try
            {
                CheckedModelEdit.Run(doc, "Cooperative cancel", false,
                    () => run = RectangularElbowRun.Create(doc, system.Id, type.Id, level.Id, a, b, c, 400.0/304.8, 250.0/304.8, tol),
                    () => run.Verify(doc, a, c, 400.0/304.8, 250.0/304.8, tol), null,
                    () => { if (++cancelChecks == 2) throw new OperationCanceledException(); });
            }
            catch (OperationCanceledException)
            {
                cancelled = true;
            }
            Need(cancelled && Inventory(doc).SequenceEqual(initial), "Cancellation left changes.");

            var x = new XYZ(30, 0, z + 3);
            var y = new XYZ(30, 15, z + 3);
            var v = new XYZ(15, 15, z + 3);
            var write = CheckedModelEdit.Run(doc, "Disposable write", false,
                () => run = RectangularElbowRun.Create(doc, system.Id, type.Id, level.Id, x, y, v, 500.0/304.8, 300.0/304.8, tol),
                () => run.Verify(doc, x, v, 500.0/304.8, 300.0/304.8, tol), null, null);
            run.Verify(doc, x, v, 500.0/304.8, 300.0/304.8, tol);
            Need(Inventory(doc).Except(initial).Count() == 3, "Unexpected added inventory.");
            return new{status="NATIVE_OK",revit=app.Application.VersionNumber,build=app.Application.VersionBuild,
                dry_child=dry.Transaction.ToString(),dry_group=dry.Group.ToString(),write_group=write.Group.ToString(),
                dry_section_mm=new[]{400,250},write_section_mm=new[]{500,300},added=3,forced_failure_rolled_back=failed,
                cancellation_rolled_back=cancelled,routing=type.Name,active_unchanged=DocumentKey(app.ActiveUIDocument?.Document)==active};
        }
        finally
        {
            doc.Close(false);
        }
    }
}

public class AccessoryFixture
{
    static void Need(bool ok, string message)
    {
        if (!ok) throw new InvalidOperationException(message);
    }

    static int[] Inventory(Document doc)
    {
        return new FilteredElementCollector(doc).WhereElementIsNotElementType()
            .Where(e => e.Category != null && (e.Category.Id.IntegerValue == (int)BuiltInCategory.OST_DuctCurves
              || e.Category.Id.IntegerValue == (int)BuiltInCategory.OST_DuctFitting
              || e.Category.Id.IntegerValue == (int)BuiltInCategory.OST_DuctAccessory))
            .Select(e => e.Id.IntegerValue).OrderBy(id => id).ToArray();
    }


    static string DocumentKey(Document doc)
    {
        return doc == null ? "" : doc.Title + "|" + doc.PathName + "|" + doc.ProjectInformation?.UniqueId;
    }

    public static object Run(UIApplication app)
    {
        var active = DocumentKey(app.ActiveUIDocument?.Document);
        var doc = app.Application.OpenDocumentFile(McpSkillFixture.AccessoryProject);
        try
        {
            Need(DocumentKey(doc) != active, "Fixture must differ from the active project.");
            var types = new FilteredElementCollector(doc).OfClass(typeof(FamilySymbol)).Cast<FamilySymbol>()
                .Where(s => s.Family.Name == McpSkillFixture.FamilyName).ToDictionary(s => s.Name);
            var source = types[McpSkillFixture.OldType];
            var target = types[McpSkillFixture.NewType];
            var level = new FilteredElementCollector(doc).OfClass(typeof(Level)).Cast<Level>().First();
            var system = new FilteredElementCollector(doc).OfClass(typeof(MechanicalSystemType)).Cast<MechanicalSystemType>()
                .First(x => x.SystemClassification == MEPSystemClassification.SupplyAir);
            var ductType = new FilteredElementCollector(doc).OfClass(typeof(DuctType)).Cast<DuctType>()
                .First(x => x.Shape == ConnectorProfileType.Rectangular);
            var width = McpSkillFixture.WidthMm / 304.8;
            var height = McpSkillFixture.HeightMm / 304.8;
            var tol = 0.1 / 304.8;
            var angleTol = 0.05 * Math.PI / 180.0;
            ElementId valveId = ElementId.InvalidElementId;
            using (var fixtureTx = new Transaction(doc, "Prepare disposable connected fixture"))
            {
                Need(fixtureTx.Start() == TransactionStatus.Started, "Fixture transaction did not start.");
                source.Activate();
                doc.Regenerate();
                var valve = doc.Create.NewFamilyInstance(new XYZ(0, 0, 10), source, level,
                    Autodesk.Revit.DB.Structure.StructuralType.NonStructural);
                valveId = valve.Id;
                valve.GetParameters(McpSkillFixture.WidthParameter).Single().Set(width);
                valve.GetParameters(McpSkillFixture.HeightParameter).Single().Set(height);
                doc.Regenerate();

                var ends = PhysicalHvac.Ports(valve).Select(port => new
                {
                    port.Id,
                    port.Origin,
                    Axis = port.CoordinateSystem.BasisZ
                }).ToArray();
                Need(ends.Length == 2, "Fixture valve requires two HVAC ports.");
                foreach (var end in ends)
                {
                    var duct = Duct.Create(doc, system.Id, ductType.Id, level.Id, end.Origin + end.Axis.Multiply(12), end.Origin);
                    duct.get_Parameter(BuiltInParameter.RBS_CURVE_WIDTH_PARAM).Set(width);
                    duct.get_Parameter(BuiltInParameter.RBS_CURVE_HEIGHT_PARAM).Set(height);
                    doc.Regenerate();
                    PhysicalHvac.Resolve(doc, valveId, end.Id).ConnectTo(PhysicalHvac.AtEnd(duct, end.Origin, tol));
                }
                Need(fixtureTx.Commit() == TransactionStatus.Committed, "Fixture transaction did not commit.");
            }

            var baseline = Inventory(doc);
            var plan = RectangularAccessoryRetarget.Capture(doc, valveId, target.Id, width, height, tol, angleTol);
            bool rejected = false;
            try
            {
                RectangularAccessoryRetarget.Capture(doc, valveId, target.Id, height, width, tol, angleTol);
            }
            catch (InvalidOperationException)
            {
                rejected = true;
            }
            Need(rejected && Inventory(doc).SequenceEqual(baseline), "Swapped dimensions were not rejected safely.");

            var dry = CheckedModelEdit.Run(doc, "Dry run of accessory retarget", true,
                () => plan.Apply(McpSkillFixture.WidthParameter, McpSkillFixture.HeightParameter, true, null),
                plan.Verify,
                () => { plan.VerifyRollback(); Need(Inventory(doc).SequenceEqual(baseline), "Dry retarget changed inventory."); },
                null);
            var write = CheckedModelEdit.Run(doc, "Commit in disposable fixture", false,
                () => plan.Apply(McpSkillFixture.WidthParameter, McpSkillFixture.HeightParameter, true, null), plan.Verify, null, null);
            plan.Verify();
            Need(Inventory(doc).SequenceEqual(baseline), "Retarget created or removed an element.");
            var live = (FamilyInstance)doc.GetElement(valveId);
            return new{status="NATIVE_OK",revit=app.Application.VersionNumber,build=app.Application.VersionBuild,
                dry_group=dry.Group.ToString(),write_group=write.Group.ToString(),same_instance=live.Id==valveId,
                type=live.Symbol.Name,section_mm=new[]{McpSkillFixture.WidthMm,McpSkillFixture.HeightMm},original_links=2,inventory_unchanged=true,
                swapped_dimensions_rejected=rejected,active_unchanged=DocumentKey(app.ActiveUIDocument?.Document)==active};
        }
        finally
        {
            doc.Close(false);
        }
    }
}

public class TakeoffFixture
{
    public static object Run(UIApplication app)
    {
        var active = DuctFixture.DocumentKey(app.ActiveUIDocument?.Document);
        var doc = app.Application.NewProjectDocument(McpSkillFixture.DuctTemplate);
        try
        {
            DuctFixture.Need(DuctFixture.DocumentKey(doc) != active, "Takeoff fixture must differ from the active project.");
            var level = new FilteredElementCollector(doc).OfClass(typeof(Level)).Cast<Level>().First();
            var system = new FilteredElementCollector(doc).OfClass(typeof(MechanicalSystemType)).Cast<MechanicalSystemType>()
                .First(t => t.SystemClassification == MEPSystemClassification.SupplyAir);
            var types = new FilteredElementCollector(doc).OfClass(typeof(DuctType)).Cast<DuctType>().ToArray();
            var junctions = RoutingPreferenceRuleGroupType.Junctions;
            DuctType TapType(ConnectorProfileType shape)
            {
                return types.First(t => t.Shape == shape && t.RoutingPreferenceManager.PreferredJunctionType == PreferredJunctionType.Tap
                    && t.RoutingPreferenceManager.GetNumberOfRules(junctions) > 0);
            }

            var rectangular = TapType(ConnectorProfileType.Rectangular);
            var round = TapType(ConnectorProfileType.Round);
            var routingSymbolId = rectangular.RoutingPreferenceManager.GetRule(junctions, 0).MEPPartId;
            ElementId symbolId;
            var tol = 0.1 / 304.8;
            var angleTol = 0.05 * Math.PI / 180.0;
            var z = level.Elevation + 10;
            var branchEnd = new XYZ(1.5, 0, z);
            var farEnd = new XYZ(12, 0, z);
            var priorEnd = new XYZ(0, 1.5, z + 3);
            ElementId branchId;
            ElementId riserId;
            ElementId priorId;
            ElementId priorFittingId;
            using (var tx = new Transaction(doc, "Prepare disposable takeoff fixture"))
            {
                DuctFixture.Need(tx.Start() == TransactionStatus.Started, "Takeoff fixture transaction did not start.");
                tx.SetFailureHandlingOptions(tx.GetFailureHandlingOptions()
                    .SetFailuresPreprocessor(new RvtMcp.Plugin.SafeFailuresPreprocessor()).SetClearAfterRollback(true));
                Duct Rectangular(XYZ start, XYZ end)
                {
                    var duct = Duct.Create(doc, system.Id, rectangular.Id, level.Id, start, end);
                    duct.get_Parameter(BuiltInParameter.RBS_CURVE_WIDTH_PARAM).Set(250.0 / 304.8);
                    duct.get_Parameter(BuiltInParameter.RBS_CURVE_HEIGHT_PARAM).Set(180.0 / 304.8);
                    return duct;
                }

                var riser = Duct.Create(doc, system.Id, round.Id, level.Id, new XYZ(0, 0, z - 10), new XYZ(0, 0, z + 10));
                riser.get_Parameter(BuiltInParameter.RBS_CURVE_DIAMETER_PARAM).Set(400.0 / 304.8);
                var branch = Rectangular(farEnd, branchEnd);
                var continuation = Rectangular(new XYZ(20, 0, z), farEnd);
                var prior = Rectangular(new XYZ(0, 12, z + 3), priorEnd);
                branchId = branch.Id;
                riserId = riser.Id;
                priorId = prior.Id;
                doc.Regenerate();
                PhysicalHvac.AtEnd(branch, farEnd, tol).ConnectTo(PhysicalHvac.AtEnd(continuation, farEnd, tol));
                priorFittingId = doc.Create.NewTakeoffFitting(PhysicalHvac.AtEnd(prior, priorEnd, tol), riser).Id;
                var routingSymbol = (FamilySymbol)doc.GetElement(routingSymbolId);
                symbolId = routingSymbol.Duplicate("MCP fixture target takeoff").Id;
                DuctFixture.Need(tx.Commit() == TransactionStatus.Committed, "Takeoff fixture did not commit.");
            }

            var duct = doc.GetElement(branchId);
            var branchPort = PhysicalHvac.AtEnd(duct, branchEnd, tol).Id;
            var farPort = PhysicalHvac.AtEnd(duct, farEnd, tol).Id;
            DuctFixture.Need(PhysicalHvac.Peers(PhysicalHvac.Resolve(doc, branchId, farPort)).Length == 1,
                "Fixture far end is unconnected.");
            var baseline = DuctFixture.Inventory(doc);
            bool rejected = false;
            try
            {
                RectangularTakeoffToRoundRiser.Capture(doc, branchId, farPort, riserId, symbolId, tol, angleTol);
            }
            catch (InvalidOperationException e) when (e.Message == "The selected branch port must be an open rectangular end.")
            {
                rejected = true;
            }
            DuctFixture.Need(rejected && DuctFixture.Inventory(doc).SequenceEqual(baseline), "Connected branch port was not rejected.");

            var plan = RectangularTakeoffToRoundRiser.Capture(doc, branchId, branchPort, riserId, symbolId, tol, angleTol);
            void CheckRollback()
            {
                plan.VerifyRollback();
                DuctFixture.Need(DuctFixture.Inventory(doc).SequenceEqual(baseline), "Rollback changed fixture inventory.");
            }
            var dry = CheckedModelEdit.Run(doc, "Dry run of rectangular takeoff", true, plan.Apply, plan.Verify, CheckRollback, null);

            bool forced = false;
            try
            {
                CheckedModelEdit.Run(doc, "Forced takeoff verification failure", false, plan.Apply, () =>
                {
                    plan.Verify();
                    throw new InvalidOperationException("forced takeoff verification failure");
                }, null, null);
            }
            catch (InvalidOperationException e) when (e.Message == "forced takeoff verification failure")
            {
                forced = true;
            }
            DuctFixture.Need(forced, "Forced failure was not reached after a native commit.");
            CheckRollback();

            var write = CheckedModelEdit.Run(doc, "Commit disposable rectangular takeoff", false, plan.Apply, plan.Verify, null, null);
            plan.Verify();
            var fit = (FamilyInstance)doc.GetElement(plan.FittingId);
            var peers = PhysicalHvac.Ports(doc.GetElement(riserId)).Where(p => p.ConnectorType == ConnectorType.Curve)
                .SelectMany(PhysicalHvac.Peers).Select(p => p.Owner.Id).ToArray();
            var added = DuctFixture.Inventory(doc).Except(baseline).ToArray();
            DuctFixture.Need(peers.Length == 2 && peers.Contains(priorFittingId) && peers.Contains(fit.Id)
                && PhysicalHvac.Ports(doc.GetElement(priorId)).SelectMany(PhysicalHvac.Peers).Any(p => p.Owner.Id == priorFittingId)
                && added.SequenceEqual(new[]{fit.Id.IntegerValue}) && !baseline.Except(DuctFixture.Inventory(doc)).Any(),
                "The existing takeoff or fixture inventory changed.");

            return new {status="NATIVE_OK",revit=app.Application.VersionNumber,build=app.Application.VersionBuild,
                dry_child=dry.Transaction.ToString(),dry_group=dry.Group.ToString(),write_group=write.Group.ToString(),
                branch_mm=new[]{250,180},riser_mm=400,existing_curve_link_preserved=true,far_end_preserved=true,
                connected_port_rejected=rejected,forced_failure_rolled_back=forced,added=added.Length,
                fitting=fit.Symbol.FamilyName,expected_type_selected=fit.GetTypeId()==symbolId,
                active_unchanged=DuctFixture.DocumentKey(app.ActiveUIDocument?.Document)==active};
        }
        finally
        {
            doc.Close(false);
        }
    }
}

public class McpDynamicScript
{
    public static object Run(UIApplication app)
    {
        return new { duct = DuctFixture.Run(app), accessory = AccessoryFixture.Run(app), takeoff = TakeoffFixture.Run(app) };
    }
}
