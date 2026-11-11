# Assess Graphify compatibility

Use this operation to determine which Graphify functions work in a specified environment. Define the requested operations, inputs, required guarantees, actual runtime and filesystem, and current rights. Use the pinned [technical profile](../../tools/graphify.md) to prepare the candidate and the selected project operation to exercise its normal entry point.

A check is required when its result or equivalent evidence is needed to justify the conclusion about an operation or guarantee in scope. Select checks by that criterion. Exercise the applicable steps with current rights and continue independent checks when a step is blocked.

## Conclude with current rights

Give one evidence-backed verdict for the scope you can establish.

- **Will work.** Every required operation and guarantee is demonstrated in the stated environment.
- **Will work with limitations.** Evidence demonstrates a usable workflow under narrower conditions than requested. State the conditions and the affected operations, inputs or guarantees.
- **Will not work.** Evidence shows that a required operation or guarantee is unavailable in the stated environment with current rights.

Report unresolved required evidence separately. If a test cannot create its fixture, record the resulting gap in coverage. For example, failure to create an out-of-root symlink leaves that probe incomplete. A successful ordinary rebuild from regular files supports a verdict for that rebuild.

Before requesting additional rights, give an evidence-backed verdict with current rights for the scope established. Identify the remaining required check, how it could change the conclusion for the requested scope, and why checks with current rights cannot supply equivalent evidence. If the evidence supports no verdict yet, report the specific gap and continue the available checks.

## Select checks for the requested guarantees

| Resource | Evidence |
|---|---|
| [Runtime probe](../../tools/probe_graphify.py) | Pinned package, native Python/Markdown extraction, directions and source locations, fragment ingestion, exports and queries on bounded fixtures. |
| [probe_graphify_structure.py](../../tools/probe_graphify_structure.py) and [structural cases](../../tools/graphify-structural-cases.json) | Execute the profile and structural recipes on bounded raw fixtures, including negative input/exclusion controls. |
| [probe_graphify_semantic.py](../../tools/probe_graphify_semantic.py) and [semantic cases](../../tools/graphify-semantic-cases.json) | Replay recorded genuine model output through expected-shard/range/EOF validation and native assembly; serial/parallel accounting, negative/uncertain/historical roles, unknown usage, tier and failure controls. |
| [probe_graphify_maintenance.py](../../tools/probe_graphify_maintenance.py) and [maintenance cases](../../tools/graphify-maintenance-cases.json) | Add/edit/rename/delete/exclude; edge-only/zero replacements; dependency/profile invalidation and no-op; cold moved clones, branches/worktrees; local bare publication, leases, dirty/nonbare/partial/corrupt refusal, lost acknowledgement, compatible rollback and interrupted export. |
| [probe_graphify_investigation.py](../../tools/probe_graphify_investigation.py) and [investigation cases](../../tools/graphify-investigation-cases.json) | Execute strict-read, real-commit binding and namespace recipes against fresh recorded fixtures; query/path/impact/community and ambiguity/budget controls, namespace round trips, export ownership and HTML aggregation. |
| [probe_view_legend.py](../../tools/probe_view_legend.py) | Pure HTML/SVG annotation checks; no replacement for a rendered-view inspection. |

Run selected probes individually with the verified interpreter and the [runtime settings](../../tools/graphify.md#prepare-and-verify-the-structural-environment). The structural probe creates a symlink to a file outside the fixture corpus. The maintenance probe uses symlinks for unsafe publication targets and exercises native locks and Git leases on a local bare remote. Record the filesystem and Git version for these claims. Commit-bound investigation requires Git with `--no-lazy-fetch`.

Run without optimization. Use fresh external directories when retaining `CONTEXT_MAINTENANCE_EVIDENCE` or `CONTEXT_INVESTIGATION_EVIDENCE`. Probes forbid network/provider extraction on their exercised routes. Recorded semantic replay establishes integration and accounting. Fresh reading, browser rendering and independent end-to-end behavior each require evidence for the requested operation.
