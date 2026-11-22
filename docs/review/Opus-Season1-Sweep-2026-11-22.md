# Opus Season 1 Sweep: S4+ plan files vs the 2026-11-22 rulings

Report only; every cited line was read.

## BLOCKER

**B1. Three files still let Kress be named before S7.** `Campaign-Arc.md:55` says "The *name* may surface S3–S4 (Stalls)". `Secrets-and-Reveals-Schedule.md:23` gives the first clue as "S3–4 (Stalls's papers)". `NPC-Index.md:38` says "S3–S4 name only". `Venues-Bank.md:183` says Bramwell may show the letterhead "allowed from S4+ per Campaign-Arc §3". In S4 Stalls is unmasked, and `Renwick-Stalls.md:30` says he "knows the name Kress". An S4 writer will have him say it. *Fix:* in all four places, write "Name on screen S7 (binder letterhead), never earlier; Stalls says only 'my investor's people at the Ministry'". Also add `Kress.{0,20}S3.?.?S?4` to `docs/tools/stale-phrases.txt`.

**B2. Nothing in the files gets the word "Architect" to the table by S4.** `Season-1-Plan.md:42`, `Secrets…:26` and `:53` all assume the word surfaces in S4 "through Harlan". But Harlan only *reacts* to the word ("Where'd you hear that name?", `Harlan-Okafor.md:34`), the trigger needs a Long-Term Project (`Campaign-Arc.md:72`), and the red-ink entry has no text (`Session-00-Prep.md:258`, `Curios-and-Chronicles.md:83`). No player has seen the word. *Fix:* GM decides the route (Readiness 3); write it into `Curios-and-Chronicles.md:83` and Arc §4.

## HIGH

**H1. The session template and the writing rules predate the rulings.** `_Session-Template.md:6` still says `runtime: "~3 hours"`. It has no score block, no downtime and no close. Its "After this session" section (`:54–55`) has no Zoltar card, no XP, no retrospective and no Pause. The checklist at `Session-Writing-Rules.md:73–88` (last updated 2026-11-18) never asks for a Payoff, Heat, the Entanglement, the fight-to-kill block or stall help. *Fix:* set `runtime: "one or more sittings"`. Add template blocks in order: Payoff (Coin N · Rep 2 ± tier) → `🔒 HEAT (the single rule)` from `Heat-and-Entanglements.md:10` → Entanglement (Wanted dice; Wanted 0 = two dice, keep lowest) → `🔒 IF THEY FIGHT TO KILL` → Downtime → Close (Zoltar → PC and crew XP, card 22 if a track fills → retrospective) → Pause (Ritual §0b). Add the same to the §10 checklist.

**H2. The score template and the catalog cannot produce a Payoff.** `_Score-Template.md:45–49` ("Loot on offer") has Coin but no Rep, no Heat, no Entanglement and no kill path. Lines `:32–33` are broken (two bullets run together with a header). `Score-Catalog.md:14` has no target-Tier or payout column, and the Rep math needs the target's Tier (SRD `:796`). *Fix:* add "Target Tier · Payout · Rep" columns to the catalog. Add Payoff, Heat and kill-path sections to the template and repair `:32–33`.

**H3. The Subway reference still shows the S6 red ink on the first visit.** `The-Subway/Stations.md:28` (the read-aloud) and `:44` both say "one of them is marked in red ink that looks newer". Canon in `Session-02-Prep.md:371,383` is a faint pencil line, and the red ink starts at S6. Every S4+ Subway visit will be written from Stations.md. *Fix:* "drawn in faint pencil that looks newer than the rest (red ink appears only when Decay goes live, S6)."

**H4. The Broker breaks the Wanted rule.** `Crossroads-Broker.md:25` offers "Lower the crew's Wanted level by 1, instantly." Under the ruling, only incarceration lowers Wanted. *Fix:* "Someone the crew names is convicted for the crew's crimes before the week is out (Wanted −1, Heat clears, SRD); the Broker's price is on top."

**H5. Reyes's trigger can fire in S4.** `Campaign-Arc.md:37` says "Session 6, or after two Returned/Refused Anchors". S1–S3 offer three such choices (collar returned, Emmerich warned, Mabel told or left), so Reyes could arrive in an S4 that is already overloaded. *Fix:* "Session 6; two Returned/Refused Anchors may bring her to S5, never S4." Also update `Deputy-Director-Reyes.md:7`, which still says "TBD".

**H6. There is no procedure for writing the next prep (E).** Boot §1 step 3a (`Session-Boot.md:19`) offers only an Evergreen episode. `Weekly-Prep-Checklist.md:18` assumes the file exists. `Night-Log.md:20` covers sizing only. *Fix:* add a "Writing the next prep" section to `Session-Writing-Rules.md`. Inputs: the last Night Log row (beats per sitting, feel); `Campaign-Current-State` and the confirmed snapshot; the prior prep's "leaves with" list; the Faction Turn result; session N's rows in `Season-1-Plan` §2, `Secrets` §B, `Clocks-Calendar` and `Ladder-S4-Plus`; the NPC files. Then list the GM's decisions, write every past choice as a branch, mark safe stops, and keep new lessons to four or fewer.

**H7. The boot state file is missing the values S4 needs.** `Campaign-Current-State.md:19–23` has no Wanted, faction standings, Twice-Born Favor, cohort (Gerald), XP or crew upgrades. It still counts "Thorne tells caught: 0/6" against the nine tells in `Campaign-Arc.md:80`. *Fix:* add those fields and change the count to 0/9.

**H8. The Gland's Spoilage cannot work as the plan describes.** `Session-01-Prep.md:391` stores a kept Gland in "the shop's cold cellar until Session 4". `Session-02-Prep.md:56` calls the same place "runed cold drawers". But the Cold Storage Locker is a Containment Suite fixture from S0 (`Crew-Sheet.md:31`), and it *pauses* Spoilage (`Active-Clocks.md:30`). So `Ladder-S4-Plus.md:14,26` and `Season-1-Plan.md:40` ("first Biological begins to rot") cannot fire from the Gland. *Fix:* the GM decides (Readiness 4), then the files use one name: Cold Storage Locker.

## MEDIUM

**M1. The Faction Turn can run twice.** `Faction-Turn-Procedure.md:7` says "after every session" (→ "every finished session, never after a Pause"), and `Evergreen-Episodes.md:28` runs another *before* the night. *Fix:* delete Evergreen step 2.

**M2. The Clocks Calendar repeats old Heat values.** `Clocks-Calendar.md:32` ("+0 (Ministry), +2 (file nothing)") and `:34` ("+0/+1/+2") contradict the single Heat lines at `Session-01-Prep.md:466` and `Session-03-Prep.md:404`. *Fix:* "Heat: per the prep's single Heat line."

**M3. The old score files contradict the preps.** `Score-01-Merton.md:57,61` ("0 Heat", "+2 Heat") and `Score-02-Emmerich.md:51–55` (no Rep) would be copied into a Score-04. *Fix:* head both "Superseded by the prep's Payoff/Heat lines."

**M4. The no-prep score drops steps.** `Improv-Kit.md:112` ("Out") has no Rep, no Entanglement and no XP, and its Heat omits the kill (+2) and well-connected (+1) terms. Twist 4 at `:110` plants the Mimic's paper trail, which `Evergreen-Episodes.md:9` forbids on an evergreen night. *Fix:* add "Rep 2 ± tier; Heat per `Heat-and-Entanglements` §1; Entanglement; finished-session close". Replace twist 4.

**M5. The teaching ladders conflict with "nothing is skipped".** `Mechanics-Teaching-Ladder.md:31` teaches "Harm levels" at S4+, but harm can happen from S1 (card 16, "just in time"). `Ladder-S4-Plus.md:67` says "do not teach another that session", which would *defer* a lesson that is due. `Mechanics-Teaching-Ladder.md:138` says to "skip stress math". *Fix:* Harm is taught the first time it is taken. If more than four lessons fall due in one session, teach the extra one at the next session's first use, and log it. Replace "skip stress math" with "repeat the card next session".

**M6. Two files disagree on when Stalls is exposed.** Apex Push segment 2 is "S7: Stalls Holdings exposed" (`Faction-Turn-Procedure.md:20`). But Stalls = Apex is revealed in S4 (`Secrets…:22`, `Renwick-Stalls.md:21`). *Fix:* segment 1 becomes "S4 sweep + Stalls unmasked"; segment 2 becomes "S7 the binder/choice".

**M7. What Aldric does from S4 is not defined.** `Season-1-Plan.md:128`, `Clocks-Calendar.md:35` and `Secrets…:32,53` all say "AM fragments from S4". `Venues-Bank.md:14` says static only from S4 and voice after S9. Yet S0 already plays the voice (`Session-00-Prep.md:236–244`). Separately, `Urban-Legends.md:39`, the S9 default lead, carries "It found the frequency", which is an S24+ line. *Fix:* the GM rules on Readiness 7. Gate the Urban-Legends line to S24+.

**M8. S4's Form 44-C breaks the form-number rule.** `Running-Gags-and-Forms-Register.md:78` says "Last number used: 140-A", but no S0–S3 prep uses 140-A. S4's 44-C (`:50`) sits below 47-B, 88-D and 140-A, which breaks `:80` ("strictly ascending … higher or stranger"). *Fix:* mark 44-C, 47-B, 22-A, 31 and 88-D as legacy (grandfathered), and set "last used" from the Live Ledger.

**M9. Session = one night.** `Campaign-Arc.md:12` contradicts `Night-Log.md:22`. *Fix:* "Session = one prep file; it may take several sittings."

**M10. Decay is taught at S6, but S6 plans no Subway visit.** The S6 Decay card is shown on the Main Hall map (`Ladder-S4-Plus.md:16,36`; `Clocks-Calendar.md:37`), but S6 *The John Doe* has no visit. *Fix:* plan a visit for S6, or teach card 21 at the first visit after Decay goes live.

**M11. Three files disagree on what Audit 4 does.** `Campaign-Arc.md:67` and `Director-Vance.md:26` give four weeks' notice. `Active-Clocks.md:70` and `Ladder-S4-Plus.md:30` lock the shop at once, and the "pay it down in downtime" mechanic is never defined. *Fix:* pick one outcome and define the pay-down roll.

**M12. Two files give different timing for Kress noticing the crew.** `Campaign-Arc.md:68` says Kress notices within about 2 sessions of a Twice-Born being protected (S2/S3, so by S4–5). `Faction-Clocks.md:14` puts segment 1 at S6. *Fix:* align them, for example "earliest S6".

## LOW

- **L1.** `Secrets…:82` tell-numbering flag is stale (`Score-Catalog.md:27,29` match the Arc): delete.
- **L2.** `Clocks-Calendar.md:39,40,44` and flag 2 at `:74` cite old-spine rows that `Campaign-Arc.md:32` deleted. Delete them.
- **L3.** `Campaign-Arc.md:129` "13-session spine below": delete.
- **L4.** `Mechanics-Teaching-Ladder.md:121` lists card 22 as "XP tally"; it is Advancement.
- **L5.** `Renwick-Stalls.md:5` ("optional … in person") contradicts `:7` ("phone only S3"). Use "phone or in person (S3 meeting)".
- **L6.** Skip-sounding wording: `Score-Catalog.md:11` "SKIPPED" → "NOT CHOSEN"; "optional tells" (`Season-1-Plan.md:14,121`, `Campaign-Arc.md:80,90–92`) → "extra tells (always planted)"; `Evergreen-Episodes.md:14–19` "skip the plant" → "do not plant (spine)"; `Express-Ending-Kit.md:26` "(optional)" → "(wrap it 4)".
- **L7.** `Downtime-Menu.md:33` shows a "D. Kress" letterhead in any downtime. Gate it to S7+.
- **L8.** `Clocks-Calendar.md:60` Audit "reset?": decide.
- **L9.** `Session-Boot.md:200` asks two of `Night-Log.md`'s three questions (`:12`).

## What a fresh Co-GM would get wrong writing S4–S7 (D)

- **Read first:** the H6 inputs, plus Session-Boot and House-Rules.
- **Do not:** name Kress (B1); use red ink before S6 (H3); show the Audit at 0; bring Reyes into S4 (H5); stack five reveals (`Secrets…:53`); teach more than four lessons; copy Heat lines from `Score-01`/`02` or the Calendar.
- **Gap:** S3's "leaves with" list (`Session-03-Prep.md:451–459`) omits Heat, Wanted, Coin, Rep, XP, Tell 5 caught, Stalls met, extra pages read, and Grief Jars sold. Add them.

## S4 readiness: decisions and inputs needed

**Decisions for the GM**
1. **The S4 premise.** How *The Bounty That Wasn't* ties together the Apex sweep, Stalls and the first Biological. Is the "unmasking" a literal Scooby disguise or a confrontation?
2. **The reveal budget** (House-Rules C4: one big reveal per session). Stalls = Apex is the reveal. The Wall, "HE WENT BACK", the V&L photo and the Audit are each played as silence or texture, or one of them moves to S5.
3. **How the word "Architect" arrives** (B2): text added to the red-ink entry, a completed Long-Term Project clock, or Harlan saying it unprompted.
4. **The Gland and Spoilage** (H8): either Cold Storage pauses the Gland (S4's Biological is newly harvested), or the cellar is not Cold Storage and the clock starts in S4.
5. **The Audit in S4:** Form 44-C appears only if Audit ≥ 1. If Audit is 0, the card waits.
6. **The lesson cap.** Candidates: Spoilage, Audit, Harm, advancement (if not yet taught), Trauma and Wanted (if triggered). Which wait (M5)?
7. **Aldric in S4:** static only, or the S0 voice (M7)?
8. **Thorne in S4:** present or not? The ring (Tell 6) is the only tell in play.
9. **Harlan as a known contact:** if a PC took him as a Friend in S0, S4 is a reunion, not a debut (`Harlan-Okafor.md:19`).
10. **Cleaners in S4:** they arrive if Heat ≥ 6 or Apex standing ≤ −2 at the end of S3 (`Campaign-Arc.md:69`).

**Inputs from S3 (confirmed snapshot)**

11. Mabel A/B/C; month-end bonus; C's pending complication; Grief Jars kept or sold; Thomas told (Favor).
12. Stalls met in person? Extra pages read (STALLS HOLDINGS seen)? His "investment opportunity" count.
13. Gland (kept, where), collar, Merton alive, Gerald kept as cohort, Emmerich thimble (seized / warned / partial; warned → the S4–6 second attempt).
14. Twice-Born standing and Favor; Apex, Ministry and rival-firm standings (incl. S0 faction reactions, hunting-grounds rival).
15. Heat, Wanted, Coin, Rep, hold, all XP tracks, Stress, Harm, Trauma; Audit (0–3); Omen (2); tells planted/caught; Mara's stage; Faction Turn result.
16. Night Log rows for S0–S3, to size S4 in beats per sitting and place safe stops.

**Counts:** BLOCKER 2 · HIGH 8 · MEDIUM 12 · LOW 9 · readiness items 16.
