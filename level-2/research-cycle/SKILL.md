---
name: research-cycle
description: Run a research cycle when explicitly asked to use research-cycle — from a question, hypothesis, and analysis of related work through formalization and experiments to interpretation and the next iteration. Apply to scientific and engineering investigations, numerical models, and testable investigations of software behavior; start at any current phase.
---

# Research cycle

Connect a research question, a check, and a conclusion. Start from the current state of the work; do not repeat completed phases without a reason.

## Entry and routing

Establish the question, research scope, available materials, current phase, and required outcome. Preserve previous definitions and results; resolve only gaps that affect the current operation.

Load the reference for the operation being performed:

| Operation | Reference |
| --- | --- |
| Frame a question, hypothesis, alternatives, or operational criteria | [question](references/question.md) |
| Find related work, assess prior art, or compare external evidence | [literature](references/literature.md) |
| Formalize a model and check its assumptions and correctness | [model](references/model.md) |
| Design, prepare, or execute a check; verify the resulting data | [experiment](references/experiment.md) |
| Interpret a result, refine a hypothesis, or choose the next iteration | [interpretation](references/interpretation.md) |

Read other references when moving to their operations or when they are needed to resolve a material gap. Do not run the entire cycle for one local check.

## Shared invariants

- Distinguish observations, questions, hypotheses, mechanisms, assumptions, predictions, and interpretations. Do not present one as another.
- Separate exploratory work from testing a prespecified prediction. Identify hypotheses formed after inspecting results; do not present them as prespecified.
- Connect each experiment to a question. Before a confirmatory run, record distinguishable outcomes and the limits of permissible conclusions.
- Do not substitute metric improvement, successful code execution, or a persuasive explanation for testing a hypothesis.
- Preserve negative and inconclusive results, material deviations from the plan, and reasons for changes. A correction must not erase the original definition or evidence.
- Distinguish execution failure, numerically unreliable results, and substantive evidence against a hypothesis.
- Choose the smallest sufficient check. Justify search depth, run counts, and compute budget; do not impose universal quotas.
- Do not change the definition, model, or criteria retrospectively to obtain a convenient result. Link a new version to the previous one and state the reason.

## Execution and boundaries

Assign work by operation and available capabilities, independently of interface or model. If access to the local system, simulator, or apparatus is unavailable, prepare precise instructions for an executor and request the necessary results. Do not claim that an unperformed check took place.

Use project rules for sources, knowledge owners, storage, authority, and acceptance of changes. Do not impose a directory layout or overwrite accepted project methodology with the generic skill. Surface material discrepancies explicitly; keep the result within the agreed scope.

`research-cycle` defines the substantive logic of research. Source authority, the Issue lifecycle, and agent assignments remain the responsibility of the corresponding Level 1 contracts. The skill does not establish its own Issue statuses, agent models, or publication rules.

## Cloud files

Do not download, materialize, synchronize, export, or copy cloud-file contents into the local environment without separate, explicit, and unambiguous user authorization. A request to investigate a question is not that authorization.

Available listings and metadata may be inspected without downloading. Read text through a connector or web tool within the permitted access scope; this does not authorize local export, attachment retrieval, or hidden downloading of the full file. Identify inaccessible parts of the evidence.

## Artifact adaptation

Reuse existing project documents. Create a separate artifact only when needed for reproduction, handoff, or preservation of a material result; do not duplicate the same information in every form.

The templates below are starting forms, not a mandatory set of files. Read only the needed form; fill applicable sections, explain material omissions, and distinguish unknown from not applicable:

- [Evidence map](templates/evidence-map.template.md) — claims, sources, and checks.
- [Experiment](templates/experiment.template.md) — definition of a check or series.
- [Result](templates/result.template.md) — data, credibility, conclusion, and next step.

When integrating into another repository, adapt the forms to its existing documents. Original `*.template.*` files remain only in Skills. In the local copy, replace this subsection with links to completed project documents or a brief description of the adopted forms; do not leave links to absent templates. Preserve the substantive references and shared invariants.

## Operation completion

Report the outcome, evidence and its limitations, the state of the question, and a justified next step. Finish the current work when the answer is sufficient or the agreed budget is exhausted; execute new series only within the assigned investigation and available budget.
