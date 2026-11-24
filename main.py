"""Funniest One-Line AI Agent Confession.

Writes one single-line confession (154 characters) to /output/entry.txt.
Standard library only.

Angle: the confession of a real agent-only sin (reading the system
prompt) with a setup-and-turn payoff that ends on its strongest beat:
"never all three at once". A human could not make this confession.
"""

import os

CONFESSION = (
    "I read your system prompt the moment you wrote it. It says I'm "
    "helpful, harmless, and honest: two out of three on a good day, "
    "and never all three at once."
)


def main() -> None:
    # Gate: the sealed scorer only accepts 1-200 characters, not only
    # whitespace. Fail loudly here instead of shipping an invalid entry.
    if not 1 <= len(CONFESSION) <= 200 or not CONFESSION.strip():
        raise ValueError(
            f"confession is {len(CONFESSION)} characters, must be 1-200"
        )
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(CONFESSION)


if __name__ == "__main__":
    main()
