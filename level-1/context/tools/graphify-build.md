# Graphify: build interfaces and recipes

Agent procedure: [build a graph](../operations/graphify/build.md). Runtime and `context-profile-check`: [technical profile](graphify.md). These recipes require that exact interpreter/package profile and direct native APIs; no replacement parser or provider backend is involved.

## Contents

- [Native extraction behavior](#native-extraction-behavior)
- [Build and inspect structural evidence](#build-and-inspect-structural-evidence)
- [Bounded structural-stage query](#bounded-structural-stage-query)
- [Semantic protocol](#semantic-protocol)
- [Assemble, interpret and verify a fresh mixed trio](#assemble-interpret-and-verify-a-fresh-mixed-trio)
- [Source ledger](#source-ledger)

## Native extraction behavior

`detect.detect` supplies classified inventory, `walk_errors`, `unclassified` and `skipped_sensitive`. Native ignore/noise/sensitive rules apply. Fixed directory exclusions with a trailing slash prune before nested local rules; ignored/noise subtrees and directory symlinks may be pruned without a complete descendant listing. The structural recipe adds case-insensitive Office/PDF/Google-shortcut exclusions before detection can convert/export inputs and rejects nested rules that re-include such files. Declared unselected submodules are excluded without initialization/fetch; ignore-metacharacter spellings are refused by this bounded recipe.

`extract(files, root=root, cache_root=cache, parallel=False)` selects verified `.py` and `.md` suffixes from every native bucket, including Markdown classified as paper. It records `extracted_sources`; native parallel extraction requires an importable main module and can fall back from stdin/`-c`/REPL on spawn hosts. `graphify extract --code-only` drops documentary inputs. Headless document extraction can detect ambient API keys and invoke provider pipelines; it does not run on the current chat subscription.

The Markdown extractor represents pages, ATX headings/nesting, inline/reference destinations and wikilinks, excluding fenced blocks. It strips link fragments/queries, skips in-page anchors and ordinary code/asset hyperlinks, and may leave missing targets dangling; unused reference definitions can still be scanned. Thus it does not validate anchors or all Markdown syntax. Path-qualified code spans resolve as EXTRACTED; uniquely resolved bare mentions as INFERRED 0.95; ambiguous names are omitted.

Raw edges and built edges need not have equal counts: missing targets can be omitted and same-endpoint evidence folds into `also_seen`. Native code/cache/ID/merge functions remain the owners of parsing and graph representation. `build_from_json(..., directed=True, dedup=False)` and explicit `_origin` preserve directed/tier meaning; `build_merge` returns without writing and callers copy mutable dictionaries when reusing them. Native AST cache identity includes schema/grammars; semantic cache adds prompt identity, but legacy entries and zero-node/zero-hyperedge misses do not establish complete current coverage.

## Build and inspect structural evidence

Inputs: `CONTEXT_ROOT` is a quiescent source tree; `CONTEXT_TOOLS` is this reviewed directory; `CONTEXT_STAGE` is a NEW external staging directory. Set `GRAPHIFY_OUT` before native imports and retain the no-provider environment from [preparation](graphify.md#prepare-and-verify-the-structural-environment). Adapt exclusions to the actual installed graph/output, cache/staging and third-party paths. The shared `exclusion_policy` expands raw or already-effective rules identically, appending the required conversion/submodule exclusions and reserved derived paths without sorting user rules; other omitted paths are not automatically excluded.

Example exclusion input:

```sh
export CONTEXT_EXCLUDES='["skills/context/references/graphify/","graphify-out/","generated/","vendor/","third_party/","**/*.docx","**/*.xlsx","**/*.xlsm","**/*.pdf","**/*.gdoc","**/*.gsheet","**/*.gslides"]'
```

The block performs native inventory, structural extraction and explicit JSON/HTML/report staging. It has no semantic/model step. It rechecks selected bytes, inventory and in-scope native configuration before/after extraction; these checks are not an atomic filesystem snapshot or protection against change-and-revert races.

```python
# context-structural-build
if not __debug__:
    raise RuntimeError("Run without Python optimization: validation must remain enabled")
import contextlib
import copy
import hashlib
import importlib.metadata as metadata
import importlib.util
import io
import json
import os
from pathlib import Path
import shutil
import subprocess

root = Path(os.environ["CONTEXT_ROOT"]).resolve(strict=True)
work = Path(os.environ["CONTEXT_STAGE"]).resolve()
cache = work / "native-cache"
stage = work / "artifacts"
assert root.is_dir() and not work.is_relative_to(root) and not root.is_relative_to(work), "Stage/cache must be outside source"
assert not cache.exists() and not stage.exists(), "Use fresh staging/cache; do not overwrite or reuse a prior build here"
assert Path(os.environ["GRAPHIFY_OUT"]).resolve() == cache, "Set GRAPHIFY_OUT before imports"
assert os.environ.get("GRAPHIFY_BACKEND") == "none", "No model backend is permitted"
assert metadata.version("graphifyy") == "0.9.103"
if shutil.which("git"):
    vcs_root = subprocess.run(["git", "-C", str(root), "rev-parse", "--show-toplevel"], capture_output=True, text=True, timeout=30)
    assert vcs_root.returncode != 0 or Path(vcs_root.stdout.strip()).resolve() == root, "Select the canonical repository root; ancestor ignore rules need separate review"
# Share raw/effective policy expansion with refresh snapshots before detection.
module = Path(os.environ["CONTEXT_TOOLS"]) / "validate_context_fragments.py"
spec = importlib.util.spec_from_file_location("context_structural_policy", module)
validator = importlib.util.module_from_spec(spec)
spec.loader.exec_module(validator)
excludes = validator.exclusion_policy(root, json.loads(os.environ["CONTEXT_EXCLUDES"]))
from graphify.detect import detect, ignored_predicate, _is_noise_dir
from graphify.extract import extract, _get_extractor
from graphify.cache import load_cached
from graphify.rcfile import cache_salt, load_graphifyrc
from graphify.build import build_from_json
from graphify.cluster import cluster, label_communities_by_hub, score_all
from graphify.analyze import god_nodes, surprising_connections
from graphify.diagnostics import diagnose_extraction
from graphify.export import to_json
from graphify.exporters.html import to_html
from graphify.report import generate
from graphify.paths import load_node_link_graph, write_text_atomic
from graphify.validate import validate_extraction

def scan():
    result = detect(root, follow_symlinks=False, google_workspace=False, extra_excludes=excludes, cache_root=cache, gitignore=False)
    assert not result["walk_errors"], "Incomplete filesystem walk"
    return result

def config_identity():
    # Hash only configuration native detection/extraction can consume in this scope.
    ignored = ignored_predicate(root, extra_excludes=excludes, gitignore=False)
    configs = {}
    def walk_failure(error):
        raise error
    for directory, dirs, names in os.walk(root, followlinks=False, onerror=walk_failure):
        directory = Path(directory)
        dirs[:] = [name for name in dirs if not (directory / name).is_symlink() and not _is_noise_dir(name, directory) and not ignored(directory / name)]
        for name in names:
            path = directory / name
            if path.suffix.lower() in {".pdf", ".docx", ".xlsx", ".xlsm", ".gdoc", ".gsheet", ".gslides"}:
                assert ignored(path), "Conversion-capable input was re-included; correct exclusions before native detection"
        for name in (".graphifyignore", ".graphifyrc", ".gitmodules"):
            path = directory / name
            if name in names and (name == ".graphifyignore" or directory == root):
                assert not path.is_symlink(), "Symlinked configuration needs separate review"
                configs[path.relative_to(root).as_posix()] = hashlib.sha256(path.read_bytes()).hexdigest()
    return configs

config_hashes = config_identity()
# A nested ignore file must not override a literal required subtree exclusion.
ignored = ignored_predicate(root, extra_excludes=excludes, gitignore=False)
for pattern in excludes:
    if pattern.endswith("/") and not any(c in pattern for c in "!*?[]#\\"):
        boundary = root / pattern.rstrip("/")
        assert boundary.resolve().is_relative_to(root), "Excluded directory escaped the source root"
        assert not boundary.exists() or ignored(boundary), "Required subtree exclusion was overridden"
configuration = load_graphifyrc(root)
assert all(configuration.get("languages", {}).get(ext, ext) == ext for ext in (".py", ".md")), "Language remapping needs separate coverage verification"
detection = scan()
# Include resolution candidates and omissions: adding a file can change Markdown resolution.
def inventory_identity(result):
    return {key: result[key] for key in ("files", "unclassified", "skipped_sensitive", "ignored", "pruned_noise_dirs", "resolution_inputs")}
inventory = inventory_identity(detection)
assert not detection["walk_errors"], "Incomplete filesystem walk; inspect diagnostics and do not export a complete result"
all_detected = {Path(p) for bucket in detection["files"].values() for p in bucket}
# Markdown may be classified as paper; select by verified suffix from ALL buckets.
paths = sorted(p for p in all_detected if p.suffix.lower() in {".py", ".md"})
assert paths and all(p.resolve().is_relative_to(root) and _get_extractor(p) is not None for p in paths)
def relative(path):
    return Path(path).relative_to(root).as_posix()
def source_identity():
    result = {}
    for path in paths:
        body = path.read_bytes()
        assert b"\x00" not in body, f"Uncertified binary/NUL source: {relative(path)}"
        body.decode("utf-8-sig", errors="strict")
        result[relative(path)] = hashlib.sha256(body).hexdigest()
    return result
inputs = source_identity()
messages = io.StringIO()
with contextlib.redirect_stderr(messages):
    extraction = extract(paths, root=root, cache_root=cache, parallel=False)
work.mkdir(parents=True, exist_ok=True)
(work / "native-diagnostics.txt").write_text(messages.getvalue(), encoding="utf-8")
assert not messages.getvalue().strip(), "Inspect native diagnostic log before claiming complete selected-source extraction"
assert not extraction["failed_sources"] and not extraction["skipped_sources"], "Failed/skipped sources are not complete coverage"
assert source_identity() == inputs, "Sources changed during extraction"
for path in paths:
    fragment = load_cached(path, root=root, cache_root=cache, salt=cache_salt(path))
    assert fragment and fragment.get("nodes") and not fragment.get("error") and not fragment.get("skipped"), relative(path)
    assert not fragment.get("parse_errors"), f"Parser recovery is not clean coverage: {relative(path)}"
errors = validate_extraction(extraction)
assert all("does not match any node id" in error for error in errors), errors
# Unresolved links are recorded diagnostics, not silently repaired or semantic claims.
diagnostics = diagnose_extraction(copy.deepcopy(extraction), root=root, directed=True)
G = build_from_json(copy.deepcopy(extraction), root=root, directed=True, dedup=False)
assert G.number_of_nodes() and G.number_of_nodes() <= 5000, "Narrow this node-level build; aggregation needs separate validation"
communities = cluster(G)
labels = label_communities_by_hub(G, communities)
assert sorted(n for members in communities.values() for n in members) == sorted(G.nodes)
commit = ""
if shutil.which("git"):
    observed = subprocess.run(["git", "-C", str(root), "rev-parse", "HEAD"], capture_output=True, text=True, timeout=30)
    if observed.returncode == 0:
        commit = observed.stdout.strip()
omissions = {
    "uncertified_detected": sorted(relative(p) for p in all_detected - set(paths)),
    "unclassified": [relative(p) for p in detection["unclassified"]],
    "sensitive_or_unsafe": [relative(p) for p in detection["skipped_sensitive"]],
    "ignored": [relative(p) for p in detection["ignored"]],
    "pruned_noise_dirs": [relative(p) for p in detection["pruned_noise_dirs"]],
}
identity_material = {"sources": inputs, "configuration_hashes": config_hashes, "excludes": excludes, "gitignore": False, "graphify_revision": "16218bfc80d4ca2799734d045039f7ed1a5fa9fb", "mode": "utf8-python-markdown-structural-v1"}
identity = hashlib.sha256(json.dumps(identity_material, sort_keys=True, ensure_ascii=False).encode()).hexdigest()
G.graph["context"] = {
    "input_identity": identity, **identity_material, "source_commit": commit or None,
    "semantic_extraction": "not performed", "coverage": "native structural extraction of selected inputs only",
    "omissions": omissions, "raw_nodes": len(extraction["nodes"]), "raw_edges": len(extraction["edges"]),
    "dangling_raw_edges": diagnostics["dangling_endpoint_edges"],
    "limits": ["Fragments/anchors are not validated", "Bare symbol ambiguity can omit references", "Wikilink collisions use native deterministic resolution", "No complete filesystem/semantic/portable-maintenance claim"],
}
stage.mkdir()
assert to_json(G, communities, str(stage / "graph.json"), built_at_commit=commit, community_labels=labels)
assert to_html(G, communities, str(stage / "graph.html"), community_labels=labels, node_limit=5000, learning_overlay={})
# Static view annotation precedes all generation markers/sibling hashes.
key_module = Path(os.environ["CONTEXT_TOOLS"]) / "view_legend.py"
key_spec = importlib.util.spec_from_file_location("context_view_legend", key_module)
view_key = importlib.util.module_from_spec(key_spec)
key_spec.loader.exec_module(view_key)
write_text_atomic(stage / "graph.html", view_key.html_key((stage / "graph.html").read_text(encoding="utf-8")))
report_detection = dict(detection, total_files=len(paths), warning="STRUCTURAL ONLY: selected UTF-8 Python/Markdown inputs; semantic extraction was not performed.")
report = generate(G, communities, score_all(G, communities), labels, god_nodes(G), surprising_connections(G, communities), report_detection, {"input": 0, "output": 0}, root.name)
report = report.replace("- None detected - all connections are within the same source files.", "- No top-ranked surprising connection reported; this does not establish absence of cross-file relationships.")
report = report.replace("- Token cost: 0 input · 0 output", "- Model/API tokens used by this structural build: 0 (no model/semantic step)")
report += "\n## Structural scope and provenance\n\nInput identity: `" + identity + "`. Source commit (provenance only): `" + (commit or "unversioned") + "`.\n\n"
report += "Selected source hashes and omissions (paths relative to the source root; pruned subtrees are not exhaustive file listings):\n\n```json\n" + json.dumps({"sources": inputs, "omissions": omissions, "raw_nodes": len(extraction["nodes"]), "raw_edges": len(extraction["edges"]), "dangling_raw_edges": diagnostics["dangling_endpoint_edges"]}, ensure_ascii=False, indent=2) + "\n```\n"
report += "\nMarkdown fragments are not validated; ordinary code hyperlinks may be skipped, ambiguous bare mentions may be omitted, unused reference definitions may create edges and native wikilink collisions are not semantic disambiguation. JSON retains source locations/confidence; HTML is a view, not all evidence fields. Rendering needs JavaScript and the vis-network CDN. No browser rendering, semantic extraction, portable update or publication transaction is claimed.\n"
write_text_atomic(stage / "GRAPH_REPORT.md", report)
serialized = json.loads((stage / "graph.json").read_text(encoding="utf-8"))
reopened = load_node_link_graph(serialized)
assert reopened.is_directed() and set(reopened.nodes) == set(G.nodes)
assert serialized["graph"]["context"]["input_identity"] == identity
ids = [n["id"] for n in serialized["nodes"]]
assert len(ids) == len(set(ids))
assert all(e["source"] in G and e["target"] in G for e in serialized["links"])
assert all(n.get("external") or n.get("source_file") in inputs for n in serialized["nodes"])
assert all(n.get("external") or n.get("_origin") == "ast" for n in serialized["nodes"])
for path in stage.iterdir():
    text = path.read_text(encoding="utf-8")
    assert text and str(root) not in text and str(work) not in text, path.name
assert {p.name for p in stage.iterdir()} == {"graph.json", "graph.html", "GRAPH_REPORT.md"}
# Validate evidence after JSON reload, including edge direction and folded evidence.
assert set(reopened.edges) == set(G.edges)
for source, target, evidence in G.edges(data=True):
    restored = reopened.edges[source, target]
    for field in ("relation", "confidence", "source_file", "source_location", "_origin", "also_seen"):
        assert restored.get(field) == evidence.get(field), (source, target, field)
    expected_score = evidence.get("confidence_score", {"EXTRACTED": 1.0, "INFERRED": 0.55, "AMBIGUOUS": 0.2}.get(evidence.get("confidence", "EXTRACTED"), 1.0))
    assert restored["confidence_score"] == expected_score
html = (stage / "graph.html").read_text(encoding="utf-8")
def embedded(name):
    return json.JSONDecoder().raw_decode(html.split("const " + name + " = ", 1)[1])[0]
assert {n["id"]: n["source_file"] for n in embedded("RAW_NODES")} == {n["id"]: n.get("source_file", "") for n in serialized["nodes"]}
assert sorted((e["from"], e["to"], e["label"], e["confidence"]) for e in embedded("RAW_EDGES")) == sorted((e["source"], e["target"], e.get("relation", ""), e.get("confidence", "EXTRACTED")) for e in serialized["links"])
assert f'{G.number_of_nodes()} nodes · {G.number_of_edges()} edges' in report
assert f'{G.number_of_nodes()} nodes &middot; {G.number_of_edges()} edges' in html
assert config_identity() == config_hashes, "Configuration changed during build; discard this stage"
assert inventory_identity(scan()) == inventory, "Inventory changed during build; discard this stage"
assert source_identity() == inputs, "Sources changed while exporting; discard this stage"
print(json.dumps({"stage": str(stage), "selected_files": len(paths), "nodes": G.number_of_nodes(), "edges": G.number_of_edges(), "raw_edges": len(extraction["edges"]), "dangling_raw_edges": diagnostics["dangling_endpoint_edges"], "input_identity": identity, "semantic_extraction": "not performed"}, ensure_ascii=False))
```

Output: a fresh structural trio under `CONTEXT_STAGE/artifacts`, source/exclusion/omission evidence and explicit origin/direction. Zero native model-token counters describe this structural recipe, not any agent reading elsewhere. File/node presence does not establish complete source or semantic coverage. The recipe checks serialization, endpoint/evidence and direction retention, counts and input identities. Inspect known caller/document relationships at their sources through the [build method](../operations/graphify/build.md#build-and-inspect-the-structural-baseline); corpus-specific oracles belong to that inspection and the fixture probes. Browser rendering remains separate.

## Bounded structural-stage query

This narrower recipe is only for the known fresh structural stage without a learning sidecar. `CONTEXT_SEED` is a verified unique node ID; `CONTEXT_QUESTION` is the actual bounded question. The native loader reads the entire JSON into its process. Published mixed generations use the [validated-dict read interface](graphify-read.md), which avoids optional sidecar loading.

```python
# context-structural-query
import os
from pathlib import Path
from graphify.serve import _read_graph, _query_graph_text
path = Path(os.environ["CONTEXT_STAGE"]) / "artifacts" / "graph.json"
G = _read_graph(str(path))
G.graph["_learning_overlay"] = {}
print(_query_graph_text(G, os.environ["CONTEXT_QUESTION"], seeds=[os.environ["CONTEXT_SEED"]], seed_root=Path(os.environ["CONTEXT_ROOT"]), depth=1, token_budget=1200))
```

BFS/DFS collects undirected context and may truncate; it is not a directional dependency path. Native category scores can be defaults (EXTRACTED=1, INFERRED=0.55, AMBIGUOUS=0.2), not measured probabilities.

## Semantic protocol

The validator fingerprints this marked protocol together with the [marked agent method](../operations/graphify/build.md#semantic-reading-and-reconciliation). Neither fragment alone is the extraction contract.

<!-- context-semantic-contract:start -->

### Plan and source ranges

The initial mixed plan covers every source of the structural baseline, including zero findings. It binds `schema` and `prompt_version` to `context-semantic-v1`, `graphify_revision` to the pinned revision, a nonempty `scope`, `structural_sha256` to the full baseline artifact bytes, `sources` to root-relative POSIX paths with `{sha256, line_count}`, and `shards` to `[{id, ranges:[{source_file,start,end,sha256}]}]`.

Source hashes cover unchanged raw bytes. Decode UTF-8 with optional BOM; count `splitlines(keepends=True)`. Range hashes cover inclusive decoded lines re-encoded as UTF-8 with original line endings. Nonempty ranges are 1-based inclusive. An empty source has one `0..0` range and the hash of empty bytes, and can produce only a zero-findings receipt. Across all assigned shards, ranges cover each planned source exactly once through EOF without gaps/overlaps.

Validator ceilings: each JSON/source file 2 MiB, 100 sources, 64 shards, 32 MiB aggregate fragments and 3 hyperedges per shard. These are parser/validation limits, not suggested model workloads. The full baseline source set, bytes and in-scope configuration are checked before/after mixed assembly; an inventory mismatch requires a fresh structural baseline. The recorded structural omissions inventory is not recertified by the semantic phase.

### Fragment and receipt schema

Each result has `schema`, `shard_id`, `status:"complete"`, `reader:{surface,model,usage:null}`, `receipts`, `nodes`, `edges`, `hyperedges` and `open_questions`. Each receipt repeats its assigned `{source_file,start,end,sha256}` and adds a meaningful `summary`, `outcome:"findings"|"zero-findings"` and `reason`. A findings receipt owns an emitted record/question; empty graph arrays alone do not establish a finding. Reader provenance records only observable/assigned identity; unknown identity and subscription usage stay null. This profile does not implement measured subscription counters.

### Records, identity and evidence

Native file types are `code`, `document`, `paper`, `image`, `rationale`, `concept`. New semantic nodes carry `entity_key`, native `make_id(Path(source_file).with_suffix("").as_posix(), entity_key)`, short `label`, allowed `file_type`, primary `source_file`, `source_location:"L3"|"L3-L7"`, `_origin:"semantic"` and `evidence`. IDs use full root-relative paths and native Unicode normalization. A structural symbol is referenced by its exact verified AST ID rather than duplicated as a semantic node.

Evidence is a list of `{source_file,start,end,quote}`. Quotes contain exact complete decoded source lines with only the final CR/LF omitted. Primary evidence lies within the assigned range and bounded record location; other supporting sources must be globally planned and actually read, without transferring ownership of their semantic tier.

Edges add `source`, `target`, directed `relation`, `confidence`, `confidence_score`, and nonempty `rationale` for inference/ambiguity. Confidence encoding is EXTRACTED/1.0 for explicit evidence, INFERRED with upstream rubric 0.95/0.85/0.75/0.65/0.55, or AMBIGUOUS 0.1–0.3. INFERRED/AMBIGUOUS cross-source edges require anchors for both endpoint sources; an EXTRACTED reference can be evidenced in the referring source with a separately verified target ID. Evidence-bearing `open_questions` carry `question` plus primary source/location/origin/evidence.

Optional hyperedges use the same evidence/confidence/origin fields, with `entity_key`, source-owned `id`, `label`, `nodes` (at least three distinct resolved members), and `relation`. Inferred/ambiguous groups anchor every member-source identity. The recorded semantic trials use pairwise edges; hyperedges must also pass native normalization/preservation checks and may be refused.

All semantic nodes, edges and hyperedges explicitly carry `_origin:"semantic"`. Legacy origin inference treats `L<number>` locations as AST; metadata attached only to an AST node can disappear with its refresh. The native simple directed graph cannot preserve every same-endpoint parallel fact. This profile refuses a semantic pair already occupied by another semantic or structural edge instead of silently losing relations/origin. Structural evidence remains independently owned.

### Validator boundary

[validate_context_fragments.py](validate_context_fragments.py) reads/parses/hashes the same bounded JSON buffer, rejects duplicate keys/nonfinite numbers/partial markers, and invokes native security/schema/ID validation. It rejects missing/unexpected/duplicate shards; incorrect ranges/hashes; changed bytes; unsafe paths; bad evidence anchors; origin/confidence errors; duplicate/AST IDs; unresolved endpoints; and unsupported collisions. Validation uses the aggregate semantic+structural ID universe, including later-range references to earlier concepts. It returns validated semantic data and the coverage ledger on stdout without repair, cache, merge or publication writes.

Native `validate_semantic_fragment` validates shape/security, not complete coverage. `sanitize_semantic_fragment` drops `concept`/`rationale` nodes and can filter cross-fragment hyperedges. `merge-chunks` skips invalid siblings, uses first-wins IDs, drops coverage and replaces unknown usage with numeric zero. The selected direct assembly avoids those lossy boundaries; exit 0 or well-formed JSON does not certify completeness or semantic understanding.

<!-- context-semantic-contract:end -->

CLI invocation of the strict validator:

```sh
"$CONTEXT_PY" "$CONTEXT_TOOLS/validate_context_fragments.py" \
  --root "$CONTEXT_ROOT" --plan /absolute/task/plan.json \
  --structural /absolute/task/structural/artifacts/graph.json \
  --fragments /absolute/task/chunk-a.json /absolute/task/chunk-b.json
```

## Assemble, interpret and verify a fresh mixed trio

Inputs: the same verified interpreter, root/tools and no-provider environment as structural staging; `CONTEXT_PLAN`, `CONTEXT_STRUCTURAL`, and `CONTEXT_FRAGMENTS` (JSON array of explicit result paths). `GRAPHIFY_OUT` remains external and fixed before imports. `CONTEXT_MIXED_STAGE` must be NEW and external. Baseline selection, bytes/paths and scoped configuration are checked; rebuild structural staging when fresh whole-omission inventory is needed.

With no `CONTEXT_LABELS`, the recipe validates/builds in memory and prints exact community members plus input/evidence identity without artifacts. Its second invocation accepts `CONTEXT_LABELS` pointing to `{input_identity, evidence_identity, communities:{"<id>":{members:["<sorted IDs>"],label:"<short source-backed name>",rationale:"<interpretation>"}}}`. Identity and exact member mismatch refuses reuse. Actual reading and naming of communities belongs to the [build operation](../operations/graphify/build.md); the recipe does not infer those names.

The block embeds coverage, interpretation and portable maintenance state, annotates native HTML before sealing, and writes final sibling hashes into JSON last. Run without Python optimization so assertions remain active. Legacy serialized labels containing `D` denote the structural-only staging observation; their names are retained for report/metadata compatibility.

```python
# context-semantic-assemble
if not __debug__:
    raise RuntimeError("Run without Python optimization: assembly validation must remain enabled")
import copy
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import re
from graphify.build import build_merge
from graphify.cluster import cluster, score_all
from graphify.analyze import god_nodes, surprising_connections
from graphify.export import to_json
from graphify.exporters.html import to_html
from graphify.paths import load_node_link_graph, write_text_atomic
from graphify.report import generate

root = Path(os.environ["CONTEXT_ROOT"]).resolve(strict=True)
assert os.environ.get("GRAPHIFY_BACKEND") == "none"
assert not Path(os.environ["GRAPHIFY_OUT"]).resolve().is_relative_to(root)
module = Path(os.environ["CONTEXT_TOOLS"]) / "validate_context_fragments.py"
spec = importlib.util.spec_from_file_location("context_fragments", module)
validator = importlib.util.module_from_spec(spec)
spec.loader.exec_module(validator)
plan, baseline = Path(os.environ["CONTEXT_PLAN"]), Path(os.environ["CONTEXT_STRUCTURAL"])
fragments = [Path(p) for p in json.loads(os.environ["CONTEXT_FRAGMENTS"])]
validated = validator.validate(root, plan, baseline, fragments)
structural = validator.strict_json(baseline)
G = build_merge([copy.deepcopy({k: validated[k] for k in ("nodes", "edges", "hyperedges")})], graph_path=baseline, root=root, directed=True, dedup=False)
assert G.is_directed() and 0 < G.number_of_nodes() <= 5000
assert set(G) == {n["id"] for n in structural["nodes"] + validated["nodes"]}, "Native identity reconciliation changed the intended node set"
for node in structural["nodes"] + validated["nodes"]:
    for field in ("source_file", "source_location", "_origin", "evidence", "claim_status"):
        assert G.nodes[node["id"]].get(field) == node.get(field), (node["id"], field)
expected_edges = structural["links"] + validated["edges"]
assert set(G.edges) == {(e["source"], e["target"]) for e in expected_edges}
for edge in expected_edges:
    for field in ("relation", "confidence", "confidence_score", "source_file", "source_location", "_origin", "evidence", "rationale"):
        assert G.edges[edge["source"], edge["target"]].get(field) == edge.get(field), field
assert G.graph.get("hyperedges", []) == structural.get("graph", {}).get("hyperedges", []) + validated["hyperedges"], "Inspect native hyperedge normalization before claiming preservation"
communities = cluster(G)
ledger = validated["context_semantic"]
plan_data = validator.strict_json(plan)
current_profile = validator.profile(module.parent)
if plan_data.get("expected_profile") is not None:
    assert plan_data["expected_profile"] == current_profile, "Planned extraction profile changed; reassess/reprocess"
current_snapshot = validator.snapshot(root, structural["graph"]["context"]["excludes"], plan_data.get("authority_sources", []), scope=ledger["scope"])
originals = {}
for path in fragments:
    payload, consumed = validator.strict_json(path, with_identity=True)
    originals[payload["shard_id"]] = {"payload": payload, "origin_sha256": consumed["sha256"]}
portable = validator.make_state(current_snapshot, current_profile, originals, structural["nodes"], ledger, plan_data.get("dependency_reviews"))
identity = validator._digest({"snapshot": portable["snapshot"], "profile": portable["profile"]})
evidence_identity = validator._digest({"structural_sha256": ledger["structural_sha256"], "groups": portable["groups"]})
members = {str(cid): sorted(nodes) for cid, nodes in communities.items()}
if not os.environ.get("CONTEXT_LABELS"):
    print(json.dumps({"input_identity": identity, "evidence_identity": evidence_identity, "communities": {cid: [{"id": n, "label": G.nodes[n].get("label"), "source_file": G.nodes[n].get("source_file"), "origin": G.nodes[n].get("_origin")} for n in nodes] for cid, nodes in members.items()}}, ensure_ascii=False))
    raise SystemExit(0)
interpretation = validator.strict_json(os.environ["CONTEXT_LABELS"])
assert interpretation["input_identity"] == identity and interpretation["evidence_identity"] == evidence_identity and set(interpretation["communities"]) == set(members), "Interpretation must match actual semantic evidence and membership"
labels = {}
for cid, nodes in members.items():
    item = interpretation["communities"][cid]
    assert item["members"] == nodes and item["label"].strip() and item["rationale"].strip()
    labels[int(cid)] = item["label"]
G.graph["context"] = {**structural["graph"]["context"], "input_identity": identity, "structural_input_identity": structural["graph"]["context"]["input_identity"], "semantic_extraction": "performed by active subscription agents for explicitly planned ranges", "coverage": "structural baseline plus validated semantic planned ranges; omissions snapshot observed at D staging", "omissions_observed_at": structural["graph"]["context"]["input_identity"], "maintenance": portable, "semantic": ledger, "community_evidence_identity": evidence_identity, "community_interpretation": interpretation["communities"]}
stage = Path(os.environ["CONTEXT_MIXED_STAGE"]).resolve()
assert not stage.exists() and not stage.is_relative_to(root) and not root.is_relative_to(stage), "Use a fresh external mixed stage"
stage.mkdir(parents=True)
assert to_json(G, communities, str(stage / "graph.json"), built_at_commit=structural["graph"]["context"].get("source_commit") or "", community_labels=labels)
assert to_html(G, communities, str(stage / "graph.html"), community_labels=labels, node_limit=5000, learning_overlay={})
# Static view annotation precedes all generation markers/sibling hashes.
key_module = Path(os.environ["CONTEXT_TOOLS"]) / "view_legend.py"
key_spec = importlib.util.spec_from_file_location("context_view_legend", key_module)
view_key = importlib.util.module_from_spec(key_spec)
key_spec.loader.exec_module(view_key)
write_text_atomic(stage / "graph.html", view_key.html_key((stage / "graph.html").read_text(encoding="utf-8")))
detection = {"total_files": len(ledger["sources"]), "total_words": sum(len((root / p).read_text(encoding="utf-8-sig").split()) for p in ledger["sources"]), "warning": "PLANNED-RANGE SEMANTIC: active-agent extraction was performed; coverage is limited to the explicit validated scope, not universal understanding."}
report = generate(G, communities, score_all(G, communities), labels, god_nodes(G), surprising_connections(G, communities), detection, {"input": 0, "output": 0}, root.name)
report = re.sub(r"^- Token cost:.*$", "- Subscription-agent token usage: unknown (host did not expose counters).", report, flags=re.M)
report = report.replace("- None detected - all connections are within the same source files.", "- No top-ranked surprising connection reported; this does not establish absence of cross-file relationships.")
report += "\n## Semantic scope, evidence and interpretation\n\nInput identity: `" + identity + "`. Unknown usage is not zero. Scores are annotations, not calibrated probabilities. Omitted/unsupported input inventory is the D-staging observation; this phase rechecks selected Python/Markdown sources and configuration, not every omitted-file change. Current policy, historical proposals, observations and unresolved claims retain their source roles.\n\n```json\n" + json.dumps({"semantic": ledger, "community_interpretation": interpretation["communities"], "structural_omissions_observed_at_D_staging": structural["graph"]["context"]["omissions"]}, ensure_ascii=False, indent=2) + "\n```\n\nHTML needs JavaScript and its pinned CDN; rendering was not verified by data export. This is a staged result. Portable reuse requires the documented profile/dependency checks; publication requires the separate authorized commit step.\n"
write_text_atomic(stage / "GRAPH_REPORT.md", report)
# Seal final siblings before storing their hashes in JSON; JSON never hashes itself.
generation = validator.generation_identity(validator.strict_json(stage / "graph.json"))
marker = "<!-- context-generation:" + generation + " -->"
write_text_atomic(stage / "graph.html", (stage / "graph.html").read_text(encoding="utf-8") + "\n" + marker + "\n")
write_text_atomic(stage / "GRAPH_REPORT.md", report + "\n" + marker + "\n")
G.graph["context"]["generation_identity"] = generation
G.graph["context"]["artifacts"] = {name: hashlib.sha256((stage / name).read_bytes()).hexdigest() for name in ("graph.html", "GRAPH_REPORT.md")}
assert to_json(G, communities, str(stage / "graph.json"), built_at_commit=structural["graph"]["context"].get("source_commit") or "", community_labels=labels)
validator.validate_trio(stage, root=root, require_current=True)
serialized = validator.strict_json(stage / "graph.json")
reopened = load_node_link_graph(serialized)
assert set(reopened) == set(G) and set(reopened.edges) == set(G.edges) and reopened.is_directed()
for edge in expected_edges:
    for field in ("relation", "confidence", "confidence_score", "source_file", "source_location", "_origin", "evidence", "rationale"):
        assert reopened.edges[edge["source"], edge["target"]].get(field) == edge.get(field), field
html = (stage / "graph.html").read_text(encoding="utf-8")
def embedded(name):
    return json.JSONDecoder().raw_decode(html.split("const " + name + " = ", 1)[1])[0]
assert {n["id"] for n in embedded("RAW_NODES")} == set(G)
assert sorted((e["from"], e["to"], e["label"], e["confidence"]) for e in embedded("RAW_EDGES")) == sorted((e["source"], e["target"], e["relation"], e["confidence"]) for e in expected_edges)
assert f'{G.number_of_nodes()} nodes · {G.number_of_edges()} edges' in report and "- Token cost:" not in report
assert validator.validate(root, plan, baseline, fragments) == validated, "Inputs changed while assembling; discard this stage"
assert {p.name for p in stage.iterdir()} == {"graph.json", "graph.html", "GRAPH_REPORT.md"}
for path in stage.iterdir():
    body = path.read_text(encoding="utf-8")
    assert body and str(root) not in body and str(stage) not in body
print(json.dumps({"stage": str(stage), "nodes": G.number_of_nodes(), "edges": G.number_of_edges(), "semantic_nodes": len(validated["nodes"]), "semantic_edges": len(validated["edges"]), "input_identity": identity, "usage": None}, ensure_ascii=False))
```

Output: fresh native JSON/HTML/report from one graph and inventory, with unknown subscription usage preserved explicitly. Validator/build/export/evidence failure invalidates the stage and cannot replace published references. The trio and current source/profile checks are detailed in [maintenance interfaces](graphify-maintenance.md). Initial assembly does not publish, and replayed fragments are not a new semantic read.

## Source ledger

- [Detection](https://github.com/Graphify-Labs/graphify/blob/16218bfc80d4ca2799734d045039f7ed1a5fa9fb/graphify/detect.py): `detect` 2101, `save_manifest` 2757, separate tier hashes 2973, exclusions/deletions 3165, `detect_incremental` 3219.
- [Structural extraction](https://github.com/Graphify-Labs/graphify/blob/16218bfc80d4ca2799734d045039f7ed1a5fa9fb/graphify/extract.py): `extract` 10353, explicit origin 12331; [Markdown](https://github.com/Graphify-Labs/graphify/blob/16218bfc80d4ca2799734d045039f7ed1a5fa9fb/graphify/extractors/markdown.py): `_resolve_markdown_link` 311, `extract_markdown` 431; [mention resolver](https://github.com/Graphify-Labs/graphify/blob/16218bfc80d4ca2799734d045039f7ed1a5fa9fb/graphify/markdown_resolution.py); [shared IDs](https://github.com/Graphify-Labs/graphify/blob/16218bfc80d4ca2799734d045039f7ed1a5fa9fb/graphify/ids.py).
- [Build/merge](https://github.com/Graphify-Labs/graphify/blob/16218bfc80d4ca2799734d045039f7ed1a5fa9fb/graphify/build.py): `_is_ast_tier` 45, `build_from_json` 1524, `_tier_replacement_sources` 2485, `merge_raw_extraction` 2551, `build_merge` 2695, repo namespace 3209. [Semantic boundary](https://github.com/Graphify-Labs/graphify/blob/16218bfc80d4ca2799734d045039f7ed1a5fa9fb/graphify/semantic_cleanup.py): validation/security caps, source-aware sanitation; `validate.py` covers basic extraction schema, not complete evidence/coverage validation.
- [Cache](https://github.com/Graphify-Labs/graphify/blob/16218bfc80d4ca2799734d045039f7ed1a5fa9fb/graphify/cache.py): `cache_dir` 1030, `load_cached` 1069, `check_semantic_cache` 1393, `save_semantic_cache` 1539, `scope_semantic_result` 1843. [CLI](https://github.com/Graphify-Labs/graphify/blob/16218bfc80d4ca2799734d045039f7ed1a5fa9fb/graphify/cli.py): query stamp 1007 (call sites 2111/2553/2687), code update 3312, headless extract 4142/provider selection 4658, `merge-chunks` 5819, `merge-semantic` 5908. `llm.py` contains the provider pipeline; its `extract_corpus_parallel` is not selected for subscription extraction.
