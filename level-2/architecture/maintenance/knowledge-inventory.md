# Architecture knowledge inventory — Issue 10, Stage A

Status: baseline evidence for the combined A+B review. This is maintenance material, not an active skill entry point or a replacement for the design methods. No physical migration or knowledge removal is performed by this report.

Baseline repository: `Krankort224/Skills`.
Baseline commit: `d260c6cb845734f9fe2e7a86bc1ca97cc1f46e72`.
Scope: `level-2/architecture/**`, all 67 baseline files.
Working branch: `architecture/issue-10-knowledge-graph`.

## Contents

- [Evidence and counting method](#evidence-and-counting-method)
- [Mechanical baseline](#mechanical-baseline)
- [File manifest](#file-manifest)
- [Knowledge and ownership findings](#knowledge-and-ownership-findings)
- [Coverage and depth priorities](#coverage-and-depth-priorities)
- [External sources and local autonomy](#external-sources-and-local-autonomy)
- [Six PDF dispositions](#six-pdf-dispositions)
- [Verification and limitations](#verification-and-limitations)
- [Reproduce the inventory](#reproduce-the-inventory)

## Evidence and counting method

The complete pinned skill was inspected mechanically. The three pilot references were read in full: `program-and-space.md`, `composition-and-style.md`, and `performance-and-coordination.md`. The current root, knowledge map, notices, source identity/adaptation sections, and checker implementation were inspected. Other references were inventoried by actual heading structure and their declared method/ownership records; this is not a claim to have independently revalidated every architectural statement or every original source.

File sizes below are UTF-8 bytes, not character counts. Lines use Python `splitlines()`; a final newline does not create an additional line. H2/H3 count ATX headings in Markdown files. File roles describe primary use and do not confer authority on indexes or generated evidence.

Local-link extraction uses the baseline checker's inline-link and reference-definition expressions after excluding fenced code. It includes table-of-contents/self links and image/data links. Distinct file edges deduplicate `(source, destination)` and exclude self edges. Reachability starts at `SKILL.md` and follows explicit Markdown links only. Code-fence commands and loader metadata are deliberately not graph edges. Fragment checks use the existing checker's slug logic, not a claim of full GitHub-flavored Markdown parsing.

For external references, keep four measurements separate: textual URL occurrences, parsed Markdown link occurrences, distinct complete URLs, and document URLs normalized only by removing `#fragment`. Do not collapse query strings, different revisions, or different documents. Exclude the skill's own repository URLs from strict external counts. The directory-based non-normative view excludes `references/normative/**`; semantic classification of regulatory material is a separate assessment.

## Mechanical baseline

| Measurement | Observed result |
| --- | ---: |
| All baseline files | 67 |
| Markdown files | 60 |
| Total file bytes | 1,151,509 |
| Primary roles | 3 navigation; 2 provenance; 1 metadata; 2 data; 8 cases; 8 operations; 30 methods; 9 normative; 4 code |
| Explicit local-link occurrences | 1,401 |
| Distinct directed file edges, excluding self links | 448 |
| Missing local files or anchors under baseline extraction | 0 |
| Markdown files unreachable from `SKILL.md` | 0 |
| Root local-link occurrences | 103 |
| Knowledge-map local-link occurrences | 102 |
| Baseline structural check | PASS; 8 operations; 64 normative records |
| Baseline unit tests | PASS; 23 tests |

Five files are not reached through Markdown links: `agents/openai.yaml` and the four Python files in `scripts/`. They are metadata/command/test entry points, not unexplained orphaned knowledge. Both JSON case-data files are reachable.

The root has 42 distinct destination files including itself; the knowledge map has 34 including itself. All 34 map destinations are also root destinations. These are file-level observations, not proof that their selected fragments or purposes are identical. Root navigation should retain operation selection; the domain map should own subject discovery. Two full subject catalogues need not remain in both places.

## File manifest

Paths are relative to the skill root. `L` is local-link occurrences, `E` is parsed HTTP(S) Markdown-link occurrences. Bare URL text is counted separately in the external-source section. H2/H3 is omitted for non-Markdown files, where a string resembling a heading may merely be a test fixture.

| Baseline path | Role | Bytes | Lines | H2/H3 | L | E |
| --- | --- | ---: | ---: | --- | ---: | ---: |
| `SKILL.md` | navigation | 19355 | 143 | 6/0 | 103 | 0 |
| `THIRD_PARTY_NOTICES.md` | provenance | 7766 | 143 | 4/0 | 8 | 0 |
| `agents/openai.yaml` | metadata | 250 | 6 | — | 0 | 0 |
| `assets/compact-fit-study.json` | data | 3692 | 312 | — | 0 | 0 |
| `assets/family-fit-study.json` | data | 6616 | 532 | — | 0 | 0 |
| `assets/styles/art-nouveau/casa-batllo/analysis.md` | case | 13997 | 168 | 6/0 | 6 | 18 |
| `assets/styles/baroque/san-carlo-alle-quattro-fontane/analysis.md` | case | 12980 | 159 | 6/0 | 7 | 18 |
| `assets/styles/brutalism/barbican/analysis.md` | case | 9067 | 143 | 5/0 | 10 | 6 |
| `assets/styles/classical/pantheon/analysis.md` | case | 6675 | 112 | 6/0 | 7 | 2 |
| `assets/styles/gothic/chartres-cathedral/analysis.md` | case | 7203 | 117 | 5/0 | 6 | 1 |
| `assets/styles/modernism/villa-savoye/analysis.md` | case | 7409 | 119 | 5/0 | 9 | 3 |
| `assets/styles/organic/fallingwater/analysis.md` | case | 8498 | 138 | 5/0 | 10 | 4 |
| `assets/styles/renaissance/villa-rotonda/analysis.md` | case | 7331 | 122 | 6/0 | 7 | 4 |
| `operations/analysis.md` | operation | 3468 | 28 | 3/0 | 9 | 0 |
| `operations/brief.md` | operation | 4330 | 34 | 3/0 | 14 | 0 |
| `operations/concept.md` | operation | 4990 | 35 | 4/0 | 13 | 0 |
| `operations/development.md` | operation | 5938 | 49 | 4/0 | 22 | 0 |
| `operations/documentation.md` | operation | 6932 | 69 | 4/0 | 15 | 0 |
| `operations/optimization.md` | operation | 2575 | 25 | 3/0 | 8 | 0 |
| `operations/presentation.md` | operation | 2792 | 19 | 3/0 | 6 | 0 |
| `operations/review.md` | operation | 4676 | 35 | 3/0 | 12 | 0 |
| `references/building-use-families.md` | method | 23205 | 344 | 9/0 | 18 | 0 |
| `references/calculators.md` | method | 18546 | 115 | 6/4 | 6 | 5 |
| `references/composition-and-style.md` | method | 52985 | 649 | 10/8 | 27 | 0 |
| `references/computational-design.md` | method | 18342 | 282 | 8/0 | 15 | 0 |
| `references/design-completion.md` | method | 22873 | 335 | 5/0 | 14 | 0 |
| `references/design-development.md` | method | 27747 | 424 | 11/0 | 20 | 0 |
| `references/dwelling-fit.md` | method | 12523 | 204 | 5/0 | 9 | 0 |
| `references/envelope-and-assemblies.md` | method | 23105 | 284 | 8/4 | 15 | 0 |
| `references/environmental-operating-modes.md` | method | 29171 | 352 | 7/5 | 9 | 0 |
| `references/existing-building-adaptation.md` | method | 29771 | 387 | 6/0 | 14 | 0 |
| `references/frame-and-core.md` | method | 17192 | 250 | 7/0 | 12 | 0 |
| `references/ground-and-basement.md` | method | 14555 | 207 | 6/0 | 10 | 0 |
| `references/housing-and-court.md` | method | 14576 | 211 | 7/0 | 13 | 0 |
| `references/knowledge-map.md` | navigation | 26058 | 167 | 9/0 | 102 | 0 |
| `references/normative/index.md` | normative | 669 | 13 | 0/0 | 4 | 0 |
| `references/normative/ru/applicability.md` | normative | 15522 | 225 | 9/0 | 39 | 2 |
| `references/normative/ru/building-typologies.md` | normative | 19979 | 167 | 16/0 | 29 | 16 |
| `references/normative/ru/environment-and-interfaces.md` | normative | 26814 | 192 | 18/0 | 33 | 29 |
| `references/normative/ru/federal-framework.md` | normative | 20229 | 118 | 11/0 | 32 | 20 |
| `references/normative/ru/fire-and-accessibility.md` | normative | 31832 | 206 | 20/0 | 47 | 34 |
| `references/normative/ru/index.md` | normative | 13333 | 156 | 9/0 | 20 | 9 |
| `references/normative/ru/routes.md` | normative | 10892 | 93 | 8/0 | 90 | 0 |
| `references/normative/ru/territory-and-special-conditions.md` | normative | 18455 | 115 | 12/0 | 18 | 21 |
| `references/operation-and-lifecycle.md` | method | 13961 | 213 | 5/0 | 8 | 0 |
| `references/performance-and-coordination.md` | method | 37660 | 481 | 11/7 | 33 | 0 |
| `references/planning-and-section.md` | method | 44942 | 606 | 6/8 | 23 | 0 |
| `references/program-and-space.md` | method | 35000 | 478 | 7/7 | 26 | 0 |
| `references/quarter-and-public-space.md` | method | 26519 | 379 | 8/0 | 18 | 0 |
| `references/requirements.md` | method | 10576 | 181 | 9/0 | 12 | 0 |
| `references/roof-and-span.md` | method | 17839 | 221 | 8/0 | 12 | 0 |
| `references/site-and-context.md` | method | 14043 | 159 | 6/0 | 13 | 0 |
| `references/sources.md` | provenance | 147609 | 483 | 11/7 | 236 | 245 |
| `references/spatial-composition.md` | method | 15493 | 198 | 7/0 | 11 | 0 |
| `references/stair-section.md` | method | 8051 | 136 | 5/0 | 6 | 0 |
| `references/style-and-precedent-methods.md` | method | 16029 | 234 | 6/0 | 19 | 0 |
| `references/style-baroque-and-art-nouveau.md` | method | 16107 | 194 | 5/6 | 13 | 7 |
| `references/style-classical-gothic-renaissance.md` | method | 15470 | 186 | 5/0 | 16 | 1 |
| `references/style-directions.md` | navigation | 7739 | 86 | 5/0 | 32 | 0 |
| `references/style-modern-organic-and-brutalist.md` | method | 15477 | 235 | 5/0 | 17 | 4 |
| `references/timber-and-joints.md` | method | 18678 | 263 | 7/0 | 10 | 0 |
| `references/visual-delivery.md` | method | 14809 | 202 | 9/0 | 16 | 0 |
| `references/wall-floor-and-opening.md` | method | 13228 | 192 | 7/0 | 12 | 0 |
| `scripts/calculators.py` | code | 7258 | 155 | — | 0 | 0 |
| `scripts/check_skill.py` | code | 10343 | 217 | — | 0 | 0 |
| `scripts/test_calculators.py` | code | 7880 | 150 | — | 0 | 0 |
| `scripts/test_check_skill.py` | code | 1884 | 71 | — | 0 | 0 |

## Knowledge and ownership findings

**The corpus is already a graph.** It does not need a graph product before it can become useful. Its 448 explicit file relationships and complete Markdown reachability are a sound migration baseline. A link count does not establish the meaning, usefulness or completeness of a relation.

**The pilot files mix independently selectable questions.** Program combines demand, temporal resources, area accounting, adjacency, access, floor allocation and bounded-change reasoning. Composition combines site response, organizing ideas, mass/void, section-led form, facade order, stylistic translation, material expression and three integrated studies. Performance combines light, acoustics/air, enclosure continuity, degradation, support/services, inclusive/emergency journeys and two integrated studies. The [section map](migration-map.md#pilot-section-map) preserves their actual boundaries and child methods.

**Not every overlap is duplication.** Demand asks how many concurrent settings are needed; room fit asks whether objects, actions and routes fit. Composition's occupied facade bay is different from Documentation's consistency of an issued elevation. Material expression, exposure mechanisms, generic replacement, and a complete maintenance journey answer different questions. Consolidation must preserve these distinctions rather than flatten them into one generic checklist.

**Shared owners already exist.** `planning-and-section` owns general room/clear-area fit; `envelope-and-assemblies` owns control functions and generic compatibility/removal; `program-and-space` owns area accounting and access closure; `computational-design` owns consistent option comparison. Existing specialized timber, stair, housing and core methods contain causal knowledge that a general pointer cannot replace. The design makes these owners more directly addressable.

**Sources are large but intentionally separate from runtime methods.** `sources.md` combines upstream line-range provenance, library identity/read extents, adaptation decisions, historical notes and object evidence. Its 147,609 bytes are a maintenance-load problem, not evidence that every design task must read it. Splitting by source ownership and consolidating repeated pins is preferable to removing its evidence.

**The checker embeds the current flat layout.** `REFERENCES` in `scripts/check_skill.py` requires named flat files. Any later accepted migration must update those expectations atomically with moved methods. The checker also scans every Markdown file, requires Contents for long references and validates local fragments; future paths in these design documents are therefore code literals, not broken active links.

**Migration has cross-boundary backlinks inside the skill.** The three pilots receive links from 20, 11 and 19 distinct other files respectively. These include `references/normative/ru/applicability.md`. A later link-only rewrite there is necessary to preserve navigation; it must not change legal facts, source selections or normative record text. A+B changes none of those files.

## Coverage and depth priorities

This is a bounded knowledge assessment, not a certification of an agent or a complete audit of architectural practice. `Local method` means substantive local mechanisms/procedures are present for the stated question. `Partial` marks missing breadth or unproved predictive depth. `Source-only` is not a usable design method. Nonpilot conclusions below use the observed content structure and existing coverage/source records; future depth increments must read and test their selected methods fully.

| Area and current owner | Established local content | Status and next useful depth work |
| --- | --- | --- |
| Demand and shared resources — `program-and-space` | Conflicting briefs, occupancy timelines, staff/equipment overlap, changeover/storage and physical capacity example | Local method, deeply read. Add variations where temporal feasibility and spatial fit disagree; preserve operating demand versus statutory population |
| Areas, room and floor fit — `program-and-space`, `planning-and-section`, `dwelling-fit` | Once-only ledger, unfinished/finished boundaries, actual action envelopes, family/compact case data | Local methods; generality beyond selected cases is partial. Test irregular rooms, simultaneous door/furniture use, residual space and uncertainty |
| Routes and closure — `program-and-space`, `spatial-composition` | Actor-specific journeys, complete closure boundaries, path through/beside/into occupied space | Local methods. Deepen coupled everyday/service/emergency states rather than repeat generic accessibility advice |
| Urban/site — `quarter-and-public-space`, `site-and-context` | Open-space hierarchy, addresses, ground ledger, phases, season/section and local edge/arrival | Bounded methods; transport, landscape planting, rights and survey conclusions are not established by this inventory |
| Composition — `composition-and-style` | Seven organizing families, massing operations, section strategies, occupied bays, character levers and tectonic expression | Local methods, deeply read. Deepen proportion/order/sequence with genuine alternative mechanisms and critique, not style-name lists |
| Style and precedent — three style profiles, transfer method, eight cases | Declared historical/directional scope, source-observation limits, changed-brief transfer | Partial world/history/region coverage. Additional traditions need their own evidence; no assumption of comprehensive style competence |
| Light and environmental operation — `performance-and-coordination`, `environmental-operating-modes` | Sun/sky/view/privacy distinctions, shading geometry, coexisting controls and failure states | Local causal methods; annual illuminance/glare/thermal prediction is not provided by current geometry calculators |
| Acoustics and air interfaces — `performance-and-coordination` | Source/path/receiver, flanking paths, natural/mechanical/mixed operation and spatial reservations | Local architectural method, deeply read. Quantitative design claims need their actual methods and inputs; expand coupled cases before implying performance |
| Support and enclosure — `frame-and-core`, `roof-and-span`, `wall-floor-and-opening`, `envelope-and-assemblies` | Support/topology, openings, core continuity, roof water, control layers and junctions | Local bounded methods; broader material/system breadth remains partial. Deepen mechanisms with coherent junction and failure tests |
| Material-specific knowledge — `timber-and-joints` and exposure methods | Timber grain/movement, bearing/joint access, wetting/drying; other materials have selected exposure reasoning | Timber is relatively developed; equivalent-depth steel, concrete, masonry, glazing and finish methods are not established by the current map |
| Existing buildings — `existing-building-adaptation` | Conditional survey evidence, retain/repair/replace, old/new substrates and occupied works | Local methods; specialist heritage diagnosis, concealed hazards and structural condition cannot be inferred from the examples |
| Typologies — `building-use-families`, housing methods | Housing, learning clusters, libraries, short stay and mixed operators | Partial typology breadth. Hospitals, specialized labs, industrial processes and all age/hospitality subtypes have no demonstrated full local method |
| Lifecycle — `operation-and-lifecycle` | Whole maintenance journeys, intervention states, takeoff and equivalent-function event comparison | Bounded methods; no universal price, service-life or carbon database. Add scenario changes without inserting unsupported defaults |
| Evidence, representation and completion — `computational-design`, `design-development`, `design-completion`, `visual-delivery` | Option eligibility, sensitivity, datums, physical correction, issue reconciliation, precision and inspection | Local methods. Validate transfer across a changed source/recipient rather than repeat a checklist |
| Normative catalogue | 64 structured discovery records and jurisdiction selection | Source navigation, not local full-text law or a compliance engine. Preserve separately; no substantive legal re-audit in A+B |

Depth priorities are decision-coupling priorities, not a claim that unlisted knowledge is forbidden. First deepen demand/room/routes and occupied light/noise/air; then composition/facade-to-junction reasoning, material-system breadth and actual typology gaps. Keep unsupported outcomes open instead of masking them with additional files.

## External sources and local autonomy

| Directory-based non-normative measurement | Result |
| --- | ---: |
| Textual external URL occurrences, excluding own repository | 322 |
| Parsed external Markdown-link occurrences, excluding own repository | 314 |
| Distinct complete external URLs | 253 |
| Distinct fragment-normalized external document URLs | 128 |
| GitHub document URLs in two upstream repositories | 75 |
| Other document/media URLs | 53 |
| Distinct hostnames among those 128 URLs | 29 |
| Direct PDF document URLs | 6 |

The eight-occurrence difference between textual and parsed links is an extraction distinction, not a source addition. The previous conversation's 322/128 result is reproducible using the textual convention. Counting only `.jpg/.webp` suffixes is not a complete media classification: an image-service endpoint without an image extension is still image evidence.

Seventy-five GitHub document URLs point into two pinned upstream collections. They can be represented by two canonical revision records plus exact per-file/section/line locators, but the underlying cited-document count must remain 75 in the audit until its coverage actually changes. Reducing clickable URL repetition is not equivalent to eliminating knowledge dependencies.

The bibliography also identifies books and course material by `Krankort224/Architecture` revision, catalog paths, titles, pages and hashes, without a URL for every document. Therefore 128 is not a count of all works that informed the skill. Twenty-nine hostnames are not 29 independent intellectual sources.

The three deeply read pilots explicitly supply operative local reasoning and treat source packs as provenance. No compulsory external rereading was found in those methods. An exhaustive claim that every non-normative method is independently sufficient has not been tested; Pass E must classify and exercise each selected method. Project-specific measurements, product properties and current law remain inputs rather than defects to conceal through local prose.

Consolidation candidates are repeated pinned upstream URLs, repeated source identities/read extents, and object evidence repeated between case and central ledger. Local-synthesis candidates are specific causal gaps discovered by task tests, not entire unreviewed books. Preserve licenses, original-source locators, rejected claims and unread status. Sources that establish attribution, observed historical fabric or an actual figure should remain available as evidence even when the explanatory method is local.

## Six PDF dispositions

These are findings about the retained records, not fresh inspection or link-availability verification of the original PDFs in this cycle. Exact URLs remain at their existing source owners; they are not duplicated here.

| Retained PDF | Current local use | Proposed disposition for Pass E |
| --- | --- | --- |
| Barbican Estate Map, City of London | Level, route and public/private relationships in the Barbican case | Keep one object-evidence record; localize the transferable relationship in authored prose. A map is not a current survey or route-right finding |
| Barbican guidelines Volume II, Residential Buildings | Selected residential organization and facade observations | Tag as site-specific heritage-management guidance outside the normative directory. Retain inspected locators, not general conservation law |
| Barbican guidelines Volume IV, Landscape | Selected outdoor-space and landscape relationships | Same semantic guidance flag; keep its distinct document identity and read extent |
| NOAA, General Solar Position Calculations | Formula/convention verification for the solar calculator | Keep the precise formula source and existing local calculation contract. This is technical provenance, not a reason for mandatory PDF reading on every calculation |
| CMN Villa Savoye visitor leaflet, April 2008, CUNY-hosted copy | Selected plan/route observations and explicitly rejected chronology statement | Mirror-hosting debt. Search for the issuer's equivalent in E; replace only after identity/coverage verification. Until then preserve the honest mirror status and bounded evidence; do not fabricate a primary URL or silently drop supported observations |
| Frank Lloyd Wright Trust, Organic Architecture | Selected principles and variation caveat | Keep one primary interpretive source record and local original synthesis; preserve that the recorded reading was text-based, not image/layout inspection |

The two Barbican guideline PDFs demonstrate why directory exclusion alone is not semantic exclusion of all regulatory or management material. A complete semantic reclassification of all 128 URLs has not been performed; do not publish a supposedly precise all-norms-excluded total by subtracting only those two.

## Verification and limitations

Executed against the pinned baseline:

```text
python3 scripts/check_skill.py
valid=true; operation_count=8; normative_record_count=64; errors=[]

python3 -m unittest discover -s scripts -p 'test_*.py'
Ran 23 tests; OK
```

The link/manifest scan was also executed, producing the counts above and no missing targets. All 67 files have explicit dispositions in [the migration map](migration-map.md#complete-file-disposition). All substantive pilot H2/H3 sections have named destinations or a stated parent-preservation rule. These are design-stage checks; no runtime migration, environmental simulation, engineering validation, source-PDF rereading, or local-only competence benchmark execution is claimed.

No new source scans, images, archives, temporary JSON inventories, logs or caches are included in the branch. The proposed design and executable acceptance scenarios are in [knowledge-design.md](knowledge-design.md). A+B changes only these three maintenance documents; its final handoff records the exact publication revision and branch-diff verification.

## Reproduce the inventory

Use an isolated checkout of the exact baseline, not the changed branch's expanded corpus. Set `BASELINE_SKILL` to its architecture directory. The following uses only the baseline checker and the Python standard library. It reproduces the file/graph/URL measurements; semantic coverage judgments still require reading.

```bash
python3 - "$BASELINE_SKILL" <<'PY'
import collections, importlib.util, json, posixpath, re, sys
from pathlib import Path
from urllib.parse import unquote, urlsplit
r = Path(sys.argv[1]).resolve()
spec = importlib.util.spec_from_file_location('baseline_check', r/'scripts/check_skill.py')
c = importlib.util.module_from_spec(spec)
spec.loader.exec_module(c)
paths = sorted(p for p in r.rglob('*') if p.is_file() and '__pycache__' not in p.parts and '.git' not in p.parts)
texts = {p.relative_to(r).as_posix(): p.read_text(encoding='utf-8') for p in paths}
edges, parsed, raw = [], [], []
for name, text in texts.items():
    if not name.endswith('.md'):
        continue
    prose = re.sub(r'(?ms)^```.*?^```\s*$', '', text)
    if not name.startswith('references/normative/'):
        raw.extend(re.findall(r'https?://[^\s<>"\x27)\]]+', prose))
    for target in c.LINK.findall(prose) + c.DEFINITION.findall(prose):
        u = urlsplit(target.strip('<>'))
        if u.scheme in ('http', 'https'):
            parsed.append((name, target))
        elif not u.scheme and not u.netloc:
            dest = posixpath.normpath(posixpath.join(posixpath.dirname(name), unquote(u.path))) if u.path else name
            edges.append((name, dest, unquote(u.fragment)))
g = collections.defaultdict(set)
for source, dest, fragment in edges:
    g[source].add(dest)
seen, queue = set(), ['SKILL.md']
while queue:
    node = queue.pop()
    if node not in seen:
        seen.add(node)
        queue.extend(g[node] - seen)
external = lambda u: not u.startswith('https://github.com/Krankort224/Skills/')
raw = [u for u in raw if external(u)]
links = [u for p, u in parsed if not p.startswith('references/normative/') and external(u)]
missing = [(a,b,f) for a,b,f in edges if b not in texts or (f and b.endswith('.md') and f not in c.anchors(texts[b]))]
print(json.dumps({
    'files': len(paths), 'markdown': sum(p.suffix == '.md' for p in paths),
    'bytes': sum(p.stat().st_size for p in paths), 'local_occurrences': len(edges),
    'file_edges': len({(a,b) for a,b,f in edges if a != b}),
    'missing': missing, 'unreachable_md': sorted(p for p in texts if p.endswith('.md') and p not in seen),
    'raw_external_occurrences': len(raw), 'parsed_external_occurrences': len(links),
    'exact_urls': len(set(raw)), 'document_urls': len({u.split('#')[0] for u in raw})
}, ensure_ascii=False, indent=2))
for p in paths:
    print(p.relative_to(r).as_posix(), p.stat().st_size, len(texts[p.relative_to(r).as_posix()].splitlines()))
PY
```
