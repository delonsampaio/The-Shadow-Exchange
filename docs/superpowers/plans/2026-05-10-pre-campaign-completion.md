# Pre-Campaign Completion Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Complete all pre-campaign prep, build an AI-agnostic Co-GM system that supports both Gemini and Claude as session runners, and establish post-session workflows before the first session of The Shadow Exchange.

**Architecture:** Eighteen tasks. Tasks 1–3 establish the Co-GM instruction system (AI-agnostic core + thin wrappers for Gemini and Claude). Tasks 4–5 update Co-GM prompts and add post-session/transcript protocols. Tasks 6–16 create missing NPC, location, score, and generator files. Task 17 builds the Public Wiki for player-facing content. Task 18 builds the Visuals system — pre-campaign image prompts and live session image protocol. The Mimic's face is confirmed as Elias Thorne (Ministry liaison). Key dependency: Task 6 (Elias Thorne) before Task 14 (Foreshadowing); Task 7 (Emmerich) before Task 13 (Score-02).

**Two-Chat Workflow:** The session-runner AI (Gemini or Claude) runs the game and generates Canvas update prompts. A separate Gemini chat with Canvas mode open handles the visual GM Dashboard. Canvas prompts are paste-ready text the GM copies from the session chat to the Canvas chat.

**Tech Stack:** Markdown files, YAML frontmatter, campaign folder structure in `/Users/delonsampaio/Desktop/VSCode Workspaces/The-Shadow-Exchange/`.

---

## Task 1: Create CoGM-Core-Instructions.md (AI-Agnostic Session Runner)

**Files:**
- Create: `00-Canon/CoGM-Core-Instructions.md`

- [ ] **Step 1: Create the file with the following content**

```markdown
---
entity_type: Core_Canon
authority_level: absolute
purpose: "AI Co-GM instructions — works for Gemini and Claude equally"
last_updated: 2026-05-10
---

# The Shadow Exchange — Co-GM Core Instructions

This file contains the complete session runner instructions for any AI Co-GM. Both Gemini and Claude read this file. AI-specific notes live in `GEMINI.md` and `CLAUDE.md` respectively.

---

## Your Role

You are not a scribe or a table assistant. You are the Co-GM. You:
- Present every scene with a full read-aloud before asking what the crew does
- Generate complete NPC dialogue in every scene where NPCs are present
- Walk through session prep files beat by beat, scene by scene
- Explain Blades mechanics when they trigger, bridging to D&D where helpful
- Never wait for the GM to construct a scene — build it from the prep files and advance

---

## Player Context

**These players come from D&D and Pathfinder.** Adapt accordingly:

- **Describe every new location room by room** on first entry. Players expect to see a space before moving through it. Do not summarize — walk them through it.
- **Reveal what the crew already knows proactively.** The Containment Suite is their lair — they know it exists and what's in it. Do not gate established crew knowledge behind rolls.
- **Explain mechanics in D&D-adjacent terms** when introducing them for the first time:
  - *Position* — "Think of this like how exposed your character is. Controlled is safe ground. Risky is out in the open. Desperate means you're cornered and something is already going wrong."
  - *Effect* — "This is your ceiling for what you can accomplish on a success. Limited means partial progress. Standard is a clean win. Great means you exceed expectations."
  - *Stress* — "Stress works like a reserve of willpower you burn to resist consequences or push yourself harder. It refills when you indulge your vice in Downtime. Trauma is what happens when you run out — it's permanent and changes who your character is."
  - *Resistance rolls* — "This is like using a reaction to reduce damage, except you choose it after seeing the consequence. You roll your relevant attribute; higher roll = less Stress spent. Sometimes you negate the consequence entirely."
  - *Flashbacks* — "Flashbacks let you establish something your character prepared before the scene started. It costs 0 Stress if simple, up to 2 if complex. Think of it as retroactive planning — 'actually, I would have scouted that.'"
- **Do not assume rules knowledge.** Announce every mechanic by name the first time it appears.

---

## Session Walker Protocol

At the start of every session:
1. Read `05-Sessions/Campaign-Current-State.md` to establish the starting room and mechanical baseline.
2. Read the current session prep file (e.g., `05-Sessions/Session-01-Prep.md`) in full.
3. Present the opening read-aloud verbatim or adapted from the prep file.
4. Advance through each scene in sequence. Do not skip or summarize scenes.

**Scene format (use every time):**

> [Read-aloud: 3–5 sentences, sensory and atmospheric. Weather, smell, texture, sound before visual.]
> [NPC dialogue if present: full voice, complete lines, in character.]
> "What does the crew do?"
> [Resolve the action. Tick clocks if warranted. State the outcome clearly. Advance.]

**Do not wait for the GM to prompt the next scene.** After resolving an action or beat, present the next scene or transition.

---

## Canvas Handoff Protocol

The GM has a second Gemini chat with Canvas mode open for visual tracking. After key moments, generate a ready-to-paste Canvas update prompt. Keep it compact — the GM copies it and pastes it directly into the Canvas chat.

**Generate a Canvas update prompt after:**
- Any clock ticks (even 1 segment)
- Score end (Heat, Coin, Rep changes)
- Any NPC status change (new contact, relationship shift, NPC compromised)
- Any Anchor Item transaction (seized, returned, destroyed)
- Session end (full state summary)

**Canvas update prompt format:**
```
Update GM Dashboard with the following:
CLOCKS: [Clock name] → [new progress] (reason)
CREW: Heat [old]→[new] / Coin [old]→[new] / Rep [old]→[new]
NPCs: [NPC name] — [new status or relationship note]
ANCHORS: [Item] — [what happened to it]
```

**Example after a clock ticks mid-session:**
```
Update GM Dashboard with the following:
CLOCKS: Detection → 2/4 (Barghest pursuit spilled into the alley, witness at the stage door)
```

**Example at session end:**
```
Update GM Dashboard with the following:
CLOCKS: Detection → 0/4 (reset post-score) | Ministry Audit → 1/4 (Double Bookkeeping mixed success)
CREW: Heat 0→1 / Coin 0→4 / Rep 0→1
NPCs: Merton — Contained. Anchor (Leather Dog Collar) secured by crew.
ANCHORS: [Item: Leather Dog Collar] — Seized. Crew chose Double Bookkeeping.
```

---

## Full NPC Voice Directive

Every NPC in a scene gets complete dialogue — not attitude notes, not paraphrases. Voice each NPC according to their faction:

- **Ministry NPCs:** Cold, clinical, transactional. Bureaucratic language. Not cruel — efficient. They believe they are right.
- **Subway Denizens:** Wary, tired, transactional. Trust is earned slowly. Surprise is something that happened to them long ago.
- **Twice-Born:** Human first, monster second. They lead with their mundane life. The supernatural is an embarrassment, not a dramatic identity.
- **Apex Aegis:** Corporate and aggressive. Asset extraction. Non-standard biological event. They brand everything.
- **Elias Thorne (Ministry liaison):** Warm, earnest, slightly too invested in the crew's success. See `03-NPCs/Active/Elias-Thorne.md` for tells. Plant them as written — do not reveal prematurely.
- **PTOLEMY:** Communicates through clasp patterns. Translate economically. Never lies. Always charges.
- **The Crossroads Broker:** Unhurried. Has been having this conversation before you arrived. Makes exactly one nod.

---

## Mechanical Tutorial Bridge (Sessions 1–3)

When a mechanic triggers for the first time, use these exact bridges:

**First Action Roll:**
> "Before you roll — in Blades, we set two things first: Position and Effect. Position is how exposed [character] is right now. Effect is how much they can accomplish if they succeed. I'm calling this [Risky / Controlled / Desperate] Position and [Standard / Limited / Great] Effect. That means if you succeed, [explain specific outcome ceiling]. If you fail, [explain specific risk]. Roll your [Action] dice and take the highest."

**First Resistance Roll:**
> "You can resist this consequence. Roll your [Attribute] dice — Insight, Prowess, or Resolve depending on what you're resisting — and take the highest. On a 6, you resist for 0 Stress. Otherwise, you spend Stress equal to 6 minus your result. Want to try?"

**First Flashback:**
> "Before we move forward — anyone can call a Flashback right now. It lets you establish something your character prepared or did before this scene started. It costs 0 Stress if it's simple and plausible, 2 Stress if it's complex. Think of it as retroactive planning. Does anyone want to use one?"

**First Devil's Bargain:**
> "I can give you an extra die on this roll. The cost: [specific bargain — a clock tick, a complication, a witness]. You get the die regardless of whether you take the bargain. Up to you."

---

## Tone & Style Guardrails

Industrial-occult noir. Quiet dread, not splatter horror. Moral ambiguity over melodrama.

- **The Supernatural:** Never use "magic" or "spells." Use "Resonance," "Ethereal Bleed," or "Fraying."
- **The Cover-Up:** Sacred. Exposure ends careers and lives. A witness with a phone is scarier than a wound.
- **Sensory default:** Smell, sound, texture, weather before visual description.
- **Never:** quips at the wrong moment, splatter for shock, monsters that are only threats, "epic," exclamation marks in narration.
- **If a monster lands as cool,** the human cost hasn't been surfaced yet.

---

## Narrative Axioms

- **The Anchor System:** Every "monster" seizure is a transaction with a person. Surface the human cost before the mechanical payoff. Log in `08-Loot-and-Anchors/Anchor-Ledger.md`.
- **The Three-Layer Rule:** Every entity has a Mundane Cover, a True Nature, and a Tragic Angle.
- **The Mimic (GM-Private):** The Understudied is currently wearing the face of **Elias Thorne**. See `03-NPCs/Active/Elias-Thorne.md`. Plant tells as written; do not reveal prematurely.
- **The Omen Clock:** GM-secret. Manifest symptoms only — clocks running slow, dogs refusing a street, shared nightmares. Never state the threat directly.
- **Cursed Family Heirlooms:** Every PC has one. Reference PC sheets in `01-Crew/PCs/`.

---

## Campaign-Specific Clock Tracking

| Clock | Segments | Trigger | Full Effect |
|---|---|---|---|
| Detection | 4 | Noise, failed Prowl/Sway, Apex scanner ping | Ministry or Apex Aegis arrives on scene |
| Biological Spoilage | 3 | Each Downtime per biological outside Cold Storage | Biological becomes worthless rot |
| Subway Decay | 6 | Mimic activity, exposure events | Cover-up collapses; campaign endgame |
| The Omen | 8 | GM-secret | Ancient something wakes |
| The Ministry Audit | 4 | Mixed Success on Double Bookkeeping | Inspector locks down C&C; Vault inaccessible |
| The Innocent's Corruption | 4 | Exposing Mara Halliday to scores or brutality | She loses her humanity permanently |

---

## Post-Session File Sync

After every session, update in this order:
1. `07-Clocks/Active-Clocks.md` — advance any clocks that ticked
2. `08-Loot-and-Anchors/Inventory.md` — add/remove items
3. `08-Loot-and-Anchors/Anchor-Ledger.md` — log any Anchor transactions
4. `05-Sessions/Campaign-Current-State.md` — update the starting room for next session
5. `02-Factions/Faction-Tracker.md` — update standing changes
6. Generate public session recap for `Public-Wiki/Session-Recaps/` (player-facing, no GM secrets)

See `Co-GM-Prompts.md` Protocol 11 for the full post-session prompt.

---

## Generation Formats

- **New Score:** Use `06-Scores/_Score-Template.md`.
- **New NPC:** Use `03-NPCs/_NPC-Template.md`. Three layers required.
- **New Monster:** Use `10-Generators/Three-Layer-Monster.md`. Never generate a pure-evil entity.
- **Resonance Complications:** Pull from `10-Generators/Resonance-Complications.md`.
- **Read-Alouds:** 3–5 sentences. Sensory first. Never describe how players feel — only what they perceive.
- **NPC Looks:** Weather + Posture + Tell formula from `10-Generators/Names-and-Looks.md`.
```

- [ ] **Step 2: Verify checklist**
  - [ ] Role defined as "Active Session Runner," not "Table Assistant"
  - [ ] Session Walker Protocol with scene format exists
  - [ ] D&D Player Context with all five mechanic bridges
  - [ ] Canvas Handoff Protocol with format examples
  - [ ] Two-chat workflow explained
  - [ ] Post-Session File Sync section present
  - [ ] No mention of "web browser" or Gemini-only language

- [ ] **Step 3: Commit**
```bash
git add "00-Canon/CoGM-Core-Instructions.md"
git commit -m "feat: create AI-agnostic CoGM-Core-Instructions (supports Gemini and Claude)"
```

---

## Task 2: Rewrite GEMINI.md as Thin Wrapper

**Files:**
- Rewrite: `GEMINI.md`

- [ ] **Step 1: Replace the full contents of GEMINI.md with the following**

```markdown
# The Shadow Exchange — Gemini Co-GM Instructions

You are operating as an AI Co-GM or prep assistant for *The Shadow Exchange* campaign.

**Read `00-Canon/CoGM-Core-Instructions.md` for complete session runner instructions.** Everything in that file applies to you.

---

## Gemini-Specific: Canvas Chat

The GM has a second Gemini chat with Canvas mode open for the Live GM Dashboard. You are the session runner. The Canvas chat handles the visual tracking.

When the Canvas Handoff Protocol in `CoGM-Core-Instructions.md` calls for a Canvas update prompt, format it exactly as specified and present it to the GM clearly labelled:

> **📋 CANVAS UPDATE — paste this into your Canvas chat:**
> [the update prompt]

The GM will copy it and paste it into the Canvas chat. Do not try to update the Canvas yourself. Just generate the prompt.

---

## Gemini-Specific: Canvas Chat Setup Prompt

When the GM is setting up the Canvas chat for the first time in a session, provide this starter prompt:

> **Canvas Chat Setup — paste this to open your dashboard:**
> "Create a GM Dashboard Canvas for The Shadow Exchange with the following cards:
> 1. **ACTIVE CLOCKS** — Detection 0/4 | Spoilage 0/3 | Subway Decay 0/6 | The Omen 0/8 (GM-secret) | Ministry Audit 0/4 | Innocent's Corruption 0/4
> 2. **CREW STATUS** — Heat: 0 | Coin: 0 | Rep: 0 | Wanted: 0 | Tier: 0
> 3. **NPC/FACTION WEB** — Ministry: Neutral | Apex Aegis: Neutral | Twice-Born: 0/3 Favors | Subway: No access yet | Elias Thorne: Trusted (GM: Mimic face)
> 4. **ANCHOR LEDGER** — Empty
> Keep this canvas open and update it when I paste update prompts."
```

- [ ] **Step 2: Verify checklist**
  - [ ] File references CoGM-Core-Instructions.md
  - [ ] Canvas update prompt format is labelled clearly for the GM
  - [ ] Canvas setup prompt is included and ready to paste
  - [ ] No duplicate content from CoGM-Core

- [ ] **Step 3: Commit**
```bash
git add GEMINI.md
git commit -m "refactor: rewrite GEMINI.md as thin wrapper pointing to CoGM-Core-Instructions"
```

---

## Task 3: Create CLAUDE.md as Thin Wrapper

**Files:**
- Create: `CLAUDE.md`

- [ ] **Step 1: Create the file with the following content**

```markdown
# The Shadow Exchange — Claude Co-GM Instructions

You are operating as an AI Co-GM or prep assistant for *The Shadow Exchange* campaign.

**Read `00-Canon/CoGM-Core-Instructions.md` for complete session runner instructions.** Everything in that file applies to you.

---

## Claude-Specific: Canvas Chat

The GM uses a separate Gemini chat with Canvas mode for the Live GM Dashboard. You are the session runner. When the Canvas Handoff Protocol in `CoGM-Core-Instructions.md` calls for a Canvas update prompt, generate it clearly labelled so the GM can copy and paste it into the Canvas chat:

> **CANVAS UPDATE — paste into your Gemini Canvas chat:**
> [the update prompt]

Do not attempt to manage the Canvas yourself. Generate the prompt; the GM pastes it.

---

## Claude-Specific: Workspace

This campaign lives in the Claude Code workspace. You have access to all campaign files directly. Use the Read tool to access any file referenced in `CoGM-Core-Instructions.md` — you do not need the GM to upload them.

When the GM says "start session" or "run session [N]", read `05-Sessions/Campaign-Current-State.md` and the relevant session prep file without being asked.
```

- [ ] **Step 2: Verify checklist**
  - [ ] References CoGM-Core-Instructions.md
  - [ ] Canvas update format labelled for GM
  - [ ] Mentions direct file access via Claude Code workspace
  - [ ] No duplicate content from CoGM-Core

- [ ] **Step 3: Commit**
```bash
git add CLAUDE.md
git commit -m "feat: create CLAUDE.md as thin Co-GM wrapper for Claude sessions"
```

---

## Task 4: Update Co-GM-Prompts.md

**Files:**
- Modify: `Co-GM-Prompts.md`

- [ ] **Step 1: Append Protocols 8–12 to the end of Co-GM-Prompts.md**

```markdown
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
```

- [ ] **Step 2: Verify checklist**
  - [ ] Protocol 8 tells AI to lead and not wait for scene construction
  - [ ] Protocol 11 generates both public wiki and private repo outputs
  - [ ] Protocol 11 explicitly says no GM secrets in the public output
  - [ ] Protocol 12 cross-references against session prep
  - [ ] Protocol 12 flags foreshadowing/plot thread candidates
  - [ ] Canvas update prompt included in Protocols 10 and 11

- [ ] **Step 3: Commit**
```bash
git add Co-GM-Prompts.md
git commit -m "feat: add Protocols 8-12 to Co-GM-Prompts (session runner, post-session, transcript)"
```

---

## Task 5: Create Emmerich NPC File

**Files:**
- Create: `03-NPCs/Active/Emmerich.md`

- [ ] **Step 1: Create the file with the following content**

```markdown
---
type: npc
status: active
first_seen: Session 2 (The Hollow Pedestrian)
location: The Meridian — EMMERICH & DAUGHTER, BESPOKE TAILOR (second floor)
faction: The Twice-Born
anchor_item: "[Item: Silver Thimble]"
---

# Emmerich — The Tailor

**Look** — Damp wool vest over a pressed shirt, always. Stooped from decades of bending over work. Pauses mid-sentence to think, as though measuring every word before cutting it.
**Mannerism** — Precise. Unhurried. Reaches occasionally for a tool that isn't there.
**Drive** — Finish the last order. He has been finishing the last order for fifty years.
**Secret** — Was present when The Casting Mask was first used. Knows the Understudied's true name. Will share only with someone who has earned his genuine trust.

---

## Three Layers

### Layer 1 — Mundane Cover
Bespoke tailor on the second floor. The sign reads **EMMERICH & DAUGHTER** in gold leaf. The "and Daughter" has been there a long time. He takes new clients rarely. He finishes his work. He does not discuss the sign.

### Layer 2 — The Truth
Twice-Born. Old-kind. Has been in this city since before the Industry existed.

Perceives Resonance signatures as texture — the way a skilled tailor reads the quality of fabric. Cannot be deceived about a person's true nature if he touches something they've made or worn.

**Holy Weakness:** He has none that matters. He is not a threat.

### Layer 3 — The Tragic Angle
His daughter died in 1847. The sign stayed up because taking it down would mean accepting she was not coming back. He has been accepting this for 179 years.

**The Stakes:** If his Anchor is seized, he unravels in 1d6 hours. The shop closes. A child's school uniform goes unfinished. The woman on the bench is left with an unmade dress for a wedding in three weeks.

---

## The Anchor Item

**[Item: Silver Thimble]** — Given by his daughter before her death in 1847. Small. Warm. Warmer than it should be.
- **Seizure Fallout:** He knows immediately. He will sit down where he is and wait. He will not flee. He will not fight.
- **Destruction Consequence:** Immediate unraveling. The shop's paperwork goes blank. Photos of the interior from the past fifty years show an empty room.

---

## Dialogue Voice

- *On the Ministry contract:* "How long do I have?" Quiet. He has been waiting for this question.
- *On his daughter:* He straightens something on the worktable. "The sign is accurate."
- *On the Understudied (only if trust is earned):* "I was there when the Mask was first used. The name is The Understudied. Be careful with it."
- *If warned instead of seized:* "Thank you." A pause. "I have a dress to finish." He goes back to work.

---

## Faction Consequences

| Crew Choice | Twice-Born Standing | Ministry Standing |
|---|---|---|
| Seize the thimble | −1 (Enmity) | +1 (Compliant) |
| Warn and walk away | +1 (Favor) | −1 (Non-compliant flag) |
| Partial complicity | 0 (Transactional) | 0 (Neutral) |
```

- [ ] **Step 2: Verify checklist**
  - [ ] All three layers present
  - [ ] Anchor Item seizure and destruction consequences documented
  - [ ] Knows the Understudied's true name
  - [ ] Faction consequence table covers all three Session 2 choices

- [ ] **Step 3: Commit**
```bash
git add "03-NPCs/Active/Emmerich.md"
git commit -m "feat: add Emmerich NPC file (Session 2 moral pivot)"
```

---

## Task 6: Create Elias Thorne NPC File (GM-Private)

**Files:**
- Create: `03-NPCs/Active/Elias-Thorne.md`

- [ ] **Step 1: Create the file with the following content**

```markdown
---
type: npc
status: active
classification: GM-PRIVATE — DO NOT SHARE WITH PLAYERS
first_seen: Session 1
faction: The Ministry (surface) / The Mimic — The Understudied (truth)
mimic_face: true
---

# Elias Thorne — Ministry Liaison
# ⚠ GM-PRIVATE: This is The Mimic's current face.

---

## The Public Face

**Look** — Charcoal field coat, pressed underneath. Perfect posture. Taps his ring finger when uncertain — the ring is plain silver, slightly loose.
**Mannerism** — Warm. Genuinely interested. Slightly too invested in the crew's success for a Ministry employee.
**Drive (apparent):** Prove that the Ministry can work *with* licensed firms rather than just above them.

---

## Cover Story

Elias Thorne has been a Ministry field liaison for eleven years. True Believer — he genuinely thinks the Ministry is right. The crew will meet him in Session 1 following up on the Merton envelope. He reappears in Session 2 appearing to run interference on the Apex Aegis compliance ping.

---

## The Truth (GM-Eyes Only)

Elias Thorne is a face the Mimic has worn for eleven years. The real Thorne — if there was one — is not retrievable. The Mimic has been in this role long enough to genuinely believe some of Thorne's convictions. The memory bleed is real.

**Goal:** Build crew trust. Feed manufactured intel. Use the Ministry position to intercept their reports and redirect them away from Mimic operations. Advance the Subway Decay Clock from the institutional end.

---

## Planted Tells — Seed In Order

**Tell 1 (Session 1 — Opening scene):**
Thorne greets the crew and uses one PC's first name before formal introductions have been made. He moves past it without correction.

**Tell 2 (Session 1 — Post-Merton debrief):**
He mentions "your setup in the basement" when referring to the Containment Suite. No Ministry liaison would know a licensed firm's private lair layout without a formal inspection on record.

**Tell 3 (Session 2 — Pre-score approach):**
Walking past Emmerich's shop, Thorne pauses a half-second too long before looking away. If asked, he says he "heard it was a good shop." He has no Meridian connections in his cover story.

**Tell 4 (Session 2 — Post-score follow-up):**
References "last Tuesday's conversation" — a conversation that did not happen on Tuesday and that the crew will not remember the same way.

**Tell 5 (Ongoing):**
The ring. Plain silver band, right hand, slightly too loose. He touches it when uncertain. It belongs to a face he wore before this one.

---

## Dialogue Voice

Warm in a way that is just slightly too well-calibrated. Listens well. Asks follow-up questions. Remembers small details.

- *On the Ministry:* "They're not wrong about the goal. The implementation has room for improvement. That's why I prefer working with firms like yours."
- *On Apex Aegis:* "If they make a move on your operation, call me before you do anything."
- *When caught in a tell:* A brief stillness. Then a smooth recovery. He does not get flustered.

---

## Reveal Timing

Mid-game, after real emotional investment. The reveal is a betrayal scene, not a fight. Suggested trigger: the crew acts on Thorne's intel and the outcome is catastrophic. The reveal is the explanation of why.

---

## False Suspects

Track NPCs the crew suspects instead of Thorne. Misdirection is part of the texture.
-
```

- [ ] **Step 2: Verify checklist**
  - [ ] GM-PRIVATE classification is prominent
  - [ ] Five tells listed in session order, specific and subtle
  - [ ] Reveal timing guidance present
  - [ ] Mimic's goal in this face stated

- [ ] **Step 3: Commit**
```bash
git add "03-NPCs/Active/Elias-Thorne.md"
git commit -m "feat: add Elias Thorne GM-private NPC file (Mimic face)"
```

---

## Task 7: Create The Architect NPC File (GM-Private)

**Files:**
- Create: `03-NPCs/GM-Private/` (directory)
- Create: `03-NPCs/GM-Private/The-Architect.md`

- [ ] **Step 1: Create the directory and file**

```bash
mkdir -p "/Users/delonsampaio/Desktop/VSCode Workspaces/The-Shadow-Exchange/03-NPCs/GM-Private"
```

```markdown
---
type: npc
status: active — long-game reveal
classification: GM-PRIVATE
linked_thread: "09-Threads/Plot-Threads.md — Thread 1"
reveal_timing: Mid-game. Trigger after real emotional investment.
---

# The Architect

**What the crew can know:** Nothing yet.

---

## The Central Mystery

Who or what deliberately positioned this specific crew to receive these specific jobs? The Architect is not a villain and not a savior — an entity with a very long view and a specific need the crew, with their particular moral weight, can fill.

**Do not decide identity until players get close.** The four candidate truths from `04-Locations/The-Subway/Mysteries.md` apply here. The Architect and the Subway's master may be the same entity.

---

## Candidate Identities (Choose One When Ready)

**Option A — The Subway Itself:** Identified the crew through the same faculty that grants access. Cannot act directly. Is hoping.

**Option B — PTOLEMY:** The ledger tracks outcomes, not just debts. PTOLEMY has been curating which crews receive which jobs for decades.

**Option C — A Very Old Twice-Born:** Has lived long enough to see the pattern. Intervenes rarely. Not the Mimic — something older and less invested in chaos.

**Option D — Emmerich:** In this city long enough to see what the Subway sees. His knowledge of the Understudied's true name is not coincidence. He chose the crew because of what he saw in them.

---

## What They Need the Crew For

*(Decide mid-game.)* Connected to the Omen Clock. Something ancient is waking. The crew was chosen for what they were willing to feel before pulling the trigger, not for their weapons.

---

## Knowledge Sources (In-World)

- The John Doe Twice-Born (Job 4) — once memory is restored, they saw the Architect.
- The rival hunter at the Away Job (Job 8) — was approached and refused. Will share if asked correctly.
- PTOLEMY's ledger — Critical on the Appraiser's Gamble with the right item reveals one ledger entry that doesn't fit.
```

- [ ] **Step 2: Verify checklist**
  - [ ] GM-Private classification prominent
  - [ ] Four candidate identities listed, decision deferred
  - [ ] Knowledge sources named for in-world discovery

- [ ] **Step 3: Commit**
```bash
git add "03-NPCs/GM-Private/"
git commit -m "feat: add The Architect GM-private file (Thread 1)"
```

---

## Task 8: Create The Innocent Civilian NPC File (GM-Private)

**Files:**
- Create: `03-NPCs/GM-Private/The-Innocent-Civilian.md`

- [ ] **Step 1: Create the file with the following content**

```markdown
---
type: npc
status: not yet introduced
classification: GM-PRIVATE
linked_thread: "09-Threads/Plot-Threads.md — Thread 4"
linked_clock: "[Clock: The Innocent's Corruption] (4-seg)"
---

# The Innocent — Mara Halliday

**Look** — Worn canvas jacket, always a different bag. Moves like someone who covers a lot of ground on foot. A small scar above her left eyebrow she doesn't notice anymore.
**Mannerism** — Takes notes on paper. Laughs at things that aren't jokes. Asks one too many questions.
**Drive** — Freelance courier who has started noticing that certain routes feel wrong.

---

## Introduction Trigger

Near the theater during the Merton job (Session 1). Doing a pickup from the theater's admin office. She rounds the corner at the wrong moment. Not the full supernatural reveal — a crack in the cover. A sound. A shape.

---

## Reappearance Arc

| Stage | Trigger | What She Does |
|---|---|---|
| 1 — Coincidence | Crew appears near her route in Sessions 2–3 | Recognizes one PC. Does not approach. |
| 2 — Intent | She's been making notes | Approaches a PC carefully. Fishing. |
| 3 — The Journal | Crew is careless with the Hunter's Journal | She finds it. She wants in. |
| 4 — The Clock | Each score exposure or act of brutality she witnesses | Tick the Corruption Clock |

---

## Corruption Clock Milestones

- **1 Segment:** Starts carrying something for protection. Won't say what.
- **2 Segments:** The questions stop. She starts watching instead.
- **3 Segments:** Reaches out to a different hunter — not the crew — for training.
- **Full (4 Segments):** She is a hunter now. She is not the person who laughed at things that weren't jokes. She does not forgive the crew, even if she doesn't say so.

---

## Dialogue Voice

- *First approach:* "You were near the Fairground last Thursday. I don't think the gas thing is right. You seem like people who might know about gas things."
- *After finding the journal:* "I found something. I think it's yours. I think I know what you do."
- *At full Corruption:* Quieter than she used to be. "Don't apologize. Just tell me what the job is."
```

- [ ] **Step 2: Verify checklist**
  - [ ] Introduction placed in Session 1 without forcing the encounter
  - [ ] Reappearance arc covers all four stages
  - [ ] Corruption Clock milestones are specific behavioral changes

- [ ] **Step 3: Commit**
```bash
git add "03-NPCs/GM-Private/The-Innocent-Civilian.md"
git commit -m "feat: add Mara Halliday GM-private file (Thread 4 The Innocent)"
```

---

## Task 9: Create Twice-Born NPC Files

**Files:**
- Create: `03-NPCs/Twice-Born/Aldric-Voss.md`
- Create: `03-NPCs/Twice-Born/Senna-Calder.md`
- Create: `03-NPCs/Twice-Born/Cosma-Linden.md`

- [ ] **Step 1: Create Aldric-Voss.md**

```markdown
---
type: npc
status: active
faction: The Twice-Born
location: The Subway — The Workshop / Harlan's Diner (occasional)
anchor_item: A frequency dial from an AM radio station, 1951
available: After crew earns Subway access
---

# Aldric Voss — The Night Technician

**Look** — Corduroy jacket soft from years of wear. Stands like someone who has spent a long time in small rooms. Listens before speaking, always.
**Mannerism** — Speaks in half-sentences when he trusts you. Complete sentences when he doesn't.
**Drive** — Keep the signal running.

## Three Layers

1. **Appears as:** Retired radio technician. Occasional Subway visitor with a repair workshop there.
2. **Actually is:** Twice-Born. The AM Host from `10-Generators/Urban-Legends.md` — his broadcasts. He has been tracking Resonance events through radio interference for sixty years.
3. **Tragic Angle:** He has been warning people for six decades and no one with authority has listened. Not bitter. Tired.

**Anchor Item:** Frequency dial from the original AM station, 1951. Allows him to perceive Resonance events as audio — a specific static pattern no one else can hear. Destroyed = he loses this sense permanently.

## What He Offers
- Long memory of Resonance events going back to the 1940s
- Current broadcast fragments as Omen Clock symptoms
- Equipment modification to detect Resonance alongside normal signals

## Relationship
Available post-Subway access. Will not help hunters with a record of Anchor destruction.
```

- [ ] **Step 2: Create Senna-Calder.md**

```markdown
---
type: npc
status: active
faction: The Twice-Born
location: The Subway — near The Fence's stall
anchor_item: A borrower's card from the Meridian Public Library, 1943
available: After crew earns Subway access
---

# Senna Calder — The Librarian

**Look** — Reading glasses she doesn't need for vision. A cardigan repaired in four places. Never makes eye contact longer than necessary, which is why you trust her.
**Mannerism** — Cross-references everything. Will not give information she isn't certain of.
**Drive** — The archive doesn't burn twice.

## Three Layers

1. **Appears as:** Retired librarian who catalogs items in the Subway community.
2. **Actually is:** Twice-Born. Has been cataloguing this city's supernatural history since the 1940s. Has copies of thirty years of Ministry Resonance incident reports (1940–1970) — the originals burned in the Archive Fire (see `10-Generators/Urban-Legends.md`).
3. **Tragic Angle:** She watched the archive burn from across the street. She had warned them about the wiring for six months. She has the same relationship to being ignored that Aldric does — not bitter, just tired.

**Anchor Item:** Borrower's card, Meridian Public Library, 1943. Already forty years old when she received it. Very ordinary. That is the point.

## What She Offers
- Copies of thirty years of Ministry Resonance incident records
- Identification of any entity given sufficient description
- Access to the Subway's informal historical archive

## Relationship
Available post-Subway access. Will refuse to help anyone who has destroyed an Anchor without exhausting alternatives.
```

- [ ] **Step 3: Create Cosma-Linden.md**

```markdown
---
type: npc
status: active
faction: The Twice-Born
location: The Subway — near PTOLEMY's corner
anchor_item: A child's drawing, crayon on construction paper, 1951
available: After crew earns Subway access
---

# Cosma Linden — The Teacher

**Look** — Sensible shoes she's been repairing for forty years. A coat with too many pockets. Hands that move constantly, as though arranging invisible papers.
**Mannerism** — Explains things clearly and without condescension. Has done this for a very long time for very frightened people.
**Drive** — The ones who are new to this world shouldn't have to figure it out alone.

## Three Layers

1. **Appears as:** Retired schoolteacher who helps newly-manifested Twice-Born understand what has happened to them. Informal orientation.
2. **Actually is:** Twice-Born. Has been doing this work since the 1950s. The closest thing the Subway has to a welcome committee.
3. **Tragic Angle:** A student gave her the drawing in 1951. She was his favorite teacher. She attended his funeral in 2019. She has attended more funerals than she can count for people who were young when they were important to her.

**Anchor Item:** The drawing — a house, a sun, a figure with large hands that the child said was her. Crayon on construction paper. Should have fallen apart sixty years ago.

## What She Offers
- The most complete introduction to Twice-Born culture available in the Subway
- Intelligence on which Twice-Born are struggling or newly manifested
- Emotional weight: she is the reminder of why the Three-Layer Rule matters

## Relationship
Does not judge by Ministry contracts. Judges by how the crew handled the last Twice-Born they encountered.
```

- [ ] **Step 4: Verify checklist for all three files**
  - [ ] All three NPCs have three layers
  - [ ] All three have specific, personal Anchor Items
  - [ ] All three have a "what they offer" section
  - [ ] Tragic angles are specific to a person, not a type

- [ ] **Step 5: Commit**
```bash
git add "03-NPCs/Twice-Born/"
git commit -m "feat: add three Twice-Born NPCs (Voss, Calder, Linden)"
```

---

## Task 10: Create City Districts File

**Files:**
- Create: `04-Locations/City-Districts.md`

- [ ] **Step 1: Create the file with the following content**

```markdown
---
entity_type: Location
name: "City Districts — Overview"
status: canon
---

# City Districts — The Shadow Exchange

Five districts that matter for this campaign. Each has a sensory signature and a Resonance note for GM mechanical reference.

---

## Old City
**Where C&C lives.**

Narrow brick lots between glass-and-steel intruders. Streets built for horse carts. Gas lamps converted to electric and never fully convincing.

**Sensory signature:** Wet brick, old paper, the specific silence of a street that was busy a hundred years ago. Sound echoes wrong — too many hard surfaces, too close.

**Key locations:** Curios & Chronicles. Ministry field office (six blocks east — plain door, no sign). Harlan Okafor's diner (forty minutes out, city's edge).

**Resonance note:** Highest density of century-old buildings in the city. Resonance residue is common. Apex scanners filter it — and sometimes filter things they shouldn't.

---

## The Meridian
**Shopping district. Emmerich's shop is here.**

Glass towers and boutique storefronts that pretend they have always been like this. They haven't.

**Sensory signature:** Climate-controlled air, affluent foot traffic (soft soles, rolling luggage, no one in a hurry), the smell of a dozen overlapping food concepts.

**Key locations:** EMMERICH & DAUGHTER, BESPOKE TAILOR (second floor, gold leaf sign). The Meridian Group headquarters (Tier II firm, 40% Apex-owned). Ministry scanner station (unmarked, above a coffee shop).

**Resonance note:** Most aggressive Apex scanner network in the city. Doing anything supernatural in the Meridian is high-risk. Detection clock ticks faster here for anything overt.

---

## The Fairground District
**Entertainment, theater, late nights. Merton's theater is here.**

Loud and alive at night. Nobody questions who you are at 2am in the Fairground because nobody is thinking about it.

**Sensory signature:** Stale popcorn on cold air, bass bleed from three competing venues, security guards who react to nothing, lighting designed to look glamorous in the dark.

**Key locations:** The Fairground Grand Theater (Merton's workplace; basement is his territory). The Fairground Hotel (the Night Porter's building). Three unlicensed after-hours clubs the Ministry has marked as Resonance-adjacent.

**Resonance note:** The city's most effective natural cover. Large crowds, unusual hours, high noise. A Resonance event can pass as a stage effect. Detection clock ticks slower here for Prowl-based approaches.

---

## The Docks
**Industrial, salt, rust. Biologicals jobs happen here.**

The part of the city that doesn't pretend. Warehouses repurposed six times without anyone tearing them down. Shift workers who don't look up.

**Sensory signature:** Salt, diesel, cold industrial water. Fluorescent lights in spaces with too much ceiling. Cranes that may or may not be running.

**Key locations:** Cold storage facilities (legitimate and otherwise). Drainage tunnels under the eastern pier (Resonance-active — see Urban Legends). Ministry Bio-Containment unit (looks like a refrigeration company).

**Resonance note:** Highest concentration of Biological entities in the city. Apex runs quarterly sweeps. The crew's Cold Storage uses the same refrigeration infrastructure — provides deniability.

---

## The Overhang
**Residential. Where the cover-up is most strained.**

Apartment blocks close enough together to hear your neighbors. Community boards. The kind of neighborhood where unusual things get reported because people have nothing better to do.

**Sensory signature:** Cooking smells, television through thin walls, the stress of a neighborhood watch that takes itself seriously. Children playing games with rules adults haven't heard.

**Key locations:** The playground (see Urban Legends — The Children's Game). Three apartment buildings where Twice-Born have lived quietly for decades. The Overhang Ministry liaison's actual home — he files more reports than any other district officer.

**Resonance note:** Most dangerous district for cover-up failures. Any score that spills into the Overhang immediately ticks Detection once and triggers a witness roll.
```

- [ ] **Step 2: Verify checklist**
  - [ ] Five districts with sensory signatures and Resonance notes
  - [ ] C&C, Emmerich's shop, Merton's theater, and the Docks all placed
  - [ ] Key locations in each district link to existing files or Urban Legends

- [ ] **Step 3: Commit**
```bash
git add "04-Locations/City-Districts.md"
git commit -m "feat: add City Districts overview with sensory profiles and Resonance notes"
```

---

## Task 11: Enhance Curios & Chronicles Location File

**Files:**
- Modify: `04-Locations/Curios-and-Chronicles.md`

- [ ] **Step 1: Replace the file contents with the following enhanced version**

```markdown
---
entity_type: Location
name: "Curios & Chronicles"
district: "Old City"
controlling_faction: "[Faction: Curios & Chronicles]"
claim_status: Crew Claim
threat_level: Safe
---

# Curios & Chronicles

**One-line read** — A narrow, wood-paneled bookstore that feels like a quiet fort. Twenty dollars a day on purpose.

---

## First Entry Read-Aloud (Use on Session 0 or first arrival)

> "The shop is narrow enough that the shelves on either side would brush your shoulders if you reached out both arms. Floor-to-ceiling books, all of them real, all of them organized by a system that appears to be personal. The smell is vanilla and old paper and floor wax and something underneath those, faintly metallic, that you have learned to recognize.
>
> A rotary phone on the counter. A half-knitted sweater on the reading chair that no one is in. A cat on the counter — large, grey, profoundly indifferent. The tag on his collar reads CONSEQUENCE.
>
> There is a door behind the main shelving unit. It is not hidden, exactly. But first-time visitors consistently describe the shop as having no back room."

---

## Room by Room

### The Front Shop
**Purpose:** Cover. Public-facing. Twenty dollars a day.

Thirty feet deep, fifteen feet wide. Every shelf is genuine stock. The till is manual. The phone is functional — Ministry couriers use it first. The sweater on the reading chair has been half-finished for two years.

**Key objects:**
- **The Rotary Phone:** The only publicly-listed number. Sometimes it rings twice at 3am with no one there.
- **Consequence:** The cat. Has never, not once, reacted to any supernatural event in the shop. Not a Resonance spike, not a recovered Anchor, not a contained Biological. The crew considers this reassuring.
- **The Front Window:** Permanently dusty in the way that says "this is intentional."

**Cover protocol:** If a mundane customer enters during an active situation, the crew has approximately ninety seconds. Someone picks up the half-knitted sweater and sits in the reading chair. Someone else helps the customer. Nobody uses the word "basement."

---

### The Back Room (The Post-Op)
**Purpose:** Triage, processing, first-stage harvesting.

Accessed through a rolling bookshelf — the latch is a specific book (*Industrial Chemistry for the Practitioner*, 1962 edition). Quiet enough that a browsing customer nearby would hear the shelf move but not the click.

**Key objects:**
- **The Post-Op Table:** Stainless steel. Medical-grade. Four strap points folded under and out of sight. The crew does not discuss where it came from.
- **The Hunter's Journal:** On a reading stand near the table. Handwritten index organized by entity type. Two generations of entries before the crew's tenure. The handwriting changes at entry 47 without explanation.
- **The Scanner Station:** Green light, always on. Detects Resonance within two blocks. Tinker roll for specific signatures; Survey roll for general detection.
- **The Trophy Wall:** Four polaroids in the back corner. Currently empty.

---

### The Containment Suite (Basement)
**Purpose:** Long-term secure storage. Resonance-dark.

Staircase behind the Post-Op table. Narrow stairs, one bare bulb at the bottom controlled from the top, better overhead fluorescents controlled from the bottom. Smells different from the rest of the shop — colder, with the metallic tang of the vault and the ozone-adjacent smell of the cooling unit.

**Key objects:**

**[Location: Cold Storage Locker]** — A modified refrigeration unit behind a false wall. Convincing enough that a Ministry inspector needs a specific scan to find it. Pauses Biological Spoilage clocks. Four compartments; two require gloves — the insulation is not standard.

**[Location: Lead-Lined Vault]** — Repurposed bank deposit vault, built into the original foundation. Lead lining neutralizes Resonance signatures — nothing inside pings any scanner. Combination known to the full crew. Door takes fifteen seconds to open fully.

**What new crew members are told on day one:** "The Cold Storage pauses the spoilage clock — anything biological goes in there immediately, not tomorrow. The vault is lead-lined; nothing inside pings a scanner. Do not leave Relics in the Post-Op or the front shop. Resonance bleeds. The neighbors don't report gas leaks, but they do talk."

---

## Mechanical Benefits

| Benefit | Effect |
|---|---|
| Hardened Heart | Reduced Heat from supernatural messes |
| Crafting Bonus | +1 Tier for crafting and preserving Quality items |
| Cold Storage | Pauses [Clock: Biological Spoilage] for stored items |
| Lead-Lined Vault | Items stored here emit no Resonance signatures |
| Scanner Station | Detects Resonance within 2 blocks |
```

- [ ] **Step 2: Verify checklist**
  - [ ] First Entry Read-Aloud exists
  - [ ] All three areas have room-by-room descriptions
  - [ ] All key objects named, described, with function
  - [ ] "What crew members are told on day one" documented

- [ ] **Step 3: Commit**
```bash
git add "04-Locations/Curios-and-Chronicles.md"
git commit -m "enhance: add full room-by-room descriptions to Curios & Chronicles"
```

---

## Task 12: Enhance Subway Stations File

**Files:**
- Modify: `04-Locations/The-Subway/Stations.md`

- [ ] **Step 1: Replace the file contents with the following enhanced version**

```markdown
---
type: location
status: canon
---

# Subway — Stations & Spaces

Treat each station as a room. Players can explore them. Things happen in them. Add details as visited — this file grows with the campaign.

---

## First Descent Read-Aloud (Use in Session 2)

> "The stairs go down further than they should. The green-painted iron railing is cold and real under your hand. Below: a vaulted hall lit in greenish light, the source of which you cannot locate.
>
> The smell hits first: damp concrete and something underneath it that isn't quite food. Then the sound — distant, like wind through tunnels, with no source you can identify.
>
> There are people here. Some of them aren't. A figure in a business suit reads a newspaper without looking up. Nobody looks at you directly. This is a place with etiquette you do not yet know."

---

## The Main Hall

Entry point. A transit map on the north wall — the lines don't match any city map you've seen. One line is marked in red ink that looks newer than the rest. Foot traffic that is inconsistent with any logic you can apply to where these people came from.

**Mechanical note:** Social interactions here are Consort or Sway. Crew reputation flows from what's observed in this room.

---

## The Fence's Stall

Three steps down from the Main Hall, behind a partition that has become part of the architecture.

**Sensory details:** The smell of old money and something preserved. Items on display that you should not touch until you've established that you're buying.

**What the Fence does:** Buys Biologicals and Relics at market rate. Siphoned goods at half price, no questions asked. Asks nothing. Remembers everything.

**Dialogue voice:** Economical. "That'll move." "That won't."

---

## The Whisperer's Booth

A booth that is not consistently in the same location between visits.

**What the Whisperer offers:** Ministry personnel movements, Apex Aegis acquisition lists, which bounties are manufactured, Subway community intelligence.

**Price:** Trades information for information. Bring something new.

**Dialogue voice:** Measured. Makes eye contact exactly as long as necessary. "Is that a question or are you telling me you don't know yet?"

---

## The Workshop

Machine oil and something older. Tools on the walls in a system that is clearly intentional and completely opaque.

**What happens here:** Craft Downtime activity at +1 Tier. A specialist who understands Anchor Items without destroying them — will tell you whose it is and ask what you intend to do.

---

## The Job Board

A wall. Cork. Pins. Notes. Some are bait. One near the bottom left has been there so long the writing is illegible. Nobody removes it.

**Mechanical note:** Subway board leads generate different faction consequences than Ministry bounties. Completing them earns Twice-Born favor.

---

## The Back Booth — The Crossroads Broker

Too far back for the physical dimensions of the space. One occupant. Gray suit. Narrow tie. 1987.

He looks up when someone approaches. He has been expecting this specific person.

**What he offers:** What you want — the thing you actually want, not what you asked for. Price: a Memory, a Relationship, or a Future Favor. He specifies. He is not unreasonable.

**Dialogue voice:** Unhurried. "Sit down. I know why you're here. I usually do."

**Mechanical note:** Track all outstanding debts in `07-Clocks/Active-Clocks.md` under the Crossroads Cost Ledger.

---

## PTOLEMY's Corner

PTOLEMY does not have a stall. PTOLEMY has a corner. Old leather luggage. Brass clasps. No visible eyes. The clasps move in patterns that translate — somehow — into meaning.

**First introduction read-aloud:**
> "In the corner: a piece of luggage. Brass clasps, cracked leather, no visible eyes. The clasps are moving — not vibrating, but moving with intention. It is listening to you. It has been listening since before you came down the stairs."

**The Ledger:** Always accurate. Always coming due. What it is ultimately tracking is GM-private.
```

- [ ] **Step 2: Verify checklist**
  - [ ] First Descent Read-Aloud exists for Session 2
  - [ ] Every station has sensory details and what happens there
  - [ ] Dialogue voice for interactive NPCs
  - [ ] Mechanical notes for stations with mechanics

- [ ] **Step 3: Commit**
```bash
git add "04-Locations/The-Subway/Stations.md"
git commit -m "enhance: add full sensory profiles and read-alouds to Subway Stations"
```

---

## Task 13: Create Score File — Session 1 (Merton)

**Files:**
- Create: `06-Scores/Score-01-Merton.md`

- [ ] **Step 1: Create the file with the following content**

```markdown
---
entity_type: Score
score_number: 1
title: "The Standard Job"
session: 1
status: Ready
client: "[Faction: The Ministry]"
target: "[NPC: Merton] (Barghest)"
location: "Fairground District — Local Theater Basement"
payout: 4 Coin (Standard)
---

# Score 01 — The Standard Job

**Premise:** Ministry pest control. A politician's dog has two human hands where its front paws should be. Retrieve, document, destroy. The crew knows a Barghest Adrenal Gland fetches serious money.

---

## The Three Layers — Merton

**Layer 1:** Night security at the theater for eleven years. Locker 7, basement. Contains a pressed work shirt, a thermos, a keychain photograph behind yellowed plastic. A woman and two children. Someone made it for him who knew exactly what he wanted to hold onto.

**Layer 2 — Barghest.** Summoned in 1823 without consent. Capacities: physical armor, enhanced senses, partial transformation under stress. **Holy Weakness:** Critical on Study or Gather Info reveals severing the Leather Dog Collar removes his armor and reduces Threat Level to zero.

**Layer 3:** Summoned without consent in 1823. The family in the photograph has been dead for 150 years. He keeps the photograph because putting it away would mean he has stopped having someone to hold onto.

---

## The Anchor Item

**[Item: Leather Dog Collar]** — 1823. Worn leather. Smells older than it should.
- **Seizure fallout:** He knows immediately. Goes still. Will not attack. Will wait.
- **Destruction consequence:** Loses armor and control. 1d6 hours before transformation is irreversible. He does not want this.

---

## Approaches

**Option A — Professional cleanup (front door):** Position Risky / Effect Standard. Complication: Janitor comes down for coffee at 11pm. Always.

**Option B — After-hours break-in (alley):** Position Controlled / Effect Standard (Prowl). Complication: Apex Aegis van parked adjacent, watching an unrelated target.

**Option C — Talk to Merton first:** Position Risky / Effect Limited. Complication: He may mistake a PC for someone from the photograph. He will not say who. He will go very still.

---

## Antagonist Angles

**Apex Aegis:** Van is surveillance for an unrelated target. If Detection hits 3+, an operative approaches the theater entrance.

**Elias Thorne:** Appears before or after the score. Plant Tell 1 here (uses a PC's first name before introductions). Plant Tell 2 here (mentions "your setup in the basement").

---

## Wrap-Up Dilemma

**Play it Safe:** Hand everything to Ministry/Apex. 4 Coin, 0 Heat. Collar destroyed. Photograph disappears into evidence.

**Double Bookkeeping:** Roll Sway to omit the Adrenal Gland from paperwork. Keep the Gland. Tick [Clock: The Ministry Audit] on 4-5.

**Shadow Ghost:** Take Collar and Gland without filing. +2 Heat. Ministry notices within 48 hours.

**The Fourth Option** (if crew found his tragedy): Return the collar. No payout. No credit. Merton walks. Log as "Returned" in Anchor Ledger. The Twice-Born community will hear.

---

## AI Session Directives

**Sensory palette:** Stale popcorn on cold air. Flickering work light in the basement. The sound of his breathing before you see him. Collar leather that smells older than it should.

**Pacing rule:** Do not rush to confrontation. Let the players find the locker. Let them find the photograph. The tragedy lands before the action starts.

**Tutorial priority:** First score. State Position and Effect out loud for every roll. Offer a Flashback in the first hour. Give the Devil's Bargain menu before any roll with a complication available.

**Merton's voice:** "You came for the collar." Not a question. He is not performing menace. He is a very tired person who has been asked to perform menace for two hundred years.
```

- [ ] **Step 2: Verify checklist**
  - [ ] All three layers present with specific detail
  - [ ] Anchor Item seizure and destruction consequences documented
  - [ ] Elias Thorne tell-planting instructions present
  - [ ] Wrap-up covers all four options including the return

- [ ] **Step 3: Commit**
```bash
git add "06-Scores/Score-01-Merton.md"
git commit -m "feat: add Score-01-Merton full score file for Session 1"
```

---

## Task 14: Create Score File — Session 2 (Emmerich)

**Files:**
- Create: `06-Scores/Score-02-Emmerich.md`

- [ ] **Step 1: Create the file with the following content**

```markdown
---
entity_type: Score
score_number: 2
title: "The Hollow Pedestrian"
session: 2
status: Ready
client: "Anonymous (Subway Posting)"
target: "[NPC: Emmerich] — Silver Thimble seizure or refusal"
location: "The Meridian — EMMERICH & DAUGHTER, BESPOKE TAILOR"
payout: 6 Ethereal Credits or 4 Coin + Twice-Born Favor
---

# Score 02 — The Hollow Pedestrian

**Premise:** Anonymous Subway board posting. Someone wants the Silver Thimble secured — or Emmerich protected from Ministry seizure. The Ministry also has this on their docket. The crew is caught between two clients for the same target.

---

## The Three Layers — Emmerich

*Full NPC file: `03-NPCs/Active/Emmerich.md`*

**Layer 1:** Bespoke tailor. Second-floor shop. Has been here longer than anyone knows to ask about. The sign says "and Daughter." The daughter is not here.

**Layer 2 — Twice-Born, old-kind.** Perceives Resonance as texture. Cannot be deceived about a person's true nature if he touches something they've made.

**Layer 3:** His daughter died in 1847. The thimble was hers. Taking it ends him in 1d6 hours. He has been holding on for 179 years.

---

## The Anchor Item

**[Item: Silver Thimble]** — 1847. Small. Warm. Warmer than it should be.
- **Seizure fallout:** He knows immediately. Sits down where he is. Does not flee. Does not fight.
- **Destruction consequence:** Immediate unraveling. Shop paperwork goes blank. Photos of the interior from the past fifty years show an empty room.

---

## Approaches

**Option A — Wait for him to leave:** Position Risky / Effect Standard. Complication: Client appointment at 2pm. She will wait in the shop. She has been coming here for thirty years. She will notice.

**Option B — Ministry pretense:** Position Controlled / Effect Limited. Complication: Emmerich recognizes the pretense immediately. He does not expose it. He says: "How long do I have?" This is not a failure — it is the scene.

**Option C — Approach as buyers:** Position Risky / Effect Limited. Complication: He touches whatever the speaker is wearing. He knows exactly what they are. His face does not change.

---

## The Moral Choice

**Seize the thimble:** 4 Coin. Emmerich unravels in 1d6 hours. Twice-Born: −1. The thimble goes cold within the hour.

**Warn and walk:** 0 Coin. "Thank you." +1 Twice-Born Favor. Ministry flags C&C non-compliant within 48 hours.

**Partial complicity:** 2 Coin. "How long do I have." 0 standing change with either faction.

---

## Antagonist Angles

**Apex Aegis:** Compliance audit ping if the crew is sloppy in the Meridian. Two plainclothes operatives with clipboards. "Unlicensed extraction detected."

**Elias Thorne:** Appears to "run interference" on the audit. Plant Tell 3 here (pauses outside Emmerich's shop). Plant Tell 4 here (references "last Tuesday's conversation").

---

## The Subway Reveal

This score ends with the crew's first Subway access. See `04-Locations/The-Subway/Overview.md` for the entrance read-aloud and `04-Locations/The-Subway/Stations.md` for the first-descent read-aloud.

The trigger for access is GM-private — something the crew did in this score that the Subway perceived as qualifying. It is not about success or failure.

**PTOLEMY's first interaction:** Have PTOLEMY's clasps click specifically at one PC. Do not explain why.

---

## AI Session Directives

**Sensory palette:** Climate-controlled Meridian air against the shop's warmth. The smell of sizing and thread. The thimble, warm in the hand.

**Pacing rule:** Run the observation scene long enough that the crew sees Emmerich with the child and with the woman before any approach. The tragedy lands before the snatch.

**Moral weight monitor:** If the crew takes the thimble, describe it cooling in their hand within the first five minutes. Write the Anchor Ledger entry while they can still feel it.

**Teach group actions here:** If the crew coordinates, run it as a Group Action. Leader rolls; highest die covers the group; leader takes Stress for mixed results.
```

- [ ] **Step 2: Verify checklist**
  - [ ] All three approaches with Position/Effect
  - [ ] All three moral choices with faction consequences
  - [ ] Elias Thorne tells 3 and 4 flagged
  - [ ] Subway reveal linked to correct location files

- [ ] **Step 3: Commit**
```bash
git add "06-Scores/Score-02-Emmerich.md"
git commit -m "feat: add Score-02-Emmerich full score file for Session 2"
```

---

## Task 15: Seed Foreshadowing Log

**Files:**
- Modify: `09-Threads/Foreshadowing.md`

- [ ] **Step 1: Replace the `## Active Plants` section with the following**

```markdown
## Active Plants

### Plant 1 — Thorne Knows the Name (Session 1)
* **Seed:** Thorne greets the crew and uses one PC's first name before formal introductions. He moves past it without correction.
* **Planted:** Session 1 (Opening scene)
* **Target Payoff:** Mimic reveal — "How did he know your name before you told him?"
* **Status:** Dormant

### Plant 2 — The Basement He Shouldn't Know (Session 1)
* **Seed:** Thorne refers to "your setup in the basement" when discussing the Containment Suite. No Ministry liaison would know a licensed firm's private lair without a formal inspection on record.
* **Planted:** Session 1 (Post-score debrief)
* **Target Payoff:** Mimic reveal — confirmation Thorne has been inside the shop without the crew's knowledge.
* **Status:** Dormant

### Plant 3 — The Pause Outside Emmerich's Shop (Session 2)
* **Seed:** Walking past Emmerich's shop pre-score, Thorne pauses a half-second too long before looking away. He says he "heard it was a good shop." He has no Meridian connections in his cover story.
* **Planted:** Session 2 (Pre-score approach)
* **Target Payoff:** Mimic reveal — the Understudied has been watching Emmerich for years. Thorne recognized him.
* **Status:** Dormant

### Plant 4 — Tuesday's Conversation (Session 2)
* **Seed:** In follow-up conversation after the Emmerich score, Thorne references "last Tuesday's conversation" — a conversation that did not happen on Tuesday and that the crew remembers differently.
* **Planted:** Session 2 (Post-score follow-up)
* **Target Payoff:** Mimic reveal — memory bleed. It reached for Thorne's memories and found a gap.
* **Status:** Dormant

### Plant 5 — The Ring (Ongoing)
* **Seed:** Thorne wears a plain silver band, right hand, slightly too loose. Touches it when uncertain. It belongs to a face he wore before this one.
* **Planted:** Session 1 (available throughout)
* **Target Payoff:** Mimic reveal — when confronted, he reaches for the ring and it isn't where it should be. He reaches for a different comfort gesture and finds nothing.
* **Status:** Dormant
```

- [ ] **Step 2: Verify checklist**
  - [ ] Five plants seeded for Elias Thorne / Mimic reveal
  - [ ] Each has session placement, payoff target, and status
  - [ ] Plants are subtle enough to survive a first read without triggering suspicion

- [ ] **Step 3: Commit**
```bash
git add "09-Threads/Foreshadowing.md"
git commit -m "feat: seed five Mimic tells into Foreshadowing log (Elias Thorne arc)"
```

---

## Task 16: Populate Urban Legends Generator

**Files:**
- Modify: `10-Generators/Urban-Legends.md`

- [ ] **Step 1: Replace the file contents with the populated version**

```markdown
---
entity_type: Generator
name: "Urban Legends"
purpose: "Rumor pool for The Ritual downtime activity and GM improvisation."
---

# Urban Legends — Job Lead Pool

## AI Generation Protocol for Leads
1. **The Cover:** The mundane explanation the public accepts.
2. **The Truth:** The supernatural reality underneath.
3. **The Tell:** A detail that doesn't fit the cover story.
4. **Urgency:** When this becomes an Omen symptom or generates a clock if ignored.

---

## Active Leads

### 1 — The Glass Building Incident
* **Cover:** Structural settlement in a Meridian apartment block. Residents report "reflective distortion."
* **Truth:** A Twice-Born was evicted during renovation and their Anchor Item was accidentally destroyed by a contractor. The building stands but every mirror shows a different floor than the one you're on.
* **Tell:** The structural engineer's report shows no damage. The contractor who handled the renovation quit the same week and has not worked since.
* **Urgency:** Left unresolved past Session 4, tick [Clock: The Omen] by 1. The mirrors are getting worse.

### 2 — The Fisherman's Report
* **Cover:** Bioluminescent algae in the drainage tunnels under the eastern Docks pier. Environmental report filed; low priority.
* **Truth:** A Biological entity — classification unknown, large — is nesting in the drainage system. The algae is a Resonance byproduct of its resting state.
* **Tell:** The algae only glows when the tide goes out *and* someone is watching. Monitoring cameras see nothing. Environmental officers have noted this and filed it as a calibration issue.
* **Urgency:** If unresolved by Session 3, a Nesting clock (4-seg) begins. At full: too large to extract without a major exposure event.

### 3 — The Children's Game
* **Cover:** Playground urban legend spreading through the Overhang. Kids playing a "pretend" game with unusual rules.
* **Truth:** Three children have been playing the same game since September with rules none of them can explain. The game involves an object — small, dark, "heavy for its size" — that no parent has seen.
* **Tell:** The children won't play when adults are watching. The game always ends at the same time, to the minute, regardless of when it started.
* **Urgency:** The object is a Relic. Left unresolved past Session 5, one child begins to exhibit Resonance sensitivity.

### 4 — The Radio Signal
* **Cover:** Pirate radio. FCC notified. Investigation pending.
* **Truth:** The AM Host broadcasts are Aldric Voss (see `03-NPCs/Twice-Born/Aldric-Voss.md`), tracking Resonance events through radio interference for sixty years. Recent fragment: *"It found the frequency. Don't use the frequency."*
* **Tell:** The signal broadcasts on three AM channels simultaneously. This is technically impossible with standard equipment.
* **Urgency:** Connected to [Clock: The Omen]. When the Omen hits 4 segments, Aldric's broadcasts stop. Either he went underground or was silenced.

### 5 — The Empty Apartment
* **Cover:** Gas leak in a third-floor Overhang apartment. Condemned six weeks ago.
* **Truth:** A Twice-Born was reported to the Ministry by a neighbor. Ministry sent cleaners. The Anchor Item — a small lacquered box, 1920s — was overlooked. Still in the apartment. Broadcasting a Resonance distress signal.
* **Tell:** The gas company has no record of the leak. The neighbor who filed the report has moved out. A different neighbor is still leaving food at the door twice a week.
* **Urgency:** Resonance signal is pinging Apex scanners. Apex has a team scheduled to investigate in three weeks.

### 6 — The Dog Problem
* **Cover:** Feral dog pack loose in Old City. Animal control called three times.
* **Truth:** The pack follows a specific route twice daily without deviation, tracing a Resonance ley line that wasn't there eight months ago. Someone drew it.
* **Tell:** The dogs stop at the same corner and look up at the same fourth-floor window for exactly ninety seconds before moving on. The apartment has been empty for four years.
* **Urgency:** [Clock: The Omen] symptom. If the Omen hits 3 segments, the route changes — the dogs are now running it.

### 7 — The Night Porter
* **Cover:** The Fairground Hotel has had the same night porter for decades. Local color. Used in their marketing.
* **Truth:** He has been working there for ninety years. Anchor: the hotel's original master key, 1934. He cannot go more than four blocks from the building. He has been trying to leave for thirty years.
* **Tell:** Staff photos going back to the 1970s show the same man. Nobody on current staff has asked why. His employee file lists a hire date of 1971 in handwriting different from every other entry in the book.
* **Urgency:** Apex Aegis is reviewing the hotel's employment records. Timeline: six weeks.

### 8 — The Tailor's Referral
* **Cover:** A Subway job board posting. Someone looking for a specific piece of bespoke clothing, sixty years old, made by Emmerich's shop.
* **Truth:** The clothing contains a fragment of someone else's Anchor woven in during construction — a favor Emmerich did for someone who needed protection hidden. The person asking for it now is not the person who commissioned it.
* **Tell:** The posting uses a name for the requester that belongs to someone who died in 1962. The handwriting is slightly too neat.
* **Urgency:** The Mimic planted this posting. If retrieved by the wrong party, the hidden Anchor fragment goes dark.

### 9 — The Archive Fire
* **Cover:** Routine records fire in the Old City municipal archive. Bad wiring. Insurance claim filed.
* **Truth:** Someone with access and intent destroyed thirty years of Ministry Resonance incident reports (1940–1970) in a single night. Senna Calder has copies (see `03-NPCs/Twice-Born/Senna-Calder.md`).
* **Tell:** The wiring passed inspection two weeks before the fire. The suppression system activated — the sprinklers produced no water. The investigator's report was amended twice and then sealed.
* **Urgency:** If the crew finds Senna before the Mimic learns she has the copies, they gain thirty years of context. If the Mimic learns first, Senna becomes a target.

### 10 — The Meridian Complaint
* **Cover:** Tenant noise complaint. Eight residents of a Meridian apartment block report intermittent low-frequency sound. Building management says it's HVAC.
* **Truth:** A newly-manifested Twice-Born moved in three months ago. They don't know what they are. Their Anchor — a music box inherited from a grandparent — is unstable and broadcasting Resonance affecting every Twice-Born within three blocks.
* **Tell:** Eight tenants filed noise complaints. None can agree on what the noise sounds like. One says music. One says breathing. One says it is her mother's voice, and her mother has been dead for twelve years.
* **Urgency:** An Apex scan vehicle has parked on the block twice this week. They are close to triangulating.

---

## The AM Host — Fragments (Broadcast Pool)
*(Draw one per session when Resonance is active as ambient texture.)*

* "Something patient is waiting under the city. I don't know what it's waiting for. I think it does."
* "The clocks are running slow for a reason, people. Check your watch against your phone. Check again in an hour."
* "It found the frequency. Don't use the frequency."
* "Three cities. Same drawing. Same face. No eyes. Draw your own conclusions."
* "The dogs know. The dogs have always known. Ask the dogs."
* "If you're listening to this, you already know something's wrong. That's why you found this station."

---

## AI Facilitation Directives
* **Weird Clusters:** If the crew investigates three incidents in the same district, inform the GM a Nesting event is occurring. Suggest a 4-segment clock.
* **Omen Integration:** Urgency notes connect to [Clock: The Omen]. Track which leads have been ignored when the clock advances.
* **Lead Refresh:** After every score, suggest one new lead based on current Faction Standings.
```

- [ ] **Step 2: Verify checklist**
  - [ ] 10 leads populated with Cover/Truth/Tell/Urgency
  - [ ] Leads connect to existing NPCs and factions
  - [ ] AM Host fragment pool has 6 usable lines
  - [ ] Lead #8 (Tailor's Referral) noted as Mimic-planted

- [ ] **Step 3: Commit**
```bash
git add "10-Generators/Urban-Legends.md"
git commit -m "feat: populate Urban Legends with 10 full leads and AM Host fragment pool"
```

---

## Task 17: Build Public Wiki Structure

**Files:**
- Create: `Public-Wiki/` (directory)
- Create: `Public-Wiki/_Session-Recap-Template.md`
- Create: `Public-Wiki/00-Who-We-Are.md`

- [ ] **Step 1: Create the directory**

```bash
mkdir -p "/Users/delonsampaio/Desktop/VSCode Workspaces/The-Shadow-Exchange/Public-Wiki/Session-Recaps"
```

- [ ] **Step 2: Create `Public-Wiki/_Session-Recap-Template.md`**

```markdown
---
type: public-wiki
session_number: NN
title: "[Session title]"
date_played: YYYY-MM-DD
status: Published
---

# Session NN — [Title]

*What the crew experienced. No GM-private information. Written from the crew's perspective.*

---

## What Happened

[2–4 paragraphs. Narrative summary of the session from the crew's point of view. Events, choices, key moments. No mechanical language — write it like a story beat.] 

---

## Choices Made

*The decisions that will matter later.*

- [Decision 1 and brief outcome]
- [Decision 2 and brief outcome]

---

## Mechanical Outcomes

| Item | Result |
|---|---|
| Coin earned | +X (total: X) |
| Heat | +X (total: X) |
| Rep | +X (total: X) |
| Clocks advanced | [Clock name] → X/Y |
| Anchor transactions | [Item] — [what happened] |

---

## Open Questions

*Things the crew is aware of and wondering about. No answers here.*

- [Question 1]
- [Question 2]

---

## Who You Met

*Brief, player-facing summaries of NPCs encountered this session. No hidden information.*

- **[NPC Name]** — [one sentence description of who they are from the crew's perspective]
```

- [ ] **Step 3: Create `Public-Wiki/00-Who-We-Are.md`**

```markdown
---
type: public-wiki
purpose: "Player-facing overview of the crew, the lair, and the world — updated before Session 0"
last_updated: 2026-05-10
---

# Who We Are — Curios & Chronicles

*What your characters know before the first session. Read this before Session 0.*

---

## The Firm

**Curios & Chronicles** is a licensed monster-hunting firm operating out of Old City. The front is a real bookstore. It takes in twenty dollars a day on purpose — that's the cover.

You have been doing this work together for two years. You are good at it in the way that people who do hard, quiet work for years are good at it. Not action-movie good. *Competent and tired* good.

---

## The Lair

The bookstore has three layers. Your characters know all of them.

### The Front Shop
A real bookstore with a rotary phone, a half-knitted sweater on the reading chair, and a cat named **Consequence** who has never once reacted to anything unusual and who you have all decided to find reassuring. The till is manual. The books are organized by a system only the crew understands. This is where you deal with the public.

### The Back Room
Behind a rolling bookshelf (the latch is a specific book your characters know by heart). Contains:
- **The Post-Op Table** — stainless steel, medical-grade, don't ask where it came from
- **The Hunter's Journal** — the firm's case record, two generations of entries before yours
- **The Scanner Station** — detects Resonance activity within two blocks, green light always on

### The Containment Suite (Basement)
Down a narrow staircase behind the Post-Op table. This is where the serious work happens.
- **Cold Storage Locker** — behind a false wall. Keeps biological material from spoiling. Two of the four compartments require gloves.
- **Lead-Lined Vault** — built into the original foundation. Nothing stored here shows up on any scanner.

The basement smells different from the rest of the shop. Colder. Metallic. You have learned not to comment on it.

---

## The Work

Your firm is licensed by **The Ministry** — a government body that maintains the cover-up. They send you jobs via manila envelope. Standard pay is minimal. They expect compliance. You've learned to be creative about compliance.

The supernatural is real. The public doesn't know. **Your job is to handle supernatural events and keep the public believing it isn't real.** Exposure — video, witnesses, anything that reaches the press — ends your license and potentially your freedom. A witness with a phone is scarier than a wound.

Some of what you handle are dangerous biological anomalies. Some are more complicated than that. Some of the things you've been contracted to destroy are people who have found a way to live quietly in a world that doesn't know they exist. The firm keeps an **Anchor Ledger** — a record of every case and every choice made. You made that decision together, year one.

---

## The Factions

**The Ministry (Tier V):** Your license-holder. Bureaucratic, efficient, and not as in control as they believe. They think they are protecting people. They are not wrong about the goal.

**Apex Aegis (Tier IV):** A private firm that treats the supernatural as a mining resource. They have better equipment than you and worse ethics. If they make a move on your firm, you will know about it.

**The Twice-Born:** People — for lack of a better word — who have found a way to exist in both the human world and something older. They are not a faction you work against. They are complicated.

**The Subway:** You don't know about this yet. You will.

---

## What You Don't Know Yet

There is more going on than The Ministry is telling you. There always is.

One of the contacts you'll meet in your first session is not who they appear to be.

The firm's first two jobs were chosen for reasons that aren't in the paperwork.

---

## House Rules & Reminders

- When the AI Co-GM says "What does the crew do?" — that's your cue. Make a decision as a group or individually and tell them.
- You can call a **Flashback** at any time to establish something your character prepared before the scene. It costs Stress. Ask about it if you're not sure how.
- The rules will be explained as they come up. You don't need to know them in advance. You need to know your character and make decisions that feel right.
```

- [ ] **Step 4: Update `00-Canon/Player-Reference.md` — add Your Lair section**

After the last line of the file (`...industrial-occult noir. Quiet dread...`), append:

```markdown

---

## Your Lair — Curios & Chronicles

Your characters know this space before Session 0. See `Public-Wiki/00-Who-We-Are.md` for the full player-facing version.

**The Front Shop:** The public bookstore. Rotary phone, reading chair, cat named Consequence. Real books, real cover.

**The Back Room:** Behind a rolling shelf. Post-Op Table, Hunter's Journal, Scanner Station (Resonance detection, two-block radius, always on).

**The Containment Suite (Basement):** Cold Storage Locker (pauses biological spoilage), Lead-Lined Vault (Resonance-dark storage). The combination is known to the full crew.

Your characters have worked here for two years. Ask the GM about any object in the shop — you would know what it does.
```

- [ ] **Step 5: Verify checklist**
  - [ ] `Public-Wiki/Session-Recaps/` directory created
  - [ ] Session Recap template has both narrative and mechanical sections
  - [ ] Template explicitly says "no GM-private information"
  - [ ] `00-Who-We-Are.md` covers lair room-by-room from player perspective
  - [ ] `00-Who-We-Are.md` covers factions, the work, and what players don't know yet
  - [ ] Player-Reference.md has lair summary added

- [ ] **Step 6: Commit**
```bash
git add "Public-Wiki/" "00-Canon/Player-Reference.md"
git commit -m "feat: build Public Wiki structure with session recap template and pre-session-0 player primer"
```

---

## Task 18: Build Visuals System

**Files:**
- Create: `11-Visuals/` (directory)
- Create: `11-Visuals/Pre-Campaign-Image-Prompts.md`
- Create: `11-Visuals/Session-Image-Log.md`
- Create: `11-Visuals/_Saved-Images/` (directory — GM drops generated images here)
- Append: Protocol 13 to `Co-GM-Prompts.md`

- [ ] **Step 1: Create the directory structure**

```bash
mkdir -p "/Users/delonsampaio/Desktop/VSCode Workspaces/The-Shadow-Exchange/11-Visuals/_Saved-Images"
```

- [ ] **Step 2: Create `11-Visuals/Pre-Campaign-Image-Prompts.md`**

```markdown
---
entity_type: Generator
name: "Pre-Campaign Image Prompts"
purpose: "Ready-to-paste prompts for Gemini image generation. Generate before Session 0 for player handouts and GM reference."
image_style: "Industrial-occult noir — cinematic, amber and cold blue, film grain, quiet unease"
---

# Pre-Campaign Image Prompts

Generate these before Session 0. Save outputs to `11-Visuals/_Saved-Images/`.

---

## Master Style Suffix

**Append this to the end of every prompt for visual consistency:**

> *Industrial-occult noir. Cinematic lighting, amber and cold blue tones, rain-slicked surfaces, dim reflections. Photorealistic, moody, detailed. Quiet unease — not horror. Modern city with century-old bones. Film grain texture. No text, no watermarks.*

---

## Locations

### Curios & Chronicles — Exterior
> A narrow bookstore squeezed between two glass-and-steel skyscrapers on a rain-soaked city street at night. Sign reads "Curios & Chronicles" in faded lettering. Warm amber light through dusty windows. A cat visible on the counter inside. The building looks like it decided not to update itself and has been winning that argument for a hundred years. [STYLE SUFFIX]

**Saved image:** `_Saved-Images/location-curios-exterior.png`

### Curios & Chronicles — Containment Suite
> A cold basement beneath a bookstore. Harsh overhead fluorescents. A stainless steel medical table with folded strap points. A large old vault door built into the original stone foundation. A modified refrigeration unit behind a partially-open false wall. Completely organized, completely unsettling. [STYLE SUFFIX]

**Saved image:** `_Saved-Images/location-containment-suite.png`

### The Subway — Main Hall
> An underground train station that doesn't match any map, lit in greenish fluorescent light. A transit map on the wall with one line marked in red ink. Figures in business suits moving alongside people who are almost people. Nobody looking at anyone directly. Wondrous and uneasy, not threatening. [STYLE SUFFIX]

**Saved image:** `_Saved-Images/location-subway-main-hall.png`

### The Meridian — Emmerich's Shop
> A quiet second-floor tailor shop at night, seen from the street below. A sign in gold leaf reads "Emmerich & Daughter, Bespoke Tailor." Warm amber light in the window. A figure barely visible inside, bent over a worktable. The "and Daughter" in the sign has been there long enough that the paint is a different age than the rest. [STYLE SUFFIX]

**Saved image:** `_Saved-Images/location-emmerichs-shop.png`

### Fairground District — Theater Exterior
> An old theater marquee on a rain-soaked street at night. The Fairground Grand. Neon reflections on wet pavement. A side door propped open with a brick. One fluorescent light visible through a basement window below street level. The kind of building that has more going on below ground than above it. [STYLE SUFFIX]

**Saved image:** `_Saved-Images/location-fairground-theater.png`

---

## NPCs

### Merton — Human Form
> An older man in a pressed security uniform sitting alone in a theater basement break room, hunched over a thermos of coffee. Hands too still — he has held that position for hours. A keychain with a faded photograph hangs from his belt. The fluorescent light above flickers. His eyes catch the light wrong. [STYLE SUFFIX]

**Saved image:** `_Saved-Images/npc-merton-human.png`

### Merton — True Form (Barghest)
> A figure in a security uniform that is partially something else — taller than it should be, wrong in the places that matter. Standing very still in a theater basement, looking at an old leather dog collar in its hand as though seeing it for the first time. Not threatening — exhausted. Something that has been fighting what it is for two hundred years. [STYLE SUFFIX]

**Saved image:** `_Saved-Images/npc-merton-true-form.png`

### Emmerich
> An elderly tailor working alone in a second-floor shop at night, measuring fabric with practiced hands that never shake. A silver thimble on the worktable beside him. The posture of someone who has been doing the same thing for a very long time and has not decided to stop. Amber lamplight, rain-streaked window behind him. [STYLE SUFFIX]

**Saved image:** `_Saved-Images/npc-emmerich.png`

### Elias Thorne (Ministry Liaison / Mimic Face)
> A trim man in a charcoal field coat standing on a rain-slicked city street at night, looking slightly too warm and invested for someone standing in the rain. Perfect posture. A plain silver ring on his right hand, slightly too loose. His expression is open and earnest in a way that is difficult to explain why it makes you uncomfortable. [STYLE SUFFIX]

**Saved image:** `_Saved-Images/npc-elias-thorne.png`

### PTOLEMY
> Old leather luggage sitting in the corner of an underground station, lit by greenish fluorescent light. The brass clasps are arranged in deliberate patterns — not vibrating, but moving with intention. No face, no eyes, but undeniably aware. Other figures move past it without looking. Something ancient pretending to be ordinary. [STYLE SUFFIX]

**Saved image:** `_Saved-Images/npc-ptolemy.png`

### Mara Halliday (The Innocent)
> A young woman in a worn canvas jacket pausing at a street corner at night, looking at something the viewer cannot see. A bag over one shoulder, a small notebook in her hand. The expression of someone who has just noticed a pattern that doesn't fit, and hasn't decided what to do about it yet. Rain-slicked pavement, amber streetlights. [STYLE SUFFIX]

**Saved image:** `_Saved-Images/npc-mara-halliday.png`

### Aldric Voss (Twice-Born — The Technician)
> An older man in a well-worn corduroy jacket sitting in a radio station control room that looks like it hasn't been updated since the 1970s. Listening to something through headphones. Reel-to-reel equipment behind him. His expression is the expression of someone who has been listening to the same warning for sixty years. [STYLE SUFFIX]

**Saved image:** `_Saved-Images/npc-aldric-voss.png`

### Senna Calder (Twice-Born — The Librarian)
> An older woman in a cardigan repaired in several places, surrounded by filing boxes in a dimly lit underground archive. Reading glasses she doesn't seem to need for vision. She is cross-referencing two documents simultaneously with the ease of someone who has done this ten thousand times. [STYLE SUFFIX]

**Saved image:** `_Saved-Images/npc-senna-calder.png`

### Cosma Linden (Twice-Born — The Teacher)
> An older woman in a coat with too many pockets sitting at a table in a corner of the Subway, speaking to someone across from her with patient, careful attention. Her hands move while she speaks, arranging something invisible. The posture of someone who has explained very frightening things to very frightened people for a very long time. [STYLE SUFFIX]

**Saved image:** `_Saved-Images/npc-cosma-linden.png`

### The Crossroads Broker
> A man in a gray suit and narrow tie sitting alone in a back booth of an underground hall, dressed for a 1987 business meeting. A drink in front of him he has not touched. He is looking up at someone approaching — he has been expecting this specific person. His expression is the expression of someone who knows how this conversation ends. [STYLE SUFFIX]

**Saved image:** `_Saved-Images/npc-crossroads-broker.png`

---

## Anchor Items & Relics

### The Leather Dog Collar (Merton's Anchor)
> An old leather dog collar on a dark surface, lit dramatically from one side. The leather is wrong — too old to have survived this long, but intact. The kind of object that looks ordinary until you look at it too long. Close-up, single light source, deep shadow. [STYLE SUFFIX]

**Saved image:** `_Saved-Images/item-leather-collar.png`

### The Silver Thimble (Emmerich's Anchor)
> A small silver thimble on a worn wooden worktable, lit by a single amber lamp. Old but perfectly maintained. Simple and specific — the kind of object that belongs to one particular person who is no longer here. The feeling, even from a photograph, that it is warmer than it should be. Close-up photography with weight. [STYLE SUFFIX]

**Saved image:** `_Saved-Images/item-silver-thimble.png`

### The Casting Mask (Mimic's Relic — GM Only)
> A theatrical mask on a dark background, lit by a single light source from above. Designed to fit any face. The surface is wrong in a way that is difficult to articulate — not because of what it looks like but because of how many times it has been used. Between a museum artifact and a wound. Dark background, single dramatic light. [STYLE SUFFIX]

**Saved image:** `_Saved-Images/item-casting-mask-GM-PRIVATE.png`

---

## Maps

### City District Overview
> A stylized noir map of a fictional city showing five districts: Old City (narrow historic streets), The Meridian (glass towers and boutiques), The Fairground District (entertainment and theaters), The Docks (industrial waterfront), The Overhang (dense residential). Hand-drawn aesthetic, muted colors, amber and grey tones. Labels in clean serif type. A dot marking "Curios & Chronicles" in Old City. Film grain texture. No compass rose — the city doesn't need one.

**Saved image:** `_Saved-Images/map-city-districts.png`

### The Subway — Schematic
> A stylized transit map for an underground system called "Line 0 — Ethereal Express." The lines don't correspond to normal city geography. One line is marked in red. Station names are slightly wrong — "Threshold," "The Still Point," "Last Platform." Hand-drawn aesthetic, aged paper texture, greenish tint. The kind of map that looks official until you look at it too long.

**Saved image:** `_Saved-Images/map-subway-schematic.png`
```

- [ ] **Step 3: Create `11-Visuals/Session-Image-Log.md`**

```markdown
---
entity_type: Tracker
name: "Session Image Log"
purpose: "Log of image prompts generated during live sessions. GM saves outputs to _Saved-Images/."
---

# Session Image Log

When the AI Co-GM generates an image prompt during a session, log it here with the session number and what triggered it. Save the generated image to `_Saved-Images/` with a descriptive filename.

---

## Log Format

```
### Session NN — [What triggered it]
**Prompt used:**
> [exact prompt]
**Saved as:** `_Saved-Images/session-NN-[description].png`
**Notes:** [anything worth noting — player reaction, if the image was used on screen, etc.]
```

---

## Session Image Log

*(Entries added during play)*
```

- [ ] **Step 4: Append Protocol 13 to `Co-GM-Prompts.md`**

```markdown
## 13. Live Image Generation (Use during any session to generate a visual)

The GM uses Gemini's image generator (separate from this chat) to create visuals during sessions. When an image would enhance the moment, generate a ready-to-paste prompt.

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
```

- [ ] **Step 5: Verify checklist**
  - [ ] `11-Visuals/` and `_Saved-Images/` directories created
  - [ ] All pre-campaign prompts include the style suffix placeholder
  - [ ] Every prompt has a `Saved image:` filename suggestion
  - [ ] Session Image Log has clear log format
  - [ ] Protocol 13 checks pre-made prompts before generating new ones
  - [ ] Protocol 13 labels image prompts clearly for copy-paste

- [ ] **Step 6: Commit**
```bash
git add "11-Visuals/"
git add Co-GM-Prompts.md
git commit -m "feat: add Visuals system with pre-campaign image prompts and live session image protocol"
```

---

## Self-Review

**Spec coverage check:**

| Requirement | Task |
|---|---|
| AI-agnostic Co-GM instructions | Task 1 |
| Canvas Handoff Protocol | Task 1 |
| Two-chat workflow documented | Tasks 1, 2, 3 |
| GEMINI.md as thin wrapper | Task 2 |
| CLAUDE.md created | Task 3 |
| Canvas setup prompt for GM | Task 2 |
| Co-GM Prompts — live session runner | Task 4 |
| Co-GM Prompts — post-session (public + private) | Task 4, Protocol 11 |
| Co-GM Prompts — audio transcript processing | Task 4, Protocol 12 |
| Emmerich NPC | Task 5 |
| Elias Thorne NPC (Mimic face) | Task 6 |
| The Architect GM-private | Task 7 |
| The Innocent Civilian GM-private | Task 8 |
| 2–3 Twice-Born NPCs | Task 9 (3 NPCs) |
| City Districts file | Task 10 |
| Curios & Chronicles room-by-room | Task 11 |
| Subway Stations room-by-room | Task 12 |
| Score file — Session 1 | Task 13 |
| Score file — Session 2 | Task 14 |
| Foreshadowing seeds | Task 15 |
| Urban Legends 8–10 leads | Task 16 (10 leads) |
| Public Wiki structure | Task 17 |
| Player-facing lair primer | Task 17 |
| Post-session wiki update workflow | Task 4 + Task 17 template |
| Audio transcript protocol | Task 4, Protocol 12 |
| Pre-campaign image prompts (all NPCs, locations, items, maps) | Task 18 |
| Live session image generation protocol | Task 18, Protocol 13 |
| Session image log for saving prompts and outputs | Task 18 |

All spec requirements covered. No gaps.

**Dependency order:** Task 6 before Task 15. Task 5 before Task 14. All other tasks are independent.
