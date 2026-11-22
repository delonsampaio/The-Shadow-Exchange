---
entity_type: Procedure
status: ADOPTED 2026-11-20 — the single rule for "something changed, so everything that mentions it changes"
purpose: "Every kind of change → what to do DURING the session → every file to update AFTER, in order. Nothing is stale until this map has been run and the check script is clean."
---

# Change Propagation Map

**The rule.** Nothing is "done" until (1) it was written to the **Live Ledger** at the moment it happened, (2) each file in its row below was updated, and (3) `python3 -I docs/tools/consistency_check.py` prints **CLEAN**. Mock sessions write nothing (no ledger, no files).

## 1. During the session (every change, at the moment it happens)
1. **Dashboard feed:** push the op (`push.sh`, Session-Boot §2b). 2. **Chat:** print `[Change: …]`. 3. **Live Ledger:** append one line to `05-Sessions/Live-Ledger.md`: `S<N> · beat · change · files-to-touch-after`. The ledger is what survives a context reset (Boot §1 step 3b) and what the end-of-session pass reads.
4. If the change is a **canon decision or ruling** (the GM changes a fact), do the **Canon Change** row at once, not at the end.

## 2. After the session — the map (work down the ledger; one row per change)
| What changed | Update these files, in this order |
|---|---|
| **Beat / where we stopped** | `05-Sessions/Campaign-Current-State.md` (starting room for next time) |
| **Heat / Coin / Rep / Wanted / Tier / hold** | `01-Crew/Crew-Sheet.md` · `Campaign-Current-State.md` · dashboard `INIT_*` + bump `SAVE_VERSION` · (Tier change: check Season-1-Plan §7 Tier targets) |
| **Clock ticked or filled** (Detection, Surge, Spoilage, Subway, Omen, Audit, Corruption, faction) | `07-Clocks/Active-Clocks.md` · `07-Clocks/Clock-History.md` · `07-Clocks/Clocks-Calendar.md` · dashboard `clock` · check caps (**Decay ≤ 3 in Season 1**; Omen pacing in Season-1-Plan §1) · Express Ending Kit §6 envelope if a mid-arc climax · players' site only if the clock is public (Wiki protocol) |
| **PC created / changed** | `01-Crew/PCs/<name>.md` · `Crew-Sheet.md` · `01-Crew/Contacts.md` (Friend/Rival) · players' site `The-Crew` / Known-Contacts (no Heirloom pattern) · `NPC-Index` if a Friend/Rival is new |
| **Stress / harm / trauma / XP** | PC file · `00-Canon/End-of-Session-Ritual.md` §1 XP tally · advancement note |
| **Heirloom pattern or stage** | PC file · `00-Canon/Heirloom-Degradation-Patterns.md` (GM-private) · Express Kit envelope line 4 · Season-1-Plan §7 (stage targets) · dashboard `pcinfo` |
| **NPC met / new** | `03-NPCs/NPC-Index.md` (Met = Y, last seen) · NPC file (if from the bench: move the card to `03-NPCs/Active/` and mark the bench row) · `09-Threads/Plot-Threads.md` · players' site Known-Contacts (spoiler-checked) · dashboard `npc_add` |
| **NPC dead / left / turned** | `NPC-Index` status · the NPC file status · `05-Sessions/Season-1-Plan.md` §4 (mark the planned death executed or changed) · `02-Factions/Faction-Tracker.md` · Known-Contacts (deceased) · Express Kit envelope · a **stale phrase** for "alive" wording (see Canon Change) |
| **Anchor taken / returned / refused / destroyed** | `08-Loot-and-Anchors/Anchor-Ledger.md` · `Inventory.md` · `02-Factions/Faction-Tracker.md` (standing) · players' site `The-Anchor-Ledger` · Twice-Born Favor in Crew-Sheet · dashboard anchor ops |
| **A real night ends** | `05-Sessions/Night-Log.md` (one row; no clock) |
| **NPC dies / leaves / is replaced** | `03-NPCs/NPC-Index.md` · `03-NPCs/Season-1B-Cast-Cards.md` · `03-NPCs/Wall-of-the-Missing-Roster.md` · `02-Factions/Ministry-Org-Chart.md` |
| **Faction clock ticked** (non-Apex) | `07-Clocks/Faction-Clocks.md` · `07-Clocks/Clock-History.md` |
| **Thorne tell planted / caught** | `09-Threads/Foreshadowing.md` · `09-Threads/Secrets-and-Reveals-Schedule.md` · `Campaign-Arc.md` §5 (state) · `03-NPCs/Active/Elias-Thorne.md` · dashboard `tell` |
| **Mechanic taught / understood** | `05-Sessions/Campaign-Current-State.md` (taught list) · check `Mechanics-Teaching-Ladder.md` order |
| **Table-invented canon** (nickname, coin code, cover story, lease theory…) | `09-Threads/Plot-Threads.md` (table canon) · `Campaign-Current-State.md` · `_Dictionary.md` if it is a term · dashboard `gag` |
| **Score played / skipped** | `06-Scores/Score-Catalog.md` (PLAYED / SKIPPED, dread, what the table did) · `Bounty-Board.md` (next lead) · `Season-1-Plan.md` (note any deviation on that row) · `Zoltar-Card-Deck.md` (mark the card USED) · if it was a bestiary creature, note it in Score-Catalog §F |
| **Faction moved / standing changed** | `02-Factions/Faction-Tracker.md` · that faction's file · `Faction-Turn-Procedure.md` (Apex clock segment) |
| **Location new / changed** | `04-Locations/*` file · `City-Districts.md` · `11-Visuals/Living-Map.md` (ledger and pins) · `File-Index.md` |
| **Image, music or other asset made** | `11-Visuals/ASSET-TODO.md` · `Session-Image-Log.md` · `docs/Manual-Work-Queue.md` (tick) · the prep's Run Sheet (❌ → ✅) |
| **New file created or renamed** | `00-Canon/File-Index.md` · if an NPC → `NPC-Index.md` |
| **New term, rule or procedure** | `00-Canon/_Dictionary.md` · `House-Rules.md` (if table procedure) · `Session-Boot.md` (if a Co-GM command or boot step) |
| **Recap and players' site** | `00-Canon/Wiki-Update-Protocol.md` (the whole protocol; strict build; spoiler sweep; push only when the GM says "push") |
| **CANON CHANGE (a GM ruling that changes a fact)** | 1. Fix **every** file that states the old fact (grep the old wording). 2. Add the old wording to `docs/tools/stale-phrases.txt`. 3. Add any new secret to `docs/tools/spoiler-words.txt` if it must stay off the players' site. 4. Log it in `docs/review/Canon-Change-Log-<date>.md`. 5. Update `_Dictionary.md` and, if procedure, `House-Rules.md`/`Session-Boot.md`. 6. Update the players' site if the fact is player-facing. 7. Express Kit envelope and Season-1-Plan if it moves a target. |

## 3. Close-out (always last)
1. Run `python3 -I docs/tools/consistency_check.py`. It checks: every referenced file exists · every NPC file is in the NPC Index · every canon file is in the File Index · no retired phrase remains · no secret word is on the players' site. **Fix everything it reports.** (A file named in the docs that is deliberately not created yet goes in the script's `PLANNED` list; remove it when the file exists.)
2. Say, in one line each: what you updated, what the check said, and what is **NOT PUSHED**.
3. Clear `05-Sessions/Live-Ledger.md` back to its header (the lines are now in the files). Reset `scene.js` and `feed.js` (Boot §6 step 6).
4. A fact that you cannot place in this map is a gap in the map: add a row to it now.
