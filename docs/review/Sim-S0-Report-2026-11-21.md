# Simulated Playthrough — Session 0 (2026-11-21)

**Report only.** I ran `05-Sessions/Session-00-Prep.md` beat by beat against Boot §2–§4, House-Rules, the Comedy Playbook, Core (TV policy), the Ladder and classes A–M. I did not open `scene.js` or `feed.js`. I rendered 10 TV states from scratch scenes with `docs/tools/render_player_screen.sh` and looked at each one.

**The table I played:**
- **Dana**, a rules-lawyer, plays Ruth Kessler, a Hound nicknamed "Footnote".
- **Theo**, a comedian, plays Barnaby Quill, a Slide nicknamed "Bad News". Theo fumbled the coin code ("two pennies, a quarter, say 'please, sir'"), claimed Rule Five, and named Greta as his Rival.
- **Ash**, a quiet player, plays Wren Hollis, a Whisper nicknamed "Static". Ash stalled on Wren's Friend and refused the Heirloom.

Theo also opened the vault, plugged Zoltar in and tried to triangulate the AM voice.

**Assets:** every required music and image file exists, and every ❌ file is correctly marked optional. No missing-asset defects.

---

## BLOCKER
None.

## HIGH

**H1 (E). The Trial Run teaches 5–6 mechanics in one beat; Boot rule 8 allows at most 2 per beat and 4 per session.**
- **Where:** `S0:383`, steps `S0:396–411`. It teaches dice, Position, Effect, Stress and Resistance, and the Ladder adds the 12 actions (`Ladder:27`). This breaks `Session-Boot.md:153` and `Ladder:10`.
- **What goes wrong:** Boot outranks the Ladder, so a Co-GM that follows the priority order defers Stress and Resistance. That breaks S1, which says Resistance was "practised in S0" (`S1:8`).
- **Fix:** add an exception to Boot rule 8 and `Ladder:10`: "S0 Trial Run = 4 lessons (dice, Position+Effect, Stress, Resistance), the only beat over 2." Then split 4b at step 5 with a ⏸.

**H2 (L). Crew creation departs from the SRD in ways House-Rules never records.**
- **Where:** `S0:325` gives "one improvement", but the SRD gives two more upgrades (SRD:1381, SRD:1510). Hunting grounds are never asked, yet `S0:463` says to record them and the players' `Session-0-Agenda.md:47` promises them. There is no favourite contact, and the faction reactions are skipped (`S0:339`). Tier 0, weak hold and 0 Coin are never said aloud.
- **What goes wrong:** `CLAUDE.md:22` says the SRD wins, so Dana wins every argument.
- **Fix:** add House-Rules A rows: "S0: one upgrade; hunting grounds = Old City; no contact or faction reactions yet." Add a 🗣 SAY at 3f with the Tier, hold and Coin. Fix `S0:463`.

**H3 (J). Friends, Rivals and Heirlooms have no stall help and no refusal branch.**
- **Where:** `S0:347`, `351`, `357`.
- **What goes wrong:** when Wren stalled, the Co-GM invented names without the NPC-Index check that the Boot "new NPC" command requires. When Ash said "pass" on the Heirloom, nothing told the Co-GM what to do.
- **Fix:** add a 🔒 three-option menu under each ask (for example, a Friend: *a pawnbroker who owes you · a night nurse · your landlady*), each checked against NPC-Index. For a refusal, add: 🗣 SAY *"Then it's the thing you wouldn't lend. We'll find out why."* Use the object from `S0:86` and never re-prompt (Boot rule 9).

**H4 (J/E). The first roll opens on a blank page, and the extra rolls invite a deferred mechanic.**
- **Where:** `S0:394` asks "What do you do?" with no 3-option menu (training wheel 3), and Wren froze. `S0:414` asks for "one quick roll **or Assist**", but Assist is taught in S2 (`Ladder:29`), and those rolls have no fiction behind them.
- **Fix:** add 🗣 *"You could (a) grab it fast, (b) hide it under something, (c) distract the customer."* Replace "or Assist" with two one-line situations: the customer asks PC 2 about cat books (Sway); Consequence goes for the till (Finesse). Put the extra rolls on the cut-list.

**H5 (I). The closing image contradicts whatever spot the table picks.**
- **Where:** `S0:426` asks where Consequence sleeps; `S0:432` shows `npc-consequence.png` "with the answer".
- **What goes wrong:** the render shows her on a *1962 DEPARTMENT-STORE CATALOG* by a rainy window. Theo said "inside the vault", so the TV contradicted him.
- **Fix:** show the image only for the counter, papers or the default answer. Otherwise set `image: null` with the caption "Closing Time".

## MEDIUM

**M1 (E). The prep never says what resisting reduces or which attribute to roll** (`S0:403–410`). Dana asked: "Am I resisting the tear or the glance, and with which attribute?" On the no branch (`S0:409`), step 6 (`S0:411`) says "6 minus your highest die", but the only die rolled is the action die. That suggests action rolls cost Stress.
**Fix:** for a 4–5, Prowess (the page doesn't tear). For a 1–3, Insight (they see only the cover). On the no branch, say "*if* you had resisted, 6 minus *that* die."

**M2 (L, secret). `S0:291` is unlabelled prose that says "Audit +1".** The Audit clock is GM-secret until S4 (`House-Rules.md:46`), and the line sits right above the SAY lines.
**Fix:** wrap it in 🔒 GM ONLY.

**M3 (B, secret). `S0:286` says "say 'that comes up.'"** The line has no label, and it hints that human-looking monsters matter (the Mimic).
**Fix:** 🗣 SAY *"Good. Noted."*

**M4 (K). Vice and purveyor are never asked; they appear only in the checklist (`S0:56`).** S1 Downtime relies on them (`S1:463`, `470`), and the dashboard field `pcinfo.vice` stays empty.
**Fix:** add an ask after `S0:86`: *"What's your Vice, and who supplies it?"*

**M5 (G). There is no step for a PC who arrives without a special ability**, although the players were promised one: "we'll choose your special ability … at Session 0" (`Character-Creation-Guide.md:39`).
**Fix:** add 🔒 "Anyone without one takes the first on their playbook (SRD default)."

**M6 (C/A). `S0:387` narrates a PC action ("one of you carried it up from the lair earlier").** The scene also jumps from the Annex to the shop counter with no transition.
**Fix:** say "left on the counter after this morning's stock-take", and open with 🗣 *"Downstairs, the shop floor. Afternoon."*

**M7 (Boot §3 rule 3). Seven asks pack two ideas into one question** (`S0:84`, `119`, `141`, `171`, `223`, `263`, `357`). A strict Co-GM would split each, doubling the stops.
**Fix:** allow "who + what" pairs at `Session-Boot.md:139`, or split `S0:119`, `263` and `357`.

**M8 (G). There are no lines for likely improvisation.** Nothing says what is in the vault or drawers at S0 (`S0:203–205`; `Curios-and-Chronicles.md:79` is silent). There is also no line for triangulating the AM voice (`S0:241`) or plugging Zoltar in. The Co-GM invents canon or calls for a roll before the Trial Run.
**Fix:** add a 🔒 "If they zig" block: "Three sealed tins from old jobs; nothing hums tonight." · "The signal only comes on clear nights; it's raining." · "Nothing happens. The lamp was already on."

**M9 (timing). The beat headings contradict the budget.**
- Beat 2 says 15 min (`S0:78`) against 25 in the budget (`S0:20`). Beat 4 says 15 against 20 (`S0:343`). The Trial Run says 10 against 15 (`S0:381`).
- My count of about 43 stops comes to roughly 2 h 50 before the buffer.
- `S0:115` says the map can be cut via the cut-list, but `S0:21` has no map item. It also says to keep the no-subway line, which sits inside the map SAY (`S0:118`).

**Fix:** sync the headings. Add to the cut-list: "map: if cut, still SAY its last sentence." Also add the extra practice rolls.

**M10 (I). The Zoltar image contradicts `S0:160`.** It shows a card on the velvet, a lit lamp and a green slot, against "the cards are long gone … unplugged for decades". This was logged as L8 in the earlier audit and is still open. Theo pointed at the card.
**Fix:** "…one bent card is still stuck to the velvet. The lamp on top glows anyway. Nobody knows why."

## LOW
- **L1 (C):** `S0:137` "The three of you stare back" narrates the PCs. `Session-Boot.md:135` uses this exact line as its model example. Change it to "The customer stares at the three of you."
- **L2 (A):** the upstairs SAY and the shelf question (`S0:271–272`) run while the corkboard is still on the TV. Move the Annex caption up to `S0:269`.
- **L3 (I):** "On a quiet afternoon" (`S0:135`) plays over a night-time, rainy exterior. Cue `location-curios-interior` there once that image exists; `S0:37` names it, but no beat cues it.
- **L4 (B):** three spoken lines have no label: `S0:175`, `S0:320` and `S0:392`.
- **L5 (J):** these questions have no stall examples: `S0:85`, `86`, `92`, `99`, `272`, and the closing questions (`S0:456` says "offer an example" but gives none).
- **L6 (L):** the menu calls Accord "safe ground" (`S0:316`), but it means turf for Tier (`GM-Rules-Reference.md:195`). Training's "double experience" (`S0:326`) mentions XP before S1.
- **L7 (E):** the players are never told the practice Stress clears (`S0:414` is GM ONLY). Add 🗣 *"Erase that Stress; it was practice."*
- **L8 (A/tooling):** the 4b banner has no `bannerId` and no point where it clears. Banners can't be checked in a render, because the tool turns off animation (`Player-Screen.html:88`). One corkboard render (a 7.4 MB PNG) came back black; it worked on a re-render.
- **L9:** add "Cold Open: none (S0)" to the Run Sheet so that Boot step 7 doesn't make the Co-GM write one.
- **L10 (L):** nobody has listened to the spoken words in `music-vocal-scanner-station` (its prompt asks for "locations of things that haven't happened yet"). The GM should listen once for any Subway or Voss detail.
- **L11 (I):** Old City has "horse-cart streets" (`S0:118`), but the shop stands between glass towers (`S0:126` and the image). Change to "on the edge of Old City, where the Meridian's towers begin".

---

## Per-beat table

| Beat | TV (rendered) | OK? | Issues |
|---|---|---|---|
| 1 Pitch | Title card | ✅ | — |
| 2 Intros | Title card | ✅ | M4 M7 M9 L5 |
| 3a map | `map-city-s00`, legible | ✅ | M9 L11 |
| 3a shop/ATM | `location-curios-exterior` | ⚠ | L1 L3 |
| 3b Zoltar | `location-zoltar-machine` | ⚠ | M10 |
| 3c Suite | `location-containment-suite`, matches | ✅ | M8 |
| 3d Scanner | `location-scanner-station`, matches | ✅ | L10 |
| 3e Corkboard | `location-corkboard-wall` + journal | ⚠ | L2 |
| 3f Annex | title card + "The Annex" | ✅ | H2 M2 M3 L6 |
| 4 Seeds | "The Annex" | ✅ | H3 |
| 4b Trial Run | title card + "Consequence" | ⚠ | H1 H4 M1 M6 L7 L8 |
| 5 Close | `npc-consequence` + fortune card (legible, no overflow) | ⚠ | H5 |

The TV never shows a secret. Canon checks pass: no subway system, no Decay, and no Menace Rule breach.

## Counts
**By severity:** BLOCKER 0 · HIGH 5 · MEDIUM 10 · LOW 11 = **26**

**By class:** A 2 · B 2 · C 2 · D 0 · E 3 · F 0 · G 2 · H 0 · I 4 · J 3 · K 1 · L 4 · M 0 · other 3 (compound asks, timing, Cold Open)
