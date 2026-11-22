# XP & Entanglement Change Audit (2026-11-21)

Scope: `git diff HEAD` for the ruling that Entanglements are rolled and XP is tallied every session from S1, plus a repo-wide sweep. Report only.

## BLOCKER

**B1. S1's Entanglement makes Greta speak on the phone before her first in-person scene.** `S1:465` says to play the result *before* the activities, so before Step 5 (`S1:488–499`: "Ah. You're real." / "Two years of your handwriting, by post"). With Wanted 0 and Heat 0–3, a 1–3 comes up 75% of the time, and both rows in that cell use a Greta phone line (`Entanglement-and-Complication-Cues.md:16`, `:20`). That spoils her debut and contradicts "by post".
**Fix:** add to `S1:465`: "S1 only: hold the Entanglement until Step 5 (SRD lets you 'hold off until an appropriate moment'). Greta delivers it **in person**, after 'Ah. You're real.' Never as a phone call before Step 5." Add the same S1 exception to the Cues rules line (`Cues:9`).

## HIGH

**H1. The XP track rule contradicts the SRD.** `End-of-Session-Ritual.md:12` says "XP from the end-of-session triggers goes on the **playbook track**". The SRD (line 891) says "any xp tracks you want (any attribute or your playbook xp track)". House-Rules A2 says we follow it exactly. The line also says "Desperate rolls already gave XP" twice.
**Fix:** "…1 XP if it happened, 2 if it happened a lot; mark it on **any track** (an attribute or the playbook track). Desperate-roll XP was already marked on the attribute in the moment."

**H2. Advancement is "deferred" while XP now fills tracks from S1.** A playbook track (8) can fill at the S2 close (up to 6 trigger XP per session plus Train). Yet `Mechanics-Teaching-Ladder.md:30` lists advancement under S3 **Defer**, `:31` puts it at S4+, and `Ladder-S4-Plus.md:14` lists it under S4. A fresh Co-GM would refuse a full track, which breaks the SRD.
**Fix:** `Ladder:30` Defer → "Trauma tables". `Ladder:31` → "advancement *(if no track filled earlier)*". `S4-Plus:14` → "(advancement: whenever a track first fills, from S2)". In the S2 and S3 XP lines (`S2:550+`, `S3:427`), add: "If a track fills, teach card 22 (`Mechanics-Teaching-Ladder-S4-Plus.md`) now. It counts as one of tonight's new lessons."

**H3. S2 and S3 put the steps in the wrong order on the page.** `S2:494–495` and `S3:392–393` give the activities SAY and `ASK EACH PLAYER` first. The Entanglement block comes next (`S2:506`, `S3:395`) and Heat after it (`S2:508`, `S3:397`). Read top-down, that runs activities → Entanglement → Heat. The SRD order is Heat → Entanglement → activities.
**Fix:** move the HEAT block, then the ENTANGLEMENT block, **above** the activities SAY in both files.

**H4. S3 still schedules the S3 Entanglement for S4.** `S3:403`: "**Next:** roll the Entanglement at the start of Session 4's Downtime". With `S3:395` ("roll it now"), the same score gets rolled twice.
**Fix:** delete `S3:403`, or change it to "Session 4 rolls its own Entanglement after the S4 score."

**H5. The S1 Entanglement guidance targets the wrong people and the wrong column.**
- `S1:465` says Gerald is the cohort. That is only true if the crew **kept** him (`S1:400–403`).
- It says "no contact yet". In fact every PC has a playbook Friend and a Vice Purveyor (`_PC-Template.md:34`, `Character-Creation-Guide.md:13`), and several suggested Friends are canon NPCs: Greta, Harlan, Kress, Drennick, Foss, Cosma (`Playbook-Hooks.md:33–63`). Usual Suspects or Flipped on Kress or Greta would leak or derail canon.
- "choose a neighbour row" breaks the SRD, and Flipped/Questioning are not in the 0–3 column at all.
- S1 Heat can reach 6+ under the SRD formula (loud 4, +2 killing if the Gland is taken, +2 for filing nothing). `Clocks-Calendar.md:32` assumes +0/+2. At 6+, Flipped/Interrogation is 75% likely.

**Fix:** replace the GM ONLY line with:
"🔒 Expected S1 Heat is 0–2 (Ministry-sanctioned; +2 if they file nothing). Inside the rolled cell, pick the option that fits:
- Gang Trouble only if Gerald was kept.
- Otherwise The Usual Suspects on a PC's **non-canon** Friend or Vice Purveyor (never Greta, Harlan, Kress, Drennick, Foss or Cosma).
- If neither fits, there is no entanglement tonight ('A quiet night').

At 4–5 use Gang Trouble/Questioning by the same test. At 6+ use Interrogation: it is Ministry, so tick Audit silently, and offer Resistance."

Also state at `S1:460` that the killing modifier does not apply to a sanctioned extraction, if that is the intent.

**H6. S1 breaks the per-beat cap.** `Ladder:10` allows "Max 2 new mechanics per beat". The Downtime beat now teaches Heat, Entanglement and Vice (plus the activity menu). The "four lessons" bundle hides about ten mechanics.
**Fix:** merge the Heat and Entanglement SAYs (`S1:459`, `S1:463`) into one ≤30 s line: *"Heat is the attention you drew. After every score I roll for the trouble that follows you home, an Entanglement; more Heat, worse trouble."* Drop the Wanted clause (card 24 teaches Wanted at the first Heat 9). Note in `Ladder:28` that Heat + Entanglement is one card.

**H7. The S1 time budget has no room for the new steps.** `S1:19` totals ≈2h35 and has no Close line. Nobody has budgeted the Entanglement (~5 min) or the first-time XP tally plus retrospective (~10 min). The cut-list (`S1:20`) protects neither, and its item 5 (C9 text mode) does not say the Entanglement still happens.
**Fix:** `S1:19` → "…Downtime 35 (incl. Entanglement 5) → Close: Zoltar + XP + retro 10 (≈2h45 + slack)." Add to `S1:20`: "Never cut the Entanglement roll or the XP tally. Resolve the Entanglement with its SRD ways out in one exchange, and shrink the retro to one question."

## MEDIUM

**M1. Heat-and-Entanglements.md:41** says "Pick the row that fits the fiction first; roll when nothing suggests itself." That deviates from the SRD, contradicts A2 and S1–S3 ("ASK THE GM TO ROLL").
**Fix:** "Always roll. Where a cell offers two, pick the one that fits the fiction."

**M2. The Audit clock can fill while still secret.** Possible pre-S4 ticks: DB (S1) plus one Ministry Entanglement per score (S1, S2, S3) = 4, which fills the 4-segment clock and locks the shop before S4. `Clocks-Calendar.md:32` (S1 row) does not list Entanglement ticks.
**Fix:** add to `Active-Clocks.md:69` and `Heat-and-Entanglements.md:39`: "Before S4, silent ticks never take Audit past 3." Add "+1 on a Ministry Entanglement" to Calendar rows S1–S3.

**M3. Ladder card 13 (`Ladder:92`)** says "you roll to see *which* trouble comes". The GM rolls (House-Rules §B).
**Fix:** "I roll…".

**M4. The dashboard's taught-mechanics panel is stale.** `GM-Dashboard.html:102` reads `'Entanglements  (S3)'`, and there is no XP-tally row. The Co-GM logs teaching here (`Ladder:135`).
**Fix:** relabel it `'Entanglements  (S1)'` and add `{ id: 'xptally', label: 'XP tally (S1 close)', state: 0 }`. Bump `SAVE_VERSION`.

**M5. The run sheets and budgets were not updated.**
- `S1:37` Teaches → "**Heat → Entanglement → Vice**".
- `S3:34` (8b) add "Entanglement". `S3:35` (Close) add "XP tally".
- `S3:19`: "Briefing + new mechanics 15" → 10, "Return + Downtime 20" → 25, "Close 5" → 10.
- `S2:19`: note that "Return … Close 35" now holds the Entanglement and XP (or raise it to 45 and cut the optional Aldric beat first).

**M6. S3 "Before We Go In" still reads as a live beat.** `S3:145` keeps `❓ ASK THE GM TO ROLL` + ⏸ inside the briefing, and the 0–3 examples at `S3:147–148` don't match their rows. A "referral fee" is not Gang Trouble or Usual Suspects, and an Apex officer asking questions is Questioning, not Rivals or Unquiet Dead.
**Fix:** move the ASK line to `S3:395`. Replace the examples with a pointer to `Entanglement-and-Complication-Cues.md` §A.

## LOW

- **L1.** `Ritual:14`: the compound question is written as a SAY. Make it `❓ ASK EACH PLAYER (one at a time): "Which of your triggers happened tonight?"` ⏸, then "Once, or a lot?" ⏸.
- **L2.** `S1:368`, "At the Close, 'Mark any Desperate XP now'": the SRD marks it in the moment. Change it to "At the Close, check Desperate XP was marked."
- **L3.** `Playbook-Hooks.md:56` "*S3* — the Entanglement/Acquire Assets session" → "the Acquire Assets session".
- **L4.** `File-Index.md:49` "(S4+)" → "(XP tally S1; the rest S4+)".
- **L5.** `Ladder:79`: retitle card 9 "Heat, Entanglement & Vice (S1 Downtime)".
- **L6.** `Cues:28`: the Interrogation clock is "wrong by eleven minutes". That is the Omen's 11:47 motif, and S3 debuts it. Use "wrong" without a number before S3.
- **L7.** `Cues:24`: Fitch Ambrose is a Requisitions bench clerk (`Ministry-Org-Chart.md:23`), not an inquiry officer. Use "a Ministry clerk".
- **L8.** `Heat-and-Entanglements.md:34` / `Cues:46`: Demonic Notice before the S2 first descent must use the Omen, never "the Subway through PTOLEMY's ledger" (the Subway-Adjacent gate at `Cues:90`).
- **L9.** The swept files (Session-Writing-Rules, Express-Ending-Kit, Live-Ledger, Campaign-Arc, Season-1-Plan, GM-Rules-Reference, Campaign-Bible-Appendix, Session-Boot, CLAUDE.md, House-Rules, Secrets schedule row 28) have no stale "skip/defer XP or Entanglement" text. The SRD restatements of Heat columns, Wanted-0 dice, ways out, crew triggers and incarceration are correct apart from H1/M1.

**Counts: BLOCKER 1 · HIGH 7 · MEDIUM 6 · LOW 9 (23 total).**
