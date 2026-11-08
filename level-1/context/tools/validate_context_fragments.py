"""Read-only pre-merge boundary for subscription-agent semantic evidence.

Original context integration code; native Graphify handles IDs/security/schema.
This validates submitted accounting/anchors, not whether a model understood text.
It does not extract, repair, merge, cache, install, query or publish anything.
"""
from __future__ import annotations

import argparse
import copy
import hashlib
import importlib.metadata as metadata
import json
import math
import os
from pathlib import Path
import re
import stat
import sys

from graphify.ids import make_id, normalize_id
from graphify.detect import ignored_predicate, _is_noise_dir, _is_sensitive, _is_installed_graphify_file, _find_vcs_root
from graphify.semantic_cleanup import validate_semantic_fragment
from graphify.validate import validate_extraction

SCHEMA = "context-semantic-v1"
REVISION = "16218bfc80d4ca2799734d045039f7ed1a5fa9fb"
MAX_BYTES = 2 * 1024 * 1024


def require(condition, message):
    if not condition:
        raise ValueError(message)


def sha(body):
    return hashlib.sha256(body).hexdigest()


def read_bounded(path):
    path = Path(path)
    require(path.is_file(), f"Missing JSON/source file: {path.name}")
    with path.open("rb") as stream:
        body = stream.read(MAX_BYTES + 1)
    require(len(body) <= MAX_BYTES, f"Oversized JSON/source: {path.name}")
    return body


def strict_json_bytes(body):
    require(len(body) <= MAX_BYTES, "Oversized JSON buffer")
    def pairs(items):
        result = {}
        for key, value in items:
            require(key not in result, f"Duplicate JSON key: {key}")
            result[key] = value
        return result
    def constant(value):
        raise ValueError(f"Nonfinite JSON number: {value}")
    def number(value):
        result = float(value)
        require(math.isfinite(result), "Nonfinite JSON number")
        return result
    value = json.loads(body.decode("utf-8"), object_pairs_hook=pairs, parse_constant=constant, parse_float=number)
    return value


def strict_json(path, *, with_identity=False):
    body = read_bounded(path)
    value = strict_json_bytes(body)
    return (value, {"sha256": sha(body), "size": len(body)}) if with_identity else value


def reject_partial(value):
    if isinstance(value, dict):
        require(not value.get("partial") and not value.get("_partial"), "Partial extraction marker contradicts complete coverage")
        for item in value.values():
            reject_partial(item)
    elif isinstance(value, list):
        for item in value:
            reject_partial(item)


def validate(root, plan_path, structural_path, fragment_paths):
    require(metadata.version("graphifyy") == "0.9.103", "Graphify version mismatch")
    origin = json.loads(metadata.distribution("graphifyy").read_text("direct_url.json") or "{}")
    require(origin.get("url") == "https://github.com/Graphify-Labs/graphify.git", "Unknown Graphify package source")
    require(origin.get("vcs_info", {}).get("commit_id") == REVISION, "Graphify revision mismatch")
    root = Path(root).resolve(strict=True)
    require(root.is_dir(), "Source root must be a directory")
    plan, plan_identity = strict_json(plan_path, with_identity=True)
    require(isinstance(plan, dict), "Plan must be a JSON object")
    require(plan.get("schema") == SCHEMA and plan.get("prompt_version") == SCHEMA and plan.get("graphify_revision") == REVISION, "Plan schema/prompt/profile mismatch")
    require(isinstance(plan.get("scope"), str) and plan["scope"].strip(), "Missing semantic scope")
    sources = plan.get("sources")
    require(isinstance(sources, dict) and 0 < len(sources) <= 100, "Invalid bounded source set")
    source_lines = {}
    def source_path(name):
        require(isinstance(name, str) and name and "\\" not in name and not Path(name).is_absolute() and ".." not in Path(name).parts and Path(name).as_posix() == name, "Unsafe/noncanonical source path")
        path = root / name
        require(path.resolve().is_relative_to(root) and path.is_file() and not path.is_symlink(), "Source escaped root or is not a regular file")
        return path
    for name, expected in sources.items():
        require(isinstance(expected, dict) and type(expected.get("line_count")) is int, "Invalid source identity schema")
        path = source_path(name)
        require(path.suffix.lower() in {".py", ".md"} and path.stat().st_size <= MAX_BYTES, "Unsupported/oversized semantic source")
        body = read_bounded(path)
        require(b"\x00" not in body, "Binary/NUL semantic source")
        lines = body.decode("utf-8-sig").splitlines(keepends=True)
        require(expected == {"sha256": sha(body), "line_count": len(lines)}, f"Source identity mismatch: {name}")
        source_lines[name] = lines
    structural, structural_identity = strict_json(structural_path, with_identity=True)
    require(plan.get("structural_sha256") == structural_identity["sha256"], "Structural artifact identity mismatch")
    require(structural.get("directed") is True, "Structural graph must be directed")
    context = structural.get("graph", {}).get("context", {})
    require(context.get("graphify_revision") == REVISION and context.get("semantic_extraction") == "not performed", "Expected verified D structural baseline")
    require(context.get("sources") == {n: s["sha256"] for n, s in sources.items()}, "Plan must cover the complete structural baseline source set")
    # Fresh initial assembly: verify all D inputs/configuration, not just successful semantic returns.
    ignored = ignored_predicate(root, extra_excludes=context["excludes"], gitignore=False)
    inventory, configs = set(), {}
    def walk_failure(error):
        raise error
    for directory, dirs, names in os.walk(root, followlinks=False, onerror=walk_failure):
        directory = Path(directory)
        dirs[:] = [n for n in dirs if not (directory / n).is_symlink() and not _is_noise_dir(n, directory) and not ignored(directory / n)]
        for name in names:
            path = directory / name
            if name == ".graphifyignore" or (directory == root and name in {".graphifyrc", ".gitmodules"}):
                require(not path.is_symlink() and path.stat().st_size <= MAX_BYTES, "Unsupported configuration")
                configs[path.relative_to(root).as_posix()] = sha(read_bounded(path))
            if path.suffix.lower() in {".py", ".md"} and not ignored(path) and not _is_sensitive(path) and path.is_file() and path.resolve().is_relative_to(root):
                inventory.add(path.relative_to(root).as_posix())
    require(configs == context["configuration_hashes"], "Structural configuration changed; redo D staging")
    require(inventory == set(sources), "Structural source inventory changed; redo D staging")
    structural_nodes = structural["nodes"]
    known = {n["id"]: n for n in structural_nodes}
    require(len(known) == len(structural_nodes), "Duplicate structural IDs")
    shards = plan.get("shards")
    require(isinstance(shards, list) and 0 < len(shards) <= 64, "Invalid bounded shard plan")
    expected_shards = {}
    planned_ranges = {n: [] for n in sources}
    fields = ("source_file", "start", "end", "sha256")
    def interval(record):
        name, start, end = record.get("source_file"), record.get("start"), record.get("end")
        require(name in sources and type(start) is int and type(end) is int, "Invalid source range")
        lines = source_lines[name]
        require((not lines and start == end == 0) or (1 <= start <= end <= len(lines)), "Range outside source/EOF")
        return name, start, end
    for shard in shards:
        require(isinstance(shard, dict), "Invalid planned shard object")
        sid = shard.get("id")
        require(isinstance(sid, str) and sid and sid not in expected_shards, "Duplicate/invalid planned shard")
        ranges = shard.get("ranges")
        require(isinstance(ranges, list) and 0 < len(ranges) <= 100, "Missing/big shard ranges")
        for item in ranges:
            require(isinstance(item, dict), "Invalid planned range object")
            require(set(item) == set(fields), "Unexpected range fields")
            name, start, end = interval(item)
            require(item["sha256"] == sha("".join(source_lines[name][max(start-1, 0):end]).encode("utf-8")), "Range content hash mismatch")
            planned_ranges[name].append((start, end))
        expected_shards[sid] = ranges
    for name, ranges in planned_ranges.items():
        next_line = 1 if source_lines[name] else 0
        for start, end in sorted(ranges):
            require(start == next_line, f"Planned coverage gap/overlap: {name}")
            next_line = end + 1
        require(next_line == len(source_lines[name]) + 1, f"Planned coverage misses EOF: {name}")
    require(0 < len(fragment_paths) <= 64 and len(set(map(str, fragment_paths))) == len(fragment_paths), "Invalid/duplicate fragment arguments")
    aggregate_bytes = 0
    combined = {"nodes": [], "edges": [], "hyperedges": []}
    coverage, questions, readers, fragment_hashes = {}, [], {}, {}
    pair_set = {(e["source"], e["target"]) for e in structural["links"]}
    ids = set(known)
    for path in fragment_paths:
        fragment, fragment_identity = strict_json(path, with_identity=True)
        aggregate_bytes += fragment_identity["size"]
        require(aggregate_bytes <= 16 * MAX_BYTES, "Aggregate fragments too large")
        reject_partial(fragment)
        require(not validate_semantic_fragment(copy.deepcopy(fragment)), "Native semantic security validation failed")
        sid = fragment.get("shard_id")
        require(fragment.get("schema") == SCHEMA and fragment.get("status") == "complete", "Incomplete/incompatible fragment")
        require(sid in expected_shards and sid not in coverage, "Unexpected/duplicate shard")
        receipts = fragment.get("receipts")
        require(isinstance(receipts, list) and [{k: r.get(k) for k in fields} for r in receipts] == expected_shards[sid], "Missing/short/changed range receipt")
        for receipt in receipts:
            require(receipt.get("outcome") in {"findings", "zero-findings"} and all(isinstance(receipt.get(k), str) and receipt[k].strip() for k in ("summary", "reason")), "Missing reading outcome/summary/reason")
        reader = fragment.get("reader")
        require(isinstance(reader, dict) and isinstance(reader.get("surface"), str) and reader["surface"].strip() and "usage" in reader, "Missing reader provenance/usage")
        require("model" in reader and (reader["model"] is None or isinstance(reader["model"], str) and reader["model"].strip()), "Missing/invalid model provenance")
        require(reader["usage"] is None, "This profile records unknown subscription usage as null; measured usage needs a separately reviewed extension")
        readers[sid], coverage[sid], fragment_hashes[sid] = reader, receipts, fragment_identity["sha256"]
        owned = expected_shards[sid]
        emitted = []
        def within(name, start, end):
            return any(r["source_file"] == name and r["start"] <= start <= end <= r["end"] for r in owned)
        def evidence(record):
            name = record.get("source_file")
            require(name in sources and record.get("_origin") == "semantic", "Invalid semantic source/origin")
            location = re.fullmatch(r"L([1-9][0-9]*)(?:-L?([1-9][0-9]*))?", str(record.get("source_location", "")))
            require(location is not None, "Missing bounded source location")
            start, end = int(location[1]), int(location[2] or location[1])
            require(within(name, start, end), "Record outside shard-owned ranges")
            emitted.append((name, start, end))
            anchors = record.get("evidence")
            require(isinstance(anchors, list) and 0 < len(anchors) <= 16, "Missing/big evidence anchors")
            primary = False
            for anchor in anchors:
                source, lo, hi = interval(anchor)
                quote = "".join(source_lines[source][lo-1:hi]).rstrip("\r\n")
                require(quote.strip() and anchor.get("quote") == quote, "Evidence quote mismatch/empty")
                if source == name and start <= lo <= hi <= end and within(source, lo, hi):
                    primary = True
            require(primary, "Primary record location lacks assigned evidence")
            for receipt in receipts:
                if receipt["outcome"] == "zero-findings":
                    require(not (name == receipt["source_file"] and receipt["start"] <= start <= end <= receipt["end"]), "Zero-findings receipt contradicts emitted record")
        for collection in ("nodes", "edges", "hyperedges"):
            require(isinstance(fragment.get(collection), list), f"Missing {collection} array")
            if collection == "hyperedges":
                require(len(fragment[collection]) <= 3, "Too many hyperedges")
            for record in fragment[collection]:
                evidence(record)
                if collection in {"nodes", "hyperedges"}:
                    key = record.get("entity_key")
                    require(isinstance(key, str) and key and normalize_id(key) == key, "Invalid stable entity key")
                    require(record.get("id") == make_id(Path(record["source_file"]).with_suffix("").as_posix(), key), "Noncanonical source-owned ID")
                    require(record["id"] not in ids, "Duplicate/structural identity collision; reconcile explicitly")
                    ids.add(record["id"])
                    require(isinstance(record.get("label"), str) and record["label"].strip(), "Missing label")
                if collection in {"edges", "hyperedges"}:
                    confidence, score = record.get("confidence"), record.get("confidence_score")
                    require(type(score) in (int, float) and math.isfinite(score), "Missing/nonfinite confidence score")
                    require((confidence == "EXTRACTED" and score == 1) or (confidence == "INFERRED" and score in (.95, .85, .75, .65, .55)) or (confidence == "AMBIGUOUS" and .1 <= score <= .3), "Invalid confidence rubric")
                    require(isinstance(record.get("relation"), str) and record["relation"].strip(), "Missing relation")
                    if confidence != "EXTRACTED":
                        require(isinstance(record.get("rationale"), str) and record["rationale"].strip(), "Inference/ambiguity lacks rationale")
                if collection == "edges":
                    pair = record.get("source"), record.get("target")
                    require(pair not in pair_set, "Endpoint-pair collision: native simple graph can discard independent evidence")
                    pair_set.add(pair)
                combined[collection].append(record)
        require(isinstance(fragment.get("open_questions", []), list), "Invalid open questions")
        for question in fragment.get("open_questions", []):
            evidence(question)
            require(isinstance(question.get("question"), str) and question["question"].strip(), "Empty open question")
            questions.append(question)
        for receipt in receipts:
            if receipt["outcome"] == "findings":
                require(any(n == receipt["source_file"] and receipt["start"] <= start <= end <= receipt["end"] for n, start, end in emitted), "Findings receipt has no owned finding/question")
    require(set(coverage) == set(expected_shards), "Missing expected shard")
    all_nodes = {**known, **{n["id"]: n for n in combined["nodes"]}}
    for edge in combined["edges"]:
        require(edge["source"] in all_nodes and edge["target"] in all_nodes, "Unresolved relationship endpoint")
        needed = {all_nodes[edge[k]]["source_file"] for k in ("source", "target")}
        if edge["confidence"] != "EXTRACTED":
            require(needed <= {a["source_file"] for a in edge["evidence"]}, "Cross-source inference lacks both endpoint sources")
    for hyperedge in combined["hyperedges"]:
        members = hyperedge.get("nodes")
        require(isinstance(members, list) and len(set(members)) == len(members) >= 3 and all(n in all_nodes for n in members), "Unknown/duplicate/short hyperedge membership")
        if hyperedge["confidence"] != "EXTRACTED":
            require({all_nodes[n]["source_file"] for n in members} <= {a["source_file"] for a in hyperedge["evidence"]}, "Cross-source hyperedge inference lacks member evidence")
    errors = validate_extraction({"nodes": list(all_nodes.values()), "edges": combined["edges"]})
    require(not errors, "Native extraction schema validation failed: " + str(errors))
    ledger = {"schema": SCHEMA, "prompt_version": SCHEMA, "graphify_revision": REVISION, "scope": plan["scope"], "sources": sources, "coverage": coverage, "readers": readers, "fragment_hashes": fragment_hashes, "plan_sha256": plan_identity["sha256"], "structural_sha256": plan["structural_sha256"], "usage": None, "open_questions": questions, "coverage_status": "complete for explicitly planned source ranges; model understanding requires source review"}
    return {**combined, "context_semantic": ledger}


MAINTENANCE_SCHEMA = "context-maintenance-v1"
CONTRACT_START = "<!-- context-semantic-contract:start -->"
CONTRACT_END = "<!-- context-semantic-contract:end -->"
REUSE_MAX_BYTES = MAX_BYTES


def _canonical(value):
    return json.dumps(value, sort_keys=True, ensure_ascii=False,
                      separators=(",", ":"), allow_nan=False).encode("utf-8")


def _digest(value):
    return sha(_canonical(value))


def _relative(name):
    require(isinstance(name, str) and name and "\\" not in name
          and not Path(name).is_absolute() and ".." not in Path(name).parts
          and Path(name).as_posix() == name and name != ".",
          "Expected canonical root-relative source path")
    return name


def profile(tools):
    """Fingerprint installed code/profile and explicitly marked extraction prose.

    Requires one marked contract in each of the operation and tool references.
    """
    tools = Path(tools)
    requirements = read_bounded(tools / "graphify-requirements.txt")
    dependencies = {}
    for raw in requirements.decode("utf-8").splitlines():
        if "==" in raw and not raw.startswith("#"):
            name, expected = raw.split("==", 1)
            observed = metadata.version(name)
            require(observed == expected, "Dependency profile mismatch: " + name)
            dependencies[name.casefold()] = observed
    dist = metadata.distribution("graphifyy")
    origin = json.loads(dist.read_text("direct_url.json") or "{}")
    require(dist.version == "0.9.103" and origin.get("url") ==
          "https://github.com/Graphify-Labs/graphify.git" and
          origin.get("vcs_info", {}).get("commit_id") == REVISION,
          "Graphify source profile mismatch")
    contracts = []
    for path in (tools.parent / "operations/graphify/build.md", tools / "graphify-build.md"):
        guide = read_bounded(path).decode("utf-8")
        require(guide.count(CONTRACT_START) == guide.count(CONTRACT_END) == 1,
              "Extraction contract requires exactly one explicit marker pair: " + str(path))
        start = guide.index(CONTRACT_START) + len(CONTRACT_START)
        end = guide.index(CONTRACT_END)
        require(end > start and guide[start:end].strip(), "Empty/reversed extraction contract: " + str(path))
        contracts.append(guide[start:end])
    result = {
        "schema": MAINTENANCE_SCHEMA, "fragment_schema": SCHEMA,
        "prompt_schema": SCHEMA,
        "mode": "utf8-python-markdown-structural-and-subscription-v1",
        "graphify_revision": REVISION,
        "graphify_version": dist.version,
        "python": {"implementation": sys.implementation.name,
                   "version": list(sys.version_info[:3]), "platform": sys.platform},
        "dependencies": dependencies,
        "requirements_sha256": sha(requirements),
        "validator_sha256": sha(read_bounded(tools / "validate_context_fragments.py")),
        "extraction_contract_sha256": sha(_canonical(contracts)),
    }
    return result


def snapshot(root, exclusions, authority_sources=(), *, previous_sources=(),
             scope="", derived_paths=("skills/context/references/graphify", "graphify-out")):
    """Read-only source/policy snapshot; failures raise and block refresh.

    gitignore=False is the accepted D lane. Explicit graph/submodule/output
    exclusions must be carried from D. Known derived subtrees are clamped
    lexically as well as with native ignore rules, including when absent.
    previous_status is evidence for assessment, not part of the input identity.
    Sensitive-file contents AND presence are outside portable input identity.
    """
    root = Path(root).resolve(strict=True)
    require(root.is_dir(), "Source root is not a directory")
    vcs_root = _find_vcs_root(root)
    require(vcs_root is None or vcs_root.resolve() == root, "Select canonical VCS root")
    require(isinstance(scope, str) and scope.strip(), "Explicit extraction scope required")
    require(isinstance(exclusions, (list, tuple)) and
          all(isinstance(x, str) for x in exclusions), "Invalid exclusion policy")
    derived = sorted({_relative(p.rstrip("/")) for p in derived_paths})
    hard = [p + "/" for p in derived]
    # Native rules are last-match-wins. Drop only earlier IDENTICAL duplicates;
    # preserve every other ordering decision, then clamp known derived outputs.
    seen, reversed_policy = set(), []
    for pattern in reversed(exclusions):
        if pattern not in seen and pattern not in hard:
            seen.add(pattern)
            reversed_policy.append(pattern)
    policy = list(reversed(reversed_policy)) + hard
    ignored = ignored_predicate(root, extra_excludes=policy, gitignore=False)

    def derived_path(path):
        rel = path.relative_to(root).as_posix()
        return any(rel == p or rel.startswith(p + "/") for p in derived)

    sources, line_counts, configs, unsupported = {}, {}, {}, []
    def walk_failure(error):
        raise ValueError("Unreadable filesystem walk; refresh blocked") from error
    for directory, dirs, names in os.walk(root, followlinks=False, onerror=walk_failure):
        directory = Path(directory)
        dirs[:] = [n for n in dirs if not (directory / n).is_symlink()
                   and not derived_path(directory / n)
                   and not _is_noise_dir(n, directory) and not ignored(directory / n)]
        for name in sorted(names):
            path = directory / name
            if name in {".git", ".gitignore", ".gitattributes", ".gitkeep"} or derived_path(path):
                continue
            rel = path.relative_to(root).as_posix()
            if name == ".graphifyignore" or (directory == root and name in {".graphifyrc", ".gitmodules"}):
                require(not path.is_symlink(), "Symlinked configuration requires separate review")
                configs[rel] = sha(read_bounded(path))
            if ignored(path) or _is_installed_graphify_file(path):
                continue
            # Never read secret bodies or persist sensitive-file presence.
            if _is_sensitive(path):
                continue
            # lstat does not turn an inaccessible/broken path into deletion.
            mode = path.lstat().st_mode
            if stat.S_ISLNK(mode) or not stat.S_ISREG(mode):
                if path.suffix.lower() in {".py", ".md"}:
                    raise ValueError("Unsafe selected source type: " + rel)
                unsupported.append(rel)
                continue
            if path.suffix.lower() not in {".py", ".md"}:
                unsupported.append(rel)
                continue
            body = read_bounded(path)
            require(b"\0" not in body, "NUL/binary selected source: " + rel)
            lines = body.decode("utf-8-sig").splitlines(keepends=True)
            sources[rel] = sha(body)
            line_counts[rel] = len(lines)
    require(0 < len(sources) <= 100, "Empty/oversized source inventory; refresh unsupported")
    authorities = sorted({_relative(p) for p in authority_sources})
    require(set(authorities) <= set(sources), "Authority sources must be selected, readable inputs")
    statuses = {}
    for name in previous_sources:
        _relative(name)
        if name in sources:
            statuses[name] = "selected"
            continue
        path = root / name
        try:
            parent = root
            for part in Path(name).parts[:-1]:
                parent = parent / part
                parent_mode = parent.lstat().st_mode
                require(not stat.S_ISLNK(parent_mode) and stat.S_ISDIR(parent_mode),
                      "Unsafe source ancestor")
            info = path.lstat()
            if not stat.S_ISREG(info.st_mode) or not path.resolve().is_relative_to(root):
                statuses[name] = "unsafe"
            elif derived_path(path) or ignored(path):
                # Positive live rules are exclusion evidence; sensitive guesses
                # and unsupported classifications are not deliberate removals.
                statuses[name] = "excluded"
            elif _is_sensitive(path):
                statuses[name] = "unexplained"
            else:
                with path.open("rb") as stream:
                    stream.read(1)
                statuses[name] = "unexplained"
        except ValueError:
            statuses[name] = "unsafe"
        except FileNotFoundError:
            statuses[name] = "missing"
        except OSError:
            statuses[name] = "unreadable"
    material = {"scope": scope, "sources": dict(sorted(sources.items())),
                "line_counts": dict(sorted(line_counts.items())),
                "configuration": dict(sorted(configs.items())),
                "exclusions": policy, "derived_paths": derived, "gitignore": False,
                "authority_sources": authorities,
                "unsupported": sorted(unsupported),
                "sensitive_policy": "native-sensitive-files-excluded-presence-and-content-v1"}
    return {**material, "identity": _digest(material), "previous_status": statuses}


def make_state(current_snapshot, current_profile, fragments, structural_nodes,
               validated_ledger, dependency_reviews=None):
    """Pack canonical ORIGINAL E-validated fragments into graph.context.maintenance.

    fragments: {shard_id: {payload: original parsed JSON, origin_sha256: raw hash}}.
    validated_ledger is the successful E context_semantic ledger for this set.
    Local declarations are human-reviewed assertions, never inferred by this code.
    """
    dependency_reviews = dependency_reviews or {}
    require({n: s["sha256"] for n, s in validated_ledger["sources"].items()}
          == current_snapshot["sources"], "E/snapshot sources differ")
    require({n: s["line_count"] for n, s in validated_ledger["sources"].items()}
          == current_snapshot["line_counts"], "E/snapshot line counts differ")
    require(validated_ledger["scope"] == current_snapshot["scope"], "E/snapshot scope differs")
    require(set(fragments) == set(validated_ledger["coverage"]), "Incomplete validated fragment set")
    node_sources = {n["id"]: n.get("source_file") for n in structural_nodes}
    owners = {}
    for sid, item in fragments.items():
        payload = item["payload"]
        require(payload["shard_id"] == sid and payload["status"] == "complete" and
              payload["schema"] == SCHEMA, "Invalid validated fragment identity")
        require(item["origin_sha256"] == validated_ledger["fragment_hashes"][sid] and
              payload["receipts"] == validated_ledger["coverage"][sid] and
              payload["reader"] == validated_ledger["readers"][sid], "E fragment provenance differs")
        require(len(_canonical(payload)) <= REUSE_MAX_BYTES, "Portable fragment exceeds bound")
        for node in payload["nodes"]:
            require(node["id"] not in node_sources, "Duplicate source-owned semantic ID")
            node_sources[node["id"]] = node["source_file"]
            owners[node["id"]] = sid
    groups = {}
    all_sources = set(current_snapshot["sources"])
    for sid, item in fragments.items():
        payload = item["payload"]
        dependencies = {r["source_file"] for r in payload["receipts"]}
        references, incomplete = set(), False
        records = [r for key in ("nodes", "edges", "hyperedges", "open_questions")
                   for r in payload.get(key, [])]
        for record in records:
            dependencies.add(record["source_file"])
            dependencies.update(a["source_file"] for a in record.get("evidence", []))
        for record in payload["edges"] + payload["hyperedges"]:
            endpoints = [record["source"], record["target"]] if "source" in record else record["nodes"]
            for endpoint in endpoints:
                source = node_sources.get(endpoint)
                if source in all_sources:
                    dependencies.add(source)
                else:
                    incomplete = True
                if endpoint in owners and owners[endpoint] != sid:
                    references.add(owners[endpoint])
        dependencies.update(current_snapshot["authority_sources"])
        require(dependencies <= all_sources, "Unknown shard dependency source")
        review = dependency_reviews.get(sid, {})
        local = review.get("mode") == "local"
        if local:
            require(review.get("reviewed") is True and review.get("ownership_complete") is True
                  and review.get("negative_or_global_comparison") is False
                  and isinstance(review.get("reason"), str) and review["reason"].strip()
                  and not incomplete and not payload.get("open_questions")
                  and not any(r["outcome"] == "zero-findings" for r in payload["receipts"]),
                  "Local dependency declaration is not sufficiently reviewed/bounded")
            declared = set(review.get("sources", []))
            require(dependencies <= declared <= all_sources, "Local declaration omits proven dependencies")
            dependencies = declared
        else:
            dependencies = all_sources
        groups[sid] = {"payload": copy.deepcopy(payload),
                       "origin_sha256": item["origin_sha256"],
                       "payload_sha256": _digest(payload),
                       "dependency_mode": "reviewed-local" if local else "all-sources",
                       "dependency_review": copy.deepcopy(review) if local else None,
                       "sources": sorted(dependencies), "owner_shards": sorted(references)}
    material = {"schema": MAINTENANCE_SCHEMA, "profile": copy.deepcopy(current_profile),
                "snapshot": {k: copy.deepcopy(v) for k, v in current_snapshot.items()
                             if k != "previous_status"},
                "groups": groups}
    return {**material, "integrity_sha256": _digest(material)}


def assess_reuse(previous, current_snapshot, current_profile, *, confirmed_removals=None):
    """Assess portable semantic reuse only; never remove/merge/write anything.

    previous is graph.context.maintenance (not an entire graph). Missing-source
    confirmation is {path:{kind:'coordinator'|'git', evidence:nonempty text,
    previous_sha256:...}}. A git label is not proof; the coordinator must verify it.
    Returned reusable payloads retain ORIGINAL reader/receipt provenance; they
    must be revalidated by E against a new plan/native D baseline before assembly.
    """
    confirmed_removals = confirmed_removals or {}
    def result(status, reasons, invalidated=(), reusable=None, required=()):
        return {"status": status, "reasons": reasons,
                "invalidated": sorted(invalidated), "reusable": reusable or {},
                "required_removal_confirmations": sorted(required)}
    if not isinstance(current_snapshot, dict) or not current_snapshot.get("sources"):
        return result("blocked", ["No successful current source snapshot"])
    if not isinstance(previous, dict) or previous.get("schema") != MAINTENANCE_SCHEMA:
        return result("reextract_all", ["Legacy/missing portable maintenance schema"])
    try:
        material = {k: v for k, v in previous.items() if k != "integrity_sha256"}
        require(previous.get("integrity_sha256") == _digest(material), "Portable state integrity mismatch")
        old = previous["snapshot"]
        groups = previous["groups"]
        require(groups and all(g["payload_sha256"] == _digest(g["payload"])
                            for g in groups.values()), "Portable shard payload integrity mismatch")
        require(all(set(g["sources"]) <= set(old["sources"]) and
                  set(g["owner_shards"]) <= set(groups) for g in groups.values()),
              "Malformed portable dependencies")
    except (KeyError, TypeError, ValueError, OverflowError):
        return result("reextract_all", ["Malformed/incomplete portable state; no reuse"])
    lost = set(old["sources"]) - set(current_snapshot["sources"])
    missing, unknown = [], []
    for name in sorted(lost):
        status = current_snapshot.get("previous_status", {}).get(name)
        if status == "missing":
            confirmation = confirmed_removals.get(name, {})
            if not (confirmation.get("kind") in {"coordinator", "git"}
                    and isinstance(confirmation.get("evidence"), str)
                    and confirmation["evidence"].strip()
                    and confirmation.get("previous_sha256") == old["sources"][name]):
                missing.append(name)
        elif status != "excluded":
            unknown.append(name)
    if missing or unknown:
        return result("blocked", ["Unconfirmed missing source" if missing else "Unexplained/unreadable source disappearance"],
                      required=missing)
    policy_keys = ("scope", "configuration", "exclusions", "derived_paths",
                   "gitignore", "authority_sources", "unsupported", "sensitive_policy")
    if previous.get("profile") != current_profile or any(old.get(k) != current_snapshot.get(k) for k in policy_keys):
        return result("reextract_all", ["Profile/scope/configuration/inventory policy changed"], groups)
    if set(old["sources"]) != set(current_snapshot["sources"]):
        return result("reextract_all", ["Selected source added/deleted/excluded"], groups)
    changed = {name for name in old["sources"]
               if old["sources"][name] != current_snapshot["sources"][name]}
    invalidated = {sid for sid, group in groups.items() if changed & set(group["sources"])}
    while True:
        more = {sid for sid, group in groups.items()
                if set(group["owner_shards"]) & invalidated}
        if more <= invalidated:
            break
        invalidated |= more
    retained = {sid: copy.deepcopy(group) for sid, group in groups.items() if sid not in invalidated}
    if not changed:
        return result("noop", ["Same selected inputs, policy and extraction profile"], reusable=retained)
    return result("reextract_all" if not retained else "reuse_some",
                  ["Changed sources: " + ", ".join(sorted(changed))], invalidated, retained)

def generation_identity(graph):
    """Noncircular graph/evidence identity before final sibling digests."""
    content = copy.deepcopy(graph)
    context = content.get("graph", {}).get("context", {})
    context.pop("generation_identity", None)
    context.pop("artifacts", None)
    return sha(json.dumps(content, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False).encode("utf-8"))


def validate_trio(stage, *, root=None, require_current=False):
    """Validate one complete immutable view and return its exact consumed bytes."""
    stage = Path(stage)
    require(stage.is_dir() and not stage.is_symlink(), "Trio must be a real directory")
    names = {"graph.json", "graph.html", "GRAPH_REPORT.md"}
    require({p.name for p in stage.iterdir()} == names, "Incomplete/unexpected trio contents")
    require(all(not (stage / n).is_symlink() for n in names), "Symlinked trio artifacts refused")
    blobs = {n: read_bounded(stage / n) for n in names}
    graph = strict_json_bytes(blobs["graph.json"])
    context = graph.get("graph", {}).get("context", {})
    require(graph.get("directed") is True and isinstance(context, dict), "Invalid directed graph context")
    generation = context.get("generation_identity")
    require(isinstance(generation, str) and generation == generation_identity(graph), "Graph generation identity mismatch")
    require(context.get("artifacts") == {n: sha(blobs[n]) for n in ("graph.html", "GRAPH_REPORT.md")}, "Trio sibling digest mismatch")
    marker = "<!-- context-generation:" + generation + " -->"
    html, report = blobs["graph.html"].decode("utf-8"), blobs["GRAPH_REPORT.md"].decode("utf-8")
    require(html.count(marker) == report.count(marker) == 1, "Missing/ambiguous trio generation marker")
    nodes, edges = graph.get("nodes"), graph.get("links")
    require(isinstance(nodes, list) and nodes and isinstance(edges, list), "Missing graph records")
    ids = {n["id"] for n in nodes}
    require(len(ids) == len(nodes) and all(e["source"] in ids and e["target"] in ids for e in edges), "Invalid graph endpoint identity")
    require(not validate_extraction({"nodes": nodes, "edges": edges}), "Invalid graph extraction schema")
    def embedded(name):
        prefix = "const " + name + " = "
        require(html.count(prefix) == 1, "Missing/ambiguous HTML graph data")
        return json.JSONDecoder().raw_decode(html.split(prefix, 1)[1])[0]
    hnodes, hedges = embedded("RAW_NODES"), embedded("RAW_EDGES")
    require(len(hnodes) == len(nodes) and {n["id"] for n in hnodes} == ids, "HTML/JSON node mismatch")
    require(sorted((e["from"], e["to"], e["label"], e["confidence"]) for e in hedges) == sorted((e["source"], e["target"], e.get("relation", ""), e.get("confidence", "EXTRACTED")) for e in edges), "HTML/JSON edge mismatch")
    require(f'{len(nodes)} nodes · {len(edges)} edges' in report and f'{len(nodes)} nodes &middot; {len(edges)} edges' in html, "Trio count mismatch")
    require("Input identity: `" + context["input_identity"] + "`" in report, "Report/input identity mismatch")
    require("Subscription-agent token usage: unknown" in report and "- Token cost:" not in report, "Unknown usage misrepresented")
    state = context.get("maintenance")
    require(isinstance(state, dict) and state.get("schema") == "context-maintenance-v1", "Missing portable maintenance state")
    require(state.get("snapshot") and state.get("profile"), "Missing portable source/profile identity")
    require(state.get("integrity_sha256") == _digest({k: val for k, val in state.items() if k != "integrity_sha256"}), "Portable state integrity mismatch")
    require(context.get("community_evidence_identity") == _digest({"structural_sha256": context["semantic"]["structural_sha256"], "groups": state["groups"]}), "Community interpretation evidence identity mismatch")
    require(context["input_identity"] == _digest({"snapshot": state["snapshot"], "profile": state["profile"]}), "Portable input identity mismatch")
    if require_current:
        require(root is not None, "Current source root required")
        require(profile(Path(__file__).resolve().parent) == state["profile"], "Published tool/prompt profile is incompatible")
        old = state["snapshot"]
        current = snapshot(root, old["exclusions"], old["authority_sources"], scope=old["scope"], derived_paths=old["derived_paths"])
        require({k: val for k, val in current.items() if k != "previous_status"} == old, "Current source/configuration/inventory differs from staged trio")
    return {"graph": graph, "blobs": blobs, "input_identity": context["input_identity"], "generation_identity": generation, "snapshot": state["snapshot"], "profile": state["profile"], "digests": {n: sha(body) for n, body in blobs.items()}}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", required=True)
    parser.add_argument("--plan", required=True)
    parser.add_argument("--structural", required=True)
    parser.add_argument("--fragments", nargs="+", required=True)
    args = parser.parse_args()
    try:
        result = validate(args.root, args.plan, args.structural, args.fragments)
    except (ValueError, OSError, TypeError, KeyError, RecursionError) as error:
        print(f"Semantic evidence refused: {error}", file=sys.stderr)
        return 1
    print(json.dumps(result, ensure_ascii=False, allow_nan=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
