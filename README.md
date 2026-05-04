---
campaign: The Shadow Exchange
system: Blades in the Dark / Forged in the Dark
tone: industrial-occult noir — quiet dread, moral ambiguity
---

# The Shadow Exchange — Project Index

This is a working folder for running and reflecting on a Blades in the Dark campaign called *The Shadow Exchange*. Treat `00-Canon/` as the source of truth. Everything else is living state — it changes between sessions, sometimes during them.

## How to use this folder

The folder layout follows the GM's actual workflow rather than a tidy taxonomy. Numbered prefixes are about reading order, not importance.

**Before a session,** open `02-Factions/Faction-Tracker.md`, `07-Clocks/Active-Clocks.md`, and `09-Threads/Plot-Threads.md`. Anything that has shifted since last session lives in those three files. Then open `06-Scores/Active/` and the matching `05-Sessions/Session-NN-Prep.md`.

**During a session,** keep `05-Sessions/Session-NN-Prep.md` open as a scratchpad and `03-NPCs/Active/` reachable for quick lookups. The Omen Clock entry in `07-Clocks/Active-Clocks.md` is GM-secret — keep that one to yourself.

**After a session,** write the recap into `05-Sessions/Session-NN-Recap.md` (second person, present tense, prose). Tick clocks in `07-Clocks/Active-Clocks.md`. Update faction standings and tier shifts in `02-Factions/Faction-Tracker.md`. Log any seized Anchor Items in `08-Loot-and-Anchors/Anchor-Ledger.md` — this is the moral weather report, treat it seriously.

## Folder map

| Folder | What lives here |
|---|---|
| `00-Canon/` | The bible (`Campaign-Bible-v4.md` — markdown is now canonical, edited directly), the SRD, the tone reference, the GM cheat sheet, the player one-pager. The original `.docx` is preserved in `_archive/` and is frozen. |
| `01-Crew/` | Crew sheet, PC sheets, cohorts, crew-wide contacts. |
| `02-Factions/` | One file per faction, plus a single-page tracker. |
| `03-NPCs/` | One file per NPC, sorted by current relevance. Twice-Born get their own subfolder because each one is a moral decision. |
| `04-Locations/` | Curios & Chronicles, the Subway, city districts, sites of interest. The Subway has its own subfolder because it accumulates mystery files. |
| `05-Sessions/` | Numbered Prep + Recap pairs. Keep them adjacent. |
| `06-Scores/` | Score plans (target, 2–3 approaches, complications, Apex/Mimic angle). Active vs completed. The Bounty Board pools urban-legend leads. |
| `07-Clocks/` | All live clocks in one file. Filled clocks move to history. |
| `08-Loot-and-Anchors/` | The Anchor Ledger and crew inventory. |
| `09-Threads/` | Open mysteries, planted foreshadowing waiting to land. |
| `10-Generators/` | Reusable scaffolds for Three-Layer monsters, urban legends, Resonance complications, names & looks. |
| `99-Workshop/` | Drafts, half-baked ideas, anything not yet ready for canon. |

## Files prefixed with underscore

`_Template.md` files (e.g. `_NPC-Template.md`) sort to the top of each folder. Copy them; never edit the original.

## Onboarding — first-time-Blades table

This campaign was scaffolded for a group with 20+ years of D&D / Pathfinder coming to Forged in the Dark for the first time. A few specific accommodations live in the folder:

- **`00-Canon/Running-Your-First-Score.md`** — longer-form GM tutorial. **Read once before Session 1.** Walks through how a Blades score actually flows at the table (engagement roll, action rolls, consequences, resistance, flashbacks, downtime) with worked examples from Heist 1. Pairs with the cheat sheet — this loads the patterns, the cheat sheet handles fast recall.
- **`00-Canon/GM-Cheat-Sheet.md`** — one-page GM reference: Position/Effect, consequences, resistance, downtime activities, when to invite flashbacks, the campaign's custom mechanics in brief. Print and keep at the table.
- **`00-Canon/Player-Reference.md`** — print-ready player one-pager. Action ratings, stress, trauma, resistance, the heist loop, downtime activities, plus a D&D→Blades translation table. One per player.
- **`01-Crew/PCs/Character-Creation-Guide.md`** — player-facing self-contained walkthrough. Players make their PCs *before* Session 0 and bring filled sheets to the table. Covers playbook picks, action ratings, friends/rivals, the Cursed Heirloom prompt.
- **`05-Sessions/Session-00-Prep.md`** — dedicated crew creation + table-culture-reset session. Assumes PCs arrive made; spends the time on crew, expectations, system orientation, and the opening montage. Paced minute-by-minute for a first-time-Blades GM.
- **The bible's Session 1 has been split across two real sessions** (Heist 1 in `Session-01-Prep.md`, Heist 2 + Subway reveal in `Session-02-Prep.md`) so the rules and the moral weight don't compete for attention on the first night.
- **All session prep files include expanded mid-scene read-alouds** beyond what the bible provides — trad players are conditioned to expect boxed text.

## House rules baked into this folder

These are the Shadow Exchange specifics — see `00-Canon/Tone-and-Style.md` for the longer tonal reference.

- **Anchor Items carry moral weight.** Every seizure goes in the ledger with the victim's name. Surface the human cost before pricing the loot.
- **Three-Layer Rule.** Every monster has (1) what it appears to be, (2) what it actually is, (3) why it became that. The NPC and Three-Layer-Monster templates enforce this.
- **The Cover-Up is sacred.** Public exposure ends careers and licenses. Frame complications around exposure risk often.
- **The Omen Clock is GM-secret.** Players see symptoms, not segments.
- **The Subway is a mystery, not a feature.** Its `Mysteries.md` accumulates hypotheses; nothing gets resolved without an explicit canon update.
