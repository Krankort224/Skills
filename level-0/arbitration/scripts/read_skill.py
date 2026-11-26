#!/usr/bin/env python3
"""Read UTF-8 material from an immutable Krankort224/Skills commit."""

import argparse
import base64
import hashlib
from http.client import HTTPException
import json
import os
from pathlib import Path
import re
import subprocess
import sys
from urllib.parse import quote
from urllib.request import Request, urlopen


REPOSITORY = "Krankort224/Skills"
CANONICAL = f"https://github.com/{REPOSITORY}.git"
DEFAULT_PATH = "level-0/arbitration/SKILL.md"
TIMEOUT = 10


def revision(value):
    if not re.fullmatch(r"[0-9a-fA-F]{40}", value):
        raise argparse.ArgumentTypeError("expected a full 40-character Git commit SHA")
    return value.lower()


def repository_path(value):
    if (any(part in {"", ".", ".."} for part in value.split("/"))
            or any(c in value for c in "\\:")
            or any(ord(c) < 32 or ord(c) == 127 for c in value)):
        raise argparse.ArgumentTypeError("expected a file path relative to the Skills repository")
    return value


def command(*args, cwd=None):
    result = subprocess.run(args, cwd=cwd, stdin=subprocess.DEVNULL, capture_output=True,
                            timeout=TIMEOUT, check=True,
                            env={**os.environ, "GIT_TERMINAL_PROMPT": "0",
                                 "GIT_NO_LAZY_FETCH": "1", "GH_PROMPT_DISABLED": "1"})
    return result.stdout


def github(endpoint, accept):
    """Try the authenticated GitHub CLI, then the public HTTPS API."""
    try:
        return command("gh", "api", "--hostname", "github.com", "-H", f"Accept: {accept}",
                       endpoint), "github-cli"
    except (OSError, subprocess.SubprocessError):
        request = Request("https://api.github.com/" + endpoint,
                          headers={"Accept": accept, "User-Agent": "Skills-read-skill",
                                   "Cache-Control": "no-cache"})
        with urlopen(request, timeout=TIMEOUT) as response:
            return response.read(), "github-https"


def live_main():
    try:
        row = command("git", "ls-remote", "--exit-code", CANONICAL, "refs/heads/main")
        sha, ref = row.decode("ascii").strip().split("\t")
        if ref == "refs/heads/main" and re.fullmatch(r"[0-9a-f]{40}", sha):
            return sha, "git-ls-remote"
    except (OSError, subprocess.SubprocessError, ValueError):
        pass
    data, source = github(f"repos/{REPOSITORY}/git/ref/heads/main",
                          "application/vnd.github+json")
    ref = json.loads(data)
    if (not isinstance(ref, dict) or ref.get("ref") != "refs/heads/main"
            or not isinstance(ref.get("object"), dict) or ref["object"].get("type") != "commit"
            or not re.fullmatch(r"[0-9a-f]{40}", str(ref["object"].get("sha")))):
        raise ValueError("GitHub returned an invalid main ref")
    return ref["object"]["sha"], source


def content_at(repo, sha, path):
    if repo is not None:
        try:
            prefix = ("git", "--no-replace-objects", "-C", str(repo))
            if command(*prefix, "cat-file", "-t", sha).strip() == b"commit":
                return command(*prefix, "cat-file", "blob", f"{sha}:{path}"), "git-object"
        except (OSError, subprocess.SubprocessError):
            pass
    body, source = github(f"repos/{REPOSITORY}/contents/{quote(path, safe='/')}?ref={sha}",
                          "application/vnd.github.object+json")
    file = json.loads(body)
    if (not isinstance(file, dict) or file.get("type") != "file" or file.get("path") != path
            or not re.fullmatch(r"[0-9a-f]{40}", str(file.get("sha")))):
        raise ValueError(f"GitHub did not return the requested file at {sha}")
    if file.get("encoding") == "base64" and isinstance(file.get("content"), str):
        data = base64.b64decode("".join(file["content"].splitlines()), validate=True)
    else:
        data, source = github(f"repos/{REPOSITORY}/git/blobs/{file['sha']}",
                              "application/vnd.github.raw+json")
    if hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest() != file["sha"]:
        raise ValueError(f"GitHub file content does not match its blob at {sha}")
    return data, source


def cached_content(file, receipt_file, path, sha):
    receipt = json.loads(receipt_file.read_bytes())
    if (not isinstance(receipt, dict) or receipt.get("repository") != REPOSITORY
            or receipt.get("path") != path or receipt.get("revision") != sha):
        raise ValueError("saved receipt does not identify the requested repository, path and revision")
    data = file.read_bytes()
    if hashlib.sha256(data).hexdigest() != receipt.get("sha256"):
        raise ValueError("cached file differs from the digest in its saved receipt")
    return data, "receipt-checked-file"


def read(args):
    if args.connector_main:
        current, main_source = args.connector_main, "caller-github-connector"
    else:
        try:
            current, main_source = live_main()
        except (OSError, HTTPException, ValueError) as exc:
            if not args.offline_known:
                raise ValueError(f"cannot resolve Skills main ({exc}); use a fresh connector "
                                 "observation, or --offline-known if all routes are unavailable") from exc
            current, main_source = None, "unavailable"
    sha = args.revision or current or args.offline_known
    if current is None and args.cached_file is not None:
        data, source = cached_content(args.cached_file, args.receipt, args.path, sha)
    else:
        data, source = content_at(args.repo, sha, args.path)
    data.decode("utf-8")
    receipt = {"repository": REPOSITORY, "path": args.path, "revision": sha,
               "selection": "explicit" if args.revision else "main" if current else "offline-known",
               "live_main": current, "main_source": main_source,
               "freshness": "connector-reported" if args.connector_main else "live" if current else "unverified",
               "source": source, "sha256": hashlib.sha256(data).hexdigest()}
    return data, receipt


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", nargs="?", default=DEFAULT_PATH, type=repository_path,
                        help="repository-relative UTF-8 file (default: arbitration/SKILL.md)")
    # A flattened installation need not carry a Git checkout.
    bundle = Path(__file__).resolve().parent
    checkout = next((p for p in bundle.parents if (p / ".git").exists()), None)
    parser.add_argument("--repo", type=Path, default=checkout, help="optional Skills Git object store")
    parser.add_argument("--revision", type=revision, help="explicitly requested historical commit")
    parser.add_argument("--offline-known", type=revision,
                        help="known Skills revision if all authorized GitHub routes are unavailable")
    parser.add_argument("--connector-main", type=revision,
                        help="fresh canonical main SHA just observed by the caller via GitHub connector")
    parser.add_argument("--cached-file", type=Path,
                        help="offline file from a prior successful read; requires its trusted --receipt")
    parser.add_argument("--receipt", type=Path, help="JSON receipt for the offline --cached-file")
    args = parser.parse_args(argv)
    if (args.cached_file is None) != (args.receipt is None):
        parser.error("--cached-file and --receipt must be supplied together")
    try:
        data, receipt = read(args)
        sys.stdout.buffer.write(data)
        sys.stdout.buffer.flush()
        print(json.dumps(receipt), file=sys.stderr)
    except (OSError, HTTPException, ValueError) as exc:
        print(f"read_skill: {args.path}: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
