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
| Current registry and historical snapshots | `core/access.rs`: `AccessRevision::snapshot`, `AccessStore::with_current` |
| Material reducer, operation plans and publication | `core/materials.rs`; see [Materials](materials.md) |

Paths abbreviated as `core/...` are under `app/src-tauri/src/`. Desktop DTOs in `workspace.rs` help map a request, but event payloads are not those DTOs verbatim.

Read immutable finals from the expected namespace and verify location, store/project/stream identity, exact bytes, closed JSON schemas, UUIDv7/SID/time forms and hash/size fields. Reject duplicate keys at every level and noninteger/out-of-range numeric values. Ignore `.tmp`; preserve unknown files. Reject reparse points/symlinks in store descendants.

Build the causal graph from `base_event_id`, `project_auth_event_id` and `depends_on`. Validate each candidate against its own causal context, schema, historical authorization and domain transition **before** selecting branches. Distinguish missing dependency, invalid transition, cycle, unsupported schema, identity collision, fork and blocked descendant. Two valid state candidates sharing the same stream/base freeze that stream at its unambiguous prefix; a later dependency failure must not promote the sibling. Prune effects whose dependencies are not accepted. Materialize accepted events in causal order; additive legacy records do not advance state heads. Match `replay.rs`, including identity collisions across entity/event/artifact IDs and project-authorization non-regression.

For a new command, require the target stream and necessary parent/authorization streams to be ready. An unrelated task conflict does not block all project work. Material replay additionally validates its topic chain, workflow references, drafts and origin rules. Never use latest filename/time/UUID, directory enumeration order or an edited SQLite row as the current state.

Prefer an available current core for these checks. A direct adapter must implement equivalent validation for the encountered records and proposed operation; read/test additional supported forms when encountered. Do not silently discard unfamiliar records or claim full replay from a permissive subset. Preserve affected data and report the exact unvalidated condition if equivalence cannot be established.

## Prepare one workflow event

All new workflow publications use protocol 2, even though `metadata/store.json.protocol_version` remains 1. The closed envelope is:

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

## Publish immutable bytes

1. Confirm the initialized store identity and schema/cutover markers. Resolve a private local recovery directory outside the shared store and Git. Preserve existing pending records; never repurpose a different actor/store's operation.
2. Persist exact workflow bytes atomically as `<local>/pending/<event_id>.json` **before** any shared mutation. For coordinated/material operations use their specific durable package as well. A receipt records expected revisions and any caller confirmation context without changing the event schema.
3. Immediately before a new workflow publication, refresh required state/rights and acquire the persistent `metadata/access.lock` with Windows read/write, no truncation/sharing, open-reparse-point and opened-handle regular-file validation. Recheck exact registry revision/snapshot and required heads; keep the access lock through publication. It serializes registry changes, not a global head or fork-resolution service. Do not claim a distributed transaction across streams.
4. In `events/<project_id>/`, create a unique `.<event_id>.<attempt_id>.tmp`, write all prepared bytes, flush to disk, close, then rename to `<event_id>.json` without replacement on the same filesystem. Windows: `MoveFileExW` with `MOVEFILE_WRITE_THROUGH`, **without** `MOVEFILE_REPLACE_EXISTING`. Configuration CAS replacement uses a different protocol. Publish material blobs/journal records in their namespaces and required lock order instead.
5. Read the final bytes and confirm exact match, identity, length and hash. Same ID/different bytes is an integrity collision. Same ID/same bytes is confirmation of the previous publication, not a fresh command. Keep pending on unknown outcome; remove the matching workflow pending only after exact publication is confirmed.
6. Release handles, rescan/replay and verify acceptance and requested semantic change. A final may be published but unapplied because a concurrent valid branch appeared. Preserve it and report the conflict; do not delete/rewrite branches or auto-publish a replacement action.

The importable [file_transport.py](../scripts/file_transport.py) implements only Windows persistent locks and immutable byte transport. The caller supplies validated root/relative paths, prepared bytes, pending strategy and all domain/access/replay checks. Acquire locks in the material-specific order when applicable. The module does not initialize a store, mutate access or clean up material versions.

For uncertain rename/network outcomes, check the original final ID first. Exact final bytes confirm publication even if the move call failed. If absent, retain the original bytes and revalidate original heads/access before retry. A stale prerequisite requires a new explicit action; do not regenerate an ID, alter the pending bytes, silently rebase or repeat a whole batch. Clean up only operation-owned temporary files, never arbitrary old files or persistent locks.
