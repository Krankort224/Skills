import argparse
import hashlib
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
BLOCKS = (
    "assets/blocks/core/checked-model-edit.md",
    "assets/blocks/core/physical-hvac.md",
    "assets/blocks/mep/rectangular-elbow-run.md",
    "assets/blocks/mep/retarget-rectangular-accessory.md",
    "assets/blocks/mep/rectangular-takeoff-to-round-riser.md",
)
HARNESS = "tests/native-smoke.cs"
EVIDENCE = "evidence/revit-2022-mcp-smoke.json"
STRING_KEYS = (
    "DuctTemplate", "AccessoryProject", "FamilyName", "OldType", "NewType",
    "WidthParameter", "HeightParameter",
)
NUMBER_KEYS = ("WidthMm", "HeightMm")
IMPORTS = "\n".join((
    "using System;",
    "using System.Linq;",
    "using System.Collections.Generic;",
    "using Autodesk.Revit.DB;",
    "using Autodesk.Revit.DB.Mechanical;",
    "using Autodesk.Revit.UI;",
))


def read_sources():
    sources = {}
    for path in BLOCKS:
        contents = (ROOT / path).read_text(encoding="utf-8")
        matches = re.findall(r"^```csharp\n(.*?)^```\s*$", contents, re.MULTILINE | re.DOTALL)
        if len(matches) != 1:
            raise ValueError(f"{path} must have one C# block")
        sources[path] = matches[0].strip()
    sources[HARNESS] = (ROOT / HARNESS).read_text(encoding="utf-8").strip()
    return sources


def source_hashes(sources):
    return {path: hashlib.sha256(code.encode("utf-8")).hexdigest() for path, code in sources.items()}


def fixture_class(config):
    keys = (*STRING_KEYS, *NUMBER_KEYS)
    if set(config) != set(keys):
        raise ValueError("Config must contain exactly: " + ", ".join(keys))
    if any(not isinstance(config[key], str) or not config[key].strip() for key in STRING_KEYS):
        raise ValueError("The fixture names and paths must be nonempty strings")
    if any(type(config[key]) is not int or config[key] <= 0 for key in NUMBER_KEYS):
        raise ValueError("The section must use positive integer millimetres")
    if config["WidthMm"] == config["HeightMm"]:
        raise ValueError("The swapped-dimension check requires a non-square section")
    for key, extension in (("DuctTemplate", ".rte"), ("AccessoryProject", ".rvt")):
        path = Path(config[key])
        if not path.is_absolute() or path.suffix.lower() != extension or not path.is_file():
            raise ValueError(f"{key} must be an existing absolute {extension} path")
    declarations = [
        f'    public const {"string" if key in STRING_KEYS else "int"} {key} = '
        f'{json.dumps(config[key], ensure_ascii=False)};'
        for key in keys
    ]
    return "\n".join(("public static class McpSkillFixture", "{", *declarations, "}"))


def main():
    parser = argparse.ArgumentParser(description="Verify Revit MCP block hashes or compose a disposable native smoke test.")
    parser.add_argument("--hashes", action="store_true", help="Print SHA-256 digests of the extracted C# sources")
    parser.add_argument("--candidate", action="store_true", help="Compose changed sources for a new native run")
    parser.add_argument("--config", type=Path, help="Local fixture JSON")
    parser.add_argument("--output", type=Path, help="New C# output file")
    args = parser.parse_args()

    sources = read_sources()
    hashes = source_hashes(sources)
    if args.hashes:
        if args.config or args.output or args.candidate:
            parser.error("--hashes is separate from candidate and verified composition")
        print(json.dumps(hashes, indent=2))
        return
    if bool(args.config) != bool(args.output):
        parser.error("--config and --output are required together")

    if args.candidate and not args.config:
        parser.error("--candidate requires --config and --output")

    evidence = json.loads((ROOT / EVIDENCE).read_text(encoding="utf-8"))
    if not args.candidate and evidence["source_sha256"] != hashes:
        raise SystemExit("C# sources differ from the recorded native run")

    if args.config:
        config = json.loads(args.config.read_text(encoding="utf-8-sig"))
        source = "\n\n".join((IMPORTS, *(sources[path] for path in BLOCKS),
                            fixture_class(config), sources[HARNESS])) + "\n"
        with args.output.open("x", encoding="utf-8", newline="\n") as out:
            out.write(source)
        print(args.output)
    else:
        print(f"Verified {len(BLOCKS)} blocks and the smoke harness against the recorded hashes.")


if __name__ == "__main__":
    main()
