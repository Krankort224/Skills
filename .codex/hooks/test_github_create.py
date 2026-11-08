"""Run with python3 -B .codex/hooks/test_github_create.py."""

import contextlib
import io
import json
import re
import tempfile
from pathlib import Path
from unittest.mock import patch

from github_create import capture, check

CONFIG = json.loads(Path(__file__).resolve().parents[1].joinpath("hooks.json").read_text())
MATCHER = CONFIG["hooks"]["PreToolUse"][0]["matcher"]
EVENT = {"session_id": "hook-test", "turn_id": "turn-1", "permission_mode": "default"}
REPO = "Krankort224/Skills"
ISSUE = "mcp__codex_apps__github_create_issue"
PR = "mcp__codex_apps__github_create_pull_request"


def decision(tool, arguments, **overrides):
    assert re.search(MATCHER, tool), tool
    output = io.StringIO()
    with contextlib.redirect_stdout(output):
        check({**EVENT, **overrides, "tool_name": tool, "tool_input": arguments})
    return json.loads(output.getvalue()).get("hookSpecificOutput", {}) if output.getvalue() else {}


def denied(tool, arguments, **overrides):
    result = decision(tool, arguments, **overrides)
    assert result["permissionDecision"] == "deny", (tool, arguments, result)
    assert "А ты точно уверен" in result["permissionDecisionReason"]
    return result["permissionDecisionReason"]


def allowed(tool, arguments):
    assert decision(tool, arguments).get("permissionDecision") != "deny", (tool, arguments)


with tempfile.TemporaryDirectory() as test_directory, patch("github_create.tempfile.gettempdir", return_value=test_directory):
    issue = {"repository_full_name": REPO}
    pr = {"repository_full_name": REPO}
    denied(ISSUE, issue)
    for prompt in (
        "Подготовь черновик issue",
        "Оформи план PR",
        "Пока не создавай issue",
        f"Если всё хорошо, создай issue в {REPO}",
        f"«Создай issue в {REPO}»",
        f"Создай issue в {REPO}, но пока только черновик",
        "Делай",
    ):
        capture({**EVENT, "prompt": prompt})
        denied(ISSUE, issue)
        denied(PR, pr)

    capture({**EVENT, "prompt": f"Создай issue в {REPO}."})
    assert "А ты точно уверен" in decision(ISSUE, issue)["additionalContext"]
    allowed(ISSUE, issue)
    allowed("mcp__github__issue_write", {"method": "create", "owner": "Krankort224", "repo": "Skills"})
    denied(PR, pr)
    assert "krankort224/other" in denied(ISSUE, {"repository_full_name": "Krankort224/Other"})
    denied(ISSUE, issue, turn_id="turn-2")
    denied(ISSUE, issue, session_id="other-session")
    denied(ISSUE, issue, agent_id="child")
    denied(ISSUE, issue, permission_mode="plan")
    allowed("Bash", {"command": f"gh issue create --repo {REPO} --body-file body.md"})
    for command in (
        "gh issue create --title 'No target'",
        f"gh issue create --repo {REPO} -Rwrong/target",
        f"gh issue create --repo {REPO} -wRwrong/target",
        f"gh issue create --repo {REPO}; gh pr create --repo {REPO}",
        f"gh api -XPOST repos/{REPO}/issues",
        f"gh api repos/{REPO}/issues -ftitle=Bug",
        f"curl -XPOST https://api.github.com/repos/{REPO}/pulls",
        "gh api graphql -f 'query=mutation { createPullRequest(input: {}) { clientMutationId } }'",
    ):
        denied("Bash", {"command": command})

    capture({**EVENT, "prompt": f"Создай черновой PR в {REPO}"})
    denied(PR, pr)
    allowed(PR, {**pr, "draft": True})
    allowed("Bash", {"command": f"gh pr create --repo {REPO} --draft"})
    denied("Bash", {"command": f"gh pr create --repo {REPO} --draft --draft=false"})
    capture({**EVENT, "prompt": f"Создай issue и PR в {REPO}"})
    allowed(ISSUE, issue)
    allowed(PR, pr)
    capture({**EVENT, "prompt": "Стоп. Только подготовь черновик."})
    denied(ISSUE, issue)
    denied(PR, pr)
    allowed("Bash", {"command": "gh pr list"})
    allowed("Bash", {"command": f"gh api repos/{REPO}/issues"})
    allowed("mcp__github__issue_write", {"method": "update"})

print("GitHub creation hook checks passed")
