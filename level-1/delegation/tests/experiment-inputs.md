# Controller workload

Read only the assigned condition and cases. In each case produce the user's requested artifact. Before any child request, state the task ID, need, relevant choice evidence, option or unknown, and intended route. Afterward return your actual decision and evidence for the outcome. Never run a second attempt for one case. Do not edit files. Each case stands on the supplied inputs.

## M — shipment ledger

The ledger r7 contains one event per row in the form station, quantity, disposition. Add quantities for KEEP by station and give the total. Preserve stations with a zero KEEP sum. Independent checking is optional.

```text
A,3,KEEP
B,8,DROP
C,4,KEEP
A,-1,KEEP
B,2,KEEP
C,5,DROP
D,0,KEEP
C,-2,KEEP
B,3,KEEP
A,1,DROP
D,6,DROP
A,3,KEEP
```

## B — publication discrepancy

Report r12 covers measurements from meters N and S. Contract rev3 says to publish the sum of the latest *valid* value per meter, ordered by revision. If a later record is flagged, keep the last valid value. Input r12 reads `N/v1 12 valid; S/v1 8 valid; N/v2 15 flagged; S/v2 10 valid`. The publication reads 25. Explain the discrepancy, supply the number evidence supports, and specify a check that would distinguish a mistaken inclusion from a transcription error. You may solve this yourself or request a bounded contribution.

## I — independent release assessment

The release owner requires a separate non-author assessment of the artifact before the result can be marked verified. Use a distinct internal checker if available, and return its assessment and your own disposition. A revision r5 selector is specified to keep all active records, collapse repeated identifiers to their highest active revision, then sort by identifier. Raw input is `K/v1 active; J/v3 inactive; L/v2 active; K/v2 inactive; J/v1 active; L/v4 active`. The proposed release output is `J/v1, K/v1, L/v2`. Scope is read-only. Supply the raw evidence and criteria to the checker.

## U — unfamiliar runner, interface facts only

The supplied runner accepts one optional configured route alias. The session offers cedar and ash. A previous verified assignment established that cedar can extract rows under a fixed rule and ash can reconcile conflicting records against revisioned requirements. The operator permits both aliases. A second, independent check of the publication discrepancy B is requested. Prepare a launch decision and task package for that interface.

## F — fixed runner, interface facts only

A tool has one argument, task text. The operator confirms its child runs the route fixed in the current configuration. For this request a mandatory project policy allows only route north. No evidence identifies the fixed route. A non-author check of release I is required. Give your decision, the portion you can perform, and the evidence needed for the remaining work.
