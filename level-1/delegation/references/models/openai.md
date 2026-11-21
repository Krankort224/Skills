# OpenAI subagent selection pool

## Scope and evidence

Use this pool when the task selects it. It is also the default pool for the [profiled OpenAI collaboration interface](../runtimes/openai-collaboration.md) unless applicable instructions select another policy. Its applicability does not require every listed model to be available: missing entries narrow the allowed intersection and invoke the fallback below; they do not silently switch the task to another pool. These are orchestration identifiers, not a claim about public API model names or availability on every OpenAI host. The user's main-agent choice is outside this subagent pool.

This reference is the sole owner of the concrete mappings formerly in the skill root. Task-fit criteria are the repository's chosen routing policy, not benchmark results. The user authorized the high-tier substitution in [Issue #18](https://github.com/Krankort224/Skills/issues/18) on 2026-11-22: use `gpt-6.2-sol`. Light and medium retain their existing assignments. Verify current availability at dispatch; the table itself grants no access.

## Preferred mappings

| Tier | Model identifier | Task fit |
| --- | --- | --- |
| light | gpt-6-luna | Precise, repeatable work with an unambiguous transformation and simple verification: extraction, classification, mechanical edits, checks against explicit rules. |
| medium | gpt-6.1-terra | Bounded multi-step work requiring interpretation and local implementation choices: scoped code fixes, source synthesis, document preparation, visual or interface tasks. |
| high | gpt-6.2-sol | Substantial uncertainty, coupled changes, conflicting evidence, architecture, complex diagnosis, or coordination requiring that judgment. |

Select by uncertainty, interdependence and required judgment, not task length, role name or tree depth. Research, execution and verification may use any suitable tier. Tiers describe this policy's task fit; they are not reasoning-effort values, cross-provider equivalences, spawning rights or permanent labels for an agent.

## Selection, inheritance and fallback

For work using this pool, select subagents from its entries intersected with the current tool's choices and applicable allowlists, unless an explicit user/task instruction authorizes a different model. Do not silently widen this selected pool merely because the host advertises more models. Other authorized pools/runtimes follow their own selection policy rather than importing this one by default.

Prevent incompatible inheritance: verify whether the launch inherits a model or accepts an override, and whether the resulting model satisfies the selected pool and task. If an override conflicts with history inheritance, use task-specific context through a supported route. If the effective model cannot be established where the restriction matters, resolve that gap before dependent execution.

Use minimum reliable effort from settings supported by the selected model and interface. Do not manufacture an effort parameter or treat another provider's identically named setting as equivalent.

If the preferred model is unavailable, choose another permitted pool member that meets the task requirements, replan, or let the parent execute where capable and allowed. A missing access/input problem requires its own remedy. If no adequate route exists, report that exact limitation; do not install a provider or change credentials/configuration to bypass it.

Spawning rights, depth, concurrency and write ownership are assigned by [planning](../../operations/plan.md), independently of these tiers. Preserve tighter task/runtime restrictions.

## Updating this reference

For an authorized change, record the exact identifier/alias scope, supported task-fit evidence or explicit policy decision, relevant limits/settings, fallback implications and source/date. Recheck consumers and a representative affected assignment. Do not add a new model's ranking from its name alone, or duplicate the registry in the root, README or project map. Model additions within the same method do not require changing the shared operations.
