# Borrowing

## Inputs

Use a script, graph, archive or pinned repository source and the behavior worth reusing. An example is evidence, not authorization to execute its writes or copy project assumptions.

## Procedure

1. Inventory relevant helpers/entry points. Inspect graphs and embedded Python with `scripts/inspect_dyn.py`. Pin repository commit/path or archive hash/graph/node; identify callers, inputs, transaction owner and evidence.
2. Choose one independently useful behavior. Separate bindings, UI state, globals and pipeline schemas from the mechanism. Record source limitations that materially affect transfer.
3. Check the [catalog](../assets/blocks/catalog.md) for an existing owner. Extend that block for the same behavior; avoid project-name variants.
4. Create one Markdown file under `assets/blocks/core/`, `mep/` or `views/`. Use the structure below with one self-contained `python` implementation fence. Declare dependencies only when callers must load/copy another block.
5. Replace implicit document/view, paths, name heuristics and silent unit/scope fallbacks with explicit inputs or rejection. Bound traversal, ambiguity, mutation and failures.
6. Add targeted tests loading the fence. Exercise substantive success/failure cases; keep mocks explicit. Review API semantics for the target profile. Link native evidence only when this generalized block was run.
7. Mark `reviewed` after recorded checks pass. Keep `verification: static` or `offline` if native behavior is untested. Validate with `scripts/check_library.py`, regenerate via `--catalog`, and check links.

## Canonical block structure

Use `# Title` and nonempty headings `## Contract`, `## Purpose`, `## Inputs and outputs`, `## Implementation`, `## Adaptation and limits`, `## Verification`, `## Provenance`. Add contents for files longer than 100 lines.

| Contract field | Values |
| --- | --- |
| `id` | Unique kebab-case filename stem |
| `group` | `core`, `mep` or `views`, matching folder |
| `status` | `draft` or `reviewed` |
| `runtime` | Explicit Python/Revit/host assumptions |
| `verification` | `static`, `offline` or `runtime`; definitions in [SKILL](../SKILL.md#reuse-the-block-library) |
| `dependencies` | `none` or comma-separated existing IDs, no cycles |
| `mutation` | `read-only`, `document-write`, `view-write` or `file-write` |

Provenance identifies source commit/path/function or archive SHA256/graph/node and substantive adaptations. An original source link does not prove the new block's native behavior.

## Result and completion

Deliver reviewed block, tests and derived catalog entry with actual verification limits. Keep full archives, reports and native logs with project owners; include only small synthetic shared examples.
