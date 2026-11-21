# OpenAI collaboration interface

## Scope and evidence

Apply only when the current host exposes the `collaboration` tools described below. This profile records the tool contracts exposed in the ChatGPT execution environment used for [Issue #18](https://github.com/Krankort224/Skills/issues/18), checked 2026-11-22. It does not certify all ChatGPT modes, Codex CLI/cloud versions, or public OpenAI APIs.

The live tool descriptions are the primary interface source. Actual assignments in that task exercised spawning, isolated task context, messages and result collection; this is not exhaustive testing of cancellation, deep recursion or every model setting. Recheck availability in the present session and follow tighter platform/task rules. Keep volatile model availability and slot counts out of this profile.

## Map operations to tools

| Need | Exposed operation and boundary |
| --- | --- |
| Start a child | `spawn_agent` accepts a task name and message; returns a canonical task name. Inspect the current signature and allowed models. |
| Select context/model | `fork_turns="none"` starts without surrounding history. With a full-history fork the parent model/effort are inherited and overrides are not accepted in this interface. Use overrides only when applicable instructions authorize them. |
| Send additional context | `send_message` queues a message but does not start a new turn for an idle agent. |
| Continue an existing task | `followup_task` can trigger an idle agent's next turn; it does not promise a new model or independent context. |
| Observe/wait | `list_agents` reports the current tree; `wait_agent` waits for a mailbox update. Its return is a notification summary, not the child's substantive result. Read the delivered message/result. |
| Interrupt | `interrupt_agent` interrupts the current turn and returns the previous status; the agent remains available. Do not equate that with permanent deletion or proof that every background process stopped. |

## Apply assignment limits

Available models, reasoning settings, active slots and descendant restrictions come from current tool/platform instructions and the approved plan. A tool's existence does not grant a worker spawning rights. For the matching model pool, read [OpenAI selection](../models/openai.md); do not copy its identifiers here.

Participants in this observed environment share the filesystem and working directory. Separate conversations therefore require disjoint write scopes or serialized edits; no automatic file isolation is implied. Pass verified source paths/pins and required skills directly, especially with no history fork.

Use completion messages and appropriately sized waits while doing independent work. When a child is replaced or interrupted, inspect its reported state and relevant filesystem/background effects before transferring a write scope. Preserve partial results and the task package. If a needed control is absent in another host, use the generic operations and disclose the gap instead of inventing a corresponding tool.
