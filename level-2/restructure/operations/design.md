# Design and migration planning

Input: sufficient current inventory and project constraints. Output: justified target structure, naming rules, migration map and explicit unresolved decisions. Apply root principles; this operation does not physically migrate files.

## Identify roles and problems

Classify by real storage/lifecycle differences: independent projects/components; sources versus authored work; editable versus immutable; current versus history; canonical versus reference; working versus deliverable; input versus generated output; durable knowledge versus temporary evidence. Keep groups together when their rules match.

State actual defects: competing authority, mixed current/history or source/output, unclear provenance, unrelated projects, temporary pollution, misleading names, local/repository divergence or inconsistent external references. Harmless stylistic inconsistency alone is not a defect.

## Establish requirements and target

Define properties before folder names: identifiable current state, clear ownership, preserved provenance, minimal duplication, appropriate Git storage, stable/automation-friendly names, history boundaries and visible unresolved material.

Create only justified levels/categories. For each area define membership, exclusions, role and how current state is identified among versions. No category exists merely for symmetry or possible future use.

Normalize names only to improve identification, relationships, navigation, automation or stability. Preserve external names/identifiers where changes could break links, integrations, provenance or tooling; no cosmetic mass rename.

## Map the migration

For each nontrivial item/group specify `old location → new location` and action: `move`, `rename`, `merge`, `archive`, `leave`, `reference_only`, `exclude_from_repository`, `unresolved`, or `defer`. Define merge handling and repository exclusions sufficiently to avoid accidental content loss; exclusion does not imply deletion of the local source.

Separate additional content changes from relocation. Identify reference updates, storage-policy changes, validation and required records. Cloud objects may remain metadata/reference entries; report dependencies requiring separately authorized local access.

Resolve material decisions and execution authority before migration. Reuse already agreed decisions rather than seeking approval again. Keep unclassified items, disputed duplicates, unknown current versions, broken provenance, external dependencies and deferred choices visible.
