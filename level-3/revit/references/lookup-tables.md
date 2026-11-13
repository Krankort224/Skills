# Embedded lookup tables

Use this procedure when editing family lookup tables or diagnosing values calculated through `size_lookup`. Identify the loaded family, formulas and affected instance/type parameters using the [modeling procedure](../operations/modeling.md). Keep family names, parameter mappings, intended size ranges and option limits in project configuration.

## Export and understand the loaded data

1. Export the tables embedded in the loaded family through `FamilySizeTableManager` and `ExportSizeTable`. Retain the original files as the baseline and record table names, row counts and file hashes. Compare library files with this export before using their contents for edits.
2. Read the family formulas. Establish the table-selection rule, output column, fallback value and complete ordered lookup key, including option selectors, dimensions, data types and units. Inspect the header's full typed column definitions. Repeated display names can have different specifications. Match columns by position and definition.
3. Parse the actual CSV dialect. Record delimiter, quoting, encoding, decimal representation and typed header syntax. Source-library files and native exports can use different delimiters. Use a CSV parser and generate files in a format verified by native import and re-export.
4. Inventory all rows by complete key and by size/configuration. Count unique option combinations per size, identify conditional combinations and compare output templates. Record identical duplicates separately from conflicting outputs for the same key. Resolve conflicting keys before using them as generation sources. Preserve original duplicate multiplicity unless their repair is included in the task.

## Define additions or reductions

Determine the intended configuration coverage from the task and the observed matrix. A missing size can require many option combinations. Compute rows per size and total additions before generation. Derive valid combinations and any size-dependent output rules from the complete table and applicable product/project sources. A Cartesian product of independently observed option values requires evidence that those combinations are valid.

When a common output pattern is demonstrated across existing sizes for a given option tuple, reuse it within the authorized scope and substitute the intended dimensions. Investigate inconsistent patterns before extending them. Table-derived project labels provide no independent confirmation of manufacturer availability or order codes.

For reductions, apply the requested criteria to typed values with explicit units and inclusive/exclusive boundaries. Check every installed lookup key and its expected output, then account for intended future configurations. Report any installed keys removed by the proposed filter before dependent writes. Keep project-specific aspect ratios, option codes and cutoffs out of general defaults.

Generate a reviewable change set with table assignment, sizes, option combinations, expected outputs and counts. Preserve table names used by formulas and verify routing at range boundaries. Estimate import and reload cost using the resulting data volume and the current model. Follow the existing [batch and recovery rules](mcp-operations.md#границы-вызовов).

## Import and verify

1. Prepare edited CSVs offline. Compare original and proposed data as typed multisets so duplicate rows remain significant. Account for each addition and authorized removal. Verify retained rows, unique new keys, expected outputs and installed-key coverage.
2. Select a supported native route using the target-version [API contract](api.md). For family-copy editing, obtain the copy from the loaded family so existing project types and formulas are represented. Keep an identifiable original RFA and CSV baseline for recovery.
3. Import one table per bounded invocation through `ImportSizeTable`, inspect its result and `FamilySizeTableErrorInfo`, and verify the transaction outcome. Reopen or reacquire the modified document in a separate read and export the table again. Compare every typed row and its multiplicity with the proposed data. Row counts alone cannot establish equality.
4. If direct project import is used, verify calculated instance values after regeneration and commit. A successful import and matching table contents can coexist with stale formula results. When observed, resolve the completed attempt and use a verified alternative, such as import into a family copy followed by reload.
5. Complete table preparation and readback before the separate family reload. Apply the [reload identity checks](mcp-operations.md#перезагрузка-семейства), then independently read the project. Check all affected lookup keys and calculated outputs, including former fallback cases, retained valid values and relevant schedule fields. Compare type parameters, instance assignments, geometry and physical connections against the baseline.
6. Verify file persistence, project commit, project save and synchronization as separate outcomes. After an error or partial receipt, inspect actual state before retrying. Recover from the recorded original data only when the observed state calls for it, within the task's authorized scope.

## Observed behavior and limits

In a working case on 2026-11-13 with Revit 2022.1 and rvt-mcp 1.2.1, library CSVs used pipe delimiters while native exports used commas. Full-table analysis established a repeated option matrix across sizes and exposed one duplicate key with a missing alternative. That matrix determined the additions. A later user-defined reduction retained every installed lookup key. These observations establish the need to inspect actual schema and coverage for each family.

In the same case, direct project `ImportSizeTable` followed by regeneration left a calculated instance value at its fallback. Import into a family copy, semantic re-export comparison and reload produced the expected project values. This records behavior in that family and host profile. The direct-import failure mechanism was not established. Validate recalculation in the actual target rather than assuming either route always succeeds.
