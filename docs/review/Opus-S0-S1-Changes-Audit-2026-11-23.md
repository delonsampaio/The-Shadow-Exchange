# Opus audit: Session 0 / Session 1 changes (2026-11-22/23)

Report only. No existing file was edited. `python3 -I docs/tools/consistency_check.py` prints **CLEAN** (it does not catch any item below). Line numbers are from the files as of 2026-11-23.

## BLOCKER
None. Both sessions can be run as written. The HIGH items below would make the GM improvise or apply a wrong rule mid-session.

## HIGH

**H1. Gang Trouble cost is invented and names the wrong faction** — `05-Sessions/Session-01-Prep.md:526`
> "🔒 *Cost (SRD Gang Trouble): pay **1 Coin**, or accept **−1 status** with Castellan Retrieval (floor −2); if they do neither, the trouble returns next session.*"

Why: the line is labelled SRD, but the SRD (`Blades-in-the-Dark-SRD.md:2096`) and `07-Clocks/Heat-and-Entanglements.md:26` both say: "lose face (forfeit rep equal to your Tier +1), make an example of one of the gang members, or face reprisals from the wronged party". Castellan has nothing to do with Gerald eating Greta's form; the wronged party is Greta (the Ministry). House-Rules A2 says Entanglements follow the SRD exactly.
Fix: replace with "🔒 *Ways out (SRD): lose face (Rep −1 at Tier 0), make an example of Gerald (no treats; Gerald is devastated), or face reprisals from Greta (an extra form; Audit tick, silent).*"

**H2. Gerald's fate is never spoken at the table, and Beat 7 sends him to the wrong place** — `Session-01-Prep.md:410`, `:412`, `:447`
- `:410` (inside the SAY italics, after the closing quote): "(Whichever they choose, it happens after the debrief; Gerald stays on his stool until then.)". The GM may read it aloud. "On his stool" is also wrong: at `:359` "Gerald, who has followed the three of you down the corridor" and at `:367` he is in the wings pulling the lever, so he is up on the stage, not on the basement stool.
- `:412` says Thorne says "the Ministry will collect the dog in the morning", but Beat 8 (`:426-446`) has no 🗣 SAY for that line.
- `:447` "*(Then carry out Gerald's fate: the Ministry collects him in the morning, you drive him to Pruitt's, or he rides in the van.)*" is a parenthetical on a PAUSE line. There is no READ ALOUD for any branch, and the Return branch's "cover story" question is never asked. Boot §3 says to "turn any 'mention in passing' instruction into a ready-to-say line".

Fix: (a) in `:410`, move the parenthetical into a 🔒 line and change "stays on his stool" to "stays with you". (b) In Beat 8, before the wrap-up SAY, add "→ **If Gerald goes to the Ministry:** 🗣 SAY (Thorne, easy) 'The Ministry will collect the dog in the morning. Leave him with the night man.'" (c) After `:447`, add one 🔊 line per branch: Ministry, "Gerald stays behind on his stool and waves at you with both hands."; Return, a drive to Pruitt's with a ❓ ASK "What do you tell the staff?" ⏸ (this is where Heat +1 comes from); Keep, "Gerald climbs into the van and takes the passenger seat."

## MEDIUM

**M1. The Heat SAY says the GM already rolled, but the roll comes after it; it also has the GM speak about himself in the third person** — `Session-01-Prep.md:481-482`
> "The GM has also rolled for the trouble that follows you home; you'll meet it shortly."

The instruction "**Ask the GM to roll** the Entanglement dice" is at `:482`, after this SAY. The GM reads the SAY, so "The GM has" is himself. Mock-1 fix 12 asked for "I've also rolled". Step 1's opening SAY (`:479`) already uses "I roll".
Fix: put the ENTANGLEMENT 🔒 block before the SAY, and change the sentence to "I've also rolled for the trouble that follows you home; you'll meet it shortly."

**M2. Greta's block contradicts itself about which Entanglements she delivers, and would put a ghost into her comedy scene** — `Session-01-Prep.md:512` vs `:527-528`
> `:512` "Greta delivers the **held Entanglement** in person (if it is a Ministry row) in her own words; other rows play right after this beat."
> `:528` "**Any other row:** read the matching cue … with Greta saying it to their faces."

Rivals (`:527`) and Gang Trouble (`:526`) are not Ministry rows, yet Greta delivers them. `:528` would have Greta deliver Unquiet Dead (possible at Heat 0–3 on a 4–5 if Merton died). That breaks the Menace Rule, because Greta is a 🟡 comedy beat.
Fix: in `:512`, write "Ministry rows, Rivals and Gang Trouble: Greta delivers them. **Unquiet Dead** plays after she leaves, as its own 🔴 beat (no jokes)." In `:528`, add "(except Unquiet Dead)".

**M3. Beat 9's new lead-in contradicts the GM note on what Mara sees** — `Session-01-Prep.md:457` vs `:462`
> `:457` "You go out through the stage door into the alley … She sees *something* — a shape on the far side of the stage-door glass"
> `:462` "the shape she sees through the stage-door glass is the crew itself"

Once the crew is in the alley, it is on her side of the glass.
Fix: change `:457` to "You reach the stage door. Through its glass, the alley, the rain thinner now. A woman … looks up, through the glass, at you." Alternatively, rewrite `:462` to say what the shape is.

**M4. Two images are told to fire in the middle of a read-aloud, with no stop for the Co-GM to fire them**
- `Session-01-Prep.md:195`: "[IMAGE CUE: location-fairground-theater.png] … fire it as you start this second paragraph". It sits inside one READ ALOUD with no ⏸.
- `Session-00-Prep.md:256`: "item-hunters-journal.png … fire it with the Journal paragraph". This is inside PART 5, also one block.

Cue Grammar §2 says "A cue that changes mid-beat gets its own pause". The Co-GM only acts between responses.
Fix: split each read-aloud at that paragraph with "⏸ PAUSE — 'go' for the next paragraph", and put the image cue right after the pause, marked *(inline)*.

**M5. Run Sheet D shows a different image from the Downtime beat; the Close cue has stale wording**
- `Session-01-Prep.md:37`: Run Sheet D is "`location-curios-exterior` → `npc-greta-fenn`". The body (`:471`) is "**[IMAGE CUE: location-curios-interior.png]** ✅ *(caption "Downtime" …)*".
- `:537`: "*(or `location-curios-interior` once it exists; clears Greta)*". The interior image exists (ASSET-TODO:52), so "once it exists" is stale.

Fix: change Run Sheet D to `location-curios-interior` → `npc-greta-fenn`, and delete "or … once it exists" at `:537` (or decide that Close uses the interior image).

**M6. Stale "third-floor light" in the stall menu** — `Session-01-Prep.md:158`
> "*"check the fire escape and the third-floor light"*"

The window line is now a cyan basement glow (`:197`).
Fix: "*"check the fire escape and that cyan basement window"*".

**M7. Session 1 never produces the Trophy Wall entry that the Crew Sheet promises** — `01-Crew/Crew-Sheet.md:52` "Merton, a Barghest, is the first after Session 1."; `Session-00-Prep.md:274` "after the **first hunt of a new monster type**, someone photographs it"

The Session 1 prep has no photo step, and the camera is not in the Load SAY (`:134`) or the wrap (`:547`). It is also unresolved whether a spared or mended Merton counts as "hunted".
Fix: add to the Session 1 wrap (`:547`): "Trophy Wall: if anyone photographed Merton (ask once: ❓ 'Did anyone take a polaroid for the board?' ⏸), add Barghest to the crew file and the `trophy` gag." Then decide whether a spared monster counts.

**M8. The kept-Biological spoilage rule disagrees across files, and "bring one" can start an untaught clock**
- `01-Crew/Crew-Sheet.md:49`: "a Biological keeps ticking Spoilage, twice per scene while away"
- `00-Canon/Campaign-Bible-Appendix.md:33`: "3-seg Spoilage Clock, ticks each Downtime; ticks twice per scene on Away Jobs" (Away Job means out of town, Appendix:50)
- `Session-01-Prep.md:398`: Spoilage is taught at S4 "on the first Biological carried **out** of Cold Storage".

If the crew brings the Barghest Gland on the S2 or S3 score, the Crew Sheet ticks a clock the Ladder defers until S4.
Fix: settle on one rule (suggested: "out of Cold Storage: ticks once per score, twice per scene on an Away Job"), write it in all three files, and add "first time: teach Spoilage (Ladder) even before S4" to the Crew Sheet.

**M9. Downstream files still contradict the new S1 outcomes**
- `06-Scores/Score-01-Merton.md:65`: "Return the collar. No payout. No credit." But S1 now gives Rep +2 (`:476`).
- `Score-01-Merton.md:55` "Play it Safe … 4 Coin, 0 Heat.": the S1 Heat line (`:480`) can never give 0 (the base is at least 0, plus 1 for a well-connected target).
- `03-NPCs/Active/Gerald.md:35` "Returned to Pruitt | … Detection +1": S1 says **Heat +1** (`:412`, `:480`). Detection is over by then.
- `Gerald.md:34` "Ministry pickup (Form 47-B(ii))": S1 `:410` and `:412` use plain **47-B** for the Ministry and 47-B(ii) for Keep.

Fix: update these four cells, and add "No payout. No credit." and "Detection +1; cover story" to `docs/tools/stale-phrases.txt`.

**M10. The Gerald "dogs know" beat is now unconditional and not tracked as a tell** — `Session-01-Prep.md:431`
> "Gerald's tail wags at the sight of a man he has never met. Then he whines and goes behind the nearest of you."

It is canon (Secrets #1 route d), and `:257` gives it cover ("slightly afraid of whoever looks most like the Ministry"). But it lands in the same scene as Tells 1 and 2, in front of players with 20+ years of experience. "a man he has never met" spells out the oddity. The dashboard note at `:443` logs only Tells 1 and 2.
Fix: cut "at the sight of a man he has never met" (it would read "Gerald's tail wags. Then he whines …"). Add to `:443`: "Gerald hiding = Secrets #1 route (d): push `tell` id `gerald` state 1." Add "(skip if Gerald is dead: Lethal-Path table)", because "always" breaks the kill-Gerald path.

**M11. Menu B "keep the collar off the books" never says what happens to Merton** — `Session-01-Prep.md:396`, `:402-405`

The Anchor Cover Rule (House-Rules D) says he keeps his human cover only while the Anchor is intact and present. Menu B gives Merton's fate only for the hand-in path ("gone within a few hours"). `Crew-Sheet.md:47` ("Leverage only: the Twice-Born owe a Favor for sparing it") does not fit a kept Anchor whose owner is left without it.
Fix: add a result line, e.g. "Keep/file nothing (collar not mended): Merton is gone within 1d6 hours unless it is mended and returned; Twice-Born −1 if they hear." Then reword the Crew-Sheet Anchor cell.

**M12. Session-Writing-Rules still teaches the old way of narrating player actions** — `00-Canon/Session-Writing-Rules.md:30`
> "Narrate what the player did ("Odette feeds the coins in, one after another …")"

This contradicts the Boot voice rule ("never narrate what they do, say or feel") and the new impersonal Zoltar read-aloud. Future preps will bring the old pattern back.
Fix: replace the example with "The coins go into the slot, one after another — [the code]" and "outcomes follow the table's stated action".

## LOW

- **L1** `Session-01-Prep.md:525`: The Usual Suspects goes "❓ ASK THE TABLE … then 🗣 SAY 'Pay one Coin, or we see what they say.' ⏸". That is two prompts with only one stop, which breaks the one-question rule. Also "Before the forms." comes after she has already produced Form 47-B (`:523`). Fix: add ⏸ after the ASK, and change it to "One more thing."
- **L2** `:523`: there is no ⏸ REACTION STOP after Greta's "I need two signatures" line, but `:524` says to wait for "the crew's reply". Fix: add ⏸.
- **L3** `:484`: "6 Cooperation lapses … 🔊 'A quiet night: nobody comes calling.'". Greta then walks in. Fix: "A quiet week: nobody comes calling, apart from the one person who always does."
- **L4** `:527`: Rivals has no cost, and Harrow may already be at −2 from creation (the SRD says a *neutral* faction). Fix: 🔒 "Forfeit 1 Rep or 1 Coin (Harrow is Tier I), or stand up and lose 1 status (floor −2 does not apply after creation; −3 = war). If Harrow is negative, use Meridian or Castellan, whichever is at 0."
- **L5** `:504`: "otherwise an NPC healer of quality 2". The SRD (`:2190`) needs a contact or PC who can treat, or else Acquire Asset (deferred tonight). Fix: "if a Friend or contact can treat (ask), quality 2; otherwise tough it out (1 Stress, 0d)".
- **L6** `:266`: if Bernard already ticked Detection and ran the clock SAY (`:226`), Gerald's beat teaches "That's a **clock**" a second time. Fix: "(if Bernard already taught it: 🗣 'Detection ticks to two.')".
- **L7** `:264` vs `:267-268`: "calm Gerald" has two result tables: 2b, the leather clue, and 2c, befriending. Fix: in 2b, write "Study or Hunt" only, and in 2c, "calm, talk to or befriend".
- **L8** `:426`: "He arrives as the Surge ends" is stale. He now arrives after the Choice. Fix: "He arrives after the Choice".
- **L9** `:526`: "Gerald, on his stool" happens in the shop, but the stool is in the theater basement. Fix: "Gerald, on the shop's good armchair".
- **L10** `:404`: the mend gives Position but no Effect. Also, if the crew mended during the Surge (`:346` "Merton walks"), Beat 7 does not say to skip the Mend roll while still applying Twice-Born +1 and +1 Favor. Fix: add "Effect Standard", plus "(already mended in the Surge: no roll; apply the Returned results)".
- **L11** `:468`: the Downtime SAY comes before the Downtime music and image cue (`:470-471`). Fix: move the cues above the SAY.
- **L12** `:52` and `:55`: the Cold Open fallback says "Consequence has not moved from the counter" (S0 lets the table put her anywhere). Under the fallback, the "Remember" bullets stay unfilled placeholders. Fix: "Consequence has not moved." and "(fallback: skip Remember)".
- **L13** `:122`: "Anything unusual you find down there", before anyone knows about a basement. Fix: "in there".
- **L14** `:212` and `:72`: the theater is closed and in probate, yet Gerald "is boarded most nights" there. Fix: one 🔒 clause, e.g. "Pruitt pays Merton under the table to mind him."
- **L15** `Session-00-Prep.md:421`: the 6 result reads "The journal is back on the shelf". The page says not to shelve it where customers can see. Fix: "back under the counter".
- **L16** `S0:178`: the "ZOLTAR JUDGES YOU" banner sits on the label line, so it fires before the joke. Fix: put it after "Zoltar looks very disappointed in you."
- **L17** `S0:350` "Floor, no stacking" and `House-Rules.md:27`: the −2 floor is a deviation from the SRD, which has no floor, and it is missing from House-Rules A/A2 (only Boot §2b and S0 state it). "No stacking" is misleading, because stacking down to −2 is allowed. Fix: add "faction floor −2 at creation" to House-Rules A2, and change "no stacking" to "stack down to −2, never below".
- **L18** `02-Factions/Faction-Tracker.md:26`: "set the weak firms' standings (… Meridian Group, Hunter Underground)". Meridian is Tier II and strong, and the Hunter Underground is not a firm. Fix: "the four firms and the Underground".
- **L19** `S0:489-491`: the after-session list leaves out the Trophy Wall type (3e) and the favourite contact. Fix: add both.
- **L20** `11-Visuals/ASSET-TODO.md:65`: "**Not wired into `Session-01-Prep.md` yet (held until mock 1 ends)**" is stale, since the lobby is now wired (S1:207). Fix: change it to "Wired 2026-11-22".
- **L21** `Crew-Sheet.md:45`: "Barghest Gland +1d on one Prowess roll". The SRD has no "Prowess roll" (Prowess is a resistance attribute). Fix: "+1d on one Finesse, Prowl, Skirmish or Wreck roll".
- **L22** `08-Loot-and-Anchors/Inventory.md:33`: "* ## Notable Items (Mundane)" is broken markdown (pre-existing).
- **L23** `05-Sessions/Campaign-Arc.md:57`: "Merton's dog Gerald". Gerald is Pruitt's dog. Fix: "Pruitt's dog Gerald".

## Checks A–H, condensed
- **A (Gerald branches):** he is present at Thorne in all branches (`:431`). The Greta "if Gerald is present" line (`:530`) is correct for Keep only. Gang Trouble is gated to Keep (`:484-485`). Heat +1 is gated to Return (`:480`). Problems: H2, M9, M10, L9.
- **B (Downtime):** the order Payoff (`:473`) → Heat SAY → Entanglement held → Vice → activities → Double Bookkeeping → Greta matches the SRD, and the numbers are said aloud. The Heat arithmetic in `:480` uses H&E §1 bases and the +2 for a death once, and the Wanted/9 rule matches House-Rules A2. The house extras (+1 staff saw Gerald, +2 file nothing) are S1-specific and consistent with `:412`. Problems: M1, M2, L1-L3.
- **C (voice and labels):** every new READ ALOUD (S0:136-140, 182, 190, 406-409; S1:52, 197, 222, 224, 267-268, 359, 407, 431, 446, 457, 526) is second person, present tense, with no "the crew" or "the hunters". `S1:457` "You go out through the stage door" narrates the move after a "go"; acceptable but see M3. Label problems: L1, L2, H2.
- **D (spoilers):** the Thorne exit (`:445-446`), Bernard's probate line (`:222`, Bernard.md:15) and the theater canon (`:212`) leak nothing. No Audit, Kress, Architect, Subway or Stalls in new player-facing text. The Double Bookkeeping SAY hides the kept item (`:476`). Watch item: M10.
- **E (SRD):** see "Verified clean" below for what is correct. Problems: H1, L4, L5, L17, L21.
- **F (cues):** every IMAGE/MUSIC name in S0 and S1 exists in `_Saved-Images` / `_Saved-Music` (checked with find). The only missing file is `music-sting-fortune-card`, which is correctly conditional ("only if the file exists"). Mismatches: M4, M5.
- **G (leftovers):** grep finds no "honest, effective", "tea importer" or "[Name] feeds the coins" in S0/S1. "Roll it yourself" is gone. "one is filled" now reads "[one is / two are …]". Remaining: M6 ("third-floor light"), M9 ("No credit" in Score-01-Merton), M12 (Writing-Rules example), M5 ("once it exists"), L20.

## Verified clean
- S0:290 reputation list = SRD:1500 (Ambitious, Brutal, Daring, Honorable, Professional, Savvy, Subtle, Strange), flagged as a flavour label, not the Rep number.
- S0:350 upgrades +1 / −2 (coin options unavailable at 0 Coin) = SRD:1512-1513. S0:352 hunting ground "pay nothing, −1" = SRD:1362-1363 and 1507. S0:367 favourite contact +1 / −1 (optional ±2) = SRD:1517-1520.
- S0:424-427 resistance: decide first, then roll. The attribute rating = the number of actions with at least one dot, and zero = two dice keep lowest. S0:430: Stress = 6 − highest die; ninth box → Trauma, in one clause. S0:419 "how many dots" question is present. S0:433: Assist deferred to S2 (matches Ladder S2); Mechanics Taught states set.
- S0:146 banner "NO WITHDRAWALS"; S0:178 "ZOLTAR JUDGES YOU"; S0:182 and 190 Zoltar read-alouds are impersonal; S0:206 and 245 ASK breaks inside the tour read-alouds each have a REACTION STOP.
- S0:118 and 126 geography (Old City walled, far west; glass towers let through the wall) fit Living-Map (walled core) and Gazetteer (West Gate / Westwall Terminal, East Gate Bridge to the Fairground).
- S0 time budget adds up to 2 h 40 with the Trial Run at 25 min. S1 adds up to about 3 h 00.
- S0:274 Trophy Wall camera rule matches Appendix:19, Crew-Sheet:51-52, Curios-and-Chronicles:82 and Hunter-Kit:21.
- Kept items: Crew-Sheet:45-49, Appendix:33 and Inventory:29 agree on one-use Biologicals, a Relic once per score with Resonance +1, Anchors never sold, and one per score (apart from the spoilage wording, M8).
- S1:197 cyan basement glow, S1:207 lobby on "go", S1:301 corridor image only if the collar is untouched (matches Run Sheet:32), S1:364 aftermath music (matches Run Sheet:33), S1:365 Surge stops once held, soothed or down.
- S1:265 Devil's Bargain wording is the SRD. S1:262 Study or Hunt are both Insight. S1:267 6 and 4–5 result text matches Mock-1 fix 6.
- S1:404 mend at Risky (Desperate if severed), with three result lines and Twice-Born +1 standing and +1 Favor. With the Twice-Born at 0 (Faction-Tracker:17), Cooperation correctly lapses at S1.
- S1:482 Entanglement dice (Wanted 0 → two dice, keep lowest; the GM rolls) = House-Rules A2, H&E §2, Boot §5. S1:504 Recover clock, Reduce Heat, Train once per track, extra activities 1 Coin or Rep = SRD. S1:490 Vice = lowest attribute.
- S1:476 and 481: payoff and Heat are said aloud, and `crew: {heat, coin, rep}` is set. Dashboard gag ids `firms`, `promises`, `rent`, `trophy`, `crewdef` exist (GM-Dashboard.html:121-135).
- The Thorne exit and Beat 9 lead-in are present (S1:445-447). The Cold Open fallback is present (S1:52).

## Counts
BLOCKER 0 · HIGH 2 · MEDIUM 12 · LOW 23
