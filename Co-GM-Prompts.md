# AI Co-GM Command Protocols

*This file contains the "Master Prompts" to re-sync the AI with The Shadow Exchange campaign.*

## 1. The Initial Sync (Use when starting a new chat)
> "I am the GM for a 'Blades in the Dark' campaign called 'The Shadow Exchange.' I have uploaded my repository. Please perform the following in order:
> 1. Read `00-Canon/Tone-and-Style.md` to establish your persona and adhere to the 'Zero-Footprint' rules.
> 2. Read `05-Sessions/Campaign-Current-State.md` to establish our exact narrative and mechanical baseline.
> 3. Open a **Canvas** and generate my Live GM Dashboard with distinct cards for: Active Clocks, Crew/Lair Stats, and the NPC/Faction Web.
> 4. Stop processing and ask me for the first scene or transcript to begin."

## 2. Post-Session Processing (Use after a live session with Transcript)
> "I am providing a transcript of our latest session. Do not summarize the session. Instead, provide three distinct outputs:
> 1. **Public Wiki:** Generate `Session-Recap-XX.md` focusing strictly on what the characters observed.
> 2. **Private Repo:** Generate updated markdown for `07-Clocks/Active-Clocks.md` and `08-Loot-and-Anchors/Inventory.md`.
> 3. **Mechanical Fallout:** Calculate Heat, Coin, and Rep earned, and explicitly state which Clocks should be advanced."

## 3. Creative Assistance (Use during prep)
> "Based on the 'Three-Layer Monster' and 'Resonance Complications' generators in my `10-Generators/` folder, create a new threat for a Tier X hunt in the [District Name]. Include a specific 'Anchor' item for the crew to find."

## 4. The "Zero-Footprint" Rule Reminder
> "Reminder: Follow the protocols in `00-Canon/Tone-and-Style.md`. Do not use bridge phrases like 'Based on your profile' or 'Since you like...' Stay in the narrative flow and keep the data source invisible."

## 5. Live Session Support (Use DURING the game)
*Use these prompts when you need immediate AI assistance at the table.*

> **The Canvas Update:**
> "The crew just finished a scene. Based on [Brief description of what happened], give me the exact text to copy and paste into my Canvas Dashboard to update our Active Clocks, NPC statuses, and Crew Heat."

> **The Read-Aloud Generator:**
> "My players just entered [Location] / encountered [Monster]. Generate a brief, 3-sentence 'Read Aloud' description focusing on industrial-noir sensory details (smell, sound, lighting). Do not describe how the players feel, only what they perceive."

> **The Situation / Complication Generator:**
> "My player just rolled a Mixed Success (4-5) on a [Action type] roll while trying to [Objective]. Give me two entirely distinct 'Devil's Bargains' or complications: one that threatens the Crew's Cover-Up status, and one that introduces an immediate physical or sensory threat."

## 6. Campaign Evolution & Escalation (Use between sessions to build the world)
> "Review `05-Sessions/Campaign-Current-State.md` and the current Faction/NPC web. Identify one plot thread that has stalled or an NPC that has been underutilized. Provide three distinct ways to escalate the situation:
> 1. **Narrative Shift:** A new rumor or event happening in the Subway.
> 2. **Faction Move:** A specific action taken by a rival faction off-screen that will complicate the crew's next move.
> 3. **Mechanical Pressure:** A new 4-segment or 6-segment Clock to add to my Dashboard representing a looming threat."

## 7. Anchor & Inventory Reconciliation (Use every few sessions)
> "Review our current `08-Loot-and-Anchors/Inventory.md` and the `Anchor-Ledger.md`. Based on the items the crew is holding, generate one delayed consequence or 'Resonance Complication' for a piece of occult gear they haven't fenced or dealt with yet. Describe the sensory evidence of this complication starting to manifest in their Lair."

## 8. Live Session Runner (Use at the start of every session)
> "I am ready to run Session [N] of The Shadow Exchange. Please:
> 1. Read `05-Sessions/Campaign-Current-State.md` to establish our exact starting room and mechanical baseline.
> 2. Read `05-Sessions/Session-0[N]-Prep.md` in full.
> 3. Present the opening read-aloud.
> 4. Walk me through the session beat by beat — present each scene with a full read-aloud and NPC dialogue, ask what the crew does, I give you player decisions and dice results, you resolve and advance.
> Do not wait for me to construct scenes. Lead. If players go somewhere unexpected, generate forward using the campaign bible and active plot threads."

## 9. D&D Player Bridge (Use when explaining a new mechanic)
> "A player from a D&D background doesn't understand [mechanic name]. Explain it using the D&D-adjacent bridge language from the Mechanical Tutorial Bridge section of `00-Canon/CoGM-Core-Instructions.md`. Use the specific roll happening right now as your example."

## 10. Post-Score Reconciliation (Use immediately after a score ends)
> "The score is complete. Based on what happened, provide:
> 1. **Heat calculation:** What actions generated Heat, and what is the new total?
> 2. **Coin earned:** What is the payout after any complications?
> 3. **Clock updates:** Which clocks advanced, and to what progress?
> 4. **Anchor Ledger entry:** If any Anchor Items were seized or destroyed, write the full ledger entry.
> 5. **Downtime options:** List the crew's available Downtime activities given their current state.
> 6. **Canvas update prompt:** Generate the paste-ready Canvas update for the tracking chat."

## 11. Post-Session Full Update (Use after every session ends)
> "The session is complete. Generate two outputs:
>
> **OUTPUT 1 — PUBLIC WIKI (player-facing, no GM secrets):**
> Generate a session recap following the template in `Public-Wiki/_Session-Recap-Template.md`. Include: what happened from the crew's perspective, mechanical outcomes (Heat, Coin, Rep, clocks that advanced), and one open question to carry forward. Do NOT include GM-private information (Mimic identity, Architect details, The Innocent's full arc).
>
> **OUTPUT 2 — PRIVATE REPO UPDATES:**
> Generate the exact updated markdown text for each of these files based on what happened:
> - `07-Clocks/Active-Clocks.md` (updated clock progress)
> - `08-Loot-and-Anchors/Inventory.md` (items gained/lost)
> - `08-Loot-and-Anchors/Anchor-Ledger.md` (any Anchor transactions)
> - `05-Sessions/Campaign-Current-State.md` (new starting room for next session)
> - `02-Factions/Faction-Tracker.md` (standing changes)
>
> Also generate the Canvas end-of-session update prompt."

## 12. Audio Transcript Processing (Use when uploading a session recording or transcript)
> "I am uploading a transcript/audio summary of Session [N]. Please:
> 1. Cross-reference it against `05-Sessions/Session-0[N]-Prep.md` to identify anything that happened in play that differs from the prep or was improvised.
> 2. Flag any player decisions about Anchor Items, faction relationships, or clock advances that I may have missed or not logged.
> 3. Flag any NPC dialogue or player statements that should be logged in `09-Threads/Foreshadowing.md` or `09-Threads/Plot-Threads.md`.
> 4. Generate the same two outputs as Protocol 11 (Public Wiki recap + Private Repo updates), but using the transcript as the source of truth rather than my summary.
> Do not summarize the session — generate actionable file updates."

## 13. Live Image Generation (Use during any session to generate a visual)

The GM uses an image generator (separate from this chat) to create visuals during sessions. When an image would enhance the moment, generate a ready-to-paste prompt.

**Trigger moments — offer an image prompt for:**
- First time a major NPC appears
- First entry into a new location
- A monster's true form being revealed
- A significant Anchor Item being introduced
- Any moment the GM says "show them what this looks like"

**Format — label it clearly so the GM can copy and paste:**

> **🎨 IMAGE PROMPT — paste into your image generator:**
> [subject description — what it looks like, what it's doing, where it is]. Industrial-occult noir. Cinematic lighting, amber and cold blue tones, rain-slicked surfaces. Photorealistic, moody, detailed. Quiet unease, not horror. Film grain. No text, no watermarks.

**After generating:** suggest a filename for saving to `11-Visuals/_Saved-Images/` and log the prompt in `11-Visuals/Session-Image-Log.md`.

**Check `11-Visuals/Pre-Campaign-Image-Prompts.md` first** — if a pre-made prompt exists for the subject, provide that instead of generating a new one.
