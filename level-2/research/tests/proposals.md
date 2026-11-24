# Proposals

These six records are fictional. Quoted procedures and observations are the supplied evidence. The task permits analysis only.

| ID | Proposal | Record |
| --- | --- | --- |
| A | Add a check that the exported row count matches the input count. | Export guide v3, step 4, already requires the two counts to be compared. The operator read v3, performed steps 1–3, and delivered 19 of 20 rows without comparing counts. |
| B | Copy the sheet-naming rules into the export guide. | In guide v3, the prescribed naming link opens a missing page. The naming guide at its current address correctly handles the sheet in question. The operator followed the published link. Both addresses were checked at that revision. |
| C | Use prefix `NW-` in all equipment exports. | The signed North Wing delivery specification requires this prefix. The shared guide reads the prefix from each project's delivery specification. A second project requires `S2-` and accepts its exports with that prefix. |
| D | Always clear the cache before retrying a failed import. | An operator recalls a failed import followed by a successful one. Between attempts they cleared the cache, corrected a header and restarted the importer. The failing file, original error and importer revision were not retained. |
| E | Match quantities by tag while keeping schedule order. | Merge guide v2 guarantees correct results for unique, matching tag sets in any worksheet order. It says to reject duplicate or unequal tag sets, then copy quantities by row position in schedule order. An operator followed v2. The comparison below records a trial of the proposed edit. |
| F | Match quantities by tag and sort output by tag. | An editor proposed this alternative to E for the same v2 guide. The delivery contract requires the output tags to follow the schedule's row order. Both candidates retain v2's input validation. |

The following are recorded outputs from the same worksheet trials. Each output cell lists tag and quantity in delivery order. Candidate E walks the schedule and looks each tag up in the quantity worksheet. Candidate F sorts the result of that lookup by ascending tag.

| Schedule tags in order | Quantity worksheet rows in order | Guide v2 | Candidate E | Candidate F |
| --- | --- | --- | --- | --- |
| A, B | B=8, A=3 | A=8, B=3 | A=3, B=8 | A=3, B=8 |
| C, A, B | B=4, C=7, A=2 | C=4, A=7, B=2 | C=7, A=2, B=4 | A=2, B=4, C=7 |
| B, A | B=5, A=1 | B=5, A=1 | B=5, A=1 | A=1, B=5 |
