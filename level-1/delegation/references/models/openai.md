# OpenAI subagent model map

Use only when the task or a standing project instruction explicitly selects this map. An authorized task override can change the applicable selection within its granted scope. The map applies to subagents and preserves the user's selected main agent.

Use the [portable selection criteria](../model-selection.md) to assess the reasoning needs of a useful child. This table owns the concrete correspondences. The identifiers are orchestration choices whose availability must be established in the live interface. The task-fit distinctions are a selection policy. They carry no comparative benchmark, cost or availability claim. [Issue #18](https://github.com/Krankort224/Skills/issues/18) records the existing high-tier substitution.

| Tier | Preferred model | Task fit |
| --- | --- | --- |
| Light | `gpt-6-luna` | Precise repeatable tasks with an unambiguous transformation and simple verification, should a child be useful. |
| Medium | `gpt-6.1-terra` | Bounded multi-step work with interpretation and local choices, such as a scoped fix or synthesis. |
| High | `gpt-6.2-sol` | Substantial uncertainty, conflicting evidence, coupled decisions or complex diagnosis and design. |

While this map applies, the eligible set is its members intersected with current usable options and all applicable restrictions. If the preferred member is unavailable, choose an adequate member of that intersection, replan or name the gap. A partial set does not switch policy or admit an advertised model outside the map. An off-map fixed or inherited route requires an authorized exception or a different authorized policy. Check automatic fallback against the same restrictions.

Use supported model-specific effort settings only when the interface exposes them, and prefer the minimum reliable setting. The tiers grant no context mode, reasoning setting, spend, descendant or access rights.

To update the map under an authorized policy decision, record the exact identifier scope, task-fit evidence or decision, relevant controls and fallback implications. Recheck affected routes and a representative assignment. Other projects can supply their own [maps](../model-selection.md#supply-another-map) without modifying this one.
