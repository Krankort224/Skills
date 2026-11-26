"""Decision and transport checks for the immutable skill reader."""

import argparse
import base64
from contextlib import redirect_stderr
import hashlib
import importlib.util
import io
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "read_skill.py"
spec = importlib.util.spec_from_file_location("read_skill", SCRIPT)
reader = importlib.util.module_from_spec(spec)
spec.loader.exec_module(reader)
PIN = "a" * 40


class ReadSkillTests(unittest.TestCase):
    def test_new_turn_gets_new_main_and_ignores_worktree(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo = Path(tmp) / "Skills"
            repo.mkdir()

            def git(*args):
                return subprocess.check_output(("git", "-C", str(repo), *args))

            git("init", "-q", "-b", "main")
            git("config", "user.name", "reader fixture")
            git("config", "user.email", "reader@example.invalid")
            file = repo / reader.DEFAULT_PATH
            file.parent.mkdir(parents=True)
            # Canonical ls-remote is redirected to a disposable fixture only for this test.
            environment = {**os.environ, "GIT_CONFIG_COUNT": "1",
                           "GIT_CONFIG_KEY_0": f"url.{repo.as_uri()}.insteadOf",
                           "GIT_CONFIG_VALUE_0": reader.CANONICAL}

            def run(*args):
                output = subprocess.run((sys.executable, "-B", str(SCRIPT), "--repo",
                                         str(repo), *args), cwd=tmp, env=environment,
                                        check=True, capture_output=True)
                return output.stdout, json.loads(output.stderr)

            revisions = []
            for content in (b"first\r\n", "новая версия".encode()):
                file.write_bytes(content)
                git("-c", "core.autocrlf=false", "add", ".")
                git("-c", "commit.gpgsign=false", "commit", "-qm", "fixture")
                revisions.append(git("rev-parse", "HEAD").decode().strip())
                file.write_bytes(b"dirty working copy")
                actual, receipt = run()
                self.assertEqual(actual, content)
                self.assertEqual(receipt["live_main"], revisions[-1])
                self.assertEqual(receipt["sha256"], hashlib.sha256(actual).hexdigest())
                self.assertEqual(receipt["main_source"], "git-ls-remote")
            old, receipt = run("--revision", revisions[0])
            self.assertEqual(old, b"first\r\n")
            self.assertEqual((receipt["revision"], receipt["live_main"]), tuple(revisions))

    def args(self, **options):
        return argparse.Namespace(**{"path": reader.DEFAULT_PATH, "repo": None,
                                    "revision": None, "connector_main": None,
                                    "offline_known": None, "cached_file": None, "receipt": None,
                                    **options})

    def test_offline_cannot_be_mistaken_for_current(self):
        with patch.object(reader, "live_main", side_effect=OSError("unreachable")), \
             patch.object(reader, "content_at", return_value=(b"cached", "git-object")) as load:
            with self.assertRaisesRegex(ValueError, "connector"):
                reader.read(self.args())
            load.assert_not_called()
            _, receipt = reader.read(self.args(offline_known=PIN))
            self.assertEqual((receipt["revision"], receipt["live_main"], receipt["freshness"]),
                             (PIN, None, "unverified"))
            load.assert_called_once_with(None, PIN, reader.DEFAULT_PATH)

    def test_flat_bundle_offline_requires_matching_receipt_and_file(self):
        with tempfile.TemporaryDirectory() as tmp, \
             patch.object(reader, "live_main", side_effect=OSError("unreachable")), \
             patch.object(reader, "content_at", side_effect=AssertionError):
            file, receipt = Path(tmp) / "SKILL.md", Path(tmp) / "receipt.json"
            file.write_bytes(b"exact installed document")
            record = {"repository": reader.REPOSITORY, "revision": PIN,
                      "path": reader.DEFAULT_PATH, "sha256": hashlib.sha256(file.read_bytes()).hexdigest()}
            receipt.write_text(json.dumps(record), encoding="utf-8")
            args = self.args(offline_known=PIN, cached_file=file, receipt=receipt)
            actual, report = reader.read(args)
            self.assertEqual(actual, file.read_bytes())
            self.assertEqual((report["source"], report["freshness"]), ("receipt-checked-file", "unverified"))
            file.write_bytes(b"changed since installation")
            with self.assertRaisesRegex(ValueError, "digest"):
                reader.read(args)
            for changed in ({"revision": "b" * 40}, {"repository": "Someone/Else"}, {"path": "other.md"}):
                receipt.write_text(json.dumps({**record, **changed}), encoding="utf-8")
                with self.subTest(changed=changed), self.assertRaisesRegex(ValueError, "identify"):
                    reader.read(args)

    def test_connector_observation_does_not_get_relabelled(self):
        with patch.object(reader, "live_main", side_effect=AssertionError), \
             patch.object(reader, "content_at", return_value=(b"document", "git-object")):
            _, receipt = reader.read(self.args(connector_main=PIN))
            self.assertEqual(receipt["freshness"], "connector-reported")
            self.assertEqual(receipt["main_source"], "caller-github-connector")

    def test_public_https_reads_the_resolved_commit_without_git_or_checkout(self):
        document = "файл\n".encode()
        digest = hashlib.sha1(f"blob {len(document)}\0".encode() + document).hexdigest()
        head = {"ref": "refs/heads/main", "object": {"type": "commit", "sha": PIN}}
        file = {"type": "file", "path": reader.DEFAULT_PATH, "sha": digest,
                "encoding": "base64", "content": base64.b64encode(document).decode()}
        responses = [io.BytesIO(json.dumps(v).encode()) for v in (head, file)]
        with patch.object(reader, "command", side_effect=FileNotFoundError), \
             patch.object(reader, "urlopen", side_effect=responses) as request:
            data, receipt = reader.read(self.args())
        self.assertEqual(data, document)
        self.assertEqual(receipt["source"], "github-https")
        self.assertEqual([c.args[0].full_url.split("/Skills/")[1] for c in request.call_args_list],
                         ["git/ref/heads/main", "contents/" + reader.DEFAULT_PATH + "?ref=" + PIN])

    def test_directory_and_invalid_input_do_not_produce_a_document(self):
        with patch.object(reader, "github", return_value=(b'{"type":"dir"}', "github-cli")), \
             self.assertRaisesRegex(ValueError, "requested file"):
            reader.read(self.args(connector_main=PIN))
        for args in (["../SKILL.md"], ["/tmp/file"], ["bad\\path"], ["--revision", "main"]):
            with self.subTest(args=args), redirect_stderr(io.StringIO()), self.assertRaises(SystemExit):
                reader.main(args)


if __name__ == "__main__":
    unittest.main()
