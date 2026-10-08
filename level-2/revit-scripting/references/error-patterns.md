# Error patterns

Select the first violated invariant and a discriminating check; do not apply every row as a checklist.

| Symptom | Boundary | Check | Correction |
| --- | --- | --- | --- |
| List/string instead of expected number/table | Wiring/schema | Actual port endpoints, producer shape, IN contract | Fix wire or explicit adapter |
| Missing OUT member despite valid wire | Legacy positional schema | Producer indices/headers vs consumer | Synchronize named/versioned contract |
| Works offline, fails in Dynamo | Runtime/wrapper/overload | Engine/build and native types | Tested host adapter and boundary unwrapping |
| Plausible but wrong magnitude | Units/specification | Typed quantity and conversions end to end | Explicit conversion; reject failures |
| Unpredictable parameter selection | Names/scope | All matches and instance/type owner | BIP/GUID/exact binding; reject ambiguity |
| Huge/repeated network selection | Logical edges/unbounded scan | Domain/type/IsConnectedTo and trace | Physical snapshot, caps and boundaries |
| Connectivity changes after regeneration | Stale handles | Reacquire owners/connectors | New handles for native readback |
| Rotated link/view shifts coordinates | Wrong frame | Known points and all bbox corners | Explicit point/vector transforms |
| Nearby unrelated element matched | Weak identity/uniqueness | Document/family/system/size/reservations | Reject ambiguous/occupied candidates |
| Reference parses, creation fails | Suitability/view geometry | Owner/link and referenced geometry | Actual native refs and suitability predicate |
| Commit attempted, no durable change | Failure handling | Returned/current statuses and rollback | Report non-commit/Pending; follow owner lifecycle |
| Partial rows reported complete | Batch/outer commit | Requested/changed/skipped/failed counts | Partial receipt and declared rollback policy |
| Fallback succeeds, intended geometry fails | Planner/executor divergence | Intended vs actual coordinates/refs | Fix owning plan; report fallback separately |
| Old run conflicts with current state | Stale/incomplete evidence | Revision, profile, run and latest raw case | Collect bounded current probe |

For write corrections use [transactions](transactions.md); for raw wire mismatches use [Dynamo](dynamo.md). Project failure diaries/logs remain with their project owners.
