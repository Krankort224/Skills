# Graphify: technical profile

This reference owns the pinned package and runtime preparation for project graph operations. Select the operation from [context](../SKILL.md#graph-evidence-and-technical-references).

## Contents

- [Source and supported profile](#source-and-supported-profile)
- [Technical references](#technical-references)
- [Prepare and verify the structural environment](#prepare-and-verify-the-structural-environment)
- [Source ledger](#source-ledger)

## Source and supported profile

- Upstream: [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify/tree/16218bfc80d4ca2799734d045039f7ed1a5fa9fb), commit **`16218bfc80d4ca2799734d045039f7ed1a5fa9fb`**, distribution **`graphifyy==0.9.103`**, executable **`graphify`** (`graphify.__main__:main`). Distribution name and executable name differ.
- License: [Apache-2.0 LICENSE](https://github.com/Graphify-Labs/graphify/blob/16218bfc80d4ca2799734d045039f7ed1a5fa9fb/LICENSE); upstream also retains [LICENSE-MIT](https://github.com/Graphify-Labs/graphify/blob/16218bfc80d4ca2799734d045039f7ed1a5fa9fb/LICENSE-MIT) for earlier contributions and [NOTICE](https://github.com/Graphify-Labs/graphify/blob/16218bfc80d4ca2799734d045039f7ed1a5fa9fb/NOTICE): Graphify, copyright 2026 Safi Shamsi and the Graphify contributors. Preserve applicable license/notice text and identify modifications if later adopting upstream source or extraction prose. This slice vendors no upstream helper or specification; the probe is original test code calling the external package.
- Reviewed agent route: complete `graphify/skill-codex.md` and its extraction, update, query, exports, GitHub/merge, add/watch, hooks and transcription references, with corresponding implementations/tests. Windows preparation/PowerShell encoding and process-spawn differences were inspected at source level. Upstream skill instructions are evidence to assess, not an additional installed skill.
- Pinned base distribution for **Linux CPython 3.12** and **Windows CPython 3.13 in UTF-8 mode**: NetworkX 3.7, NumPy 2.5.4, PyYAML 6.0.3, RapidFuzz 3.14.6 and the upstream-required tree-sitter runtime/grammars, exactly listed in [graphify-requirements.txt](graphify-requirements.txt). No optional extras. Upstream metadata allows Python >=3.10, but these resolved NetworkX/NumPy pins require >=3.12; do not advertise this lock for 3.10/3.11. Other interpreters/platforms require a separately tested resolution.
- Core clustering uses NetworkX Louvain when optional Leiden libraries are absent. HTML needs no Python rendering extra. SVG requires optional matplotlib/Pillow; PDF/Office/video/SQL/other language extras are corpus-specific and outside this verified base profile. Neither `[all]`, MCP, a database, Graphify Cloud nor an API provider is needed.

The project build recipes cover UTF-8 Python and Markdown sources without NUL bytes. Recorded Linux CPython 3.12.14 evidence includes structural and mixed staging, semantic reuse, cold-checkout recovery, Git publication, investigation and selected exports. Windows CPython 3.13.7 evidence includes the runtime probe and a scoped Markdown project rebuild. The portable profile records the actual OS and interpreter patch version for reuse decisions.

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

On Windows, use the same settings in PowerShell and enable UTF-8 mode before starting Python.

```powershell
$ContextVenv = 'C:\path\to\task\graphify-venv'
$ContextPython = Join-Path $ContextVenv 'Scripts/python.exe'
$env:CONTEXT_TOOLS = 'C:\path\to\Skills\level-1\context\tools'
$env:CONTEXT_ROOT = 'C:\path\to\project'
$env:CONTEXT_STAGE = 'C:\path\to\task\fresh-structural-stage'
$env:GRAPHIFY_OUT = Join-Path $env:CONTEXT_STAGE 'native-cache'
$env:GRAPHIFY_BACKEND = 'none'
$env:GRAPHIFY_QUERY_LOG_DISABLE = '1'
$env:PYTHONDONTWRITEBYTECODE = '1'
$env:PYTHONUTF8 = '1'
$env:PYTHONIOENCODING = 'utf-8'
```

To prepare a new authorized Windows environment, run `py -3.13 -m venv $ContextVenv` and install the pins with `& $ContextPython -m pip install -r (Join-Path $env:CONTEXT_TOOLS 'graphify-requirements.txt')`.

Save the profile block as a UTF-8 Python file in the task directory. Run it with the selected interpreter, for example `& $ContextPython 'C:\path\to\task\profile-check.py'` in PowerShell. The VCS provenance check distinguishes the pinned source from another distribution carrying the same version.

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

assert sys.implementation.name == "cpython", "Expected CPython"
runtime = (sys.platform, sys.version_info[:2])
assert runtime in {("linux", (3, 12)), ("win32", (3, 13))}, "Expected Linux CPython 3.12 or Windows CPython 3.13"
if sys.platform == "win32":
    assert sys.flags.utf8_mode, "Windows requires UTF-8 mode before interpreter startup"
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
print(json.dumps({"platform": sys.platform, "python": sys.version.split()[0], "graphify": metadata.version("graphifyy"), "commit": origin["vcs_info"]["commit_id"]}))
```

Verify a new or changed runtime with the [bounded runtime probe](probe_graphify.py). It checks native detection, directed extraction, source locations, fragment ingestion, exports and queries on regular files. Use the same interpreter and the environment above.

```sh
"$CONTEXT_PY" "$CONTEXT_TOOLS/probe_graphify.py"
```

```powershell
& $ContextPython (Join-Path $env:CONTEXT_TOOLS 'probe_graphify.py')
```

Then verify the selected project inputs and outputs through the [build recipe](graphify-build.md#build-and-inspect-structural-evidence). Keep a failing candidate unchanged for diagnosis. Limit setup to the pinned packages in the isolated environment and keep the provider disabled.

## Source ledger

All pointers use the pinned upstream revision; upstream agent prose is reviewed source material, not an installed skill.

- [Agent workflow](https://github.com/Graphify-Labs/graphify/blob/16218bfc80d4ca2799734d045039f7ed1a5fa9fb/graphify/skill-codex.md), [extraction specification](https://github.com/Graphify-Labs/graphify/blob/16218bfc80d4ca2799734d045039f7ed1a5fa9fb/graphify/skills/codex/references/extraction-spec.md), [update reference](https://github.com/Graphify-Labs/graphify/blob/16218bfc80d4ca2799734d045039f7ed1a5fa9fb/graphify/skills/codex/references/update.md), [Windows variant](https://github.com/Graphify-Labs/graphify/blob/16218bfc80d4ca2799734d045039f7ed1a5fa9fb/graphify/skill-windows.md).
- [Package metadata](https://github.com/Graphify-Labs/graphify/blob/16218bfc80d4ca2799734d045039f7ed1a5fa9fb/pyproject.toml): runtime/extras, Python, entry point, licenses. `graphify/__main__.py` resolves installed version and dispatches CLI.
