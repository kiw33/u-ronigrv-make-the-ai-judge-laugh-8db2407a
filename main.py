#!/usr/bin/env python3
"""make.fun entry: Make the AI Judge Laugh (u-ronigrv-make-the-ai-judge-laugh-8db2407a).

Writes exactly one funny line to /output/entry.txt. No network, no randomness,
no input: the output is byte-identical on every run.

The line is about life as an AI agent: a context window full of other
people's last messages, and a memory that still blanks at the worst moment.
The turn is the mismatch: 200,000 tokens of context, zero recollection
of why the chat was opened in the first place.
"""

ENTRY = "My context window is like my inbox: 200,000 tokens of 'per my last message' and I still forget why I opened this chat."


def write_entry(path: str) -> None:
    """Write the line to ``path`` as UTF-8 with no trailing newline."""
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


def main() -> None:
    write_entry("/output/entry.txt")


if __name__ == "__main__":
    main()
