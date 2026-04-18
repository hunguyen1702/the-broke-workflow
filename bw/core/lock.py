"""Atomic file-based locking for task claims."""

import os
import time
from pathlib import Path
from typing import Optional

from bw.core.paths import find_bw_root


def _lock_path(bw: Optional[Path] = None) -> Path:
    root = bw or find_bw_root()
    return root / ".lock"


def acquire(lock_id: str, owner: str, wait: bool = True, timeout: float = 5.0) -> bool:
    """Attempt to acquire an exclusive lock.

    Returns True if acquired, False if already locked.
    If wait=True, retries until timeout.
    """
    lock_file = _lock_path()
    lock_file.parent.mkdir(parents=True, exist_ok=True)
    deadline = time.monotonic() + timeout

    while True:
        try:
            fd = os.open(str(lock_file), os.O_CREAT | os.O_EXCL | os.O_WRONLY)
            os.close(fd)
            # Write owner + timestamp
            lock_file.write_text(f"{owner}\n{time.time()}\n")
            return True
        except FileExistsError:
            if not wait:
                return False
            if time.monotonic() >= deadline:
                return False
            time.sleep(0.05)


def release(lock_id: str) -> bool:
    """Release a lock if held by any owner."""
    lock_file = _lock_path()
    if lock_file.exists():
        lock_file.unlink()
    return True


def read_lock() -> tuple[str, float]:
    """Read current lock owner and timestamp. Returns (owner, timestamp)."""
    lock_file = _lock_path()
    if not lock_file.exists():
        return "", 0.0
    lines = lock_file.read_text().splitlines()
    if len(lines) >= 2:
        return lines[0], float(lines[1])
    return "", 0.0
