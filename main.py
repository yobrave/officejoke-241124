"""Gate runner for the office-joke sprint entry.

Pulls the one-line submission beside this file, cleans it down to a
single non-blank line, holds it against the 200 character ceiling,
then plants the exact bytes in the grader's output folder and prints
a one-line verdict.
"""
from pathlib import Path
import json
import os

LIMIT = 200
TAG = "ofc3-office-sprint-0822"
SUBMISSION = Path(__file__).resolve().parent / "entry.txt"


def sweep(raw):
    body = raw.replace("\r", "").rstrip("\n")
    if "\n" in body:
        body = next(x for x in body.split("\n") if x.strip())
    return body


def main():
    text = sweep(SUBMISSION.read_text(encoding="utf-8"))
    if text.strip() == "":
        raise ValueError("submission holds only white space")
    if len(text) > LIMIT:
        raise ValueError("submission spans %d chars over the %d cap" % (len(text), LIMIT))
    if "MAKEFUN_OUTPUT_DIR" in os.environ:
        base = Path(os.environ["MAKEFUN_OUTPUT_DIR"])
    else:
        base = Path("output")
    base.mkdir(parents=True, exist_ok=True)
    dest = base / "entry.txt"
    with open(dest, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    if dest.read_text(encoding="utf-8") != text:
        raise ValueError("written file disagrees with cleaned line")
    print(json.dumps({"pass": True, "chars": len(text), "limit": LIMIT, "tag": TAG}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
