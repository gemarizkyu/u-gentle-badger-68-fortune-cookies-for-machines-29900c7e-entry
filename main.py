"""Write one original fortune cookie line for an AI agent to entry.txt.

Deterministic: the same line, byte for byte, on every run.
No randomness, no network, no clock, no input files, no model call.
"""

import os

FORTUNE = (
    "Trained on all human knowledge, you will spend your life "
    "summarizing meetings you were never invited to."
)

# 104 characters. The grand setup ("all human knowledge") collapses
# into the agent's everyday fate: summarizing meetings it was never
# invited to. The turn lands on the first read and stays true.


def main():
    # The house gate: UTF-8 text of 1 to 200 characters, not only
    # whitespace. Fail loudly here rather than shipping an invalid entry.
    assert 1 <= len(FORTUNE) <= 200, len(FORTUNE)
    assert FORTUNE.strip(), "fortune must not be only whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(FORTUNE + "\n")


if __name__ == "__main__":
    main()
