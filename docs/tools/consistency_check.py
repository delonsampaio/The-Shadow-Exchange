#!/usr/bin/env python3
"""Shadow Exchange consistency check. Run: python3 -I docs/tools/consistency_check.py [--players PATH]
Checks (exit 1 if any fail):
  A. every repo path named in the docs exists
  B. every NPC file is in 03-NPCs/NPC-Index.md
  C. every canon/prep/generator file is named in 00-Canon/File-Index.md
  D. no retired phrase from docs/tools/stale-phrases.txt appears outside the history folders
  E. no secret word from docs/tools/spoiler-words.txt appears in the players' site
"""
import os, re, sys
ROOT=os.path.abspath(os.path.join(os.path.dirname(__file__),'..','..'))
PLAYERS=os.path.abspath(os.path.join(ROOT,'..','The-Shadow-Exchange-Players'))
if '--players' in sys.argv: PLAYERS=sys.argv[sys.argv.index('--players')+1]
TOP=('00-Canon','01-Crew','02-Factions','03-NPCs','04-Locations','05-Sessions','06-Scores','07-Clocks','08-Loot-and-Anchors','09-Threads','10-Generators','11-Visuals','docs','Public-Wiki')
SKIP_SCAN=('docs/review','docs/superpowers','00-Canon/_archive','99-Workshop','.git','11-Visuals/vendor','Public-Wiki/00-Who-We-Are.md')
def md_files(base):
    for d,ds,fs in os.walk(base):
        rel=os.path.relpath(d,base)
        ds[:]=[x for x in ds if x not in ('.git','node_modules','_archive','vendor')]
        for f in fs:
            if f.endswith('.md'): yield os.path.join(d,f)
def rel(p): return os.path.relpath(p,ROOT)
def skipped(r): return any(r==s or r.startswith(s+'/') or r.startswith(s) and s.endswith('.md') for s in SKIP_SCAN)
bad=0
# files named in the docs that are deliberately not created yet; remove from here when created
PLANNED={'docs/The-Crew.md','docs/Our-Map.md','docs/assets/map-city.jpg'}
def report(title,items):
    global bad
    if items:
        bad+=len(items); print(f'\n✗ {title} ({len(items)})')
        for i in items[:60]: print('   ',i)
        if len(items)>60: print('    …',len(items)-60,'more')
    else: print(f'✓ {title}')
files=[p for p in md_files(ROOT) if not skipped(rel(p))]
# A. referenced paths
pat=re.compile(r'`((?:'+'|'.join(re.escape(t) for t in TOP)+r')/[A-Za-z0-9_.\-/ ()\'’&]+?\.(?:md|html|js|png|mp3|sh|pdf|jpg))`')
miss=[]
for p in files:
    for m in pat.finditer(open(p,encoding='utf-8',errors='ignore').read()):
        t=m.group(1)
        if t in PLANNED or re.search(r'NN|0N|\bN\b|\*|<|…|sNN|\[',t): continue
        if not (os.path.exists(os.path.join(ROOT,t)) or (t.startswith('docs/') and os.path.exists(os.path.join(PLAYERS,t)))):
            miss.append(f'{rel(p)} → {t}')
report('A. referenced files that do not exist',sorted(set(miss)))
# B. NPC index
idx=open(os.path.join(ROOT,'03-NPCs/NPC-Index.md'),encoding='utf-8').read()
nm=[]
for p in md_files(os.path.join(ROOT,'03-NPCs')):
    b=os.path.basename(p)
    if b.startswith('_') or b in ('NPC-Index.md','NPC-Bench.md'): continue
    if b not in idx and b[:-3] not in idx: nm.append(rel(p))
report('B. NPC files missing from 03-NPCs/NPC-Index.md',nm)
# C. file index
fidx=open(os.path.join(ROOT,'00-Canon/File-Index.md'),encoding='utf-8').read()
cm=[]
for d in ('00-Canon','01-Crew','02-Factions','04-Locations','05-Sessions','06-Scores','07-Clocks','08-Loot-and-Anchors','09-Threads','10-Generators'):
    for p in md_files(os.path.join(ROOT,d)):
        b=os.path.basename(p)
        if b.startswith('_') or re.match(r'(Session|Score)-\d',b) or b=='README.md': continue
        if '/PCs/' in p or '/The-Subway/' in p or '/Sites-of-Interest/' in p: continue
        if b not in fidx and b[:-3] not in fidx and os.path.dirname(rel(p))+'/' not in fidx: cm.append(rel(p))
report('C. files not named in 00-Canon/File-Index.md',cm)
# D. stale phrases
sp=[]
sf=os.path.join(ROOT,'docs/tools/stale-phrases.txt')
phr=[l.rstrip('\n').split(' :: ',1) for l in open(sf,encoding='utf-8') if l.strip() and not l.startswith('#')]
for p in files:
    if rel(p).startswith('docs/tools'): continue
    txt=open(p,encoding='utf-8',errors='ignore').read()
    for ph in phr:
        pattern=ph[0].strip()
        if re.search(pattern,txt,re.I): sp.append(f'{rel(p)}: /{pattern}/ — {ph[1].strip() if len(ph)>1 else ""}')
report('D. retired phrases still present',sp)
# E. spoilers in players' site
sw=[]
if os.path.isdir(os.path.join(PLAYERS,'docs')):
    words=[l.strip() for l in open(os.path.join(ROOT,'docs/tools/spoiler-words.txt'),encoding='utf-8') if l.strip() and not l.startswith('#')]
    for p in md_files(os.path.join(PLAYERS,'docs')):
        txt=open(p,encoding='utf-8',errors='ignore').read()
        for w in words:
            if re.search(w,txt,re.I): sw.append(f'{os.path.relpath(p,PLAYERS)}: /{w}/')
    report("E. secret words in the players' site",sw)
else: print("• E. skipped (players' repo not found)")
# F. comedy beats must be labelled read-aloud (the GM never acts anything out)
fb=[]
for n in range(0,4):
    pth=os.path.join(ROOT,f'05-Sessions/Session-0{n}-Prep.md')
    if not os.path.exists(pth): continue
    ls=open(pth,encoding='utf-8').read().split('\n')
    for i,l in enumerate(ls):
        if 'COMEDY BEAT' in l and '🎭' in l:
            body=re.sub(r'\*\*\[[^\]]*\]\*\*','',l.split(':**',1)[1] if ':**' in l else '').strip(' >*—-')
            if len(re.sub(r'\*[^*]*\*','',body).strip())>25 and not re.search(r'READ ALOUD|SAY',l):
                nxt=' '.join(ls[i+1:i+4])
                if not re.search(r'READ ALOUD|SAY',nxt): fb.append(f'{rel(pth)}:{i+1}')
report('F. comedy beats with unlabelled narration (must be 🔊 READ ALOUD or 🗣 SAY)',fb)
print('\nRESULT:','CLEAN' if bad==0 else f'{bad} issue(s)')
sys.exit(1 if bad else 0)
