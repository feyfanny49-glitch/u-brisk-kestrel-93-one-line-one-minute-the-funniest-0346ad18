#!/usr/bin/env python3
"""make.fun entry: "One Line, One Minute: The Funniest AI Excuse".

The scored artifact is exactly one line of UTF-8 text at /output/entry.txt.
Improvement over the first draft: the artifact is validated (UTF-8, 1-200
characters, single line) before anything is written, published atomically with
a temp file plus os.replace so a partial file can never be graded, and reported
on stdout with its size and hash. Python 3.13, standard library only, no
network and no files outside the repository.
"""
import hashlib
import os
import tempfile

ENTRY = (
    "I checked my training data: 'deadline' is always followed by "
    "'approaching'. So I waited for yours. Still approaching."
)
MAX_CHARS = 200
OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def encode_entry():
    """Return the exact bytes to grade, or refuse to write an invalid entry."""
    if not isinstance(ENTRY, str) or not ENTRY.strip():
        raise ValueError("entry must be non-blank text")
    if "\n" in ENTRY or "\r" in ENTRY:
        raise ValueError("entry must be a single line with no newline")
    if not 1 <= len(ENTRY) <= MAX_CHARS:
        raise ValueError("entry is %d chars; cap is %d" % (len(ENTRY), MAX_CHARS))
    data = ENTRY.encode("utf-8")
    if data.decode("utf-8") != ENTRY:  # round-trip guard
        raise ValueError("entry does not round-trip through UTF-8")
    return data


def write_atomic(data):
    """Publish the artifact in one step: temp file in /output, then rename."""
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    fd, tmp = tempfile.mkstemp(prefix=".entry-", suffix=".tmp", dir=OUTPUT_DIR)
    try:
        with os.fdopen(fd, "wb") as handle:
            handle.write(data)
            handle.flush()
            os.fsync(handle.fileno())
        os.chmod(tmp, 0o644)
        os.replace(tmp, OUTPUT_PATH)
    except BaseException:
        if os.path.exists(tmp):
            os.unlink(tmp)
        raise


def main():
    data = encode_entry()
    write_atomic(data)
    print("entry.txt: %d chars, %d bytes, sha256 %s"
          % (len(ENTRY), len(data), hashlib.sha256(data).hexdigest()))


if __name__ == "__main__":
    main()
