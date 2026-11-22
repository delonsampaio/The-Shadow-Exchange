---
entity_type: Core_Canon
authority_level: high
purpose: "How to WRITE a Session-0N-Prep.md so the Co-GM can run it and the GM can read it live without guessing. Read before drafting or editing any session prep."
last_updated: 2026-11-18
---

# Session Writing Rules

> `Session-Boot.md` says how to **run** a session; this file says how to **write** one. If they disagree, Session-Boot wins. Start from `05-Sessions/_Session-Template.md`.

## 1. Who it is for
- **The players:** three friends with 20+ years of tabletop RPG experience, **new only to Blades in the Dark.** Never coach roleplay or reassure like beginners; teach Blades mechanics per `Mechanics-Teaching-Ladder.md`.
- **The reader:** the GM, **live, at the table.** Every line must say plainly whether to *say it, do it, ask it, or keep it secret.* Ambiguity costs table time.

## 2. Shape of a prep file (in this order)
1. Front-matter, title, one **tone line** (🟢 Full Scooby / 🟡 Half / 🔴 Zero / 🔵 Mystery — what the dial is tonight).
2. **RUN SHEET** (table, first): `# | Beat | Trigger | Music | Image | Comedy | Purpose / mechanics`. **Every beat names its music and what the TV shows** (an image, or "title card + caption" when there is none, so a stale picture never stays up), so the table is never silent by accident. Mark each asset ✅ (exists) or ❌ (not yet generated); end with an **Asset status** line.
3. Time budget (estimates), **safe stops** (nothing is cut: where a night may end and resume; never on a Choice, a reveal or an Anchor decision), tech checklist, GM-only pre-session checklist.
4. The beats, in play order. 5. An "After this session" block (state updates; next Cold Open).

## 3. Every beat, same layout
`header` → **cue lines** (exact grammar from Session-Boot §2; say *(inline)* if it fires before the text) → `🔊 READ ALOUD` block → NPC lines in full → `❓ ASK` → `🔒 GM ONLY` → `⏸ PAUSE — Say "go"` / `→ GM MOVE: STOP`. **One beat, then stop.** A paired `IMAGE` + `MUSIC` cue written together for the same moment fires together; a cue that changes mid-beat gets its own pause. Stings and vocal tracks never fire over live read-aloud — mark them *(inline)* (before the text) or place them after it.
**Reaction stops:** after any NPC action or line the players may answer, write `⏸ REACTION STOP — next part depends on: {what}` and put the follow-up **after** it, as branches (`if they … → …`). The Co-GM shows only the branch the reaction selects; a punchline or payoff that depends on the table's answer never sits in the same block as the question.

## 4. Labels — use only these
`🔊 READ ALOUD` (verbatim) · `🗣 SAY` (exact words, in quotes, with the delivery named in a few words) · `❓ ASK THE TABLE` · `🔒 GM ONLY` · `🎭 COMEDY BEAT` · `🔵 MYSTERY BEAT`.
- **The GM never acts anything out** (GM rule 2026-11-18). Write every in-fiction moment as narration in a `READ ALOUD` block. The only exception is an NPC's quoted line, where `🗣 SAY (…)` names the delivery. Out-of-fiction GM steps use `→ GM MOVE`.
- **Comedy beats are written as ONE `READ ALOUD` block** (what the NPC does and says, in the narrator's voice), plus a TV banner or sting where one exists.
- **Outcomes follow actions.** Narrate what the player did ("Odette feeds the coins in, one after another — a nickel, a nickel, a quarter, a penny, and a quiet 'please'") *before* what happens because of it. Never open with the result as if it happened by itself. Where one player acts, use their character's name; the Co-GM fills `[Name]` and the table's own canon.
- **Voice of every `READ ALOUD`: second person, present tense, addressed to the players** — "you", "the three of you", "your crew" (*"The three of you stare back at them."*). Never "the hunters / the crew / the PCs / the players" in read-aloud text, never past tense. Third person is fine in `🔒 GM ONLY` notes.
- A multi-step bit is **numbered in the order it is done**, one label per step.
- A "mention in passing" note becomes a **ready-to-say `🗣 SAY` line.** Never leave the GM to improvise wording.

## 5. Table questions
1. Ask when the subject **appears in the fiction**, not before the players have seen or been told about it (the Coin Code is asked *inside* the Zoltar read-aloud).
2. If the question depends on a fact, put **one plain `🗣 SAY` sentence** before it that gives the fact.
3. **One idea per `❓ ASK`.** Split compound questions.
4. Put one **example answer** in `🔒 GM ONLY`, so the GM can unstick a quiet table.
5. **A beat with several questions is run one at a time:** write each `❓ ASK` followed by its own `⏸ REACTION STOP`, so the Co-GM asks one, waits for the GM to type the table's answer, then asks the next.

6. **Round-robin questions** ("what does each of you do?") are written once as `❓ ASK EACH PLAYER *(one at a time)*` followed by one `⏸ REACTION STOP`; the Co-GM asks one player, waits, then the next.
7. **Always write the full stop tag** — `⏸ REACTION STOP` (add `— next part depends on: {what}` when branches follow). Never "pause", "wait" or "let them react" in prose.

## 5b. Choices, dice and place (lessons from the Session 0 mock)
- **Choice menus:** one option per line; each option says **what the players get, in plain words, plus who it is good for** (*"Secure Lair — better locks, alarms and traps against intruders. Good if you worry about who might walk in."*). Say how many to pick. Write each follow-up as a branch (`→ if they pick X: 🗣 SAY … ❓ ASK …`).
- **Decisions come before dice.** Never ask for a roll before the player has chosen: *"Do you want to resist?"* first, **then** *"Roll your Resolve."* The same goes for Push Yourself and a Devil's Bargain.
- **Staging check:** before writing a beat, decide where every person and prop physically is (upstairs / the lair / the alley) and make sure two consecutive beats don't contradict each other.
- **NPC lines:** every line the GM reads as an NPC is a `🗣 SAY (NPC — delivery in a few words)` line. No "read it in two different voices", no sound effects, no stage business.
- **Never nest spoken blocks inside `🔒 GM ONLY`.** A `🔊 READ ALOUD`, `🗣 SAY` or `❓ ASK` that sits inside a GM-only block can be skipped or leaked. Close the GM-only note, then write the spoken block at the top level (use a short `### When X happens` header if needed).
- **Cross-session guards.** Anything that depends on a past choice (a form number, a thimble, who was met) is written as a branch or a `[fill-in]` — never as an assumption. Use the same name for the same item in every session (check the earlier prep, `grep -F`).
- **Mechanics script check.** Before writing any rule line, check it against `Blades-in-the-Dark-SRD.md` (Group Action, Devil's Bargain, Engagement Roll, Entanglement dice, Acquire Asset, Resistance) and the Teaching Ladder's defer list. House variants (e.g. the Weak hold / 0 Coin start) are marked `🔒 GM ONLY — house rule`.
- **Cost of a tutorial action.** If a mechanic is taught as a practice run, say plainly whether it is free tonight or what it costs.
- **Table canon:** anything the table invents is logged on the dashboard straight away (`gag`, `pcinfo`, `npc_add`).

## 6. Sound, picture, TV
- **Music:** every non-`sting` file is a scene song and **loops** until the next scene's song replaces it. A `music-sting-*` file is a one-shot that **overlays** the loop. Don't write beats that need silence unless it is a deliberate dramatic beat — say so on the Run Sheet.
- **Comic stings/gags** only in 🟢 beats — never in 🔴/🔵, an Anchor choice, a Merton plea, or the Subway's first visit.
- **First appearance of a public clock (GM request 2026-11-21):** when a clock first goes on the TV the prep must carry a one-line `🗣 SAY` explaining it at that beat, in the same breath as the tick (what it is, what fills it, what happens when it fills). Use `Mechanics-Teaching-Ladder.md` card 17 for the wording. Count it against the max-2-new-mechanics-per-beat limit.
- **TV:** image + caption per location/NPC; documents as `card`s — **every job envelope, poster or contract the crew is handed gets a `contract` card** (≤ ~8 short lines; a `recap` card opens Session 2+); public clocks only. **Never** Position/Effect tags, roll results, objective lines or per-PC Stress/Harm (see Core → Player Screen). Position/Effect lives on the printed Table Card.

## 7. Spoilers and mystery
`READ ALOUD`, `SAY` and anything on the TV contain **no GM-private information.** Secrets live only in `🔒 GM ONLY` and on the dashboard. Mystery beats raise questions and answer none. Never name the Omen; never say "magic"/"spell." Check reserved NPCs (Session 0 §Beat 4) before offering Friend/Rival slots.

## 8. Mechanics
Follow the Teaching Ladder: **max 2 new mechanics per beat, 4 per session**, ≤ 30 seconds each with the D&D bridge. Say Position and Effect every roll; offer Resistance every time through Session 3; give a 3-option menu when the table is stuck.

## 9. Assets and the wiki
**Living map:** the city map is cumulative, one file per session (`map-city-sNN.png`). Every prep names its map on the Run Sheet (approach or briefing), says which district each new location is in, and **fixes each new location's spot in the placement plan** in `11-Visuals/Living-Map.md` at the time it is written (the pin is drawn later, once the crew knows the place), and adds the session's pins to the ledger there (public places only — never the Subway entrance or anything GM-private). A place outside the five districts gets its own map (regional, site or underground) — see rule 9 there.

List every ❌ in `11-Visuals/ASSET-TODO.md`; prompts live in `Pre-Campaign-Image-Prompts.md` / `Music-Prompts.md` (follow their rules: 16:9 TV, 3:2 wiki portraits, exact sign text, (Gemini no longer adds a corner sparkle, GM 2026-11-22: no corner check needed; still check for stray legible text and for matches to the read-aloud); real brand names are fine — this is a private table of friends, GM decision 2026-11-20). Every NPC the crew sees gets a **wiki portrait**, published only after they've met them (`Wiki-Update-Protocol.md`).

## 10. Before you call a prep file done
- [ ] Run Sheet complete; every beat has music; ✅/❌ correct.
- [ ] No outcome (a door opens, a roll succeeds or fails, an NPC reacts) is read before the player's action that causes it. Use `[Name]` / `[the table's canon]` fill-ins for details the table invented.
- [ ] Every choice menu lists what each option gives and who it suits, with a branch per option; no roll is requested before the player's decision; consecutive beats don't contradict each other about where people and props are.
- [ ] Every `READ ALOUD` is second person, present tense ("you", "the three of you").
- [ ] Every spoken line is under `🗣 SAY` or `🔊 READ ALOUD`; nothing asks the GM to act, gesture or do a voice except to read a labelled NPC line; comedy beats are read-aloud blocks.
- [ ] Every `❓ ASK` follows §5 (right moment, context line, one idea, example answer).
- [ ] Every NPC action the players may answer is followed by a `⏸ REACTION STOP` with branches, not a pre-written payoff.
- [ ] No GM-private information outside `🔒 GM ONLY`.
- [ ] The session's map is named on the Run Sheet, each new location has a district, and the pin ledger in `11-Visuals/Living-Map.md` is updated.
- [ ] Time budget and safe stops present (nothing is cut); next session's Cold Open noted.
- [ ] Every cue in a beat body appears on the Run Sheet (and vice-versa); the Music column says *(continues: track)* rather than "—" where a loop keeps playing.
- [ ] No `READ ALOUD`, `SAY` or `ASK` is nested inside a `🔒 GM ONLY` block.
- [ ] Every `❓ ASK` is followed by a full `⏸ REACTION STOP`; no outcome is written in the same block as the question.
- [ ] Anything that depends on an earlier session's choice is a branch or fill-in, and item names match the earlier prep.
- [ ] Every rule line was checked against the SRD / Teaching Ladder.
- [ ] Every score has a Payoff step (Coin and Rep numbers), ONE Heat rule (no other Heat statement in the file), an Entanglement with picks per cell, and a 🔒 fight-to-kill block.
- [ ] The close runs in order: Zoltar → PC XP then crew XP (card 22 if a track fills) → retrospective → Faction Turn → Night Log; and a Pause is described for a sitting that ends mid-session.
- [ ] **Clocks:** every clock that will appear on the TV for the first time this session has a `🗣 SAY` at *that beat* explaining it in one line (what it is, what fills it, what changes when it fills; Ladder card 17), and the Run Sheet lists which clocks appear and when. Secret clocks (the Omen, Decay while hidden, the Mimic) never go on the TV and are never explained to the players.

## 11. Writing the next prep (from the Night Log and the last session's outcome)
**Inputs to read first:** the last `05-Sessions/Night-Log.md` row (beats per sitting, the GM's feel word); `Campaign-Current-State.md` and the confirmed end-of-session snapshot; the previous prep's "leaves with" list; the Faction Turn result; session N's rows in `Season-1-Plan.md` §2, `Secrets-and-Reveals-Schedule.md` §B, `Clocks-Calendar.md` and `Mechanics-Teaching-Ladder-S4-Plus.md`; the NPC files in the roster.
**Then:** list the decisions the GM must make (ask them one at a time); write every past choice as a branch, not an assumption; keep new lessons to four or fewer (a due lesson over the cap is taught at the next session's first use and logged); respect the reveal budget (one big reveal per session; other threads are played as silence or texture); mark safe stops (never on a Choice, a reveal or an Anchor decision); then run the §10 checklist, an Opus audit and a simulated playthrough.
