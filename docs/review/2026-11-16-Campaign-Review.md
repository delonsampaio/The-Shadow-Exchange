# The Shadow Exchange — Full Campaign Review

**Date:** 2026-11-16 · **Reviewer:** Claude (Sonnet 5.5) · **Scope:** both repos (`The-Shadow-Exchange/` private, `The-Shadow-Exchange.wiki/` player-facing), the original v4 bible (extracted from the .docx), the dashboard code, every cue and filename in the session preps.
**Not covered:** I audited the 32 images and 22 tracks by **filename and cue**, not by looking/listening. I only skimmed the two stale plan docs in `docs/superpowers/`.

---

## 1. Verdict

The bones are excellent: a strong three-layer moral engine (Merton → Emmerich → Mabel), a genuinely good mystery spine (Subway, Mimic, Architect), a distinctive voice, and the Anchor Ledger as the campaign's conscience. The problems were almost all **continuity and runtime**, not ideas:

1. The **campaign arc after Session 3 had vanished** (Bible v5 dropped the v4 "Jobs 3–8", relics, Null-Tech, clock staging, Trophy Wall/Journal bonuses).
2. The **lair was described four different ways**; players were told **spoilers** (the Mimic, the Subway) in handouts.
3. **Session 1 was the thinnest and weakest** (truncated read-alouds; the "politician's dog" never connected to Merton; forced combat that punished mercy).
4. **Tone mismatch:** the files said "deadpan, subtle"; you want *Supernatural*/*Scooby-Doo* — obviously funny.
5. **Rules drift** across the cheat sheet, rules reference, wiki and sessions (flashback costs, downtime activities, Double Bookkeeping, the playbook count).
6. **Runtime fragility** for the Co-GM (no cue grammar, duplicated/stale instructions, a dashboard that lost state on refresh).

All are addressed below. **No git commits or pushes were made.**

---

## 2. How the World Connects (the spine that now holds)

```
Understudied (wears Thorne, 11 yrs) ──routes manufactured contracts──► Emmerich job (S2) ─► silences the one who knows its name
        │                                                               └► Vantage & Lowe's "Preservation Order" bait (S7)
        │ (supplies routing exploit)                                   
Kress (Ministry Suppression Bureau, signs forms) ◄──compatible goals──► Apex Aegis (skims bounties, hunts the Subway)
                                                                          └► Stalls Holdings = Apex shell (S3 Form 88-D extra pages → S4 reveal)
The Subway (chose the crew; ledger dated 3 days BEFORE) ─ Architect ─ red-ink Journal entry ─ the lease nobody signed ─ the Omen
Omen (clock slow S2 → stopped 11:47 S3 → dogs/static → dreams → something wakes at Line 0) ─ the Conductor announces it
Heirlooms ─ each PC's final scene.   Anchor Ledger ─ the epilogue read aloud.
```
Every thread now has a **payoff session**, a **trigger rule**, and a **truth-table entry** (`05-Sessions/Campaign-Arc.md`).

---

## 3. What I Changed (by theme)

### World & story
- **NEW `05-Sessions/Campaign-Arc.md`** — Sessions 0–13 spine, truth table, 10 trigger rules, six Thorne tells, four **endgame** families, Season-Two seeds, and an **open-ended** side-score pool (it is *not* a 13-session campaign).
- **NEW `00-Canon/Campaign-Bible-Appendix.md`** — restored the v4 mechanics v5 dropped.
- **Subway made robust:** NEW `04-Locations/The-Subway/Living-Subway.md` (rules, economy, layout, 6 new regulars, services, job-board/rumor/encounter/exit tables, visible Decay stages, clue trails for all four truths). **`Overview.md`** now states *why they can see it* (conscience, not "goodness"; the ledger-dated-before wrinkle) and **First-Visit Mystery Rules** (Session 2 is pure mystery — no jokes, no explaining).
- **Lair unified** (`04-Locations/Curios-and-Chronicles.md` is the single source of truth): former savings bank, Zoltar → eleven steps → one cold Suite, upper floors (Annex, Lofts), **the Wall of Rules**, Trophy Wall/Journal bonuses, Lair Upgrade Menu, Lair Incidents d8.
- **Timeline fixed:** the crew has worked there **two years**; Thorne was newly assigned to their file; Greta has been processing their forms by mail (first in-person visit Session 1).

### Sessions (all four now start with a **Run Sheet**: beat → trigger → music → image → comedy → what it teaches; plus time budgets)
- **Session 0 — rewritten:** tech checklist, coin code, savings-bank joke, Wall of Rules, scanner reconciled, Zoltar's card, reserved-NPC list.
- **Session 1 — rewritten:** Gerald; full read-alouds; **The Surge** replaces mandatory combat (compassion no longer punished); the collar's location fixed; Thorne tells 1–2 with dialogue; Mara glimpse; correct Heat/Vice/Double Bookkeeping.
- **Session 2 — heavily edited:** Thorne on the street (Tell 3) + evening call (Tell 4); **Door Chase** with Drennick & Foss; entrance **Mystery Layer**; Cosma restrained; downtime moved to the return; Subway tour marked **splittable**; contract now Ministry-routed (fixes the "Subway posting before Subway access" paradox).
- **Session 3 — edited:** clocks stopped at **11:47**, Stalls Holdings clue, Stalls scene, Mabel's fake-out haunt, Grief Jar hum, Agnes's serial, Thorne's pier call (Tell 5), corrected Entanglement/Acquire Assets, "last habitation 1991".

### Comedy (your new direction)
- **NEW `00-Canon/Comedy-Playbook.md`** — Supernatural banter + Scooby chaos, **perform-it** delivery, dial 🟢/🟡/🔴, Laugh-then-Land, running gags (Consequence, Zoltar's cards, Greta's forms, PTOLEMY's charges, Drennick & Foss, Agnes's serial, Gerald), Scooby **unmasking** staging for the Mimic reveal, and a proposed bookmobile van.
- Core Instructions rewritten to match; Tone doc, wiki, Player Reference updated.

### Characters
- **NEW NPC cards:** Merton, Gerald, Drennick & Foss, Renwick Stalls, Agnes Pell, Bernard, Subway Regulars (Conductor, Dev, Bram, Quill, Wim, Ottilie), Zoltar & Consequence (with tables).
- **NEW `01-Crew/PCs/Playbook-Hooks.md`** — spotlight beats, comedy niche, heirloom fit and trauma flavor for all seven playbooks.
- Fixed names: *Mira Solano → Tamsin Solano* (clash with Mara Halliday); *Corvin Ashby → Corvin Pryce* (clash with Mabel Ashby); funeral timeline error; Mask "cost vs accumulation" reconciled; Vantage & Lowe **canon chain** (Understudied supplied the exploit; Kress signed; Apex profited).

### Runtime for Claude
- **NEW `00-Canon/Session-Boot.md`** — boot order, **cue grammar** (what "inline"/"go" mean), label legend, hard rules, GM command table, end-of-session checklist. `CLAUDE.md` now points to it first.
- **Player Screen:** NEW `11-Visuals/Player-Screen.html` + `player-screen/scene.js` — a no-dependency TV display the Co-GM updates (image, caption, cards, public clocks, **comedy banners**). Replaces opening a new Preview window per cue.
- **GM Dashboard:** auto-saves (refresh-safe), `INIT_ANCHORS` now exists, **Thorne-tells tracker**, **running-gags panel**, Surge clock.
- **NEW `00-Canon/Wiki-Update-Protocol.md`** + `Session-Recaps` wiki page — how to update the player wiki after every session (with a spoiler check).

### Teaching Blades to first-timers
- **NEW `00-Canon/Mechanics-Teaching-Ladder.md`** — which mechanic is taught when (max 4 new per session; Group Action moved to Session 2, Entanglements/Acquire Assets to Session 3), a ≤30-second D&D-bridge script for each, training-wheels that fade, and a one-card table reference.
- **Session 0 now has a 10-minute Trial Run** (Beat 4b): one low-stakes practice roll (Consequence knocks the Hunter's Journal off the stand; ninety seconds before a customer walks in) teaching dice, Position, Effect, Stress and Resistance before anything real happens.
- **Player wiki:** NEW `Quick-Start.md` (5 minutes, linked first from Home and the Session 0 Agenda); the long Rules page is now explicitly a reference.
- **GM Dashboard:** NEW **Mechanics Taught** tracker (introduced vs understood).

### Rules accuracy (checked against the Blades SRD)
Flashback costs; Push/Assist/Resist; **two** free downtime activities (SRD) vs one; Group Action stress; Acquire Assets; Entanglement timing; Vice uses *lowest* attribute; "Physick" isn't an action; **seven** playbooks, not eight; 4 dots + playbook, max 2 per action.

### Player-facing wiki (`The-Shadow-Exchange.wiki/`)
Removed a dead `[[Safety and Content]]` link; fixed Ministry tier (V); removed the Subway spoiler; added "this game is funny"; corrected Harlan's distance; added Greta; added TV note; added Session Recaps index and Home link. `Public-Wiki/00-Who-We-Are.md`: **removed the line that told players a first-session contact is not who they seem** (it burned the Mimic).

### Assets
`11-Visuals/ASSET-TODO.md` — the full image/music to-do. **Renamed** `cover-comic-interlude.mp3` → `music-comic-interlude.mp3`; fixed a double-dot filename and a prompt typo. Added prompts for the new cues.

---

## 4. Decisions I Made — **veto any**

| # | Decision | Why | Easiest undo |
|---|---|---|---|
| 1 | **Gerald the dog** (the politician's dog) is a real character; the crew may keep him as a Scooby-style cohort | Connects the hook to Merton; gives the comedy a face | Cut from S1 Beat 4 and Gerald.md |
| 2 | **The Surge replaces mandatory combat** | Compassion shouldn't trigger a punishing fight | Restore the old GM-ONLY block from git |
| 3 | **Emmerich's contract is Ministry-routed** (manufactured by the Understudied) | Fixes "Subway posting before Subway access"; ties the Mimic into S2 | Score-02 + Bounty Board |
| 4 | **Savings-bank history, the Wall of Rules, Zoltar's fortune cards** | Lair richness + comedy engine + foreshadowing | Remove from lair file |
| 5 | **Stalls = Apex shell** | Connects S3 to Apex and the bounty-skimming arc | Stalls file + S3 clue |
| 6 | **Bookmobile van "C&C MOBILE LIBRARY"** (proposed) | The Mystery Machine | Lair Upgrade Menu |
| 7 | **Session 2's Subway first visit has no jokes** (your "mysterious" request) | The reveal should feel impossible | Playbook dial |
| 8 | **Safety/content tools left removed** (you deliberately removed them twice) | Respecting your call | — |

---

## 5. Open Items for You
1. **Generate the assets** (`ASSET-TODO.md`): 13 P0 images, 6 P0 tracks.
2. **Name the city** (S0 checklist): unnamed vs. named.
3. **Decide the Architect** by ~Session 8 (`The-Architect.md`) — Option D (Emmerich) rewards the Session 2 choice.
4. **Dashboard offline:** it loads React/Tailwind/Babel from CDNs; I can vendor them locally.
5. ~~Stale plan docs~~ — **marked STALE** with a banner (`docs/superpowers/*`); safe to delete or archive.
6. **Playtest the Run Sheets** in a mock session (`run session 1 — mock`) before the real Session 0.
7. **Read-aloud check:** read Session 1 Beats 5–6 aloud once to hear pacing.

*Everything is uncommitted. Review `git status` / `git diff` in both repos before committing.*


## 6. Second Pass (end of review)
Full end-to-end reads of Sessions 2 and 3 after the edits fixed: a joke inside the Subway first visit (Cosma's coat gag moved to the second visit), Cosma over-explaining why they were chosen, an out-of-order closing sequence, ambiguous beat numbering, stale downtime rules (Acquire Assets is a Session 3 mechanic), Agnes's contradictory "knows nothing" line, leftover "deadpan" instructions, and nested/duplicated labels. Session 1's engagement-roll math was simplified for first-time players.
