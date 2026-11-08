"""Check static view-key fidelity against pinned native HTML/SVG exporters."""
from __future__ import annotations
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import socket
import tempfile
import xml.etree.ElementTree as ET

TOOLS = Path(__file__).resolve().parent


def main():
    assert __debug__
    attempts = []
    def forbidden(*args, **kwargs):
        attempts.append("network")
        raise RuntimeError("No network in view-key probe")
    socket.socket.connect = socket.create_connection = forbidden
    spec = importlib.util.spec_from_file_location("context_view_key", TOOLS / "view_legend.py")
    key = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(key)
    with tempfile.TemporaryDirectory(prefix="context-view-key-") as temporary:
        out = Path(temporary)
        os.environ["MPLCONFIGDIR"] = str(out / "plot-cache")
        from graphify.exporters.html import to_html
        import networkx as nx
        g = nx.DiGraph()
        for node in ("a", "b", "c"):
            g.add_node(node, label=key.KEY_ID if node == "c" else node, source_file="source.py", file_type="code")
        g.add_edge("a", "b", relation="calls", confidence="EXTRACTED", confidence_score=1.0, weight=37)
        g.add_edge("b", "c", relation="explains", confidence="INFERRED", confidence_score=.95, weight=1)
        original = nx.node_link_data(g, edges="links")
        assert to_html(g, {0: list(g)}, str(out / "native.html"), community_labels={0: "Fixture"}, learning_overlay={})
        native = (out / "native.html").read_text()
        decorated = key.html_key(native)
        def embedded(text, name):
            return json.JSONDecoder().raw_decode(text.split("const " + name + " = ", 1)[1])[0]
        assert all(embedded(native, name) == embedded(decorated, name) for name in ("RAW_NODES", "RAW_EDGES", "LEGEND"))
        assert decorated.count('id="context-visual-key"') == 1
        assert 'not link count, strength or calibrated confidence' in decorated
        assert 'selectionWidth: 3' in decorated
        rows = embedded(decorated, 'RAW_EDGES')
        assert [e['width'] for e in rows] == [2, 1] and [e['dashes'] for e in rows] == [False, True]
        # The unrelated weight37 does not make the first edge 37 times thicker.
        assert nx.node_link_data(g, edges='links') == original
        for bad in (decorated, '<html>unknown</html>', 'x' * (key.MAX_BYTES + 1)):
            try: key.html_key(bad)
            except ValueError: pass
            else: raise AssertionError('Unsupported HTML accepted')
        svg = 'not run: optional plotting environment absent'
        if importlib.util.find_spec('matplotlib'):
            from graphify.export import to_svg
            to_svg(g, {0: list(g)}, str(out / 'native.svg'), community_labels={0: 'Fixture'}, figsize=(20.123456789,14.123456789))
            text = (out / 'native.svg').read_text()
            marked = key.svg_key(text)
            parser = lambda: ET.XMLParser(target=ET.TreeBuilder(insert_comments=True))
            before, after = ET.fromstring(text, parser=parser()), ET.fromstring(marked, parser=parser())
            def tree(node):
                return (node.tag, dict(node.attrib), node.text, node.tail, [tree(child) for child in node])
            assert [tree(child) for child in before] == [tree(child) for child in list(after)[:-1]]
            assert before.get('width') == after.get('width')
            assert before.get('viewBox').split()[:3] == after.get('viewBox').split()[:3]
            assert float(after.get('height')[:-2]) == float(before.get('height')[:-2]) + 56
            assert after[-1].get('id') == key.KEY_ID
            assert 'fixed 0.8 pt stroke' in ''.join(after[-1].itertext())
            for bad in (marked, '<svg/>', text.replace('pt"', 'px"')):
                try: key.svg_key(bad)
                except ValueError: pass
                else: raise AssertionError('Unsupported SVG accepted')
            svg = 'PASS: original child geometry/metadata preserved; footer height added'
        assert not attempts
        print(json.dumps({'status':'PASS','html_graph_data_unchanged':True,'native_styles':{'widths':[2,1],'selection_increment':3},'svg':svg,'network_attempts':len(attempts)}))


if __name__ == '__main__':
    main()
