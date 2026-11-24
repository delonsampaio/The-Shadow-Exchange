#!/usr/bin/env python3
"""Generate campaign images with the official Gemini API (replaces hand-pasting into the web app).

Calls the REST endpoint directly (no SDK), because the SDK on this Mac's Python 3.9 cannot set
image_size. The API key is read from ~/.config/shadow-exchange/gemini_api_key (or GEMINI_API_KEY).
It is never printed and never stored in this repo.

Run with the venv that has pillow installed:
  ~/.config/shadow-exchange/venv/bin/python docs/tools/gemini_image.py \
      --prompt-file prompt.txt --ref 11-Visuals/_Saved-Images/_anchors/anchor-x.png \
      --out-dir /path/to/candidates --name wiki-x --aspect 3:2 --size 1K

Writes <name>-pro.png and <name>-flash.png and prints each file's pixel size.
Cost per image (Google's pricing page, Nov 2026): Pro about $0.134 at 1K/2K, Flash about $0.067 (1K) / $0.101 (2K).
Observed sizes: 1K 16:9 = 1376x768; 2K should be about 2752x1536.
"""
import argparse
import base64
import io
import json
import mimetypes
import os
import sys
import urllib.error
import urllib.request
import warnings

warnings.filterwarnings("ignore")

from PIL import Image  # noqa: E402

MODELS = {
    "pro": "gemini-3-pro-image",
    "flash": "gemini-3.1-flash-image",
}
KEY_FILE = os.path.expanduser("~/.config/shadow-exchange/gemini_api_key")
URL = "https://generativelanguage.googleapis.com/v1beta/models/%s:generateContent"


def load_key():
    key = os.environ.get("GEMINI_API_KEY", "").strip()
    if not key and os.path.exists(KEY_FILE):
        key = open(KEY_FILE, encoding="utf-8").read().strip()
    if not key:
        sys.exit("No API key: set GEMINI_API_KEY or create " + KEY_FILE)
    return key


def generate(key, model, prompt, ref_paths, aspect, size):
    parts = [{"text": prompt}]
    for p in ref_paths:
        mime = mimetypes.guess_type(p)[0] or "image/png"
        parts.append({"inlineData": {"mimeType": mime, "data": base64.b64encode(open(p, "rb").read()).decode()}})
    img_cfg = {"aspectRatio": aspect}
    if size:
        img_cfg["imageSize"] = size
    body = {
        "contents": [{"parts": parts}],
        "generationConfig": {"responseModalities": ["IMAGE"], "imageConfig": img_cfg},
    }
    req = urllib.request.Request(
        URL % model,
        data=json.dumps(body).encode(),
        headers={"Content-Type": "application/json", "x-goog-api-key": key},
    )
    try:
        with urllib.request.urlopen(req, timeout=300) as r:
            data = json.loads(r.read().decode())
    except urllib.error.HTTPError as e:
        raise RuntimeError("HTTP %s %s" % (e.code, e.read().decode()[:300]))
    for cand in data.get("candidates", []):
        for part in cand.get("content", {}).get("parts", []):
            inline = part.get("inlineData") or part.get("inline_data")
            if inline and inline.get("data"):
                return Image.open(io.BytesIO(base64.b64decode(inline["data"])))
    raise RuntimeError("no image returned: " + json.dumps(data)[:300])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--prompt-file", required=True)
    ap.add_argument("--ref", action="append", default=[], help="reference image (up to 2 recommended)")
    ap.add_argument("--out-dir", required=True)
    ap.add_argument("--name", required=True)
    ap.add_argument("--aspect", default="16:9", help="16:9 or 3:2 etc.")
    ap.add_argument("--size", default="1K", help="1K or 2K")
    ap.add_argument("--models", default="flash", help="comma list from: pro, flash (default: one cheap Flash image; redo with pro if it is not good enough)")
    a = ap.parse_args()

    key = load_key()
    prompt = open(a.prompt_file, encoding="utf-8").read().strip()
    os.makedirs(a.out_dir, exist_ok=True)

    for tag in [t.strip() for t in a.models.split(",") if t.strip()]:
        try:
            img = generate(key, MODELS[tag], prompt, a.ref, a.aspect, a.size)
        except Exception as e:  # never leak the key
            print("%s FAILED: %s" % (tag, str(e).replace(key, "<key>")[:500]))
            continue
        path = os.path.join(a.out_dir, "%s-%s.png" % (a.name, tag))
        img.save(path)
        print("%s ok: %s  %dx%d" % (tag, path, img.width, img.height))


if __name__ == "__main__":
    main()
