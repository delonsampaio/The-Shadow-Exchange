---
entity_type: Core_Canon
authority_level: absolute
purpose: "Exactly how Claude updates the PLAYER-FACING wiki after every session — what to add, what to never copy, and how to publish."
last_updated: 2026-11-16
---

# Wiki Update Protocol (after every session)

The player-facing guide is now a **website**: **https://delonsampaio.github.io/The-Shadow-Exchange-Players/** — built with MkDocs Material and published by GitHub Pages from the repo **`The-Shadow-Exchange-Players`** (sibling folder). Players read the site; they never see this private repo.

| Place | What it is | Who sees it |
|---|---|---|
| **`The-Shadow-Exchange-Players/docs/`** (its own public git repo → GitHub Pages) | **The one maintained player guide.** Edit the Markdown here; a push rebuilds the site in ~1 minute. | Everyone with the link |
| `The-Shadow-Exchange/Public-Wiki/` | A **staging area** in the private repo: recap drafts. | GM only until copied |
| `The-Shadow-Exchange.wiki/` (the old GitHub wiki) | **Deprecated.** Do not edit. It may be disabled. | — |

**Never publish anything from a 🔒 GM ONLY block, any `GM-Private/` file, `Campaign-Arc.md`, the Casting Mask, the Architect, Kress, Stalls = Apex, the six Thorne tells, or the Omen's cause.**

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

### 3. Publish to the player site
In `The-Shadow-Exchange-Players/` (it has its own `MAINTAINING.md` and `CLAUDE.md` for anyone working inside that repo; the spoiler check stays **here**, in the private repo):
1. **Add** `docs/Session-NN-Recap.md` (copy the reviewed draft). Use **normal Markdown links** — `[Text](Page-Name.md)` — **not** `[[wiki links]]`.
2. **Add the page to the nav** in `mkdocs.yml` under *The Campaign* (e.g. `- Session 1 Recap: Session-01-Recap.md`).
3. **Update** `docs/Session-Recaps.md` (the index): add one line — `- [Session NN Recap](Session-NN-Recap.md) — **Title** — one-sentence hook.`
4. **Update** `docs/The-Anchor-Ledger.md`: add one row per Anchor transaction — *Date · Location · Anchor Description · Status* (Seized / Destroyed / Returned / Refused). **Do not** include GM-private consequences; use the *player-known* description.
5. **Update** `docs/Known-Contacts.md`: add NPCs the crew has *actually met* (one paragraph, in-world voice, no secrets; crew's perspective).
6. **Update** `docs/Our-Lair.md` **only** if the lair changed (new upgrade, room, van, a new rule on the Wall).
7. **Update** `docs/index.md` / `mkdocs.yml` only if a new top-level page is added.
8. **Check the build** (optional but recommended): `mkdocs build --strict` — it fails on broken links.

### 4. Commit & push *(only when the GM asks)*
The players repo's branch is `main`. **A push publishes the site automatically** (GitHub Actions → Pages, ~1 minute).
```
cd "…/The-Shadow-Exchange-Players"
git add -A && git commit -m "docs: session N recap and updates" && git push
```
Never copy the private repo's `Public-Wiki/` staging folder to the site wholesale.

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
