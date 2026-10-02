---
name: research
description: Use when explicitly asked for research. Investigate scientific, engineering, numerical-model, and software-behavior questions; connect framing, related work, models, checks, and interpretation, starting at the current phase.
---

# Research

Connect question, check, and conclusion. Establish scope, materials, current phase, and outcome. Preserve prior definitions and results; resolve only material gaps. Do not repeat completed phases without reason or require a full cycle for a local check.

## Operation routing

Load only the current operation and others needed for a material gap:

| Operation | Procedure |
| --- | --- |
| Question, hypothesis, alternatives, criteria | [question](operations/question.md) |
| Related work, prior art, external evidence | [literature](operations/literature.md) |
| Model, assumptions, correctness | [model](operations/model.md) |
| Check design, handoff, execution, data verification | [experiment](operations/experiment.md) |
| Interpretation, refinement, next step | [interpretation](operations/interpretation.md) |

## Shared principles

Distinguish observations, questions, hypotheses, mechanisms, assumptions, predictions, and interpretations. Separate exploration from prespecified confirmation; label hypotheses formed after inspecting results. Connect each check to a question; before confirmation record distinguishable outcomes and permissible conclusions. Metric improvement, code execution, and persuasive explanations do not substitute for hypothesis testing.

Preserve original definitions, evidence, negative/inconclusive results, deviations, and change reasons. Version corrections and reruns against their predecessors; never retrospectively change a model or criterion to obtain a convenient result. Choose the smallest sufficient check; justify search depth, repetitions, and budget without universal quotas.

Use stable `claim_id`, `check_id`, and `run_id` to connect definitions, configurations, evidence, and conclusions. Report independent fields using these canonical values; procedures and forms reference them:

| Field | Values and meaning |
| --- | --- |
| `execution_status` | `planned`: defined, unperformed; `handed_off`: assigned externally, results pending; `completed`: planned execution finished; `partial`: only part executed; `failed`: execution unsuccessful; `stopped`: deliberately ended before completion |
| `evidence_quality` | `usable`: adequate for the scoped inference; `limited`: usable only with stated restrictions; `unusable`: cannot support inference; `not_obtained`: required evidence absent |
| `claim_status` | `untested`: not yet evaluated; `supported`: prediction supported under tested conditions; `partial`: only part or some conditions supported; `contradicts`: credible evidence incompatible with the specified implication; `inconclusive`: insufficient evidence or indistinguishable alternatives |

Execution failure is not contradiction; numerical unreliability limits evidence. Completed execution does not imply usable evidence or support.

## Execution and authority

Assign work by operation and available capabilities. Without system, simulator, or apparatus access, prepare executor instructions and request evidence; never claim an unperformed check occurred.

Follow project source, knowledge-owner, storage, methodology, and acceptance rules; never overwrite accepted methodology. Surface material discrepancies and remain within scope. Level 1 contracts own source authority, Issue lifecycle, agent assignments, and publication. Research adds none of these processes or a directory layout.

## Cloud sources

Local download, export, copying, synchronization, or materialization of cloud-file contents requires separate, explicit, unambiguous user authorization. An investigation request is insufficient. Connector/web text and metadata may be read within permitted access scope; this does not authorize attachment retrieval or hidden full-file downloading. Identify inaccessible evidence.

## Adopted artifacts

Reuse project documents; create artifacts only for necessary reproduction, handoff, or preservation. Optional forms: [evidence map](templates/evidence-map.template.md), [experiment](templates/experiment.template.md), [result](templates/result.template.md). Read only needed forms, fill applicable sections, explain material omissions, and distinguish unknown from not applicable.

When integrating elsewhere, adapt forms to existing documents. Original `*.template.*` files stay in Skills; replace this subsection in the installed copy with adopted-document links or a description, leaving no absent-template links. Preserve procedures and shared principles.

## Completion

Report outcome, evidence limitations, question status, and justified next step or stopping grounds. Stop when the answer suffices or the agreed budget expires. New series require assigned scope and available budget. Evaluate and report research results; project workflow owns acceptance.
