---
entity_type: Core_Canon
authority_level: absolute
purpose: "Exactly how Claude updates the PLAYER-FACING wiki after every session — what to add, what to never copy, and how to publish."
last_updated: 2026-11-24
---

# Wiki Update Protocol (after every session)

The player-facing guide is now a **website**: **https://delonsampaio.github.io/The-Shadow-Exchange-Players/** — built with MkDocs Material and published by GitHub Pages from the repo **`The-Shadow-Exchange-Players`** (sibling folder). Players read the site; they never see this private repo.

| Place | What it is | Who sees it |
|---|---|---|
| **`The-Shadow-Exchange-Players/docs/`** (its own public git repo → GitHub Pages) | **The one maintained player guide.** Edit the Markdown here; a push rebuilds the site in ~1 minute. | Everyone with the link |
| `The-Shadow-Exchange/Public-Wiki/` | A **staging area** in the private repo: recap drafts. | GM only until copied |
| ~~`The-Shadow-Exchange.wiki/`~~ (the old GitHub wiki) | **Removed.** The wiki feature was disabled on the main repo (2026-11-16); the local `.wiki` folder, if still present, is a dead copy — do not edit it. | — |

**Never publish anything from a 🔒 GM ONLY block, any `GM-Private/` file, `Campaign-Arc.md`, the Casting Mask, the Architect, Kress, Stalls = Apex, the Thorne tells (all nine), or the Omen's cause.**

---

## Steps (do these *after* the GM confirms the session's results; skip all if mock)

**0. Gate.** Run only if the GM said the session was real (not "mock"). Take PC names and table canon from the GM's confirmed end-of-session snapshot, never from dashboard state left over from a mock. If unsure, ask.

**Every update ends with the propagation map and the check:** `00-Canon/Change-Propagation-Map.md`, then `python3 -I docs/tools/consistency_check.py` (it also sweeps the players' site for secret words).

**After Session 0 (no recap):** (a) `Our-Lair.md` → add a "The Crew" section: firm reputation, crew abilities (Double Bookkeeping in one plain line with no Audit wording, plus the pick), the upgrade, the coin code, and any Wall-of-Rules rule a PC claimed; (b) add `docs/The-Crew.md`: per PC name, playbook, look and nickname (no Heirloom pattern, no closing answers) and add it to the nav under The World; (c) the Session-Recaps placeholder stays; (d) Home stays the onboarding version; (e) start the Soundtrack page (§3c, heading "Session 0 — Opening the Shop") and the Our Map page (§3d, `map-city-s00`). No recap banner and no Anchor card for Session 0. Never publish the players' closing-question answers.

**Recap naming:** file `Session-NN-Recap.md` (two digits). Nav label `Session N — Title`, added newest-first under *The Campaign → Session Recaps*; index line at the top; strip the template's front matter except `title`; keep staging `status: Draft` until the GM confirms.

### 1. Draft the recap (staging)
Create `The-Shadow-Exchange/Public-Wiki/Session-Recaps/Session-NN-Recap.md` from `_Session-Recap-Template.md`:
- **Second person, present tense, prose.** What the crew did, in order. 2–4 paragraphs.
- **Choices Made** — the decisions that matter later (the collar returned; the thimble kept; Gerald adopted).
- **Mechanical Outcomes** — Coin, Heat, Rep, only clocks the GM has shown on the TV by name; *never* the Omen, Subway Decay or the tells.
- **Open Questions** — only things the *players* are wondering. **No answers.**
- **Who You Met** — one sentence each, from the crew's perspective.
- Tone: dry noir, with the funny parts left funny (only the funny parts that actually happened this session).

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
4. **Update** `docs/The-Anchor-Ledger.md`: add one row per Anchor transaction — *Date · Location · Anchor Description · Status* (exactly one of Seized / Destroyed / Returned / Refused; "kept" means Seized). Delete the `*Pending*` row on the first entry; *Date* = the session played (`S1`); *Description* = what the crew saw. "Active Crew Concerns" = at most 3 bullets copied from the recap's Open Questions. **Known Contacts:** add only NPCs who spoke with the crew on screen (`### Name`, one paragraph, then `*Where to find them.*`); edit existing backstory entries (Harlan, Greta) on first appearance instead of duplicating them; for pre-cast NPCs (e.g. Thorne) surface behaviour only. **Do not** include GM-private consequences; use the *player-known* description.
5. **Update** `docs/Known-Contacts.md`: add NPCs the crew has *actually met* (one paragraph, in-world voice, no secrets; crew's perspective).
6. **Update** `docs/Our-Lair.md` **only** if the lair changed (new upgrade, room, van, a new rule on the Wall).
7. **Update** `docs/index.md` / `mkdocs.yml` only if a new top-level page is added.
8. **Check the build (mandatory):** `mkdocs build --strict` — it fails on broken links, and the site's CI builds with `--strict`, so a broken link means it silently does not publish. **Spoiler sweep:** run `grep -n -i -E "architect|kress|casting|understud|mimic|omen|decay|stalls|subway|tell" <changed files>`; every hit needs a reason the crew saw it, or it goes; no NPC from an unplayed session may be named.

### 3b. Wiki images — dedicated portraits only *(rule adopted 2026-11-17)*
**Never reuse a session/TV image on the wiki.** Table images are *scenes* — they carry props, clues and reveals (Greta's has a shape in the window; Harlan's has the Wall of the Missing) and the crew should first see them *at the table*.
- **Every NPC the crew sees on screen gets a wiki portrait — one-scene cameos included (GM decision, 2026-11-17; no tiers).** Cheapest workflow: generate the portrait right after the NPC's table image, in the *same* Gemini chat, and hold it until the crew has met them. If the chat is gone, attach the saved table image as the face reference.
- **Each NPC gets a separate wiki portrait** — head-and-shoulders or full-body, **plain/neutral setting, no scene clues, no GM-secret props**. A **true form** (e.g. Merton's Barghest) may get a portrait **only after the crew has seen it at the table**, and it must show the *outcome as it actually ended* (e.g. whether the collar was returned, kept or destroyed) — including the shop cat (Consequence).
- **Publish an NPC's portrait only after the crew has met them on screen** (for backstory contacts like Greta and Harlan: after their first appearance). Until then the Known Contacts entry is text only.
- **Format:** 3:2 landscape, subject centered, head about one-third from the top (so the site's float-right desktop card *and* the cropped phone banner both work). Save as `wiki-<name>.png` in `11-Visuals/_Saved-Images/`; resize to ~900 px wide JPG into the players repo's `docs/assets/`, and **crop out any generator corner logo**.
- **A portrait may also go on the Player Screen** at the NPC's introduction — it is spoiler-free by construction. The reverse is never allowed.
- Location images follow the same test: fine for the wiki only if they show nothing the crew hasn't visited and no clue (the shop exterior is fine).

### 3c. Soundtrack page *(GM decision 2026-11-24: public, small covers, first live after Session 0)*
1. List the tracks that **actually played**, in order, from this session's cue log (not the prep's plan). Generic backup tracks count if they played.
2. Check each one in `11-Visuals/Wiki-Soundtrack.md`: it needs a row (public title). Any **Track hold** other than `—` must be cleared by the GM first: a `listen` track is a vocal one with generated words, so ask *"Did you listen to [title]? Anything in the words that gives something away?"* For a **Cover hold** of `outcome`, check the cover against how the scene really ended.
3. Run `~/.config/shadow-exchange/venv/bin/python docs/tools/wiki_soundtrack.py --session N --title "<recap title>" --tracks <file,file,…> [--covers-ok <file,…>]` (add `--dry-run` first). It compresses the tracks to 128 kbps, makes 300 px covers, skips tracks already on the page, and adds the section and the nav entry. About 2 MB a track.
4. The public titles get the same spoiler check as the recap.

### 3d. Our Map page *(first live after Session 0)*
- Publish the **newest city map that was on the TV this session** (`map-city-sNN.png`, pins drawn by `docs/tools/map_pins.py`), never a later stage. Resize to 1600 px wide JPG as the players' `docs/assets/map-city.jpg`, replacing the last one.
- After Session 0, create `docs/Our-Map.md` and add `- Our Map: Our-Map.md` under *The World* in `mkdocs.yml`:
  ```
  # Our Map

  The city as the crew knows it. New places are marked as we learn them: red for the newest, brown for the ones before.

  ![The city](assets/map-city.jpg)

  *Last updated after Session N.*
  ```
- Each session after that: replace the JPG (only if a newer map was shown) and update the last line. A regional or zoom map gets its own heading on the same page once it has been shown.

### 3e. Recap banner *(one per recap, from Session 1)*
- One wiki-only picture per recap, made **after** the session from the confirmed recap text: a neutral moment the crew lived (the van outside the theater, the crew round the bookshop counter). **No reveal, no true form, no clue, no hidden figure, no NPC the crew hasn't met, no text.**
- Make it with `docs/tools/gemini_image.py` (Flash, `--aspect 16:9 --size 1K`, the painted-style block, "Full-bleed, no border. No readable text. No watermark."). For faces, use only the `wiki-*` portraits as references, **never a TV scene image** (they carry props and clues).
- Save as `wiki-recap-sNN.png` in `11-Visuals/_Saved-Images/`; resize to 1400 px wide JPG as the players' `docs/assets/recap-sNN.jpg`; put `![](assets/recap-sNN.jpg)` right under the recap's title. It gets the §2 spoiler check like the text.

### 3f. Anchor cards *(when an Anchor row is added)*
- For each new Anchor Ledger row, one picture of the object **as the crew last saw it** (mended, broken, kept), alone on a plain dark surface, no scene, no hands, no text. Flash, `--aspect 1:1 --size 1K`, the painted-style block.
- Save as `wiki-anchor-<name>.png`; resize to 400 px JPG as the players' `docs/assets/anchors/<name>.jpg`. In `The-Anchor-Ledger.md`, under the table, keep an `## Anchor cards` section: `<div class="anchor-cards">` holding one `<figure><img src="../assets/anchors/<name>.jpg" alt=""><figcaption>Session N · Description</figcaption></figure>` per Anchor, newest first.

### 4. Evolve the Home page *(after Session 1 is played, then every session)*
Home (`docs/index.md`) is the site's front door. **Before Session 1 it is an onboarding page** (the three "Start here" cards). **After the first recap is published it becomes campaign-first:**
- **Keep** the hero and the pitch quote.
- **Replace** the three "Start here" cards with three **current-state cards** (template in the players repo's `MAINTAINING.md`):
  1. **Latest recap** — link to the newest `Session-NN-Recap.md` + a one-sentence hook.
  2. **Where we left off** — 2–3 sentences from the **crew's perspective** (what they carry into the next session).
  3. **What we're wondering** — 2–4 open questions the *players* have, **no answers**.
- **Add** a one-line pointer under the cards: *"New here? [Start here](Quick-Start.md)."* The **Start Here** tab and the onboarding pages stay for reference.
- **Optional "Crew status" table** (Coin, Heat, Rep and any clock the players have actually *seen*; only clocks the GM has shown on the TV by name).
- **Every session:** refresh the three cards. They get the **same spoiler check** as the recap.

### 5. Build check (mandatory)
Run `mkdocs build --strict` and fix every error before reporting.

### 6. Report to the GM
`GM ONLY — WIKI UPDATED: [files changed]. Spoiler check: passed/flagged X.`

---

### 7. Commit & push *(only when the GM asks)*
The players repo's branch is `main`. **A push publishes the site automatically** (GitHub Actions → Pages, ~1 minute).
```
cd "…/The-Shadow-Exchange-Players"
git add -A && git commit -m "docs: session N recap and updates" && git push
```
Never copy the private repo's `Public-Wiki/` staging folder to the site wholesale.
Run `git status` first, add files by name (not `-A`), then `gh run list -L1` to confirm the deploy succeeded. If the GM did not ask to push, end the report with: **NOT PUSHED — say "push the wiki" to publish.**

## What *to* publish every time (quick list)
✅ Recap (with its banner) · ✅ Anchor Ledger rows (with their cards) · ✅ New contacts met · ✅ Public clocks that moved · ✅ A "What the crew is thinking about" line · ✅ The Zoltar fortune card text *(players saw it)* · ✅ The session's tracks (Soundtrack) · ✅ The newest map shown

## What *never* to publish
🚫 Anything in `GM-Private/` · 🚫 `Campaign-Arc.md` · 🚫 Thorne's tells as tells · 🚫 Omen/Decay *causes* · 🚫 Unlearned NPC secrets · 🚫 The dashboard's GM-secret panel

---

## Mock sessions
**Skip the whole protocol.** Do not draft, copy, or commit. Mock canon (PC names, nicknames, the coin code) can persist in the dashboard — never carry it into a real recap or the site.
