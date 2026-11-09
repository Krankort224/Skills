# Publication and replay

Read this before workflow/material writes. This is a direct-writer procedure, not permission to weaken the owning protocol. The current `docs/storage-protocol.md` and validators own exact schemas; read the relevant implementation when versions differ.

## Source routes and accepted state

| Concern | Project-space implementation |
| --- | --- |
| Workflow closed schemas and legacy read compatibility | `app/src-tauri/src/core/protocol.rs`: `EventRecord::parse`, `Event::validate_schema`, `task_content_shape` |
| Domain transitions and actual actor relationships | `core/domain.rs`: `apply`, proposal/result helpers |
| Causal validation, forks, accepted prefixes, diagnostics | `core/replay.rs`: `Evaluator::evaluate_context`, `replay` |
| Command-time heads, authorization snapshot, publication | `core/commands.rs`: `prepare`, `validate_new`, `publish_prepared` |
| Paths, exact final bytes, pending and no-replace rename | `core/store.rs`: `scan_project`, `is_published`, `publish` |
| Activated global task-number authority, old-task backfill and create reservation | `core/task_numbers.rs` and `core/store.rs`; `docs/storage-protocol.md` §1.1 |
| Current registry and historical snapshots | `core/access.rs`: `AccessRevision::snapshot`, `AccessStore::with_current` |
| Material reducer, operation plans and publication | `core/materials.rs`; see [Materials](materials.md) |

Paths abbreviated as `core/...` are under `app/src-tauri/src/`. Desktop DTOs in `workspace.rs` help map a request, but event payloads are not those DTOs verbatim.

Read immutable finals from the expected namespace and verify location, store/project/stream identity, exact bytes, closed JSON schemas, UUIDv7/SID/time forms and hash/size fields. Reject duplicate keys at every level and noninteger/out-of-range numeric values. Ignore `.tmp`; preserve unknown files. Reject reparse points/symlinks in store descendants.

Build the causal graph from `base_event_id`, `project_auth_event_id` and `depends_on`. Validate each candidate against its own causal context, schema, historical authorization and domain transition **before** selecting branches. Distinguish missing dependency, invalid transition, cycle, unsupported schema, identity collision, fork and blocked descendant. Two valid state candidates sharing the same stream/base freeze that stream at its unambiguous prefix; a later dependency failure must not promote the sibling. Prune effects whose dependencies are not accepted. Materialize accepted events in causal order; additive legacy records do not advance state heads. Match `replay.rs`, including identity collisions across entity/event/artifact IDs and project-authorization non-regression.

For a new command, require the target stream and necessary parent/authorization streams to be ready. An unrelated task conflict does not block all project work. Material replay additionally validates its topic chain, workflow references, drafts and origin rules. Never use latest filename/time/UUID, directory enumeration order or an edited SQLite row as the current state.

Ordinary synchronization inventories all final IDs in the relevant namespaces and reads only unknown records. Reuse previously validated immutable bytes/hashes and normalized local projections; no timestamp/UUID watermark. Direct dependencies and affected-scope validation must give the same result as cold replay. A warm read does not detect hidden rewrites of an already validated immutable file: use the explicit full integrity audit for that storage fault. Missing known finals are an error/uncertain view, never a deletion command. Failed discovery retains the last verified projection without calling it current. SQLite is disposable derived state; generation-CAS updates prevent stale local refreshes overwriting newer ones, with network I/O outside the SQL transaction. Keep pending/plans separate.

Prefer an available current core for these checks. A direct adapter must implement equivalent validation for the encountered records and proposed operation; read/test additional supported forms when encountered. Do not silently discard unfamiliar records or claim full replay from a permissive subset. Preserve affected data and report the exact unvalidated condition if equivalence cannot be established.

## Prepare one workflow event

All new workflow publications use envelope protocol 2. Store metadata may be version 1 before task-number activation or version 2 afterward; those versions are independent of event envelopes. A current writer must obey the numbering/activation contract in `docs/storage-protocol.md` §1.1. The closed envelope is:

```text
protocol_version: 2
store_id, event_id, project_id: canonical UUIDv7 strings
stream: {kind: project|topic|task, id: entity UUIDv7}
actor_sid: actual registered Windows process SID
recorded_at: automatically generated UTC RFC3339 with milliseconds and Z
type: supported event name
kind: state
base_event_id: accepted head of this stream, or null for its creation
project_auth_event_id: healthy current project head; null only for project.created
authorization: {registry_revision, participants, actor_root, actor_project_create}
depends_on: sorted unique additional event IDs
payload: closed object for the selected operation
```

`authorization.registry_revision` is lowercase SHA-256 of exact current `metadata/access.json` bytes. `participants` is the current registry's project membership transformed exactly as `AccessRevision::snapshot` does, including its resolved display names; `actor_root` and `actor_project_create` come from that same validated registry. Do not copy the raw schema-2 member records verbatim or invent inherited privilege entries. Historical snapshots are historical assertions, not today's access authority.

Entity and event IDs must differ. Creation has `base_event_id = null`; every other event names its own stream's accepted head. A project update uses the same ID for `base_event_id` and `project_auth_event_id`. `topic.created.depends_on` includes the accepted `project.created` event; `task.created.depends_on` includes the accepted parent `topic.created` event. All references stay within the same store/project and satisfy causal authorization non-regression.

The only new task-content form uses `title`, `description` and `deadline`. Use empty strings for empty descriptions, never old `wording`/`task_type`. New task creation has `initial_artifacts: []`; submission and self-completion have `result_artifact_ids: []`. New materials use the separate journal, not legacy `artifact.added`/`topic.material_added`.

Capture expected heads and raw access revision; derive the operation and replay the candidate with existing records. It must be accepted and authorized as the actual actor. Serialize final bytes once as UTF-8 without BOM and store event ID, length and SHA-256. Future retry uses these exact bytes.

## Task-number authority and creation

`metadata/store.json` protocol 1 means numbering is **not yet activated**. Its one-time protocol-2 activation may occur on the first upgraded workspace read or task creation, and requires a healthy **full-store** inventory/replay of accepted legacy creations under the existing `metadata/access.lock`. Allocate deterministic initial `#1..#N` by parsed creation UTC time, then creation event ID, then task ID; publish and read back a complete immutable-named number registry first, then atomically activate the protocol-2 `store.json` pointer. Once active, this pointed-to registry is **mandatory mutable shared authority**, not a disposable cache. Do not trigger this on a corporate store until all active clients are upgraded together and a complete store backup exists. A direct writer unable to prove this exact activation procedure must stop instead of producing a partial upgrade.

The activated `metadata/task-number-registry-<UUIDv7>.json` has a closed `schema_version:1` document with `store_id`, `next_number` and `entries`: task UUID → `{number, project_id, creation_event_id, creation_sha256}`. The number is a positive integer in the safe JSON range; allocations are globally sequential **including unfinished reservations**, and `next_number` follows all entries. The activation filename and store identity must match `store.json`. Registry structural/identity faults, missing active registry or mismatching sealed creation hashes fail closed. Never recreate an active authority by sorting events, assign a fresh number to an existing task, or edit creation history.

For each new `task.created`: prepare and seal the normal event **without** its display number. Under the **existing final `access.lock` gate**, first check for an already present exact final; confirmation also verifies the existing number binding and never repairs missing authority. For an unpublished event, refresh and validate current access, required heads/health and unchanged command intent; establish active numbering through the separately authorized activation above if needed, then durably save the exact bytes in local pending. Reserve the next `#n` by atomic full-registry CAS replacement and exact readback, bound to task/project/event UUIDs and SHA-256 of the sealed bytes. Then publish/read back the *same* immutable creation event under that gate. A retry with the same exact sealed event reuses its reservation; a different event/hash for an occupied task ID is a conflict. A failed or uncertain publication may leave a gap forever; never recycle it. Keep pending until exact final confirmation, and verify the mapping against accepted creation on read/replay.

Ordinary healthy workspace refresh loads the shared registry once per snapshot rather than per task, without rereading all historical workflow records. Cache deletion cannot change numbers; a damaged/lost **active** registry requires operator recovery from a consistent **full-store backup** (events plus metadata and registry). The task-number registry is **not** an authority for material permissions. The transport helper in `scripts/file_transport.py` does not implement this business transaction, validator, backfill or recovery.

## Publish immutable bytes

1. Confirm the initialized store identity and schema/cutover markers. Resolve a private local recovery directory outside the shared store and Git. Preserve existing pending records; never repurpose a different actor/store's operation.
2. Preserve the exact sealed workflow bytes and expected revisions in the private recovery plan. For coordinated/material operations use their specific durable package as well. A receipt records caller confirmation context without changing the event schema. Before command publication or task-number reservation, persist exact workflow bytes atomically as `<local>/pending/<event_id>.json`; for new tasks, do this after final validation inside the gate below.
3. Acquire the persistent `metadata/access.lock` with Windows read/write, no truncation/sharing, open-reparse-point and opened-handle regular-file validation. **Inside this gate**, first confirm an already present exact final if applicable; otherwise perform fresh relevant discovery and recheck exact registry revision/snapshot, required heads/health and the prepared operation. A check done only before acquiring the lock cannot exclude a competing manager. Keep the gate through required create-task number reservation/readback (above) and no-replace event publication/readback. Reuse the existing gate rather than adding stream locks or a shared head file; it does not make a multi-event batch a distributed transaction. Material lifecycle locks, when required, come first.
4. In `events/<project_id>/`, create a unique `.<event_id>.<attempt_id>.tmp`, write all prepared bytes, flush to disk, close, then rename to `<event_id>.json` without replacement on the same filesystem. Windows: `MoveFileExW` with `MOVEFILE_WRITE_THROUGH`, **without** `MOVEFILE_REPLACE_EXISTING`. Configuration CAS replacement uses a different protocol. Publish material blobs/journal records in their namespaces and required lock order instead.
5. Read the final bytes and confirm exact match, identity, length and hash. Same ID/different bytes is an integrity collision. Same ID/same bytes is confirmation of the previous publication, not a fresh command. Keep pending on unknown outcome; remove the matching workflow pending only after exact publication is confirmed.
6. Release handles, rescan/replay and verify acceptance and requested semantic change. A final may be published but unapplied because a concurrent valid branch appeared. Preserve it and report the conflict; do not delete/rewrite branches or auto-publish a replacement action.

The importable [file_transport.py](../scripts/file_transport.py) implements only Windows persistent locks and immutable byte transport. The caller supplies validated root/relative paths, prepared bytes, pending strategy and all domain/access/replay checks. Acquire locks in the material-specific order when applicable. The module does not initialize a store, mutate access or clean up material versions.

For uncertain rename/network outcomes, check the original final ID first. Exact final bytes confirm publication even if the move call failed. If absent, retain the original bytes and revalidate original heads/access before retry. A stale prerequisite requires a new explicit action; do not regenerate an ID, alter the pending bytes, silently rebase or repeat a whole batch. Clean up only operation-owned temporary files, never arbitrary old files or persistent locks.


A missing active task-number registry, conflicting creation seal or unmapped late creation is a safe stop, not an invitation to allocate around corruption. Preserve original sealed bytes and reservations throughout recovery.
