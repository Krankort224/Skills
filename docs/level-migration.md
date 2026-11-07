# Four-level migration and adoption

Selection policy is owned by [AGENTS.md](../AGENTS.md#usage). This document records migration compatibility, not another orchestration contract.

## Source map

Baseline: `c11000bae812d9a87b366f44fa6d5706a5915a4a`.

| Previous source | Current source | Skill identifier |
| --- | --- | --- |
| `level-2/revit-scripting/` | `level-3/revit/` | `revit-scripting` becomes `revit` |
| `level-2/word/` | `level-3/word/` | `style-transfer` is preserved |
| `level-2/project-space/` | `level-3/project-space/` | `project-space` is preserved |

`architecture`, `research` and `restructure` remain Level 2. Level-0 arbitration and the three Level-1 skills retain their source locations. No `mep` directory or new Revit functionality is introduced.

Move each complete skill subtree; keep its internal relative layout and resources. Old and new source paths have equal depth. Word is an exact subtree move; Revit and Project-space change selection metadata, not their operations or libraries. The architecture interface and structural validator must agree on semantic invocation.

## Existing installations

Source reclassification does not itself migrate an installed skill. Keep installed skills directly under the project's skill directory, preserve local adaptations and record the adopted revision. Update current installation pointers and Revit invocation names when adopting this revision. Do not rewrite immutable historical source pins merely because their paths are old. A historical pin still names the source as it existed then.

Operations-hub's existing `skills/SOURCES.json` records a prior adoption and is not rewritten by this migration. Bulk downstream changes require their own scope. Original `*.template.*` files remain in Skills; adopted completed maps/forms remain with their projects.

## Selection review cases

These are expected contract outcomes, not claims of a model-execution benchmark. Level-1 roots apply in every row; only task-relevant supporting procedures load.

| Task/role | Expected selection |
| --- | --- |
| Ordinary root implementing a bounded change | Level 1; no automatic arbitration |
| Worker carrying out a bounded assignment | Level 1 and relevant domain/software skills |
| dot or a user-assigned equivalent coordinating arbitration | Level 0 plus Level 1 and task-relevant skills |
| Develop a building concept without mentioning a skill | `architecture` |
| Design an evidence-producing engineering experiment | `research` |
| Reorganize a repository using an agreed migration map | `restructure` |
| Diagnose a Revit/Dynamo parameter-access failure | `revit` |
| Develop architectural decisions in an established Revit workflow | `architecture` plus applicable `revit` knowledge |
| Create or restyle an editable Word/DOCX document | `style-transfer` from `level-3/word` |
| Manage a task in an identified Project-space store | `project-space`; existing actor/access rules still apply |
| Mention Revit while asking a software-independent design question | No automatic Revit operation solely from the mention |
| Ambiguous use of “architecture” for software structure | Establish the actual domain; do not infer building design from the word |
| No Issue is being worked on | Read workflow's applicability rule; do not start its Issue lifecycle |
| Ponytail appears in external references | No automatic installation, hooks or policy import |

## Regression evidence

Review the final Git diff with rename detection and compare the unchanged resource tree/blob identities to the baseline. Search active sources for obsolete paths and explicit-only selection rules; the previous paths above and immutable source links are intentional historical references.

Available checkout checks include the architecture structural validator and its tests, Revit library/Dynamo tests, and the existing Word/Project-space checks. Run only applicable available checks and distinguish source/object preservation, syntax checks, offline tests and native-host execution in the Issue handoff. A directory move or a passing static check does not certify Revit, Word or Windows runtime behavior.
