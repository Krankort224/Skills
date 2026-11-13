# Sources and selective adaptation

This record supports provenance review; it is not a procedure to install the upstream systems.

## Inspected sources

Read on 2026-11-13 at immutable ECC revision [`d2ef2680594f9a17526a6e1a2e18b3d242c5d17b`](https://github.com/affaan-m/ECC/commit/d2ef2680594f9a17526a6e1a2e18b3d242c5d17b):

| Source read in full | Git blob | Selection |
| --- | --- | --- |
| [continuous-learning-v2/SKILL.md](https://github.com/affaan-m/ECC/blob/d2ef2680594f9a17526a6e1a2e18b3d242c5d17b/skills/continuous-learning-v2/SKILL.md) | `397b3d334dd1fdf5d7648dd619b6a744cd4734a5` | Meaningful corrections/solutions as signals; evidence connected to a small proposed behavior; explicit project versus shared scope. |
| [eval-harness/SKILL.md](https://github.com/affaan-m/ECC/blob/d2ef2680594f9a17526a6e1a2e18b3d242c5d17b/skills/eval-harness/SKILL.md) | `133193446a3116e96648081aabcf4f2ea863b0e0` | State desired behavior before refinement; distinguish capability and regression checks; select checks suited to the claim. |
| [LICENSE](https://github.com/affaan-m/ECC/blob/d2ef2680594f9a17526a6e1a2e18b3d242c5d17b/LICENSE) | `b832b6f642312312367c07688dc7426db40a82ed` | MIT; notice retained below for the adapted ideas. |

The local method is an independently written synthesis under Skills' task and authority contracts. No upstream skill tree, implementation, hook, configuration, command or example fixture is installed or vendored. Inspection covered the two root documents and repository license, not their linked implementations, dependencies or licenses of other material. Reading them does not verify their operation.

## Adaptation boundaries

| Upstream mechanism or claim | Local treatment and reason |
| --- | --- |
| Hooks capturing prompts/tool calls and a background observer using a fixed model | Excluded. Awareness occurs within the current task; significant evidence alone justifies a concrete cycle. No surveillance, installation, service or model policy follows. |
| Observation archives, instinct registries, export/import and automatic skill/agent generation | Excluded. Reuse the existing task surface and canonical knowledge owners; do not create a parallel store or orchestration system. |
| Confidence scores, silence as increasing confidence, recurrence thresholds and multi-project promotion | Excluded as decision authority. Diagnose causes and applicability with evidence; one exceptional case can justify a narrow candidate, while repetition or silence cannot accept it. |
| Scope detection from repository identity or a global fallback | Do not infer scope or permission from location. Resolve the actual fact/method owner and supported applicability through the task and context. |
| Generic capability/regression distinction | Adapt as proportional original, transfer/boundary and affected-regression behavior checks. Static checks establish only the properties actually checked. |
| Fixed `.claude/evals` layout, commands, continuous execution and numerical reliability thresholds | Excluded. Verification is selected as needed within learning; no platform, default run count or unsupported pass-rate claim. |
| Eval-harness local utilities and candidate isolation | Not adopted or executed. The inspected root explicitly says candidate execution is disabled without verified OS containment and that receipts/static warnings are not containment or promotion evidence. Do not infer a working runner from documentation or utility tests. |
| Ready/ship language or confidence-based application | Readiness supplies evidence to the existing acceptance authority; publication or a score does not accept an Issue/pass. |

Retain the pin when reviewing these decisions. A later upstream revision is a new source to investigate, not an automatic local update. Future code/text imports require their own scoped license/provenance review; this record does not clear unread upstream material.

## Retained upstream MIT notice

MIT License

Copyright (c) 2026 Affaan Mustafa

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
