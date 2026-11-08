# Graphify: native read interfaces

Question selection, identity resolution and source follow-through: [read a graph](../operations/graphify/read.md). Runtime: [technical profile](graphify.md). Trio integrity/currentness API: [maintenance reference](graphify-maintenance.md).

## Contents

- [Read effects and memory boundary](#read-effects-and-memory-boundary)
- [Validated graph recipe](#validated-graph-recipe)
- [Traversal and analysis limits](#traversal-and-analysis-limits)
- [Source ledger](#source-ledger)

## Read effects and memory boundary

CLI `query`, `path` and `explain` call `_touch_query_stamp` and attempt `cache/last_query_stamp` beside the graph. Optional query logging can be disabled process-locally with `GRAPHIFY_QUERY_LOG_DISABLE=1`; that does not remove the CLI stamp. Server `_read_graph` can also load a neighboring learning sidecar and hash its referenced sources.

The recipe below works from `validate_trio`'s exact consumed graph dict, without `graph_path` or `_read_graph`, stamps/logs, sidecars, servers, providers, installation or rebuild. Set `PYTHONDONTWRITEBYTECODE=1` before launching the verified interpreter. The structural-only stage has a [separate bounded no-sidecar query](graphify-build.md#bounded-structural-stage-query).

The validator loads bounded full artifact buffers and NetworkX loads the full graph in memory. Bounded agent-visible output is not streaming or bounded-load evidence. Large portable payloads/metadata are not a useful candidate list; the recipe prints needed IDs, labels and source locators.

## Validated graph recipe

Inputs: `CONTEXT_ROOT`, `CONTEXT_TRIO`, `CONTEXT_TOOLS`, `CONTEXT_SEED` and `CONTEXT_QUESTION`; optional `CONTEXT_TARGET` enables a directed path. The trio view contains one immutable generation. Currentness claims require the operation's source/profile assessment; checksum integrity alone does not prove current sources. Both endpoints must resolve unambiguously.

The direct native APIs are pinned private interfaces, so an upstream upgrade requires their regression checks.

```python
# context-investigate
import sys
sys.dont_write_bytecode = True
import importlib.util
import os
from pathlib import Path
from graphify.paths import load_node_link_graph
from graphify.serve import _resolve_single_node, _query_graph_text, _neighbor_lines, _cut_lines_to_budget, _shortest_path_text

root = Path(os.environ["CONTEXT_ROOT"]).resolve(strict=True)
view = Path(os.environ["CONTEXT_TRIO"]).resolve(strict=True)
module = Path(os.environ["CONTEXT_TOOLS"]) / "validate_context_fragments.py"
spec = importlib.util.spec_from_file_location("context_read_validator", module)
validator = importlib.util.module_from_spec(spec)
spec.loader.exec_module(validator)
checked = validator.validate_trio(view, root=root, require_current=True)
G = load_node_link_graph(checked["graph"])
assert G.is_directed()
seed, refusal = _resolve_single_node(G, os.environ["CONTEXT_SEED"])
if refusal:
    raise ValueError(refusal)
print("Input:", checked["input_identity"], "Generation:", checked["generation_identity"])
print("Node:", {k: G.nodes[seed].get(k) for k in ("label", "source_file", "source_location", "_origin")})
print(_query_graph_text(G, os.environ["CONTEXT_QUESTION"], seeds=[seed], seed_root=root, mode="bfs", depth=2, token_budget=1200))
print(_cut_lines_to_budget(_neighbor_lines(G, seed), 1200, "Narrow the node or relationship"))
if os.environ.get("CONTEXT_TARGET"):
    target, refusal = _resolve_single_node(G, os.environ["CONTEXT_TARGET"])
    if refusal:
        raise ValueError(refusal)
    print(_shortest_path_text(G, {"source": seed, "target": target, "max_hops": 8}))
```

## Traversal and analysis limits

| Interface | Technical behavior |
|---|---|
| `_resolve_single_node` | Exact node ID or uniquely qualified identity; fuzzy CLI scoring does not replace disambiguation. |
| `_query_graph_text` with BFS/DFS | Undirected context gathering. Nonseed hubs at/above `max(50, p99 degree)` are not expanded. Filters, depth and output budget can omit evidence. |
| `_neighbor_lines` | Immediate incoming/outgoing relation, confidence and source sites. |
| `_shortest_path_text` | Follows directed stored arcs/legacy markers with an implied reverse `contains` hop from symbol to owning file. The reverse arrow is not a forward runtime dependency. `max_hops` limits the reported result after search; at most 256 equal shortest routes; confidence reflects weakest evidence. |
| `resolve_seed_outcome` / `affected_nodes` | Reverse impact over explicit relation names and depth, with static native class/member/override handling. Default relations exclude arbitrary semantic relation names. |
| `god_nodes(G, top_n=5)` | Degree ranking with native file/builtin/no-source-concept noise heuristics; source-backed semantic concepts may remain. |
| `surprising_connections(G, communities, top_n=5)` | For multi-source graphs, ranks cross-file connections including within-community edges; single-source fallback uses cross-community/centrality. It is not an exhaustive cut-edge algorithm. |

Native token budget is approximate: all-fits results can exceed it with a notice. `_cut_lines_to_budget` formats an already-built list. A hard host output cap needs a smaller query/depth or split result; truncation never establishes absence. Path text may omit source sites, which remain in neighbor/source records.

For selected impact, inspect actual relation names before calling `graphify.affected.resolve_seed_outcome(G, query, root)` and `affected_nodes(G, seed, relations=("calls", "implements_current_grant_window"), depth=2)`. That tuple is illustrative, not a universal relation set. Bound returned hits and retain `node_id`, `depth`, `via_file`, `via_location`, matched relation and omitted count. Empty impact with wrong/default filters does not demonstrate no impact.

Existing `community` attributes and the generation's stored interpretation permit membership inspection without reclustering/renaming. Degree-zero nodes and weak components can reflect coverage/parser boundaries or distinct source roles. A hub/bridge heuristic mentioning directories does not establish repository boundaries, architecture, authority, runtime reachability or test coverage. Graph-assisted and direct-source effort comparisons belong to a requested investigation, not an automatic benchmark on every read.

## Source ledger

- [Traversal](https://github.com/Graphify-Labs/graphify/blob/16218bfc80d4ca2799734d045039f7ed1a5fa9fb/graphify/serve.py): query 1490, undirected context walks 1436, directional path 2287–2530, source/confidence rendering 1168–1381. These functions also serve CLI calls; no MCP service is required. `affected.py` 302–388 owns bounded reverse impact; `analyze.py` owns graph differences (637), hubs and bridges; `cluster.py` owns Louvain/Leiden and cohesion.
