"""Replay recorded genuine E model outputs through coverage/native boundaries.

Replaying is not a new semantic extraction. Fresh semantic trials require an
active subscription agent reading the raw files, as documented in
../operations/graphify/build.md; graphify-build.md owns the assembly recipe.
"""
from __future__ import annotations
import copy
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import re
import shutil
import sys
import tempfile

TOOLS = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("structural_probe", TOOLS / "probe_graphify_structure.py")
probe = importlib.util.module_from_spec(spec)
spec.loader.exec_module(probe)
matches = re.findall(r"```python\n(# context-semantic-assemble\n.*?)\n```", (TOOLS / "graphify-build.md").read_text(encoding="utf-8"), re.S)
assert len(matches) == 1
code = matches[0]


def dump(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")


def check_profile_contracts(base, state):
    """Both canonical semantic owners must independently govern valid reuse."""
    spec = importlib.util.spec_from_file_location("profile_validator", TOOLS / "validate_context_fragments.py")
    validator = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(validator)
    tools = base / "profile-controls/context/tools"
    tools.mkdir(parents=True)
    owners = (tools.parent / "operations/graphify/build.md", tools / "graphify-build.md")
    for source, target in ((TOOLS.parent / "operations/graphify/build.md", owners[0]),
                           (TOOLS / "graphify-build.md", owners[1]),
                           (TOOLS / "graphify-requirements.txt", tools / "graphify-requirements.txt"),
                           (TOOLS / "validate_context_fragments.py", tools / "validate_context_fragments.py")):
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, target)
    expected = validator.profile(TOOLS)
    assert validator.profile(tools) == validator.profile(tools) == expected == state["profile"]
    def assessment(profile):
        return validator.assess_reuse(state, state["snapshot"], profile)
    assert assessment(expected)["status"] == "noop"
    start, end = validator.CONTRACT_START, validator.CONTRACT_END
    bodies = [path.read_bytes().decode("utf-8").split(start)[1].split(end)[0] for path in owners]
    assert expected["extraction_contract_sha256"] == hashlib.sha256(validator._canonical(bodies)).hexdigest()
    assert expected["extraction_contract_sha256"] != hashlib.sha256(validator._canonical(bodies[::-1])).hexdigest()
    refusals = []
    for index, path in enumerate(owners):
        original = path.read_bytes()
        text = original.decode("utf-8")
        path.write_text(text.replace(end, "\nTest-only substantive semantic instruction.\n" + end), encoding="utf-8", newline="\n")
        changed = validator.profile(tools)
        assert {key for key in expected if expected[key] != changed[key]} == {"extraction_contract_sha256"}
        result = assessment(changed)
        assert result["status"] == "reextract_all" and result["reasons"] == ["Profile/scope/configuration/inventory policy changed"]
        path.write_text(text + "\n<!-- presentation-only test note -->\n", encoding="utf-8", newline="\n")
        assert validator.profile(tools) == expected and assessment(validator.profile(tools))["status"] == "noop"
        damaged = {
            "missing-start": text.replace(start, ""),
            "missing-end": text.replace(end, ""),
            "duplicate-start": text.replace(start, start + start),
            "duplicate-end": text.replace(end, end + end),
            "reversed": text.replace(start, "CONTRACT_SWAP").replace(end, start).replace("CONTRACT_SWAP", end),
            "empty": text[:text.index(start) + len(start)] + "\n" + text[text.index(end):],
            "missing-owner": None,
        }
        for name, replacement in damaged.items():
            try:
                if replacement is None:
                    path.unlink()
                else:
                    path.write_text(replacement, encoding="utf-8", newline="\n")
                try:
                    validator.profile(tools)
                except (ValueError, OSError) as error:
                    assert replacement is None or "extraction contract" in str(error).lower(), str(error)
                else:
                    raise AssertionError((index, name, "Damaged contract accepted"))
                refusals.append(f"owner-{index + 1}:{name}")
            finally:
                path.write_bytes(original)
    implementation = tools / "validate_context_fragments.py"
    implementation.write_bytes(implementation.read_bytes() + b"\n# Test-only validator identity change.\n")
    changed = validator.profile(tools)
    assert {key for key in expected if expected[key] != changed[key]} == {"validator_sha256"}
    assert assessment(changed)["status"] == "reextract_all"
    return {"unchanged_noop": True, "order": ["operational-method", "technical-protocol"],
            "each_contract_independently_invalidates": True, "validator_independently_invalidates": True,
            "outside_marker_edit_preserves_noop": True, "refusals": refusals}


def main():
    if not __debug__:
        raise SystemExit("Run without -O")
    data = json.loads((TOOLS / "graphify-semantic-cases.json").read_text(encoding="utf-8"))
    with tempfile.TemporaryDirectory(prefix="context-semantic-") as temporary:
        base = Path(temporary)
        root = base / "corpus"
        for name, body in data["files"].items():
            path = root / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(body, encoding="utf-8", newline="\n")
        initial_sources = probe.snapshot(root)
        env = {k: v for k, v in os.environ.items() if not any(word in k.upper() for word in ("API_KEY", "TOKEN", "SECRET", "PASSWORD", "PROVIDER", "AWS_", "GOOGLE_", "GEMINI_", "OPENAI_", "ANTHROPIC_"))}
        env.update(CONTEXT_ROOT=str(root), CONTEXT_TOOLS=str(TOOLS), CONTEXT_STAGE=str(base / "structural"), CONTEXT_EXCLUDES="[]", GRAPHIFY_OUT=str(base / "structural/native-cache"), GRAPHIFY_BACKEND="none", GRAPHIFY_QUERY_LOG_DISABLE="1", PYTHONDONTWRITEBYTECODE="1", OPENAI_API_KEY="forbidden-synthetic", GEMINI_API_KEY="forbidden-synthetic")
        probe.run("profile-check", env)
        probe.run("structural-build", env)
        baseline = base / "structural/artifacts/graph.json"
        structural = json.loads(baseline.read_text(encoding="utf-8"))
        env["CONTEXT_STRUCTURAL"] = str(baseline)
        totals = {}
        for mode, trial in data["recorded_trials"].items():
            plan = dict(trial["plan"], structural_sha256=hashlib.sha256(baseline.read_bytes()).hexdigest())
            plan_path = base / mode / "plan.json"
            dump(plan_path, plan)
            paths = []
            for i, fragment in enumerate(trial["fragments"]):
                path = base / mode / f"fragment-{i}.json"
                dump(path, fragment)
                paths.append(path)
            # Exercise the documented CLI as well as the assembly's in-process validator.
            cli = 'import runpy,sys\nsys.argv=' + repr([str(TOOLS / "validate_context_fragments.py"), "--root", str(root), "--plan", str(plan_path), "--structural", str(baseline), "--fragments", *map(str, paths)]) + '\nrunpy.run_path(' + repr(str(TOOLS / "validate_context_fragments.py")) + ',run_name="__main__")'
            before_cli = probe.snapshot(base)
            checked = json.loads(probe.execute(cli, env).stdout)
            assert probe.snapshot(base) == before_cli and checked["context_semantic"]["usage"] is None
            if mode == "parallel":
                missing_cli = 'import runpy,sys\nsys.argv=' + repr([str(TOOLS / "validate_context_fragments.py"), "--root", str(root), "--plan", str(plan_path), "--structural", str(baseline), "--fragments", *map(str, paths[:-1])]) + '\nrunpy.run_path(' + repr(str(TOOLS / "validate_context_fragments.py")) + ',run_name="__main__")'
                refused = probe.execute(missing_cli, env, success=False, reason="Missing expected shard")
                assert not refused.stdout and probe.snapshot(base) == before_cli
            e = dict(env, CONTEXT_PLAN=str(plan_path), CONTEXT_FRAGMENTS=json.dumps(list(map(str, paths))), CONTEXT_MIXED_STAGE=str(base / f"{mode}-artifacts"))
            members = json.loads(probe.execute(code, e).stdout)
            labels = {"input_identity": members["input_identity"], "evidence_identity": members["evidence_identity"], "communities": trial["community_interpretation"]}
            label_path = base / mode / "labels.json"
            dump(label_path, labels)
            e["CONTEXT_LABELS"] = str(label_path)
            built = json.loads(probe.execute(code, e).stdout)
            output = Path(e["CONTEXT_MIXED_STAGE"])
            graph = json.loads((output / "graph.json").read_text(encoding="utf-8"))
            ledger = graph["graph"]["context"]["semantic"]
            assert ledger["usage"] is None and all(r["usage"] is None for r in ledger["readers"].values())
            assert all(n["_origin"] == "semantic" for n in graph["nodes"] if n["id"] not in {n["id"] for n in structural["nodes"]})
            assert any(edge["source"] == "src_gate_usable" and (edge["target"] == "docs_policy" or edge["target"].startswith("docs_policy_")) and edge["confidence"] == "INFERRED" and edge["_origin"] == "semantic" for edge in graph["links"])
            assert not any(edge.get("_origin") == "semantic" and (edge["source"].startswith("docs_unrelated") or edge["target"].startswith("docs_unrelated") or edge["source"].startswith("docs_неясно") or edge["target"].startswith("docs_неясно")) for edge in graph["links"])
            assert ledger["open_questions"] and any(n.get("claim_status") == "superseded" for n in graph["nodes"])
            assert any(edge["source"] == "docs_журнал_boundary_observations" and edge["target"] == "docs_журнал_north_grant" and edge["source_location"] == "L2205-L2206" for edge in graph["links"])
            assert any(r["outcome"] == "zero-findings" and r["source_file"] == "docs/unrelated.md" for rs in ledger["coverage"].values() for r in rs)
            report = (output / "GRAPH_REPORT.md").read_text(encoding="utf-8")
            assert report.count("Subscription-agent token usage: unknown") == 1 and "- Token cost:" not in report and "0 input" not in report
            # The exact call+semantic relation sites remain queryable without CLI stamps.
            query_code = 'from graphify.serve import _read_graph, _query_graph_text\nG=_read_graph(' + repr(str(output / "graph.json")) + ')\nG.graph["_learning_overlay"]={}\nprint(_query_graph_text(G,"Which rule does usable implement?",seeds=["src_gate_usable"],seed_root=Path(os.environ["CONTEXT_ROOT"]),depth=1,token_budget=1600))'
            before = probe.snapshot(base)
            answer = probe.execute("import os\nfrom pathlib import Path\n" + query_code, e)
            assert "INFERRED" in answer.stdout and "at=src/gate.py:" in answer.stdout
            assert probe.snapshot(base) == before
            # Native AST-tier refresh of unchanged bytes must preserve explicit semantic L-located evidence.
            retention = '''import copy, json, os
from pathlib import Path
from graphify.extract import extract
from graphify.build import build_merge
root=Path(os.environ["CONTEXT_ROOT"])
original=json.loads(Path(os.environ["MIXED_JSON"]).read_text())
paths=[root / n for n in original["graph"]["context"]["sources"]]
raw=extract(paths,root=root,cache_root=Path(os.environ["RETENTION_CACHE"]),parallel=False)
G=build_merge([copy.deepcopy(raw)],graph_path=Path(os.environ["MIXED_JSON"]),root=root,directed=True,dedup=False,ast_sources=raw["extracted_sources"])
for node in original["nodes"]:
    if node.get("_origin")=="semantic":
        assert node["id"] in G and G.nodes[node["id"]]["_origin"]=="semantic"
for edge in original["links"]:
    if edge.get("_origin")=="semantic":
        restored=G.edges[edge["source"],edge["target"]]
        assert all(restored.get(k)==edge.get(k) for k in ("relation","confidence","source_file","source_location","_origin","evidence"))
'''
            probe.execute(retention, dict(e, MIXED_JSON=str(output / "graph.json"), RETENTION_CACHE=str(base / f"{mode}-retention")))
            totals[mode] = built
        assert probe.snapshot(root) == initial_sources
        # Negative/recovery tests use the real recorded serial output; source truth is unchanged.
        trial = data["recorded_trials"]["serial"]
        original_plan = dict(trial["plan"], structural_sha256=hashlib.sha256(baseline.read_bytes()).hexdigest())
        original_fragment = trial["fragments"][0]
        negative_root = base / "negative"
        plan_path, fragment_path = negative_root / "plan.json", negative_root / "fragment.json"
        check_code = 'import importlib.util,os\nfrom pathlib import Path\nspec=importlib.util.spec_from_file_location("validator",Path(os.environ["CONTEXT_TOOLS"])/"validate_context_fragments.py")\nv=importlib.util.module_from_spec(spec);spec.loader.exec_module(v)\nv.validate(os.environ["CONTEXT_ROOT"],os.environ["CHECK_PLAN"],os.environ["CONTEXT_STRUCTURAL"],[Path(os.environ["CHECK_FRAGMENT"])])'
        checks = []
        def refusal(name, reason, change_fragment=None, change_plan=None, raw=None):
            fragment, plan = copy.deepcopy(original_fragment), copy.deepcopy(original_plan)
            if change_fragment:
                change_fragment(fragment)
            if change_plan:
                change_plan(plan)
            dump(plan_path, plan)
            dump(fragment_path, fragment)
            if raw is not None:
                fragment_path.write_text(raw, encoding="utf-8", newline="\n")
            before = probe.snapshot(base)
            probe.execute(check_code, dict(env, CHECK_PLAN=str(plan_path), CHECK_FRAGMENT=str(fragment_path)), success=False, reason=reason)
            assert probe.snapshot(base) == before
            checks.append(name)
        refusal("partial shard", "Incomplete/incompatible", lambda f: f.update(status="partial"))
        refusal("native partial marker", "Partial extraction marker", lambda f: f.update(partial=True))
        refusal("partial record", "Partial extraction marker", lambda f: f["nodes"][0].update(_partial=True))
        refusal("missing/short receipt", "Missing/short/changed", lambda f: f["receipts"].pop())
        refusal("unknown shard", "Unexpected/duplicate shard", lambda f: f.update(shard_id="unexpected"))
        refusal("range gap through EOF", "Planned coverage misses EOF", change_plan=lambda p: p["shards"][0]["ranges"].pop())
        refusal("source path escape", "Unsafe/noncanonical", change_plan=lambda p: p["sources"].update({"../outside.md": p["sources"].pop("docs/policy.md")}))
        refusal("uncovered baseline source", "complete structural baseline", change_plan=lambda p: p["sources"].pop("src/ledger.py"))
        refusal("no actual findings", "Findings receipt has no owned", lambda f: f.update(nodes=[],edges=[],hyperedges=[],open_questions=[]))
        refusal("false zero findings", "Zero-findings receipt contradicts", lambda f: f["receipts"][0].update(outcome="zero-findings"))
        refusal("bad evidence", "Evidence quote mismatch", lambda f: f["nodes"][0]["evidence"][0].update(quote="invented"))
        refusal("AST origin", "Invalid semantic source/origin", lambda f: f["nodes"][0].update(_origin="ast"))
        refusal("duplicate semantic ID", "Duplicate/structural identity", lambda f: f["nodes"].append(copy.deepcopy(f["nodes"][0])))
        refusal("invalid confidence", "Invalid confidence rubric", lambda f: f["edges"][0].update(confidence_score=.5))
        refusal("boolean score", "Missing/nonfinite confidence", lambda f: f["edges"][0].update(confidence_score=True))
        refusal("missing inference rationale", "lacks rationale", lambda f: f["edges"][0].pop("rationale"))
        refusal("unknown endpoint", "Unresolved relationship endpoint", lambda f: f["edges"][0].update(target="unknown_node"))
        def ast_pair(fragment):
            item = copy.deepcopy(fragment["edges"][0])
            item.update(source="src_gate_admit",target="src_gate_usable",relation="calls")
            fragment["edges"]=[item]
        refusal("structural pair collision", "Endpoint-pair collision", ast_pair)
        refusal("pair collision", "Endpoint-pair collision", lambda f: f["edges"].append(copy.deepcopy(f["edges"][0])))
        refusal("missing reader model", "Missing/invalid model", lambda f: f["reader"].pop("model"))
        refusal("fabricated usage", "unknown subscription usage", lambda f: f["reader"].update(usage={"input":0,"output":0}))
        refusal("duplicate JSON key", "Duplicate JSON key", raw='{"nodes":[],"nodes":[]}')
        refusal("NaN", "Nonfinite JSON number", raw='{"bad":NaN}')
        refusal("exponent overflow", "Nonfinite JSON number", raw='{"bad":1e999}')
        refusal("oversized JSON", "Oversized JSON/source", raw=" " * (2*1024*1024+1))
        # Changes after D must invalidate even without a new semantic finding.
        changed = root / "src/gate.py"
        changed.write_text(data["files"]["src/gate.py"].replace("168", "169"), encoding="utf-8", newline="\n")
        refusal("changed baseline bytes", "Source identity mismatch")
        changed.write_text(data["files"]["src/gate.py"], encoding="utf-8", newline="\n")
        added = root / "added.py"
        added.write_text("def added(): pass\n", encoding="utf-8", newline="\n")
        refusal("added baseline source", "Structural source inventory changed")
        added.unlink()
        config = root / ".graphifyrc"
        config.write_text("# new config\n", encoding="utf-8", newline="\n")
        refusal("changed baseline configuration", "Structural configuration changed")
        config.unlink()
        # Cross-source hyperedge needs all inferred member evidence, not just valid IDs.
        def bad_hyperedge(fragment):
            item = copy.deepcopy(fragment["nodes"][0])
            item.update(id="docs_policy_grant_group",entity_key="grant_group",nodes=[n["id"] for n in fragment["nodes"][:3]],relation="participate_in",confidence="INFERRED",confidence_score=.85,rationale="Synthetic negative test of insufficient member evidence.")
            fragment["hyperedges"]=[item]
        refusal("hyperedge member evidence", "Cross-source hyperedge inference", bad_hyperedge)
        # Complete empty findings are allowed only when every receipt explicitly says zero.
        dump(plan_path, original_plan)
        empty = copy.deepcopy(original_fragment)
        empty.update(nodes=[],edges=[],hyperedges=[],open_questions=[])
        for receipt in empty["receipts"]:
            receipt.update(outcome="zero-findings",reason="Synthetic accounting-only negative-result acceptance, not this corpus truth.")
        dump(fragment_path, empty)
        probe.execute(check_code, dict(env,CHECK_PLAN=str(plan_path),CHECK_FRAGMENT=str(fragment_path)))
        assert probe.snapshot(root) == initial_sources
        state = json.loads((Path(totals["parallel"]["stage"]) / "graph.json").read_text(encoding="utf-8"))["graph"]["context"]["maintenance"]
        profile_checks = check_profile_contracts(base, state)
        print(json.dumps({"status":"PASS","recorded_model_replay_only":True,"trials":totals,"negative_checks":checks,"profile_contract_checks":profile_checks,"complete_empty_accounting":"accepted, not claimed as source truth","unknown_usage_preserved":True,"unchanged_AST_refresh_preserves_semantics":True,"network_or_provider_attempts":len(probe.ATTEMPTS)},ensure_ascii=False,indent=2))


if __name__ == "__main__":
    main()
