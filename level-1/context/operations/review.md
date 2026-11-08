# Review project references

Assess whether the references give an accurate, useful and appropriately bounded project view. Review is read-only. Findings do not authorize corrections unless the task also asks for fixes; perform authorized reference fixes through maintain and then check them again.

## 1. Set review scope and evidence

Identify the target repository/root, branch/worktree/platform and requested breadth: whole-project overview, selected scope, changed references or a specific uncertainty. Locate the installed map and its fact-owning sources. Shared templates supply criteria, not project facts.

Choose representative questions before following the map's proposed routes. For an overview, cover purpose, major components, an important interaction, a material constraint, current state and its owner. For a targeted review, choose the task's relevant subset. Include a conflict/history/derived-evidence case when present. Use direct sources to establish the answers; checking only that links exist is insufficient.

If no map exists, assess the available direct-source route and state whether the missing overview materially impedes the task. Do not initialize a map or install Graphify during review.

## 2. Check usefulness and accuracy

| Area | Review method |
|---|---|
| Purpose and boundaries | Can another agent explain the project's goal, supported scope and material exclusions from the overview, then verify them at the right owners? |
| Components and interactions | Does the map explain meaningful hierarchy/roles and how inputs, decisions, data or outputs move between parts? Is it more than a directory listing/link index? |
| Source ownership and authority | For different kinds of facts, does the map identify owners, evidence and update destinations where needed? Are immutable inputs and unclear ownership distinguished? |
| Current versus historical | Are accepted current facts separated from archived decisions, superseded drafts, prototype/other-branch claims and unresolved alternatives? |
| Constraints and language | Are material constraints scoped/sourced and human-facing knowledge in its established language? Are detailed contracts kept with their owners? |
| Navigation and sufficiency | Do representative routes reach resolving sources with useful locators and bounded reading? Are missing/renamed links and unnecessary detours visible? |
| Local adaptations | Have project-specific sections, source roles and valid local notes survived refresh, rather than being replaced by template boilerplate? |
| Evidence/coverage | Are verified facts, inference, uncertainty and unexamined areas distinguishable? Does a statement of completeness have actual evidence? |

For each material claim sampled, inspect its cited owner and enough surrounding context to establish correctness. Broaden a sample only when findings or the requested scope justify it. Record what was actually checked: a targeted sample cannot certify every source or every project scope.

## 3. Review derived graph material only as warranted

A graph's absence is not automatically a defect in a map-based project. If graph-backed claims are part of the review, check available artifact identity, source/coverage status, direction, confidence/origin and correspondence to canonical sources. Missing, stale, incompatible, partial or corrupt artifacts reduce the relevant claim's support; they do not block direct-source review.

For a mixed graph, sample semantic claims against exact supporting source ranges, source authority and confidence/rationale. Inspect the expected-shard/receipt ledger, including EOF, zero findings and unresolved questions; declared receipts and successful mechanical validation do not prove model understanding. Unknown usage must remain unknown. A supported native refresh preserving explicit semantic origin is a tier-retention check, not proof of fresh semantics after source changes.

For refreshed/published mixed evidence, resolve one immutable artifact commit and check the complete trio, generation markers, final sibling hashes, portable coverage/original-fragment provenance and current source/profile/scope identity using the guide's [freshness method](../tools/graphify.md#freshness-portability-and-publication). Sample dependency ownership, common authority inputs, confirmed removals and invalidation propagation; review labels against the semantic evidence identity as well as membership. A checksum or a declaration of complete ownership cannot prove model understanding. Changed-source work needs a fresh structural baseline and actual newly read invalidated semantics; unknown or failed work cannot be filled with old claims. Confirm that competing/failed publication preserves a coherent last-good commit and that a claimed rollback is a new compatible fast-forward commit.

Do not equate three filenames, a build exit code, node count or a connected graph with a complete semantic read or a successful publication transaction. HTML generation is distinct from browser rendering; network/CDN requirements and aggregation affect what the view can show. The shared `.gitkeep` promises none of these capabilities.

When presentation or an optional derived view is in scope, inspect actual [HTML/report/export behavior](../tools/graphify.md#inspect-presentation-and-select-optional-exports), not only file creation: source/count correspondence, render assets, filtering and aggregation loss. GraphML/SVG/wiki/Obsidian are optional and have distinct evidence/ownership limits; their presence is not a current trio or complete semantic summary. Cross-repository review checks [explicit input namespaces and versions](../tools/graphify.md#inspect-scoped-cross-repository-views), directed/parallel arc preservation, external identity joins and separate destinations. Compare representative answers with direct-source controls; record both missed/false suggestions and avoid unsupported effort-saving claims.

Use the technical guide only for a specifically needed audited limit/method. Review does not install optional tools, regenerate artifacts, invoke provider APIs or enable feedback/hook services. Unsupported/untested graph capabilities remain explicit findings or later gates.

## 4. Return actionable findings

Lead with material defects: an incorrect fact, authority error, scope leak, missing relationship, unsafe write boundary, broken route or unsupported claim. For each finding give the affected claim/location, authoritative evidence or unresolved gap, practical impact, and correction destination/action. Separate a known contradiction from lack of evidence and distinguish task-blocking gaps from minor navigation improvements.

Report the representative questions checked, their source-backed outcomes, review breadth and remaining limits. If no material defect is found, state the checked scope rather than claiming universal correctness. Do not accept/close an Issue or major pass from a review result alone.

When fixes were already requested, make only the authorized changes using maintain, preserve unrelated sources/adaptations and recheck affected questions/routes. Clearly distinguish original findings, corrections made and unresolved items; avoid presenting a recommendation as an applied change.
