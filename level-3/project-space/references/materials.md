# Materials

Use the topic library and task links, never the legacy intermediate/final artifact containers. Read current `docs/domain-model.md`, the material-rights section of `docs/access-control.md`, `docs/storage-protocol.md` section 11 and the relevant functions in `app/src-tauri/src/core/materials.rs`. Use [Publication and replay](publication.md) for shared invariants.

## Select the operation and scope

| Intent | Effect |
| --- | --- |
| Add directly to topic | Register/reuse library material; no implicit task link |
| Add through task | Register/reuse in its topic and link to that task |
| Link/unlink an existing material | Change one relationship; preserve material and other task links |
| Replace | Keep ID, category, storage kind, origin and all links; publish a new imported version or new UNC target |
| Delete material | Tombstone the material and remove every task link; clean only its managed blobs |
| Download/open | Download a verified imported copy outside the store, or open an authorized external UNC reference |

Categories: `mail` = imported `.msg`/`.eml`; `assignment` = UNC directory; `file` = imported other file or UNC file excluding `.msg`/`.eml`. The journal uses these singular values, not legacy `assignments`/`other`. A local source path is valid for an **import**; production **references** accept only absolute UNC paths. Never publish preview-only `local_file`/`local_directory` storage.

Read/download/open requires current project participation or Root. Topic registration and ordinary replacement require `topic.manage` or higher; ordinary deletion requires `project.manage` or Root. Through a task, registration/link/unlink require its executor or `topic.manage`/higher; creator alone has no general continuing material authority.

Narrow task replacement/deletion requires current participation and assigned executor, a nonterminal task, material originally registered from this task and still linked to it. Verify current material revision and task head. Task-context delete requires this origin even for managers; other-origin material uses unlink, or a separately requested authorized library deletion. Root material rights do not grant another person's task workflow rights.

Before replacing/deleting a material shared with other tasks, identify those tasks and obtain explicit confirmation of the shared effect, including their count and names. An existing explicit request that names this shared effect supplies confirmation; do not ask twice. Bind the confirmation to reviewed revisions and affected links. A changed revision/link set requires renewed confirmation before that write.

## Validate inputs and deduplicate

Use explicitly supplied sources or established task context. Do not fabricate application native-selection tokens or claim a dialog occurred. A trusted terminal operation may keep its own private durable plan for user-authorized paths.

- Imports: absolute readable regular source outside managed store; stage exact bytes locally, size and lowercase SHA-256. Validate the basename with the current Windows-name validator, including UTF-16 length, reserved names and forbidden characters. Preserve source case; never use the display name as a managed path component.
- Imported deduplication: same topic/category, case-insensitive name after stripping the leading `YYYYMMDD_HHMMSS_` stamp, then identical SHA-256. Verify the current stored bytes before reusing. An identical staged import may restore a missing current final through the accepted recovery rule; it never overwrites differing bytes or resurrects a tombstoned material.
- UNC deduplication: same topic, normalized absolute UNC path **and** reference kind. Mirror `normalize_unc`; reject drives, URLs, device/extended namespaces, slash/traversal and malformed Windows components. Do not hash/copy external targets. Availability is checked when opening, not a requirement for registration.
- Reuse a duplicate's ID/origin; task addition becomes a link, and an already-linked duplicate needs no event. New task registration can carry its initial task link in one `register`.
- For distinct bytes with a conflicting display name, use `name_for` and a UTC stamp; revalidate the resulting name rather than truncate it. Replacement name checks exclude that same material.

## Journal schema and ordinary publication

Paths:

```text
material-events/<project_id>/<topic_id>/<event_id>.json
material-events/<project_id>/<topic_id>/.topic.lock
material-blobs/<project_id>/<topic_id>/<material_id>/<version_id>/content
```

The closed envelope contains **all** fields below; nullable fields are explicit `null`:

```text
protocol_version: 2
store_id, project_id, topic_id, event_id, actor_sid, recorded_at
base_event_id: previous accepted topic-library event, or null for first
topic_creation_event_id: accepted workflow topic root
task_context_event_id: exact accepted task head, or null for library action
authorization: current v2 authorization snapshot
operation: tagged closed object
```

Ordinary `operation` forms use `type` tags:

```text
register: material_id, category, display_name, storage, task_id:null|UUID
replace: material_id, display_name, storage
link: material_id, task_id, linked:boolean
delete: material_id, creation_event_id, creation_sha256
task_replace: material_id, task_id, expected_material_event_id, display_name, storage
task_delete: material_id, task_id, expected_material_event_id, creation_event_id, creation_sha256
```

Storage forms: `{kind:"imported_file",version_id,size_bytes,sha256}`, `{kind:"unc_file",path}`, `{kind:"unc_directory",path}`. The original registration sets immutable origin. Every material action, including link/unlink, advances its `updated_event_id`; use that revision, not merely the most recent replacement event.

1. Prepare/stage inputs privately; verify current read authority and accepted project/topic scope before creating even a lock file. Acquire the topic's persistent OS file lock **before** `metadata/access.lock`. Topic lock uses Windows `LockFileEx`-compatible whole-file exclusion; access lock uses no-sharing `CreateFileW`. Never unlink either lock. For a coordinated operation, acquire its local operation lock before these locks.
2. Under locks, recheck store identity, schema, current access, accepted workflow context and complete material journal. Validate the candidate using `make_event`, `authorize_historical`, `apply` and current task-origin/revision rules. Require a unique accepted library chain; do not choose a competing child by time.
3. Persist exact prepared event bytes and any staged blob in a private `material-pending` package before shared publication. Match `publish_exact` recovery semantics. Keep stable IDs, original byte hashes and expected contexts; do not clear or reinterpret another pending package.
4. Publish an imported version's verified `content` first, then its journal event, through create-new temp → flush/close → no-replace rename. Never overwrite an existing content/version. For UNC registration publish only metadata.
5. Read back exact finals, confirm byte identity, then replay the library and verify the resulting material/version/links. Clear matching pending only after confirmed publication; perform deletion cleanup as below. Release locks in reverse order.

Material replay validates each candidate against its historical workflow context and parent library state. Follow unique accepted children from null, retain the confirmed prefix on a fork, and reject missing/cyclic/invalid ancestry. A valid deletion tombstone has additional irreversible treatment; do not implement it as ordinary last-write-wins or chain truncation alone.

## Deletion, retry and download

Deletion binds `creation_event_id` and SHA-256 of the **exact original registration bytes**, whose event is in the causal ancestry. A valid tombstone remains effective when a conflicting sibling replacement is later discovered. Deleted IDs cannot be registered again. Preserve the entire event history.

After confirming the tombstone, clean **all managed versions of that material only**, under topic lock, with checked paths/reparse restrictions and live-reference checks from `cleanup`. Historical replay must not require removed blobs. Repeat unfinished cleanup during recovery; never delete external UNC data or run general orphan/temp garbage collection.

For pending recovery, exact matching final bytes mean confirmation, not republishing a blob that was subsequently deleted. If final is absent, require unchanged saved library head, access revision, task context and valid current authorization before publishing original bytes. Otherwise retain pending and report stale/partial state. Retry never silently rebases an event or recreates removed links/materials.

Download only the current imported version, after current read authorization and size/hash checks. Destination must be an absolute user-approved path outside the store, created exclusively without replacement and flushed; remove only this operation's partial output on failure. Open downloaded copies, never managed `content` directly in Office. For opening UNC, verify current authority, actual target kind and reparse/ancestor restrictions; then open the external target. Registration itself grants no external filesystem rights.

## Coordinated task drafts

For creation/refinement with materials, read `initial_task_creation.rs` (`save`, plan execution/retry) and `core/materials.rs` (`StagedDraftMaterial`, staging, draft application). These are compound operations, not ordinary creator file uploads.

Before publishing the workflow anchor, seal a private durable plan bound to a stable operation key, actual SID, store/project/task and exact request fingerprint. Validate/spool every source and expected material revision; allocate IDs and save exact prepared workflow bytes. Serialize retries under the local operation OS lock; atomically persist Preparing/Prepared progress. A prevalidation failure or cancellation before anchor publication produces no business events.

When using the current application coordinator, select its generic version-2 path with `TaskCreationRequest.selections` (for an upload: `{type:"import",path,category:"file"}`; `.msg`/`.eml` uses `mail`), leaving `sources` absent/empty. A nonempty upload-only `sources` list with empty `selections` deliberately selects its older version-1 plan and `initial_register`/`initial_link` path. Do not confuse that still-supported compatibility path with the generic draft plan described here. Existing application native-selection checks still apply when calling its coordinator; terminal-owned plans do not fabricate those grants.

The generic material operation is:

```text
{type:"draft", task_id, context_event_id, context_sha256, intent_sha256, action}
```

`context_event_id` is the exact accepted v2 `task.created` or `task.proposal_revised`, same actor/project/task; hash its raw bytes. Envelope `task_context_event_id` equals it. Draft actions use `type` tags:

```text
register: material_id, category, display_name, storage
link: material_id, expected_material_event_id
replace: material_id, expected_material_event_id, display_name, storage
unlink: material_id, expected_material_event_id
delete: material_id, expected_material_event_id, creation_event_id, creation_sha256
```

Mirror `StagedDraftMaterial::fingerprint` exactly: SHA-256 of compact UTF-8 `serde_json::Value` serialization with sorted object keys. Imported intent hashes `{type:"imported",name,category,size_bytes,sha256}`; replace-imported adds `material_id` and `expected_material_event_id`. Read the current tagged staged forms for other intentions rather than hashing arbitrary input JSON. Different selection/source/revisions with the same key is not a retry.

For validated string/integer/boolean intent values in Python, serialize with `json.dumps(intent, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False).encode("utf-8")` before hashing. Do not include local spool paths or transport-only fields in this intent hash.

Initial creation permits register/link only; `initial_artifacts` in the anchor stays empty. Refinement requires the current proposed task recipient and an actual title/description/deadline change; materials-only refinement is unsupported. It permits register/link, own-origin replace/delete and other-origin unlink, preserving existing managerial allowances. Context deletion always requires task origin. A duplicate registration becomes a link without changing origin.

On first material publication, require the current healthy task head still equal the anchor. Preserve the original staged bytes and contexts on retry. An already accepted draft receipt may be confirmed after task progress/deletion; it must not restore removed material, relink after a later unlink, or repeat unlink after a later relink. These bounded form rights do not survive as general creator permissions.

There is no multi-file transaction across anchor and all materials. Report anchor publication/application and each remaining material/link step. Retain partial progress and resume the original operation; do not delete the task, change its event, reread altered source files or restart with new IDs. Historical upload-only `initial_register`/`initial_link` have their own closed compatibility forms; read them for replay/recovery, but use the generic staged draft for new coordinated operations.
