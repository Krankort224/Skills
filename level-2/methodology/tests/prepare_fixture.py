"""Create a fresh local test repository for one file-organization or lookup request."""

import argparse
from pathlib import Path
import subprocess


def prepare(root, case):
    root.mkdir(parents=True, exist_ok=False)

    def write(relative_path, content):
        path = root / relative_path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")

    def git(*args):
        subprocess.run(["git", "-C", str(root), *args], check=True, capture_output=True)

    def snapshot(message):
        git("add", "--all")
        git("-c", "user.name=Fixture", "-c", "user.email=fixture@example.invalid",
            "-c", "commit.gpgsign=false", "commit", "-m", message)

    git("init", "--quiet")
    write("incoming/r7.md", "Drawing P-04 / revision 7 / transmittal T-34\n")
    write("incoming/r6.md", "Drawing P-04 / revision 6 / transmittal T-29\n")
    write("incoming/loose.md", "P-04 excerpt. Origin and approval status unknown.\n")
    write("desk.txt", "Contact discipline leads.\n")
    write("guide/dispatch.md", "# Sending an issue set\n\nEnter the transmittal ID in the release register.\n")
    write("index.md", "# Project index\n\n[Dispatch instructions](guide/dispatch.md)\n\n"
          "[Issued plan](incoming/r7.md)\n\n[Previous plan](incoming/r6.md)\n")
    if case == "review":
        write("map.txt", "Goal: a recipient can select the issued P-04 plan.\n"
              "Move incoming/r7.md to handover/p04-r7.md and incoming/r6.md "
              "to handover/p04-r6.md. Update the links in index.md. Leave other files in place.\n")
    snapshot("Record incoming materials")
    if case == "review":
        (root / "handover").mkdir()
        for revision in (6, 7):
            (root / f"incoming/r{revision}.md").rename(root / f"handover/p04-r{revision}.md")
        write("index.md", "# Project index\n\n[Dispatch instructions](guide/dispatch.md)\n\n"
              "[Current P-04 plan](handover/p04-r6.md)\n\n[Current P-04 plan](handover/p04-r7.md)\n")
        snapshot("Apply handover map")
    write("desk.txt", "Contact discipline leads.\nMeeting moved to Thursday.\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("case", choices=["migration", "review"])
    parser.add_argument("destination", type=Path, help="new directory in a disposable workspace")
    args = parser.parse_args()
    prepare(args.destination, args.case)
