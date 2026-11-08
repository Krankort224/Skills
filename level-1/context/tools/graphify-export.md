# Graphify: export and namespace interfaces

View selection, interpretation and verification: [export a graph view](../operations/graphify/export.md). Package/runtime: [technical profile](graphify.md). Loaders and `validator` setup: [native read interfaces](graphify-read.md).

## Contents

- [HTML and report](#html-and-report)
- [Visual encoding and annotation](#visual-encoding-and-annotation)
- [Optional exporters](#optional-exporters)
- [Bind cross-repository inputs to commits](#bind-cross-repository-inputs-to-commits)
- [Compose a scoped namespace view](#compose-a-scoped-namespace-view)
- [Source ledger](#source-ledger)

The mandatory trio remains `graph.json`, `graph.html`, `GRAPH_REPORT.md`. Optional exports use fresh dedicated output outside source and that reserved trio directory. They derive from a checked generation and do not supply new currentness evidence. Exporters may update several outputs independently; none is a multi-file publication transaction. `to_graphml` also uses a fixed sibling `.tmp`, requiring one writer per destination.

## HTML and report

The HTML embeds nodes/edges/counts that must correspond to exact JSON; the report binds input identity/coverage. JSON retains detailed evidence, rationale, origin and confidence that the HTML node panel omits. Report hubs/communities/surprising connections are bounded navigation summaries and preserve unknown subscription usage.

The pinned renderer loads vis-network 9.1.6 from unpkg with SRI. JavaScript, network, origin/CORS and browser policy affect rendering; an empty canvas with counts is not a working graph. The browser can save theme preference in localStorage, separate from project-file effects. No browser-rendering claim follows from an HTML file, XML parse or recipe success.

The native default limit is 5000 nodes. Without an override, oversized input raises. With an explicit lower `node_limit`, HTML can aggregate into an UNDIRECTED community summary: internal arcs vanish and opposing/parallel cross-community arcs merge into a count, even if an arrow is drawn. Full mixed staging refuses oversized graphs; an aggregate cannot replace the full-evidence trio. Aggregation with fewer than two communities can return false and omit HTML. Its recursive export can read a sibling learning overlay even when the outer caller passed `{}`; use a separate fresh destination. The recorded small explicit-limit control does not establish large-corpus/browser performance.

## Visual encoding and annotation

[view_legend.py](view_legend.py) adds a static HTML sidebar key before generation markers/sibling hashes. Native node size is normalized stored degree (in+out for directed graphs), or member count in an aggregate; color is community. Edge base width is category styling (2 for EXTRACTED, 1 otherwise), and vis-network selection adds 3. Solid/dashed style and opacity distinguish categories; zoom/selection change apparent size. These encodings are not relationship counts, measured strengths or calibrated probabilities. See the pinned export source and [vis-network edge semantics](https://visjs.github.io/vis-network/docs/network/edges.html).

`view_key.svg_key(native_svg_text)` adds a footer after native SVG export into fresh output. It describes relative node area 300–1500 by stored degree, community color, fixed 0.8 pt edge stroke, solid/dashed categories and 0.6/0.3 opacity. Native SVG has no direction arrows/relation labels or hyperedge encoding. The annotation preserves native data/geometry above the added footer; it is not a renderer. Import the same helper with `importlib` as in the build recipe. Existing sealed siblings cannot be patched without fresh export/sealing.

## Optional exporters

Use `G` loaded from an already validated graph dict, group integer `community` values, and take labels from that exact generation's `community_interpretation`. Output/source fingerprints support verification that export left inputs unchanged.

| Format / call | Technical contract and losses |
|---|---|
| `to_graphml(G, communities, path)` | A directed native graph plus `nx.read_graphml(path)` round trip preserves tested IDs and directed/parallel/opposing arcs. `_` attributes, including origin and fallback direction markers, are removed. Nested evidence/hyperedges become JSON strings, `None` becomes empty text, XML control characters are stripped. Not a lossless portable-state import. |
| `to_obsidian(G, communities, directory, community_labels=labels)` | Selected per-node fields and community navigation, not all evidence. Foreign filename collisions can be skipped with partial count/warning. Owned notes/local edits are overwritten/pruned; absent manifest can allow tagged-note adoption/pruning. Use a dedicated generated child/vault. |
| `to_wiki(G, communities, directory, community_labels=labels, god_nodes_data=god_nodes(G, top_n=5))` | Owns ALL top-level Markdown at destination and deletes unrelated `.md` on refresh. Produces bounded community/source/hub selections, not whole-document summaries. Requires a dedicated generated directory. |
| `to_svg(G, communities, path, community_labels=labels)` | Requires plotting extras. No direction arrows/relation labels; parallel/opposing arcs overlap; no hyperedges. Short/small output can clip labels or overlap legends; actual readability requires visual inspection. |

SVG uses a separate task-owned plotting environment. The exercised Linux resolution adds matplotlib 3.11.2, Pillow 13.0.0 and resolved plotting dependencies while retaining NumPy 2.5.4; the upstream full lock's older NumPy is not a substitute. Record the exact resolution, and set external `MPLCONFIGDIR` before importing matplotlib. The base-only SVG call should refuse missing matplotlib without output. Parsing alone does not establish readability.

## Bind cross-repository inputs to commits

Inputs have stable explicit repository tags excluding `::`, distinct from checkout basenames, and reviewed immutable artifact/source commits, exact graph hashes, input/generation identities and pinned Graphify revision. Currentness is separately checked at each source root. A cross-repository output is a separate view, not a per-repository maintenance state or globally writable graph.

Native `prefix_graph_for_global` with NetworkX `MultiDiGraph` preserves directed/parallel arcs. CLI `merge-graphs` instead converts to undirected simple graphs and adds shared-type/member-call inferences, collapsing opposing/parallel evidence; it is a lossy overview, not an exact merged snapshot.

First load the `validator` module as in [the read recipe](graphify-read.md#validated-graph-recipe). `cross_records` contains `tag`, canonical local `repository`, full `artifact_commit`, and `checked` returned by `validate_trio` for a materialized trio. This block binds it to real Git objects without checkout/fetch/index/ref changes. The tested Git 2.52.0 [no-lazy-fetch option](https://git-scm.com/docs/git/2.52.0#Documentation/git.txt---no-lazy-fetch) prevents missing promisor objects triggering retrieval; optional locks are disabled. Other Git versions must enforce the same boundary or refuse. The adopted artifact path is the maintenance publication contract.

```python
# context-bind-cross-inputs
import hashlib
import json
import os
from pathlib import Path
import subprocess

assert not any(os.environ.get(k) for k in ("GIT_DIR", "GIT_WORK_TREE", "GIT_INDEX_FILE", "GIT_COMMON_DIR", "GIT_OBJECT_DIRECTORY", "GIT_ALTERNATE_OBJECT_DIRECTORIES", "GIT_REPLACE_REF_BASE"))
git_env = dict(os.environ, GIT_NO_REPLACE_OBJECTS="1", GIT_OPTIONAL_LOCKS="0")
def object_read(repository, *args):
    return subprocess.run(["git", "--no-lazy-fetch", "--no-optional-locks", "-C", str(repository), *args], capture_output=True, env=git_env, check=True, timeout=30).stdout
def commit_id(value):
    return isinstance(value, str) and len(value) == 40 and all(ch in "0123456789abcdef" for ch in value)
checked_inputs = []
for item in cross_records:
    checked = item["checked"]
    repository = Path(item["repository"]).resolve(strict=True)
    artifact_commit = item["artifact_commit"]
    source_commit = checked["graph"]["graph"]["context"].get("source_commit")
    assert commit_id(artifact_commit) and commit_id(source_commit), "Missing/invalid version provenance"
    assert Path(object_read(repository, "rev-parse", "--show-toplevel").decode("utf-8").strip()).resolve(strict=True) == repository
    for commit in (artifact_commit, source_commit):
        assert object_read(repository, "cat-file", "-t", commit).strip() == b"commit"
    object_read(repository, "merge-base", "--is-ancestor", source_commit, artifact_commit)
    for name in ("graph.json", "graph.html", "GRAPH_REPORT.md"):
        assert object_read(repository, "show", artifact_commit + ":skills/context/references/graphify/" + name) == checked["blobs"][name], "Artifact commit/view mismatch"
    assert json.loads(checked["blobs"]["graph.json"]) == checked["graph"], "Checked graph/buffer mismatch"
    for group in ("sources", "configuration"):
        for path, digest in checked["snapshot"][group].items():
            assert validator._relative(path) == path
            assert hashlib.sha256(object_read(repository, "show", source_commit + ":" + path)).hexdigest() == digest, "Source commit/input mismatch"
    checked_inputs.append((item["tag"], artifact_commit, checked))
```

## Compose a scoped namespace view

`checked_inputs` must be the `(stable_tag, verified_artifact_commit, checked_view)` records produced above; manually pairing a commit and a JSON view does not establish provenance.

```python
# context-cross-repository-view
import copy
import networkx as nx
from graphify.build import prefix_graph_for_global
from graphify.export import attach_hyperedges
from graphify.paths import load_node_link_graph

assert 1 < len(checked_inputs) <= 4
assert len({tag for tag, _, _ in checked_inputs}) == len(checked_inputs)
assert all(isinstance(tag, str) and tag and "::" not in tag for tag, _, _ in checked_inputs)
merged = nx.MultiDiGraph()
hyperedges, inputs, external_attributes = [], [], {}
offset = 0
for tag, artifact_commit, checked in checked_inputs:
    original = load_node_link_graph(checked["graph"])
    assert original.is_directed() and not any(d.get("repo") for _, d in original.nodes(data=True))
    G = nx.MultiDiGraph(original)
    assert not any(G.nodes[u].get("external") and G.nodes[v].get("external") for u, v in G.edges()), "External-only arcs require separate provenance; unsupported in this view"
    for node, attrs in G.nodes(data=True):
        if attrs.get("external"):
            assert node not in external_attributes or external_attributes[node] == dict(attrs), "Conflicting external identity"
            external_attributes[node] = copy.deepcopy(dict(attrs))
    H = prefix_graph_for_global(G, tag, community_offset=offset)
    assert len(H) == len(G), "Local prefix/external ID collision"
    assert all(merged.nodes[n].get("external") and H.nodes[n].get("external") for n in set(merged) & set(H))
    assert not (set(merged.edges(keys=True)) & set(H.edges(keys=True))), "Shared external edge-key collision"
    hyperedges.extend(copy.deepcopy(H.graph.get("hyperedges", [])))
    offset = max([offset] + [d["community"] + 1 for _, d in H.nodes(data=True) if type(d.get("community")) is int])
    merged = nx.compose(merged, H)
    assert len(merged) <= 5000 and merged.number_of_edges() <= 10000
    c = checked["graph"]["graph"]["context"]
    assert isinstance(artifact_commit, str) and len(artifact_commit) == 40 and all(ch in "0123456789abcdef" for ch in artifact_commit)
    inputs.append({"repo": tag, "artifact_commit": artifact_commit, "source_commit": c["source_commit"], "graph_sha256": checked["digests"]["graph.json"], "input_identity": checked["input_identity"], "generation_identity": checked["generation_identity"], "graphify_revision": c["graphify_revision"]})
merged.graph.clear()  # The final input's context cannot identify the whole view.
attach_hyperedges(merged, hyperedges)
merged.graph["cross_repository_view"] = {"inputs": inputs, "limits": ["separate versioned navigation view; no inferred cross-repository links; shared external IDs do not prove compatible versions"]}
```

External-only arcs are refused because neither endpoint carries a repository owner. The view preserves inputs separately unless another explicit provenance-preserving method is selected; it does not silently drop those arcs.

Serialize `nx.node_link_data(merged, edges="links")` to NEW separate output and reload with `load_node_link_graph`. Verify node IDs, complete directed arc rows/keys, hyperedge membership and input manifests, then recheck input fingerprints. A combined view cannot be used as one repository's maintenance trio.

Native prefixing rewrites local IDs, `_src`/`_tgt`, hyperedge IDs/members and community offsets while preserving labels, repo-relative `source_file`, `repo` and `local_id`. Arbitrary nested evidence/references are not recursively namespaced; source resolution still needs the input repo+commit. Common external IDs are navigation joins, not proof of matching versions/interoperability. Same-labeled local entities are not joined. Conflicting external attributes, collisions or insufficient provenance are refused; no new semantic/runtime relationship is inferred.

## Source ledger

- [JSON/other exports](https://github.com/Graphify-Labs/graphify/blob/16218bfc80d4ca2799734d045039f7ed1a5fa9fb/graphify/export.py): `to_json` 303, original-link preservation 414, graph metadata 506, Obsidian 792, GraphML 1333, SVG 1413; [HTML](https://github.com/Graphify-Labs/graphify/blob/16218bfc80d4ca2799734d045039f7ed1a5fa9fb/graphify/exporters/html.py): `to_html` 508, scale 538, escaping 715 and CDN 733; [report](https://github.com/Graphify-Labs/graphify/blob/16218bfc80d4ca2799734d045039f7ed1a5fa9fb/graphify/report.py): `generate` 111; `wiki.py` 306.
