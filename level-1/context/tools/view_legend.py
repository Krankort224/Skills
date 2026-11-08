"""Add a static visual key to trusted pinned native Graphify views.

Pure text transforms only: no extraction, graph mutation, loading, I/O or network.
Call before sealing a fresh trio; never patch a published sibling in place.
"""
from __future__ import annotations

import re
from decimal import Decimal
import xml.etree.ElementTree as ET

MAX_BYTES = 2 * 1024 * 1024
KEY_ID = "context-visual-key"


def html_key(text: str) -> str:
    """Insert the pinned renderer's size/style explanation in its sidebar."""
    if len(text.encode("utf-8")) > MAX_BYTES or f'id="{KEY_ID}"' in text:
        raise ValueError("Oversized/already annotated native HTML")
    anchor = '<div id="legend-wrap">'
    if text.count(anchor) != 1:
        raise ValueError("Unknown native HTML sidebar")
    key = '''<section id="context-visual-key" aria-label="Visual key" style="padding:10px 12px;border-bottom:1px solid var(--border);font-size:11px;line-height:1.4">
<strong>Visual key</strong>
<p>Size: stored degree; in a community view, member count. Color: community.</p>
<p>Stroke is category/selection styling, not link count, strength or calibrated confidence.</p>
<details><summary>Exact styles</summary>
<p>Node size: 10-40 relative to this view's maximum. Edges: width 2 for EXTRACTED, 1 otherwise; selecting adds 3. Solid: EXTRACTED; dashed: other categories. Opacity: 0.7 / 0.35.</p>
<p>Full-view arrows follow stored arcs. Community summaries are undirected; their arrows do not prove direction. Zoom/selection can change apparent size.</p>
</details></section>\n'''
    return text.replace(anchor, key + anchor)


def svg_key(text: str) -> str:
    """Append a footer without moving/clipping the native diagram above it."""
    if len(text.encode("utf-8")) > MAX_BYTES:
        raise ValueError("Oversized/already annotated native SVG")
    ns = "http://www.w3.org/2000/svg"
    ET.register_namespace("", ns)
    ET.register_namespace("xlink", "http://www.w3.org/1999/xlink")
    parser = ET.XMLParser(target=ET.TreeBuilder(insert_comments=True))
    root = ET.fromstring(text, parser=parser)
    height = re.fullmatch(r"([0-9.]+)pt", root.get("height", ""))
    box_tokens = root.get("viewBox", "").split()
    box = [float(v) for v in box_tokens]
    if any(node.get("id") == KEY_ID for node in root.iter()):
        raise ValueError("Already annotated native SVG")
    if root.tag != "{" + ns + "}svg" or not height or len(box) != 4 or box[:2] != [0, 0]:
        raise ValueError("Unknown native SVG geometry")
    height_value = Decimal(height[1])
    if height_value != Decimal(box_tokens[3]):
        raise ValueError("Unexpected native SVG units")
    footer = 56
    root.set("height", f"{height_value + footer}pt")
    root.set("viewBox", " ".join(box_tokens[:3]) + " " + str(height_value + footer))
    group = ET.SubElement(root, "{" + ns + "}g", {"id": KEY_ID})
    ET.SubElement(group, "{" + ns + "}rect", {"x": "0", "y": str(height_value), "width": box_tokens[2], "height": str(footer), "fill": "#1a1a2e"})
    lines = [
        "Visual key - color: community; node area: 300-1500, relative to stored degree.",
        "Edges: fixed 0.8 pt stroke; solid EXTRACTED / dashed other categories; opacity 0.6 / 0.3.",
        "Stroke is not link count, strength or calibrated confidence. No arrow or hyperedge encoding.",
    ]
    for index, line in enumerate(lines):
        label = ET.SubElement(group, "{" + ns + "}text", {"x": "12", "y": str(height_value + 15 + 14 * index), "font-family": "DejaVu Sans, sans-serif", "font-size": "9", "fill": "#e0e0e0"})
        label.text = line
    return ET.tostring(root, encoding="unicode", xml_declaration=True)
