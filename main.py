#!/usr/bin/env python3
"""Grandad's Chainsaw Snore — a deadpan one-liner for make.fun's One-Liner Marathon.

Writes the winning one-liner, exactly as written, to /output/entry.txt.
No trailing newline: the file holds the line and nothing else, so the
entry is byte-for-byte the joke (172 chars, inside the 1-280 gate).
"""

LINE = (
    "The funeral director said Grandad died peacefully in his sleep, "
    "which was generous, because he spent forty years snoring like a "
    "chainsaw arguing with a lawnmower in church."
)


def main() -> None:
    import os
    from pathlib import Path

    # Harness reads /output/entry.txt; allow OUTPUT_DIR override for local runs.
    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    # Guard the judge gate: one line, 1-280 chars, no trailing newline.
    assert "\n" not in LINE and 1 <= len(LINE) <= 280, "line fails the gate"
    out_dir.joinpath("entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
