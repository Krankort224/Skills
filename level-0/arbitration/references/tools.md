# Running the arbitration tools

Both commands use Python 3 and the standard library. Invoke the scripts from the directory of the actual activated skill. The working directory can be any project. A system command or registered harness tool may replace a script if it provides the same inputs, checks and results. Inspect the exposed command/schema when choosing it. Neither script starts a session, assigns work or changes a project.

## Read a skill

At the beginning of an arbiter turn, a standing instruction can say: “Use arbitration from Krankort224/Skills each turn. Resolve the current revision immediately before reading; open the file by that commit.” This also works on the first turn without a preinstalled command. Use Git or a GitHub connector to resolve main and fetch the entry point by SHA, then use the tools from that verified package. A copied manifest, an old receipt and an earlier session preload each identify a possible source; check the current read separately.

```text
python "<skill directory>/scripts/read_skill.py"
python "<skill directory>/scripts/read_skill.py" level-0/arbitration/references/codex-dot.md --repo "<Skills checkout>"
```

The optional path is relative to the canonical Skills repository. The default is `level-0/arbitration/SKILL.md`. Stdout contains the exact UTF-8 document. Stderr carries the selected commit, observed main, how they were obtained, and the document's SHA-256. A nonzero exit means the read failed. Use the selected commit for related resources in the same read. The tool reads committed objects or content addressed by commit. It can use an available checkout as an object store, or GitHub without a clone.

- For an explicit version, pass `--revision FULL_SHA`. Preserve the difference between that version and the separately observed current main.
- When the shell cannot resolve GitHub, query the canonical main ref through an available authorized connector and supply the freshly observed `--connector-main FULL_SHA`. A connector-only host can instead fetch the path at that SHA through the connector. Record the actual route.
- If all available GitHub routes fail, supply the last known full SHA via `--offline-known FULL_SHA` and use verified local content. A flattened installation without Git objects can add `--cached-file FILE --receipt RECEIPT.json`: keep the document and stderr receipt from an earlier trusted successful read. The reader verifies repository, path, selected commit and actual file digest. Freshness remains unverified. If the exact content cannot be recovered, report the unavailable read.

## Review an assignment

Run `python "<skill directory>/scripts/review_assignment.py" show` with one UTF-8 JSON object on stdin. Send the actual source, user amendments in order, recipient and complete draft. For example:

```json
{"source":"Explain why the two row counts differ. Read only.","amendments":[],"recipient":"comparison worker","assignment":"Find the extra row, then remove it."}
```

Inspect the returned `packet` and `digest` before deciding. Supply those two values unchanged to the same script's `decide` command, together with the following fields:

```json
{"comparison":"Finding the extra row explains the count. Removing it would write to the source.","reason":"The requested result is a read-only explanation.","decision":"revise"}
```

Use a JSON serializer or stdin redirection to preserve the input exactly. Always check the exit status and the `ready` field. A successful `revise` decision has `ready: false`. Correct that example to “Identify the extra row and return its ID and the source counts.” Present the revised packet with `show`, compare it and decide again. On `ready: true`, dispatch only the exact assignment to its declared recipient through the authorized route. Corrections and later work orders repeat the procedure even for an existing worker. The program checks fields and packet identity. Its result records the arbiter's judgment; it cannot observe a send, verify that a source was authentic or decide whether a text matches the user's intent.

## Find the package in each host

- **Codex.** Use the actual skill path advertised by the active catalog or the exact shared checkout selected for this task. Invoke the script via the callable execution surface.
- **Hermes.** Use the directory reported on skill activation (or the supported `${HERMES_SKILL_DIR}` substitution), and confirm the same files are visible to the terminal backend. A URL installation needs explicit file references in `SKILL.md`. A session preload alone does not establish a fresh read on a later turn.

For an installed copy, identify the source revision and verify the scripts actually used against that snapshot. When only a text-reading connector is exposed, it can perform the immutable read. Assignment review still requires an equivalent registered tool or an authorized environment able to run the verified reviewer with the actual input.
