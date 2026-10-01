---
name: context
description: Load the minimum authoritative repository context required for the current task.
metadata:
  short-description: Load repository context
---

# Context

Load the minimum context required to understand the current task correctly.

For a repository-local installation, use `references/repository.md` as the context map. It defines repository scopes, source authority, and reading routes.

If `repository.md` is absent, do not treat `repository.template.md` as project context.

## Principles

### Start from the task

Determine which repository scope the current task belongs to and load only context relevant to it.

Do not expand the reading scope without a task-specific reason.

### Follow the local map

Do not assume universal precedence for code, documentation, Issues, history, generated results, or newer files.

Use the authority rules defined in `repository.md`.

### Load progressively

Typical order:

1. local context map;
2. primary source for the relevant scope;
3. task-relevant canonical sources;
4. code, primary data, tests, or runtime evidence when needed to verify a fact;
5. history and archive only when needed for provenance, regression analysis, or conflict resolution.

Stop when further reading is unlikely to materially change the understanding of the current task.

### Respect scope boundaries

If the repository is divided by branches, components, platforms, projects, experiments, or other scopes, resolve the applicable scope first.

Do not transfer state or decisions across scopes unless an explicit relationship exists.

### Verify facts at their owner

When a claim belongs to a specific source, verify it there when necessary.

For example, actual behavior may belong to implementation or runtime evidence, a numerical value to a primary source, and a decision to a canonical document.

Maps and indexes are navigation aids; they do not automatically replace the source that owns the fact.

### Resolve conflicts by authority

When sources disagree:

1. identify their roles;
2. apply the local authority rule;
3. distinguish stale information from a genuinely unresolved conflict;
4. load additional evidence only when needed.

If the local map cannot resolve a material conflict, preserve the uncertainty. Do not choose a source arbitrarily.

### Keep history separate from current state

Use history for decision provenance, rejected alternatives, investigations, and regressions.

History does not define current state unless the local map explicitly says otherwise.

### Treat derived data carefully

Logs, reports, snapshots, builds, previews, exports, and other derived artifacts may be evidence, inputs, or outputs.

Their role is defined by the local map.

### Reuse loaded context

Do not reread an unchanged source within the same task.

For large sources, prefer targeted reading after identifying the relevant area.

## Context sufficiency

Context is sufficient when the following are known:

- the applicable repository scope;
- authoritative sources for the current question;
- task-relevant current state and constraints;
- required supporting evidence;
- material unresolved conflicts, if any.

Do not load additional context merely to become generally familiar with the repository.

## Boundary

`context` only reads and interprets context.

It does not modify files, Git or GitHub state, project knowledge, or task state.
