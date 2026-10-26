"""Windows file mechanics only; callers own schema, access, replay and pending checks.

Import this module from a terminal script. It has no command-line interface and
never initializes a store, edits mutable configuration or resolves a conflict.
"""

from contextlib import contextmanager
import ctypes
from ctypes import wintypes
import hashlib
import os
from pathlib import Path
import secrets
import stat
import time
import uuid


def new_id():
    """Canonical UUIDv7 with random remaining bits, matching the current core."""
    millis = time.time_ns() // 1_000_000
    if not 0 <= millis < 1 << 48:
        raise ValueError("clock outside UUIDv7 range")
    value = bytearray(secrets.token_bytes(16))
    value[:6] = millis.to_bytes(6, "big")
    value[6] = (value[6] & 15) | 0x70
    value[8] = (value[8] & 63) | 0x80
    return str(uuid.UUID(bytes=bytes(value)))


def sha256(data):
    return hashlib.sha256(data).hexdigest()


def _kernel():
    if os.name != "nt":
        raise OSError("Windows file transport required")
    api = ctypes.WinDLL("kernel32", use_last_error=True)
    api.CreateFileW.argtypes = [wintypes.LPCWSTR, wintypes.DWORD, wintypes.DWORD,
                               wintypes.LPVOID, wintypes.DWORD, wintypes.DWORD,
                               wintypes.HANDLE]
    api.CreateFileW.restype = wintypes.HANDLE
    api.CloseHandle.argtypes = [wintypes.HANDLE]
    api.CloseHandle.restype = wintypes.BOOL
    api.GetFileType.argtypes = [wintypes.HANDLE]
    api.GetFileType.restype = wintypes.DWORD
    api.GetFileInformationByHandleEx.argtypes = [wintypes.HANDLE, ctypes.c_int,
                                                wintypes.LPVOID, wintypes.DWORD]
    api.GetFileInformationByHandleEx.restype = wintypes.BOOL
    api.LockFileEx.argtypes = [wintypes.HANDLE, wintypes.DWORD, wintypes.DWORD,
                              wintypes.DWORD, wintypes.DWORD, wintypes.LPVOID]
    api.LockFileEx.restype = wintypes.BOOL
    api.MoveFileExW.argtypes = [wintypes.LPCWSTR, wintypes.LPCWSTR, wintypes.DWORD]
    api.MoveFileExW.restype = wintypes.BOOL
    return api


def _checked_metadata(path):
    info = path.lstat()
    if stat.S_ISLNK(info.st_mode) or getattr(info, "st_file_attributes", 0) & 0x400:
        raise ValueError("reparse/symlink path rejected")
    return info


def checked_path(root, relative, *, create_parents=False):
    """Check an existing trusted root and each descendant; never resolve aliases.

    The caller verifies store identity and authority. As in the trusted-client
    store contract, ACLs must prevent hostile concurrent directory substitution.
    """
    root, relative = Path(root), Path(relative)
    if not root.is_absolute() or relative.drive or relative.is_absolute():
        raise ValueError("absolute root and relative descendant required")
    if not relative.parts or any(p in (".", "..") for p in relative.parts):
        raise ValueError("empty/traversing relative path rejected")
    for part in relative.parts:
        if (any(c in part for c in ':*?"<>|') or part.endswith((".", " "))
                or any(ord(c) < 32 for c in part)):
            raise ValueError("invalid path component")
    if not stat.S_ISDIR(_checked_metadata(root).st_mode):
        raise ValueError("root is not an existing directory")
    current = root
    for part in relative.parts[:-1]:
        current /= part
        if create_parents:
            try:
                current.mkdir()
            except FileExistsError:
                pass
        if not stat.S_ISDIR(_checked_metadata(current).st_mode):
            raise ValueError("parent is not a directory")
    result = current / relative.name
    try:
        if not stat.S_ISREG(_checked_metadata(result).st_mode):
            raise ValueError("target is not a regular file")
    except FileNotFoundError:
        pass
    return result


def _open_regular(api, path, access, sharing, disposition):
    handle = api.CreateFileW(str(path), access, sharing, None, disposition,
                             0x00200000, None)  # FILE_FLAG_OPEN_REPARSE_POINT
    if handle == wintypes.HANDLE(-1).value:
        raise ctypes.WinError(ctypes.get_last_error())
    try:
        attrs = (wintypes.DWORD * 2)()  # FILE_ATTRIBUTE_TAG_INFO
        if not api.GetFileInformationByHandleEx(handle, 9, attrs, ctypes.sizeof(attrs)):
            raise ctypes.WinError(ctypes.get_last_error())
        if api.GetFileType(handle) != 1 or attrs[0] & (0x400 | 0x10):
            raise ValueError("opened handle is not a regular non-reparse disk file")
        return handle
    except BaseException:
        api.CloseHandle(handle)
        raise


def read_final(root, relative):
    """Read bytes through a checked Windows handle; missing means None."""
    api = _kernel()
    import msvcrt
    try:
        path = checked_path(root, relative)
        handle = _open_regular(api, path, 0x80000000, 7, 3)  # read, share all, existing
    except OSError as error:
        if error.winerror in (2, 3):
            return None
        raise
    try:
        fd = msvcrt.open_osfhandle(handle, os.O_RDONLY | os.O_BINARY)
    except BaseException:
        api.CloseHandle(handle)
        raise
    with os.fdopen(fd, "rb") as stream:
        return stream.read()


class _Overlapped(ctypes.Structure):
    _fields_ = [("Internal", ctypes.c_size_t), ("InternalHigh", ctypes.c_size_t),
                ("Offset", wintypes.DWORD), ("OffsetHigh", wintypes.DWORD),
                ("hEvent", wintypes.HANDLE)]


@contextmanager
def persistent_lock(root, relative, *, kind, timeout=3.0):
    """kind='access': share-none; kind='topic'/'operation': whole-file LockFileEx.

    Keep the handle through validation and publication. Closing releases the
    lock; the persistent file is never truncated or deleted.
    """
    if kind not in ("access", "topic", "operation") or not 0 <= timeout <= 60:
        raise ValueError("invalid lock kind/timeout")
    api = _kernel()
    path = checked_path(root, relative, create_parents=True)
    deadline = time.monotonic() + timeout
    while True:
        try:
            handle = _open_regular(api, path, 0xC0000000, 0 if kind == "access" else 7, 4)
            break  # read/write, OPEN_ALWAYS without truncation
        except OSError as error:
            if error.winerror not in (32, 33):
                raise
            if time.monotonic() >= deadline:
                raise TimeoutError("persistent lock busy") from error
            time.sleep(0.01)
    try:
        if kind != "access":
            overlapped = _Overlapped()
            while not api.LockFileEx(handle, 3, 0, 0xFFFFFFFF, 0xFFFFFFFF,
                                     ctypes.byref(overlapped)):
                error = ctypes.WinError(ctypes.get_last_error())
                if error.winerror != 33:
                    raise error
                if time.monotonic() >= deadline:
                    raise TimeoutError("persistent lock busy") from error
                time.sleep(0.01)
        yield
    finally:
        api.CloseHandle(handle)


def publish_immutable(root, relative, data):
    """Publish already validated bytes; return 'published' or 'confirmed'.

    Caller must persist pending first and hold the correct lock(s). This function
    neither checks business authorization nor clears pending. Exact same final
    bytes confirm an earlier attempt; different final bytes are never replaced.
    """
    if not isinstance(data, bytes):
        raise TypeError("prepared bytes required")
    api = _kernel()
    target = checked_path(root, relative, create_parents=True)
    before = read_final(root, relative)
    if before is not None:
        if before != data:
            raise FileExistsError("immutable final byte collision")
        return "confirmed"
    temp = target.with_name(f".{target.stem}.{new_id()}.tmp")
    # 'xb' is create-new; no live final is opened for writing.
    with temp.open("xb") as stream:
        stream.write(data)
        stream.flush()
        os.fsync(stream.fileno())
    moved = api.MoveFileExW(str(temp), str(target), 8)  # WRITE_THROUGH, no REPLACE
    move_error = None if moved else ctypes.WinError(ctypes.get_last_error())
    final = read_final(root, relative)
    if final == data:
        # A successful rename consumed temp. Preserve a remaining temp on an
        # ambiguous attempt rather than unlink a possibly changed path.
        return "published" if moved else "confirmed"
    if final is not None:
        raise FileExistsError("immutable final byte collision")
    if move_error is not None:
        raise move_error
    raise OSError("publication outcome unknown; preserve pending and original IDs")
