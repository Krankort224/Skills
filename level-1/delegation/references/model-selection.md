# Select a model route

Use after establishing that a model child provides a useful contribution. Model suitability, runtime capability and permission are distinct.

## Assess the subtask

Fix the inputs, expected result, dependencies and verification. Identify the needed tools, source access, modality and context capacity. Separate hard requirements, including independence and resource limits, from preferences. Describe the reasoning the child needs.

| Demand | Evidence in the assignment |
| --- | --- |
| Precise execution | The input and rule are settled, valid outputs are easy to check, and any useful contribution still justifies a child. Consider direct work or deterministic code first. |
| Bounded judgment | A local diagnosis, implementation or synthesis needs interpretation across several steps. Its scope, evidence and verification are defined. |
| Substantial judgment | Conflicting evidence, coupled choices or consequential unknowns require designing discriminating checks or weighing material tradeoffs. |

Use these distinctions to characterize the work. A research, implementation, review or coordination assignment can fall anywhere in the range. Size, title and tree depth alone supply no ranking. Model identity and model-specific `reasoning_effort` are separate from the task's reasoning demand. Use only settings supported by the specific model and live interface. Choose a proportionate setting when selectable and known.

## Apply the authorized policy and live controls

1. **Resolve policy.** Use a model map only when explicitly selected for the task or by a standing project instruction. Apply an authorized task override according to its scope and preserve all still-applicable restrictions. A vendor name, configured alias, runtime adapter or partial availability does not activate or change the selected policy.
2. **Establish eligible routes.** Intersect currently available routes with actual user/project limits and assignment permissions, including any map restriction. Check selectable identifiers or configured aliases, fixed or inherited defaults, required context modes, provider or model fallbacks and any supported runtime readback. The successful invocation of an unrelated task or a provider's catalog does not establish availability for this child.
3. **Choose within the intersection.** Follow the selected map's fit preferences and mandatory boundaries. A preferred route may yield to an adequate allowed alternative. A hard route, required capability, independence condition or budget must be satisfied before dependent work proceeds. Without a selected map, choose an allowed route whose adequacy has support, such as relevant documented capability or comparable checked work. Use the adequate fixed or inherited route if permitted and it is the only supported route. Report material unknowns rather than guessing fitness, latency or cost from an identifier.
4. **Handle an unavailable or incompatible choice.** Try a supported context mode if it can preserve all requirements, or use an allowed adequate fallback, reframe the work or perform it directly where authorized and capable. Check any automatic fallback against the same boundaries. If no route satisfies a hard requirement or budget, report the exact gap. An unavailable option grants no model, provider, profile, override or budget change.

Capture the selection rationale and recommendation, the requested model/option if selectable, the host's routing decision including inheritance or fallback, and independently observable effective model when relevant. Use available native metadata or traces and say what they establish. A preference, accepted call, saved session label or route alias alone cannot identify a provider's effective model. Report the exact selection or readback limitation if the host fixes the route or hides identity.

## Supply another map

A task or project can select its own map through an accessible pinned source or an explicit policy statement. Record its scope, eligible model identifiers or route aliases and their known correspondence, task-fit preferences and hard limits, any permitted exceptions, evidence and fallback. No central registry or adapter is required. This selection policy can be applied through any authorized harness. Hermes's `model_map` backend is a runtime routing control, with its own aliases and configuration.
