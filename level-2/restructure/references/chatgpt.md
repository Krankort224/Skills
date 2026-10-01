# ChatGPT Contour

Own semantic analysis, target-structure design, migration planning, ambiguity resolution, and final review.

Do not assume direct access to the local filesystem. Base structural decisions on inventory and evidence collected by the execution environment.

## 1. Start from inventory

Do not design the target structure from filenames remembered from conversation or from a partial repository impression.

Use the current inventory produced by Codex.

The inventory should be sufficient to understand:

- existing directory structure;
- file groups and formats;
- obvious project/component boundaries;
- current, historical, source, derived, reference, temporary, and unresolved material where distinguishable;
- Git/LFS state when relevant;
- large or binary files;
- external or cloud-hosted objects;
- obvious duplicates or competing versions;
- material whose role cannot yet be determined.

If the inventory is insufficient, request a targeted follow-up inspection rather than guessing.

## 2. Identify real storage roles

Classify by lifecycle and ownership, not by convenient folder names.

Useful distinctions may include:

- independent projects or components;
- source material versus authored work;
- editable versus immutable material;
- current state versus history;
- canonical versus reference-only material;
- working files versus deliverables;
- source inputs versus generated outputs;
- durable knowledge versus temporary evidence.

Do not create a separate category unless it has a practical storage or lifecycle difference.

If two groups follow the same rules, keeping them together is usually better than creating extra structure.

## 3. Identify actual problems

Describe only problems the restructuring must solve.

Typical examples:

- current state is ambiguous;
- several competing copies look authoritative;
- source and generated output are mixed;
- historical files look current;
- unrelated projects are mixed;
- provenance is unclear;
- temporary artifacts pollute durable storage;
- names do not identify role;
- repository state and local file accumulation diverge;
- important external material is referenced inconsistently.

Do not treat harmless stylistic inconsistency as a structural defect.

## 4. Define target requirements

Before naming folders, state what the new structure must make true.

Requirements may include:

- one obvious place for each durable role;
- clear distinction between source and result;
- identifiable current state;
- preserved provenance;
- minimal duplication;
- Git suitability;
- predictable naming;
- automation-friendly paths;
- explicit history boundaries;
- visible unresolved material.

Requirements describe properties, not folder names.

## 5. Design the minimal target structure

Create only the levels and categories justified by the inventory and requirements.

For each proposed area, make clear:

- what belongs there;
- what does not;
- what role the area plays;
- whether it is source, working, canonical, derived, historical, reference, or another real category;
- how current state is identified if multiple versions may exist.

Do not create empty future-facing architecture without a concrete need.

## 6. Normalize naming deliberately

Use naming rules only where they materially improve identification, navigation, automation, or stability.

A useful name should help identify:

- the entity;
- its role;
- its relation to neighboring objects;
- whether it is current, historical, source, or output when that distinction matters.

Preserve external identifiers and filenames when renaming could break links, integrations, provenance, or downstream tooling.

Do not mass-rename solely for visual consistency.

## 7. Produce the migration map

Before physical migration, define:

`old location → new location`

For each non-trivial item or group, the action should be explicit:

- move;
- rename;
- merge;
- archive;
- leave in place;
- reference only;
- exclude from repository;
- unresolved;
- defer.

Do not silently resolve uncertain cases.

If a content change is needed in addition to relocation, distinguish it from the mechanical migration.

## 8. Respect the cloud-file boundary

Cloud objects may appear in inventory as references or metadata-only entries.

Do not ask Codex to download, materialize, synchronize, export, or copy their contents locally unless the user has separately and explicitly authorized that specific action.

A restructuring instruction alone is not authorization.

If local content is necessary for a decision, surface the dependency to the user instead of treating download as implicit.

## 9. Review the migration

After Codex completes migration, review the result against the approved target structure and migration map.

Check:

- expected material is present;
- nothing important was lost;
- no unintended duplicate source of truth was created;
- provenance remains understandable;
- current versus historical state is clear where required;
- unresolved items remain explicit;
- naming and boundaries match the accepted design;
- Codex did not invent structural decisions during migration;
- cloud-file restrictions were respected.

If the result differs from the approved design, distinguish:

- harmless implementation detail;
- necessary discovered exception;
- material structural deviation.

Only the last two require an explicit decision before acceptance.

## 10. Keep unresolved cases visible

Do not force closure where evidence is insufficient.

Preserve a concise list of:

- unclassified items;
- disputed duplicates;
- unknown current versions;
- broken provenance;
- external dependencies;
- deferred structural decisions.

A complete restructuring may still contain explicitly unresolved material.
