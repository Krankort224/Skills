"""Read-only selective views of the authoritative Markdown preset files."""
from __future__ import annotations

import re
from pathlib import Path

from document_tools import load_preset, resolve_preset_path
from preset_markdown import cells


_SECTION = re.compile(r"^## (.+?)\s*$")
_TITLE = re.compile(r"^# (.+?)\s*$")
_STATUS = re.compile(r"^Status: (ready|draft)$")


def _outside_fences(lines):
    """Yield source offsets and lines outside fenced code blocks."""
    fence_char = None
    fence_size = 0
    for index, line in enumerate(lines):
        fence = re.match(r"^\s{0,3}(`{3,}|~{3,})", line)
        if fence:
            marker = fence.group(1)
            if fence_char is None:
                fence_char, fence_size = marker[0], len(marker)
            elif marker[0] == fence_char and len(marker) >= fence_size:
                fence_char, fence_size = None, 0
            continue
        if fence_char is None:
            yield index, line


def _headings(lines):
    """Return level-two headings outside fenced code blocks, with offsets."""
    return [(index, heading.group(1)) for index, line in _outside_fences(lines)
            if (heading := _SECTION.match(line))]


def _parameter_block(lines, headings):
    matches = [(offset, title) for offset, title in headings if title == "Parameters"]
    if len(matches) != 1:
        raise ValueError("Preset requires exactly one ## Parameters section")
    start = matches[0][0]
    end = next((offset for offset, _ in headings if offset > start), len(lines))
    return start, end


def _selected_sections(lines, headings, requested):
    by_name = {}
    for offset, title in headings:
        if title != "Parameters":
            by_name.setdefault(title, []).append(offset)
    chunks = []
    seen = set()
    for title in requested:
        if title in seen:
            raise ValueError("Section requested more than once: " + title)
        seen.add(title)
        offsets = by_name.get(title, [])
        if not offsets:
            raise ValueError("Unknown narrative section: " + title)
        if len(offsets) != 1:
            raise ValueError("Ambiguous duplicate narrative section: " + title)
        start = offsets[0]
        end = next((offset for offset, _ in headings if offset > start), len(lines))
        chunks.append("\n".join(lines[start:end]).strip())
    return chunks


def _selected_parameters(lines, start, end, requested):
    if len(set(requested)) != len(requested):
        raise ValueError("Parameter path requested more than once")
    wanted = set(requested)
    rows = {}
    table = [line.strip() for line in lines[start + 1:end] if line.strip()]
    header, separator = table[:2]  # Full loader validation established these rows.
    for stripped in table[2:]:
        parsed = cells(stripped)
        if len(parsed) == 4 and parsed[0] in wanted:
            rows[parsed[0]] = stripped
    missing = [path for path in requested if path not in rows]
    if missing:
        raise ValueError("Unknown parameter path: " + ", ".join(missing))
    result = ["## Parameters", "", header, separator]
    result.extend(rows[path] for path in requested)
    return "\n".join(result)


def show_preset(name_or_path, sections=None, parameters=None):
    """Render a selective read-only view after fully validating the preset."""
    sections = list(sections or [])
    parameters = list(parameters or [])
    path = resolve_preset_path(name_or_path)
    # Full canonical validation happens before any selective output is assembled.
    load_preset(path, allow_draft=True)
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    titles = [match.group(1) for _, line in _outside_fences(lines)
              if (match := _TITLE.match(line))]
    statuses = [match.group(1) for line in lines if (match := _STATUS.match(line))]
    if len(titles) != 1:
        raise ValueError("Preset requires exactly one title")
    if len(statuses) != 1:
        raise ValueError("Preset requires exactly one Status: ready or Status: draft")
    headings = _headings(lines)
    params_start, params_end = _parameter_block(lines, headings)

    output = ["# " + titles[0], "", "Status: " + statuses[0]]
    if sections:
        output.extend(["", "\n\n".join(_selected_sections(lines, headings, sections))])
    elif not parameters:
        # Keep the source prose intact, dropping only the title/status already
        # rendered above and the canonical parameter table block.
        retained = [
            line for index, line in enumerate(lines)
            if index not in (next(i for i, row in _outside_fences(lines) if _TITLE.match(row)),
                             next(i for i, row in enumerate(lines) if _STATUS.match(row)))
            and not params_start <= index < params_end
        ]
        prose = "\n".join(retained).strip()
        if prose:
            output.extend(["", prose])
    if parameters:
        output.extend(["", _selected_parameters(lines, params_start, params_end, parameters)])
    return "\n".join(output).rstrip() + "\n"
