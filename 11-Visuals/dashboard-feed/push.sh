#!/bin/bash
# Append one or more ops to the live dashboard feed (seq numbers are assigned automatically).
# usage:  bash push.sh '{"op":"clock","id":"det","value":1,"note":"Detection 1/4"}' '{"op":"stress","pc":2,"value":2,"note":"Inez Stress 2"}'
# ops:    crew{key:heat|coin|rep|wanted|tier|xp,value|delta}  clock{id,value|delta}  stress{pc,value}  harm{pc,slot,value}
#         pc{pc,name,role}  pcinfo{pc,vice,purveyor,heirloom,pattern,stage,friend,rival,trauma,xp}  scene{beat,title,next}
#         tell{id,state}  taught{id,state}  gag{id,note,label?}  faction{id,standing}  anchor_add{name,status}  anchor_status{name,status}  npc_add{name,faction,note,status}
DIR="$(cd "$(dirname "$0")" && pwd)"
python3 -I - "$DIR/feed.js" "$@" <<'PY'
import sys, re, json
f = sys.argv[1]; ops = sys.argv[2:]
s = open(f, encoding="utf-8").read()
seqs = [int(x) for x in re.findall(r'"?seq"?\s*:\s*(\d+)', s)]
n = max(seqs) if seqs else 0
out = []
for o in ops:
    d = json.loads(o); n += 1; d = {"seq": n, **d}
    out.append("DASH_FEED.ops.push(" + json.dumps(d, ensure_ascii=False) + ");\n")
open(f, "a", encoding="utf-8").write("".join(out))
print("pushed", len(out), "op(s); last seq", n)
PY
