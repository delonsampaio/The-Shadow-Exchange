#!/usr/bin/env python3
"""Build printable HTML + PDF handouts from the Markdown sources (headless Chrome).
Usage (needs the `markdown` package, e.g. the scratchpad venv):
    python3 docs/tools/make_handout_pdfs.py
Outputs to 11-Visuals/handouts/. Sources: 01-Crew/Hunter-Kit.md, 00-Canon/Player-Reference.md."""
import re, subprocess, sys
from pathlib import Path
import markdown

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "11-Visuals" / "handouts"
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
JOBS = [
    ("01-Crew/Hunter-Kit.md", "Hunter-Kit", "The Shadow Exchange · Hunter's Kit", "Loadout reference"),
    ("00-Canon/Player-Reference.md", "Player-Reference", "The Shadow Exchange · Player Reference", "Blades in the Dark for D&D players"),
]
CSS = """
@page { size: letter; margin: 0.55in; }
:root { --amber:#b45309; --ink:#111; --soft:#555; --line:#bbb; }
* { box-sizing:border-box; }
body { margin:0; font-family:'Helvetica Neue',Arial,sans-serif; font-size:10.4pt; line-height:1.38; color:var(--ink); }
header { display:flex; justify-content:space-between; align-items:flex-end; border-bottom:2.5px solid var(--amber); padding-bottom:5px; margin-bottom:10px; }
header b { font-size:15pt; letter-spacing:.05em; text-transform:uppercase; }
header span { font-size:8.6pt; color:var(--soft); letter-spacing:.08em; text-transform:uppercase; }
h1 { display:none; }
h2 { margin:14px 0 4px; font-size:11.5pt; letter-spacing:.08em; text-transform:uppercase; color:var(--amber); border-bottom:1px solid var(--line); padding-bottom:2px; break-after:avoid; }
h3 { margin:10px 0 3px; font-size:10.8pt; break-after:avoid; }
p { margin:4px 0; } ul, ol { margin:3px 0; padding-left:20px; } li { margin:2px 0; }
table { border-collapse:collapse; width:100%; margin:6px 0; break-inside:avoid; }
th, td { border:1px solid var(--line); text-align:left; vertical-align:top; padding:3px 6px; }
th { background:#f4efe6; font-size:9pt; text-transform:uppercase; letter-spacing:.05em; }
hr { border:0; border-top:1px solid var(--line); margin:10px 0; }
blockquote { margin:6px 0; padding:2px 10px; border-left:3px solid var(--amber); color:#333; }
code { font-family:Menlo,monospace; font-size:9pt; }
"""
for src, stem, title, sub in JOBS:
    text = (ROOT / src).read_text(encoding="utf-8")
    text = re.sub(r"\A---\n.*?\n---\n", "", text, flags=re.S)          # strip front matter
    text = re.sub(r"<!--.*?-->", "", text, flags=re.S)
    body = markdown.markdown(text, extensions=["tables", "sane_lists"])
    html = f"<!DOCTYPE html><html lang='en'><head><meta charset='UTF-8'><title>{title}</title><style>{CSS}</style></head><body><header><b>{title.split(' · ')[1]}</b><span>{sub}</span></header>{body}</body></html>"
    h = OUT / f"{stem}.html"; h.write_text(html, encoding="utf-8")
    pdf = OUT / f"{stem}.pdf"
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--no-pdf-header-footer", f"--print-to-pdf={pdf}", h.as_uri()], check=True, capture_output=True, timeout=120)
    print("wrote", pdf)
