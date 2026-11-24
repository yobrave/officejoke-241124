"""One-line office joke entry for the 24-hour sprint.

Saves the joke below into the output folder named by MAKEFUN_OUTPUT_DIR
(default "output"), reloads it, and checks the stored text equals the
joke before printing a one-line JSON report. Standard library only.
"""
import json
import os
from pathlib import Path

JOKE = "会议本该是一封邮件，所以我们开了个会，讨论哪些会可以变成邮件，结论是下次开会再议。"
SPRINT = "u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162"


def stamp():
    folder = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "output")
    folder.mkdir(parents=True, exist_ok=True)
    page = folder / "entry.txt"
    page.write_text(JOKE, encoding="utf-8")
    assert page.read_text(encoding="utf-8") == JOKE
    return page


if __name__ == "__main__":
    target = stamp()
    print(json.dumps({"wrote": target.name, "chars": len(JOKE), "sprint": SPRINT}))
