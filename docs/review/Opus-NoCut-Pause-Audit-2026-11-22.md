# Opus audit: "nothing is cut" and the Pause (commit 7ef0498), 2026-11-22

Report only. I verified every claim below by reading the line. I did not read `scene.js` or `feed.js`.

## BLOCKER

**B1. The S2 railing stop ends the night on the reveal.** `Session-02-Prep.md:20` says "(A) the railing: after the Door Chase, when the alley dead-ends and the railing is there". The railing is the campaign's first impossible thing (`:323–327`). Stopping there also leaves a pursuit running (Detection, Foss at the mouth `:300`), the Twist flashback ask pending (`:309`) and "whether they go down" undecided (`:339`). `:516` says the entrance "lands best as a surprise *mid-flight*". S2 is the prep the file itself expects to take two nights (`:19`), so this is the stop most likely to be used.
*Fix:* replace (A) with "after the Emmerich Choice: the matching passage read (`:231–248`), before the crew leaves the building; resume with the Door Chase (caper music inline)". Add "(A2) after Cosma's Favor lesson, before Aldric and the Job Board" so that `:13` ("can be a second-night opening") points at a real stop.

**B2. Nothing tells the Co-GM how to pause or resume, and the existing commands do the forbidden things.** `Weekly-Prep-Checklist.md:10` says "Say **"end session"** … if it was not run". `Session-Boot.md:178` maps "end session" to §6, and §6 step 0 (`:192`) runs the Ritual, which includes Zoltar and XP. `:11` asks for the Faction Turn and `:12` publishes a recap after every evening. On the next evening, "start session N" (`Weekly-Prep:27`, `Boot:165`) boots from `Campaign-Current-State.md`, readies the Cold Open (`Boot:31`) and presents the first beat (`:34`). The §5 table (`:161–186`) has no "pause" command. "resume" (`:185`) only covers a context reset.
*Fix:* add to Boot §5 `"pause here" / "stop for tonight" → Ritual §0b only` and `"continue session N" → Boot 3b + the Previously card; do not re-read the Cold Open; start at the beat saved in the Night Log`. Make `Boot:178` conditional: "end session (only when the session is finished; otherwise §0b)". Rewrite `Weekly-Prep:9–12` as "after a **finished** session". Add a line: "after a Pause, nothing here runs except checking the Night Log row".

## HIGH

**H1. The "Previously" card has no source in the middle of a session.** `Boot:34` and `CoGM-Core-Instructions.md:76` say it is written "only from the public player recap (the one published to the wiki)". `Core:76` also says "Skip it for Session 0/1". A paused S0 or S1 gets no card, and no wiki recap exists until a session finishes (Boot §6 step 5).
*Fix (Core:76, Boot:34):* "When resuming after a Pause (any session, S0 included), build the card from the Pause's one-line recap (Ritual §0b), which is written player-safe and checked against `spoiler-words.txt` when it is logged."

**H2. Nothing says what happens to the screens and files at a Pause.** Ritual §0b (`End-of-Session-Ritual.md:12`) says only "title card … Live Ledger current". `Boot:201` (reset `scene.js` and `feed.js`) and `Change-Propagation-Map.md:45` (clear the ledger and reset both) sit in the close-out. A Co-GM who treats the end of the evening as close-out will wipe the state that the 3b resume needs (`Boot:20`). On step 6's question: **a Pause must keep both files.**
*Fix (add to §0b):* "Do **not** reset `feed.js`, edit `INIT_*`, bump `SAVE_VERSION` or clear `Live-Ledger.md`. Set `scene.js` to `card:{style:'note', title:'To be continued'}`, `clocks:[]`, `crew:null`. Ask for the dashboard's 'Copy end-of-session snapshot' and paste it into the Live Ledger, along with the GM-private resume state (Load and engagement Position, live clock values, held results, who has which item)." Add a "Pause" row to the Change-Propagation-Map, and in `Live-Ledger.md:3` change "cleared at close-out" to "at a **finished** session's close-out".

**H3. The hard stop and "play to the next safe stop" conflict.** `House-Rules.md:42` says "Never run more than 15 minutes over". `Boot:153` only offers the *next* safe stop. The gaps between stops are long: S2 (A→B) is the whole Subway, about 70 minutes; S0 (A→B) is about 55 minutes. The GM then has to choose between running over and stopping somewhere unsafe.
*Fix (Boot 7a):* "About 45 minutes before the agreed end, name the last safe stop that can be reached in time. If none can, offer to stop at the previous one."

**H4. House-Rules C7 still shortens play.** `House-Rules.md:42` reads "offer 'cliffhanger here, or a five-minute fast-forward?'" A fast-forward is a shortening, and an unchosen "cliffhanger" can fall on a reveal.
*Fix:* "Hard stop at the agreed time: stop at a safe stop and run the Pause (C9). Never fast-forward."

**H5. Cut and skip wording is still in the preps.**
- `Session-03-Prep.md:130` says "skip if time is short — he reappears in Session 4". *Fix:* "played if the crew takes the meeting".
- `S3:89` says "Only if Session 2's Aldric / Job Board / Broker beats were cut". *Fix:* "if the crew asks to go back".
- `S3:95` says "If the crew never made the S2 descent (it was cut)". *Fix:* delete the sentence.
- `S2:35` (row 11 "*(optional)*") and `S2:462` ("The Broker *(optional — one nod…)*") contradict `S2:13` ("played too"). *Fix:* "*(player-driven: offered in full; played if the crew engages)*". `:446`/`:452` (Aldric "DO NOT FORCE", Job Board "only if the crew looks") are player-gated, not cuts, and should stay. Say so in `:13` so a Co-GM does not force them.

**H6. The players' site still promises the old short night.** `../The-Shadow-Exchange-Players/docs/House-Rules.md:20–21` reads "five-minute fast-forward" and "Short night (90 minutes): … downtime as one sentence per person". *Fix:* update it through `Wiki-Update-Protocol.md` to "Nothing is cut; a session may take two evenings; we stop at a safe point and pick up next time".

**H7. The XP and retrospective questions say "tonight".** `Ritual:18` ("Which of your triggers happened tonight?"), `:19` (crew XP) and `:27`. When a session took two sittings, players will count only the second evening.
*Fix:* "…happened **this session** (both evenings, if it took two)?" Before the ask, the Co-GM reads the first sitting's highlights from the Live Ledger in one SAY.

## MEDIUM

**M1. The Night Log contradicts itself and is missing questions.** `Night-Log.md:9` says "One line per sitting", but `:21` says "Two sessions in one night … log them as separate lines". `:21` also duplicates `:22`.
*Fix:* delete `:21`, and in `:22` add "if a session ends mid-sitting, run its full close there, then continue". Add the questions ❓ "Is the session finished?" and, on a Pause, "Resume at which beat?". Add a "Resume beat / recap line" column so the next boot has one source.

**M2. The Faction Turn is left out of four lists.** `Boot:153`, `House-Rules:44`, and the safe-stop lines `S0:21`, `S1:20`, `S2:20`, `S3:20` all list "Zoltar, XP, retrospective" only. `Ritual:12` and `Night-Log:22` include the Faction Turn. *Fix:* add "and the Faction Turn" to each.

**M3. S1 (B) "before the Choice" is legal but the weakest stop** (`S1:20`). It breaks the 🔴 run from Beat 5 to Beat 7 (Merton: "I have a few minutes", `:321`). It is unclear whether the aftermath gags (`:349–357`) run before the stop, and Merton may be "gone within 1d6 hours" (`:337`).
*Fix:* "(B, last resort) after the aftermath gags; log Merton's state (down, held or soothed; collar; Surge and Subdue values); resume with one 🔴 READ ALOUD line of the stage, then Beat 7 'go'."

**M4. S1 (C) is ambiguous.** It reads "after … Thorne's debrief, before Downtime" (`S1:20`), but Beat 9, Mara (`:438`), sits in between. "Greta's scene and the held Entanglement are one unit" does not forbid a pause between the roll (`:468`) and Greta (`:497`).
*Fix:* "(C) after Beat 9 (Mara)". Then: "Downtime Steps 1–5 are one unit; never pause between the Entanglement roll and Greta."

**M5. S3 (B) "before the Moral Pivot" breaks the beat's design.** `S3:321` says "When Agnes leaves: CUT the comic music … *Laugh, then land.*" The crew is also mid-score: Load, Detection, the hum, and possibly the November 1991 jar reveal just before Agnes (`:289`). The "one line of the house" in `S3:20` is never written.
*Fix:* mark (B) "last resort" and write the re-entry 🔊 line (e.g. "The house is quiet. Every clock reads 11:47. Mabel stands in the kitchen doorway with the teapot."). Never stop there if the November 1991 jar opened that sitting. Add "(B2) after the Pivot's matching read-aloud, before the Return".

**M6. S0 tells the table to hurry.** `Session-00-Prep.md:89` says "Cap each introduction at about 2 minutes. If someone runs long: SAY 'Great — we'll see more in play. Next.'" That contradicts rule 7a. *Fix:* delete it, or soften it to "if an answer stalls, offer the stall menu".

**M7. Leftover short-session tools.**
- `Improv-Kit.md:113` says "in 90 minutes, merge steps 4–5". *Fix:* "on a short evening, stop after step 3 or 4 and Pause".
- `Evergreen-Episodes.md:4` lists "or a short session" as a use. A short evening continues the prep in progress. *Fix:* delete.
- `Boot:182` still has the "short session" command. *Fix:* rename it "short night" and point it at C9.

## LOW

- **L1.** `Ritual:9`: change "cliffhanger or close → Zoltar" to "the session's last beat → Zoltar".
- **L2.** `_Dictionary.md` has no entry for *sitting*, *safe stop*, *Pause* or *Previously card*, although `Change-Propagation-Map:38` requires one. *Fix:* add them.
- **L3.** `docs/tools/stale-phrases.txt` misses the variants above. *Fix:* add "skip if time is short", "beats were cut", "(it was cut)", "five-minute fast-forward", "short session", "in 90 minutes, merge".
- **L4.** `House-Rules:39` says "next week's cold open". Make it "the next session's cold open". `House-Rules:45` (absent player): say whether half XP is per session or per sitting.
- **L5.** `S3:20`, "Keep the Parish Records available", is left over from the cut-list. It can go (`:157` already covers it).
- **L6.** `Express-Ending-Kit.md:10` treats sessions as weeks ("6 months / ~26 sessions"). *Fix:* add "(sessions, not evenings; see the Night Log)".
- **L7.** `House-Rules:37` and `S1:137` (planning capped at about 10 minutes) are an existing decision clock, not a content cut. Keep them, but note them in rule 7a so a Co-GM does not read them as "rush".

**Verdict on the other stops.** S0 (A), (B) and (C) are sound, and (C) already sits before the Trial Run. A stop after the Trial Run would leave a 15-minute second evening and practice Stress outstanding, so it would not be better. S1 (A) is safe if Load, the engagement Position and the cover story are logged (H2). S2 (B), after the Exit, is safe: it resolves the evening, and the Return line `:507` re-enters cleanly. S3 (A) and (C) are safe. No held Entanglement crosses any listed stop.

**Counts:** BLOCKER 2 · HIGH 7 · MEDIUM 7 · LOW 7.
