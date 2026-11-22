# Simulated Playthrough — Session 3 (2026-11-21)

**Report only.** I ran `05-Sessions/Session-03-Prep.md` (`S3:line`) beat by beat against the canon files, Heat-and-Entanglements (H&E) and the SRD. I did not open `scene.js` or `feed.js`. I rendered and viewed 13 TV states; no WARNING remained after the script's retries.

**Start:** thimble seized, Heat 4, Coin 4, Rep 4, Audit 2 (secret), Twice-Born Enmity. **Table:** Dana (rules), Theo (chaos), Ash (stalls).
**Branches run:** (a) briefing + Acquire (Dana: tiers, quality, Coin); (b) Subway second visit; (c) approach, Agnes, jars, tea; (d) Push at the first Risky roll; (e) Pivot A, B (records / 1991 jar / curtains jar / crit), C; (f) Theo attacks Mabel, then Agnes; Drennick & Foss at the door, fight to kill; (g) Downtime at Heat 5 and 11; (h) Close with an attribute track filling.

## BLOCKER
None.

## HIGH

**H1 (L). There is no Payoff step, and nothing has a number.** The pivot gives only "pays in full" (`S3:324`), "standard **Coin**" (`333`) and "Partial Coin" (`336`), and the card gives only "STANDARD EXTRACTION RATE" plus a bonus (`114`). Downtime opens at Heat (`388`). Rep is never awarded (SRD:1940). Dana asked what each option pays, and the Co-GM had no answer. C's "one complication of the GM's choice" (`336`) is never named.
**Fix:** add "Step 0 — Payoff" before `388`: A 4 Coin (+2 if cleared before month end) · B 0 Coin (the jars sell for 4 in Downtime) · C 2 Coin, and the complication is Stalls's seventeen questions (Questioning) · Rep +2 for every option.

**H2 (L). The Heat rules contradict each other.** "Loud … +2" (`388`) contradicts SRD/H&E:10 (loud 4, contained 2); the Overhang hostile-turf +1 (named at H&E:10) is missing though `167` cites the district; "Double Bookkeeping failed +1" has no S3 trigger; `335` says Heat can reach 9 yet `390` hard-codes "Wanted 0 → two dice". **Fix:** use one 🔒 line: "quiet 0 · Agnes or a neighbour saw you 2 · D&F at the door 4; +1 Overhang; +2 if anyone died. At 9: Wanted 1, roll one die." Delete the other statements.

**H3 (L). The Entanglement has no pick for each cell, and it points at examples that do not exist.** `144` says "Keep the 0–3 examples below at hand", but none follow (`145–147`). At Heat 5, a 4–5 offers Unquiet Dead. That would bring Mabel back as a scary ghost, which contradicts her file and Option B. The Audit cap (H&E:39, never above 3 before S4) is not restated at `146`.
**Fix:** a picks table. **Heat 4–5:** 1–3 Questioning (Agnes is asked about the visitors; Audit +1 silent, cap 3) · 4–5 Reprisals (Agnes's street "inspected"; Unquiet Dead only after a violent A) · 6 Show of Force (an Apex van on Calloway Street). **Heat 6+:** 1–3 Interrogation (pay 3 of the crew's 4 Coin) · 4–5 Show of Force, never Demonic Notice · 6 Arrest.

**H4 (L, A2). The Close ends the session before XP and the retrospective.** This repeats S2 H8. The XP pointer (`423`) sits above the card. `426` then says "then **end the session.**" Ritual §2 (the retrospective) is never referenced. The cut-list (`20`) has no never-cut clause.
**Fix:** after `425`, add the steps "XP (each PC, then crew XP; card 22 if a track fills) → retrospective (Ritual §2) → end". Add "never cut the Entanglement or the XP tally" to `20`.

**H5 (E). Push Yourself and the Devil's Bargain menu come after the Moral Pivot.** Both sit at `346–355`. A Co-GM who reads in order reaches them only after the first Risky roll (Breach, `194`) has passed. The Run Sheet's Teaches column (`24–34`) never lists Push. Dana asked whether she could push and take the bargain. The prep never says that the push die and the bargain die do not stack (SRD:348).
**Fix:**
- Move `346–355` to just after Her Toolkit (`229`).
- Add "**Push Yourself**" to Run Sheet row 4.
- Add a 🔒 line: "Push for +1d *or* take the bargain, not both; a push for +1 effect can stack."

**H6 (H/B). The fight paths are prose with no lines; Agnes has none at all.** Mabel (`335`): no Effect, no clock, no 🔊 for her going cold, no SAY. D&F's door scene stops at "Then they assess the situation" (`367`): no SAY for what Apex wants, no ❓, no exit. Theo swung at Agnes: neither the prep nor `Lethal-Path-Quick-Table.md:22–35` has a row, and S3 never points to the table (S2 M12 pattern). **Fix:**
- Mabel: Effect Limited, salt/iron Standard; on a hit 🔊 *"The room drops ten degrees. Her cardigan stops moving. She is looking at you the way she looked at the jar."* 🗣 *"Sit. Down."*
- Drennick & Foss: 🗣 Foss *"Unlicensed extraction. Calloway Street. Residential."* ❓ *"Who talks to them?"*
- Agnes: add a row: a civilian, +2 Heat, Detection +2, and Mabel turns against the crew. Point to the Lethal-Path table at `20`.

**H7 (G). The Subway visit ignores the assumed branch.** `61` says "Cosma Linden does not appear this session", but `95` gives her a coat gag. Under Enmity every line stays warm, against Living-Subway:19 ("Especially Anchors"), its encounter 4 and Faction-Tracker:44. S2:416 ("the debut moves to S3") has no first-visit variant here, so a debut would run with comedy, which is forbidden on a first visit. **Fix:** under Enmity, 🔊 *"The Quiet Platform goes quiet in a ring around you."*, no Cosma, PTOLEMY charges double; with no S2 descent, run the Stations.md first-visit beats with no comedy.

**H8 (A, asset). The missing S3 music has no stand-in.** `music-ashby-approach` and `music-ashby-interior` are ❌ (`26–28`, `171`, `209`). Under Boot §2a the loop keeps playing, so the cosy bookshop loop runs through the 11:47 house and the haunt.
**Fix:** add "❌ → play `music-approach.mp3`" at `171` and `209` (the S1 precedent, Music-Prompts:221), and `music-score.mp3` if a fight breaks out.

## MEDIUM
- **M1 (A).** The Subway visit (`87–100`) has no Run Sheet row or cue; the bookshop image and loop stay up underground. **Fix:** row 0b: `music-subway-loop`, `location-subway-main-hall`; re-cue the exterior at the exit.
- **M2 (L/G).** Subway gaps: Aldric and the Job Board promised (`13`, `88`), no lines; Theo tried to board and there is no train line (**fix:** 🔊 *"The red platform is empty. The departure board ticks."*); Bram is "a transit cop in a 1970s uniform" (`98`) but canon is a gargoyle on a pillar (Subway-Regulars:26); "No roll" (`92`) vs the Consort Downtime activity (House-Rules:21, Living-Subway:81).
- **M3 (A/E/H).** Detection (`73`) is never shown, ticked or given a fill consequence; the Overhang tick and Agnes-as-witness (`167`) do nothing. **Fix:** `clocks:[Detection 0/4]` at `176`; Agnes ticks 1; full → D&F knock.
- **M4 (F).** Load is asked only inside IF THEY STALL (`187`). **Fix:** ❓ "Light, Normal or Heavy?" before `183`.
- **M5 (E/L).** The Acquire lesson (`154`) never says what a 1–3 gives at Tier 0 (quality −1), what "quality" means, or that the GM sets a minimum (SRD:2163); `160` lists "+1d from Greta" as if it were a route to a 6; the free pre-score roll (`153`) is a deviation House-Rules A never records. **Fix:** 🗣 *"Quality is how good it is; I'll tell you the minimum first. A 1–3 at Tier 0 gets you something shoddy: Limited effect."* Add a House-Rules row for the practice roll.
- **M6 (G/J).** Pivot gaps: `321` waits on "whether they tell her the truth" but has no lie branch and no stall help; "opened a jar" (`327`) unlocks Thomas even after the curtains jar alone, so the option leaks the secret; a crit (`334`) has no read-aloud; `Mabel-Ashby.md:61` omits the jar. **Fix:** records, the 1991 jar or a crit only; lie → Mabel *"I know why you're here. I made the kettle first."* (file:68); add a crit 🔊.
- **M7 (G).** Option B loose ends: Greta's "Spectral Subject Declined Removal" (`397`) though she departed (`341`); the needle is left and nothing stops the crew taking it for the payout (Dana tried); the live portrait stays up (`316` covers only A); "+1 Favor" under Enmity (`334`) — token or standing? **Fix:** form "Departed, Voluntary"; 🔊 *"The needle is cold now. It is just a needle."*; `image:null`, caption "The Ashby House"; rule "Enmity → Ambivalence, no token".
- **M8 (Menace/G).** The Hum (`271`) follows *any* jar, including the November 1991 jar (`266`), so a gag lands right on the grief reveal. **Fix:** the Hum fires only for "Tuesday, 1978" or the birthday jar.
- **M9 (B).** No labelled lines for Cosma's card (`61`: no 🔊, no `note` card, no beat), Greta's square-footage question (`62`) or the Agnes coda ("Do not narrate it", `304`; the GM cannot act); a GM instruction sits inside the READ ALOUD bullets (`53`).
- **M10 (G).** Hedged lines: 🔊 "in an evidence pouch, or it isn't" (`380`), 🗣 "You have the needle, or you don't" (`419`). **Fix:** one line per branch.
- **M11 (L).** The in-person pitch (`128–136`) contradicts `Renwick-Stalls.md:5`, `21` ("phone only S3"). GM decision: update the file, or make it a call.
- **M12 (G).** The Inspection (`234`) grades and hands the lowest a biscuit *before* the table grades (`236`). **Fix:** read-aloud ends at "grading"; ask; then the biscuit.
- **M13 (J/E).** No stall help at `126`, `155`, `321`, `393`, `420`; Downtime activities have no procedures (S2 M1 pattern). **Fix:** three options each; copy S1's activity lines.
- **M14 (D).** "She invited you; the door is already open" (`184`): no invitation exists, and it spoils the Door gag (`198`). **Fix:** "Walk in — up the path, to the front door."
- **M15 (E).** Fight paths add Harm (card 16) and Wanted to Acquire, Push and card 22: 5 lessons. **Fix:** 🔒 "Wanted: one sentence; full card in S4."

## LOW
- **L1 (I):** Mabel seated by daylight vs "She comes downstairs" (`213`); wraith standing vs "She sits in the chair" (`340`); ~70 jars vs "forty-three" (`258`); D&F image is a Meridian street with an "EMMERICH & DAUGHTER" sign, used for a porch (`364`); night exterior under an afternoon briefing (`125`).
- **L2 (C):** "you heard it click on" (`234`), "it was not there this morning" (`190`), "One of you notices" (`405`).
- **L3 (B):** GM asides on SAY lines: `119`, `411`, `412`.
- **L4 (A):** "BOO?" never cleared (`241`); needle and wraith both cued for A (`316`, `339`); "once generated" stale (`167`); Greta never gets her image (`117`, `395`).
- **L5 (L):** beets repeat S2 (`365–366`), not "the aftertaste" (`Drennick-and-Foss.md:23`).
- **L6 (F):** the dampener bargain (`352`) assumes it was acquired.
- **L7 (secret):** "The line is silent for one second" (`415`) underlines Tell 5.
- **L8 (G):** Mara fires only "if a PC looks out" (`401`); nothing prompts it.
- **L9:** "Put the kettle on" (`199`) vs "already on" (`234`).
- **L10:** messenger and Stalls both in ill-fitting coats (`112`, `131`); Dana asked if they were one man.

## Per-beat table
| Beat | TV (rendered) | OK? | Issues |
|---|---|---|---|
| 0 Cold open | recap card (legible) | ✅ | M9 |
| 0b Subway | *no cue: bookshop stays up* | ❌ | H7 M1 M2 |
| 1 Briefing | exterior + contract (legible, no overflow) + strip | ⚠ | H1 L1 L10 |
| 1 Stalls | coffee shop, two cups ✓ | ⚠ | M11 |
| 1 Acquire | same | ✅ | M5 |
| 2 Approach | `map-city-s03`, Ashby pin, no Subway pin ✓ | ✅ | H8 M4 M14 |
| 3 House | exterior: amber upper-right window ✓, no clocks ✓ | ⚠ | M3 |
| 4 First contact | interior → Mabel seated | ⚠ | H5 M12 L1 L9 |
| 5 Jars | PRIVATE ✓, about 70 jars | ⚠ | M8 L1 |
| 6 Agnes | tureen + ladle ✓ | ⚠ | H6 |
| 7 Pivot | live → wraith (standing) / needle (on a table) | ⚠ | H6 M6 M7 L4 |
| — D&F | Meridian street + Emmerich sign | ❌ | H6 L1 L5 |
| 8–8b Return / Downtime | exterior | ⚠ | H1 H2 H3 M10 M13 |
| 9 Close | fortune card (legible) | ⚠ | H4 |

No secret reached the TV: no Decay, Audit hidden, nothing dug, the Omen a symptom only, Stalls = Apex 🔒.

## Time vs budget
Budget (`S3:19`) **2 h 55** with the Subway. My count: cold open 12 · Subway 20 · briefing/Stalls/Acquire 28 · approach 8 · entry/haunt 17 · jars/Push 18 · Agnes 10 · Pivot 20 (+10 fight) · Downtime/Greta 32 · Omen/Mara/Thorne 8 · Close 20 = **3 h 13** (**3 h 23** fighting). The cut-list (−35) gives about **2 h 38 / 2 h 48**. Budget the Close at 20, not 10, and drop the unbudgeted "What does tonight feel like?" round (`420`), which duplicates the retrospective.

## Counts
**By severity:** BLOCKER 0 · HIGH 8 · MEDIUM 15 · LOW 10 = **33**

**By class:** A 4 · B 3 · C 1 · D 1 · E 4 · F 2 · G 9 · H 2 · I 1 · J 1 · K 0 · L 9 · M 0 · other 3 (asset, timing, secret)
