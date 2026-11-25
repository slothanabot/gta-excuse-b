"""make.fun entry: The Excuse That Almost Works.

One line a gamer texts the boss to skip work on GTA 6 launch week.

Judge brief (tired manager who has heard every excuse twice):
the winning excuse is a real, specific, boring workplace detail rather
than a wild story; funny on its own logic; reads like a text sent in a
hurry (one line, plain words, no setup, no explanation, no signature);
and finds an angle the obvious excuses miss (no dead grandmother, flat
tyre, or sudden fever). A long excuse sounds rehearsed, and a rehearsed
one is already a confession.

This entry's angle: the dentist's office moved the appointment to
Thursday on its own, "without asking" -- the gamer is almost apologetic
about a calendar that betrayed them. No illness, no disaster, just a
boring appointment that landed on launch week and "can't be changed".
Lowercase, no signature, sent in a hurry. The "without asking" is the
laugh: the excuse's own logic is that the calendar did it to them, not
that they chose it.

Gate (RULES.txt): /output/entry.txt must be UTF-8 text of 1-140
characters, not only whitespace, a single line, at most 20 words.
"""

ENTRY = "sorry dentist rang, they moved my appointment to thursday without asking, cant change it, wont be in tomorrow"

OUTPUT_PATH = "/output/entry.txt"


def verify(text):
    """Enforce the gate: 1-140 chars, <=20 words, non-blank, single line."""
    if not text or not text.strip():
        raise ValueError("entry is blank")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if len(text) > 140:
        raise ValueError("entry exceeds 140 characters")
    words = text.split()
    if len(words) > 20:
        raise ValueError("entry exceeds 20 words")
    return len(text), len(words)


def write_entry(path=OUTPUT_PATH):
    """Verify the entry and write it (plus trailing newline) to path."""
    chars, words = verify(ENTRY)
    import os

    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    return chars, words


def main():
    chars, words = write_entry()
    print(f"{chars} characters, {words} words")
    print(ENTRY)


if __name__ == "__main__":
    main()
