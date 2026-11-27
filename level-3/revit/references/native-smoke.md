# Native C# smoke checks in Revit

`scripts/compose_smoke.py` verifies the sources against the hashes in the evidence record. Given a local configuration, it builds one C# script for `revit_send_code_to_revit`.

The sources and [evidence record](../evidence/revit-2022-mcp-smoke.json) came from a local `revit-mcp` installation on 12 November 2026. The record covers a prior run with Revit 2022 build 22.1.70.9 and rvt-mcp 1.2.1. Matching hashes confirm that the tested source was preserved. Runtime evidence comes from that prior run. Project owners retain their working logs separately.

The original field cases `evidence/kod-separate-calls-field-case.md` and `evidence/rectangular-takeoff-field-case.md` are in the local archive of the original skill. Their reusable methods are documented under [invocation boundaries](mcp-operations.md#invocation-boundaries) and [edit boundaries](geometry-and-connectors.md#edit-boundaries). The field cases establish the source of those methods. The separate evidence record above covers the generalized C# blocks. The local adapter records the archive location.

```powershell
python scripts/compose_smoke.py
python scripts/compose_smoke.py --config C:/temp/fixture.json --output C:/temp/revit-mcp-smoke.cs
```

The configuration specifies the absolute path to an MEP template with a rectangular elbow routing rule and the absolute path to a separate test RVT with two loaded types of the same damper. The RVT needs a level, a rectangular duct type and a supply air system type. The example uses illustrative names. The damper parameters must drive the sizes of both connectors.

```json
{
  "DuctTemplate": "C:/temp/mechanical-test.rte",
  "AccessoryProject": "C:/temp/accessory-fixture.rvt",
  "FamilyName": "Test Rectangular Damper",
  "OldType": "500-300",
  "NewType": "800-300",
  "WidthParameter": "B",
  "HeightParameter": "H",
  "WidthMm": 800,
  "HeightMm": 300
}
```

Run the script only with dedicated fixtures. It creates a document from the template and opens the test RVT in the background. It closes both documents without saving. For the damper, it verifies the two original connections and the cross-section. Swapping B and H must cause rejection before any write. For the duct run, it checks two cross-sections, independent readback after commit, rollback following a verification failure and cancellation.

Record the Revit version, the MCP version when applicable, fixture details, command result and block hashes. After changing the code, run it in Revit again and record the new evidence. Use `--hashes` to print the current hashes.

## Add a native smoke scenario

For the first run of a new source revision, build the script with `--candidate`, `--config` and `--output`.

```powershell
python scripts/compose_smoke.py --candidate --config C:/temp/fixture.json --output C:/temp/revit-mcp-candidate.cs
```

For the takeoff test, the same MEP template must contain round and rectangular duct types with Tap as the preferred junction type. The first rule in the selected rectangular duct type's Junctions group must specify a rectangular takeoff suitable for a round riser. The test creates a separate document from the template, adds the original takeoff and checks that it is preserved. It also checks the branch's far connection, selection of a different type from the same family, rejection of an occupied connector, rollback after a native commit and connectivity through the new takeoff after the write.

Record the result of the exact script submitted to Revit. After updating the evidence, verify that the standard build succeeds without `--candidate`.
