#!/usr/bin/env python3
"""Generate campaign music candidates with Lyria through the Gemini API (REST, no SDK).

Key: ~/.config/shadow-exchange/gemini_api_key (or GEMINI_API_KEY). Never printed, never in a repo.

  python3 docs/tools/gemini_music.py --prompt-file p.txt --out-dir DIR --name music-ashby-approach

Models: clip = lyria-3-clip-preview (fixed 30 s, about $0.04), full = lyria-3.5 (about a couple of minutes, about $0.08),
pro = lyria-3-pro-preview (about $0.08). Writes <name>-a.mp3, <name>-b.mp3 ... and prints size and (if ffprobe exists) duration.
The prompt text is prefixed with a strict instrumental line, because Lyria sometimes sings; any returned text is printed
so unwanted lyrics are noticed. The GM listens and picks; Claude then renames and loops the chosen file.
"""
import argparse
import base64
import json
import os
import shutil
import subprocess
import sys
import urllib.error
import urllib.request

MODELS = {"clip": "lyria-3-clip-preview", "full": "lyria-3.5", "pro": "lyria-3-pro-preview"}
KEY_FILE = os.path.expanduser("~/.config/shadow-exchange/gemini_api_key")
URL = "https://generativelanguage.googleapis.com/v1beta/models/%s:generateContent"
PREFIX = ("Strictly instrumental only. No vocals, no singing, no choir, no humming, no spoken words. "
          "Instrumental score, not a song. ")


def load_key():
    key = os.environ.get("GEMINI_API_KEY", "").strip()
    if not key and os.path.exists(KEY_FILE):
        key = open(KEY_FILE, encoding="utf-8").read().strip()
    if not key:
        sys.exit("No API key: set GEMINI_API_KEY or create " + KEY_FILE)
    return key


def generate(key, model, prompt):
    body = {"contents": [{"parts": [{"text": prompt}]}]}
    req = urllib.request.Request(URL % model, data=json.dumps(body).encode(),
                                 headers={"Content-Type": "application/json", "x-goog-api-key": key})
    try:
        with urllib.request.urlopen(req, timeout=600) as r:
            data = json.loads(r.read().decode())
    except urllib.error.HTTPError as e:
        raise RuntimeError("HTTP %s %s" % (e.code, e.read().decode()[:300]))
    audio, text = None, []
    for cand in data.get("candidates", []):
        for part in cand.get("content", {}).get("parts", []):
            inline = part.get("inlineData") or part.get("inline_data")
            if inline and inline.get("data") and str(inline.get("mimeType", inline.get("mime_type", ""))).startswith("audio"):
                audio = base64.b64decode(inline["data"])
            elif part.get("text"):
                text.append(part["text"])
    if audio is None:
        raise RuntimeError("no audio returned: " + json.dumps(data)[:300])
    return audio, "\n".join(text)


def duration(path):
    if not shutil.which("ffprobe"):
        return None
    try:
        out = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", path],
                             capture_output=True, text=True).stdout.strip()
        return float(out)
    except Exception:
        return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--prompt-file", required=True)
    ap.add_argument("--out-dir", required=True)
    ap.add_argument("--name", required=True)
    ap.add_argument("--model", default="full", choices=list(MODELS), help="full = lyria-3.5 (default, minutes long); clip = fixed 30 s only; pro = redo if not good enough")
    ap.add_argument("--n", type=int, default=1, help="number of candidates (a, b, c ...); default one, redo with --model pro if not good enough")
    a = ap.parse_args()

    key = load_key()
    prompt = PREFIX + open(a.prompt_file, encoding="utf-8").read().strip()
    os.makedirs(a.out_dir, exist_ok=True)
    for i in range(a.n):
        tag = "abcdefgh"[i]
        try:
            audio, text = generate(key, MODELS[a.model], prompt)
        except Exception as e:
            print("%s FAILED: %s" % (tag, str(e).replace(key, "<key>")[:500]))
            continue
        path = os.path.join(a.out_dir, "%s-%s.mp3" % (a.name, tag))
        open(path, "wb").write(audio)
        d = duration(path)
        print("%s ok: %s  %.0f KB  %s" % (tag, path, len(audio) / 1024.0, ("%.1f s" % d) if d else "duration n/a"))
        if text.strip():
            print("   returned text (check for lyrics): " + text.strip()[:200].replace("\n", " | "))


if __name__ == "__main__":
    main()
