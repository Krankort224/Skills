# Configuration edits

Use the current Project-space owning contracts and implementation to validate the deployed version. The map below describes the schema-2 registry baseline, not permission to migrate or invent fields for another version.

## Identify the file authority

| Location | Role and edit boundary |
| --- | --- |
| `metadata/store.json` | Store identity/protocol. Read and match it; do not rotate the ID or recreate it during a configuration edit. |
| `metadata/access.json` | Mutable employee/access authority; the target for an explicitly requested supported registry change. |
| `metadata/access.lock` | Persistent OS-handle-owned lock for registry changes and command publication. Keep the file; acquire its Windows exclusion semantics. |
| `metadata/access-migrated.json` | Fail-closed cutover marker, bound to the store. Preserve it; it is not a toggle for restoring old permissions. |
| `.project-space-deployment*`, `metadata/deployment-*.json` | First-deployment plans, locks and receipts. Historical recovery inputs, not current user settings. |
| `events/`, `material-events/`, `material-blobs/`, legacy `artifacts/` | Published workflow/material history and managed contents. Inspect only as needed; no routine configuration writes. |
| Local `cache.db`, `pending/`, `material-pending/`, `task-creation/` | Disposable projections or unpublished operation recovery state, not authority for editing business state. Do not clear them as an access/configuration fix. |

## Employee/access registry

Resolve the current Windows process SID/account locally without elevation or impersonation. Confirm the intended operator scope. Filesystem write permission alone does not authorize unrelated access changes.

For schema 2, validate the complete candidate against the current owning schema, including:

- Exact top-level fields: `schema_version`, `store_id`, `employees`, `roots`, `system_grants`, `projects`; correct version/store identity and no duplicate JSON keys or unknown fields.
- `employees`: a map keyed by canonical Windows SID. Each value has exactly `employee_id`, `full_name`, `windows_account`. IDs and accounts are unique without regard to case; names and IDs are nonempty, trimmed and contain no control characters. Use the current account syntax validator; require an explicit domain-qualified account rather than a guessed account name.
- Verify supplied/changed Windows accounts through Windows account-to-SID resolution and compare with their keys; reverse resolution must agree with the intended account. Do not derive a SID from a short ID/name, reuse an unverified SID or silently rebind a profile. Read only the approved columns when a staff source contains additional personal data.
- Every SID in `roots`, `system_grants` and project membership refers to a registered employee. A project map contains SID-to-`{privileges}` membership records, not duplicate profile names/accounts. Project IDs must satisfy the current ID validator and refer to the intended existing project.
- Current allowed system privilege: `project.create`; project privileges: `project.manage`, `topic.manage`. Preserve inheritance instead of writing an extra explicit privilege merely because it is inherited. Root and project creation are independent.

Changing employee profiles is operator maintenance. An ordinary project manager selects an existing employee; that action does not create or rename a global profile. A normal participation request adds membership with no privileges unless a privilege was also requested. Resolve ambiguous display names before selecting a SID.

For ordinary project administration, preserve the current actor's management requirements and the restrictions on managing another Root, removing one's own management and granting/revoking `project.manage`. Do not use direct files to silently evade them. Root assignments or system-grant maintenance require a specific operator request and the applicable canonical procedure; they are not incidental effects of membership/profile edits.

### Registry transaction

Use available Windows filesystem/identity APIs from the shell. This protocol does not require a new application executable. Do not substitute a non-atomic editor overwrite when the necessary primitives are unavailable.

1. Read the existing raw bytes and SHA-256 revision, matching store identity/marker, and identify the requested semantic delta. Preserve any needed original bytes privately outside Git and the shared namespaces. Prepare the candidate without modifying unrelated records.
2. Acquire `metadata/access.lock` with the same Windows behavior as `AccessStore::lock`: an open read/write handle, create-if-missing without truncation, no sharing, and rejection of reparse points. With native Windows APIs, use `CreateFileW` with `OPEN_ALWAYS`, share mode zero and `FILE_FLAG_OPEN_REPARSE_POINT`; validate the opened handle is a regular file without reparse attributes. A path check before opening is insufficient. Keep the handle open through validation, replacement and readback. Use a bounded wait for a busy lock; never delete the lock file or treat its existence as proof it is held.
3. Under the lock, recheck store identity/marker and reread the complete registry. Compare SHA-256 of the exact current bytes with the expected revision; whitespace-only changes count. On mismatch stop this write and report the stale revision; do not overwrite or silently rebase it. Reject invalid existing state rather than manufacture a replacement registry from history.
4. Validate the candidate's closed schema, identity mappings, references and requested rights. Recheck the expected source revision immediately before replacement. Preserve the target's access restrictions; do not broaden filesystem ACLs to complete the edit.
5. Write UTF-8 without BOM to a uniquely created temporary file in the same `metadata` directory. Flush the file to the filesystem and close the temporary handle. Use the accepted atomic replacement primitive: Windows `MoveFileExW` with `MOVEFILE_REPLACE_EXISTING | MOVEFILE_WRITE_THROUGH`, as in `AccessStore::replace`/`atomic_replace`. No cross-volume move, delete-then-move, copy fallback or direct truncation of the live registry.
6. Read back the final raw bytes under the lock, confirm the expected candidate, rerun schema/store checks, and inspect the semantic delta. For an ambiguous rename result, an exact final-byte match establishes the committed outcome; a different/unknown final does not authorize a blind retry or rollback. Remove only temporary files created by this operation whose ownership is known. Leave unknown residual files for a separately scoped recovery.
7. Release the lock handle. Report the updated profiles/memberships/rights and observed verification. Do not edit events or deployment records to make them match today's rights. Published historical authorization snapshots keep their original meaning.

If schema/account validation, exclusion, compare-and-swap or atomic replacement cannot be established, preserve the original and report that specific missing condition. Do not make MCP/CLI installation, a full build, CI or application reinstallation the default prerequisite for this file operation.

## Local settings

Resolve the local directory through the current runtime contract; the baseline is the system Local App Data directory plus `Project-space`. Read the current schema in `app/src-tauri/src/local.rs` before proposing a field edit.

The current closed `config.json` schema is only `{"version":2}`. It contains no user-selectable shared-store path. The production deployment root is a compile-time application input, not a setting to add here. Do not resurrect legacy `sharedStoreRoot`, fabricate a project selector, or increment `version` to obtain a requested behavior.

If a deployed version supports an actually editable field, preserve its schema, unrelated settings and existing access restrictions; coordinate with the runtime's write behavior and replace atomically. Preserve corrupt/unknown-version files for a separately requested diagnosis or migration. Never reset local pending operations or SQLite to conceal an unsupported configuration change.
