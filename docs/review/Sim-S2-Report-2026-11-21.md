# Simulated Playthrough — Session 2 (2026-11-21)

**Report only.** I ran `05-Sessions/Session-02-Prep.md` (cited as `S2:line`) beat by beat against Boot, House-Rules, the Ladder, the Ritual, Heat-and-Entanglements, the Cues, the Lethal-Path table, Hunter-Kit, the Subway files and the SRD. I did not open `scene.js` or `feed.js`. I rendered 13 TV states; none raised a warning.

**Starting state:** collar returned, Gerald kept, Heat 2, Coin 0, Rep 2, Audit 1.
**Table:** Dana (rules), Theo (chaos), Ash (stalls).
**Branches run:** (a) seize; (b) warn, then talk to the Peacekeepers; (c) partial; (d) kill; (e) the chase; (f) the descent, the optional beats included; (g) a train and digging; (h) Downtime at Heat 7 (Entanglement 2 → Interrogation); (i) the Close.
**Assets:** all required files exist; every missing file is marked ❌ or optional.

## BLOCKER
None.

## HIGH

**H1 (D). The crew never goes inside the shop.**
- **Where:** after the plan and the engagement roll (`S2:183–192`), the prep jumps to the Choice (`S2:196`).
- **What goes wrong:**
  - Emmerich never speaks, and the engagement Position is never used.
  - Yet `S2:219` says "Emmerich has stopped talking".
  - The Ministry pretense triggers his Aggro Trigger (`Emmerich.md:48`), and no line covers it.
- **Fix:** add an "Inside the shop" beat:
  1. 🔊 One read-aloud per plan.
  2. 🗣 Emmerich: *"You're not here for a coat."*
  3. ❓ *"Who speaks?"* ⏸
  4. One roll at the engagement Position.
  5. Then the Choice.

**H2 (L). There is no Payoff step, and Coin has no numbers.**
- **Where:** `S2:212–214` say only "Coin" and "Half Coin". Downtime opens at Heat (`S2:492`). S1 has a Payoff step (`S1:457`).
- **What goes wrong:** Dana asks what the job pays and what Rep it earns; there is no answer.
- **Fix:** add "Step 0 — Payoff": Seize 4 Coin, partial 2, warn 0, kill 4 (if turned in); Rep +2.

**H3 (L). The Heat statements contradict each other.**
- **Where:**
  - `S2:495` adds "Double Bookkeeping failed +1", but that is an S1 ability.
  - `S2:512` gives "a Heat tick".
  - `S2:213` says only "Potential Heat".
- **Also missing:** the Meridian hostile-turf +1 (`Heat-and-Entanglements.md:10`). The kill path reaches Heat 9, which means Wanted +1 and a different Entanglement roll; the prep never says so.
- **Fix:** one 🔒 line: "talked 2 · ran 4; +1 Meridian; +2 if anyone died; at 9, Wanted +1 and the rest rolls over." Delete the other statements.

**H4 (B, secret). A 🔒 note naming the Omen sits inside the Hall READ ALOUD quote** (`S2:354`, within `349–364`).
- **What goes wrong:** a verbatim copy prints "Omen / Line 0 plant" for the GM to read out.
- **Fix:** move the note below `S2:364`.

**H5 (G). Carrying the thimble into the Subway draws no reaction.**
- **Where:** Cosma is warm in every branch (`S2:406–420`). That contradicts:
  - `Living-Subway.md:19`: "No taking… Especially Anchors";
  - its encounter 4;
  - `Cosma-Linden.md:34`: "judges by how the crew handled the last Twice-Born".
- **Fix:** add a variant for when the thimble is on them. 🔊 *"The hall goes quiet in a ring around you."* 🗣 Cosma: *"You're carrying someone."* On the kill path, Cosma does not get up.

**H6 (H, Menace). The kill has no lines, and Full Scooby follows it.**
- **Where:** `S2:216` is prose only: no read-aloud, no image, no empty-shop variant (in an empty shop there is no witness). The next beat fires caper music and a "RUH-ROH?" banner inline (`S2:239–240`), during a death.
- **Fix:** add 🔊 *"He doesn't raise his hands. The tape measure is still around his neck."* Then ❓ what they do with the thimble. In an empty shop: no Detection +2. After a kill, the chase runs straight on `music-approach`, with no banner and no gags.

**H7 (G/E). The "stand and talk" branch is empty and skips the lessons.**
- **Where:**
  - `S2:257` says only "It stays funny and slow", and its bridge narrates the crew ducking into an alley.
  - The Twist (`S2:290`) says "You're being chased".
  - Group Action and Assist are taught only "if they run" (`S2:262`).
- **Fix:** write three Foss form questions and ❓ *"Who signs?"* Then 🔊 the scanner van; Foss says *"Hold on —"*; ❓ *"Where do you go?"* Add a talk variant of the Twist. Teach Group Action on the forms: everyone signs, rolling Consort; the best die counts.

**H8 (L, A2). The Close ends the session before XP and the retrospective.**
- **Where:** `S2:554` says "then end the session". `S2:551` points to Ritual §1 only, never §2. Run Sheet row 14 has no XP. The cut-list lacks S1's "never cut the Entanglement or the XP tally" (`S1:20`).
- **Fix:** change `S2:554` to "then XP (with crew XP), then the retrospective, then end". Copy the never-cut clause.

**H9 (L, canon). "The railing is simply there tomorrow" (`S2:396`) gives the Subway a fixed place.**
- **Where:** this contradicts `Overview.md:27`. The refusal branch also has no lines.
- **Fix:** 🔊 *"When you look back, it is a brick wall."* The debut moves to S3, somewhere else.

**H10 (G). The Audit fallout fires tonight, and it has no lines.**
- **Where:** Audit is at 1, so `S2:65` puts a "plainclothes agent in the bookstore". There is no read-aloud, no SAY, no TV state and no exit.
- **Fix:** 🔊 *"A man in a grey raincoat has read the same paperback by the window for twenty minutes. He leaves when the envelope arrives."* 🔒 If asked: "Just browsing." Never say "Audit".

## MEDIUM
- **M1 (E):** the activities have no procedures, and there is no cost for an extra one (`S2:503–508`). The menu SAY sits inside a "remind only if asked" block (`S2:501–502`). **Fix:** copy `S1:486`.
- **M2 (L):** the Entanglement (`S2:496`) has no pick for each cell. At Heat 7, Interrogation with Coin 0 forces harm and Heat +3. Nothing places it relative to Greta's visit. **Fix:** a table of picks; resolve it before Greta.
- **M3 (A):** Detection is never cleared. Renders 07 and 08 show it at 4/4 over the railing and the hall. **Fix:** `clocks:[]` on the Subway Beat 1 "go".
- **M4 (A):** if the optional Drennick & Foss image is skipped, the thimble stays up through the chase (`S2:241`). The banner is never cleared, and the fight branch (`S2:256`) keeps the caper music. **Fix:** make the D&F image required; set `banner:null`; switch to `music-approach` in a fight.
- **M5 (L/SRD):** the chase contradicts itself and the SRD.
  - "Each success ticks nothing" sits beside "4–5 = +1" (`S2:265`).
  - There is no Position, Effect or roll count.
  - "Fill it and Apex has you" (`S2:264`), yet filling it costs nothing (`S2:314`).
  - Assist is taught inside a group action where everyone rolls, which SRD:1880 forbids. The Assist SAY omits "one helper" and "shared consequences" (SRD:1878).
  - **Fix:** Risky/Standard; three rolls; a full clock corners one PC, and Assist is taught on that individual roll.
- **M6 (L):** the engagement roll sets Position (`S2:190`), but `S2:192` fixes a Position for each plan. **Fix:** make `S2:192` Effect only.
- **M7 (A):** `S2:129` and `S2:137` say "show the shop image"; `S2:158` says hold it. **Fix:** delete the clause in 129 and 137.
- **M8 (I):** "Mid-morning" (`S2:161`) plays over dusk and night images (renders 03, 04, 06). **Fix:** "Late afternoon, the lamps coming on".
- **M9 (I):** Greta is seated and writing (render 12), but fires before "comes in shaking the rain off" (`S2:519–521`). This repeats S1 L12. **Fix:** show the image after her first SAY.
- **M10 (Menace):** the Cologne gag (`S2:168`) makes "every NPC remark" on the smell for the rest of the session, including the 🔴 Choice and the Subway. **Fix:** "…until you leave the Meridian".
- **M11 (F):** a thimble sealed in a packed containment jar (`Hunter-Kit.md:21`) should not ping the scanners, yet `S2:233` and `S2:251` assume it does. **Fix:** add a jar branch that uses the "bookshop people" line.
- **M12 (H):** there is no Lethal-Path pointer (S1 has one at `S1:20`). Theo swung at Thorne, and nothing covered it. **Fix:** copy the S1 pointer, naming Thorne and Greta.
- **M13 (E):** no Flashback is offered in the first hour (Ladder rule 5), and Run Sheet row 2's "Flashback" has no line. The Twist ask (`S2:291`) has no examples and no effect. **Fix:** give three examples; a success is Detection −1.
- **M14 (J):** these questions have no stall help: `S2:118`, `224`, `227` (also compound), `321`, `411`, `543`. **Fix:** three options each. For Cosma: *"Who are they? / Why us? / What's the luggage?"*
- **M15 (B):** the Return READ ALOUD carries branch arrows inside the quote (`S2:485`). The Tell 4 aside "*(The crew has never been to his office.)*" (`S2:534`) is unlabelled. **Fix:** split it into two 🔊 variants and label the aside 🔒.
- **M16 (G):** "If Apex Aegis got involved" (`S2:525`) is always true (`S2:233`), so it collides with the branch forms. Seize and warn have no ⏸. **Fix:** make it an add-on line, then ⏸.
- **M17 (L/I):** the businessman "turns the corner at the end" of a dead end (`S2:305/307`). "Two stories deep" and "slightly damp" (`S2:333`) clash with the one-storey canon and the dry descent (`S2:133`). **Fix:** "…gone back the way he came"; "cold and dry".
- **M18 (G):** there are no lines for a train or for digging. **Fix:** 🔒 "Platforms; no train tonight." 🔊 *"Past the yellow line the tunnel is dark and dry. Nothing comes."* / *"Under the tile is more tile."*
- **M19 (timing):** the cut threshold is 2 h 00 at `S2:13` but 2 h 15 at `S2:400`. The Return-to-Close block is too short (see below).
- **M20 (G):** the warn branch ends on an ask (`S2:224`). **Fix:** 🗣 *"Thank you."* Then 🔊 he goes back to the uniform (`Emmerich.md:59`).

## LOW
- **L1 (C):** these lines narrate the PCs' feelings or knowledge: `S2:309`, `333`, `337`, `362`, `457`.
- **L2 (I):**
  - The "Elias Thorne" caption sits over a street without him.
  - The railing is on a side wall.
  - The hall's map looks like a real city's, and its floor is wet.
  - Cosma is seated, though she walks over in the text.
  - The thimble is on a table while the SAY says "on his right hand" (`S2:203`).
- **L3 (L):** the Group Action SAY says "per teammate", but SRD:1886 says each PC, the leader included. Desperate group XP (SRD:883) is never mentioned.
- **L4 (L):** Cosma's "sixty years" (`S2:414/416`) contradicts her file (the 1950s). `S2:415` repeats a sentence.
- **L5 (L):** `Living-Subway.md:18` ("No blood") contradicts `S2:396`, and its "one funny beat every visit" contradicts the first-visit rule.
- **L6 (L, secret):** both Tells are narrated overtly (`S2:146`, `537`).
- **L7 (F):** the REJECTED stamp (`S2:114`) was never established.
- **L8:** Run Sheet row 2's "Cover-story callback" has no text.
- **L9 (B):** the Favor label's "otherwise add…" (`S2:420`) is not a ready line.
- **L10 (G):** the unravelling never reaches the Return.
- **L11 (B):** the "woodsmoke" directive (`S2:560`) invites unlabelled narration.
- **L12 (A):** the Job Board has no caption (`S2:430`).
- **L13 (L):** "Not a good reputation" (`S2:207`) reads as lost Rep.

## Per-beat table
| Beat | TV (rendered) | OK? | Issues |
|---|---|---|---|
| 0–1 Cold open, envelope | recap → exterior + contract (legible) | ✅ | H10 L7 |
| 2 Approach | `map-city-s02`, no Subway pin | ✅ | M13 L8 |
| 3 Thorne | street, "Elias Thorne" | ⚠ | M7 M12 L2 L6 |
| 4 Observation | street → Emmerich (thimble on the right hand ✓) | ⚠ | H1 M6 M8 M10 |
| 5 Choice | thimble on a table | ⚠ | H1 H6 M20 L13 |
| 6 Chase | D&F + Detection | ⚠ | H6 H7 M4 M5 M11 |
| 7 Entrance | railing + stale 4/4 clock | ⚠ | H9 M3 M17 |
| 8 Hall | hall + stale clock | ⚠ | H4 M3 M18 |
| 9 PTOLEMY | three cases, clasps ✓ | ✅ | — |
| 10 Cosma | seated | ⚠ | H5 M14 L4 |
| 11 Optional | Aldric/Broker; Job Board none | ⚠ | L12 |
| 12 Exit | pier, 1973 ad ✓ | ✅ | L1 |
| 13 Downtime, Greta, call | Greta + strip | ⚠ | H2 H3 M1 M2 M9 M15 M16 |
| 14 Close | fortune card (legible) | ⚠ | H8 |

No secret reached the TV. There is no Decay, the Audit stayed hidden, and no train was boarded.

## Time vs budget
On the seize + run path, my count is **3 h 23**, against a budget of 2 h 55 (`S2:19`):

| Stretch | Minutes |
|---|---|
| Opening | 34 |
| Shop and Choice | 32 |
| Chase and Subway | 77 |
| Return to Close | 60 |

The cut-list brings it to about **2 h 51**. The Return-to-Close block (Payoff, Entanglement, Downtime, Greta, the call, XP and the retrospective) took 60 minutes, not the 45 budgeted. **Fix:** budget it at 60; text mode keeps Greta and the Entanglement.

## Counts
**By severity:** BLOCKER 0 · HIGH 10 · MEDIUM 20 · LOW 13 = **43**

**By class:** A 4 · B 4 · C 1 · D 1 · E 2 · F 2 · G 7 · H 2 · I 3 · J 1 · K 0 · L 14 · M 0 · other 2
