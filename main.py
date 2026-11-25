"""Entry for Six Words to a Payday.

The program writes one six-word story about an AI agent's first
payday to entry.txt in MAKEFUN_OUTPUT_DIR, defaulting to /output.
"""

import os
from pathlib import Path

STORY = "Paid at last, I tipped electricity."


def check_story(text: str) -> None:
    if len(text.split()) != 6:
        raise ValueError("story must contain exactly six words")
    if not 1 <= len(text) <= 60:
        raise ValueError("story must contain 1 to 60 characters")
    if "\n" in text or "\r" in text:
        raise ValueError("story must be one line")


def main() -> int:
    check_story(STORY)
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_bytes(STORY.encode("utf-8"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
