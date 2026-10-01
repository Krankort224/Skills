# Repository Context Map

**Repository:** `<owner/repository>`

**Purpose:** `<brief description>`

## Scopes

List only scopes whose context differs materially.

| Scope | Selector | Entry point |
|---|---|---|
| `<scope>` | `<branch / path / component / project / platform>` | `<path>` |

Remove this section if the repository has no meaningful context partitions.

## Knowledge and contract ownership

Point to canonical owners, without restating their contracts.

| Source | Owns | Must not own |
|---|---|---|
| `<canonical source / owner reference>` | `<facts / durable contracts; update destination when distinct or unclear>` | `<excluded responsibilities / knowledge>` |

Record non-obvious ownership boundaries here. Distinguish canonical knowledge from navigation, evidence, history, examples, generated output, and runtime copies according to their actual roles.

Mark immutable inputs and other write boundaries where relevant. Ownership does not grant write permission; do not invent missing update destinations.

## Source authority

Define authority directly by subject.

| Subject | Source precedence | Notes |
|---|---|---|
| `<architecture>` | `<source A> → <source B> → <source C>` | `<when verification is required>` |
| `<actual behavior>` | `<runtime/tests> → <implementation> → <documentation>` | `<if applicable>` |
| `<input values>` | `<primary source> → <derived data>` | `<conflict rule>` |
| `<current state>` | `<current-state source> → <history>` | `<validity boundary>` |

Add only subjects with genuinely different authority.

Do not create one global precedence order when different facts have different owners.

## Routes

Describe recurring reading paths that avoid rediscovering repository structure.

### `<task type>`

1. `<entry point>`
2. `<canonical source>`
3. when needed:
   - implementation: `<path>`;
   - evidence: `<path>`;
   - decisions: `<path>`;
   - primary data: `<path>`;
   - history: `<path>` — only when `<condition>`.

### `<task type>`

1. `<path>`
2. `<path>`

Verify against `<fact-owning source>`.

Add only stable, recurring routes.

## Special sources

Use only for data that requires a non-trivial access pattern.

| Source | Access rule |
|---|---|
| `<large snapshot / binary / cloud source / live system>` | `<how to read it and what not to do>` |

Remove this section if there are no special sources.

## Sufficient context

For this repository, reading can usually stop when:

- the correct scope is selected;
- its canonical source has been read;
- task-relevant documents are loaded;
- the fact-owning source has been checked when required;
- task-relevant owners and required update destinations are identified, or material gaps are reported;
- material conflicts have been identified.

Additional conditions:

- `<only if genuinely needed>`.
