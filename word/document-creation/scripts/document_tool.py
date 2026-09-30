"""Command line entry points for the document-creation toolkit."""
import argparse
import json
from pathlib import Path
from docx import Document
from document_tools import apply_preset, load_preset, package_report, source_coverage


def main():
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command", required=True)
    for name in ("inspect", "validate"):
        p = sub.add_parser(name); p.add_argument("input", type=Path); p.add_argument("--out", type=Path)
        if name == "validate":
            p.add_argument("--expected-text", type=Path); p.add_argument("--exact-counts", action="store_true")
    p = sub.add_parser("new"); p.add_argument("--preset", required=True); p.add_argument("--out", type=Path, required=True)
    p = sub.add_parser("apply-preset"); p.add_argument("input", type=Path); p.add_argument("--preset", required=True)
    p.add_argument("--out", type=Path, required=True); p.add_argument("--restyle", action="store_true", required=True)
    args = parser.parse_args()
    if args.command in ("new", "apply-preset"):
        if args.command == "apply-preset" and args.input.resolve() == args.out.resolve():
            parser.error("Refusing same-path input overwrite")
        if args.out.exists(): parser.error("Output already exists; choose a new path")
        doc = Document(args.input) if args.command == "apply-preset" else Document()
        apply_preset(doc, load_preset(args.preset)); args.out.parent.mkdir(parents=True, exist_ok=True); doc.save(args.out)
        report = package_report(args.out)
    else:
        report = package_report(args.input)
        if args.command == "validate" and args.expected_text:
            coverage = source_coverage(args.input, args.expected_text.read_text(encoding="utf-8").splitlines())
            report["coverage"] = coverage
            if coverage["missing"]: report["errors"].append("Missing source blocks")
            if args.exact_counts and coverage["extra_occurrences"]: report["errors"].append("Unexpected source block repetitions")
    rendered = json.dumps(report, ensure_ascii=False, indent=2)
    if args.command in ("inspect", "validate") and args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True); args.out.write_text(rendered + "\n", encoding="utf-8")
    else: print(rendered)
    return 1 if report["errors"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
