#!/usr/bin/env python3
"""Add one session's played tracks to the players' Soundtrack page.

Reads the GM table `11-Visuals/Wiki-Soundtrack.md` (public titles and holds), then for each track that
played (in play order):
  - skips it if it is already on the page (listed once, at its first session),
  - refuses it if its Track hold is not "—" (the GM must clear "listen" first; "held" never goes up),
  - compresses the MP3 to 128 kbps into the players' repo `docs/assets/music/`,
  - makes a 300 px JPG of its album cover unless the Cover hold says "never" (or "outcome" without --covers-ok),
and appends a "## Session N — Title" section to `docs/Soundtrack.md` (created with a nav entry if missing).

Run with the venv that has pillow (ffmpeg must be on PATH):
  ~/.config/shadow-exchange/venv/bin/python docs/tools/wiki_soundtrack.py --session 0 --title "Opening the Shop" \
      --tracks music-s00-the-pitch,music-bookshop-loop,... [--covers-ok music-s01-the-choice] [--dry-run]
Never run it for a mock. It changes only the players' repo; nothing is committed.
"""
import argparse
import os
import re
import subprocess
import sys

from PIL import Image

GM = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PLAYERS = os.path.join(os.path.dirname(GM), "The-Shadow-Exchange-Players")
TABLE = os.path.join(GM, "11-Visuals", "Wiki-Soundtrack.md")
MUSIC = os.path.join(GM, "11-Visuals", "_Saved-Music")
COVERS = os.path.join(GM, "11-Visuals", "_Album-Covers")
PAGE = os.path.join(PLAYERS, "docs", "Soundtrack.md")
ASSETS = os.path.join(PLAYERS, "docs", "assets", "music")
MKDOCS = os.path.join(PLAYERS, "mkdocs.yml")

PAGE_HEAD = """# Soundtrack

The music from our sessions, in the order it played. Every track was made for this campaign with Google's Lyria music model (AI-generated).

New tracks are added after each session.
"""


def read_table():
    rows = {}
    for line in open(TABLE, encoding="utf-8"):
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) >= 5 and cells[0].startswith("music-"):
            rows[cells[0]] = {"title": cells[1], "session": cells[2], "track_hold": cells[3], "cover_hold": cells[4]}
    return rows


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--session", required=True, type=int)
    ap.add_argument("--title", required=True, help="the session's recap title")
    ap.add_argument("--tracks", required=True, help="comma-separated file names, in the order they played")
    ap.add_argument("--covers-ok", default="", help="tracks whose 'outcome' cover the GM checked against the ending")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--players", default=PLAYERS, help="players' repo (default: the sibling folder)")
    a = ap.parse_args()
    global PAGE, ASSETS, MKDOCS
    PAGE = os.path.join(a.players, "docs", "Soundtrack.md")
    ASSETS = os.path.join(a.players, "docs", "assets", "music")
    MKDOCS = os.path.join(a.players, "mkdocs.yml")

    rows = read_table()
    covers_ok = {t.strip().removesuffix(".mp3") for t in a.covers_ok.split(",") if t.strip()}
    page = open(PAGE, encoding="utf-8").read() if os.path.exists(PAGE) else PAGE_HEAD
    heading = "## Session %d — %s" % (a.session, a.title)
    if re.search(r"^## Session %d\b" % a.session, page, re.M):
        sys.exit("Session %d is already on the Soundtrack page; nothing done." % a.session)

    blocks, problems = [], []
    for name in [t.strip().removesuffix(".mp3") for t in a.tracks.split(",") if t.strip()]:
        row = rows.get(name)
        if not row:
            problems.append("%s: no row in Wiki-Soundtrack.md (add its public title first)" % name)
            continue
        if row["track_hold"] != "—":
            problems.append("%s: Track hold is '%s'; clear it in the table first" % (name, row["track_hold"]))
            continue
        if "assets/music/%s.mp3" % name in page or name in [b[0] for b in blocks]:
            print("skip  %s (already on the page)" % name)
            continue
        src = os.path.join(MUSIC, name + ".mp3")
        if not os.path.exists(src):
            problems.append("%s: no file in _Saved-Music" % name)
            continue
        hold = row["cover_hold"]
        cover = os.path.join(COVERS, "cover-%s.png" % name.removeprefix("music-"))
        use_cover = os.path.exists(cover) and (hold == "—" or (hold == "outcome" and name in covers_ok))
        blocks.append((name, row["title"], src, cover if use_cover else None))
        print("add   %s as \"%s\"%s" % (name, row["title"], "" if use_cover else "  (no cover: %s)" % (hold if os.path.exists(cover) else "missing")))

    if problems:
        print("\nNOT DONE. Fix these first:\n  " + "\n  ".join(problems))
        sys.exit(1)
    if not blocks:
        sys.exit("Nothing new to add.")
    if a.dry_run:
        print("\n(dry run: nothing written)")
        return

    os.makedirs(ASSETS, exist_ok=True)
    out = ["", heading, ""]
    for name, title, src, cover in blocks:
        dst = os.path.join(ASSETS, name + ".mp3")
        subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-i", src, "-map", "0:a", "-map_metadata", "-1",
                        "-codec:a", "libmp3lame", "-b:a", "128k", dst], check=True)
        img = ""
        if cover:
            Image.open(cover).convert("RGB").resize((300, 300), Image.LANCZOS).save(
                os.path.join(ASSETS, "cover-%s.jpg" % name.removeprefix("music-")), quality=85)
            img = '<img src="../assets/music/cover-%s.jpg" alt="">' % name.removeprefix("music-")
        out.append('<div class="track">%s<div><strong>%s</strong><br>'
                   '<audio controls preload="none" src="../assets/music/%s.mp3"></audio></div></div>'
                   % (img, title, name))
        print("wrote %s (%.1f MB)" % (os.path.relpath(dst, a.players), os.path.getsize(dst) / 1e6))
    open(PAGE, "w", encoding="utf-8").write(page.rstrip("\n") + "\n" + "\n".join(out) + "\n")
    print("wrote docs/Soundtrack.md")

    nav = open(MKDOCS, encoding="utf-8").read()
    if "Soundtrack.md" not in nav:
        anchor = "      - The Anchor Ledger: The-Anchor-Ledger.md\n"
        if anchor not in nav:
            print("Add the nav entry by hand: '- Soundtrack: Soundtrack.md' under The Campaign.")
        else:
            open(MKDOCS, "w", encoding="utf-8").write(nav.replace(anchor, anchor + "      - Soundtrack: Soundtrack.md\n"))
            print("added the nav entry under The Campaign")


if __name__ == "__main__":
    main()
