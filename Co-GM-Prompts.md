# The Shadow Exchange — Co-GM Prompts

Reference prompts for common tasks. Claude runs sessions; Gemini generates images and music.

---

## Session Running (Claude)

**Start a session:**
```
run session [N]
```

**Start a mock session (no file saves):**
```
run session [N] — this is a mock session. Do not update any files, do not commit anything. Read-only.
```

**Full autonomous mock (Claude improvises everything):**
```
run session [N] — this is a mock session. Do not update any files. Run the entire session autonomously from start to finish — make up players with distinct voices, improvise all responses. Generate the complete session in one output.
```

---

## During a Session (Claude)

**Explain a mechanic to a D&D player:**
```
A player from a D&D background doesn't understand [mechanic]. Explain it using the D&D bridge language from CoGM-Core-Instructions.md, using the specific roll happening right now as the example.
```

**Generate a complication for a mixed success:**
```
My player rolled a mixed success (4–5) on [action] while trying to [objective]. Give me two distinct Devil's Bargains or complications: one that threatens the crew's cover, one that introduces an immediate physical or sensory threat.
```

**Generate a read-aloud on the fly:**
```
My players just entered [location] / encountered [NPC or monster]. Generate a 3–5 sentence READ ALOUD using industrial-noir sensory details (smell, sound, lighting). Do not describe how players feel — only what they perceive.
```

---

## After a Session (Claude)

**Post-score reconciliation:**
```
The score is complete. Based on what happened, provide:
1. Heat calculation — what actions generated Heat and the new total
2. Coin earned — payout after complications
3. Clock updates — which clocks advanced and to what progress
4. Anchor Ledger entry — if any Anchor Items were seized or destroyed
5. Downtime options — available activities given current crew state
Then update GM-Dashboard.html, Campaign-Current-State.md, and any changed tracking files. Commit with message: chore: post-score reconciliation session [N]
```

**Full post-session update:**
```
The session is complete. Generate two outputs:

OUTPUT 1 — PUBLIC WIKI (player-facing, no GM secrets):
Session recap following the template in Public-Wiki/_Session-Recap-Template.md. Include what happened from the crew's perspective, mechanical outcomes, and one open question. Do NOT include GM-private information (Mimic identity, Architect details, The Innocent arc).

OUTPUT 2 — PRIVATE REPO UPDATES:
Updated markdown for:
- 07-Clocks/Active-Clocks.md
- 08-Loot-and-Anchors/Inventory.md
- 08-Loot-and-Anchors/Anchor-Ledger.md
- 05-Sessions/Campaign-Current-State.md
- 02-Factions/Faction-Tracker.md

Then update GM-Dashboard.html INIT_* constants and commit everything.
```

**Transcript processing:**
```
I am uploading a transcript of Session [N]. Please:
1. Cross-reference against Session-0[N]-Prep.md — flag anything that differed from prep or was improvised
2. Flag player decisions about Anchor Items, faction relationships, or clock advances I may have missed
3. Flag NPC dialogue or player statements worth logging in 09-Threads/
4. Generate the same two outputs as the full post-session update above, using the transcript as source of truth
Do not summarize the session — generate actionable file updates.
```

---

## Between Sessions (Claude)

**Campaign evolution:**
```
Review Campaign-Current-State.md and the current faction web. Identify one plot thread that has stalled or an NPC that has been underutilized. Provide three escalation options:
1. Narrative Shift — a new rumor or event in the Subway
2. Faction Move — a specific off-screen action by a rival faction that complicates the crew's next move
3. Mechanical Pressure — a new clock representing a looming threat
```

**Generate a new score:**
```
Based on the Three-Layer Monster generator in 10-Generators/ and the current campaign state, create a new score for a Tier [X] hunt in [District]. Include: the target entity (three layers), the Anchor Item, three engagement approaches with Position/Effect, and the wrap-up dilemma.
```

**Anchor and inventory check:**
```
Review 08-Loot-and-Anchors/Inventory.md and Anchor-Ledger.md. For any item the crew is holding that hasn't been fenced or resolved, generate one delayed Resonance Complication starting to manifest in the Lair. Describe the sensory evidence.
```

---

## Image Generation (Gemini)

Paste these into your Gemini image chat. Pre-written prompts for all major locations and NPCs are in `11-Visuals/Pre-Campaign-Image-Prompts.md` — check there first.

**On-the-fly image prompt format:**
```
[Subject — what it looks like, what it's doing, where it is, key details.]
Industrial-occult noir. Cinematic lighting, amber and cold blue tones, rain-slicked surfaces, dim reflections. Photorealistic, moody, detailed. Quiet unease — not horror. Modern city with century-old bones. Film grain texture. No text, no watermarks.
```

Save outputs to `11-Visuals/_Saved-Images/` and log in `11-Visuals/Session-Image-Log.md`.

---

## Music Generation (Gemini — Lyria 3)

Paste into your Gemini music chat (separate from the session runner chat). **Full prompts (campaign presets + all session cues) are in `11-Visuals/Music-Prompts.md`.** Save generated tracks to `11-Visuals/_Saved-Music/`.

**Prompt structure:** `[Instrumental]` + Genre/Era + Instrumentation + Mood + Tempo/BPM

**Quick reference** — for mid-session use. ☰ = long scene, prompt includes loop language:

| Scene | Saved file (if pre-made) | Short prompt |
|---|---|---|
| Bookshop / downtime ☰ | `music-bookshop-loop.mp3` | `[Instrumental] Dark Victorian ambient, warm dusty piano, clock tick, rain on glass, 55 BPM, no vocals, seamless loop, no melodic resolution.` |
| Theater basement ☰ | `music-theater-loop.mp3` | `[Instrumental] Empty stage ambience, distant crowd echo, creaking wood, single decaying piano note, melancholic and hollow, 50 BPM, seamless loop, no melodic resolution.` |
| Containment Suite ☰ | `music-containment-suite-loop.mp3` | `[Instrumental] Cold industrial ambient, fluorescent hum, sub-bass drone, metallic resonance, clinical, 40 BPM, no melody, seamless loop, no melodic resolution.` |
| Approach / stakeout | `music-approach.mp3` | `[Instrumental] Dark Victorian ambient, cello drone, mechanical ticking, tense suspenseful, 60 BPM.` |
| Active score | `music-score.mp3` | `[Instrumental] Industrial darkwave, metallic percussion, distorted bass, 120 BPM.` |
| Subway ☰ | `music-subway-loop.mp3` | `[Instrumental] Ethereal dark ambient, hollow PA echo, distant train, dissonant strings, 50 BPM, seamless loop, no melodic resolution.` |
| Supernatural reveal | `music-supernatural.mp3` | `[Instrumental] Ethereal dark ambient, wordless choir pad, discordant violin, 45 BPM.` |
| Aftermath | `music-aftermath.mp3` | `[Instrumental] Sparse neoclassical, solo cello, unresolved harmonic, 48 BPM, no resolution chord.` |

**Image-to-music:** Upload any image from `11-Visuals/_Saved-Images/` directly into Gemini music chat — it generates a matching track from the image's mood and setting.
