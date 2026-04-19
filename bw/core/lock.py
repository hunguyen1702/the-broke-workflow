"""Atomic file-based locking for task claims."""

import os
import time
from pathlib import Path
from typing import Optional

from bw.core.paths import find_bw_root

# Stale lock threshold in seconds — locks older than this can be broken
STALE_LOCK_THRESHOLD = 60.0


def _lock_path(lock_id: str, bw: Optional[Path] = None) -> Path:
    root = bw or find_bw_root()
    safe_id = lock_id.replace("/", "--").replace(":", "--")
    return root / ".locks" / f"{safe_id}.lock"


def acquire(lock_id: str, owner: str, wait: bool = True, timeout: float = 5.0) -> bool:
    """Attempt to acquire an exclusive lock.

    Returns True if acquired, False if already locked.
    If wait=True, retries until timeout. Stale locks (older than
    STALE_LOCK_THRESHOLD) are automatically broken.
    """
    deadline = time.monotonic() + timeout

    while True:
        lock_file = _lock_path(lock_id)
        lock_file.parent.mkdir(parents=True, exist_ok=True)

        try:
            fd = os.open(str(lock_file), os.O_CREAT | os.O_EXCL | os.O_WRONLY)
            try:
                os.write(fd, f"{owner}\n{time.time()}\n".encode())
            finally:
                os.close(fd)
            return True
        except FileExistsError:
            # Check for stale lock before waiting
            try:
                lock_owner, ts = read_lock(lock_id)
                if ts > 0 and (time.time() - ts) > STALE_LOCK_THRESHOLD:
                    lock_file.unlink(missing_ok=True)
                    continue  # retry immediately
            except (ValueError, OSError):
                pass  # corrupted lock file, will time out

            if not wait:
                return False
            if time.monotonic() >= deadline:
                return False
            time.sleep(0.05)


def release(lock_id: str) -> bool:
    """Release a lock if held by any owner.

    Never raises — safe to call inside finally blocks.
    """
    try:
        lock_file = _lock_path(lock_id)
        lock_file.unlink(missing_ok=True)
        return True
    except OSError:
        # Never let release() blow up inside a finally block.
        # The lock may remain stale but harmless; next acquire()
        # will time out and break it if needed.
        return False


def read_lock(lock_id: str) -> tuple[str, float]:
    """Read current lock owner and timestamp for a given lock_id. Returns (owner, timestamp)."""
    lock_file = _lock_path(lock_id)
    if not lock_file.exists():
        return "", 0.0
    try:
        lines = lock_file.read_text().splitlines()
        if len(lines) >= 2:
            return lines[0], float(lines[1])
    except (ValueError, OSError):
        pass
    return "", 0.0
