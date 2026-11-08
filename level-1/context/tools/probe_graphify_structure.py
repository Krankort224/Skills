"""Exercise the documented structural runbook on bounded raw fixtures.

This is a test harness, not a project-build command. Production instructions
remain in graphify.md and call the pinned native APIs directly.
"""
from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import textwrap

TOOLS = Path(__file__).resolve().parent
BOOK = (TOOLS / "graphify.md").read_text(encoding="utf-8")
BLOCKS = {}
for name in ("profile-check", "structural-build", "structural-query"):
    match = re.search(r"```python\n(# context-" + name + r"\n.*?)\n```", BOOK, re.S)
    assert match, name
    BLOCKS[name] = match.group(1)
GUARD = '''import socket
observed_attempts = []
def forbidden(*args, **kwargs):
    observed_attempts.append("network_or_provider")
    raise AssertionError("Network/provider access forbidden in the structural probe")
socket.socket.connect = forbidden
socket.create_connection = forbidden
from graphify import llm
llm.extract_corpus_parallel = forbidden
llm._call_llm = forbidden
import graphify.detect
# Conversion is also outside this certified Python/Markdown slice.
graphify.detect.convert_office_file = forbidden
'''


def snapshot(root):
    return {p.relative_to(root).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in root.rglob("*") if p.is_file()}


ATTEMPTS = []


def execute(code, environment, *, before="", success=True, reason=None):
    guarded = before + "\n" + GUARD + "\nimport json\ntry:\n" + textwrap.indent(code, "    ") + "\nfinally:\n    print('CONTEXT_ATTEMPTS=' + json.dumps(observed_attempts))\n"
    result = subprocess.run([sys.executable, "-c", guarded], env=environment,
                            capture_output=True, text=True, timeout=60)
    lines = result.stdout.splitlines()
    markers = [line for line in lines if line.startswith("CONTEXT_ATTEMPTS=")]
    assert len(markers) == 1, (result.stdout, result.stderr)
    attempts = json.loads(markers[0].split("=", 1)[1])
    ATTEMPTS.extend(attempts)
    assert not attempts, (attempts, result.stderr)
    result.stdout = "\n".join(line for line in lines if not line.startswith("CONTEXT_ATTEMPTS="))
    assert (result.returncode == 0) == success, (result.stdout, result.stderr)
    if reason:
        assert reason in result.stderr, (reason, result.stderr)
    return result


def run(name, environment, **kwargs):
    return execute(BLOCKS[name], environment, **kwargs)


def main():
    if not __debug__:
        raise SystemExit("Run without -O")
    data = json.loads((TOOLS / "graphify-structural-cases.json").read_text(encoding="utf-8"))
    with tempfile.TemporaryDirectory(prefix="context-structural-") as temporary:
        base = Path(temporary)
        root = base / 'corpus "Связи"'
        root.mkdir()
        for relative, text in data["files"].items():
            path = root / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(text, encoding="utf-8")
        outside = base / "external.py"
        outside.write_text("def out_of_scope_marker(): pass\n", encoding="utf-8")
        (root / "escaped.py").symlink_to(outside)
        environment = {k: v for k, v in os.environ.items()
                       if not any(word in k.upper() for word in ("API_KEY", "TOKEN", "SECRET", "PASSWORD", "PROVIDER", "AWS_", "GOOGLE_", "GEMINI_", "OPENAI_", "ANTHROPIC_"))}
        environment.update(CONTEXT_ROOT=str(root), CONTEXT_TOOLS=str(TOOLS),
                           CONTEXT_EXCLUDES=json.dumps(data["excludes"]),
                           GRAPHIFY_BACKEND="none", GRAPHIFY_QUERY_LOG_DISABLE="1",
                           PYTHONDONTWRITEBYTECODE="1",
                           GEMINI_API_KEY="forbidden-synthetic-test-value",
                           OPENAI_API_KEY="forbidden-synthetic-test-value")
        def stage_environment(name):
            stage = base / name
            return dict(environment, CONTEXT_STAGE=str(stage), GRAPHIFY_OUT=str(stage / "native-cache"))
        env = stage_environment("first")
        original = snapshot(root)
        profile = run("profile-check", env)
        # The same check is used to reuse a compatible installation, with no installer.
        reused = run("profile-check", env)
        assert profile.stdout == reused.stdout
        build = run("structural-build", env)
        artifacts = Path(env["CONTEXT_STAGE"]) / "artifacts"
        raw = json.loads((artifacts / "graph.json").read_text(encoding="utf-8"))
        nodes = {n["id"]: n for n in raw["nodes"]}
        links = raw["links"]
        metadata = raw["graph"]["context"]
        assert metadata["semantic_extraction"] == "not performed"
        assert set(metadata["sources"]) == set(data["selected"]), metadata["sources"]
        for node, location in data["locations"].items():
            assert nodes[node]["source_location"] == location, (node, nodes.get(node))
        for expected in data["edges"]:
            assert any(all(edge.get(k) == v for k, v in expected.items()) for edge in links), expected
        assert not any(e["source"] == "docs_guide_guide" and e["relation"] == "references" and e["target"] == "src_other_renew" for e in links)
        assert not any(e["source"] == "docs_guide" and e["target"] in {"src_lease", "docs_b_duplicate", "docs_missing"} and e["relation"] == "references" for e in links)
        assert not any("not_a_heading" in node.lower() for node in nodes)
        assert metadata["dangling_raw_edges"] == 1
        assert "notes.txt" in metadata["omissions"]["uncertified_detected"]
        assert "extra.sql" in metadata["omissions"]["uncertified_detected"]
        assert any("escaped.py" in p for p in metadata["omissions"]["sensitive_or_unsafe"])
        assert any("unselected/module" in p for p in metadata["excludes"])
        assert snapshot(root) == original
        report = (artifacts / "GRAPH_REPORT.md").read_text(encoding="utf-8")
        html = (artifacts / "graph.html").read_text(encoding="utf-8")
        assert "STRUCTURAL ONLY" in report and "semantic extraction was not performed" in report
        assert "compare to check if the graph is stale" not in report
        assert "all connections are within the same source files" not in report
        assert f'{len(nodes)} nodes · {len(links)} edges' in report
        assert f'{len(nodes)} nodes &middot; {len(links)} edges' in html
        assert "vis-network@9.1.6" in html
        assert all("out_of_scope_marker" not in p.read_text(encoding="utf-8") for p in artifacts.iterdir())
        query_env = dict(env, CONTEXT_SEED="src_lease_authorize", CONTEXT_QUESTION="What does authorize call?")
        before_query = snapshot(base)
        answer = run("structural-query", query_env)
        assert "EDGE authorize() --calls [EXTRACTED context=call]--> renew() at=src/lease.py:L5" in answer.stdout, answer.stdout
        assert not any(e["source"] == "src_lease_renew" and e["target"] == "src_lease_authorize" and e["relation"] == "calls" for e in links)
        assert snapshot(base) == before_query

        # A real built trio is the last-good target; no negative case may modify it.
        published = root / "skills/context/references/graphify"
        published.mkdir(parents=True, exist_ok=True)
        for path in artifacts.iterdir():
            shutil.copy2(path, published / path.name)
        after_publication = snapshot(root)
        second = stage_environment("second")
        run("structural-build", second)
        assert snapshot(root) == after_publication
        second_raw = json.loads((Path(second["CONTEXT_STAGE"]) / "artifacts/graph.json").read_text())
        assert second_raw["graph"]["context"]["input_identity"] == metadata["input_identity"]

        # Simulated incompatible distribution metadata; installed package files are untouched.
        fake = base / "mismatch" / "graphifyy-0.0.dist-info"
        fake.mkdir(parents=True)
        (fake / "METADATA").write_text("Metadata-Version: 2.1\nName: graphifyy\nVersion: 0.0\n")
        mismatch = run("profile-check", env, before="import sys; sys.path.insert(0," + repr(str(fake.parent)) + ")", success=False, reason="Graphify version mismatch")
        assert "Graphify version mismatch" in mismatch.stderr
        # Simulated absent CLI in this check only; do not rename an installed executable.
        absent = run("profile-check", env, before="from pathlib import Path\n_real_is_file=Path.is_file\nPath.is_file=lambda p: False if p.name=='graphify' else _real_is_file(p)", success=False, reason="Candidate CLI is missing")
        assert "Candidate CLI is missing" in absent.stderr

        # Native optional grammar really is absent in the base profile.
        sql_code = '''from graphify.extract import extract
from pathlib import Path
r=extract([Path(os.environ["CONTEXT_ROOT"])/"extra.sql"],root=Path(os.environ["CONTEXT_ROOT"]),cache_root=Path(os.environ["CONTEXT_STAGE"]),parallel=False)
assert r["failed_sources"] and not r["nodes"]
'''
        missing = execute("import os\n" + sql_code, stage_environment("optional-sql"))
        assert "not installed" in missing.stderr, missing.stderr

        for name, content, reason in (("binary", "# Bad\n\x00\n", "Uncertified binary/NUL source"), ("encoding", "\xff", "UnicodeDecodeError"), ("parse", "def broken(:\n return 1\n", "Parser recovery is not clean coverage")):
            path = root / ("broken.py" if name == "parse" else "broken.md")
            if name == "encoding":
                path.write_bytes(b"\xff")
            else:
                path.write_text(content, encoding="utf-8")
            failed = run("structural-build", stage_environment(name), success=False, reason=reason)
            assert not (base / name / "artifacts").exists(), failed.stderr
            path.unlink()

        # Mutate inputs after extraction: each observed change must invalidate staging.
        for name, mutation, reason in (
            ("new-source", '(root / "added.md").write_text("# Added\\n")', "Inventory changed during build"),
            ("config-edit", '(root / "docs/.graphifyignore").write_text("# Changed\\n")', "Configuration changed during build"),
            ("source-edit", '(root / "src/lease.py").write_text("def replacement(): pass\\n")', "Sources changed during extraction"),
        ):
            hook = 'import graphify.extract as module\n_original_extract = module.extract\ndef changed(*a, **kw):\n    result = _original_extract(*a, **kw)\n    root = kw["root"]\n    ' + mutation + '\n    return result\nmodule.extract = changed\n'
            run("structural-build", stage_environment(name), before=hook, success=False, reason=reason)
            (root / "added.md").unlink(missing_ok=True)
            (root / "docs/.graphifyignore").write_text(data["files"]["docs/.graphifyignore"], encoding="utf-8")
            (root / "src/lease.py").write_text(data["files"]["src/lease.py"], encoding="utf-8")
        (root / "docs/.graphifyignore").write_text("!UPPER.DOCX\n")
        run("structural-build", stage_environment("conversion-reinclude"), success=False, reason="Conversion-capable input was re-included")
        (root / "docs/.graphifyignore").write_text(data["files"]["docs/.graphifyignore"], encoding="utf-8")
        # A file allowlist still consumes a nested ignore file even when a made-up
        # descendant filename would be ignored. Verify the real directory semantics.
        allowlist = root / ".graphifyignore"
        allowlist.write_text("*\n!docs/\n!docs/policy.md\n")
        allowed_env = stage_environment("allowlist")
        run("structural-build", allowed_env)
        allowed = json.loads((Path(allowed_env["CONTEXT_STAGE"]) / "artifacts/graph.json").read_text())
        assert "docs/.graphifyignore" in allowed["graph"]["context"]["configuration_hashes"]
        hook = 'import graphify.extract as module\n_original_extract=module.extract\ndef changed(*a, **kw):\n    result=_original_extract(*a, **kw)\n    (kw["root"] / "docs/.graphifyignore").write_text("# Mutated\\n")\n    return result\nmodule.extract=changed\n'
        run("structural-build", stage_environment("allowlist-mutation"), before=hook, success=False, reason="Configuration changed during build")
        allowlist.unlink()
        (root / "docs/.graphifyignore").write_text(data["files"]["docs/.graphifyignore"], encoding="utf-8")
        modules = root / ".gitmodules"
        modules.write_text('[submodule "unsafe"]\n path = !module\n')
        run("structural-build", stage_environment("submodule-pattern"), success=False, reason="Unsupported submodule spelling")
        modules.write_text(data["files"][".gitmodules"].replace("unselected/module", "./unselected//module"), encoding="utf-8")
        normalized_env = stage_environment("normalized-submodule")
        run("structural-build", normalized_env)
        normalized = json.loads((Path(normalized_env["CONTEXT_STAGE"]) / "artifacts/graph.json").read_text())
        assert set(normalized["graph"]["context"]["sources"]) == set(data["selected"])
        modules.write_text(data["files"][".gitmodules"], encoding="utf-8")
        assert snapshot(root) == after_publication
        print(json.dumps({"status": "PASS", "profile": json.loads(profile.stdout),
                          "selected_files": len(metadata["sources"]), "nodes": len(nodes), "edges": len(links),
                          "raw_dangling_edges": metadata["dangling_raw_edges"],
                          "cases": ["documented blocks", "exact identity", "compatible reuse", "source/root exclusion", "native structural truth", "trio counts and embedded HTML evidence", "read-only query", "real last-good target unchanged", "metadata mismatch simulated", "CLI absence simulated", "optional SQL dependency absent", "binary/encoding/parser failure", "source/inventory/config mutation", "submodule pattern rejection", "Office conversion excluded for all casing", "nested exclusion negations", "allowlisted nested configuration"],
                          "semantic_extraction": "not performed", "network_or_provider_attempts": len(ATTEMPTS)}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
