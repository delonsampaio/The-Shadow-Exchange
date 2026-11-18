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
| ~~`The-Shadow-Exchange.wiki/`~~ (the old GitHub wiki) | **Removed.** The wiki feature was disabled on the main repo (2026-11-16); the local `.wiki` folder, if still present, is a dead copy — do not edit it. | — |

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

### 3b. Wiki images — dedicated portraits only *(rule adopted 2026-11-17)*
**Never reuse a session/TV image on the wiki.** Table images are *scenes* — they carry props, clues and reveals (Greta's has a shape in the window; Harlan's has the Wall of the Missing) and the crew should first see them *at the table*.
- **Every NPC the crew sees on screen gets a wiki portrait — one-scene cameos included (GM decision, 2026-11-17; no tiers).** Cheapest workflow: generate the portrait right after the NPC's table image, in the *same* Gemini chat, and hold it until the crew has met them. If the chat is gone, attach the saved table image as the face reference.
- **Each NPC gets a separate wiki portrait** — head-and-shoulders or full-body, **plain/neutral setting, no scene clues, no GM-secret props**. A **true form** (e.g. Merton's Barghest) may get a portrait **only after the crew has seen it at the table**, and it must show the *outcome as it actually ended* (e.g. whether the collar was returned, kept or destroyed) — including the shop cat (Consequence).
- **Publish an NPC's portrait only after the crew has met them on screen** (for backstory contacts like Greta and Harlan: after their first appearance). Until then the Known Contacts entry is text only.
- **Format:** 3:2 landscape, subject centered, head about one-third from the top (so the site's float-right desktop card *and* the cropped phone banner both work). Save as `wiki-<name>.png` in `11-Visuals/_Saved-Images/`; resize to ~900 px wide JPG into the players repo's `docs/assets/`, and **crop out any generator corner logo**.
- **A portrait may also go on the Player Screen** at the NPC's introduction — it is spoiler-free by construction. The reverse is never allowed.
- Location images follow the same test: fine for the wiki only if they show nothing the crew hasn't visited and no clue (the shop exterior is fine).

### 4. Commit & push *(only when the GM asks)*
The players repo's branch is `main`. **A push publishes the site automatically** (GitHub Actions → Pages, ~1 minute).
```
cd "…/The-Shadow-Exchange-Players"
git add -A && git commit -m "docs: session N recap and updates" && git push
```
Never copy the private repo's `Public-Wiki/` staging folder to the site wholesale.

### 5b. Evolve the Home page *(after Session 1 is played, then every session)*
Home (`docs/index.md`) is the site's front door. **Before Session 1 it is an onboarding page** (the three "Start here" cards). **After the first recap is published it becomes campaign-first:**
- **Keep** the hero and the pitch quote.
- **Replace** the three "Start here" cards with three **current-state cards** (template in the players repo's `MAINTAINING.md`):
  1. **Latest recap** — link to the newest `Session-NN-Recap.md` + a one-sentence hook.
  2. **Where we left off** — 2–3 sentences from the **crew's perspective** (what they carry into the next session).
  3. **What we're wondering** — 2–4 open questions the *players* have, **no answers**.
- **Add** a one-line pointer under the cards: *"New here? [Start here](Quick-Start.md)."* The **Start Here** tab and the onboarding pages stay for reference.
- **Optional "Crew status" table** (Coin, Heat, Rep and any clock the players have actually *seen*; never the Omen, Subway Decay, or Audit unless the crew knows about them).
- **Every session:** refresh the three cards. They get the **same spoiler check** as the recap.

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
