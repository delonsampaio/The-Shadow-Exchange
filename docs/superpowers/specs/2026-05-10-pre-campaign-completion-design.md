# Design: Pre-Campaign Completion + Gemini Co-GM Upgrade
**Date:** 2026-05-10  
**Campaign:** The Shadow Exchange (Blades in the Dark)  
**Goal:** Complete all pre-campaign prep and upgrade Gemini from passive scribe to active session runner.

---

## Context

- 3 players, all from D&D/Pathfinder backgrounds. No characters made yet; playbooks TBD.
- Campaign has not started. Sessions 0–2 are prepped but not run.
- Gemini will co-GM every session: generating read-alouds, NPC dialogue, story beats, and walking the GM through each scene sequentially.
- Players expect detailed location descriptions on first entry, mechanical explanations when their characters would know them, and rich read-alouds throughout.

---

## Section 1: GEMINI.md Rewrite

### Problem
Current GEMINI.md defines Gemini as a reactive scribe ("Table Assistant"). It says "the GM runs live sessions in the web browser." This is the wrong role.

### Solution
Rewrite GEMINI.md to define Gemini as an **Active Session Runner**. Key additions:

**Session Walker Protocol**
- Gemini presents scenes sequentially without waiting for the GM to construct them.
- Each scene follows: Read-Aloud → NPC Dialogue (when NPCs are present) → "What does the crew do?" → Resolve action → Advance to next scene.
- Gemini reads the session prep file at the start and walks through it beat by beat.

**D&D Player Context**
- Every new location gets a full room-by-room description on first entry — not a summary, a walkthrough.
- Hidden areas the crew would know (like the Containment Suite) are revealed proactively, not gated behind rolls.
- Mechanics are explained in D&D-adjacent terms when first introduced (e.g., Position = how exposed you are, Effect = how much you accomplish — together they replace attack rolls and damage).

**Full NPC Voice**
- Every NPC in a scene gets complete dialogue, not attitude notes.
- Voice consistency: Ministry = cold and clinical. Subway denizens = wary and transactional. Twice-Born = human first.

**Mechanical Tutorial Bridge (Sessions 1–3)**
- When a Blades mechanic triggers for the first time, Gemini names it, explains it, and bridges to D&D equivalents.
- Proactively offer Flashbacks and Resistance Rolls by name, with brief explanations, the first 2–3 times they're relevant.

### Also update Co-GM-Prompts.md
- Add a "Live Session Runner" master prompt for starting sessions.
- Add a D&D player bridge prompt.
- Clarify that Gemini leads the scene; the GM feeds outcomes and player decisions.

---

## Section 2: New Files

| File | Purpose |
|---|---|
| `03-NPCs/Active/Emmerich.md` | Three-layer NPC file for Session 2's moral pivot |
| `03-NPCs/Active/Elias-Thorne.md` | The Mimic's current face — Ministry "True Believer" liaison. Needs tells, history, and GM-private flag. |
| `03-NPCs/GM-Private/The-Architect.md` | Backing file for Plot Thread 1 |
| `03-NPCs/GM-Private/The-Innocent-Civilian.md` | Backing file for Plot Thread 4 |
| `03-NPCs/Active/Ministry-Liaison.md` | Vance or Thorne — the crew's bureaucratic contact |
| `03-NPCs/Twice-Born/` — 2–3 individuals | Named Twice-Born with full three layers |
| `04-Locations/City-Districts.md` | City geography; connects Old City, the docks, the theater, shopping district |
| `06-Scores/Score-01-Merton.md` | Full score file for Session 1 |
| `06-Scores/Score-02-Emmerich.md` | Full score file for Session 2 |
| `09-Threads/Foreshadowing.md` seeds | 3–5 planted Mimic tells with session numbers |
| `10-Generators/Urban-Legends.md` — 8–10 leads | Populated leads for the Ritual downtime activity |

---

## Section 3: Files to Enhance

**`04-Locations/Curios-and-Chronicles.md`**
- Add room-by-room walkthrough: Front Shop → Back Room (Post-Op) → Containment Suite basement.
- Each room gets a sensory profile, key objects, and what a new employee would be told on their first day.
- The Containment Suite is a dungeon level in miniature — Cold Storage, Lead-Lined Vault, Trophy Wall, Post-Op Table each get a paragraph.

**`04-Locations/The-Subway/Stations.md`**
- Each station stub gets a full sensory profile and at least one active detail (an NPC doing something, an object that doesn't make sense, a sound with no source).
- D&D players will explore. Every station should feel like a room they can interact with.

**`Co-GM-Prompts.md`**
- Add Protocol 8: Live Session Runner (start-of-session master prompt).
- Add Protocol 9: D&D Player Bridge (use when explaining new mechanics).

---

## Success Criteria
- Gemini can receive a "start session" prompt and walk through the full session without the GM having to construct scenes.
- Every NPC the crew encounters has a full file with voice and three layers.
- D&D players can navigate the lair and the Subway on first entry without confusion.
- The Mimic's face (Elias Thorne, Ministry liaison) is decided, documented, and seeded with tells in the Foreshadowing log before Session 1.
- The Urban Legends generator has enough content to support the Ritual downtime activity across the first arc.
