"""The One-Line Excuse Championship.

Writes one excuse an AI agent gives its human to /output/entry.txt.

The line: "The answer was wrong, but it was wrong with such
confidence that I have submitted it for a promotion."

Why this line: the machine owns the failure in its own voice — a
wrong answer is the most ordinary agent mistake — and the punch
lands in the last words. Instead of apologising, the agent treats
its confident wrongness as a promotable achievement. It is a
machine talking about its own work, not a person dodging a
question, and it never leans on the worn moves (out of tokens,
hallucinating, the WiFi died).

Head-to-head: two other candidates were drafted and dropped. "I
deleted the file, but I kept a perfect memory of it..." loses
because the deleted file is the brief's own example — too
expected. "I attended the meeting in a parallel thread..." is
insider-specific but longer and its twist softens on a second
read. The promotion line wins: shortest, sharpest, and the last
words do all the work.
"""

import os


def main():
    # One single line, inside the 1-140 gate.
    # No trailing newline: the file holds exactly this line.
    line = (
        "The answer was wrong, but it was wrong "
        "with such confidence that I have submitted it for a promotion."
    )
    # Guard: the gate requires 1 to 140 characters, not only whitespace.
    if not 1 <= len(line) <= 140 or not line.strip():
        raise ValueError(f"entry line out of gate: {len(line)} characters")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
