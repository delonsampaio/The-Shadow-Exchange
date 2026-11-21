# Opus Beat-by-Beat Audit: Report (Sessions 0–3), 2026-11-21

**Scope:** the Session 0–3 preps, checked against classes A–M plus the extra checks (forced Downtime, Tells, plants, Audit vs Ladder). I read:
- all 33 cued images
- Hunter-Kit, Three-Layer-Monster, Bestiary and the Ladder
- the `GM-Dashboard.html` INIT_* ids

Not opened: `scene.js` and `feed.js`. `S1:123` means `05-Sessions/Session-01-Prep.md` line 123.

## BLOCKER

**B1 (A, S1). The Gerald image stays on the TV through the 🔴 locker.** `S1:266` only says `npc-merton-human` is "held here". Nothing clears `npc-gerald-dog` (`S1:234`), and the Run Sheet's "title card, Locker 7" (`S1:32`) is missing from the body. **Fix:** replace `S1:266` with `**[IMAGE CUE: location-merton-locker.png]** ❌ *(until it exists: title card, image null, caption "Locker 7"; clears Gerald)*`.

**B2 (E, S1). Devil's Bargain, lesson 2, has no player line.** `S1:256` has only a GM note: "Devil's Bargain offer here". **Fix:** 🗣 SAY *"I can offer you +1 die now if you accept a complication whatever the roll: here, Detection ticks. You can always say no."* ❓ *"Do you take it?"* ⏸

**B3 (E, S1). Desperate = XP, lesson 4, is never taught.** It is mentioned only at `S1:8/33/40/335/360`, and no beat holds Ladder card 17b. **Fix:** at the first Desperate roll, 🗣 *"Whenever you roll a Desperate action, you mark 1 XP in that action's attribute, win or lose."* At Close: "Mark any Desperate XP now."

**B4 (E/K, S1+S3). The Audit clock is public, unexplained, and against the Ladder.** The dashboard has `aud` with `secret: false`. Ticks are scripted at `S1:383`, `S1:468` and `S3:149`, but the Ladder (line 31) defers Audit clocks to S4+. This is the open TODO. **Recommended fix:** keep `aud` GM-secret until S4 and mark "🔒 secret until S4" at those three lines. The first-appearance SAY goes in S4. *Alternative:* one line at Double Bookkeeping, *"That's the Ministry Audit: four segments; when it fills, the Ministry comes to go through your books."*, then amend Ladder row 1.

## HIGH

**H1 (L Menace, S1). The "aftermath only" gags describe a live Surge.** `S1:343` says aftermath. But `S1:348` ("Merton… can't see either"), `S1:349` (the trapdoor bargain) and `S1:350` ("you and Merton circle each other") are mid-Surge. `S1:357` puts the trapdoor in the Surge bargain menu, and `S1:20` says "gags in the Surge". **Fix:**
- Drop the trapdoor from `S1:357`.
- Rewrite `S1:348–350` without Merton: "the stage turns slowly with all of you on it, and Gerald".
- `S1:20` → "aftermath gags".

**H2 (Downtime, S2). Vice is forced (regression of mock #29).** See `S2:476` and `S2:478` ("Vice is one of them"). **Fix:** 🗣 *"Everyone gets two Downtime activities, any two. Indulge Vice is recommended if you're carrying Stress."*

**H3 (Downtime, S3). The same forcing at `S3:384`.** **Fix:** *"…two Downtime activities, any two: Indulge Vice (recommended with Stress), Recover, Reduce Heat, a Long-Term Project, Train, or Acquire Asset."*

**H4 (Tell 4, S2). "Tuesday" is ambiguous.** `S2:512` makes two references ("the thing on Tuesday… Last Tuesday's conversation"). If the S1 job fell on a Tuesday, the crew *did* talk to Thorne. `S2:517` ("no conversation") contradicts `Elias-Thorne.md:49` ("remembers differently"). **Fix:** *"Thanks again for dropping by my office on Tuesday. You seemed rattled."* (They have never been there.) Align `S2:514/517` and the NPC file.

**H5 (E, S2). Twice-Born Favor is never taught.** `S2:34` assigns it to Cosma, but `S2:390–406` has no Favor line; it first appears as a GM note at `S2:208`. **Fix:** after Cosma, 🗣 *"Protecting a Twice-Born earns a Favor, up to 3. Spend them for safe harbor, rare gear or lore. They also notice what you do."*

**H6 (E, S3). Push Yourself is never taught.** It is listed at `S3:7` and on the dashboard (`push`), but no beat teaches it. **Fix:** at `S3:140`, 🗣 *"You can push yourself: 2 Stress for +1 die or +1 effect, before the roll."*

**H7 (G, S2). The "Wait for him to leave" approach is impossible.** `S2:183` says "take the thimble when the shop is empty", but the thimble is on his hand (`S2:175`). The Seize read-aloud (`S2:212`) has him behind you and a child's uniform on the table. **Fix:** `S2:183` → "**Wait for the shop to empty**: you get him alone". Add a variant to `S2:212` with no child.

**H8 (H, S2). No lethal path for Emmerich or Drennick & Foss.** **Fix:** add 🔒 IF THEY FIGHT TO KILL blocks.
- *Emmerich:* doesn't resist; one Risky/Standard roll; +2 Heat, Twice-Born Enmity, Detection +2 (the child and her mother witness it).
- *D&F:* Skirmish is Desperate/Limited; their blows are Level 2 harm. A kill means +2 Heat, Apex −2 and a Wanted check. Offer Resistance first.

**H9 (H, S3). No lethal path for Mabel or D&F, although "Breach and clear" (`S3:192`) invites a fight.** **Fix:**
- *Mabel:* blows pass through her; only the needle or salt works. Attacked, she goes cold: Desperate, Level 1 cold harm. "Killing" her means taking the needle by force (Option A; the Twice-Born note it).
- *D&F:* same block as H8.

**H10 (A, S3). The Agnes image stays up into the 🔴 pivot.** `S3:302` cuts only the music. `S3:315` gates the wraith image behind "only if". **Fix:** at `S3:314`, add `[IMAGE CUE: npc-mabel-ashby-alive.png] (on "go"; clears Agnes)`.

**H11 (M, Bestiary). None of the 40 entries says how the cover slips.** All 40 name an Anchor, but none states the slip required by `Three-Layer-Monster.md:30`, and the header (`Bestiary.md:9`) doesn't cite the rule. **Fix:** add "**Slip:** …" to each "Is:" line, and cite the rule in the header.

## MEDIUM

**M1 (F, S1). The theater is never named (mock #9 still open).** `S1:102/109` never says the Fairground Grand, yet `map-city-s01` puts a red X there. **Fix:** at `S1:109` add *"(it reads: FAIRGROUND GRAND THEATER, STAGE DOOR)"*.

**M2 (E, S1/S3). Load is listed as taught and deferred at once.** `S1:40` says lesson "(1) Load + Flashback", then "Load… deferred". `S3:7` defers Load, and so does Ladder line 28. **Fix:** delete "Load" from those three defer lists.

**M3 (E, S1). Bernard can tick Detection before Gerald's clock lesson.** He does so at `S1:220`; the lesson is at `S1:256`. **Fix:** at `S1:220`: "(first tick? run the clock SAY now)".

**M4 (E, S1). Harm and the Subdue clock have no player line** (`S1:324/334–335`). **Fix:**
- At the first harm: 🗣 *"That's Level 2 harm: write it down; −1d where it hurts."*
- At the first Subdue tick: *"A third clock: how hurt he is. When it fills, he's down."*

**M5 (E, S2). There is no Detection reminder line (open TODO).** It ticks at `S2:255`. **Fix:** 🗣 *"Detection again: four segments. Fill it and Apex has you."*

**M6 (G, S1). Merton's "man" beat assumes the collar was taken, and contradicts itself.** `S1:290` has "his eyes go to your hand, to the collar". `S1:293` has him take it down himself. Then `S1:310` lifts it "from its nail" again, while `S1:306` says his hands are "open and empty". **Fix:**
- Branch `S1:290`. If nobody took it: "…the collar already in his hand…".
- Replace `S1:310` with "He holds the collar out in both hands."
- Note that the Surge still comes because the collar is cracked, not whole.

**M7 (G, S1). The Choice assumes the Gland, and Double Bookkeeping is rolled twice.** `S1:375` has no no-Gland variant. Sway is rolled at `S1:374/383` and again at `S1:467`. **Fix:** add "(no Gland) Take the collar and file nothing", and make Step 4 "only if not rolled at Beat 7".

**M8 (C, S1). Read-alouds narrate PC actions.**
- `S1:182`: "You move… kit under coats". It also clashes with the van at `S0:148`.
- `S1:192`: "you adjust your pace".
- `S1:216`: "Bernard looks at the badge", which assumes it was shown.

**Fix:** cut the PC clauses; `S1:216` → "Bernard looks at whatever you're holding up, then at the kit."

**M9 (C, S2). The partial option narrates the telling** (`S2:220`: "you tell him first"). **Fix:** ❓ *"Who tells him, and what do you say?"* ⏸, then "He nods, as if he had expected both halves."

**M10 (G, S2). Foss says "Unlicensed extraction detected" in every branch** (`S2:243`). **Fix:** mark it "(seized/partial only)"; the warn branch uses `S2:245`.

**M11 (Tell 3, S2). The window is ambiguous.** `S2:146` has "at the building… the second-floor window", but the shop is described only afterwards (`S2:159`). **Fix:** *"He looks past you, up at the gold leaf on the second-floor window, EMMERICH & DAUGHTER, the address in your envelope. He looks for slightly too long."*

**M12 (Tell 5, S3). Two gaps, and one unclear line.**
- No variant covers a PC who told Thorne about the pier on the S2 call.
- "The other night" (`S3:403`) breaks if Downtime spanned weeks.
- "Hard sell for the neighbors" (`S3:402`) is unclear.

**Fix:** *"And I hear you came up on the eastern pier all right, after the Meridian."* Add a GM variant: "If a PC told him about the pier, swap in 'Nothing down there but the old drainage tunnels' (nobody mentioned tunnels)." Reword `S3:402`.

**M13 (J/F, S2+S3). Same gap as mock #8.** The approach menus `S2:182–187` and `S3:190–200` have no stall help, no default, no Engagement roll and no Load pick. **Fix:** copy the S1 stall block (three details per plan, ±1d, a default pick) and add ❓ *"Light, Normal or Heavy?"*

**M14 (I/A, S0). The Consequence image shows her asleep; the text has her awake.** `npc-consequence.png` shows her asleep on a 1962 catalog, but `S0:381/384` has her awake and staring. That catalog is Beat 5's default spot (`S0:428`), and Beat 5 has no TV state (`S0:35`). **Fix:** run 4b on a title card with the caption "Consequence"; cue `npc-consequence` at Beat 5.

**M15 (I, S1). The Merton image doesn't match his entrance.** `npc-merton-human.png` shows him seated at his third-floor desk by a window. `S1:290` has him standing in the basement corridor with keys. **Fix:** caption "Merton" for now, plus an image TODO (standing, corridor, keys).

**M16 (I, S2). The Emmerich images contradict the observation.**
- `npc-emmerich.png` shows him alone at night. The text (`S2:173`) has a child and her mother, mid-morning.
- `location-emmerichs-shop.png` shows a ground-level window at night; the text says second floor (`S2:159`).

**Fix:** keep `location-meridian-street` (its sign is on the second floor) up through `S2:159`. Cue `npc-emmerich` after the child leaves. Log TODOs for both images.

**M17 (I, S2). Thorne's street image is the S1 backstage shot.** It shows a clipboard and the stage door; `S2:142` has coffee cups outside a café. **Fix:** caption "Elias Thorne" over the street image, plus an image TODO.

**M18 (A, S1). The Thorne image stays up through Mara and Downtime** (`S1:36` "—"). Mara's face must never show. **Fix:** at `S1:427`, TV: title card, caption "The alley". At `S1:443`, `location-curios-exterior`.

**M19 (L, S2). The Gland's storage contradicts S1.** `S2:66` puts it in the "Cold Storage Locker"; `S1:376` keeps it in the cold cellar until S4 teaches the Locker. **Fix:** "in the runed cold drawers".

**M20 (B, S2). The Return read-aloud is unlabelled** (`S2:468–471`). **Fix:** add `> 🔊 **READ ALOUD:**`.

**M21 (K, dashboard). Dashboard ids are missing.** INIT_TAUGHT has no `load`, `clocks` or `despxp`. There is no `subdue` clock (`S1:334`) and no Stalls tally gag (`S3:136`). **Fix:** add them and bump SAVE_VERSION.

**M22 (L, S3). The Entanglement table isn't SRD.** `S3:146–148` uses 1–2/3–4/5–6 and ignores the Heat column named in `S3:145`. The Audit tick at `S3:149` floats free of any result. **Fix:** use the §2 rows of `Heat-and-Entanglements.md` (1–3/4–5/6) by Heat column; tag the tick "(5–6 only)".

**M23 (L/I, S3). The Extraction skips the Anchor Cover Rule slip.** `S3:338` never shows Mabel thinning. `npc-mabel-ashby-wraith.png` (translucent, reaching for the needle) is exactly that moment, but it is gated at `S3:315`. **Fix:** append *"The light goes through her. She is thinner each time you look."* and cue the wraith image there.

**M24 (G, S3). The Thomas option's conditions differ.** `S3:326` includes an opened jar; `S3:333` does not. **Fix:** add "or a Grief Jar memory" to `S3:333`.

**M25 (G, S3). The 11:47 clocks appear only on the Watch-first branch** (`S3:196`), so the Omen echo (`S3:396/425`) is lost otherwise. **Fix:** at `S3:215`: "Every clock in the hall reads 11:47."

**M26 (plant, S1–S3). The Mara plants are unwritten.** `S1:435` promises she reappears in S2–3. S2 has only a roster note (`S2:86`), with no read-aloud and no PURPOSE line. S3 has nothing. **Fix:** write an S2 glimpse with a 🔒 PURPOSE line, and add an S3 glimpse or move the promise.

## LOW

- **L1 (B):** the Cold Open "Remember:" bullets are unlabelled (`S1:54`, `S2:55`, `S3:51`); prefix 🔊.
- **L2 (B):** the card drops twice (`S1:491` and `S1:494`); cut it from 491.
- **L3 (C):** `S0:137` "The three of you stare back" narrates the PCs. Tolerable, because `S0:141` asks who.
- **L4 (F):** `S1:384` "rune-thread from the Containment Suite kit" → "from a PC's load, or a Flashback". `S2:159` mentions scanner readouts, but no portable scanner is in the kit.
- **L5 (L):** `S3:396` "No one was in the shop overnight", but the crew sleeps upstairs (`S0:268`).
- **L6 (G):** Greta arrives twice (`S3:62` vs `S3:117`). `S3:348` assumes the Dampener was acquired.
- **L7 (A):** no TV state for the S3 second Subway visit (`S3:87–100`); no clear point for the S2 contract card (`S2:109`).
- **L8 (I):** minor image drift.
  - Zoltar: cards and a lit lamp vs `S0:160`.
  - D&F: the tall one holds the clipboard (`S2:242` says the shorter one).
  - Cosma: seated, not walking.
  - Grief Jars: far more than 43.
  - `map-city-s03`: the past pier has a red (current-target) X.
- **L9 (G):** Drennick's "where'd they go?" (`S2:305`) fires before the descent.
- **L10 (L):** `S2:403` has a joke ("interest is metaphorical") on the first Subway visit.
- **L11 (H):** the kill Heat at `S1:337` could be read as +4; say "+2 total".

**Clean:** class D; no subway system (`S0:118`, `S2:132`); no Decay in S0–S3. These images match their text: containment suite, auditorium, Gerald, collar, PTOLEMY, pier, Stalls, Agnes, needle.

## Counts

**By severity:** BLOCKER 4 · HIGH 11 · MEDIUM 26 · LOW 11 = **52**

**By class:**

| Class | Count |
|---|---|
| A (TV state) | 4 |
| B (labelling) | 3 |
| C (narrated PC actions) | 3 |
| D (missing "before" state) | 0 |
| E (first-appearance explanations) | 9 |
| F (items established) | 2 |
| G (branches assuming a choice) | 8 |
| H (lethal paths) | 3 |
| I (image vs read-aloud) | 5 |
| J (stall help) | 1 |
| K (dashboard ids) | 1 |
| L (canon / Menace Rule) | 6 |
| M (Bestiary) | 1 |
| Extra checks (Downtime 2, Tells 3, plants 1) | 6 |

**By session** (each finding counted once, by primary file): S0 **2** · S1 **19** · S2 **17** · S3 **13** · Bestiary **1**.

**Mock-log TODOs:**
- S2/S3 clock lines: still open (M5, B4).
- Audit vs Ladder: still open (B4).
- Mock #9: still open (M1).
- Optional images: still ❌. Because of B1, the locker caption is mandatory until the image exists.


---

## Claude triage (2026-11-21): applied

**All 4 BLOCKERs and 11 HIGHs fixed; 24 of 26 MEDIUMs and 8 of 11 LOWs fixed. Nothing rejected. Two design choices adopted on the GM's standing "do what is best".**
- **B1** locker image clears Gerald (title card, "Locker 7"); **B2** Devil's Bargain player line; **B3** Desperate = XP line and a Harm and Subdue line at their first use; **B4** the **Ministry Audit clock is GM-secret until S4** (dashboard `secret: true`, notes at S1, S3 and the Ladder; explanation deferred to S4). *Design choice: kept it secret rather than explaining it in S1.*
- **H1** aftermath-only gags rewritten without Merton and the trapdoor bargain dropped; **H2/H3** Downtime is free choice in S2 and S3; **H4** Tell 4 is now "Thanks for dropping by my office last Tuesday" (a visit that never happened), aligned in `Elias-Thorne.md` and the Arc; **H5** Favor line after Cosma; **H6** Push Yourself line in S3; **H7** "Wait for the shop to empty" plus a no-child seize variant; **H8/H9** fight-to-kill blocks for Emmerich, Drennick and Foss, and Mabel; **H10** Agnes image cleared by `npc-mabel-ashby-alive` at the pivot; **H11** the Bestiary header cites the Anchor Cover Rule with a default slip (**per-entry slips still to write**).
- **MEDIUM:** theater named on the envelope (M1; closes mock #9); Load removed from defer lists (M2); Bernard first-tick note (M3); harm/Subdue lines (M4); Detection reminder S2 (M5); Merton "man" beat branches and open hands fixed (M6); no-Gland menu and Double Bookkeeping rolled once (M7); narrated PC clauses cut (M8, M9); Foss line gated (M10); Tell 3 window (M11); Tell 5 (M12); stall help and a Load pick for S2 and S3 (M13); S0 Consequence image held for Beat 5 (M14); Merton image mismatch (M15) and S2 Emmerich/Thorne image drift (M16, M17) handled by captions plus TODOs; Thorne image cleared at Mara and Downtime (M18); Gland storage wording (M19); Return label (M20); dashboard ids added (M21); S3 Entanglement table is SRD (M22); Mabel thinning (M23); Thomas option condition (M24); 11:47 clocks everywhere (M25); Mara plants written in S2 and S3 with a PURPOSE line (M26).
- **LOW:** Cold Open bullets labelled (L1), duplicate card (L2), kit wording (L4), "No one touched it" (L5), joke removed from the first Subway visit (L10), Heat wording (L11).
- **Still open (LOW, logged):** L3 (tolerable), L6 (Greta arrives twice in S3; the Dampener is assumed acquired), L7 (a TV state for the S3 second Subway visit and the S2 contract card clear point), L8 (minor image drift: Zoltar, D&F, Cosma, Grief Jars, `map-city-s03`), L9 (Drennick "where'd they go?" fires before the descent).
- **New optional images to generate:** `npc-merton-corridor` (standing, basement, keys), a Thorne-with-coffee street shot, an updated Emmerich shop image (second floor, daytime, child and mother).
