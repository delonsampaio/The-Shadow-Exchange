---
entity_type: Core_Canon
authority_level: absolute
purpose: "Exactly how Claude updates the PLAYER-FACING wiki after every session — what to add, what to never copy, and how to publish."
last_updated: 2026-11-16
---

# Wiki Update Protocol (after every session)

There are **two places** with player-facing content. Know the difference:

| Place | What it is | Who sees it |
|---|---|---|
| **`The-Shadow-Exchange.wiki/`** (sibling folder; its own git repo → GitHub wiki) | **The real player wiki.** Players read this. | Players |
| `The-Shadow-Exchange/Public-Wiki/` | A **staging area** inside the private repo: the recap draft and `00-Who-We-Are.md`. | GM only until copied |

**Never edit the wiki with anything from a 🔒 GM ONLY block, any `GM-Private/` file, `Campaign-Arc.md`, the Casting Mask, the Architect, Kress, Stalls = Apex, the six Thorne tells, or the Omen's cause.**

---

## Steps (do these *after* the GM confirms the session's results; skip all if mock)

### 1. Draft the recap (staging)
Create `The-Shadow-Exchange/Public-Wiki/Session-Recaps/Session-NN-Recap.md` from `_Session-Recap-Template.md`:
- **Second person, present tense, prose.** What the crew did, in order. 2–4 paragraphs.
- **Choices Made** — the decisions that matter later (the collar returned; the thimble kept; Gerald adopted).
- **Mechanical Outcomes** — Coin, Heat, Rep, public clocks (Detection, Audit); *not* the Omen, Decay (unless the crew has seen it), or tells.
- **Open Questions** — only things the *players* are wondering. **No answers.**
- **Who You Met** — one sentence each, from the crew's perspective.
- Tone: dry noir, with the funny parts left funny (include Gerald, Agnes's serial, the beets).

### 2. Spoiler check (mandatory)
Before copying anything to the wiki, scan for these and **remove** them:
- [ ] The Understudied / the Casting Mask / "Thorne is…" / any tell labelled as a tell
- [ ] The Omen as a clock (symptoms only, written as "odd things the crew noticed")
- [ ] The Architect, Kress, Stalls Holdings = Apex, the V&L contract chain
- [ ] What the Subway *is* (the crew still doesn't know) — you may write "the crew found a place beneath the city…" once they've been there
- [ ] Any NPC's secret (Mabel's Thomas, Emmerich's naming secret, Thorne's ring) **unless the crew learned it in play**
- [ ] Anything the crew did **not** actually see or hear

### 3. Publish to the wiki
In `The-Shadow-Exchange.wiki/`:
1. **Add** `Session-NN-Recap.md` (copy the reviewed draft).
2. **Update** `Session-Recaps.md` (the index): add one line — `- [[Session NN Recap]] — [title] — [one-sentence hook]`.
3. **Update** `The-Anchor-Ledger.md`: add one row per Anchor transaction — *Date · Location · Anchor Description · Status* (Seized / Destroyed / Returned / Refused). **Do not** include GM-private consequences. Use the *player-known* description.
4. **Update** `Known-Contacts.md`: add NPCs the crew has *actually met* (one paragraph, in-world voice, no secrets). Use the **crew's perspective** (e.g., Cosma — "retired schoolteacher; helped us through the stairs").
5. **Update** `Our-Lair.md` **only** if the lair changed (a new upgrade, a new room, the van, a new rule on the Wall).
6. **Update** `Home.md` only if a new top-level page was added.
7. **Check** all `[[wiki links]]` resolve.

### 4. Commit & push *(only when the GM asks)*
The wiki repo's branch is `master`.
```
cd "…/The-Shadow-Exchange.wiki"
git add -A && git commit -m "docs: session N recap and updates" && git push
```
Never push the private repo's `Public-Wiki/` staging folder to the public wiki wholesale.

### 5. Report to the GM
`GM ONLY — WIKI UPDATED: [files changed]. Spoiler check: passed/flagged X.`

---

## What *to* publish every time (quick list)
✅ Recap · ✅ Anchor Ledger rows · ✅ New contacts met · ✅ Public clocks that moved · ✅ A "What the crew is thinking about" line · ✅ The Zoltar fortune card text *(players saw it)*

## What *never* to publish
🚫 Anything in `GM-Private/` · 🚫 `Campaign-Arc.md` · 🚫 Thorne's tells as tells · 🚫 Omen/Decay *causes* · 🚫 Unlearned NPC secrets · 🚫 The dashboard's GM-secret panel

---

## Mock sessions
**Skip the whole protocol.** Do not draft, copy, or commit.
