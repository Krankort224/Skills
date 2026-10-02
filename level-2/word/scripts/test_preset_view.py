"""Focused checks for the read-only selective preset view."""
import hashlib
import re
import subprocess
import sys
import tempfile
from pathlib import Path

from document_tools import ROOT
from extract_preset import extract_preset
from preset_view import show_preset


def run():
    scripts = Path(__file__).resolve().parent
    technical = ROOT / "assets" / "presets" / "technical.md"
    before = hashlib.sha256(technical.read_bytes()).hexdigest()

    default = show_preset("technical")
    assert default.startswith("# Technical style preset\n\nStatus: ready\n")
    assert "## Purpose" in default and "## Provenance" in default
    assert "## Parameters" not in default and "| page.width_mm |" not in default

    # Make a real captured draft so the late diagnostics sections are exercised.
    with tempfile.TemporaryDirectory() as tmp:
        tmp_path = Path(tmp)
        source_doc = tmp_path / "source.docx"
        from docx import Document
        Document().save(source_doc)
        draft, _ = extract_preset(source_doc, "technical", 0)
        draft_path = tmp_path / "draft.md"
        draft_path.write_text(draft, encoding="utf-8")
        draft_view = show_preset(draft_path)
        for heading in ("Capture observations", "Unobserved defaults",
                        "Direct formatting observations", "Limitations"):
            assert "## " + heading in draft_view
        assert "Status: draft" in draft_view and "## Parameters" not in draft_view

        later_section = tmp_path / "later.md"
        later_section.write_text(technical.read_text(encoding="utf-8") +
                                 "\n## Later narrative\n\nThis remains visible after Parameters.\n",
                                 encoding="utf-8")
        assert "## Later narrative" in show_preset(later_section)

        focused = show_preset(draft_path, sections=["Unobserved defaults"])
        assert "## Unobserved defaults" in focused
        assert "## Capture observations" not in focused
        assert "## Limitations" not in focused

        selected = show_preset("technical", parameters=["palette.ink", "page.width_mm"])
        assert "## Purpose" not in selected
        assert "| Path | Value | Type | Unit |" in selected
        assert "| palette.ink | 000000 | string | - |" in selected
        assert "| page.width_mm | 210 | number | mm |" in selected
        assert "| palette.accent |" not in selected

        mixed = show_preset("technical", sections=["Purpose"], parameters=["palette.ink"])
        assert "## Purpose" in mixed and "| palette.ink | 000000 | string | - |" in mixed
        assert "## Parameters" in mixed

        # Headings that look real inside fences must not split prose or select.
        fenced = tmp_path / "fenced.md"
        fenced.write_text(draft.replace(
            "## Purpose\n\n",
            "## Purpose\n\n```md\n## Fake\n```\n\n"), encoding="utf-8")
        fenced_view = show_preset(fenced, sections=["Purpose"])
        assert "## Fake" in fenced_view and "## Capture observations" not in fenced_view

        title_example = tmp_path / "title-example.md"
        title_example.write_text(draft.replace("## Purpose\n\n",
            "## Purpose\n\n```md\n# Sample title\n```\n\n"), encoding="utf-8")
        assert "# Sample title" in show_preset(title_example)

        aligned = tmp_path / "aligned.md"
        aligned.write_text(draft.replace("| --- | --- | --- | --- |",
            "| :--- | ---: | :---: | --- |"), encoding="utf-8")
        assert "| page.width_mm |" in show_preset(aligned, parameters=["page.width_mm"])

        for args in (("--section", "missing"), ("--section", "Purpose", "--section", "Purpose"),
                     ("--parameter", "Palette.ink"), ("--parameter", "missing.path")):
            cli = subprocess.run([sys.executable, str(scripts / "document_tool.py"),
                                  "show-preset", str(draft_path), *args],
                                 capture_output=True, text=True)
            assert cli.returncode != 0 and not cli.stdout

        broken = tmp_path / "broken.md"
        broken.write_text(re.sub(r"\| page\.width_mm \| [^|]+ \| number \| mm \|",
                                 "| page.width_mm | no | number | mm |", draft), encoding="utf-8")
        cli = subprocess.run([sys.executable, str(scripts / "document_tool.py"),
                              "show-preset", str(broken)], capture_output=True, text=True)
        assert cli.returncode != 0 and not cli.stdout

        empty_table = tmp_path / "empty-table.md"
        empty_table.write_text("# Empty\n\nStatus: ready\n\n## Parameters\n\n",
                               encoding="utf-8")
        cli = subprocess.run([sys.executable, str(scripts / "document_tool.py"),
                              "show-preset", str(empty_table)], capture_output=True, text=True)
        assert cli.returncode != 0 and not cli.stdout

        # A duplicate matching heading is ambiguous and must fail explicitly.
        duplicate = tmp_path / "duplicate.md"
        duplicate.write_text(draft.replace("## Purpose\n", "## Purpose\n\n## Purpose\n", 1),
                             encoding="utf-8")
        try:
            show_preset(duplicate, sections=["Purpose"])
        except ValueError as exc:
            assert "Ambiguous" in str(exc)
        else:
            raise AssertionError("Duplicate section heading was accepted")

    assert hashlib.sha256(technical.read_bytes()).hexdigest() == before
    print("Passed 22 preset-view behavior checks")


if __name__ == "__main__":
    run()
