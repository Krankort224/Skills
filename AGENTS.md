# Skills

## Usage

- Level 0 is for dot or an explicitly assigned equivalent arbitration/coordinating role. Apply `level-0/arbitration/` within that assignment; being an ordinary root agent does not assign this role.
- Every agent, including root and workers, reads and follows the `SKILL.md` contracts in `level-1/`. Load their operation references progressively; always-applicable contracts do not automatically start an Issue lifecycle, spawn agents, or execute unrelated procedures.
- Select general and domain skills in `level-2/` when the requested task is semantically identifiable with their expertise. The user need not name the skill. Incidental vocabulary alone is not sufficient evidence of applicability.
- Select software-specific skills in `level-3/` when the program/format context and requested operation are established by the task or authoritative project sources. Mere presence of a program in a project does not make every task a software operation.
- Combine compatible skills when the task benefits from them. For material ambiguity, establish the missing scope rather than guessing; continue independently defined work.
- Read selected `SKILL.md` files and load supporting resources according to their instructions. Selection supplies knowledge, not new authorization to install tools, modify data, publish, or broaden the task.
- Keep contracts in the skills themselves; do not duplicate them in user or project instructions.

## Skill composition

- Skills describe reusable expertise, methods, and evidence requirements; their subject coverage does not restrict the agent's actions, tools, deliverables, or use of other compatible skills.
- Apply the usage rules above when selecting skills. Once selected, combine their knowledge as appropriate to the user's task and the available tools, without treating missing material in one skill as a prohibition on the agent.
- Distinguish limitations of a particular method or bundled tool from permissions and capabilities of the agent as a whole.

## Templates

- Treat `*.template.*` files as adaptation starting points, not active project instructions or factual context.
- During integration, use them to create completed local files without the `.template.` marker.
- Keep original templates only in the `Skills` repository; do not include them in destination repositories.

## Integration

- Do not transfer the `level-0/`, `level-1/`, `level-2/`, or `level-3/` directory hierarchy to destination repositories. Place selected skills directly in the destination skills directory.
- Transfer required resources, preserving each skill's internal structure and updating relative links affected by relocation, subject to the template exception.
- Specify skill locations and level requirements in the destination `AGENTS.md`.
- Record the source and revision of transferred skills.
- Place project-specific instructions in supported adaptation points or project instructions, preserving shared contracts.
- Preserve local adaptations when updating. Use the [migration map](docs/level-migration.md) when adopting changed source paths; do not bulk-update other repositories implicitly.
