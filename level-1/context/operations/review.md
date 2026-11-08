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

For mixed evidence, use the [build method](graphify/build.md#semantic-reading-and-reconciliation) as the reading/evidence criterion: sample semantic claims, authority/confidence, complete expected coverage, zero findings and uncertainty against actual source ranges. Receipts, checksums and successful validation do not establish understanding. Distinguish fresh agent reading from replay and preserve unknown usage.

For refreshed/published evidence, use [graph maintenance](graphify/maintain.md) to inspect one immutable complete generation, current source/profile compatibility, retained provenance, dependency/removal decisions and newly read invalidated material. Sample interpretation against current evidence as well as membership. Review publication/recovery claims against coherent last-good output and the existing authorized workflow.

When presentation or an optional view is in scope, use [graph export inspection](graphify/export.md) to check actual rendering/correspondence, output ownership, format loss and cross-repository namespaces/versions. File creation, three filenames, graph counts or connectivity cannot substitute for semantic completeness, source truth or successful publication.

Load only the applicable method and its needed technical references. Review findings do not authorize installation, regeneration, optional exports, provider calls or background integrations; unsupported/untested capabilities remain explicit findings or later verification gates.

## 4. Return actionable findings

Lead with material defects: an incorrect fact, authority error, scope leak, missing relationship, unsafe write boundary, broken route or unsupported claim. For each finding give the affected claim/location, authoritative evidence or unresolved gap, practical impact, and correction destination/action. Separate a known contradiction from lack of evidence and distinguish task-blocking gaps from minor navigation improvements.

Report the representative questions checked, their source-backed outcomes, review breadth and remaining limits. If no material defect is found, state the checked scope rather than claiming universal correctness. Do not accept/close an Issue or major pass from a review result alone.

When fixes were already requested, make only the authorized changes using maintain, preserve unrelated sources/adaptations and recheck affected questions/routes. Clearly distinguish original findings, corrections made and unresolved items; avoid presenting a recommendation as an applied change.
