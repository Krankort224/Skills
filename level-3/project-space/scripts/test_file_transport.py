"""Isolated Windows transport checks; no live store or business validation."""

import ctypes
import msvcrt
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
import uuid
from unittest.mock import patch

import file_transport as transport


class TransportTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="project-space-transport-")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)

    def test_immutable_publish_confirmation_and_collision(self):
        relative = Path("events") / transport.new_id() / f"{transport.new_id()}.json"
        original = '{"title":"Проверка"}'.encode("utf-8")
        self.assertEqual(transport.publish_immutable(self.root, relative, original), "published")
        self.assertEqual(transport.read_final(self.root, relative), original)
        self.assertEqual(transport.publish_immutable(self.root, relative, original), "confirmed")
        with self.assertRaises(FileExistsError):
            transport.publish_immutable(self.root, relative, b"different")
        self.assertEqual(transport.read_final(self.root, relative), original)
        self.assertEqual(list(self.root.rglob("*.tmp")), [])

    def test_uncertain_success_confirms_original_bytes(self):
        relative = Path("pending") / f"{transport.new_id()}.json"
        api = transport._kernel()

        class LostMoveResponse:
            def __getattr__(self, name):
                return getattr(api, name)

            def MoveFileExW(self, source, target, flags):
                if not api.MoveFileExW(source, target, flags):
                    raise ctypes.WinError(ctypes.get_last_error())
                ctypes.set_last_error(64)  # Network error reported after commit.
                return False

        with patch.object(transport, "_kernel", return_value=LostMoveResponse()):
            self.assertEqual(transport.publish_immutable(self.root, relative,
                             b"original prepared bytes"), "confirmed")
        self.assertEqual(transport.read_final(self.root, relative), b"original prepared bytes")

    def test_failed_flush_never_exposes_final(self):
        relative = Path("events") / f"{transport.new_id()}.json"
        with patch.object(transport.os, "fsync", side_effect=OSError("flush failed")):
            with self.assertRaises(OSError):
                transport.publish_immutable(self.root, relative, b"prepared bytes")
        self.assertIsNone(transport.read_final(self.root, relative))
        self.assertEqual(len(list(self.root.rglob("*.tmp"))), 1)

    def test_path_escape_and_non_file_are_rejected(self):
        for relative in ("../escape", str(self.root / "escape"), "name:stream"):
            with self.assertRaises(ValueError):
                transport.publish_immutable(self.root, relative, b"x")
        (self.root / "directory").mkdir()
        with self.assertRaises(ValueError):
            transport.read_final(self.root, "directory")

    def test_uuid_version_variant_and_uniqueness(self):
        values = [transport.new_id() for _ in range(200)]
        self.assertEqual(len(set(values)), 200)
        for value in values:
            parsed = uuid.UUID(value)
            self.assertEqual(parsed.version, 7)
            self.assertEqual(parsed.variant, uuid.RFC_4122)
            self.assertEqual(str(parsed), value)

    def test_persistent_lock_exclusion_release_and_contents(self):
        for kind in ("access", "topic", "operation"):
            relative = f"{kind}.lock"
            target = self.root / relative
            target.write_bytes(b"persistent contents")
            with transport.persistent_lock(self.root, relative, kind=kind):
                with self.assertRaises(TimeoutError):
                    with transport.persistent_lock(self.root, relative, kind=kind, timeout=0):
                        self.fail("second holder entered")
            self.assertEqual(target.read_bytes(), b"persistent contents")
            with transport.persistent_lock(self.root, relative, kind=kind, timeout=0):
                pass
            self.assertTrue(target.exists())

    def test_topic_lock_interoperates_with_windows_byte_range_lock(self):
        target = self.root / ".topic.lock"
        target.write_bytes(b"x")
        with target.open("r+b") as external:
            msvcrt.locking(external.fileno(), msvcrt.LK_NBLCK, 1)
            try:
                with self.assertRaises(TimeoutError):
                    with transport.persistent_lock(self.root, ".topic.lock", kind="topic", timeout=0):
                        self.fail("entered over external Windows byte-range lock")
            finally:
                external.seek(0)
                msvcrt.locking(external.fileno(), msvcrt.LK_UNLCK, 1)

    def test_process_crash_releases_both_lock_types(self):
        script = (
            "import file_transport as t, os, sys\n"
            "with t.persistent_lock(sys.argv[1], sys.argv[2], kind=sys.argv[3]):\n"
            "    os._exit(0)\n"
        )
        for kind in ("access", "topic"):
            result = subprocess.run([sys.executable, "-B", "-c", script, str(self.root),
                                     f"{kind}.lock", kind], cwd=Path(__file__).parent,
                                    capture_output=True, timeout=10)
            self.assertEqual(result.returncode, 0, result.stderr)
            with transport.persistent_lock(self.root, f"{kind}.lock", kind=kind, timeout=0):
                pass


if __name__ == "__main__":
    unittest.main()
