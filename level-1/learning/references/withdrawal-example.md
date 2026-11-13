# Worked withdrawal: an added file can acquire another owner

Use this example when a candidate spans an operation, a new resource and its route. It deepens the existing [consolidate](../operations/consolidate.md#roll-back-only-the-candidate) method; it is not a general inverse tool or permission to edit a project. The runnable [fixture](../tests/evaluation_fixture.py) uses authored text in temporary files, not production rollback.

## Establish the change set and current state

| File | Baseline | Candidate | Later unrelated work |
| --- | --- | --- | --- |
| `operation.md` | Original check sentence | Sentence replaced with an added boundary check | A separate local note appended |
| `index.md` | Route to the operation | Route to new `boundary.md` added | A route to existing `retained.md` appended |
| `boundary.md` | Absent | Candidate-only explanation | Either unchanged, or a contributor note added |
| `retained.md` | Existing reference | Unchanged | Must remain |

Compare these actual states before writing. The candidate's file list alone is insufficient: a file absent at baseline can contain protected work now. Likewise, a later route can depend on it even when the original candidate route is removable.

## Derive a bounded inverse

When the operation sentence and candidate route still match their reviewed edits, and the added resource contains only candidate content:

1. Inverse only the operation sentence, preserving the local note.
2. Remove only the candidate's route; preserve the later route and its existing destination.
3. Remove the added resource only after checking its current content/ownership and remaining references.
4. Re-read exact resulting content and inspect every affected surviving route. Record what behavior the restored baseline still lacks; withdrawal does not resolve the original gap.

These checks require the actual current state and the project's established coordination of writes. Matching text or a hash is a local preservation check, not an atomicity or universal ownership guarantee.

## Refuse an ambiguous deletion

If the added resource now contains the contributor's independent note, deleting the whole file loses protected work. If the operation sentence changed in an overlapping way, applying the old inverse guesses at intent. Preserve the affected current files/routes and return the exact overlap/dependency to its existing owner. Claim partial withdrawal or deferral as appropriate; do not report a clean rollback while candidate-dependent content remains.

Moving the note elsewhere can be a separate authorized resolution after its meaning, owner and incoming references are established. Do not invent that destination merely to make a deletion check pass.

The useful reusable technique is a current-state change map followed by a verified minimal inverse. It adds a worked boundary, not another approval ceremony, global journal or rule to remove all newly created files.
