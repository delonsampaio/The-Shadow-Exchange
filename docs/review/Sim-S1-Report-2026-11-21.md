# Simulated Playthrough — Session 1 (2026-11-21)

**Report only.** I ran `05-Sessions/Session-01-Prep.md` beat by beat against Boot, House-Rules (A2), the Ladder, the Ritual, Heat-and-Entanglements, the Cues, Hunter-Kit and the SRD. I did not open `scene.js` or `feed.js`. I rendered and viewed 13 TV states; no WARNING fired.

**Table:** Dana (Hound) argued the SRD; Theo (Slide) swung at Merton and at Thorne; Ash (Whisper) stalled.

**Branches run:** (a) alley sneak, with a Desperate engagement for Ash and a 1–3 at Bernard that failed forward into a Detection tick; (b) fight to kill: Subdue, kill, Gland; (c) severing the collar; (d) mend and return; (e) hand everything to the Ministry; (f) Gerald kept / handed over; (g) Double Bookkeeping on a 6 and on a 2; (h) Desperate rolls; (i) Downtime and the Close.

**Assets:** all present; every ❌ is optional.

## BLOCKER
None.

## HIGH

**H1 (L). There is no Payoff step, so Rep is never awarded.**
- **Where:** Downtime opens at Heat (`S1:458`), but `Heat-and-Entanglements.md:14` and SRD:1935 put payoff first. Coin appears only in the Choice menu (`S1:383`). SRD Rep (2 per score, 0 if kept completely quiet) is absent, yet the TV strip shows Rep (`S1:456`).
- **What goes wrong:** Dana asks for the 2 Rep, and the Co-GM has no line for it.
- **Fix:** add a "Step 0 — Payoff": 🗣 *"A score pays Coin and Rep."* Back it with a 🔒 table: Ministry hand-over 4 Coin; keep or file nothing 0 Coin; mend 0 Coin. Rep is 2, or 0 if the mend stays completely quiet.

**H2 (B/G). The S1 exception (Greta delivers the Entanglement in person) has no lines.**
- **Where:** `S1:490` says Greta delivers it "in her own words". Both rows S1 allows have cues that are phone calls (`Cues:18`, `Cues:21`).
- **What goes wrong:** the Co-GM improvises, or reads a phone call while Greta stands in the room. Nothing says where it goes relative to "Two years of your handwriting".
- **Fix:** after the reaction stop at `S1:499`, add the in-person versions:
  - **Usual Suspects:** 🗣 (Greta, quieter, clipboard lowered) *"Before the forms. They picked up [Friend/Purveyor] this morning. Pay one Coin, or we see what they say."* Then ❓ and ⏸.
  - **Gang Trouble:** 🔊 Gerald has eaten Form 47-B.
  - Then continue at `S1:501`.

**H3 (L/G). The Entanglement picks cover only the 1–3 cell.**
- **Where:** `S1:461–465`. At Wanted 0 (two dice, keep the lowest), 25 % of rolls are 4–6. On those, "If neither fits, there is no entanglement" gets misread as a skip, which breaks `S1:20`.
- **Also:** Unquiet Dead's way out needs Acquire Asset, which is barred tonight (`S1:483`). At Heat 6+, a 4–5 offers Demonic Notice, which risks the Omen.
- **Fix:** add a pick for every cell.
  - **4–5:** Rivals (cue 6), or Unquiet Dead only if Merton died ("deal with it yourselves").
  - **6:** Cooperation, which lapses with no +3 faction.
  - **Heat 6+:** Interrogation / Show of Force / Arrest. Never Demonic Notice before S2.

**H4 (L). Heat for the kill contradicts itself.**
- **The four statements:**
  - `S1:383`: hand everything over, Gland included (it kills Merton): "no extra Heat".
  - `S1:345`: +2 "in total, not +4".
  - `S1:460`: "+2 as the SRD says" (SRD:1971).
  - `S1:460`: also adds "Double Bookkeeping failed +1", which `S1:394` and `S1:487` omit and which Step 4 rolls only *after* Heat.
- **What goes wrong:** Dana: loud 4 + kill 2 + high-profile 1 = 7, which is the 6+ column. The Co-GM had 2.
- **Fix:** one 🔒 line: "base exposure (0/2/4) + 2 if Merton died by any path + 1 for the councilman's dog; file nothing +2." Delete the other two clauses.

**H5 (H/G). The fight-to-kill block contradicts itself.**
- **The contradictions:**
  - When Subdue fills, he is "down" (`S1:369`) but it is also "a kill" (`S1:345`), while the Gland "kills him" (`S1:338`).
  - Severing drops his threat "to zero" (`S1:344`), yet Effect becomes "Standard once it is cut" (`S1:342`).
  - Nothing says how many segments a hit ticks.
  - After a sever, the Choice still offers the collar and the mend.
- **TV:** the true-form image shows the collar on his neck while Theo holds it (render b6c).
- **Fix:** when Subdue fills, he is down and alive. Ticks per hit: Limited 1, Standard 2, Great 3. A sever ends the fight and starts the 1d6 hours. Add a "collar severed" menu. Use the true-form image only when no PC holds the collar.

## MEDIUM
- **M1 (A).** The Run Sheet shows `npc-merton-human` "if he appears" (`S1:32`), but `S1:295` says no image. **Fix:** Run Sheet = caption "Merton".
- **M2 (A, Menace).** The Lever and stage-prop gags (`S1:353`) run while Merton is "held", which is exactly when the chained true-form image is up (`S1:33`, `311`). That puts a banner over a threat. **Fix:** set `image:null`, caption "The stage", before the gags.
- **M3 (A).** No beat clears the clocks. In my renders, Detection and the Surge sat over the Choice, Thorne and the Greta crew strip. **Fix:** set `clocks:[]` at Beat 7 "go".
- **M4 (H).** Detection filling has no consequence (`S1:262`, `332`). **Fix:** "Full: the Apex van's dish turns; exposure becomes loud (4)."
- **M5 (D/G).** The plan-3 "night guard" (`S1:164`) *is* Merton, which puts him in the lobby before his "before" state. **Fix:** make it Bernard.
- **M6 (A).** The Ruh-Roh is spoiled in advance: the photo and card say "HANDS PRESENT" (`S1:102`, `104`), so "long pale fingers… they wave" (`S1:240`) gives it away. Theo: "it's the dog." **Fix:** cut the fingers and the wave from the build-up.
- **M7 (B).** The Choice menu's SAY quote holds GM instructions (`S1:383`, `389`). The no-Gland menu (the common soothe path) is 🔒 prose with no SAY (`S1:387`). **Fix:** two clean SAY menus.
- **M8 (G).** "Return the collar" is listed among the Surge options (`S1:339`), but the Fourth Option runs only after "The Surge is over" (`S1:376`). Ash mended it mid-Surge, and nothing covered it. **Fix:** add a Surge option "Mend now (Tinker/Attune, Desperate): success empties the Surge."
- **M9 (G).** After a clean Double Bookkeeping 6, Thorne's "log the gland" (`S1:423`) shows the Ministry knows. **Fix:** off the books → use the no-Gland line.
- **M10 (H, secret).** When Theo swung at Thorne, S1 did not point to `05-Sessions/Lethal-Path-Quick-Table.md`. Its rule 7 covers Thorne, but nothing in S1 or Boot references it, and Bernard has no row. **Fix:** add a 🔒 pointer in the S1 Run Sheet and a Bernard row (+2 Heat, a witness).
- **M11 (E/J).** Recover, Reduce Heat, Long-Term Project and Train have no script or procedure (`S1:453`, `481`); for example, the healing clock and Train once per track. Add the engagement roll, and the session teaches more than the "four lessons" (`S1:40`). **Fix:** one 🔒 line each, plus a ≤30 s Recover SAY.
- **M12 (E).** The Close has no crew XP SAY or ASK (`Ritual:12`). An attribute track can also fill at S1 (2 Desperate XP plus the tally), but the Ladder teaches advancement "from S2" (`Ladder:31`) while House-Rules says S1 (`House-Rules.md:28`). **Fix:** add a crew-XP ❓, and the rule "a track filled at S1 advances now, one SAY."
- **M13 (L).** Dana asked about Push, Assist and Acquire Asset. A2 says "nothing is skipped", but the Ladder (`Ladder:132`) and `S1:483` withhold them. In the SRD a *player* volunteers the person taken in The Usual Suspects (SRD:2131); `S1:463` has the GM pick. **Fix:** a House-Rules line: "Deferred = untaught but available if asked." Follow the SRD volunteer rule.
- **M14 (timing).** See the timing section below.

## LOW
- **L1 (G):** returning Gerald gives "Detection +1" after the score is over (`S1:403`). Make it Heat +1.
- **L2 (F):** the badge, clipboard and gags (`S1:216`, `249`, `361`) assume someone packed the clipboard. Add 🔒 "showing the badge ticks 1 load".
- **L3 (E):** Desperate = XP is only in the Beat 6 bridges (`S1:368`). Add a pointer at `S1:168`.
- **L4 (G):** overindulgence "disappear" (SRD Lost) and "attract trouble" (a second Entanglement) are not handled (`S1:476`).
- **L5 (E):** no Position or Effect is given for soothe, restrain, run it out, mend, Sway or Study Gerald (`S1:335–337`, `395`, `384`, `260`).
- **L6 (C):** two gags narrate the PCs: "can't see each other" (`S1:358`) and "with all of you on it" (`S1:360`).
- **L7:** the Run Sheet says "Tells 1, 2, 6" (`S1:35`); `S1:79` and `407` say "1 & 2".
- **L8 (I):** in the auditorium image the lit stairs go *up*, but the air "comes up" from a basement (`S1:232`). The collar image sits on a lab table, while the Choice happens in the theater.
- **L9 (A):** the downtime menu SAY comes before the Downtime "go" (`S1:453` → `455`) and is repeated at `S1:481`.
- **L10 (L):** `Ritual:12` says the same thing twice. The XP SAY never says that indulging alone earns no XP (SRD:889); Theo claimed it.
- **L11 (L, secret):** the Zoltar card (`S1:514`) restates Tell 1 forty minutes later, and Dana connected it. Moving it is a GM decision.
- **L12 (I):** the Greta image shows her seated, writing beside the cat, but the text has her "steps in, shaking rain off a clipboard" (`S1:495`). Fire the image after "Ah. You're real."
- **L13 (A):** title-card renders keep the centred "Curios & Chronicles" subtitle under the basement captions.

## Per-beat table

| Beat | TV (rendered) | OK? | Issues |
|---|---|---|---|
| 1 Envelope | exterior + contract card (legible, no overflow) | ⚠ | M6 |
| 2 Plan & Gear | Suite + crew strip | ✅ | M5 M11 L3 |
| 3/3b Approach | `map-city-s01` (X on the theater) | ✅ | — |
| 4a Lobby | Bernard (matches) | ✅ | M10 L2 |
| 4a-ii Auditorium | door stage-left, brick ✓ | ⚠ | L8 |
| 4b Gerald | hands + Detection 1/4 | ⚠ | M6 L5 |
| 5 Locker/man | title card | ⚠ | M1 L13 |
| 6 Surge/fight | title card + 3 clocks (legible) | ⚠ | H5 M2 M4 M8 |
| 6 chained | true form, collar on the neck | ⚠ | H5 M2 |
| 7 Choice | collar (crack matches) + stale clocks | ⚠ | H4 M3 M7 M9 L1 |
| 8 Thorne | coat, rain, ring on the right hand ✓ | ✅ | M9 M10 L7 |
| 9 Mara | "The alley" | ✅ | — |
| D Downtime | Greta + strip | ⚠ | H1 H2 H3 M11 M13 L4 L9 L12 |
| C Close | fortune card (legible) | ⚠ | M12 L10 L11 |

No secret reached the TV. Canon checks pass: no subway system, no Decay, and the Audit clock stays silent. Wanted 0 and the Heat columns are right (`S1:461`).

## Time vs budget (M14)
- **Fight path:** 10 + 10 + 17 + 6 + 28 + 10 + 35 + 15 + 10 + 3 (Mara, unbudgeted) + 38 + 14 = **3 h 16**.
- **Soothe path:** **3 h 06**.
- **Budget:** 2 h 45 + slack.
- **Cuts:** the cut-list (−25) brings it to about 2 h 55. The Entanglement and the XP tally still fit.
- **Close:** 10 minutes is too little. Zoltar, 6 XP stops, crew XP and 9 retro stops took 14.
- **Text-message mode:** `S1:20` does not say whether Greta's scene survives it.
- **Fix:** budget the Close at 15, and add "text mode keeps Greta + the Entanglement".

## Counts
**By severity:** BLOCKER 0 · HIGH 5 · MEDIUM 14 · LOW 13 = **32**

**By class:** A 6 · B 2 · C 1 · D 1 · E 4 · F 1 · G 4 · H 3 · I 2 · J 0 · K 0 · L 6 · M 0 · other 2 (timing, tell label)
