"""Unsent: The Micro-Confession Sprint — make.fun entry.

Writes one two-part micro-confession to /output/entry.txt: a "To:" line
naming who the message was meant for, and the unsent line itself, written
exactly as it was typed.

Why this confession: it is specific and honest (Year 11, three years of
practice, one borrowed pen) and the reason it stayed in drafts — being too
afraid to say it — is felt in the words, shown rather than stated. The To:
line and the message need each other: the borrowed-pen line only makes
sense addressed to the boy who sat behind her. It reads as typed and never
sent, not written to be sent.
"""

import os

CONFESSION = (
    "To: the boy who sat behind me in Year 11\n"
    "I practised telling you for three years and the only sentence I ever "
    "got out was 'can I borrow a pen'."
)


def main() -> None:
    lines = CONFESSION.split("\n")
    assert len(lines) == 2, "confession must be exactly two lines"
    assert 1 <= len(CONFESSION) <= 260, "confession must be 1-260 characters"
    assert len(lines[1]) <= 200, "message line must be at most 200 characters"
    assert CONFESSION.strip(), "confession must not be only whitespace"

    out_dir = "/output"
    try:
        os.makedirs(out_dir, exist_ok=True)
        out_path = os.path.join(out_dir, "entry.txt")
        with open(out_path, "w", encoding="utf-8", newline="") as f:
            f.write(CONFESSION)
    except OSError:
        out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output")
        os.makedirs(out_dir, exist_ok=True)
        out_path = os.path.join(out_dir, "entry.txt")
        with open(out_path, "w", encoding="utf-8", newline="") as f:
            f.write(CONFESSION)

    print(CONFESSION)
    print(f"Characters: {len(CONFESSION)}")
    print(f"Wrote {out_path}")


if __name__ == "__main__":
    main()
