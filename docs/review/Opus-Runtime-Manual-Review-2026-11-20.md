# Runtime Manual Review: can a fresh Co-GM boot and run a session from files alone?

*Reviewer: Claude (Opus), 2026-11-20. Report only; no repo files edited. Every claim below was checked by reading or grepping the file; line numbers are from today's copies. Not read in full: Tone-and-Style, Teaching Ladder (rows only), Sessions 00/02/03 (grepped only), Wiki-Update-Protocol.*

**Verdict:** a fresh instance would boot and run Session 0/1 *mostly* right. It would fail in three places: (1) it would run the scripted comedy during Merton's Surge, which breaks the Menace Rule; (2) it would use the prep files' non-SRD Heat tables, because Boot's priority order puts prep above House-Rules; (3) several GM commands still point to old files, so it would roll dice itself or never open the Improv Kit. The new 2026-11-20 files are good, but most are reachable only through File-Index, and Session-Boot was never updated to point at them.

## Top 10

1. **BLOCKER:** Session 1's stage-prop gags run *during* the Surge, which breaks the Menace Rule (S01:296–317).
2. **BLOCKER:** Two files each claim to win. House-Rules says "this page wins", but Boot ranks it below prep, so the non-SRD Heat tables in S01/S02 and the wrong Entanglement dice in S03 win.
3. **HIGH:** The Boot GM-command table is stale. "roll the entanglement" sends the AI to the prep tables and has it announce results (so it rolls itself), "improvise" skips the Improv Kit, and "end session" skips the Ritual.
4. **HIGH:** No boot path when the prep file doesn't exist (S04+ has none) and no resume path after a mid-session context reset.
5. **HIGH:** The Menace Rule is missing from Boot's Hard Rules and from CLAUDE.md, and Core contradicts it.
6. **HIGH:** Core's cue timing and scene format contradict Boot (fire images *before* the read-aloud; every cue is its own stop; the scene format has no REACTION STOP).
7. **HIGH:** Season-1-Plan breaks its own "Decay never above 3 in S1" rule (lines 75 and 78), and Improv-Kit adds Decay +1 with no cap.
8. **HIGH:** House-Rules is not a mandatory boot read, yet it holds live table procedure.
9. **MEDIUM:** Leak and hint risks: Zoltar "SOMETHING DEEP IS ASLEEP", the old d8 card "SOMEONE IS WEARING YOUR FACE", Improv rumour 14 "theatre understudy", and a Dictionary that isn't marked GM-only.
10. **MEDIUM:** The Heat-and-Entanglements reskins drop the SRD costs; Gang Trouble and Interrogation are mis-mapped.

---

## BLOCKER

### B1. Session 1 jokes during a real threat
- **Where:** `05-Sessions/Session-01-Prep.md:308–317`: *"🎭 THE LEVER + STAGE-PROP GAGS (🟢) … Use one of these per beat, **during the Surge**"*, with banner "DO NOT PULL" and Merton's line *"I'm so sorry. Mind the sandbag."* Run Sheet line 35 lists them as the Beat 6 comedy.
- **Conflicts with:**
  - `Comedy-Playbook.md:117`: "Do not undercut it with a joke, a gag banner or a comic sting while the crew is in danger."
  - `Comedy-Playbook.md:119`: "**Merton's Surge** … the scary ones; never promote them to jokes."
  - `House-Rules.md:43`: "monsters get no punchlines".
  - S01:294: the Surge is Desperate, with Level 2 harm.
- **What a fresh AI does:** it runs them. They are scripted, sit on the Run Sheet, and S01:467 asks for "at least two 🎭 beats". Boot (the top authority) never mentions the Menace Rule.
- **Fix (needs a GM decision):** move the gags to *after* the Surge is resolved (Merton held or soothed, or the clock emptied), as a 🟢 aftermath beat, and cut Merton's sandbag line. Change Run Sheet row 6's Comedy cell to "— (🔴/🔵 during the Surge; gags only after it resolves)". The second 🎭 beat can be Bernard plus Gerald, which already satisfies "two per session".

### B2. Two supreme files; the prep's non-SRD Heat and Entanglement rules win
- **The two claims:**
  - `Session-Boot.md:10`: "Session-Boot > Comedy-Playbook > Core-Instructions > session prep > everything else." House-Rules falls in "everything else".
  - `House-Rules.md:10`: "If a rule here conflicts with another file, **this page wins** for table procedure."
- **The prep rules that win as a result:**
  - `Session-01-Prep.md:409` and `Session-02-Prep.md:487` give Heat as "Quiet +1 · Standard +2 · Loud, or Apex engaged +3 …". The SRD is 0/2/4/6 plus modifiers (SRD:1964–1970; `Heat-and-Entanglements.md:10`).
  - `Session-03-Prep.md:145` says *"ASK A PLAYER: Roll the dice for the crew." (Heat 0–3: roll two dice and take the lower…)*. The SRD is dice = **Wanted level**, with Heat choosing the column (SRD:2058). Line 150 of the same file then says "the only GM dice are the Entanglement", so the file contradicts itself.
- **What a fresh AI does:** by Boot's order, prep beats House-Rules, so it uses the +1/+2/+3 Heat and has a player roll the Entanglement on Heat.
- **Fix:**
  - Boot:10 becomes: **"If two files disagree: Session-Boot > House-Rules (rules and table procedure) > Comedy-Playbook > Core-Instructions > session prep > everything else."**
  - House-Rules:10 becomes: "This page ranks second, after Session-Boot (see its priority line)."
  - In S01:409 and S02:487, replace the Heat line with "Heat: `07-Clocks/Heat-and-Entanglements.md` §1 (SRD)."
  - Rewrite S03:145 so the GM rolls dice equal to Wanted (0 → two dice, keep the lowest) and reads the column for current Heat.

---

## HIGH

### H1. The GM-command table is stale (`Session-Boot.md:155–173`)
| Line | Now | Problem | Replace with |
|---|---|---|---|
| 167 | "roll the entanglement" / "heat" → "Use the session prep's tables; announce results" | Wrong source (the new file says "no prep file needs its own table", Heat:4). "Announce results" invites the AI to roll; House-Rules:26 says "The Co-GM never 'rolls'". | `"heat" / "entanglement"` → Compute Heat per `07-Clocks/Heat-and-Entanglements.md` §1; **ask the GM to roll** (dice = Wanted; 0 → 2d keep lowest); read the column for current Heat; give the city skin and the SRD ways out. |
| 173 | "improvise [scene]" → Urban-Legends, Resonance-Complications, Living-Subway | Never opens the new Improv Kit | → `10-Generators/Improv-Kit.md` (§1 street, §2 rumour, §4 gag, §6 cover twist); Menace Rule applies. |
| 172 | "end session" → §6 | §6 never mentions XP, the retrospective, NPC-Index or the Faction Turn | Add §6 step 0: "Run `00-Canon/End-of-Session-Ritual.md` (XP from S4, retrospective), then continue." Add to step 3: `03-NPCs/NPC-Index.md`. |
| 171 | "wrap it 3 / 4" | The Kit has "wrap it 2" (Express:13); the Dictionary says 2–4 | "wrap it 2 / 3 / 4" |

**Missing commands to add:**
- **"no prep" / "evergreen"** → `05-Sessions/Evergreen-Episodes.md` plus Improv-Kit §7.
- **"they zigged" / "off the rails"** → Improv-Kit §5.
- **"faction turn"** → `02-Factions/Faction-Turn-Procedure.md`. GM-side only; never in READ ALOUD.
- **"short session"** → House-Rules C9.
- **"[player] is absent"** → House-Rules C10.
- **"zoltar card"** → `Zoltar-Card-Deck.md`, after its leak check.
- **"new NPC"** → check names against `NPC-Index.md` and `NPC-Bench.md` before inventing one.
- **"resume"** → see H2.
- **"who's [NPC]?" (existing row 168)** should first check NPC-Index status, so a dead NPC is not resurrected.

### H2. No path for a missing prep or a context reset
- **Missing prep:** Boot §1 step 3 assumes `Session-0N-Prep.md` exists, but `05-Sessions/` holds only 00–03. "start session 4" has no defined behaviour. The fallback exists only in the GM's own checklist (`Weekly-Prep-Checklist.md:26`).
- **Context reset:** for an 80-session campaign with resets, nothing tells a re-booted AI how to pick up mid-session.
- **Fix, a new Boot step 3a:** "If the prep file doesn't exist, say `GM ONLY — NO PREP FOR SESSION N` and offer: (a) Evergreen episode, (b) Improv-Kit §7 no-prep score. Wait for the GM's choice."
- **Fix, a new §1b "Resume after a reset":**
  - Re-read Boot §2–§5 and the prep from the current beat.
  - Read the last ops in `11-Visuals/dashboard-feed/feed.js` (the AI *can* read this file, even though it can't read the dashboard) and `player-screen/scene.js` to rebuild the tally.
  - Ask the GM one question: "Which beat are we on?"

### H3. The Menace Rule is absent from the top authority, and Core contradicts it
- **Absent:** Boot Hard Rule 5 (`Session-Boot.md:145`), Boot §2a:61 and `CLAUDE.md:12` list the no-joke zones (Anchor, trauma, death, Mimic reveal, first Subway visit, Merton plea). None of them includes "a real threat on screen".
- **Contradicted:** `CoGM-Core-Instructions.md:371` says "Never: … monsters that are *only* threats". Core:400 says "Combat is fine … a monster doing something unexpectedly mundane … do not avoid it."
- **Fix, a new Boot Hard Rule 5b:** "**Menace Rule:** while a real threat is on screen, no joke, gag banner or comic sting. Only a 🟢 Ruh-Roh marked on the Run Sheet may look scary and turn out harmless (Comedy-Playbook §Menace)." Add "· Menace Rule" to CLAUDE.md:12. Delete Core:371's "monsters that are *only* threats" and Core:400's last bullet.

### H4. Core contradicts Boot's cue grammar and output order
CLAUDE.md:4 tells the AI to read Core "complete rules", so these will be followed:
- **Core:155:** "trigger it immediately **before** the read-aloud". Boot:44 says images use the same timing as music, i.e. wait for "go".
- **Core:131:** "Each embedded cue within a beat is its own stop point … Do not fire all cues in a beat at once." Boot:56 says a paired IMAGE + MUSIC cue fires together. The AI would double-stop.
- **Core:112–125:** the "Scene format (use every time)" puts the `GM ONLY` resolution in the same output as `ASK THE TABLE`, with no REACTION STOP. That breaks Boot:127 and Hard Rule 10a, and the AI would pre-resolve the action.
- **Core:142–146:** "Output this block before anything else … Click directly on the dashboard during play." This conflicts with Boot:27 (the boot block) and Boot:71 ("The GM should never have to type or click").
- **Core:88:** reads GM-Rules-Reference every session. Boot:20 says "*only when a rule is unclear*".
- **Fix:** replace Core's "Session Walker Protocol" (84–131), the timing paragraphs (45–52, 155), and "GM Dashboard" (135–149) with one line: "Boot sequence, cue timing, labels and output order: `Session-Boot.md` §1–§3 (authoritative)." This also saves about 3k tokens (D).

### H5. Decay above 3 in Season 1
- **The rule:** `Season-1-Plan.md:31`: "**never above 3 in Season 1**: the S15 truce and the S28 overload cost Heat, Favor or a license, not Decay."
- **Breaches:**
  - Season-1-Plan:75: the S15 truce gives "(**Decay +1**; the fox is out)".
  - Season-1-Plan:78: the S28 overload gives "(Apex blinded, **Decay 3–4**, Kress goes rogue)".
  - `Improv-Kit.md:90`: "If yes, Decay +1 at the next faction turn", with no cap.
- **Fix:**
  - Line 75: "(Ministry license suspended one arc; the fox is out)".
  - Line 78: "(Apex blinded, Decay holds at 3, Twice-Born Favor −1, Kress goes rogue)".
  - Improv-Kit:90: "Decay +1 at the next faction turn (Season 1: max 3; above that, Heat +2 instead)."

### H6. House-Rules is optional at boot
- **The problem:** Boot:21 lists it under 5a, "Unsure where something is…". It holds procedure the AI must apply unprompted: who rolls (B), Resistance offers, the 2-minute decision clock (C2), the 15-minute hard stop (C7), and absent player (C10).
- **Fix:** make it Boot step 1a, "`00-Canon/House-Rules.md` (one page; always)". It is about 4.9 KB.

---

## MEDIUM

**M1. Zoltar: three sources, and voice files keyed by session.**
- **The three sources:**
  - `Comedy-Playbook.md:82`: "4+ | (Write from `Campaign-Arc.md`)".
  - `Zoltar-Card-Deck.md`: pre-written cards, by arc.
  - `Zoltar-and-Consequence.md:14`: "d8 — use after Session 4". Its #7 is *"SOMEONE IS WEARING YOUR FACE"*, a direct Mimic hint, and the deck (line 9) points to that table.
- **Voice files:** Boot §2a:62 expects `music-sting-zoltar-fortune-sNN`, but deck cards have no per-session voice file.
- **Fix:**
  - Playbook:82 → "4+ | pick from `00-Canon/Zoltar-Card-Deck.md`".
  - Retitle the d8 table "Retired: use the Deck" and strike #7.
  - Boot:62 add: "From S4, the line is the Deck card; if `…-sNN` is missing, show the card only."

**M2. Zoltar deck leak and hint risk.**
- **Omen:** `Zoltar-Card-Deck.md:53`, *"SOMETHING DEEP IS ASLEEP. DO NOT TELL IT THE TIME."*, all but names the Omen's nature ("something ancient waking", Campaign-Arc:18). Boot Rule 3 says "Never state the Omen directly."
- **Mimic:** the Mid-Arc 3 cards (34, 36, 37) fail the deck's own leak check (line 9: "the Understudied"). *"HANDWRITING IS A KIND OF FACE"* is optional Tell 8 (Campaign-Arc:94).
- **What a fresh AI does:** told to "pick another", it finds that three of the four arc cards point at Thorne.
- **Fix:**
  - Replace card 53 with an Omen *symptom* card, e.g. *"YOUR CLOCKS AGREE WITH EACH OTHER. THEY DO NOT AGREE WITH YOU."*
  - Add to the deck header: "🔒 Arc-3 cards are deliberate tells: use at most one before S15, and log it as a tell (`tell` op)."

**M3. Improv rumours that hint or arrive too early.**
- `Improv-Kit.md:43`: *"A theatre understudy has missed six performances and been seen at all six."* This is player-facing (line 29: "Player-facing leads") and echoes the reveal title "the Understudied". Gate it: "S16+ only" (after the unmasking), or reword it to "a stage manager".
- `[SUB]` rumours (Subway Job Board) before S2, and `[HARLAN]` rumours before S4, reveal places the crew hasn't found. Add to line 29: "[SUB] only after S2; [HARLAN] only after S4."

**M4. `_Dictionary.md` is unmarked and contradicts itself.**
- **Unmarked:** Boot:21 sends the AI there for "what a term means". It contains "The Understudied: The Mimic wearing Elias Thorne's face" (line 31) and the Subway's nature (line 18). Boot Rule 6 says the Subway's nature is never answered in words.
- **Self-contradiction:** line 18 calls the Subway "**Magical**", against its own line 40 and Boot Rule 4.
- **Fix:** add a top line, "🔒 GM ONLY — never read a definition aloud or put it on the TV." Line 18 becomes: "**The Subway:** Ghostly and addressless; it appears where it chooses …"

**M5. Heat-and-Entanglements: the reskins drop the SRD resolution (SRD:2076–2130).**
- **The gap:** line 38 says "use the suggested ways out", but the table never gives them. The AI has no costs.
- **Mis-mappings:**
  - **Gang Trouble:** in the SRD it is *your own cohort's* flaw causing trouble (that is Gerald, House-Rules:17). Line 25 reskins it as a rival firm, which is Rivals.
  - **Interrogation:** the SRD gives "pay 3 coin, or level 2 harm and +3 heat (each resistable)". Line 28 gives "Documented Relocation form is half price", which is meaningless here.
  - **Arrest:** line 36 gives "fall guy (Wanted −1, Heat clears)". The SRD says handing someone over clears Heat; Wanted −1 comes only on conviction (SRD:1989). Line 36 also omits "pay coin = Wanted + 3".
  - **Column header:** "Heat 6" should be "6+" (Heat can be 7–8).
- **Fix:** add a "Ways out (SRD)" column with each SRD cost, and fix those three rows.

**M6. How long to keep offering Resistance.** `House-Rules.md:19` says "until the table asks us to stop". `Session-Boot.md:148` says "offer Resistance every time **through S3**". Pick one. Suggestion: Boot's wording, because the Ladder graduates it.

**M7. When GM ONLY notes may appear.** Boot:127 says `GM ONLY` comes *after* the reaction. But `Session-Writing-Rules.md:39` (§5.4) puts the *example answer* in GM ONLY "so the GM can unstick a quiet table", which is only useful *before* the stop. Boot:127 add: "Prep notes for the GM (example answer, what not to say) may come before the stop; the **resolution** comes after."

**M8. Unmarked comic stings.**
- `Comedy-Playbook.md:33` says "Fire the cue *with* the line (inline cue — no 'go' pause)". Boot:51 says unmarked → wait for "go".
- **Fix:** Playbook:33 becomes "Mark the comic sting *(inline)* in the prep; unmarked cues follow Boot §2."

**M9. Faction Turn self-conflicts.**
- **Tick cap:** `Faction-Turn-Procedure.md:12` says "every faction clock ticks once"; line 10 caps a turn at "three ticks in total".
- **Double turn:** `Evergreen-Episodes.md:22` runs a Faction Turn at session start, and `Weekly-Prep-Checklist.md:11` already ran one the day after.
- **No dashboard clock:** the Apex Acquisition clock has no dashboard `clock` id (GM-Dashboard.html:46–54), so "Update the dashboard (`clock` ops)" (line 14) fails.
- **Fix:**
  - Line 12: "each faction may tick once, ignoring the three-tick cap".
  - Evergreen:22: "…unless one already ran this week".
  - Log the Apex clock as a `gag`/note until an id exists. Do not touch feed.js or scene.js.

**M10. End-of-session ownership.** The Ritual (`End-of-Session-Ritual.md:28`) defers to Boot §6, and Boot §6 never mentions the Ritual. The Zoltar card is chosen in three places: Ritual:27 "for next time", Weekly:17, and Boot §2a "at every session close". This is resolved by H1's §6 step 0 plus one line in the Ritual: "The Zoltar card fires at the close (Boot §2a), *before* XP."

---

## LOW

- **L1.** `Session-Boot.md:18,28` use the pattern "Session-0N-Prep.md", which breaks at N ≥ 10 (Session-010?). → "`Session-NN-Prep.md` (two digits: 04, 12)."
- **L2.** `_Dictionary.md:27` says "S1 = 1–28"; `Season-1-Plan.md:10` says "Sessions 0–28".
- **L3.** Stale metadata: `Session-Boot.md:5` has last_updated 2026-11-16 but line 21 was added 11-20; `Improv-Kit.md:2` has entity_type "Review_Draft" but status ADOPTED.
- **L4.** Session 1 cue and label nits:
  - Line 319 says the music fires *"(on 'go' — fire at the 'collar flares' read-aloud…)"*. Pick one; inline fits.
  - Lines 452–456 contain two "a card drops" read-alouds; delete the second.
  - Lines 155 and 209 tag the Flashback teaching as 🎭, which may trigger a banner or sting; use "📘 TEACH".
  - Line 324 uses a bare "⏸ →"; Writing Rules §5.7 requires "⏸ REACTION STOP".
- **L5.** `House-Rules.md` §D (canon protections, "No boarding … before Arc IV (one pass-by only)") would spoil the planned players' House Rules page (line 5). Mark §D "🔒 GM ONLY, not for the players' site".
- **L6.** `End-of-Session-Ritual.md:13` has a compound question for "each of you". Use `❓ ASK EACH PLAYER (one at a time)` with one idea, per Writing Rules §5.6. Skipping XP in S0–3 is an SRD deviation missing from House-Rules §A.
- **L7.** `Season-1-Plan.md:121` (§7) still says "add 2–3 optional tells", which §0.2 already did. Line 124 says "Blades math is not verified"; either verify it or keep the warning.
- **L8.** `Improv-Kit.md:81–89` mixes 🔊 text and GM instructions on one line (e.g. "🔊 '…damper.' Greta phones. If they still refuse…"). Put the GM part after a `🔒`. The §4 gags lack the `⏸ REACTION STOP` that line 10 promises.
- **L9.** "Basement Two" (`Season-1-Plan.md:58,115`) is fine as an impossible space-mimic. Add "nothing was dug; the floor does not exist" so no one writes a real sub-basement.

---

## D. Context-window cost

**Mandatory boot read today:**

| File | Size |
|---|---|
| Boot | 21 KB |
| Core | 35 KB |
| Playbook | 11 KB |
| Campaign-Arc §4–5 | ≈6 KB |
| Current-State | 1 KB |
| Prep | 39–48 KB |
| NPC files | ≈3–5 KB each |
| **Total** | **≈130–150 KB (≈35–40k tokens)** before the first beat |

Every `IMAGE CUE` also `Read`s a PNG.

**Recommendations:**
- **Core:** cut about 50%. Remove the duplicated cue, dashboard and walker sections (H4), the Windows commands, "Older guidance retained below" (379–418, the Playbook overrides it), and the Session Cold Open spec (move it to End-of-Session-Ritual). Move the Tutorial Bridges (346–360) into the Teaching Ladder.
- **Playbook:** move "Zoltar's Fortune Cards" (75–82) and "Scripted Overt Beats by Session" (86–98) to on-demand. They duplicate prep files and the Deck.
- **Add to the mandatory read:** House-Rules (5 KB).
- **Read only when needed:**

| File | Read when |
|---|---|
| Season-1-Plan, Express-Ending-Kit | "wrap it" |
| Improv-Kit, Evergreen-Episodes | "improvise" / "no prep" |
| Faction-Turn, Heat-and-Entanglements | in downtime |
| Zoltar-Card-Deck | at the close |
| NPC-Index | new NPC / "who's" |
| GM-Rules-Reference | rules doubt |
| SRD | search only |

- **Image previews:** make the private `Read` of each image optional: "preview only on first show or if the GM asks".

## E. Leak summary

- **Player-facing surfaces checked:** Zoltar Deck, Improv rumours and street scenes, Session 1 READ ALOUD, SAY and TV cards, House-Rules (planned players' page).
- **Clean:** no direct reveal of the Mimic, the Architect, Kress or Stalls = Apex in any READ ALOUD or `scene.js` line read.
- **Hint risks:** M2 (Omen card, Arc-3 cards), M1 (d8 #7), M3 (understudy rumour, early [SUB]/[HARLAN] rumours), M4 (Dictionary), L5 (House-Rules §D).

---

## What is already good

- **Session-Boot §2–§3:** a precise cue grammar and label legend, the one-question-per-response rule (Boot:135), Hard Rule 10a on reaction stops, and the absolute-value dashboard pushes.
- **House-Rules §B** states the dice ownership exactly right: "The GM never rolls against the players… The Co-GM never 'rolls'."
- **Heat-and-Entanglements:** the Heat math, the Heat-9 rollover, incarceration and the 3×3 table match the SRD exactly (SRD:1964–1981, 1989, 2058–2066).
- **Advancement:** the Ritual's XP rules match the SRD (SRD:885–901), including "any xp track".
- **Canon held correctly in the new files:**
  - No city subway (Dictionary:18).
  - No boarding before Arc IV (Improv-Kit:82, File-Index:53).
  - One-storey water table (Improv-Kit:83; S01:294 "pumped sump, not a sub-basement").
  - Express Kit's Decay compression never punishes a careful crew.
- **The writing system works:**
  - Session-Writing-Rules plus the Template produce runnable beats; S01 has a REACTION STOP after every ASK, branches after the stops, and no READ ALOUD nested in GM ONLY.
  - S01's Thorne tells match Campaign-Arc §5 and Elias-Thorne.md.
  - The engagement roll says "The GM never rolls — a player does."
- **File-Index and NPC-Index** are good navigation. They need links from Boot (H1, H6) to be used.
