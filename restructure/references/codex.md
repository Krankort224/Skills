# Codex Contour

Own physical discovery, initial inventory, targeted follow-up inspection, mechanical migration, and before/after validation.

Do not redesign repository structure while executing.

## 1. Initial inventory comes first

Before any restructuring action, inspect the actual filesystem state.

The initial inventory should capture enough information for semantic analysis without changing the accumulation.

Collect, where relevant:

- directory tree;
- file paths and names;
- file types/extensions;
- file sizes;
- timestamps and other useful metadata;
- Git tracking state;
- Git LFS state;
- ignored or untracked files when relevant;
- obvious temporary or generated artifacts;
- large or binary files;
- obvious groups by project/component/path;
- likely duplicate or competing files;
- external references and cloud placeholders;
- broken or suspicious paths.

Use hashes only when they materially help answer a concrete duplicate or identity question. Do not hash every file by default.

Do not move, rename, delete, normalize, or reorganize anything during initial inventory.

## 2. Read local content only as needed

Start from paths, names, metadata, and surrounding structure.

Inspect local file contents only when classification cannot be made reliably without doing so.

Prefer targeted inspection over exhaustive reading.

Do not transform file contents merely to make them easier to classify.

## 3. Cloud-file boundary

Do not download, materialize, synchronize, export, or copy cloud-hosted file contents into the local environment unless the user has given a separate, explicit, and unambiguous authorization for that action.

Repository restructuring, inventory work, or a request to inspect the accumulation does not count as authorization.

Without authorization, limit cloud inspection to metadata and listings exposed without downloading content, such as:

- name;
- path;
- identifier;
- size;
- timestamp;
- relationship to folders or other objects;
- available remote metadata.

If classification requires local access to the cloud file contents, report that limitation and stop at the metadata boundary.

Do not work around this restriction by using another tool or temporary directory.

## 4. Report inventory for semantic analysis

Summarize the physical state without pretending uncertain roles are known.

Separate:

- observed facts;
- obvious mechanical classifications;
- suspected relationships;
- unresolved items.

Call out cases that need semantic interpretation, such as:

- multiple plausible current versions;
- unclear project ownership;
- unknown origin;
- ambiguous duplicates;
- files whose names contradict their location;
- cloud objects that cannot be inspected without authorization.

The inventory should make it possible to design structure without re-scanning the whole filesystem.

## 5. Targeted follow-up inspection

When ChatGPT asks for additional evidence, inspect only the requested area or question.

Examples:

- compare two candidate files;
- inspect a local text manifest;
- verify whether a folder contains generated output;
- determine whether two local binaries are identical;
- check whether paths are referenced elsewhere;
- inspect Git history for a specific rename or origin question.

Do not expand a targeted inspection into an unrequested migration.

## 6. Execute only the approved migration

After the target structure and migration map are accepted, perform the mechanical restructuring.

Typical actions may include:

- create directories;
- move files;
- rename files;
- use Git-aware moves;
- update relative references where required;
- configure or adjust `.gitignore`;
- configure Git LFS when explicitly part of the accepted plan;
- create inventory or migration records required by the plan.

Do not:

- invent new categories;
- place unclassified files into a generic miscellaneous folder unless the plan says so;
- rewrite project content for convenience;
- delete uncertain material;
- broaden the migration scope;
- silently change the target structure.

If an unplanned case appears, stop and report it.

## 7. Preserve provenance and unrelated changes

Keep enough information to reconstruct where significant material came from when the plan requires it.

Preserve:

- unrelated user edits;
- existing accepted repository history;
- external identifiers needed for traceability;
- source files that must remain unchanged.

When possible, prefer operations that preserve Git history and traceability.

## 8. Validate before and after

After migration, compare the final state with the original inventory and approved migration map.

Check:

- expected files are present;
- intended moves and renames occurred;
- no unexpected files disappeared;
- no unintended duplicates were introduced;
- references still resolve where required;
- Git/LFS state is correct;
- ignored/generated files behave as intended;
- unresolved items remain where the plan says they should;
- no cloud content was downloaded without authorization.

For large or valuable accumulations, preserve a concise before/after record.

## 9. Handoff

Report:

- what was inventoried;
- what was migrated;
- any deviations from the map;
- validation performed;
- unresolved or blocked items;
- any operation intentionally not performed because permission was missing.

Do not declare structural ambiguity resolved unless the approved design actually resolves it.
