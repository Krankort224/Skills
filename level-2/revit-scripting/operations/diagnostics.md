# Diagnostics

## Inputs

Use exact code/graph revision, runtime/engine, input shape, error/log and expected behavior. Keep collection read-only. Review does not authorize executing a document write.

## Procedure

1. Classify the failure: wiring/payload, runtime/API, parameters/units, geometry/reference, transaction/readback or model constraints. Follow the matching [error pattern](../references/error-patterns.md).
2. Inspect the raw artifact before trusting its report. Run `scripts/inspect_dyn.py`; load relevant Python with `--code NODE_ID`. Trace the wire to its producer and compare actual `IN[n]`/`OUT` contracts.
3. Separate observations from hypotheses. Pin revision and find the first violated invariant. Distinguish absent input, unsupported scope, ambiguity and failed API calls. Read only the reference needed to discriminate causes.
4. Reduce the case with raw records or a read-only probe. Preserve units, document identity, frame and schema; do not build a reproduction that assumes the intended answer.
5. Test the cause using available capabilities. Mocks test their stated logic assumptions; native behavior needs Revit evidence. Successful fallback does not prove the primary path worked.
6. Report finding, evidence, affected scope and minimal correction. If a fix is authorized, continue with [adaptation](adaptation.md), preserving the baseline. Otherwise deliver findings without document writes.

## Result and completion

Provide demonstrated cause or a bounded ranked set of unresolved causes, supporting raw artifact, reproduction and next discriminating check. Mark inaccessible or unfinished evidence; an old successful log does not establish current model state.
