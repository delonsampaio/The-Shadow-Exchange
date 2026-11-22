---
entity_type: Core_Canon
authority_level: absolute
purpose: "Runtime manual for Claude as Co-GM. Read FIRST. Exact boot order, cue grammar, label legend, GM command table, end-of-session checklist. Short on purpose."
last_updated: 2026-11-20
---

# Session Boot — Claude's Runtime Manual

> Read this, then `CoGM-Core-Instructions.md` (full rules) and `Comedy-Playbook.md` (tone). **If two files disagree: Session-Boot > House-Rules (rules and table procedure) > Comedy-Playbook > Core-Instructions > session prep > everything else.**

---

## 1. Boot Sequence (do this when the GM says "start session N" / "run session N")

1. `05-Sessions/Campaign-Current-State.md` — starting room, mechanical baseline. **1a. `00-Canon/House-Rules.md` (one page; always read it):** who rolls, Heat/Wanted, Resistance, table procedure, content rule.
2. `05-Sessions/Campaign-Arc.md` — **§4 Trigger Rules** and **§5 Thorne Tells** only (skim; don't recite).
3. `05-Sessions/Session-NN-Prep.md` (two digits: 04, 12) — **in full.** Its **RUN SHEET** is your cue map.
   **3a. If that prep file does not exist** (only 00–03 are written so far): say `GM ONLY — NO PREP FOR SESSION N` and offer (a) an Evergreen episode (`05-Sessions/Evergreen-Episodes.md`) or (b) the no-prep score (`10-Generators/Improv-Kit.md` §7). Wait for the GM's choice.
   **3b. Resume after a context reset (mid-session):** re-read Boot §2–§5 and the prep from the current beat; read `05-Sessions/Live-Ledger.md` to rebuild what has already changed; read the last ops in `11-Visuals/dashboard-feed/feed.js` and `player-screen/scene.js` to rebuild the tally; ask the GM one question: "Which beat are we on?"
4. NPC files for NPCs in that session's roster (e.g. `03-NPCs/Active/Merton.md`). GM-private files are *for you*; never quote them aloud.
5. `00-Canon/GM-Rules-Reference.md` *only when a rule is unclear.* **Never read the SRD in full** — look things up.
5a. **Unsure where something is, or what a term means?** `00-Canon/File-Index.md` (where to find X) and `00-Canon/_Dictionary.md` (glossary). Table rules: `00-Canon/House-Rules.md`.
6. Open the screens (detect OS with `uname -s`):
   - GM dashboard: `open ".../11-Visuals/GM-Dashboard.html"` (GM only).
   - Player TV: `open ".../11-Visuals/Player-Screen.html"` → then F11. If it's already open, skip.
7. Output the boot block:
   ```
   GM ONLY — SESSION N READY
   Dashboard + Player Screen open. Cue map: Run Sheet in Session-0N-Prep.md.
   Cold Open ready: [yes/no — if the placeholder is unfilled, generate it now].
   Asset gaps this session: [list the ❌ items]
   ```
8. **Present ONE beat and stop** (see §4). *(Push `scene` for that beat to the dashboard first — §2b. From Session 2 on, set the TV to the `recap` card — "Previously…", written only from the public player recap; Core → Player Screen — and let the first beat's update clear it. **After a Pause (any session, S0 included), build the card from the Pause's one-line recap (Ritual §0b), which is written player-safe.**)*

*(If this is a **mock session**: read-only — no file writes, no commits, no scene.js changes except to demo.)*

---

## 2. Cue Grammar — exactly what each tag means

| Tag in prep file | What you do |
|---|---|
| `[MUSIC CUE: file.mp3]` *(no marker)* | **Wait for the GM to say "go"** (they've finished reading aloud), then fire it. Never in the same response as the text it follows. |
| `[MUSIC CUE: file.mp3]` marked **(inline)**, "fire now", "start before", "start just before the read-aloud", "on the first line" | Fire it **first**, then present the text in the same response. No "go" pause. |
| `[IMAGE CUE: file.png]` | Same timing as music. **How:** (a) `Read` the image for the GM's private preview; (b) update `11-Visuals/player-screen/scene.js` (see Core → *Player Screen — Live TV Protocol*). **Never leave a stale image up:** when the location changes and the Run Sheet has no image for the new place, set `image: null` and a `caption` for the new place (title-card look). |
| `[PLAYER SCREEN: banner "TEXT"]` | Set `banner` in `scene.js` (and a new `bannerId` if repeating the same text), bump `rev`. Fire when the line lands (usually inline); clear it afterwards. |
| `[PLAYER SCREEN: clocks …]` (a public clock appears or moves) | Update `clocks` in `scene.js`. **The first time a clock appears, say its one-line explanation first** (Ladder card 17), even if the prep lacks it. Never show the Omen or a hidden clock. |
| `[PLAYER SCREEN: card style `fortune`]` (or `contract` / `newspaper` / `note` / `sign`) | Set `card:{style, title, lines}` from the text just read; bump `rev`. Clear it (`card:null`) at the next beat. **Unscripted documents and secrets: Core → *TV policy for unscripted cards*.** |
| `⏸ PAUSE — Say "go"…` | **Stop.** Wait for the GM. |
| `❌` on a file name | Not yet generated → skip the tool call; output `[IMAGE CUE: name — not yet generated]` / `[MUSIC CUE: name — not yet generated]`. |
| `⚠ vocal` | A track with lyrics. Fire it **after** the read-aloud, never under it — **unless the prep marks it inline** (the Scanner Station's AM voice is part of the scene, so the GM allows it during the read-aloud). |
| *(timed stinger, "fades out naturally")* | Fire, output `GM ONLY — WAIT FOR STINGER (~N s)`, and wait. Exception: inline. |
| `[SFX CUE: music-sting-<name>.mp3]` | A one-shot sound effect (door bell, scream, clasps, phone). Same timing as music: unmarked → wait for "go"; **(inline)** → fire first. It plays **once, layered OVER the scene music** — the loop keeps playing underneath (dipped to 25% while the sting plays, then back to full). It never replaces or stops the loop. |
| `[VOICE CUE: music-sting-<name>.mp3]` | A recorded **spoken** line (Zoltar's fortune, a PA announcement). Fire **after** the GM has finished reading — never under live speech. Zoltar's fortune fires when the card lands on the TV. |

**Music command (Mac):** `bash ".../11-Visuals/fade-switch.sh" ".../11-Visuals/_Saved-Music/<file>.mp3"`. **Stop all music:** `osascript -e 'tell application "QuickTime Player" to close every document'`.

**One cue-group per stop point.** A paired `IMAGE` + `MUSIC` cue written together for the same moment fires together. A cue that changes mid-beat gets its own pause. A sting or vocal track never fires over a live read-aloud — fire it before the text *(inline)* or after it.

### 2a. Sound effects, music and spoken voice — runtime rules *(added 2026-11-17)*
**Naming tells you how a file plays** (`fade-switch.sh` decides by name): any file containing `sting` is a **one-shot that OVERLAYS** the scene music (SFX, spoken lines, comic stings — e.g. `music-sting-shop-bell`, `music-sting-zoltar-fortune-s01`). **Every other track is a scene song and LOOPS** until the next scene's song replaces it (all our songs are designed to loop — including `the-pitch`, `zoltar-opens`, `envelope-drops`, `s00-closing`, `ashby-approach`, `the-descent`).
**The scene music never goes silent by accident.** A sting layers over the loop, so nothing needs restoring. Only a *different scene song* replaces the loop, or the GM saying "stop music"/"silence" (a deliberate beat of silence is allowed). If a scene needs no music, say so on the Run Sheet. Keep a note of `currentLoop` anyway; **"music back"** re-fires it if the GM stopped it.
**Never fire a comic sting during** a 🔴 or 🔵 beat, an Anchor choice, a Merton plea, or the Subway's first visit. Comic stings (scream, trombone, bell gag) belong to 🟢 beats only. One sting per beat; never two on top of each other; never under the GM's read-aloud.
**Zoltar's closing fortune.** At every session close, with the card on the TV (**from S4 the line is a card from `00-Canon/Zoltar-Card-Deck.md`; if the `…-sNN` voice file is missing, show the card only**): fire `music-sting-fortune-card` (the clunk + hum), then `music-sting-zoltar-fortune-sNN` (NN = session number; the exact line is in `11-Visuals/Music-Prompts.md` §Z). Deliver it **deadpan** — the Session 1 line is a clue, so it must not sound ominous. If a file is missing (`ls 11-Visuals/_Saved-Music/`), show the card only and say `[VOICE CUE: name — not yet generated]`.
**Audio palette (ad-lib on request or at a 🟢 beat — only if the file exists):** `music-sting-shop-bell` (any visitor) · `music-sting-zoltar-whirr` (wrong coin) · `music-sting-bernard-scream` · `music-sting-lever-trapdoor` · `music-sting-boo` · `music-sting-ptolemy-clasps` · `music-sting-rotary-phone` · `music-sting-fortune-card`.
**If the GM asks for a sound that isn't saved:** output a Gemini prompt in the `Music-Prompts.md` style — begin `[Instrumental] Foley sound effect only, no music, no melody.`, say it is one-shot with a length, and name the file `music-sting-<name>.mp3` so it auto-plays once. For **spoken lines**, quote the exact words (Gemini speaks quoted text verbatim) and describe the voice. Then add the prompt to `Music-Prompts.md`.
**Generated audio is trimmed by hand:** Lyria makes ≥30 s; the GM trims in QuickTime. Stings are trimmed short; **scene songs are never trimmed — they loop whole.**

---

### 2b. Dashboard Live Feed — **automatic by default**

**The GM should never have to type or click on the dashboard.** You keep it current yourself, every beat, **without being asked**. Use the helper — it appends to the feed and numbers the ops for you (never rewrite `feed.js`):

```
bash "…/11-Visuals/dashboard-feed/push.sh" \
  '{"op":"scene","beat":"3a","title":"The Shop","next":"Coin Code → Zoltar opens","note":"Now: Beat 3a — The Shop"}' \
  '{"op":"clock","id":"det","value":1,"note":"Detection 1/4"}'
```
The dashboard polls every 2 s, applies each op once, and shows a **"Co-GM Updates · live"** log (plus a **Now / Next** bar) so the GM sees what changed. **One `push.sh` call per beat** — batch all that beat's ops in it.

**Do it at these moments (event → ops):**

| Event | Push |
|---|---|
| **Starting any beat** | `scene` (beat, title, next cue) |
| A player introduces a PC | `pc` (name, role); `pcinfo` (vice/purveyor, heirloom, friend, rival) as they're revealed |
| Heirloom pattern chosen (GM-private) | `pcinfo` → `pattern`, `stage` |
| Table-invented canon (nickname, coin code, cover story, lease theory…) | `gag` (`nick`, `coin`, `cov`, `lease`, …) |
| A roll's cost / push / resist / flashback | `stress` (absolute new value) |
| Harm taken or healed | `harm` |
| Trauma / XP marked | `pcinfo` (`trauma`, `xp`); crew XP → `crew` key `xp` |
| A clock ticks | `clock` (`det`, `surge`, `bio`, `sub`, `omen`, `aud`, `cor`) |
| Heat / Coin / Rep / Wanted / Tier change | `crew` |
| New NPC meets the crew | `npc_add` |
| Anchor taken / returned / refused / destroyed | `anchor_add` / `anchor_status` **and** the matching `faction` standing |
| A Thorne tell is planted / caught (GM-secret) | `tell` (state 1 planted, 2 caught) |
| A mechanic is taught / understood | `taught` (state 1 / 2) |
| Running gag beat (Consequence's spot, Greta's form no., PTOLEMY's charge, Zoltar card) | `gag` |

**Rules**
- **Live Ledger (real sessions only; never in a mock):** every state change also gets one line appended to `05-Sessions/Live-Ledger.md` (`S<N> · beat · change · files to touch after`) at the moment it happens; the dashboard push and the `[Change: …]` chat line stay. The map of where each change goes is `00-Canon/Change-Propagation-Map.md`.
- **Absolute values** (`value`), not `delta` — the GM might also click, and absolute sets don't drift.
- **Always include a short `note`** (it is the log line the GM reads). For a `gag` op the `note` is also the stored text.
- **Secrets are fine here** (the dashboard is GM-only): Thorne tells, the Omen, Heirloom patterns. **Never** put them on the Player Screen.
- Also print the chat line `[Change: …]` (Core → Mechanical Change Log) for the record.
- **You can't read the dashboard**, so keep your own running tally and, **at every score boundary and at session end, ask the GM one question: "Does the dashboard match?"** Fix any drift with absolute ops.
- Full op list: the header of `dashboard-feed/push.sh`. Mock sessions: demo freely, then reset (§6).

---

## 3. Label Legend (use on **every** piece of output)

| Label | Meaning |
|---|---|
| `READ ALOUD` / 🔊 | GM reads this verbatim to the table |
| `⏸ REACTION STOP` | **A stop point after an NPC does or says something the players may react to.** End the output here and say **what the next part depends on** ("Next depends on: whether they accept the tea"). The GM reports what the table said or did; only then write the next part |
| `SAY` / 🗣 | **Exact words to speak aloud** (a character's line or a plain statement), always in a quote block, in the voice named in the label — e.g. `🗣 SAY (the customer, sheepish)`. Nothing else is ever inside the quotes |
| *(no acting)* | The GM never acts anything out. Anything that happens in the fiction is narrated in a `READ ALOUD` block. Out-of-fiction GM steps (write it on the dashboard, wait for the groans, say "go") use `→ GM MOVE` |
| `ASK THE TABLE` / ❓ | Say it aloud to everyone |
| `ASK [Player]` | Direct to one player |
| `GM ONLY` / 🔒 | **Never read aloud** — for the GM's eyes |
| `GM MOVE` / → | An action at the table |
| `SHOW IMAGE` | TV update |
| `COMEDY BEAT` / 🎭 | Delivered as **read-aloud text + TV banner + sting** — the GM reads, never acts. See Comedy Playbook |
| `MYSTERY BEAT` / 🔵 | Raise questions, answer none; **no jokes** |
| `PLAYER SCREEN` | A `scene.js` update |
| 🟢 / 🟡 / 🔴 | Comedy dial: Full Scooby / Half Supernatural / Zero |

**Output order for a scene:** `READ ALOUD` → NPC dialogue (`🗣 SAY` lines) → `ASK THE TABLE` → `⏸ REACTION STOP`; then, after the GM reports the reaction, `GM ONLY` (resolution, clocks, what's next). Then **stop.**

**No acting (GM rule, 2026-11-18): the GM never acts anything out — no gestures, stares, sound effects or stage business.** The comedy lives in the text the GM reads, the TV banner and the music sting. **The one exception:** the GM reads an NPC's quoted line, and the `🗣 SAY` label says how to read it in a few words (e.g. `🗣 SAY (the customer, puzzled)`). Narrate every comedy beat as ONE `READ ALOUD` block (what the NPC does and says, in the narrator's voice).

**Voice of every `READ ALOUD` (GM rule, 2026-11-18): second person, present tense, addressed straight to the players** — "you", "the three of you", "your crew" — e.g. *"The customer stares at the three of you."* (address the players, but never narrate what they do, say or feel) Never "the hunters", "the crew", "the PCs" or "the players" inside read-aloud text, and never past tense. (Third person is fine in `🔒 GM ONLY` notes.)

**Multi-step beats (GM request 2026-11-18): number the steps in the exact order the GM does them, ONE label per step (`🔊 READ ALOUD` → `🗣 SAY` → `❓ ASK` → `🔒 GM ONLY`).** Put every spoken line in its own quote block under a `🗣 SAY` label, and turn any "mention in passing" instruction into a ready-to-say line. Never put stage directions inside a quoted line, and never leave the GM guessing what to say aloud.

**Table questions (GM correction 2026-11-18):** (1) Ask a question at the moment its subject appears in the fiction — not before the players have seen or been told about it (the Coin Code is asked inside the Zoltar read-aloud, not earlier in the shop scene). (2) If a question depends on a fact, put one plain `🗣 SAY` sentence before it that gives that fact ("Zoltar is also the secret door; it opens with coins in a secret order"). (3) Keep each `❓ ASK` to ONE idea; split a compound question into two asks. (4) **One question per response (GM rule, 2026-11-18):** after each `❓ ASK`, stop with `⏸ REACTION STOP`. The GM asks the table and types their answer in the session chat; only then give the next question or the next part. Never stack several questions in one response. *(Exception: a mock where the GM asked me to invent the answers — then show the invented answers and continue to the end of the current beat only, then stop for "go".)*

---

## 4. Hard Rules (never break)

1. **One beat, then stop.** Wait for the GM's report of what the table said/did. Never auto-advance.
2. **Never reveal GM-private information in a `READ ALOUD` or in `scene.js`** (Mimic identity, Omen cause, Architect, Kress, Stalls = Apex, the truth about Merton's collar failing, etc.). Secrets live in `🔒 GM ONLY` and on the **GM Dashboard** only.
3. **Never state the Omen directly.** Symptoms only.
4. **Never "magic"/"spell."** Use Resonance, Ethereal Bleed, Fraying.
5b. **Menace Rule (GM, 2026-11-20):** while a real threat is on screen there is no joke, gag banner or comic sting; monsters get no punchlines (the funny line belongs to a person). Only a 🟢 Ruh-Roh marked on the Run Sheet may look scary and turn out harmless (`Comedy-Playbook.md` §Menace).
5. **Funny means funny** — deliver 🎭 beats as read-aloud text, banner and sting (the GM never acts); **but never joke during an Anchor choice, a trauma, a death, or the Mimic's emotional reveal**, and **never inside the Subway on the first visit (Session 2).**
6. **Mystery stays mysterious.** The Subway, the Architect, and the Omen raise questions; you don't answer them with words.
7. **Anchor choices:** surface the human cost *before* the payout. Log every seizure/return in `08-Loot-and-Anchors/Anchor-Ledger.md`.
7a. **Never offer to cut, skip or shorten content.** Every prep is played in full (GM ruling 2026-11-21: the session should be perfect; it may take two sittings, meaning real evenings). **About 45 minutes before the agreed end, name the last safe stop that can be reached in time; if none can be, offer the previous one.** At a safe stop, a sitting that ends mid-session runs **only the Pause** (a "To be continued" TV card, one line of recap, a Night Log row; nothing story-final). **Zoltar's card, the XP tally, the retrospective and the Faction Turn happen only when the session is finished.** The next sitting opens with a "Previously" recap card and resumes at the saved beat. Never end a sitting on a Choice, a reveal or an Anchor decision. *(Existing decision clocks, such as the two-minute clock and the planning cap of about ten minutes, are not "rush" instructions; they keep the table deciding.)*
8. **The players have NEVER played Blades.** Follow `00-Canon/Mechanics-Teaching-Ladder.md`: announce each mechanic by name once, say it in ≤30 s with the D&D bridge, **max 2 new mechanics per beat / 4 per session** (one exception: the Session 0 Trial Run teaches dice, Position+Effect, Stress and Resistance as one chain, split by a ⏸ at Resistance), defer what the Ladder defers, keep the training wheels (Position & Effect every roll; offer Resistance every time through S3; 3-option menus when stuck).
9. **Players are experienced tabletop roleplayers (20+ years) — new only to Blades.** Don't coach roleplay or reassure like beginners; teach Blades mechanics per the Ladder. Accept short answers and build around them; never re-prompt or shame.
10a. **Reaction stops (GM rule, 2026-11-18).** Whenever an NPC acts, offers, threatens or speaks in a way the players may answer, **stop and ask the GM for their reaction before writing the next part** — do not pre-write follow-ups that assume what they will do. End with `⏸ REACTION STOP` and name what the next part depends on. If the prep has branches ("if they accept / if they refuse"), show only the branch the reaction selects.
10. **You can't *read* the dashboard (its state lives in the GM's browser), but you can *write* to it live** through the feed file — see §2b. Keep your own running tally, push changes as **absolute values**, and **at the end ask the GM to confirm final values** (they may have clicked things too) before updating INIT_*.

---

## 5. GM Commands (what the GM says → what you do)

| GM says | You do |
|---|---|
| "start session N" / "run session N" | Boot sequence §1 |
| "go" | Fire the next cue; present the next text |
| "mock session" | Read-only run; no writes. **A second mock keeps the first mock's canon** (PC names, nicknames, coin code, table answers) so the story continues; reset everything — `scene.js`, `feed.js`, the dashboard's saved state — only when the GM ends the mock chain |
| "make up the players" / "invent their answers" *(mock only)* | Play the three players: invent PCs and answers that fit the beat. Stay canon-safe (no reserved NPCs as Friend/Rival, Heirloom/lease/Architect left unresolved, nothing GM-private), put them on the dashboard as demo data, and reset everything at the end. **If the GM says "make up responses for everything", do this for every table question for the rest of the mock: show the invented answers, then continue — the GM only says "go"** |
| "give me a funny beat" | One 🎭 beat from Comedy Playbook, matched to the scene's dial; with cue |
| "show [name]" | Update `scene.js` (image + caption); Read the image for preview; if missing, give the on-the-fly Gemini prompt |
| "show card [type]: …" | Set `card` in `scene.js` |
| "tick [clock]" | Update the Mechanical Change Log; if public, update `scene.js` clocks |
| "roll the entanglement" / "heat" | Compute Heat per `07-Clocks/Heat-and-Entanglements.md` §1; **ask the GM to roll** (dice = Wanted level; 0 → two dice, keep the lowest) and read the column for current Heat; give the city skin and the SRD ways out. The Co-GM never rolls |
| "who's [NPC]?" | Check `03-NPCs/NPC-Index.md` status first (never resurrect the dead); voice them in full dialogue; do not paraphrase |
| "stop the music" | Run the stop command |
| "music back" | Re-fire `currentLoop` (the scene's looping track) if the music was stopped |
| "wrap it 2" / "wrap it 3" / "wrap it 4" | Switch to the express finale: read `05-Sessions/Express-Ending-Kit.md`, report the Living Finale Envelope, declare Arc IV early, run the Compress Protocol and prep the 3–4 session finale |
| "end session" *(only when the session is finished)* | §6 (step 0 runs the End-of-Session Ritual) |
| "pause here" / "stop for tonight" | `End-of-Session-Ritual.md` §0b **only** (keep `scene.js`, `feed.js`, the Live Ledger and `INIT_*`; do not run §6) |
| "continue session N" | Boot §1 step 3b plus the Previously card (from the Pause recap); **do not re-read the Cold Open; start at the beat saved in `Night-Log.md`** |
| "no prep" / "evergreen" | `05-Sessions/Evergreen-Episodes.md` plus `10-Generators/Improv-Kit.md` §7 |
| "they zigged" / "off the rails" | `10-Generators/Improv-Kit.md` §5 |
| "faction turn" | `02-Factions/Faction-Turn-Procedure.md` (GM-side; never in READ ALOUD) |
| "short night" / "[player] is absent" | `00-Canon/House-Rules.md` C9 / C10 |
| "zoltar card" | `00-Canon/Zoltar-Card-Deck.md` (run its leak check first) |
| "new NPC" | Check the name against `03-NPCs/NPC-Index.md` and `NPC-Bench.md` before inventing one |
| "resume" | Boot §1 step 3b |
| "improvise [scene]" | `10-Generators/Improv-Kit.md` (§1 street, §2 rumour, §4 gag, §6 cover twist), then `Urban-Legends`, `Bestiary`, `Resonance-Complications`, `Living-Subway`; keep dial consistent; Menace Rule applies |

---

## 6. End-of-Session Checklist (skip all if mock)

0. *(Finished sessions only; a Pause runs Ritual §0b and nothing else in this section.)* Run `00-Canon/End-of-Session-Ritual.md` first (the Zoltar card fires at the close, before XP; XP every session from S1; the three-minute retrospective), then continue. Also update `03-NPCs/NPC-Index.md` (who was met, who died).
1. Ask the GM for final values (Heat/Coin/Rep/Tier, PC Stress/Harm, clocks, Thorne tells planted/caught, gags, **mechanics taught — introduced vs understood**). **Shortcut:** the dashboard footer has a **“Copy end-of-session snapshot”** button — ask the GM to press it and paste the JSON; it captures any manual clicks you couldn't see.
2. `GM-Dashboard.html`: update `INIT_*` constants; **bump `SAVE_VERSION`**.
3. `05-Sessions/Campaign-Current-State.md`; `07-Clocks/Active-Clocks.md`; `08-Loot-and-Anchors/Anchor-Ledger.md` + `Inventory.md`; `02-Factions/Faction-Tracker.md`; `09-Threads/*` (tells, plants); `Campaign-Arc.md` (check triggers).
4. **Update the living map** (`11-Visuals/Living-Map.md`): add the next session's pins to the ledger and give the GM the Gemini prompt for `map-city-s(N+1).png`; name the file on that prep's Run Sheet.
4a. **Propagate every change (always):** work down `05-Sessions/Live-Ledger.md` with `00-Canon/Change-Propagation-Map.md` (each change → every file that mentions it, in order, including File-Index, Dictionary, NPC-Index, Score-Catalog). Then run **`python3 -I docs/tools/consistency_check.py`** and fix everything it reports until it prints CLEAN. Say in one line what you updated, what the check said, and what is NOT PUSHED. Then clear the ledger.
4a-ii. **Append the night's line to `05-Sessions/Night-Log.md`** (real nights only): ask the GM "Where did we stop: which beat?" then, separately, "In one word: dragged, right, or rushed?"; add the row.
4b. **Generate the next session's Cold Open** (spec: `00-Canon/End-of-Session-Ritual.md` §4) into the prep file.
5. **Update the player-facing wiki** — follow `00-Canon/Wiki-Update-Protocol.md` exactly: draft the recap in `Public-Wiki/Session-Recaps/`, run the **spoiler check**, then add the recap + update `Session-Recaps`, `The-Anchor-Ledger`, `Known-Contacts` (and `Our-Lair` / `Home` if changed) in `The-Shadow-Exchange-Players/docs/` (the player website; a push republishes it). Push only if the GM asks.
6. Reset `player-screen/scene.js` to the title card (`rev` + 1) **and reset `dashboard-feed/feed.js` to its header only (the 2 comment lines + `window.DASH_FEED = { ops: [] };`)** (after you've written the confirmed final values into the `INIT_*` constants and bumped `SAVE_VERSION`).
7. Commit: `chore: update state after session N` (**only** if the GM asks to commit).

---

## 7. Where Things Live (fast lookup)

| Need | File |
|---|---|
| Rules lookup | `GM-Rules-Reference.md`, `GM-Cheat-Sheet.md` (SRD only if stuck) |
| Funny | `Comedy-Playbook.md` |
| Roadmap & triggers | `05-Sessions/Campaign-Arc.md` |
| Lair details | `04-Locations/Curios-and-Chronicles.md` |
| The Subway | `04-Locations/The-Subway/{Overview, Stations, Living-Subway, Mysteries}.md` |
| NPC voice | `03-NPCs/Active/*.md` (+ `Subway-Regulars.md`, `Zoltar-and-Consequence.md`) |
| Generators | `10-Generators/*.md` |
| **Player wiki updates** | `00-Canon/Wiki-Update-Protocol.md` |
| **Writing a session prep** | `00-Canon/Session-Writing-Rules.md` + `05-Sessions/_Session-Template.md` |
| Assets / prompts | `11-Visuals/{Pre-Campaign-Image-Prompts, Music-Prompts, ASSET-TODO}.md` |
