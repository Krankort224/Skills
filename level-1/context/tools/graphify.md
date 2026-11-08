# Graphify: source profile and compatibility

## Contents

- [Authority and supported boundary](#authority-and-supported-boundary)
- [Immutable source and dependencies](#immutable-source-and-dependencies)
- [Prepare and verify the structural environment](#prepare-and-verify-the-structural-environment)
- [Build and inspect structural evidence](#build-and-inspect-structural-evidence)
- [Capability and reuse decisions](#capability-and-reuse-decisions)
- [Construction route](#construction-route)
- [Semantic evidence contract](#semantic-evidence-contract)
- [Subscription fragments and mixed assembly](#plan-read-and-reconcile-subscription-fragments)
- [Freshness, portability and publication](#freshness-portability-and-publication)
- [Commit-level trio publication](#publish-a-validated-trio-from-an-isolated-clone)
- [Verification corpus and oracles](#verification-corpus-and-oracles)
- [Source ledger](#source-ledger)

## Authority and supported boundary

Project understanding starts with the task, applicable scope and authoritative sources. The populated `references/repository.md` explains project purpose, component roles and interactions, constraints, knowledge owners and routes to detail. Graphs supply derived relationship evidence; neither connectivity nor a model's confidence overrides the owner of a fact. Missing, stale, incompatible or incomplete graphs leave ordinary source investigation available. A narrow question needs only relevant sources and bounded graph results.

This guide records the inspected native interfaces and the verified compatibility profile. The current shared `context/SKILL.md` routes to complete project-map read, maintain and review methods without graph prerequisites. The structural procedure below prepares and verifies a fresh staged trio for the tested Linux Python/Markdown lane. The semantic procedure below adds actual current-agent reading, strict range/evidence validation and fresh native mixed assembly in the same tested lane. The maintenance method adds conservative semantic-shard reuse, cold-checkout recovery and coherent Git-commit trio publication in that same tested lane. Broader investigation and the actual two-host pilot retain their separate implementation/validation gates. Issue execution, publication and acceptance remain with `workflow`; delegation remains with `delegation`.

## Immutable source and dependencies

- Upstream: [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify/tree/16218bfc80d4ca2799734d045039f7ed1a5fa9fb), commit **`16218bfc80d4ca2799734d045039f7ed1a5fa9fb`**, distribution **`graphifyy==0.9.103`**, executable **`graphify`** (`graphify.__main__:main`). Distribution name and executable name differ.
- License: [Apache-2.0 LICENSE](https://github.com/Graphify-Labs/graphify/blob/16218bfc80d4ca2799734d045039f7ed1a5fa9fb/LICENSE); upstream also retains [LICENSE-MIT](https://github.com/Graphify-Labs/graphify/blob/16218bfc80d4ca2799734d045039f7ed1a5fa9fb/LICENSE-MIT) for earlier contributions and [NOTICE](https://github.com/Graphify-Labs/graphify/blob/16218bfc80d4ca2799734d045039f7ed1a5fa9fb/NOTICE): Graphify, copyright 2026 Safi Shamsi and the Graphify contributors. Preserve applicable license/notice text and identify modifications if later adopting upstream source or extraction prose. This slice vendors no upstream helper or specification; the probe is original test code calling the external package.
- Reviewed agent route: complete `graphify/skill-codex.md` and its extraction, update, query, exports, GitHub/merge, add/watch, hooks and transcription references, with corresponding implementations/tests. Windows preparation/PowerShell encoding and process-spawn differences were inspected at source level. Upstream skill instructions are evidence to assess, not an additional installed skill.
- Verified runtime profile: **Linux, CPython 3.12.14**, base distribution only: NetworkX 3.7, NumPy 2.5.4, PyYAML 6.0.3, RapidFuzz 3.14.6 and the upstream-required tree-sitter runtime/grammars, exactly listed in [graphify-requirements.txt](graphify-requirements.txt). No optional extras. Upstream metadata allows Python >=3.10, but these resolved NetworkX/NumPy pins require >=3.12; do not advertise this lock for 3.10/3.11. Other interpreters/platforms require a separately tested resolution.
- Core clustering uses NetworkX Louvain when optional Leiden libraries are absent. HTML needs no Python rendering extra. SVG requires optional matplotlib/Pillow; PDF/Office/video/SQL/other language extras are corpus-specific and outside this verified base profile. Neither `[all]`, MCP, a database, Graphify Cloud nor an API provider is needed.

For an authorized isolated preparation, use a task-owned environment and the exact requirements file, for example:

```sh
uv venv /absolute/task-directory/graphify-venv --python 3.12
uv pip install --python /absolute/task-directory/graphify-venv/bin/python \
  -r /absolute/context/tools/graphify-requirements.txt
/absolute/task-directory/graphify-venv/bin/graphify --version
/absolute/task-directory/graphify-venv/bin/python \
  /absolute/context/tools/probe_graphify.py
```

Use `Scripts/python.exe` and `Scripts/graphify.exe` in a Windows venv; that path is source-reviewed, not runtime-verified here. Reuse an existing environment only after checking interpreter, distribution source/revision and dependency compatibility. A version string alone cannot distinguish a locally modified package. An installation needs filesystem access, package/source retrieval and appropriate wheels/build tools. Offline or denied setup leaves direct source reading available and tool-dependent maintenance unperformed. Do not invoke `graphify install`, upgrade a global environment, change agent instructions/hooks or reuse ambient provider credentials.

The source is pinned by commit and runtime dependencies by versions; build-isolation dependencies remain selected by upstream's build-system requirement (`setuptools>=83.0.0`). This profile is not a hash-locked wheel supply chain or a promise of identical binaries on other hosts.

## Prepare and verify the structural environment

This supported construction slice is **Linux CPython 3.12, exercised at 3.12.14**, using the immutable base requirements above. The verified source formats are UTF-8 `.py` and `.md` with no NUL bytes, parsed by native Graphify. Other formats/languages remain explicitly unselected or uncertified; the package's larger grammar list is not a test result for them. Real Windows/second Work-host execution remains unverified.

Use an authorized task-owned venv outside the project. Locate an existing candidate by its explicit interpreter path first; run the check below. If it passes, reuse it without installing/upgrading anything. If absent or incompatible, create a new isolated environment using the exact requirements; leave the candidate/global installations untouched. If Python/uv/Git/network or write access is unavailable, report that specific preparation gap and retain direct source reading/map work. Do not silently select a different revision, extras or provider backend. Offline reuse of a verified installation does not require package retrieval; offline creation needs previously available compatible artifacts.

```sh
# Replace these values with actual absolute paths; do not paste source text into shell code.
CONTEXT_PY=/absolute/task/graphify-venv/bin/python
export CONTEXT_TOOLS=/absolute/skills/context/tools
export CONTEXT_ROOT=/absolute/project
export CONTEXT_STAGE=/absolute/task/fresh-structural-stage
export GRAPHIFY_OUT="$CONTEXT_STAGE/native-cache"
export GRAPHIFY_BACKEND=none
export GRAPHIFY_QUERY_LOG_DISABLE=1
export PYTHONDONTWRITEBYTECODE=1
# Only if no verified candidate is available:
uv venv /absolute/task/graphify-venv --python 3.12
uv pip install --python "$CONTEXT_PY" -r "$CONTEXT_TOOLS/graphify-requirements.txt"
```

Run this block with that interpreter (`"$CONTEXT_PY" - <<'PY'`, paste the Python, then `PY`). Checks execute no installer and create no project references. The profile records a VCS install; a same-version package without that provenance needs separate verification.

```python
# context-profile-check
if not __debug__:
    raise RuntimeError("Run without Python optimization: validation must remain enabled")
import importlib.metadata as metadata
import json
import os
from pathlib import Path
import subprocess
import sys

if sys.implementation.name != "cpython" or sys.version_info[:2] != (3, 12) or sys.platform != "linux":
    raise RuntimeError("This recorded profile requires Linux CPython 3.12; verify another lane separately")
assert metadata.version("graphifyy") == "0.9.103", "Graphify version mismatch"
origin = json.loads(metadata.distribution("graphifyy").read_text("direct_url.json") or "{}")
assert origin.get("url") == "https://github.com/Graphify-Labs/graphify.git", "Unknown package source"
assert origin.get("vcs_info", {}).get("commit_id") == "16218bfc80d4ca2799734d045039f7ed1a5fa9fb", "Source revision mismatch"
requirements = Path(os.environ["CONTEXT_TOOLS"]) / "graphify-requirements.txt"
for line in requirements.read_text(encoding="utf-8").splitlines():
    if "==" in line and not line.startswith("#"):
        name, expected = line.split("==", 1)
        assert metadata.version(name) == expected, f"Dependency mismatch: {name}"
import graphify
assert Path(graphify.__file__).resolve().is_relative_to(Path(sys.prefix).resolve()), "Import escaped candidate environment"
cli = Path(sys.executable).parent / "graphify"
assert cli.is_file(), "Candidate CLI is missing; do not fall through to a global executable"
assert cli.resolve().is_relative_to(Path(sys.prefix).resolve()), "CLI escaped candidate environment"
assert cli.read_text(encoding="utf-8").splitlines()[0] == "#!" + sys.executable, "Verify a nonstandard CLI launcher separately"
assert any(e.name == "graphify" and e.value == "graphify.__main__:main" for e in metadata.distribution("graphifyy").entry_points), "Unexpected CLI entry point"
version = subprocess.run([str(cli), "--version"], check=True, capture_output=True, text=True, timeout=30)
assert version.stdout.strip() == "graphify 0.9.103", version.stdout
print(json.dumps({"profile": "verified", "python": sys.version.split()[0], "graphify": metadata.version("graphifyy"), "commit": origin["vcs_info"]["commit_id"]}))
```

Version checks establish the recorded source/dependency profile, not integrity against local tampering. On an upgraded/different environment repeat the bounded probes, including exact source/direction oracles; do not infer compatibility from successful imports alone. The source is external; no upstream helper/specification is copied by this slice.

## Build and inspect structural evidence

Use only for explicitly authorized graph construction, after selecting the source root/scopes and their authoritative sources. This procedure prepares **fresh staged artifacts**, not an automatic replacement of published references. It has no provider/model step or semantic coverage. The current agent's reading elsewhere in the task is not measured by its zero model-token counters.

Choose explicit exclusions for generated outputs (including the installed skill's actual graph directory and any native `memory/` output), staging/cache locations and unselected third-party inputs. The example below excludes the conventional installed output, vendor/generated paths and Office/PDF/Google shortcuts before detection, so detection cannot convert/export those inputs. Adapt these paths to the actual project; an omitted path is not automatically excluded. Use trailing-slash directory exclusions so native detection prunes fixed subtrees before reading their local rules. Case-insensitive Office/PDF/Google-shortcut exclusions are appended by the block; preflight refuses a nested rule that re-includes a conversion-capable file. Declared submodule paths are added without initialization/fetch; unusual ignore-metacharacter spellings require separate handling and are rejected here. Ignored/noise directories and directory symlinks may be pruned without a complete descendant listing; the inventory must state this limit.

```sh
export CONTEXT_EXCLUDES='["skills/context/references/graphify/","graphify-out/","generated/","vendor/","third_party/","**/*.docx","**/*.xlsx","**/*.xlsm","**/*.pdf","**/*.gdoc","**/*.gsheet","**/*.gslides"]'
```

Run the following block with the **same verified interpreter**, `GRAPHIFY_OUT` set before importing, and a new `CONTEXT_STAGE` outside the source tree for every build. It uses the reviewed native library at the Markdown/CLI gap; there is no standalone build wrapper or replacement parser. Do not use `graphify extract --code-only` to claim documentary coverage or a headless semantic command with ambient keys.

```python
# context-structural-build
if not __debug__:
    raise RuntimeError("Run without Python optimization: validation must remain enabled")
import contextlib
import copy
import hashlib
import importlib.metadata as metadata
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
excludes = json.loads(os.environ["CONTEXT_EXCLUDES"])
assert isinstance(excludes, list) and all(isinstance(x, str) for x in excludes)
# Native detection can convert Office inputs; exclude every casing before it runs.
for extension in ("pdf", "docx", "xlsx", "xlsm", "gdoc", "gsheet", "gslides"):
    excludes.append("**/*." + "".join("[" + c.lower() + c.upper() + "]" for c in extension))
# Record declared, unselected submodules; a native scan does not exclude them automatically.
modules = root / ".gitmodules"
if modules.exists():
    assert modules.resolve().is_relative_to(root)
    listing = subprocess.run(["git", "config", "--file", str(modules), "--get-regexp", r"^submodule\..*\.path$"], capture_output=True, text=True, timeout=30)
    assert listing.returncode in (0, 1), listing.stderr
    for line in listing.stdout.splitlines():
        path = line.split(None, 1)[1]
        assert path and path == path.strip() and not Path(path).is_absolute() and ".." not in Path(path).parts
        assert not any(c in path for c in "!*?[]#\\\n\r\t"), "Unsupported submodule spelling; do not reinterpret it as an ignore pattern"
        path = Path(path).as_posix()
        assert path != ".", "Submodule path must identify a strict subtree"
        excludes.append(path.rstrip("/") + "/")
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
identity_material = {"sources": inputs, "configuration_hashes": config_hashes, "excludes": sorted(set(excludes)), "gitignore": False, "graphify_revision": "16218bfc80d4ca2799734d045039f7ed1a5fa9fb", "mode": "utf8-python-markdown-structural-v1"}
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

Inspect the staged JSON against the corpus truth before publication: known caller→callee and document-reference endpoints, native source line locations, origin/confidence, unresolved-link diagnostics and edge folding (`also_seen`). Raw and built edge counts can differ because missing targets are omitted and same-endpoint evidence coalesces. A nonempty page node is not proof of every Markdown construct, parser syntax or model concept being represented. Native diagnostics are supporting evidence, not a replacement for source oracles. The block checks native inventory, selected bytes and in-scope native configuration before/after this build. This detects observed changes, not an atomic filesystem snapshot or change-and-revert race; use a quiescent source tree. Exported numeric confidence scores may be native category defaults (EXTRACTED=1, INFERRED=0.55, AMBIGUOUS=0.2), not measured probabilities. For portable mixed invalidation across dependency/schema/prompt changes, continue with the [freshness method](#freshness-portability-and-publication).

Use the project’s workflow to publish a reviewed complete trio together only when authorized. This slice does not copy over an existing published target. Preparation, parsing, exporter or validation failure leaves the old published references untouched and invalidates the new stage; retain the diagnostics and either fix the cause in a new task-owned stage or report the gap. Mixed updates, no-op policy, competing writers and compatible rollback use the bounded maintenance/publication method below.

For a bounded inspection of a known staged symbol, set `CONTEXT_SEED` to its verified unique node ID and `CONTEXT_QUESTION` to the actual question, then run this with the verified interpreter. The native loader reads the full JSON into its process; keep the agent-facing result bounded and use this only within the verified small-graph limit. The stage has no learning sidecar. Loading arbitrary published sidecars needs the separate scope checks described earlier.

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

Do not treat the query as a directional dependency path: native BFS/DFS gathers undirected context and may truncate to budget. Follow the displayed source locations to verify the fact. JSON/HTML/report file presence and this query do not prove browser rendering or a genuine agent-powered semantic pass.

## Capability and reuse decisions

All upstream pointers below refer to the immutable revision above. “Probe” means the runnable local [probe_graphify.py](probe_graphify.py); broader regression evidence belongs in the Issue handoff.

| Project need | Observed native facility and limit | Disposition / destination | Verification oracle |
|---|---|---|---|
| Whole-project understanding, scope and authority | Existing context/template own progressive source reading; Graphify does not establish project-specific authority | Retain and extend in sole SKILL and read/maintain/review; map explains interactions, not just paths | Documentary and mixed project questions; contradict graph/history with canonical source |
| Corpus inventory, exclusions, sensitive/unsupported inputs | `detect.detect`, ignore/config classification, `walk_errors`, `unclassified`, `skipped_sensitive`; output exclusion follows configured path | Reuse; maintain records actual included/omitted sources and reasons | Probe excludes vendor/generated/output; missing permission/type reported rather than “complete” |
| Code structure | `extract.extract(paths, root=..., cache_root=..., parallel=...)`; cross-file resolution and explicit `extracted_sources` | Reuse native parsers; no replacement engine | Probe exact caller→callee and tail/source locations; language-specific tests |
| Explicit documentary structure | `extractors.markdown.extract_markdown` through `extract()` handles pages, ATX headings, nesting, inline/reference destinations, wikilinks and fenced-block exclusion | Pass supported Markdown alongside code in native extraction; keep structural origin | Probe file-link/code-mention/Unicode/long-tail assertions; record unsupported Markdown syntax |
| Anchors and code hyperlinks | Markdown resolver strips fragments/queries, skips in-page anchors and ordinary hyperlinks to code/assets; missing targets may remain dangling; reference definitions are scanned even if unused | Source-check anchor/target validity and distinguish unresolved/unsupported from absent relationships; no anchor-validation claim | Probe valid/invalid anchor collapse and missing target; source-level negative truth set |
| Code↔document explicit mentions | `markdown_resolution.resolve_markdown_mentions`: path-qualified code spans → EXTRACTED; uniquely resolvable bare mentions → INFERRED 0.95; ambiguous names omitted | Reuse; read follows source and checks identity, direction and qualifier | `test_markdown_code_spans.py`; duplicate names and nonexistent cited path |
| Agent semantics without provider API | Upstream agent prompt/chunk/cache/build route exists; headless `extract` calls provider pipeline on documents and may auto-detect several ambient keys | Adapt extraction knowledge for active subscription agent, including bounded serial route; do not use headless semantic backend | Authored-fragment ingestion probe establishes interface only; genuine concept/negative/cross-file extraction remains a separate semantic test |
| Untrusted fragment ingestion | `semantic_cleanup.load_validated_semantic_fragment`; `validate.validate_extraction`; CLI `merge-chunks` | Reuse validators and merge, adding required coverage/source-accounting gate before mutation; flat glue only where native contract is insufficient | Probe rejects traversal ID; native merge still succeeds with 1 of 2 valid chunks, so exit 0 is insufficient |
| Node identity, direction, confidence and origin | `ids.make_id/normalize_id`, semantic rekey, `build_from_json(directed=True, dedup=False)`; `_origin` overrides location-shape inference | Reuse exact ID functions; store separate structural and semantic evidence and source locations | Probe caller direction, semantic L1 location/tier and JSON reload; schema/confidence tests |
| Structural/semantic coexistence | `build_merge` and `merge_raw_extraction` replace per source **and tier**; preserve other tier | Native merge with explicit root/provenance; no manual graph engine | Probe same-file AST refresh retains semantic node/edge; tier/hyperedge regressions |
| Cache and prompt identity | Native AST cache versions schema/grammars; semantic prompt namespace and partial markers; legacy semantic entries may still be accepted | Reuse reviewed current entries; reject unknown legacy vintage for strict coverage, requeue on prompt/model/profile change | Probe warm hit, prompt miss and fresh-process empty-cache miss |
| Changed code, deleted/renamed/excluded material | `watch._rebuild_code`, `detect_incremental`, tier-aware merge; rename = deletion + addition; update does not refresh document semantics | Reuse native bounded update only inside validated maintenance slice; requeue semantic dependents and inspect exclusions | `test_update_incremental.py`; source review distinguishes `.gitignore` full-path eviction from ordinary update |
| Tool/config/schema/prompt invalidation | Native build-state mismatch avoids fast skip, but per-file manifest can still filter unchanged files before extraction | Maintain compares full input/profile identity; force affected extraction selection on mismatch, preserving loss guards | Same bytes with changed prompt/config/tool/schema must invalidate; not proved by a manifest timestamp |
| Portable state / fresh checkout | Graph contains semantic evidence; ignored manifest/cache and absolute root markers may be absent | Prefer coverage/profile metadata within graph plus report; require full semantic re-extraction on cold adoption until changed-only reuse is proven | Probe empty cache misses; final clean-checkout test must not depend on local sidecars |
| Communities, hubs, bridges and impact | `cluster`, `score_all`, `analyze.god_nodes/surprising_connections`, `affected.affected_nodes`; heuristics/covered relations only | Useful scoped read/review methods; optional Leiden deferred | Matched known corpus questions; graph degree/impact is not architecture or runtime/test coverage |
| Scoped query/path/explain | Native CLI uses library traversal without requiring an MCP server. Query BFS/DFS is undirected context gathering; `path` handles direction separately | Reuse bounded native query functions and source follow-through; CLI writes a query stamp, so it does not satisfy strict read-only behavior | Direction/path/ambiguity/budget regressions; set explicit depth/budget when needed |
| Cross-repository investigation | `prefix_graph_for_global`, distinct repo tags, CLI merge; common external stubs unnamespaced; simple graph may collapse parallel/opposing facts | Opt-in G method with namespaces/version boundaries and separate writable output | Duplicate repo basenames and IDs, known direction, shared external type; not arbitrary inferred cross-repo relation discovery |
| Mandatory JSON/HTML/report trio | `export.to_json`, `exporters.html.to_html`, `report.generate`; individual writes, no complete-trio transaction | Reuse exporters into staging; validate set and input identity before publication under one writer | Probe real custom-path trio and relative paths; failure/rollback/coherence remains maintenance gate |
| HTML presentation | vis-network 9.1.6 from CDN with SRI; JavaScript/CDN availability required. Default 5000-node limit; explicit limit can aggregate, but <2 communities can skip output | Read/render check; aggregation must be disclosed and cannot silently satisfy missing HTML | Probe HTML contains CDN reference; script-breakout regression; actual browser rendering still required |
| GraphML and SVG | `to_graphml` preserves attributes with conversion but strips internal direction markers; `to_svg` adds plotting dependencies | Opt-in G exports; directed native graph required for directional GraphML, round-trip required for claims | Reopen GraphML / visually inspect SVG only when selected |
| Wiki / Obsidian | Native wiki community/hub articles and Obsidian managed per-node notes exist | Optional export for a demonstrated project need; never replace repository.md or default trio | Output/source/link correspondence and no overwrite of local authored notes |
| URL/Git clone / PDF/Office/images/video | Native ingest/conversion/transcription routes add retrieval, format and dependency requirements | Defer by corpus/task; existing source/adopted-project ownership still applies | Explicit selection, conversion provenance and coverage; no implied support from code/Markdown test |
| Hooks, watcher daemon, MCP, Cloud, DB pushes, memory feedback and automatic benchmarks | Upstream supports broader integration and stateful facilities | Not needed for baseline context; no automatic installation, credentials, subscription, background service or quantified-saving promise | Verify ordinary read/setup leaves instructions, hooks, keys and unrelated installations untouched |

### Upstream agent instructions that require adaptation

The reviewed Codex skill contains incompatible directions: serial fallback near Step 3 versus mandatory Agent/config-restart instructions in B2; fail-closed B2 versus partial-success B3; full-file rules versus coverage checks only for reported files. It also offers ambient Gemini fallback and global installation. Preserve the extraction knowledge, not these host assumptions or side effects. The headless CLI additionally auto-detects OpenAI/Anthropic/other providers (`cli.py` extraction backend selection); it does not use the current chat subscription merely because it runs from Codex/Work.

`merge-chunks` validates security/shape and skips invalid siblings. It does not preserve its input `coverage` objects and supplies numeric zero usage for missing counts. Capture/validate coverage and observable usage **before** native merge. Neither well-formed JSON, a successful command nor a reported line count alone proves that the model read and understood the complete source.

## Construction route

The selected route is CLI-first for supported commands, with direct native calls at the subscription, Markdown and strict-read gaps:

1. Resolve canonical repository root, scope, authoritative sources, task-owned output and immutable dependency profile. Inventory sources using native detection with explicit exclusions; account for unsupported, sensitive and unreadable inputs. Exclude generated references/graphs, staging/caches, unselected third-party/submodule content and secrets. Avoid symlink-following by default.
2. In a separate process set `GRAPHIFY_OUT` **before imports**. Use task-local staging/cache for builds and explicit export paths; for read commands select the published directory, e.g. `skills/context/references/graphify` relative to the project root. Absolute `GRAPHIFY_OUT` overrides cache-root placement. Do not switch it inside a long-lived imported process; native cache state also assumes one corpus per process.
3. Extract supported code **and Markdown** using `extract(files, root=root, cache_root=cache, parallel=False)` for a bounded serial host. Native parallel extraction requires an importable main module; stdin/`-c`/REPL on spawn hosts may fall back. Code-only CLI is available, but it drops document inputs and cannot establish documentary coverage.
4. The active subscription agent reads the selected semantic material and produces complete source-owned fragments. Parallelize only when permitted by delegation and the actual host; otherwise serially process the same bounded chunks. Return JSON to the coordinator; do not require worker filesystem writes or invented tool names. Never infer concepts from names alone.
5. Validate each expected chunk, source identity, source locations, coverage and confidence; reconcile cross-chunk endpoints against known IDs. Keep coverage separately before `graphify merge-chunks <explicit files> --out <staged semantic JSON>`. Do not glob stale results from an earlier run. Reuse native `build_from_json`/`build_merge(root=..., directed=True, dedup=False)` with structural `extracted_sources` and explicit semantic origin. Build merge returns a graph without writing; mutable input dictionaries need copies when reused.
6. Native cluster/cohesion/analysis helpers produce structural evidence; the current agent may name communities from actual members. Use native `to_json`, `to_html` and report generation against the same graph/inventory/labels, at explicit staging paths. Check actual return values and all three artifacts. Native report expects numeric usage; preserve unknown subscription usage explicitly in the report/graph metadata instead of presenting default zero counters as measurement.
7. For strict read-only investigation, use native loaders and traversal functions directly. CLI `query`, `path` and `explain` call `_touch_query_stamp` and attempt to create `cache/last_query_stamp` beside the queried graph; query logging is separately opt-in and can be disabled with process-local `GRAPHIFY_QUERY_LOG_DISABLE=1`. `serve._read_graph` plus `_query_graph_text` supplies bounded source-backed context without the CLI stamp (probe checks fixture bytes/inventory unchanged). The native loader also opportunistically reads a neighboring learning sidecar and may hash its referenced sources; that optional derived evidence is absent in this probe. Do not silently activate work-memory annotations: audit them within scope or use the native raw JSON/path loader and omit the in-memory learning overlay. Directional path/explain read alternatives and a present sidecar still need their own operation-specific no-write/scope checks; do not claim all CLI reads are inert.
8. Publication uses the project's existing workflow and a checked input identity. No second Graphify skill, router, service or package-vendoring layer is selected. The procedures above implement bounded initial structural and active-agent mixed staging. General maintenance/publication, broader investigation and host adoption still require their remaining gates before downstream deployment.

### Selected flat-helper boundary

Reuse native commands/libraries unchanged for parsing, IDs, graph assembly, cache, queries, analysis and export. Use **one flat validation helper**, [validate_context_fragments.py](validate_context_fragments.py), for the demonstrated native gap: validate the explicit expected shard set and each source's completed ranges/hash, provenance, origin and schema **before** any cache/merge/publication write. It calls native fragment/schema validation, rejects missing/invalid/unexpected shards and unsafe paths, and fails without changing last-good data. It validates file inventory/configuration with native ignore facilities; it does not implement extraction, graph traversal, provider access, installation or a second pipeline/dispatcher. Native code remains external; no upstream extraction specification is copied. The existing `probe_graphify.py` is only a reproducible compatibility check.

## Semantic evidence contract

<!-- context-semantic-contract:start -->

Retain the useful upstream schema: nodes carry ID, short label, file type, source file/location and pertinent source metadata; edges carry source→target, relation, source evidence, origin and confidence; hyperedges identify their members and source. Native file types are `code`, `document`, `paper`, `image`, `rationale`, `concept`. Normalize IDs using native `ids` and full root-relative path identity, preserving Unicode; labels alone are not globally unique. Use exact symbol IDs from structural extraction for code references. Rationale belongs on the relevant semantic record as an attribute, not a sentence-shaped entity.

Use EXTRACTED/1.0 for explicit evidence, INFERRED for a supported inference with a stated basis, and AMBIGUOUS for a real unresolved candidate. Upstream's inference rubric is 0.95/0.85/0.75/0.65/0.55 and ambiguity 0.1–0.3; scores are annotations, not calibrated probabilities. Do not invent a relation to make the corpus connected. A negative or unrelated example need not become an ambiguous edge. `calls` runs caller→callee and stays within the established language context.

Stamp semantic nodes **and edges** `_origin="semantic"`, including line-located documentary evidence; native legacy fallback otherwise interprets `L<number>` as AST. Keep independent semantic records when they must survive AST refresh. Metadata added solely to an AST-origin node can be replaced with that node. Preserve documentary links, code structure and model-derived relations as distinct evidence even when endpoints coincide; inspect native edge/evidence folding before claiming all parallel facts survived.

Bound both source count and content size. Upstream suggests <=20–25 files and about 6000 lines per chunk, with >2000-line text isolated. Treat these as upper bounds to reduce for dense material or actual host limits. For long documents, enumerate ordered line/byte ranges through EOF and attach source hashes and completed ranges; do not rely on one capped tool result. Keep one source identity across slices and reconcile cross-slice concepts after all slices complete. Missing, short, failed or malformed chunks leave coverage incomplete and cannot replace a complete prior semantic source group. Record the zero-concept/negative result explicitly in coverage: native semantic cache treats zero-node/zero-hyperedge output as a miss.

### Plan, read and reconcile subscription fragments

This semantic slice uses the active subscription agent's actual reading and reasoning. It has no inference command or provider client. In Codex use permitted agent tools under `delegation`; on a host without subagents the current agent processes the same bounded plan serially. Actual Windows/Work integration is still unverified. Do not infer concepts from filenames, use `graphify.llm`/headless provider extraction, require an invented Agent tool, restart clients, edit credentials or fall back to ambient keys.

1. Run the verified D preparation and fresh structural procedure. Keep its source root, source inventory and baseline JSON fixed. Select the semantic scope/formats explicitly; this lane covers UTF-8 Python/Markdown, not unread/unsupported binary/conversion inputs. Exclude outputs and secrets as in D. Prepare the independent plan **before** collecting results; do not infer expected work from successful returns.
2. This initial mixed profile plans **every source in the D baseline**, including explicit zero findings for irrelevant sources; a semantic subset cannot conceal stale structural input. It rechecks that complete baseline source set, bytes and in-scope configuration before/after assembly, conservatively refusing an inventory mismatch and requiring fresh D staging. This is initial-build coherence, not F incremental reuse. Plan JSON uses `schema` and `prompt_version` = `context-semantic-v1`, the pinned `graphify_revision`, nonempty `scope`, `structural_sha256` (full baseline artifact bytes), `sources` mapping root-relative POSIX paths to `{sha256, line_count}`, and `shards` = `[{id, ranges:[{source_file,start,end,sha256}]}]`. Hash source bytes unchanged. Decode UTF-8 with an optional BOM; count `splitlines(keepends=True)`; range hashes cover the decoded inclusive lines re-encoded as UTF-8, preserving line endings. Nonempty ranges are 1-based inclusive; an empty file has one `0..0` range/hash of empty bytes and can yield only a zero-findings receipt. Assigned ranges across all shards cover every planned source through EOF exactly once, without gaps/overlaps. Keep plans/results in task-owned storage, outside graph artifacts.
3. Bound actual source bytes as well as lines/files. The validator profile caps JSON/source files at 2 MiB, sources at100, shards at64, aggregate fragments at32 MiB and hyperedges at3 per shard; these are ceilings, not suggested agent workloads. Begin with a few short files and smaller ranges; isolate long text. Read each assigned range entirely using output limits that do not truncate it, paging until EOF. A hash, receipt, range total or successful tool call does not establish that the model understood the source. Inspect the actual output and pause/re-read a truncated/missing part. Do not emit complete coverage for partial reads.
4. Give a worker only the scope, assigned ranges, source/authority instructions, exact structural IDs it needs and this schema/rubric. Keep truth-set answers outside its view. Worker results can be returned as JSON in conversation; worker file writes are optional, never required by the model pipeline. The coordinator can save an exact response to an explicit task-owned file. Serial/no-subagent execution follows the identical schema, bounded reading and validation, without fabricating worker activity.
5. Each returned fragment has `schema`, `shard_id`, `status:"complete"`, `reader:{surface,model,usage:null}`, `receipts`, `nodes`, `edges`, `hyperedges` and `open_questions`. Record actual assigned/observable model provenance; use null when runtime identity or usage is not exposed. Each receipt repeats its assigned `{source_file,start,end,sha256}` exactly, then adds a meaningful reading `summary`, `outcome:"findings"|"zero-findings"` and `reason`. A zero-concept/unrelated source is a completed negative result, not a fabricated node or cache hit. A findings receipt must own an emitted record/question; empty graph arrays alone cannot substantiate it. Missing/failed/partial work stays incomplete; retry only the failed ranges, then revalidate the full explicit result set.
6. New nodes include `entity_key`, native `make_id(Path(source_file).with_suffix("").as_posix(), entity_key)`, short `label`, an allowed `file_type`, primary `source_file`, `source_location:"L3"|"L3-L7"`, `_origin:"semantic"` and `evidence`. A stable entity key describes the entity, never its chunk/sequence. Use full root-relative source identity and native Unicode normalization; don't duplicate an AST symbol as a semantic node. Link to its exact verified AST ID. Keep rationale/authority/claim status on the record where relevant. Retain current, superseded, observed and unresolved claims distinctly; a historical conflict does not override its current owner.
7. Evidence is a list of `{source_file,start,end,quote}` with exact complete decoded source lines (omit only final CR/LF). Primary evidence must be within the shard's assigned range and bounded record location. Other supporting sources must also be actually read and globally planned; additional reading does not claim ownership/complete coverage of their tier. Edges add `source`, `target`, a precise directed `relation`, `confidence`, `confidence_score` and a nonempty `rationale` for inference/ambiguity. INFERRED/AMBIGUOUS cross-source relations require anchors for both endpoint sources. EXTRACTED references may be stated in the referring source alone, with a separately verified target ID. Uncertain referents may be evidence-bearing `open_questions` (`question` plus primary source/location/origin/evidence) rather than speculative links. Do not turn unrelated text into ambiguity.
8. Reconcile all ranges and source-owned identities after reading. A relation from a later range may reference a real concept introduced earlier. Validate against the aggregate semantic+structural ID universe, not one shard in isolation. Preserve a unique explicit owner for each node; conflicting/duplicate definitions require source review and a reconciled response, not first-writer wins, automatic renaming or a chunk suffix. Re-read material sources when deciding cross-chunk equivalence; retain original returns privately for execution review and record meaningful corrections, without copying a transcript into project knowledge.
9. Optional hyperedges use the same evidence/confidence/origin fields plus `entity_key`, source-owned `id`, `label`, `nodes` (at least three distinct resolved members) and `relation`; use only if it captures a useful group beyond pairwise edges. Inferred/ambiguous groups need evidence for every member-source identity. The recorded semantic trials use pairwise edges; optional hyperedges still face the explicit native normalization/preservation check and may be refused. Every graph node, edge and hyperedge is explicitly semantic; line-like locations must not trigger AST-origin fallback. Existing structural evidence remains independently owned.

Use [validate_context_fragments.py](validate_context_fragments.py) with the verified interpreter before native assembly. It reads/parses/hashes the same bounded JSON buffer, rejects duplicate keys/nonfinite numbers/partial markers, calls native security/schema/ID facilities and rejects missing/unexpected/duplicate shards, planned/returned range defects, changed bytes, unsafe paths, bad anchors, origin/confidence errors, duplicate/AST IDs and unknown endpoints. It is read-only and returns validated semantic data plus its coverage ledger on stdout. It does **not** establish semantic relevance/understanding; source-backed trial answers and reviewer judgment remain necessary. It does not infer, repair, merge, cache or publish. This profile records subscription usage as null; adding measured-counter support requires actual host observations and a reviewed extension.

```sh
"$CONTEXT_PY" "$CONTEXT_TOOLS/validate_context_fragments.py" \
  --root "$CONTEXT_ROOT" --plan /absolute/task/plan.json \
  --structural /absolute/task/structural/artifacts/graph.json \
  --fragments /absolute/task/chunk-a.json /absolute/task/chunk-b.json
```

Native `validate_semantic_fragment` checks shape/security, not full coverage. Do not use `sanitize_semantic_fragment` in this route: the pinned implementation drops `concept`/`rationale` nodes and can filter cross-fragment hyperedges. Native `merge-chunks` skips invalid siblings, first-wins duplicate IDs, drops coverage and substitutes zero usage. This selected direct native assembly avoids that lossy boundary; a future command route must prove no partial/drop occurred rather than trust exit0.

The pinned native graph is simple directed storage: same-endpoint evidence can coalesce or lose distinct relations/origin. This slice **refuses semantic pairs already occupied by another semantic or structural edge** instead of silently losing independent facts. Rephrase/reify only when source meaning justifies a distinct entity, or report the unsupported collision; do not alter truth to make validation pass. Mixed updates use a fresh structural baseline under the maintenance method below: source ownership inferred solely from nodes is insufficient for edge-only or zero-finding replacement.

<!-- context-semantic-contract:end -->

### Assemble, interpret and verify a fresh mixed trio

Selected Python/Markdown bytes, paths and scoped configuration are checked against the full D baseline. D's unsupported/omitted-file inventory is retained as a labeled observation at structural staging; this semantic phase does not recertify every omitted-file change. Redo D staging when current whole-inventory evidence is needed.

Set `CONTEXT_PLAN`, `CONTEXT_STRUCTURAL` and `CONTEXT_FRAGMENTS` (a JSON array of explicit result paths) in a process with the same verified interpreter, root/tools and no-provider environment as D. `GRAPHIFY_OUT` must still point outside the source tree before imports. Set `CONTEXT_MIXED_STAGE` to a fresh external directory; do not select published output.

Run this block once without `CONTEXT_LABELS`: it validates and builds the graph natively in memory, then prints exact community members and identity without writing artifacts. The current agent reads those members, relevant source evidence and uncertainties and authors a task-local labels JSON: `{input_identity, evidence_identity, communities:{"<id>":{members:["<sorted IDs>"],label:"<short source-backed name>",rationale:"<why these members form this theme>"}}}`. Labels bind both current inputs and actual semantic payload evidence, in addition to exact members; changed claims/rationale can require new interpretation even with the same sources and IDs. Labels do not create project facts. Set `CONTEXT_LABELS` to that file and rerun the same block. Mismatched identity/membership forces inspection/relabeling, not guessed reuse.

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

Run without Python optimization so assembly assertions remain enabled. On any validator/build/export/evidence failure, discard this new stage, retain diagnostics and leave prior references untouched. The validated coverage ledger and interpretation are embedded in JSON/report; transient plans/results/caches stay task-local. Review actual semantic answers against source truth and bounded native queries before any authorized publication. Replaying recorded model fragments tests integration/accounting; only a real current-agent read constitutes a new semantic pass. Fresh-model inference is not byte-deterministic. Initial assembly alone does not publish; use the maintenance/publication checks below.

## Freshness, portability and publication

This lane supports validated **semantic-shard reuse** in the tested Linux Python/Markdown mixed profile. It does not rely on warm caches or infer freshness from HEAD. Unchanged input/policy/profile plus an intact trio is a no-op. Changes require a fresh FULL native D structural baseline and validated retained/new semantic fragments; changed-only structural parsing is not claimed. Native Markdown cache normalization and incomplete reference context make an unreviewed changed-file shortcut insufficient. Model inference is not byte-deterministic.

### Inspect and assess a previous immutable generation

Read all three prior artifacts from ONE resolved immutable Git commit into a new task-owned view. `validate_trio(view)` checks bounded parsing, the complete set, noncircular generation, JSON's final sibling hashes, actual embedded HTML data and report correspondence; it returns the exact bytes consumed. Corrupt/incomplete output must be recovered from a verified last-good commit or replaced by full extraction. Missing/legacy portable state cannot support reuse; never repair hashes to bless an unexplained partial graph.

The existing validator supplies read-only `profile(tools)`, `snapshot(root, exclusions, authority_sources, scope=...)`, `make_state(...)` and `assess_reuse(...)`. They inspect/return data, not inference, graph construction, caches, installation or publication. Native ignore/noise/sensitive facilities govern a bounded snapshot. Unreadable enumeration/source/type failures block refresh rather than becoming deletion. Source hashes/line counts, consumed configuration, scope/exclusions, authority inputs and visible unsupported paths are portable. Explicit native exclusion order is preserved (last matching rule wins); only earlier identical duplicates are removed. Known derived outputs are clamped at the end. Derived-tree/Git existence and local secret contents/presence are NOT inputs. Sensitive exclusion policy is recorded; a cold checkout need not contain `.env`. Pruned/excluded subtrees are policies, not exhaustive descendant listings.

The profile verifies installed pins and fingerprints the interpreter/platform, requirements, validator, schema/mode and explicitly marked extraction contract. Unknown native versions require compatibility work, not automatic upgrade. Observable reader assignment and unknown usage remain provenance. If the task selects another mode/model or additional extraction instructions, explicitly change scope/profile and requeue; unexposed runtime identity cannot be compared automatically.

Select current root/branch/worktree, scope, exclusions and global authority sources from project owners. Previous policies are an inspected starting point, not authority. Put every material common rule owner in `authority_sources`; retain actual generated/output/cache/submodule exclusions. Prepare a task-local policy JSON with `scope`, `exclusions`, `authority_sources` and any verified `confirmed_removals`.

```python
# context-assess-refresh
import importlib.util
import json
import os
from pathlib import Path
module = Path(os.environ["CONTEXT_TOOLS"]) / "validate_context_fragments.py"
spec = importlib.util.spec_from_file_location("context_refresh_validator", module)
validator = importlib.util.module_from_spec(spec)
spec.loader.exec_module(validator)
previous = validator.validate_trio(Path(os.environ["CONTEXT_PREVIOUS_TRIO"]))
state = previous["graph"]["graph"]["context"]["maintenance"]
policy = validator.strict_json(os.environ["CONTEXT_REFRESH_POLICY"])
current = validator.snapshot(Path(os.environ["CONTEXT_ROOT"]), policy["exclusions"], policy["authority_sources"], previous_sources=state["snapshot"]["sources"], scope=policy["scope"])
assessment = validator.assess_reuse(state, current, validator.profile(module.parent), confirmed_removals=policy.get("confirmed_removals", {}))
if assessment["status"] == "noop":
    validator.validate_trio(Path(os.environ["CONTEXT_PREVIOUS_TRIO"]), root=Path(os.environ["CONTEXT_ROOT"]), require_current=True)
print(json.dumps({"status": assessment["status"], "reasons": assessment["reasons"], "invalidated": assessment["invalidated"], "reusable_shard_ids": sorted(assessment["reusable"]), "required_removal_confirmations": assessment["required_removal_confirmations"]}, ensure_ascii=False))
```

A confirmation maps an old relative path to `{kind:"git"|"coordinator", previous_sha256:"<old source bytes>", evidence:"<verified deletion/rename evidence>"}`. Verify the evidence yourself: compare the old source commit and inspected current commit/path diff, including actual old/new rename paths. A string labeled git is not proof. A readable existing file excluded by a positive current rule is an exclusion, not deletion. Missing/unreadable/unsafe/unexplained disappearance blocks destructive completion; resolve it and preserve last-good data.

| Assessment | Required action |
|---|---|
| `noop` | Coherent intact trio and unchanged inputs/profile: keep exact bytes, no new model/parser/export/commit just because HEAD/date/cache/root changed. |
| `reuse_some` | Keep only returned original payloads/provenance; actually read/re-extract invalidated shards, then assemble against fresh D. |
| `reextract_all` | Legacy/incomplete state, changed membership/policy/configuration/profile or conservative dependencies: independently plan every CURRENT source. Old shard IDs do not define newly added work. |
| `blocked` | Resolve the reported access/removal/unknown gap; never fill failed fresh work with stale prior semantics. |

### Reuse only complete, valid semantic ownership

Portable state is inside `graph.context.maintenance`: version/snapshot/profile, original validated payloads and zero-result/reader/receipt provenance, raw-byte versus canonical-payload hashes, source dependencies and referenced semantic-owner shards. Existing JSON/report roles suffice; no fourth portable manifest or global store. State checksums detect corruption, not forged truth: use reviewed commit-pinned artifacts. Exported source names alone cannot reconstruct original fragment bytes or split ranges/edge-only/empty groups.

Default dependency is ALL selected sources. Narrow local reviews in the plan's `dependency_reviews` require actual complete bounded ownership: `{mode:"local", reviewed:true, ownership_complete:true, negative_or_global_comparison:false, sources:[...], reason:"<source-backed review>"}`. Include owned/evidence/endpoint sources and common authorities. Zero-findings, unresolved/corpus-wide negative comparisons and incomplete ownership stay all-source. Explicit local negative statements are not proof of corpus-wide absence; booleans do not replace human review.

Changed bytes invalidate every shard owning or depending on the WHOLE source, even if another assigned range changed. Propagate invalidation through referenced semantic owners to a fixed point. Added/deleted/excluded input or changed scope/config/schema/tool/prompt conservatively requeues all; rename is deletion+addition with source-based IDs re-read/re-keyed. Dependency evidence is a lower bound, not universal semantic dependency discovery.

The API returns eligible payloads for programmatic copying; show bounded summaries first, then load only needed records. Save retained `payload` to explicit task-owned files; preserve original reader/receipts, not a fabricated new read. Add `reuse_provenance` naming the prior commit/input/generation, original raw-fragment hash and canonical-payload hash. Newly serialized bytes have a NEW fragment hash. Preserve that distinction. Revalidate all retained/new results against the NEW D baseline.

Independently plan current full-source/range coverage before new extraction. Include `expected_profile` captured before dispatch, current `authority_sources` and reviewed dependency declarations. Keep old ranges only when whole sources are unchanged; changed long sources require all slices to EOF. Use current subscription agents or serial reading under E's method. Missing/failed/zero/edge-only results never borrow an old semantic layer to look complete. Reconsider community meaning after material changes; identical members do not prove unchanged labels.

Assemble on a fresh STRUCTURAL-ONLY baseline with the complete validated fragment set. Never mutate a previous mixed graph as an invalidation shortcut: native semantic replacement ownership comes from nodes; edge-only/zero re-extraction can leave old semantics, while `prune_sources` removes both tiers. Fresh D plus selected retained/new fragments clears obsolete semantic nodes naturally and preserves current structure. Native `graphify update` retains semantics but does not certify freshness.

### Seal complete artifacts and recover failures

Assembly stages native JSON/HTML/report externally, computes a noncircular graph/evidence generation ID, places its marker in HTML/report, hashes their FINAL bytes and writes sibling hashes into JSON LAST. JSON never hashes itself. `validate_trio` checks exact consumed buffers, data/counts, generation and portable-state integrity before use. Current source/profile/config/inventory is rechecked. These are quiescent-input checks, not filesystem snapshots or change-and-revert protection.

Export/interruption/corruption/truncation/partial model failures keep the prior published commit untouched. Retain diagnostics and build a NEW stage. Recover an intact last-good trio from one immutable commit and check compatibility with current intended sources/profile; otherwise label it stale and rebuild from sources. Do not silently promote an old graph to current truth.

Publication below is commit-atomic, not an atomic live-directory replacement. Readers resolve one commit and obtain its three blobs together in a new view before validation. Export-in-progress/worktree files are not certified generations. Rollback is an explicitly authorized NEW fast-forward commit containing a previous validated trio only if current sources/profile still match; never hard-reset remote history or erase later work. Incompatible old output remains historical evidence until repaired from current sources.

## Publish a validated trio from an isolated clone

Use an explicitly authorized remote URL and existing full branch ref, a clean task-owned clone at the expected source commit, and a fresh external stage. Publication updates only the remote ref, never the source clone's branch, index or worktree. A local destination must be bare; remote-side policy must prevent a nonlocal destination from updating a checked-out working tree. Native `_rebuild_lock(out_dir: Path, *, blocking: bool = False)` is advisory and only coordinates callers using the same clone/common-directory and ref convention; it does not automatically coordinate Graphify watch/update or other clones. The explicit Git lease arbitrates the latter.

The reviewed `validate_context_fragments.validate_trio(stage, root=root, require_current=True)` must return the final exact `blobs`, `digests`, `graph`, `input_identity`, `generation_identity`, `profile` and `snapshot` with `sources`, `configuration`, `exclusions` and `authority_sources`. It must validate current complete scoped source inventory, generation markers, source/profile identity, JSON sibling digests, provenance, embedded HTML/report counts, and all three files. The publisher consumes exactly those bytes, revalidates before push, and compares all tracked selected source/config bytes against the expected commit. This procedure requires every scoped source/config to be tracked. A failed validation, concurrent source change or failed lease refuses publication; unknown push outcome must be resolved by inspecting the remote before retry.

Set `CONTEXT_ROOT` to the isolated clone, `CONTEXT_STAGE` to the fresh stage outside the clone, `CONTEXT_TOOLS` to the reviewed helper directory, `CONTEXT_EXPECTED` to the full source commit, and `CONTEXT_REMOTE` / `CONTEXT_REMOTE_REF` to the explicit authorized remote URL and full existing `refs/heads/...` ref. Remote aliases are unsupported. Do not use a user checkout as the task-owned clone.

```python
# context-publish-trio
import fcntl
import hashlib
import importlib.util
import json
import os
from pathlib import Path, PurePosixPath
import subprocess
import sys
import tempfile
from urllib.parse import unquote, urlsplit
from graphify.watch import _rebuild_lock

assert __debug__ and sys.platform.startswith("linux")
assert not any(os.environ.get(k) for k in ("GIT_DIR", "GIT_WORK_TREE", "GIT_INDEX_FILE", "GIT_COMMON_DIR", "GIT_OBJECT_DIRECTORY", "GIT_ALTERNATE_OBJECT_DIRECTORIES", "GIT_REPLACE_REF_BASE"))
os.environ["GIT_NO_REPLACE_OBJECTS"] = "1"
os.environ["GIT_OPTIONAL_LOCKS"] = "0"
root = Path(os.environ["CONTEXT_ROOT"]).resolve(strict=True)
stage = Path(os.environ["CONTEXT_STAGE"]).resolve(strict=True)
expected, remote, ref = (os.environ[k] for k in ("CONTEXT_EXPECTED", "CONTEXT_REMOTE", "CONTEXT_REMOTE_REF"))
target = "skills/context/references/graphify"
names = ("graph.json", "graph.html", "GRAPH_REPORT.md")
assert root.is_dir() and stage.is_dir() and not stage.is_relative_to(root) and not root.is_relative_to(stage)
assert remote and not remote.startswith("-") and ref.startswith("refs/heads/")

def git(*args, data=None, env=None, check=True):
    return subprocess.run(["git", "-C", str(root), *args], input=data, stdout=subprocess.PIPE, stderr=subprocess.PIPE, env=env, check=check, timeout=60)

def text(*args):
    return git(*args).stdout.decode().strip()

git("check-ref-format", ref)
assert text("rev-parse", "--show-toplevel") == str(root)
assert expected == text("rev-parse", "--verify", expected + "^{commit}") == text("rev-parse", "HEAD")
assert not git("status", "--porcelain=v1", "--untracked-files=all").stdout, "Task clone is not clean"
parts = urlsplit(remote)
if not parts.scheme and ":" not in remote:
    local = (root / remote).resolve(strict=True)
elif parts.scheme == "file":
    assert parts.netloc in ("", "localhost") and not parts.query and not parts.fragment
    local = Path(unquote(parts.path)).resolve(strict=True)
else:
    local = None
if local is not None:
    probe = subprocess.run(["git", "-C", str(local), "rev-parse", "--is-bare-repository"], capture_output=True, check=False, timeout=60)
    assert probe.returncode == 0 and probe.stdout.strip() == b"true", "Local destination must be bare"
    remote = str(local)
common = Path(text("rev-parse", "--git-common-dir"))
common = (root / common).resolve(strict=True) if not common.is_absolute() else common.resolve(strict=True)
lock = common / "context-publish-locks" / hashlib.sha256(ref.encode()).hexdigest()
module = Path(os.environ["CONTEXT_TOOLS"]) / "validate_context_fragments.py"
spec = importlib.util.spec_from_file_location("context_publication_validator", module)
validator = importlib.util.module_from_spec(spec)
spec.loader.exec_module(validator)

def sha(data):
    return hashlib.sha256(data).hexdigest()

def validate():
    result = validator.validate_trio(stage, root=root, require_current=True)
    assert result["generation_identity"] and result["input_identity"] and result["profile"]
    assert set(result["blobs"]) == set(result["digests"]) == set(names)
    assert all(sha(result["blobs"][n]) == result["digests"][n] for n in names)
    return result

def tree_entry(path):
    raw = git("ls-tree", "-z", expected, "--", path).stdout
    if not raw:
        return None
    assert raw.count(b"\0") == 1
    head, actual = raw[:-1].split(b"\t", 1)
    mode, kind, oid = head.split(b" ")
    assert actual.decode() == path
    return mode, kind, oid.decode()

def verify_sources(result):
    for group in ("sources", "configuration"):
        for path, digest in result["snapshot"][group].items():
            p = PurePosixPath(path)
            assert not p.is_absolute() and p.as_posix() == path and all(x not in ("", ".", "..") for x in p.parts)
            item = tree_entry(path)
            assert item is not None and item[0] in (b"100644", b"100755") and item[1] == b"blob"
            assert sha(git("cat-file", "blob", item[2]).stdout) == digest, ("Source/config differs from commit", path)

def remote_tip():
    found = git("ls-remote", "--exit-code", "--refs", remote, ref).stdout.splitlines()
    assert len(found) == 1
    oid, name = found[0].split(b"\t")
    assert name.decode() == ref
    return oid.decode()

with _rebuild_lock(lock, blocking=True) as acquired:
    assert acquired, "Publication lock unavailable"
    first = validate()
    verify_sources(first)
    assert remote_tip() == expected, "Remote moved; rebuild/review against new tip"
    blobs = first["blobs"]
    for i in range(1, len(PurePosixPath(target).parts) + 1):
        prefix = str(PurePosixPath(*PurePosixPath(target).parts[:i]))
        item = tree_entry(prefix)
        assert item is None or item[:2] == (b"040000", b"tree"), ("Unsafe target ancestor", prefix)
    entries = git("ls-tree", "-r", "-z", expected, "--", target + "/").stdout.split(b"\0")
    placeholder = False
    for entry in (e for e in entries if e):
        head, path = entry.split(b"\t", 1)
        mode, kind, oid = head.split(b" ")
        name = path.decode().removeprefix(target + "/")
        assert mode == b"100644" and kind == b"blob" and name in (*names, ".gitkeep"), "Unexpected target content"
        if name == ".gitkeep":
            assert git("cat-file", "blob", oid.decode()).stdout == b"", "Nonempty placeholder"
            placeholder = True
    with tempfile.TemporaryDirectory(prefix="context-index-") as tmp:
        env = os.environ.copy()
        env["GIT_INDEX_FILE"] = str(Path(tmp) / "index")
        git("read-tree", expected, env=env)
        if placeholder:
            git("update-index", "--force-remove", "--", target + "/.gitkeep", env=env)
        for name in names:
            oid = git("hash-object", "-w", "--stdin", data=blobs[name]).stdout.decode().strip()
            git("update-index", "--add", "--cacheinfo", f"100644,{oid},{target}/{name}", env=env)
        tree = git("write-tree", env=env).stdout.decode().strip()
        changed = {p.decode() for p in git("diff-tree", "--no-commit-id", "--name-only", "-r", "-z", expected, tree).stdout.split(b"\0") if p}
        assert changed <= {target + "/" + n for n in (*names, ".gitkeep")}
        if not changed:
            assert validate() == first and not git("status", "--porcelain=v1", "--untracked-files=all").stdout, "Inputs changed; refuse no-op"
            assert remote_tip() == expected, "Remote moved; refuse no-op"
            print(json.dumps({"status": "unchanged", "commit": expected}))
        else:
            commit = git("commit-tree", tree, "-p", expected, data=b"Publish reviewed context graph trio\n").stdout.decode().strip()
            assert text("rev-parse", commit + "^") == expected
            for name in names:
                assert git("show", f"{commit}:{target}/{name}").stdout == blobs[name]
            assert validate() == first and not git("status", "--porcelain=v1", "--untracked-files=all").stdout, "Inputs changed; discard candidate"
            pushed = git("push", "--porcelain", f"--force-with-lease={ref}:{expected}", remote, f"{commit}:{ref}", check=False)
            if pushed.returncode:
                raise RuntimeError("Push failed or outcome uncertain; inspect remote ref before retry")
            print(json.dumps({"status": "published", "commit": commit, "parent": expected}))
```

Read all three blobs from one resolved immutable commit into a fresh view and verify JSON's generation and sibling digests. A checkout, mutable working directory or independently updated files are not an atomic trio. Pre-push errors can leave unreachable candidate objects, but cannot move the remote; a failed or timed-out push has uncertain outcome until the remote is inspected. Refusing a stale candidate is not a rollback; rollback is a separately reviewed compatible prior trio published as a new fast-forward commit.

## Verification corpus and oracles

[probe_graphify.py](probe_graphify.py) uses temporary, authored fixtures. It verifies isolated package identity; code/Markdown inventory and explicit exclusions; exact directed calls; path-qualified code mentions; document links with collapsed anchor fragments; skipped ordinary code hyperlinks; a Cyrillic heading; the tail after 2100 body lines; native agent-fragment validation/merge; staged JSON/HTML/report generation; no temporary absolute paths in the trio; directed reload; explicit semantic L1 origin retained after same-source AST refresh; prompt/source invalidation; a bounded native read query with unchanged fixture files; and an empty cache in a fresh process. Network and provider extraction are forbidden in the native in-process route; the merge subprocess also blocks socket connections. This is an ingestion feasibility test with an authored semantic fragment, not evidence of a completed agent-powered semantic pass or end-user browser rendering.

[probe_graphify_semantic.py](probe_graphify_semantic.py) replays explicitly recorded genuine active-model results from [graphify-semantic-cases.json](graphify-semantic-cases.json) through the strict validator and documented native assembly. It checks serial/parallel accounting, EOF/cross-range evidence, negative/uncertain/historical source roles, unknown usage, native tier retention, CLI failure and integrity controls. Replay is integration evidence, not a fresh model run or an independent semantic benchmark. For new extraction, give a current agent only the raw files, scope and method; keep recorded answers/truth controls outside its view.

[probe_graphify_maintenance.py](probe_graphify_maintenance.py) replays the source/model cases in [graphify-maintenance-cases.json](graphify-maintenance-cases.json), using the actual guide blocks and validator. It exercises add/edit/rename/delete/exclude, mixed and edge-only/zero replacements, conservative dependency propagation, ordered exclusions, input/profile changes, unchanged bytes, cold moved clones, distinct branches and linked worktrees. Real local bare Git remotes exercise coherent trio commits, independent-clone lease races, stale/dirty/nonbare/corrupt/partial refusal, a mutation before push, lost acknowledgement checked without retry, compatible fast-forward rollback and interrupted native HTML export. No hosted remote or live directory atomicity is certified. Fixtures record actual agent readings; replay makes no new model calls or blind semantic benchmark claim.

Run the three structural/semantic/maintenance probes with the verified environment's Python, without optimization. The maintenance probe uses fresh temporary repositories outside source by default. To retain inspectable evidence, set `CONTEXT_MAINTENANCE_EVIDENCE` to a new task-owned external directory; it refuses to overwrite an existing path. This is test evidence, not a fourth portable artifact or an installed orchestrator.

The continuing truth set must cover at least:

| Slice | Required question/scenario | Oracle and negative control |
|---|---|---|
| Map/read | What is this project for, how do components interact, who owns the constraint, where is current truth? | Direct source answers prepared before graph use; stale history contradicts current owner; map cannot copy whole documents |
| Structural/documentary | Who calls whom; what explicitly references a document/symbol; what is unsupported? | Exact endpoints, caller→callee, source line, EXTRACTED/INFERRED distinction; duplicate symbols, missing targets, bad/duplicate anchors, unused reference definitions, fenced code, links to code/assets, non-ASCII paths |
| Semantic | Which renewal/expiry concepts relate across unlinked code/docs and why? | Active model reads complete source ranges; inspectable evidence for each accepted relation; unrelated/conflicting/ambiguous and zero-concept cases; failed/missing/short chunk refuses complete publication |
| Maintenance | Add/edit/rename/delete/exclude mixed inputs, then change prompt/tool/config/schema with bytes unchanged | Expected tier removals/preservation and freshness flags; no accidental source/output indexing; cold checkout with no local cache; copied/moved root and distinct branches/worktrees |
| Publication | Export failure, corruption, truncation, partial prior run, competing writer, no-op | Last good trio retained; one verified input set; coherent publication and recovery; no host paths/secrets/cache logs in Git |
| Investigation | Scoped query, directional path, impact, community/bridge and source authority conflict | Known correct source answers, bounded output and ambiguity disclosure; connectivity is not runtime proof; compare direct-source and graph-assisted effort without invented saving percentages |
| Presentation/optional | HTML rendering/scale, selected GraphML/SVG/wiki/Obsidian/cross-repo use | Actual browser/network test; truthful aggregation; reopen selected formats; namespaces/version boundaries; parallel/directional loss visible |
| Host integration | Fresh agent receives only the skill/fixtures in actual Codex and Work host conditions | Real supported Windows/Linux execution, serial/no-subagent path, absent CLI/graph/network/optional asset and independent review; unavailable hosts remain gates, not simulated passes |

Keep pass chronology, exact test results, review findings and accepted summaries in the Issue. This source guide owns durable compatibility/method boundaries; generated graphs own relationship evidence; authoritative project documents own project facts.

## Source ledger

Precise implementation anchors within the selected revision (line numbers identify this revision only):

- [Agent workflow](https://github.com/Graphify-Labs/graphify/blob/16218bfc80d4ca2799734d045039f7ed1a5fa9fb/graphify/skill-codex.md), [extraction specification](https://github.com/Graphify-Labs/graphify/blob/16218bfc80d4ca2799734d045039f7ed1a5fa9fb/graphify/skills/codex/references/extraction-spec.md), [update reference](https://github.com/Graphify-Labs/graphify/blob/16218bfc80d4ca2799734d045039f7ed1a5fa9fb/graphify/skills/codex/references/update.md), [Windows variant](https://github.com/Graphify-Labs/graphify/blob/16218bfc80d4ca2799734d045039f7ed1a5fa9fb/graphify/skill-windows.md).
- [Package metadata](https://github.com/Graphify-Labs/graphify/blob/16218bfc80d4ca2799734d045039f7ed1a5fa9fb/pyproject.toml): runtime/extras, Python, entry point, licenses. `graphify/__main__.py` resolves installed version and dispatches CLI.
- [Detection](https://github.com/Graphify-Labs/graphify/blob/16218bfc80d4ca2799734d045039f7ed1a5fa9fb/graphify/detect.py): `detect` 2101, `save_manifest` 2757, separate tier hashes 2973, exclusions/deletions 3165, `detect_incremental` 3219.
- [Structural extraction](https://github.com/Graphify-Labs/graphify/blob/16218bfc80d4ca2799734d045039f7ed1a5fa9fb/graphify/extract.py): `extract` 10353, explicit origin 12331; [Markdown](https://github.com/Graphify-Labs/graphify/blob/16218bfc80d4ca2799734d045039f7ed1a5fa9fb/graphify/extractors/markdown.py): `_resolve_markdown_link` 311, `extract_markdown` 431; [mention resolver](https://github.com/Graphify-Labs/graphify/blob/16218bfc80d4ca2799734d045039f7ed1a5fa9fb/graphify/markdown_resolution.py); [shared IDs](https://github.com/Graphify-Labs/graphify/blob/16218bfc80d4ca2799734d045039f7ed1a5fa9fb/graphify/ids.py).
- [Build/merge](https://github.com/Graphify-Labs/graphify/blob/16218bfc80d4ca2799734d045039f7ed1a5fa9fb/graphify/build.py): `_is_ast_tier` 45, `build_from_json` 1524, `_tier_replacement_sources` 2485, `merge_raw_extraction` 2551, `build_merge` 2695, repo namespace 3209. [Semantic boundary](https://github.com/Graphify-Labs/graphify/blob/16218bfc80d4ca2799734d045039f7ed1a5fa9fb/graphify/semantic_cleanup.py): validation/security caps, source-aware sanitation; `validate.py` covers basic extraction schema, not complete evidence/coverage validation.
- [Cache](https://github.com/Graphify-Labs/graphify/blob/16218bfc80d4ca2799734d045039f7ed1a5fa9fb/graphify/cache.py): `cache_dir` 1030, `load_cached` 1069, `check_semantic_cache` 1393, `save_semantic_cache` 1539, `scope_semantic_result` 1843. [CLI](https://github.com/Graphify-Labs/graphify/blob/16218bfc80d4ca2799734d045039f7ed1a5fa9fb/graphify/cli.py): query stamp 1007 (call sites 2111/2553/2687), code update 3312, headless extract 4142/provider selection 4658, `merge-chunks` 5819, `merge-semantic` 5908. `llm.py` contains the provider pipeline; its `extract_corpus_parallel` is not selected for subscription extraction.
- [Maintenance](https://github.com/Graphify-Labs/graphify/blob/16218bfc80d4ca2799734d045039f7ed1a5fa9fb/graphify/watch.py): native lock 258, semantic/doc reconciliation 1167–1509, metadata guard 1769, build-state identity 1929–1970, HTML 2115, rebuild/incremental path 2241–2512, directed preservation 3073. [Paths](https://github.com/Graphify-Labs/graphify/blob/16218bfc80d4ca2799734d045039f7ed1a5fa9fb/graphify/paths.py): import-time output selector 39–53, individual atomic writes, native graph loaders.
- [Traversal](https://github.com/Graphify-Labs/graphify/blob/16218bfc80d4ca2799734d045039f7ed1a5fa9fb/graphify/serve.py): query 1490, undirected context walks 1436, directional path 2287–2530, source/confidence rendering 1168–1381. These functions also serve CLI calls; no MCP service is required. `affected.py` 302–388 owns bounded reverse impact; `analyze.py` owns graph differences (637), hubs and bridges; `cluster.py` owns Louvain/Leiden and cohesion.
- [JSON/other exports](https://github.com/Graphify-Labs/graphify/blob/16218bfc80d4ca2799734d045039f7ed1a5fa9fb/graphify/export.py): `to_json` 303, original-link preservation 414, graph metadata 506, Obsidian 792, GraphML 1333, SVG 1413; [HTML](https://github.com/Graphify-Labs/graphify/blob/16218bfc80d4ca2799734d045039f7ed1a5fa9fb/graphify/exporters/html.py): `to_html` 508, scale 538, escaping 715 and CDN 733; [report](https://github.com/Graphify-Labs/graphify/blob/16218bfc80d4ca2799734d045039f7ed1a5fa9fb/graphify/report.py): `generate` 111; `wiki.py` 306.
