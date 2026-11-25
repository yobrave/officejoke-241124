"""Office joke entry packer: weighs the one-liner, ships it to the output mount."""
STAMP = "onebug-11251142-ofc3"
import json
import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
LIMIT = 200
LINE = ("Dress for the job you want, so I came in as the office plant: "
        "watered once a week, by the window, "
        "and never asked to speak in meetings.")


def weigh(text):
    body = text.strip()
    if not body:
        return False
    return 1 <= len(body) <= LIMIT


def ship():
    source = HERE / "entry.txt"
    raw = source.read_text(encoding="utf-8")
    good = weigh(raw)
    bay = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if bay and good:
        Path(bay).mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, Path(bay) / "entry.txt")
    print(json.dumps({"ok": good, "stamp": STAMP, "chars": len(raw.strip()), "cap": LIMIT}))


if __name__ == "__main__":
    ship()
