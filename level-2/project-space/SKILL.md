---
name: project-space
description: Use when explicitly asked to use project-space to inspect a Project-space store or directly maintain its employee registry, project membership, privileges or supported local configuration through files.
---

# Project-space

Inspect and maintain Project-space configuration directly through available filesystem and terminal tools. This version requires no MCP server, application CLI, application rebuild or developer toolchain. It does not implement task/workflow or material publication.

## Resolve context

- Distinguish the Project-space application repository, the deployed shared store, the user's local runtime directory and the project coordinated inside the application.
- Resolve the intended store from explicit input, established task context or a trusted local deployment record. Reuse an already established location; ask only if the actual target remains ambiguous. Never select a store from a plausible folder name or initialize an empty/missing store as a side effect.
- Read applicable project instructions and the owning Project-space contracts. Prefer the relevant local checkout; otherwise retrieve the required files from [Krankort224/Project-space](https://github.com/Krankort224/Project-space). A local clone is not a prerequisite.
- For shared identities and rights, read `docs/access-control.md`; for store identity, immutable namespaces and publication rules, read the relevant sections of `docs/storage-protocol.md`. For local settings, read `docs/architecture.md` and the current `app/src-tauri/src/local.rs` schema. Consult `app/src-tauri/src/core/access.rs` and `app/src-tauri/src/identity.rs` when validating a registry change. Do not copy these evolving contracts into project instructions.
- Verify `metadata/store.json`, the access marker and registry belong to the same supported store. Treat unknown schemas, a missing established registry or conflicting identities as a reason to stop the affected edit while preserving the files.

## Select the operation

| Request | Direct-file behavior |
| --- | --- |
| Explain structure, inspect configuration or diagnose access | Read only the relevant metadata and report observed facts. |
| Maintain employee profiles, membership or explicit privileges | Apply the requested registry change using [Configuration edits](references/configuration.md). |
| Change a supported local setting | Verify that the current schema actually supports the field, then follow the local-setting guidance in the same reference. |
| Explain materials or inspect their metadata | Distinguish uploaded bytes from external UNC references. Read only the records needed; do not register, replace, move or delete material contents. |
| Create/modify a project, topic, task, decision or material | Explain that this is an application operation, outside this configuration-only version. Do not simulate it by rewriting history or introduce a CLI/MCP as an unrequested dependency. |

Raw events provide historical facts. Do not infer current task state, accepted branches or current permissions by sorting UUIDs/timestamps or choosing the newest JSON file. Current workflow summaries require the application's validated replay/projection; distinguish that from a raw-file inspection.

## Change only the requested configuration

- An explicit ordinary edit request supplies execution intent; do not require a second approval solely because files are involved. Clarify only missing identity, target, desired rights or another material ambiguity. The skill itself grants no additional operational authority.
- Resolve people through the existing registry and Windows account/SID lookup. Do not invent employee IDs, full names, accounts or SIDs. Short IDs and display names are labels, not authorization identities.
- Preserve unrelated employees, memberships, Root assignments and explicit grants. Adding a participant does not implicitly grant management rights. Distinguish ordinary project administration from explicitly requested operator-level registry maintenance; preserve the application boundaries described in the owning access contract.
- Perform access edits under the existing `metadata/access.lock`, with raw-byte revision checking and an atomic replacement. A normal editor save or direct overwrite is not the registry update protocol. Read the reference before any write.
- Leave store identity, access migration markers, deployment plans/receipts, published events, material journals/blobs, local pending packages and SQLite projections unchanged. They are not editable configuration for routine maintenance. Deployment, migration, recovery or cleanup needs its own explicit task and applicable procedure.
- Do not enable `project.create` to make an unrelated operation work. The ordinary client remains governed by its runtime authorization source even if a registry grant exists.

## Verify and report

After a configuration write, reread the committed bytes, validate their schema/store identity and compare the semantic delta with the requested change. Confirm unrelated records and the intended access restrictions were preserved. If the write outcome is uncertain, inspect the final state before retrying; never blindly repeat or roll back over a newer revision.

Report the affected configuration, actual change and verification result. Separate a verified file update from an observed application refresh. Do not claim task/material execution, native UI checks or replay validation that did not occur.

Keep corporate paths, live rosters, SID/account mappings and any private working copies outside skill sources and Git. Report names/short IDs when useful to the user; avoid dumping full registries or raw identifiers into shared reports.
