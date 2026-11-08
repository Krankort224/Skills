# Read project context

Use for ordinary context gathering and project questions. This operation reads and interprets; it does not repair references, install tools, rebuild graphs or change task/Git/GitHub state.

## 1. Locate the task and current scope

Identify the project root, requested outcome and the branch/worktree/component/platform actually under discussion. Establish whether the question asks about intended design, actual behavior, a constraint, a decision or history. Different questions can have different owners.

Use the installed `references/repository.md` when available. If using a shared skill against another project, locate that project's installed map; the shared source template does not describe the target project. Check path conventions rather than assuming that a map's paths are relative to the shell's working directory.

With no map, inspect project instructions, the stated entry point/README and a bounded inventory of relevant sources. Infer only a provisional reading route, verify it at those sources, and disclose any material missing overview/owner. Do not create a map during a read task. A missing template or CLI is irrelevant to this fallback.

## 2. Form a useful project view

Read enough of the overview to explain the project's purpose, material boundaries, component roles and key interactions. A narrow lookup usually needs only the relevant overview portion; a whole-project assessment needs its major relationships before local detail.

For example, knowing that a repository has `api`, `jobs` and `reports` directories is insufficient to explain whether the API queues work, whether a worker reads approved input, or who owns the report format. Follow the sources that establish the task-relevant relationships. Do not invent a dependency from directory proximity or shared terminology.

Before relying on a map claim, check that its scope and cited owner still fit the current checkout. A dead link, renamed component, copied branch claim or source contradiction reduces that claim's reliability; it does not invalidate every other route in the map. Treat map freshness observations as local evidence, not a blanket promise that the whole project was checked.

## 3. Follow the authoritative route

Resolve three roles for each material question:

| Role | Question |
|---|---|
| Knowledge owner | Which canonical source owns the durable fact or contract? |
| Evidence | Which document, implementation, data, test or observation verifies this particular claim? |
| Update destination, if changes are under consideration | Where would an authorized correction belong? Is that source editable? |

These roles can differ. An accepted design may own intended behavior while code/tests show a defect in actual behavior. An archived primary input may own historical measurements while a current design document owns the selected design value. Preserve both roles; do not silently rewrite one into the other.

Follow the map's stable route to the necessary primary/canonical source. Verify exact symbols, values, definitions, evidence locations and applicable editions/scopes when they affect the answer. Read relevant surrounding conditions, not only a search hit. Search and targeted ranges are appropriate after locating the area; expand when dependencies or contradictions make them insufficient.

If the owner/destination is missing or ambiguous, inspect authoritative project instructions or subject-specific source references. Where further accessible evidence cannot resolve it, state the gap and its practical effect. Do not decide by recency alone or invent an owner to make the answer look complete.

## 4. Resolve contradictions and derived evidence

When claims disagree, identify each claim's source, scope, role and validity boundary; apply the project's authority rule for that subject. Distinguish a superseded/historical statement, a map error, a design/implementation mismatch and a genuinely unresolved conflict. Check history only if it helps establish those roles.

An existing graph/report can suggest related sources when useful. Select only relevant nodes/edges/excerpts and inspect source file/location, direction, confidence, extraction origin and available corpus/coverage identity. A missing edge is not evidence of no relationship; file presence is not proof of full semantic reading. A stale or unverified claim must be checked directly at its owner before use. Do not place a whole graph into agent context for a narrow question or impose graph-first reading. Native loaders may read the full JSON in their process before returning bounded results; check size/resource suitability separately.

No graph/CLI is needed for this operation. If native Graphify investigation is deliberately selected, first use the technical guide's strict-read limits: CLI query/path/explain can attempt file writes, and a native loader may read optional derived sidecars. Use only a verified read-only, in-scope route or continue with direct sources. For a known fresh structural or mixed stage without sidecars, the guide supplies a tested bounded read-only query. Arbitrary published graphs and broader investigative methods retain their separate scope/validation requirements.

## 5. Stop at sufficient context and answer

Context is sufficient when the following are known to the extent needed by the task:

- the project's purpose and the applicable scope/component relationships;
- the relevant fact/contract owners and authoritative supporting evidence;
- current task-relevant state, constraints and material dependencies;
- update destinations and immutable/write boundaries when a change is contemplated;
- material conflicts, uncertainty and coverage/access limits.

Stop when further reading is unlikely to materially change the result. Do not read every source to claim familiarity. Give a direct answer with useful source locations/links and distinguish verified facts from inference or unresolved questions. Mention stale/missing reference material when it affects confidence or the next action; leave repairs to an authorized maintain task.
