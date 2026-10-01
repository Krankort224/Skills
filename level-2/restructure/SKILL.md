---
name: restructure
description: Restructure an existing repository or file accumulation by inventorying what exists, designing a minimal target structure, and migrating it without losing provenance, current state, or important data.
metadata:
  short-description: Restructure repository contents
---

# Restructure

Restructure an existing repository or file accumulation by reducing ambiguity and future work cost.

Do not impose a universal directory tree. Derive the target structure from the actual contents, roles, lifecycle boundaries, and project needs.

The work normally alternates between two execution contours:

1. Codex discovers and inventories the physical file state.
2. ChatGPT interprets the inventory and designs the target structure.
3. Codex performs the approved migration and validates it.
4. ChatGPT reviews the result and resolves remaining ambiguity.

Load only the instructions for the active contour:

- ChatGPT: read `references/chatgpt.md`.
- Codex: read `references/codex.md`.

## Invariants

- Inventory before restructuring.
- Separate observation, design, migration, and review.
- Preserve provenance.
- Prefer the smallest structure that resolves real ambiguity.
- Do not create categories only for symmetry or future possibility.
- Do not force uncertain items into arbitrary categories.
- Restructuring changes organization by default, not content or project architecture.
- Preserve unrelated user changes.
- Do not delete potentially valuable material merely because its role is unclear.
- Keep unresolved cases explicit.

## Cloud-file boundary

Cloud-hosted file contents must not be downloaded, materialized, synchronized, exported, or copied into the local environment without a separate, explicit, and unambiguous user authorization.

Without that authorization, it is acceptable to inspect available listings and metadata such as names, paths, sizes, timestamps, identifiers, and relationships when the platform exposes them without downloading the file contents.

Do not interpret repository restructuring as implicit permission to download cloud files.

## Quality criterion

A good restructuring is not defined by a neat directory tree.

It is defined by lower ambiguity, clearer ownership of current state, preserved provenance, and lower cost of future work.
