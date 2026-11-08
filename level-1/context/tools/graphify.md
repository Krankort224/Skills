# Graphify: technical profile

This reference owns the pinned package, runtime preparation and reproducible compatibility evidence. Agent methods live in [Graphify operations](../operations/graphify/build.md) and the selected `context` operation.

## Contents

- [Source and supported profile](#source-and-supported-profile)
- [Technical references](#technical-references)
- [Prepare and verify the structural environment](#prepare-and-verify-the-structural-environment)
- [Qualify an actual Windows host](#qualify-an-actual-windows-host)
- [Verification resources](#verification-resources)
- [Source ledger](#source-ledger)

## Source and supported profile

- Upstream: [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify/tree/16218bfc80d4ca2799734d045039f7ed1a5fa9fb), commit **`16218bfc80d4ca2799734d045039f7ed1a5fa9fb`**, distribution **`graphifyy==0.9.103`**, executable **`graphify`** (`graphify.__main__:main`). Distribution name and executable name differ.
- License: [Apache-2.0 LICENSE](https://github.com/Graphify-Labs/graphify/blob/16218bfc80d4ca2799734d045039f7ed1a5fa9fb/LICENSE); upstream also retains [LICENSE-MIT](https://github.com/Graphify-Labs/graphify/blob/16218bfc80d4ca2799734d045039f7ed1a5fa9fb/LICENSE-MIT) for earlier contributions and [NOTICE](https://github.com/Graphify-Labs/graphify/blob/16218bfc80d4ca2799734d045039f7ed1a5fa9fb/NOTICE): Graphify, copyright 2026 Safi Shamsi and the Graphify contributors. Preserve applicable license/notice text and identify modifications if later adopting upstream source or extraction prose. This slice vendors no upstream helper or specification; the probe is original test code calling the external package.
- Reviewed agent route: complete `graphify/skill-codex.md` and its extraction, update, query, exports, GitHub/merge, add/watch, hooks and transcription references, with corresponding implementations/tests. Windows preparation/PowerShell encoding and process-spawn differences were inspected at source level. Upstream skill instructions are evidence to assess, not an additional installed skill.
- Verified runtime profile: **Linux, CPython 3.12.14**, base distribution only: NetworkX 3.7, NumPy 2.5.4, PyYAML 6.0.3, RapidFuzz 3.14.6 and the upstream-required tree-sitter runtime/grammars, exactly listed in [graphify-requirements.txt](graphify-requirements.txt). No optional extras. Upstream metadata allows Python >=3.10, but these resolved NetworkX/NumPy pins require >=3.12; do not advertise this lock for 3.10/3.11. Other interpreters/platforms require a separately tested resolution.
- Core clustering uses NetworkX Louvain when optional Leiden libraries are absent. HTML needs no Python rendering extra. SVG requires optional matplotlib/Pillow; PDF/Office/video/SQL/other language extras are corpus-specific and outside this verified base profile. Neither `[all]`, MCP, a database, Graphify Cloud nor an API provider is needed.

The exercised lane is UTF-8 Python/Markdown on Linux CPython 3.12.14: native structural staging, current-subscription-agent mixed staging, conservative semantic-shard reuse, cold-checkout recovery, commit-coherent publication, bounded native investigation and selected exports. Python/Markdown files must contain no NUL bytes. A package grammar list does not certify other formats. Actual Windows/Work execution and independent end-to-end agent integration remain separate gates; replay, metadata checks and file creation do not establish them.

The source is pinned by commit and runtime dependencies by versions. Upstream build isolation still selects `setuptools>=83.0.0`; this is not a hash-locked wheel supply chain or a cross-host binary guarantee. Version/provenance checks do not detect local package tampering.

## Technical references

| Interface | Reference |
|---|---|
| Native detection/extraction, plan and fragment schemas, structural and mixed assembly | [Build recipes and contracts](graphify-build.md) |
| Portable state, profile/snapshot/reuse API, trio sealing and Git publication | [Maintenance interfaces](graphify-maintenance.md) |
| Strict-read loaders, query/path/neighborhood/impact and analysis | [Read interfaces](graphify-read.md) |
| HTML/report, GraphML/SVG/wiki/Obsidian and repository namespaces | [Export interfaces](graphify-export.md) |

Executable recipes remain direct calls to the pinned package; the `probe_*.py` files extract their marked blocks for regression checks. [validate_context_fragments.py](validate_context_fragments.py) supplies the demonstrated source/range/evidence and portable-state validation gap. [view_legend.py](view_legend.py) annotates native views. Neither helper is an extraction engine, provider client or workflow dispatcher.

## Prepare and verify the structural environment

Use an explicit task-owned interpreter outside the source tree. Check an existing candidate first; installation is needed only for an absent/incompatible candidate and an authorized preparation task. Offline reuse can use a verified installation; offline creation needs compatible cached artifacts. Installation requires Python/uv/Git, source/package retrieval, write access and suitable wheels/build tools. The package is not installed by merely reading this reference.

The following setup supplies the environment for [structural staging](graphify-build.md#build-and-inspect-structural-evidence). Replace placeholders with actual absolute paths. `GRAPHIFY_OUT` is read at import time and overrides cache-root placement; use a fresh process for another corpus/output. Native cache state assumes one corpus per process.

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

Run the profile block with that interpreter (`"$CONTEXT_PY" - <<'PY'`, the Python block, then `PY`). It executes no installer and writes no project references. Its VCS provenance check distinguishes the pinned source from another distribution carrying the same version.

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

qualification = os.environ.get("CONTEXT_QUALIFY_HOST", "")
if qualification:
    assert qualification == "windows-cpython-3.13", "Unknown qualification lane"
    assert sys.implementation.name == "cpython" and sys.platform == "win32" and sys.version_info[:2] == (3, 13), "Qualification requires actual Windows CPython 3.13"
    assert sys.flags.utf8_mode, "Windows qualification requires PYTHONUTF8=1 before interpreter startup"
    profile_status = "qualification-only-unverified"
else:
    assert sys.implementation.name == "cpython" and sys.version_info[:2] == (3, 12) and sys.platform == "linux", "This recorded profile requires Linux CPython 3.12; qualify another lane explicitly"
    profile_status = "verified-linux-runtime"
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
cli = Path(sys.executable).parent / ("graphify.exe" if sys.platform == "win32" else "graphify")
assert cli.is_file(), "Candidate CLI is missing; do not fall through to a global executable"
assert cli.resolve().is_relative_to(Path(sys.prefix).resolve()), "CLI escaped candidate environment"
if sys.platform == "win32":
    assert cli.read_bytes().startswith(b"MZ"), "Expected a Windows console launcher"
else:
    assert cli.read_text(encoding="utf-8").splitlines()[0] == "#!" + sys.executable, "Verify a nonstandard CLI launcher separately"
assert any(e.name == "graphify" and e.value == "graphify.__main__:main" for e in metadata.distribution("graphifyy").entry_points), "Unexpected CLI entry point"
version = subprocess.run([str(cli), "--version"], check=True, capture_output=True, text=True, timeout=30)
assert version.stdout.strip() == "graphify 0.9.103", version.stdout
print(json.dumps({"profile": profile_status, "platform": sys.platform, "python": sys.version.split()[0], "graphify": metadata.version("graphifyy"), "commit": origin["vcs_info"]["commit_id"]}))
```

Re-run the bounded native probes after an environment/profile change; imports alone do not verify source locations or direction. Keep a failing candidate unchanged. `graphify install`, global upgrades, instruction/hook installation and ambient-provider use are not part of these recipes. In a Windows venv the corresponding executables are `Scripts/python.exe` and `Scripts/graphify.exe`.

After the profile check, run the bounded compatibility probe with that same candidate and tool directory:

```sh
"$CONTEXT_PY" "$CONTEXT_TOOLS/probe_graphify.py"
```

## Qualify an actual Windows host

Windows CPython 3.13 is a qualification candidate. Set `CONTEXT_QUALIFY_HOST=windows-cpython-3.13` only on that real host; the check labels it `qualification-only-unverified`. Interpreter patch/platform participate in the portable profile, so a Linux generation is not automatically a Windows-compatible generation.

The PowerShell recipe below targets the reported actual Python 3.13.7 host. Supply the exact reviewed Skills commit, use a new short local task directory and start a new PowerShell process. Long paths and network/WSL shares are not qualified. The structural unsafe-symlink control requires already-authorized symlink permission and fails if absent. Git must support `--no-lazy-fetch` for commit-bound investigation; the exercised Linux Git was 2.52.0. Record the actual Windows Git version. The semantic/maintenance/investigation probes replay recorded model output; fresh independent agent reading, browser rendering and a separate Work host require their own evidence.

```powershell
# Set to the full reviewed Skills commit supplied by the owner/handoff:
$SkillsRevision = '<reviewed-Skills-commit>'
$ContextTask = Join-Path $env:TEMP ('context-win-' + [guid]::NewGuid().ToString('N'))
New-Item -ItemType Directory -Path $ContextTask -ErrorAction Stop | Out-Null
$ContextSource = Join-Path $ContextTask 'skills'
$env:PYTHONUTF8 = '1'
$env:PYTHONIOENCODING = 'utf-8'
$env:PYTHONDONTWRITEBYTECODE = '1'
$env:CONTEXT_QUALIFY_HOST = 'windows-cpython-3.13'
$env:GRAPHIFY_BACKEND = 'none'
$env:GRAPHIFY_QUERY_LOG_DISABLE = '1'
git -c core.autocrlf=false clone --no-checkout https://github.com/Krankort224/Skills.git $ContextSource
if ($LASTEXITCODE -ne 0) { throw 'Skills clone failed' }
git -C $ContextSource -c core.autocrlf=false checkout --detach $SkillsRevision
if ($LASTEXITCODE -ne 0) { throw 'Exact Skills checkout failed' }
$env:CONTEXT_TOOLS = Join-Path $ContextSource 'level-1/context/tools'
$ContextVenv = Join-Path $ContextTask 'venv'
py -3.13 -m venv $ContextVenv
if ($LASTEXITCODE -ne 0) { throw 'CPython 3.13 environment unavailable' }
$ContextPython = Join-Path $ContextVenv 'Scripts/python.exe'
& $ContextPython -c "import sys; assert sys.platform == 'win32' and sys.version_info[:3] == (3,13,7), sys.version; print(sys.version)"
if ($LASTEXITCODE -ne 0) { throw 'This rerun targets the reported actual Python 3.13.7 host' }
& $ContextPython -m pip install -r (Join-Path $env:CONTEXT_TOOLS 'graphify-requirements.txt')
if ($LASTEXITCODE -ne 0) { throw 'Pinned candidate installation failed; do not relax requirements' }
git --version
$env:CONTEXT_MAINTENANCE_EVIDENCE = Join-Path $ContextTask 'f-evidence'
$env:CONTEXT_INVESTIGATION_EVIDENCE = Join-Path $ContextTask 'g-evidence'
foreach ($Probe in @('probe_graphify.py', 'probe_graphify_structure.py', 'probe_graphify_semantic.py', 'probe_graphify_maintenance.py', 'probe_graphify_investigation.py')) {
    & $ContextPython -B (Join-Path $env:CONTEXT_TOOLS $Probe)
    if ($LASTEXITCODE -ne 0) { throw ('Qualification stopped: ' + $Probe + '; preserve ' + $ContextTask) }
}
Write-Output ('Candidate replay finished; retain actual outputs/evidence in ' + $ContextTask)
```

An existing isolated candidate can replace the creation/install lines with its actual `Scripts/python.exe`; all checks still target the same reviewed Skills revision. Do not alter platform, interpreter, provenance or pins to bypass a failure. Record failed/blocked stages separately from earlier successful ones. Publication tests exercise local bare repositories, cooperative locks, killed-holder recovery and independent-clone leases; they certify only the filesystem/host exercised, not hosted transport or every Windows filesystem. Optional SVG has a separate plotting resolution.

## Verification resources

| Resource | Reproducible evidence and limit |
|---|---|
| [probe_graphify.py](probe_graphify.py) | Package identity; Python/Markdown detection, exclusions, directed calls, code/document references, Unicode and long-tail source locations; native fragment ingestion, trio/reload, origin/tier and cache controls; bounded query with unchanged fixtures. Authored fragments establish ingestion, not fresh semantic reading or browser rendering. |
| [probe_graphify_structure.py](probe_graphify_structure.py) and [structural cases](graphify-structural-cases.json) | Execute the profile and structural recipes on bounded raw fixtures, including negative input/exclusion controls. |
| [probe_graphify_semantic.py](probe_graphify_semantic.py) and [semantic cases](graphify-semantic-cases.json) | Replay recorded genuine model output through expected-shard/range/EOF validation and native assembly; serial/parallel accounting, negative/uncertain/historical roles, unknown usage, tier and failure controls. |
| [probe_graphify_maintenance.py](probe_graphify_maintenance.py) and [maintenance cases](graphify-maintenance-cases.json) | Add/edit/rename/delete/exclude; edge-only/zero replacements; dependency/profile invalidation and no-op; cold moved clones, branches/worktrees; local bare publication, leases, dirty/nonbare/partial/corrupt refusal, lost acknowledgement, compatible rollback and interrupted export. |
| [probe_graphify_investigation.py](probe_graphify_investigation.py) and [investigation cases](graphify-investigation-cases.json) | Execute strict-read, real-commit binding and namespace recipes against fresh recorded fixtures; query/path/impact/community and ambiguity/budget controls, namespace round trips, export ownership and HTML aggregation. |
| [probe_view_legend.py](probe_view_legend.py) | Pure HTML/SVG annotation checks; no replacement for a rendered-view inspection. |

Run probes with the verified interpreter without optimization; `PYTHONDONTWRITEBYTECODE=1` keeps fixture reads free of bytecode writes. Probes use temporary fixtures and forbid network/provider extraction in the exercised route. Optional `CONTEXT_MAINTENANCE_EVIDENCE` and `CONTEXT_INVESTIGATION_EVIDENCE` retain inspectable evidence only in a new external directory; existing targets are refused. These are test outputs, not additional portable graph artifacts.

Replay checks integration/accounting, not a fresh model run or blind benchmark. New semantic trials expose raw inputs and the method to the reader while keeping recorded answers/oracles separate. Rendering, format readability, actual host execution and independent end-to-end behavior require their specific observations. Test chronology and exact results belong to the task's evidence/Issue when applicable; this reference records durable interfaces and compatibility boundaries.

## Source ledger

All pointers use the pinned upstream revision; upstream agent prose is reviewed source material, not an installed skill.

- [Agent workflow](https://github.com/Graphify-Labs/graphify/blob/16218bfc80d4ca2799734d045039f7ed1a5fa9fb/graphify/skill-codex.md), [extraction specification](https://github.com/Graphify-Labs/graphify/blob/16218bfc80d4ca2799734d045039f7ed1a5fa9fb/graphify/skills/codex/references/extraction-spec.md), [update reference](https://github.com/Graphify-Labs/graphify/blob/16218bfc80d4ca2799734d045039f7ed1a5fa9fb/graphify/skills/codex/references/update.md), [Windows variant](https://github.com/Graphify-Labs/graphify/blob/16218bfc80d4ca2799734d045039f7ed1a5fa9fb/graphify/skill-windows.md).
- [Package metadata](https://github.com/Graphify-Labs/graphify/blob/16218bfc80d4ca2799734d045039f7ed1a5fa9fb/pyproject.toml): runtime/extras, Python, entry point, licenses. `graphify/__main__.py` resolves installed version and dispatches CLI.
