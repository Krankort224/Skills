# Graphify: maintenance and publication interfaces

Agent decisions, source verification and recovery: [maintain a graph](../operations/graphify/maintain.md). Package/runtime: [technical profile](graphify.md). Initial native structural/mixed recipes: [build reference](graphify-build.md).

## Contents

- [Portable state and validation API](#portable-state-and-validation-api)
- [Input identity and reuse assessment](#input-identity-and-reuse-assessment)
- [Assess a previous immutable generation](#assess-a-previous-immutable-generation)
- [Sealing and publication model](#sealing-and-publication-model)
- [Publish a validated trio from an isolated clone](#publish-a-validated-trio-from-an-isolated-clone)
- [Source ledger](#source-ledger)

## Portable state and validation API

The flat [validator](validate_context_fragments.py) exposes read-only `profile(tools)`, `exclusion_policy(root, exclusions)`, `snapshot(root, exclusions, authority_sources, scope=...)`, `make_state(...)`, `assess_reuse(...)` and `validate_trio(...)`. They inspect/return data without inference, graph construction, installation, caches or publication. `validate_trio(view)` consumes bounded exact buffers of all three artifacts, verifies generation, final sibling hashes, embedded HTML data/counts and report correspondence, and returns those same consumed bytes.

Portable state lives in `graph.context.maintenance`: version/snapshot/profile, original validated fragment payloads, zero-result/reader/receipt provenance, raw-byte and canonical-payload hashes, source dependencies and referenced semantic-owner shards. There is no fourth portable manifest or warm-cache prerequisite. Checksums detect corruption, not forged truth; exported source names cannot reconstruct original range/edge-only/empty-group payloads.

`profile()` verifies installed pins and fingerprints interpreter patch/platform, requirements, validator bytes, schema/mode and BOTH marked contracts: [semantic reading method](../operations/graphify/build.md#semantic-reading-and-reconciliation) and [semantic protocol](graphify-build.md#semantic-protocol), in that order. The combined contract replaces the previous single-file contract. This refactor changes the validator/profile fingerprint; an old-profile generation must pass the normal conservative re-extraction path before becoming eligible for reuse. No checksum is rewritten to imply compatibility. Reader assignment and unknown usage remain provenance; unexposed model identity cannot be compared automatically.

## Input identity and reuse assessment

Native ignore/noise/sensitive facilities govern bounded source snapshots. Inputs include source hashes/line counts, consumed configuration, scope/exclusions, authority sources and visible unsupported paths. The same `exclusion_policy` expands raw `CONTEXT_EXCLUDES` and already-effective graph rules before structural detection and refresh snapshots: required case-insensitive conversion and declared-submodule exclusions are appended, followed by the reserved derived paths. This expansion is idempotent for unchanged configuration. Native user-rule order is significant (last match wins); only earlier identical duplicates are removed. The structural artifact records this ordered effective list, never a sorted set. Reusing the original raw policy on unchanged inputs therefore yields the same snapshot/no-op; it does not require copying generated rules from a graph. Explicit rule-order or configuration changes remain identity changes. Derived-tree/Git existence and local secret contents/presence are not snapshot inputs. Sensitive exclusion policy is recorded; `.env` need not exist in a cold checkout. Pruned subtrees are exclusion policies, not exhaustive descendant inventories. Unreadable enumeration/source/type failure is blocking evidence, not deletion.

The bounded lane supports semantic-shard reuse. Changed inputs always require a fresh FULL structural baseline; changed-only native structural update is not certified. Native Markdown cache normalization and incomplete reference context make a changed-file shortcut insufficient. Native build-state mismatch can avoid fast skip while a per-file manifest still filters unchanged files, so tool/config/schema/prompt changes must participate in full identity checks.

| Assessment | Interface meaning |
|---|---|
| `noop` | Coherent intact trio and unchanged input/policy/profile; changed HEAD/date/cache/root alone is not an extraction trigger. |
| `reuse_some` | `reusable` contains eligible original payloads/provenance; invalidated shards require new reading before complete assembly. |
| `reextract_all` | Legacy/incomplete state or changed membership/policy/configuration/profile/conservative dependencies; independent current-source plan required. |
| `blocked` | Access, removal or unknown-state gap prevents completion. |

Default shard dependency is ALL selected sources. A local `dependency_reviews` declaration is `{mode:"local", reviewed:true, ownership_complete:true, negative_or_global_comparison:false, sources:[...], reason:"<source-backed review>"}`. It includes owned/evidence/endpoint sources and common authorities. Zero-findings, unresolved/corpus-wide negative comparisons and incomplete ownership retain all-source dependency. These declarations encode a review; booleans do not perform it.

Changed bytes invalidate all shards owning or depending on the WHOLE source, even if only another assigned range changed. Invalidation propagates through semantic owners to a fixed point. Added/deleted/excluded input or changed scope/configuration/schema/tool/prompt conservatively requeues all. Rename is deletion plus addition; IDs remain source-based.

Eligible original `payload` can be copied to explicit task-owned files while preserving original reader/receipts. `reuse_provenance` names prior commit/input/generation, original raw-fragment hash and canonical-payload hash. Reserialization creates a NEW raw-fragment hash. A new plan binds `expected_profile`, authority sources and reviewed dependencies before dispatch; all retained/new fragments validate against the NEW structural baseline.

Native tier replacement derives ownership from nodes. Updating a previous mixed graph can leave old edge-only/zero semantics, while `prune_sources` removes both tiers. The supported assembly therefore uses a fresh structural-only graph plus the complete retained/new semantic set. `graphify update` retaining a semantic tier is not evidence that tier is current.

## Assess a previous immutable generation

`CONTEXT_PREVIOUS_TRIO` names a new task-owned view containing three blobs from ONE resolved immutable commit. `CONTEXT_REFRESH_POLICY` names a task-local JSON object with `scope`, `exclusions`, `authority_sources`, and optional `confirmed_removals`. Root and tools are explicit. The recipe prints bounded assessment summaries rather than every portable fragment.

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

A removal confirmation maps an old relative path to `{kind:"git"|"coordinator", previous_sha256:"<old source bytes>", evidence:"<verified deletion/rename evidence>"}`. The operation verifies the actual old/current commit/path evidence; the JSON string does not prove it. A readable file excluded by a current positive rule is an exclusion. Missing/unreadable/unsafe/unexplained disappearance refuses destructive completion.

## Sealing and publication model

Native JSON/HTML/report writes are independent. Mixed assembly computes a noncircular graph/evidence generation ID, adds it to HTML/report, hashes their FINAL bytes and writes sibling hashes into JSON LAST; JSON never hashes itself. `validate_trio` verifies exact buffers, data/counts, markers, provenance, portable state and current source/profile/config/inventory. Source rechecks assume quiescent inputs, not atomic snapshots or change-and-revert protection.

Publication is atomic at the Git commit/ref boundary, not a live-directory replacement. A reader resolves one commit and obtains its three blobs into a new view before validation. An export-in-progress worktree is not a certified generation. Compatible rollback uses a new fast-forward commit of a validated prior trio only when present sources/profile still match; old output with incompatible identity remains historical.

## Publish a validated trio from an isolated clone

The recipe takes an authorized explicit remote URL, an EXISTING full branch ref, a clean task-owned clone at an expected source commit, and a fresh external stage. It updates only the remote ref, not the source clone's branch/index/worktree. A local destination must be bare; remote policy must prevent updating a nonlocal checked-out working tree. Remote aliases are unsupported.

Native `_rebuild_lock(out_dir: Path, *, blocking: bool=False)` is advisory among cooperating callers sharing the same clone/common-directory and ref convention; it does not automatically coordinate watch/update or independent clones. An explicit Git lease arbitrates competing ref writers. The recipe requires actual native locks and refuses lock diagnostics; Windows qualification covers a local filesystem with byte-range locks, not network/WSL shares.

`validate_trio(stage, root=root, require_current=True)` returns `blobs`, `digests`, `graph`, `input_identity`, `generation_identity`, `profile` and `snapshot` with `sources`, `configuration`, `exclusions` and `authority_sources`. The publisher consumes precisely those buffers, checks every selected source/config file is tracked and agrees with the expected commit, and revalidates before push. A validation error, source change or failed lease refuses publication. Unknown push outcome requires remote inspection before retry.

Environment: `CONTEXT_ROOT` = isolated clone; `CONTEXT_STAGE` = fresh external stage; `CONTEXT_TOOLS` = reviewed helpers; `CONTEXT_EXPECTED` = full source commit; `CONTEXT_REMOTE` = explicit remote URL; `CONTEXT_REMOTE_REF` = existing `refs/heads/...` ref. `CONTEXT_GRAPH_TARGET` = required normalized repository-relative POSIX directory, verified from the destination project context (for example, `skills/context/references/graphify`, `level-1/context/references/graphify` or a custom project-owned directory). No default is inferred from the helper location. A user's checkout is not the task-owned clone.

```python
# context-publish-trio
import contextlib
import io
import hashlib
import importlib.util
import json
import os
from pathlib import Path, PurePosixPath
import subprocess
import sys
import tempfile
from urllib.parse import urlsplit
from urllib.request import url2pathname
from graphify.watch import _rebuild_lock

assert __debug__
qualification = os.environ.get("CONTEXT_QUALIFY_HOST", "")
if qualification:
    assert qualification == "windows-cpython-3.13" and sys.platform == "win32" and sys.implementation.name == "cpython" and sys.version_info[:2] == (3, 13), "Qualification requires actual Windows CPython 3.13"
    assert sys.flags.utf8_mode, "Windows qualification requires PYTHONUTF8=1"
    import msvcrt  # Fail closed if the actual host has no native locking API.
else:
    assert sys.platform == "linux" and sys.implementation.name == "cpython" and sys.version_info[:2] == (3, 12), "Publication requires the verified Linux lane or explicit Windows qualification"
    import fcntl
assert not any(os.environ.get(k) for k in ("GIT_DIR", "GIT_WORK_TREE", "GIT_INDEX_FILE", "GIT_COMMON_DIR", "GIT_OBJECT_DIRECTORY", "GIT_ALTERNATE_OBJECT_DIRECTORIES", "GIT_REPLACE_REF_BASE"))
os.environ["GIT_NO_REPLACE_OBJECTS"] = "1"
os.environ["GIT_OPTIONAL_LOCKS"] = "0"
root = Path(os.environ["CONTEXT_ROOT"]).resolve(strict=True)
stage = Path(os.environ["CONTEXT_STAGE"]).resolve(strict=True)
expected, remote, ref = (os.environ[k] for k in ("CONTEXT_EXPECTED", "CONTEXT_REMOTE", "CONTEXT_REMOTE_REF"))
target = os.environ["CONTEXT_GRAPH_TARGET"]
target_parts = target.split("/")
assert target and not PurePosixPath(target).is_absolute() and PurePosixPath(target).as_posix() == target, "Invalid CONTEXT_GRAPH_TARGET"
assert all(part not in ("", ".", "..") and part.casefold() != ".git" and part == part.strip() and not part.endswith(".") for part in target_parts), "Invalid CONTEXT_GRAPH_TARGET"
assert not any(ord(ch) < 32 or ord(ch) == 127 or ch in '\\:<>"|?*[]' for ch in target), "Invalid CONTEXT_GRAPH_TARGET"
names = ("graph.json", "graph.html", "GRAPH_REPORT.md")
assert root.is_dir() and stage.is_dir() and not stage.is_relative_to(root) and not root.is_relative_to(stage)
assert remote and not remote.startswith("-") and ref.startswith("refs/heads/")

def git(*args, data=None, env=None, check=True):
    return subprocess.run(["git", "-C", str(root), *args], input=data, stdout=subprocess.PIPE, stderr=subprocess.PIPE, env=env, check=check, timeout=60)

def text(*args):
    return git(*args).stdout.decode().strip()

git("check-ref-format", ref)
assert Path(text("rev-parse", "--show-toplevel")).resolve(strict=True) == root
assert expected == text("rev-parse", "--verify", expected + "^{commit}") == text("rev-parse", "HEAD")
assert not git("status", "--porcelain=v1", "--untracked-files=all").stdout, "Task clone is not clean"
assert not Path(remote).drive or Path(remote).is_absolute(), "Drive-relative local remote is unsupported"
parts = urlsplit(remote)
if Path(remote).is_absolute() or (not parts.scheme and ":" not in remote):
    local = (root / remote).resolve(strict=True)
elif parts.scheme == "file":
    assert parts.netloc in ("", "localhost") and not parts.query and not parts.fragment
    local = Path(url2pathname(parts.path)).resolve(strict=True)
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

# Reject unsafe target ancestors before creating locks, objects or an index.
for i in range(1, len(target_parts) + 1):
    prefix = "/".join(target_parts[:i])
    ancestor = root.joinpath(*target_parts[:i])
    assert not ancestor.is_symlink() and (not ancestor.exists() or ancestor.is_dir()), ("Unsafe target ancestor", prefix)
    assert not ancestor.exists() or not getattr(ancestor.lstat(), "st_file_attributes", 0) & 0x400, ("Unsafe target ancestor", prefix)
    item = tree_entry(prefix)
    assert item is None or item[:2] == (b"040000", b"tree"), ("Unsafe target ancestor", prefix)

with contextlib.ExitStack() as locks:
    # Native Windows locking can deliberately continue unlocked on unsupported
    # filesystems. Refuse its diagnostic before any publication work instead.
    with contextlib.redirect_stderr(io.StringIO()) as lock_messages:
        acquired = locks.enter_context(_rebuild_lock(lock, blocking=True))
    assert acquired and not lock_messages.getvalue(), "Publication lock unavailable: " + lock_messages.getvalue()
    first = validate()
    verify_sources(first)
    assert remote_tip() == expected, "Remote moved; rebuild/review against new tip"
    blobs = first["blobs"]
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
            published = remote_tip()
            assert published == commit, "Published remote tip differs; inspect before retry"
            for name in names:
                assert git("show", f"{published}:{target}/{name}").stdout == blobs[name]
            print(json.dumps({"status": "published", "commit": published, "parent": expected}))
```

Postcondition: read the three published blobs from one resolved immutable commit and verify generation/sibling digests. Pre-push failure can leave unreachable candidate objects without moving the remote; failed/timed-out push has unknown outcome until inspection. Refusal of a stale candidate is not rollback. The graph-specific decisions and task authorization remain with [maintain](../operations/graphify/maintain.md) and the applicable project/workflow contract.

## Source ledger

- [Maintenance](https://github.com/Graphify-Labs/graphify/blob/16218bfc80d4ca2799734d045039f7ed1a5fa9fb/graphify/watch.py): native lock 258, semantic/doc reconciliation 1167–1509, metadata guard 1769, build-state identity 1929–1970, HTML 2115, rebuild/incremental path 2241–2512, directed preservation 3073. [Paths](https://github.com/Graphify-Labs/graphify/blob/16218bfc80d4ca2799734d045039f7ed1a5fa9fb/graphify/paths.py): import-time output selector 39–53, individual atomic writes, native graph loaders.
