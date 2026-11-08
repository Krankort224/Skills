"""Bounded Pass-B interface probes, not a project build/maintenance command.

Run with the isolated, pinned Graphify interpreter. All fixtures/cache/outputs
are temporary; network attempts and provider extraction fail the probe.
The authored semantic fragment checks ingestion, not semantic model quality.
"""
from __future__ import annotations

import copy
import importlib.metadata
import json
import os
from pathlib import Path
import socket
import subprocess
import sys
import tempfile


def main() -> None:
    if not __debug__:
        raise SystemExit("Run without -O: this probe uses assertions")
    assert importlib.metadata.version("graphifyy") == "0.9.103"
    distribution = importlib.metadata.distribution("graphifyy")
    origin = json.loads(distribution.read_text("direct_url.json") or "{}")
    assert origin.get("vcs_info", {}).get("commit_id") == "16218bfc80d4ca2799734d045039f7ed1a5fa9fb", origin
    assert origin.get("url") == "https://github.com/Graphify-Labs/graphify.git", origin
    requirements = Path(__file__).with_name("graphify-requirements.txt").read_text(encoding="utf-8")
    for requirement in requirements.splitlines():
        if "==" in requirement and not requirement.startswith("#"):
            name, expected = requirement.split("==", 1)
            assert importlib.metadata.version(name) == expected, requirement
    with tempfile.TemporaryDirectory(prefix="graphify-profile-") as temporary:
        base = Path(temporary)
        root = base / "corpus"
        cache = base / "cache"
        output = base / "stage" / "references" / "graphify"
        root.mkdir()
        output.mkdir(parents=True)
        # Set before importing graphify: its output/cache selector is import-time.
        os.environ["GRAPHIFY_OUT"] = str(cache)
        os.environ["GRAPHIFY_BACKEND"] = "none"
        attempts = []

        def no_network(*args, **kwargs):
            attempts.append("network")
            raise AssertionError("network is forbidden in this probe")

        socket.socket.connect = no_network
        socket.create_connection = no_network
        from graphify import llm
        llm.extract_corpus_parallel = no_network
        llm._call_llm = no_network
        from graphify.build import build_from_json, build_merge
        from graphify.cluster import cluster, score_all, label_communities_by_hub
        from graphify.detect import detect
        from graphify.extract import extract
        from graphify.export import to_json
        from graphify.exporters.html import to_html
        from graphify.analyze import god_nodes, surprising_connections, suggest_questions
        from graphify.paths import load_node_link_graph
        from graphify.serve import _read_graph, _query_graph_text
        from graphify.report import generate
        from graphify.semantic_cleanup import load_validated_semantic_fragment
        from graphify.cache import save_semantic_cache, check_semantic_cache

        corpus = {
            "src/lease.py": "def renew(age):\n    return age <= 7\n\ndef authorize(age):\n    return renew(age)\n",
            "docs/policy.md": "# Lease policy\n\nA successful renewal restarts the seven-day access window.\n## Expiry\nExpiry closes access.\n",
            "docs/guide.md": "# Guide\nSee [policy](policy.md#expiry), [bad anchor](policy.md#absent).\nSee [missing](missing.md), [ref][p].\n[p]: policy.md\nSee `src/lease.py::renew` and `authorize()`.\n[code file](../src/lease.py)\n[external](https://example.invalid)\n[#local](#guide)\n",
            "docs/Данные.md": "# Связи\n[Политика](policy.md#expiry)\n",
            "docs/long.md": "# Long document\n" + "Repeated body line.\n" * 2100 + "## Tail marker\n",
            "excluded/vendor.py": "def excluded(): pass\n",
            "generated/derived.md": "# Generated output\n",
            "references/graphify/old.md": "# Must not be indexed\n",
        }
        for name, body in corpus.items():
            path = root / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(body, encoding="utf-8")
        detection = detect(root, extra_excludes=["excluded/**", "generated/**", "references/graphify/**"], cache_root=cache, gitignore=False)
        files = [Path(p) for category in ("code", "document") for p in detection["files"].get(category, [])]
        inventory = sorted(p.relative_to(root).as_posix() for p in files)
        assert inventory == sorted(k for k in corpus if not k.startswith(("excluded/", "generated/", "references/"))), inventory
        ast = extract(files, root=root, cache_root=cache, parallel=False)
        assert all(n.get("_origin") == "ast" for n in ast["nodes"])
        assert any(n["label"] == "Tail marker" for n in ast["nodes"])
        assert any(n["label"] == "Связи" for n in ast["nodes"])
        locations = {n["id"]: n["source_location"] for n in ast["nodes"]}
        assert locations["src_lease_renew"] == "L1"
        assert locations["src_lease_authorize"] == "L4"
        assert next(n["source_location"] for n in ast["nodes"] if n["label"] == "Tail marker") == "L2102"
        assert any(e["relation"] == "calls" and e["source"] == "src_lease_authorize" and e["target"] == "src_lease_renew" for e in ast["edges"])
        assert any(e["relation"] == "references" and e["target"] == "src_lease_renew" for e in ast["edges"])
        # Document links collapse fragments to a file node: this is NOT anchor validation.
        policy_refs = [e for e in ast["edges"] if e["source"] == "docs_guide" and e["target"] == "docs_policy" and e["relation"] == "references"]
        assert len(policy_refs) == 1, policy_refs
        assert not any(e["relation"] == "references" and e["source"] == "docs_guide" and e["target"] == "src_lease" for e in ast["edges"])

        semantic = {
            "nodes": [{"id": "src_lease_access_window", "label": "Access window", "file_type": "concept", "source_file": "src/lease.py", "source_location": "L1", "_origin": "semantic"}],
            "edges": [{"source": "src_lease_access_window", "target": "src_lease_renew", "relation": "implemented_by", "confidence": "INFERRED", "confidence_score": 0.85, "source_file": "src/lease.py", "source_location": "L1-L2", "_origin": "semantic"}],
            "hyperedges": [], "coverage": {"src/lease.py": 5},
        }
        chunk = base / "chunk.json"
        chunk.write_text(json.dumps(semantic), encoding="utf-8")
        checked, errors = load_validated_semantic_fragment(chunk)
        assert not errors, errors
        merged_chunk = base / "merged.json"
        runner = "import socket,sys; socket.socket.connect=lambda *a,**k: (_ for _ in ()).throw(RuntimeError('network forbidden')); from graphify.__main__ import main; sys.argv=['graphify']+sys.argv[1:]; main()"
        child_env = {k: v for k, v in os.environ.items() if not any(word in k.upper() for word in ("API_KEY", "TOKEN", "SECRET", "PASSWORD", "PROVIDER", "AWS_", "GOOGLE_", "GEMINI_", "OPENAI_", "ANTHROPIC_"))}
        child_env["GRAPHIFY_BACKEND"] = "none"
        result = subprocess.run([sys.executable, "-c", runner, "merge-chunks", str(chunk), "--out", str(merged_chunk)], env=child_env, capture_output=True, text=True, timeout=30)
        assert result.returncode == 0, result.stderr
        sem = json.loads(merged_chunk.read_text(encoding="utf-8"))
        assert len(sem["nodes"]) == 1
        invalid_chunk = base / "invalid.json"
        invalid_chunk.write_text(json.dumps({"nodes": [{"id": "../../escape"}], "edges": []}), encoding="utf-8")
        assert load_validated_semantic_fragment(invalid_chunk)[1]
        partial_merge = subprocess.run([sys.executable, "-c", runner, "merge-chunks", str(chunk), str(invalid_chunk), "--out", str(base / "partial-merge.json")], env=child_env, capture_output=True, text=True, timeout=30)
        assert partial_merge.returncode == 0 and "1 of 2 chunks" in partial_merge.stdout
        assert "skipping invalid chunk" in partial_merge.stderr
        combined = {"nodes": ast["nodes"] + sem["nodes"], "edges": ast["edges"] + sem["edges"], "hyperedges": []}
        graph = build_from_json(copy.deepcopy(combined), directed=True, root=root, dedup=False)
        assert "src_lease_access_window" in graph
        assert graph.has_edge("src_lease_access_window", "src_lease_renew")
        communities = cluster(graph)
        labels = label_communities_by_hub(graph, communities)
        graph.graph["context_profile_probe"] = {"schema": 1, "coverage_complete": True}
        graph_path = output / "graph.json"
        assert to_json(graph, communities, str(graph_path), community_labels=labels, built_at_commit="probe")
        assert to_html(graph, communities, str(output / "graph.html"), community_labels=labels, node_limit=5000)
        report = generate(graph, communities, score_all(graph, communities), labels, god_nodes(graph), surprising_connections(graph, communities), detection, {"input": 0, "output": 0}, "probe-corpus", suggested_questions=suggest_questions(graph, communities, labels), built_at_commit="probe")
        # Native report requires numeric usage: state the actual unknown agent usage explicitly.
        report += "\nProbe interface data only; subscription-agent token usage unknown.\n"
        (output / "GRAPH_REPORT.md").write_text(report, encoding="utf-8")
        serialized = json.loads(graph_path.read_text(encoding="utf-8"))
        reopened = load_node_link_graph(serialized)
        assert reopened.is_directed()
        assert reopened.graph["context_profile_probe"] == {"schema": 1, "coverage_complete": True}
        assert reopened.has_edge("src_lease_access_window", "src_lease_renew")
        for path in output.iterdir():
            assert str(base) not in path.read_text(encoding="utf-8"), path.name
        assert "vis-network@9.1.6" in (output / "graph.html").read_text(encoding="utf-8")
        assert {p.name for p in output.iterdir()} == {"graph.json", "graph.html", "GRAPH_REPORT.md"}
        before_query = {p.relative_to(base): p.read_bytes() for p in base.rglob("*") if p.is_file()}
        query_graph = _read_graph(str(graph_path))
        answer = _query_graph_text(query_graph, "renew", seeds=["src_lease_renew"], seed_root=root, depth=1, token_budget=1200)
        assert "renew" in answer and "src/lease.py" in answer and "L1" in answer, answer
        after_query = {p.relative_to(base): p.read_bytes() for p in base.rglob("*") if p.is_file()}
        assert after_query == before_query, "native read query changed fixture files"

        save_semantic_cache(semantic["nodes"], semantic["edges"], [], root=root, allowed_source_files=[root / "src/lease.py"], prompt="probe-v1", cache_root=cache)
        hits = check_semantic_cache([str(root / "src/lease.py")], root=root, prompt="probe-v1", cache_root=cache)
        assert hits[0] and not hits[3]
        changed_prompt = check_semantic_cache([str(root / "src/lease.py")], root=root, prompt="probe-v2", cache_root=cache)
        assert changed_prompt[3]
        empty_cache = base / "fresh-cache"
        cold_env = dict(child_env, GRAPHIFY_OUT=str(empty_cache))
        cold_code = "import sys,json; from pathlib import Path; from graphify.cache import check_semantic_cache; r=check_semantic_cache([sys.argv[2]],root=Path(sys.argv[1]),prompt='probe-v1'); print(json.dumps({'hits':len(r[0]),'misses':len(r[3])}))"
        cold_run = subprocess.run([sys.executable, "-c", cold_code, str(root), str(root / "src/lease.py")], env=cold_env, capture_output=True, text=True, timeout=30)
        assert cold_run.returncode == 0, cold_run.stderr
        assert json.loads(cold_run.stdout) == {"hits": 0, "misses": 1}, cold_run.stdout

        # An AST-only refresh of the same source must retain its separate semantic tier.
        (root / "src/lease.py").write_text(corpus["src/lease.py"] + "\ndef cancel():\n    return False\n", encoding="utf-8")
        fresh = extract(files, root=root, cache_root=cache, parallel=False)
        refreshed = build_merge([fresh], graph_path=graph_path, root=root, directed=True, dedup=False)
        assert "src_lease_access_window" in refreshed
        assert refreshed.has_edge("src_lease_access_window", "src_lease_renew")
        assert "src_lease_cancel" in refreshed
        # Retained semantics now have a stale source hash and must be reprocessed.
        stale = check_semantic_cache([str(root / "src/lease.py")], root=root, prompt="probe-v1", cache_root=cache)
        assert stale[3] and not stale[0]
        corrupt = base / "corrupt.json"
        corrupt.write_text("{", encoding="utf-8")
        before = graph_path.read_bytes()
        corrupt_before = corrupt.read_bytes()
        try:
            build_merge([fresh], graph_path=corrupt, root=root, directed=True, dedup=False)
        except RuntimeError:
            pass
        else:
            raise AssertionError("corrupt graph must refuse merge")
        assert corrupt.read_bytes() == corrupt_before
        assert not to_json(graph, communities, str(corrupt), built_at_commit="probe")
        assert corrupt.read_bytes() == corrupt_before
        assert graph_path.read_bytes() == before
        assert not attempts, attempts
        print(json.dumps({"status": "PASS", "version": importlib.metadata.version("graphifyy"), "python": sys.version.split()[0], "inputs": inventory, "structural_nodes": len(ast["nodes"]), "structural_edges": len(ast["edges"]), "mixed_nodes": graph.number_of_nodes(), "mixed_edges": graph.number_of_edges(), "same_source_semantics_preserved": True, "cache_prompt_invalidation": True, "changed_source_cache_miss": True, "exact_dependency_pins": True, "native_query_preserves_fixture_files": True, "upstream_commit": origin["vcs_info"]["commit_id"], "cold_cache_requires_semantic_reextraction": True, "network_or_backend_attempts": len(attempts), "trio": sorted(p.name for p in output.iterdir())}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
