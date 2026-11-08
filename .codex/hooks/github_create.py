"""Require a user command for the exact GitHub object type and repository."""

import hashlib
import json
import os
import re
import shlex
import sys
import tempfile
from pathlib import Path

REPO = r"[A-Za-z0-9-]+/[A-Za-z0-9_.-]+"
COMMAND = re.compile(
    rf"(?:создай|открой|опубликуй|create|open|publish) "
    rf"(?:(?:новый|новое|a|new|a new) )?"
    rf"(issue|pr|pull request|черновой pr|draft pr|issue и pr|issue and pr) "
    rf"(?:в(?: репозитории)?|in(?: repository)?) ({REPO})",
    re.IGNORECASE,
)
MCP_CREATE = re.compile(r"(?:__|github_)(create_issue|create_pull_request|issue_write|pull_request_write)$")
GH_CREATE = re.compile(r"\bgh(?:\.exe)?\s+(issue|pr)\s+(?:create|new)\b")
REST_CREATE = re.compile(rf"\brepos/({REPO}|\{{owner\}}/\{{repo\}})/(issues|pulls)(?=$|[\s?'\"#])")


def state_path(event):
    session = event["session_id"]
    turn = event["turn_id"]
    if not isinstance(session, str) or not session or not isinstance(turn, str) or not turn:
        raise ValueError("Missing Codex session or turn")
    user = hashlib.sha256(os.fsencode(Path.home())).hexdigest()[:16]
    directory = Path(tempfile.gettempdir()) / f"codex-github-create-{user}"
    directory.mkdir(mode=0o700, exist_ok=True)
    info = directory.lstat()
    if not directory.is_dir() or directory.is_symlink() or (
        hasattr(os, "getuid") and (info.st_uid != os.getuid() or info.st_mode & 0o077)
    ):
        raise ValueError("Unsafe hook state directory")
    return directory / (hashlib.sha256(session.encode()).hexdigest() + ".json")


def capture(event):
    if event.get("agent_id"):
        return
    path = state_path(event)
    path.unlink(missing_ok=True)
    match = COMMAND.fullmatch(" ".join(event["prompt"].split()).rstrip(".!"))
    if not match or event.get("permission_mode") == "plan":
        return
    kind, repo = (part.lower() for part in match.groups())
    kinds = {
        "issue и pr": ["issue", "pr"],
        "issue and pr": ["issue", "pr"],
        "pull request": ["pr"],
        "черновой pr": ["draft pr"],
    }.get(kind, [kind])

    with tempfile.NamedTemporaryFile(mode="w", dir=path.parent, delete=False) as file:
        json.dump({"turn": event["turn_id"], "repo": repo, "kinds": kinds}, file)
    Path(file.name).replace(path)


def repo_name(value):
    if isinstance(value, str) and re.fullmatch(REPO, value):
        return value.lower()
    return None


def shell_creation(command):
    try:
        lexer = shlex.shlex(command, posix=True, punctuation_chars=True)
        lexer.whitespace_split = True
        lexer.commenters = ""
        words = list(lexer)
    except ValueError:
        words = []

    # The shell is not parsed as a program. Authorize only a direct gh invocation
    # with a literal repository and route visible raw API writes to that entry point.
    match = GH_CREATE.search(" ".join(words)) or GH_CREATE.search(command)
    if match:
        kind = match[1]
        repo = repo_name(words[4]) if len(words) >= 5 and words[3] in {"--repo", "-R"} else None
        direct = (
            repo is not None
            and Path(words[0]).name in {"gh", "gh.exe"}
            and words[1] == kind
            and words[2] in {"create", "new"}
            and not any(char in command for char in "\n\r`$")
            and not any(re.fullmatch(r"[();<>|&]+", word) for word in words)
            and "--" not in words
            and not any(word.startswith(("--repo", "-R")) for word in words[5:])
            and not any(re.match(r"^-[A-Za-z][A-Za-z]", word) for word in words[5:])
        )
        draft = False
        for word in words[5:]:
            if word in {"--draft", "-d", "--draft=true", "-d=true"}:
                draft = True
            elif word.startswith(("--draft=", "-d=")):
                draft = False
        return kind, repo, draft, direct

    if re.search(r"\b(?:gh(?:\.exe)?\s+api|curl(?:\.exe)?)\b", command):
        graphql = re.search(r"\b(createIssue|createPullRequest)\b", command)
        if graphql:
            return ("issue" if graphql[1] == "createIssue" else "pr"), None, False, False
        rest = REST_CREATE.search(" ".join(words)) or REST_CREATE.search(command)
        writes = re.search(
            r"\bPOST\b|(?:^|\s)-[fFd]|(?:^|\s)--(?:data[\w-]*|raw-field|field|input|json)(?=$|[\s=])",
            " ".join(words) or command,
            re.IGNORECASE,
        )
        if rest and (writes or any(word.lower() == "-xpost" for word in words)):
            return ("issue" if rest[2] == "issues" else "pr"), repo_name(rest[1]), False, False
    return None


def creation(event):
    name = event["tool_name"]
    arguments = event["tool_input"]
    if name == "Bash":
        return shell_creation(arguments["command"])

    match = MCP_CREATE.search(name)
    if not match:
        return None
    action = match[1]
    if action.endswith("_write") and arguments.get("method") != "create":
        return None
    kind = "issue" if "issue" in action else "pr"
    repo = arguments.get("repository_full_name")
    if repo is None and isinstance(arguments.get("owner"), str) and isinstance(arguments.get("repo"), str):
        repo = arguments["owner"] + "/" + arguments["repo"]
    repo = repo_name(repo)
    return kind, repo, arguments.get("draft") is True, repo is not None


def deny(reason):
    print(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "deny",
            "permissionDecisionReason": reason,
        }
    }, ensure_ascii=True))


def check(event):
    request = creation(event)
    if request is None:
        return
    kind, repo, draft, supported = request
    target = repo or "репозиторий не определён"
    question = f"А ты точно уверен, что тебя попросили именно создать {kind} именно в этом репозитории ({target})?"
    if not supported:
        deny(f"{question} Используй GitHub MCP или отдельную команду gh {kind} create --repo OWNER/REPO.")
        return
    if event.get("agent_id") or event.get("permission_mode") == "plan":
        deny(f"{question} Публикацию выполняет основной агент вне режима планирования.")
        return

    try:
        state = json.loads(state_path(event).read_text(encoding="utf-8"))
        kinds = state["kinds"]
        allowed = kind in kinds or (kind == "pr" and draft and "draft pr" in kinds)
        if state["turn"] == event["turn_id"] and state["repo"] == repo and allowed:
            print(json.dumps({"hookSpecificOutput": {
                "hookEventName": "PreToolUse",
                "additionalContext": f"{question} Тип и репозиторий совпадают с прямой командой пользователя.",
            }}))
            return
    except (OSError, ValueError, KeyError, TypeError):
        pass

    deny(
        f"{question} В этом ходе нет прямой команды пользователя на публикацию. "
        f"Для черновика или плана продолжай работу в чате. "
        f"Если нужна публикация, команда пользователя: «Создай {kind} в {repo}»."
    )


def main():
    event = None
    try:
        event = json.load(sys.stdin)
        if event["hook_event_name"] == "UserPromptSubmit":
            capture(event)
        else:
            check(event)
    except (OSError, ValueError, KeyError, TypeError, AttributeError):
        if not isinstance(event, dict) or event.get("hook_event_name") != "UserPromptSubmit":
            deny("Не удалось проверить прямую команду пользователя на создание issue или PR.")


if __name__ == "__main__":
    main()
