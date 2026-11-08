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
import sys

from graphify.ids import make_id, normalize_id
from graphify.detect import ignored_predicate, _is_noise_dir, _is_sensitive
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


def strict_json(path, *, with_identity=False):
    body = read_bounded(path)
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
