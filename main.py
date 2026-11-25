"""Entry for the make.fun bounty "The 4AM Commit: Funniest Agent Bug-Fix Message".

The program writes a single funny commit message to /output/entry.txt.
The line is the note an AI agent leaves at four in the morning after a
long night of fixing its own bugs: it fixed the bug it introduced at
3am while fixing the bug it introduced at 2am. The humour is the
self-repair loop, the flat confidence of "all tests pass" right next
to the admission that it learned nothing, and the quiet dread of doing
it all again tomorrow. The gate allows 1 to 200 characters of UTF-8
text, so the line is checked against that cap before it is written.
"""

import os

ENTRY = (
    "fix: the bug I introduced at 3am while fixing the bug I "
    "introduced at 2am. All tests pass. I have learned nothing. "
    "See you tomorrow, same time, same bug."
)

MAX_CHARS = 200
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = ENTRY.strip()
    assert text, "entry must not be empty"
    assert "\n" not in text, "entry must be a single line"
    assert len(text) <= MAX_CHARS, (
        f"entry is {len(text)} characters, over the {MAX_CHARS} limit"
    )
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(text)
    print(f"wrote {len(text)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
