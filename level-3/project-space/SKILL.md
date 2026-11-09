---
name: project-space
description: Manage projects, topics, cross-project task registers, task workflow, employees, access and materials in a Project-space shared store through filesystem and terminal tools. Use when Project-space is the established application context and the task concerns its supported operations.
---

# Project-space

Manage the supported Project-space lifecycle through files: inspect project/topic/global/personal task registers, resolve permanent task numbers, maintain access, update project properties, create and update topics, execute task workflow (including self-task delegation), and manage the topic material library and task links. Use existing filesystem/terminal capabilities; no MCP server or separately installed application CLI is required.

Configuration changes update the mutable registry. Business changes append validated immutable events. Direct file access does not mean editing old JSON, changing SQLite rows or replacing published content in place.

## Establish the working context

- Distinguish the application repository, deployed shared store, local runtime/recovery directory and coordinated project. Reuse an explicitly supplied or already established store; consult trusted deployment records if needed. Ask only when the actual target is ambiguous. An unavailable store is not permission to initialize a replacement.
- Read applicable project instructions and locate the target application's task-relevant owning contracts: `docs/access-control.md`, `docs/storage-protocol.md`, `docs/task-workflow.md` and `docs/domain-model.md`. Prefer a relevant local checkout; otherwise retrieve the required files. A clone, build or reinstall is not a default prerequisite.
- Match the deployed version and activated store metadata to the current implementation before **reads that may activate the store** or writes. `store.json` protocol 1 is the pre-numbering state; protocol 2 references the mandatory authoritative shared task-number registry. Workflow/material event envelopes remain protocol 2, employee/access registry schema 2, workflow validator 4 and local SQLite schema 3; these version numbers are independent. The first upgraded workspace read can activate numbering after a healthy full-store backfill: coordinate client upgrades and preserve a full-store backup before touching a corporate protocol-1 store. Never fabricate a local registry or silently trigger a mixed-client migration.
- Resolve the current Windows process SID locally without elevation/impersonation, then match its registered employee and project rights. Resolve requested people from verified profiles; never choose the actor from a supplied name or another employee's SID.
- Establish the accepted project/topic/task state and material projection, not merely a list of JSON files. Read [Publication and replay](references/publication.md) before workflow/material writes.

## Route by the requested result

| Work | Procedure |
| --- | --- |
| Inspect projects, topics, global «Реестр задач», «Мои задачи», deadlines, history or materials; find `#n` | [Workspace reporting](references/workflow.md#workspace-reporting): one validated access/workflow snapshot and authoritative task numbers; scope to the actual actor and report diagnostics separately. |
| Employees, membership, privileges, supported local settings | [Configuration](references/configuration.md) |
| Project/topic edits, task creation/agreement/execution/review, own active self-task delegation | [Projects and tasks](references/workflow.md), then the shared publication procedure; task creation additionally requires [number reservation](references/publication.md#task-number-authority-and-creation) |
| Import mail/files, add UNC references, replace/delete materials, link/unlink tasks, download | [Materials](references/materials.md), then the shared publication procedure |
| Create a task with initial materials or revise a proposal with material changes | The coordinated operation in the workflow/material references; preserve its sealed plan and partial outcome |
| New project/store, migration, recovery, unsupported archive/delete operation | Check the current owning contract. Carry out an explicitly authorized supported procedure; never manufacture a product operation or bypass a creation gate. |

## Execute the user's operation

An explicit request supplies execution intent; do not add an approval merely because publication uses files. Resolve only material ambiguity: which project/topic/task, person, desired change, source path or intended scope of a shared material change. Continue independent authorized work while clarification is pending.

Use a locally callable current core when available, or implement the required direct-file operation against its authoritative schema/replay rules. The references provide the operation mapping and publication steps. The bundled [file transport](scripts/file_transport.py) supplies Windows locks, UUIDv7 and immutable byte publication; it does **not** validate business commands. It is an importable helper for terminal scripts, not a new application CLI.

Perform semantic validation before network writes. For a direct adapter, read the relevant validator/reducer and validate its required behavior on synthetic data before using a new or changed adapter. Reuse an already verified compatible adapter. Do not make the absence of an MCP/CLI/build itself a blocker; identify the precise missing protocol check or filesystem primitive if one cannot be established.

- Act only as the actual Windows user. Root/management rights do not let the agent accept a proposal as its recipient, submit another executor's result or approve it as another creator.
- Preserve stable project/topic/task/material UUIDs when updating, revising, delegating, reassigning or replacing. A task's permanent display `#n` is resolved from the shared registry, not a replacement for its UUID. Generate new IDs only for new entities, events and attempts.
- Preserve unchanged title/description/deadline values when a request changes only one field. A missing deadline means no deadline only for a new task; it does not silently remove an existing deadline.
- For `task.created`, persist sealed exact workflow bytes to local pending before reserving the next global `#n` under the existing final publication gate; publish/read back the same creation event only after confirmed registry reservation. A direct-file writer without the current protocol-2 number authority must not publish new tasks. Never reuse gaps, silently backfill an active missing registry or derive IDs from local row order.
- Treat batches as ordered, separately verified operations. Keep an operation receipt outside Git with stable IDs, prepared bytes and step results. Retry from confirmed progress, not from the start with fresh IDs. Material/task coordinators have their own stronger rules.
- Observe actual runtime gates. Ordinary production new-project creation currently uses `DenyNewProjects`; Root or a hand-edited `project.create` grant cannot bypass it. Explicit first deployment is a distinct bounded procedure in `docs/deployment.md`.
- Never rewrite/delete published workflow or material events, edit `cache.db` to change business state, or clear pending work as a fix. Material deletion has its own event and constrained blob cleanup. Store identity, migration markers and deployment receipts remain outside ordinary operations.

## Verify and report

After each mutation, confirm exact final bytes and replay acceptance, then verify the requested visible result: current title/status, task version/recipient/result, new creation's authoritative `#n`, material version/links, or access registry delta. Report assigned-but-unpublished task numbers as pending/uncertain, not as completed task creation. Distinguish **prepared**, **published**, **applied**, **partial**, **conflict** and **unknown**; final-file existence alone is not success.

On stale state/access, reload and report the actual conflict without silently rebasing a decision. On uncertain publication, inspect the original ID/bytes before any retry. Never resolve forks by newest timestamp or roll back over another writer.

Report what changed, where the material bytes/reference live, and any remaining blocked step. Do not claim native UI refresh or core replay that did not run; describe an equivalent direct validation accurately. Keep live corporate paths, employee/SID mappings, material contents and private operation receipts outside shared skill sources and Git.
