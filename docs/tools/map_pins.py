#!/usr/bin/env python3
"""Draw the pins (hand-inked X plus a two-line serif label with a cream halo) onto the painted city map.

Why: asking Gemini to add pins kept rewriting the district names (it turned "THE FAIRGROUND DISTRICT" into
"THE FAIRGROUND GRAND"). Drawing the pins ourselves gives exact spelling and placement and changes nothing else.

Each stage is built from the stage-0 map (base + "CURIOS & CHRONICLES" label), with every earlier pin in brown ink
and the newest pins in red, as the Living-Map pin rules say. Coordinates are in pixels of the 2752x1536 map.

Run with the venv that has pillow:
  ~/.config/shadow-exchange/venv/bin/python docs/tools/map_pins.py --base map-city-s00.png --out-dir DIR
Add a stage by appending to STAGES (new pins at the end of the list for that stage; earlier pins are carried).
"""
import argparse
import os
import random

from PIL import Image, ImageDraw, ImageFilter, ImageFont

FONT = "/System/Library/Fonts/Supplemental/Baskerville.ttc"
RED = (172, 24, 30)
BROWN = (84, 48, 26)
INK_EDGE = {RED: (112, 14, 18), BROWN: (52, 28, 14)}

# name: (X centre, label centre, label lines, label font size)
PINS = {
    "fairground_grand": ((1620, 700), (1405, 692), ["THE FAIRGROUND", "GRAND"], 28),
    "emmerich": ((1955, 865), (2215, 862), ["EMMERICH &", "DAUGHTER"], 38),
    "eastern_pier": ((2441, 1239), (2585, 1160), ["EASTERN", "PIER"], 38),
    "ashby_house": ((1843, 198), (1990, 178), ["ASHBY", "HOUSE"], 38),
}
# stage -> pins in order of arrival
STAGES = {
    "s01": ["fairground_grand"],
    "s02": ["fairground_grand", "emmerich"],
    "s03": ["fairground_grand", "emmerich", "eastern_pier", "ashby_house"],
}


def stroke(layer, p0, p1, width, color, rnd):
    d = ImageDraw.Draw(layer)
    n = 24
    for i in range(n + 1):
        t = i / n
        x = p0[0] + (p1[0] - p0[0]) * t
        y = p0[1] + (p1[1] - p0[1]) * t
        # hand wobble perpendicular to the stroke
        dx, dy = p1[0] - p0[0], p1[1] - p0[1]
        L = (dx * dx + dy * dy) ** 0.5
        nx, ny = -dy / L, dx / L
        w = rnd.uniform(-1.6, 1.6) + 2.2 * (0.5 - abs(t - 0.5))
        x, y = x + nx * w, y + ny * w
        r = width / 2 * (0.82 + 0.4 * (0.5 - abs(t - 0.5)) + rnd.uniform(-0.05, 0.05))
        d.ellipse([x - r, y - r, x + r, y + r], fill=color + (255,))


def draw_x(img, cx, cy, color, half=52, width=13, seed=1):
    rnd = random.Random(seed)
    layer = Image.new("RGBA", img.size, (0, 0, 0, 0))
    edge = Image.new("RGBA", img.size, (0, 0, 0, 0))
    a0, a1 = (cx - half, cy - half * 0.95), (cx + half * 0.95, cy + half)
    b0, b1 = (cx + half * 0.9, cy - half), (cx - half, cy + half * 0.9)
    for p0, p1 in ((a0, a1), (b0, b1)):
        stroke(edge, p0, p1, width + 5, INK_EDGE[color], rnd)
        stroke(layer, p0, p1, width, color, rnd)
    edge = edge.filter(ImageFilter.GaussianBlur(0.8))
    layer = layer.filter(ImageFilter.GaussianBlur(0.6))
    img.alpha_composite(edge)
    img.alpha_composite(layer)


def draw_label(img, lines, cx, cy, size):
    font = ImageFont.truetype(FONT, size)
    line_h = int(size * 1.12)
    total = line_h * len(lines)
    halo = Image.new("RGBA", img.size, (0, 0, 0, 0))
    txt = Image.new("RGBA", img.size, (0, 0, 0, 0))
    hd, td = ImageDraw.Draw(halo), ImageDraw.Draw(txt)
    y = cy - total / 2
    for line in lines:
        w = td.textlength(line, font=font)
        pos = (cx - w / 2, y)
        hd.text(pos, line, font=font, fill=(252, 240, 212, 255), stroke_width=9, stroke_fill=(252, 240, 212, 255))
        td.text(pos, line, font=font, fill=(18, 12, 8, 255))
        y += line_h
    halo = halo.filter(ImageFilter.GaussianBlur(7))
    img.alpha_composite(halo)
    img.alpha_composite(txt)


def build(base_path, pins):
    img = Image.open(base_path).convert("RGBA")
    for i, name in enumerate(pins):
        newest = i >= len(pins) - NEW_COUNT.get(len(pins), 1)
        (xc, yc), (lx, ly), lines, size = PINS[name]
        draw_x(img, xc, yc, RED if newest else BROWN, seed=sum(ord(c) for c in name))
        draw_label(img, lines, lx, ly, size)
    return img.convert("RGB")


# how many of the last pins in a stage are new (red)
NEW_COUNT = {1: 1, 2: 1, 4: 2}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--base", required=True, help="stage-0 map (base + CURIOS & CHRONICLES label)")
    ap.add_argument("--out-dir", required=True)
    ap.add_argument("--stages", default="s01,s02,s03")
    a = ap.parse_args()
    os.makedirs(a.out_dir, exist_ok=True)
    for st in a.stages.split(","):
        out = os.path.join(a.out_dir, "map-city-%s.png" % st)
        build(a.base, STAGES[st]).save(out)
        print("wrote", out)


if __name__ == "__main__":
    main()
