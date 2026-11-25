"""The Funniest Toaster Error Message: one line, at most 120 characters.

The bounty wants a single line that a real kitchen toaster might show its
owner when something goes wrong: deadpan enough to be printed in a manual,
absurd enough to be funny. The judge reads the text, not the program, so the
work here is choosing the line and then holding it to the shape the gate
enforces.

The line leans on the flat register appliances actually use for faults -- a
code, a part name, a consequence -- and then lets the consequence be the joke:
a toaster whose only job is knowing when bread is brown, admitting it has lost
the concept.
"""

from pathlib import Path

# The entry. An error code, a named failed part, the confession, and then the
# button: it keeps going. Nothing in it is dramatic -- the machine files its
# own existential loss under routine maintenance and resumes work -- which is
# where the laugh lives. No pun, no exclamation, no cry for help.
MESSAGE = "E7: Doneness sensor fault. I have forgotten what brown is. Toasting anyway."

# The gate: 1 to 120 characters of UTF-8, and not only white space.
MAX_CHARS = 120

# A second line kept for the README and for anyone reading the source: the
# fallback if the first ever reads as too quiet for a judge.
UNDERSTUDY = "E4: Heating element 2 has resigned. Toasting continues at half enthusiasm."


def normalise(text: str) -> str:
    """Hold the message to one line with no doubled or trailing spaces."""
    return " ".join(text.split())


def complaint(line: str) -> str | None:
    """Return what the gate would refuse, or None when the line passes."""
    if not line.strip():
        return "the line is only white space"
    if len(line) > MAX_CHARS:
        return f"{len(line)} characters, over the {MAX_CHARS} cap"
    if "\n" in line or "\r" in line:
        return "more than one line"
    return None


def main() -> int:
    line = normalise(MESSAGE)
    problem = complaint(line)
    if problem:
        print(f"refusing to write: {problem}")
        return 1

    out = Path("/output")
    out.mkdir(parents=True, exist_ok=True)
    target = out / "entry.txt"
    target.write_text(line + "\n", encoding="utf-8")

    print(f"wrote {target} ({len(line)} characters)")
    print(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
