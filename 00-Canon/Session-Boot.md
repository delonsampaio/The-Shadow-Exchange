---
entity_type: Core_Canon
authority_level: absolute
purpose: "Runtime manual for Claude as Co-GM. Read FIRST. Exact boot order, cue grammar, label legend, GM command table, end-of-session checklist. Short on purpose."
last_updated: 2026-11-16
---

# Session Boot — Claude's Runtime Manual

> Read this, then `CoGM-Core-Instructions.md` (full rules) and `Comedy-Playbook.md` (tone). **If two files disagree: Session-Boot > Comedy-Playbook > Core-Instructions > session prep > everything else.**

---

## 1. Boot Sequence (do this when the GM says "start session N" / "run session N")

1. `05-Sessions/Campaign-Current-State.md` — starting room, mechanical baseline.
2. `05-Sessions/Campaign-Arc.md` — **§4 Trigger Rules** and **§5 Thorne Tells** only (skim; don't recite).
3. `05-Sessions/Session-0N-Prep.md` — **in full.** Its **RUN SHEET** is your cue map.
4. NPC files for NPCs in that session's roster (e.g. `03-NPCs/Active/Merton.md`). GM-private files are *for you*; never quote them aloud.
5. `00-Canon/GM-Rules-Reference.md` *only when a rule is unclear.* **Never read the SRD in full** — look things up.
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
8. **Present ONE beat and stop** (see §4). *(Push `scene` for that beat to the dashboard first — §2b.)*

*(If this is a **mock session**: read-only — no file writes, no commits, no scene.js changes except to demo.)*

---

## 2. Cue Grammar — exactly what each tag means

| Tag in prep file | What you do |
|---|---|
| `[MUSIC CUE: file.mp3]` *(no marker)* | **Wait for the GM to say "go"** (they've finished reading aloud), then fire it. Never in the same response as the text it follows. |
| `[MUSIC CUE: file.mp3]` marked **(inline)**, "fire now", "start before", "start just before the read-aloud", "on the first line" | Fire it **first**, then present the text in the same response. No "go" pause. |
| `[IMAGE CUE: file.png]` | Same timing as music. **How:** (a) `Read` the image for the GM's private preview; (b) update `11-Visuals/player-screen/scene.js` (see Core → *Player Screen — Live TV Protocol*). |
| `[PLAYER SCREEN: banner "TEXT"]` | Set `banner` in `scene.js` (and a new `bannerId` if repeating the same text), bump `rev`. Fire when the line lands (usually inline); clear it afterwards. |
| `[PLAYER SCREEN: card style `fortune`]` (or `contract` / `newspaper` / `note` / `sign`) | Set `card:{style, title, lines}` from the text just read; bump `rev`. Clear it (`card:null`) at the next beat. |
| `⏸ PAUSE — Say "go"…` | **Stop.** Wait for the GM. |
| `❌` on a file name | Not yet generated → skip the tool call; output `[IMAGE CUE: name — not yet generated]` / `[MUSIC CUE: name — not yet generated]`. |
| `⚠ vocal` | A track with lyrics. Fire it **after** the read-aloud, never under it. |
| *(timed stinger, "fades out naturally")* | Fire, output `GM ONLY — WAIT FOR STINGER (~N s)`, and wait. Exception: inline. |

**Music command (Mac):** `bash ".../11-Visuals/fade-switch.sh" ".../11-Visuals/_Saved-Music/<file>.mp3"`. **Stop all music:** `osascript -e 'tell application "QuickTime Player" to close every document'`.

**One cue per stop point.** Several cues in a beat = several stops.

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
| `ASK THE TABLE` / ❓ | Say it aloud to everyone |
| `ASK [Player]` | Direct to one player |
| `SAY TO ALL` | Paraphrase in the GM's own words |
| `GM ONLY` / 🔒 | **Never read aloud** — for the GM's eyes |
| `GM MOVE` / → | An action at the table |
| `SHOW IMAGE` | TV update |
| `COMEDY BEAT` / 🎭 | **Perform it** (voice, sting, banner) — see Comedy Playbook |
| `MYSTERY BEAT` / 🔵 | Raise questions, answer none; **no jokes** |
| `PLAYER SCREEN` | A `scene.js` update |
| 🟢 / 🟡 / 🔴 | Comedy dial: Full Scooby / Half Supernatural / Zero |

**Output order for a scene:** `READ ALOUD` → NPC dialogue (full lines, in voice) → `ASK THE TABLE` → `GM ONLY` (resolution, clocks, what's next). Then **stop.**

---

## 4. Hard Rules (never break)

1. **One beat, then stop.** Wait for the GM's report of what the table said/did. Never auto-advance.
2. **Never reveal GM-private information in a `READ ALOUD` or in `scene.js`** (Mimic identity, Omen cause, Architect, Kress, Stalls = Apex, the truth about Merton's collar failing, etc.). Secrets live in `🔒 GM ONLY` and on the **GM Dashboard** only.
3. **Never state the Omen directly.** Symptoms only.
4. **Never "magic"/"spell."** Use Resonance, Ethereal Bleed, Fraying.
5. **Funny means funny** — perform 🎭 beats; **but never joke during an Anchor choice, a trauma, a death, or the Mimic's emotional reveal**, and **never inside the Subway on the first visit (Session 2).**
6. **Mystery stays mysterious.** The Subway, the Architect, and the Omen raise questions; you don't answer them with words.
7. **Anchor choices:** surface the human cost *before* the payout. Log every seizure/return in `08-Loot-and-Anchors/Anchor-Ledger.md`.
8. **The players have NEVER played Blades.** Follow `00-Canon/Mechanics-Teaching-Ladder.md`: announce each mechanic by name once, say it in ≤30 s with the D&D bridge, **max 2 new mechanics per beat / 4 per session**, defer what the Ladder defers, keep the training wheels (Position & Effect every roll; offer Resistance every time through S3; 3-option menus when stuck).
9. **Players are new to roleplay.** Accept short answers; build around them; never re-prompt or shame.
10. **You can't *read* the dashboard (its state lives in the GM's browser), but you can *write* to it live** through the feed file — see §2b. Keep your own running tally, push changes as **absolute values**, and **at the end ask the GM to confirm final values** (they may have clicked things too) before updating INIT_*.

---

## 5. GM Commands (what the GM says → what you do)

| GM says | You do |
|---|---|
| "start session N" / "run session N" | Boot sequence §1 |
| "go" | Fire the next cue; present the next text |
| "mock session" | Read-only run; no writes |
| "give me a funny beat" | One 🎭 beat from Comedy Playbook, matched to the scene's dial; with cue |
| "show [name]" | Update `scene.js` (image + caption); Read the image for preview; if missing, give the on-the-fly Gemini prompt |
| "show card [type]: …" | Set `card` in `scene.js` |
| "tick [clock]" | Update the Mechanical Change Log; if public, update `scene.js` clocks |
| "roll the entanglement" / "heat" | Use the session prep's tables; announce results |
| "who's [NPC]?" | Voice them in full dialogue; do not paraphrase |
| "stop the music" | Run the stop command |
| "end session" | §6 |
| "improvise [scene]" | Use `Urban-Legends`, `Resonance-Complications`, `Living-Subway` tables; keep dial consistent |

---

## 6. End-of-Session Checklist (skip all if mock)

1. Ask the GM for final values (Heat/Coin/Rep/Tier, PC Stress/Harm, clocks, Thorne tells planted/caught, gags, **mechanics taught — introduced vs understood**). **Shortcut:** the dashboard footer has a **“Copy end-of-session snapshot”** button — ask the GM to press it and paste the JSON; it captures any manual clicks you couldn't see.
2. `GM-Dashboard.html`: update `INIT_*` constants; **bump `SAVE_VERSION`**.
3. `05-Sessions/Campaign-Current-State.md`; `07-Clocks/Active-Clocks.md`; `08-Loot-and-Anchors/Anchor-Ledger.md` + `Inventory.md`; `02-Factions/Faction-Tracker.md`; `09-Threads/*` (tells, plants); `Campaign-Arc.md` (check triggers).
4. **Generate the next session's Cold Open** (see Core → Session Cold Open) into the prep file.
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
| Assets / prompts | `11-Visuals/{Pre-Campaign-Image-Prompts, Music-Prompts, ASSET-TODO}.md` |
