# World-Building Expansion Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Fill identified world-building gaps: Subway entry WTF rewrite, Subway Mysteries content, Vanished Firm identity, Casting Mask backstory, Ministry internal factions, and Heirloom degradation patterns.

**Architecture:** Six independent tasks. All are markdown file creates or modifications. No task depends on another. Tasks 1–2 are Subway-related and should be done together for consistency. Tasks 3–6 are standalone.

**Tech Stack:** Markdown files in `/Users/delonsampaio/Desktop/VSCode Workspaces/The-Shadow-Exchange/`.

---

## Task 1: Rewrite Subway Entry — The WTF Moment

**Problem:** The current entrance read-aloud in `04-Locations/The-Subway/Overview.md` is three sentences and tells rather than shows. The descent in `Stations.md` is atmospheric but undersells the physical impossibility of the space. For D&D players this is the "Diagon Alley moment" — it needs to land as genuinely arresting.

**Files:**
- Modify: `04-Locations/The-Subway/Overview.md`
- Modify: `04-Locations/The-Subway/Stations.md`

- [ ] **Step 1: Replace the "Standing scene-setter (first descent)" section in Overview.md with the following**

Replace from `## Standing scene-setter (first descent)` to end of file with:

```markdown
## The Entrance Read-Aloud (Use when crew first finds it)

The entrance appears after the Emmerich score. They are not looking for it. They are in a dead-end alley, and it is just there.

> "The alley ends in a brick wall. That's what it should be. Except there's a green-painted iron railing set into the concrete at the far end — waist high, leading down, the kind of railing you'd find at any subway entrance in any city. A sign above it, tiled in white ceramic, reads: **LINE 0 — ETHEREAL EXPRESS**. The tiles look original. They look like they've been there since the twenties.
>
> A man in a suit rounds the corner behind you at full stride, phone to his ear, and walks directly through the railing without slowing. Through the sign. Through the top step. He doesn't stumble. He doesn't notice. He turns the corner at the end of the alley and is gone.
>
> The railing is still there. You can see it. You could reach out right now and put your hand on it and feel the cold paint. You didn't do anything to earn this. Nothing changed about you between the street and this alley. Something decided you qualify, and it didn't ask."

**GM note — the qualifying moment:** Something specific the crew did in the Emmerich score is what opened access. It is not about success or failure. It is about what they were willing to feel before they acted. The Subway perceived this. See `04-Locations/The-Subway/Mysteries.md` for the full range of qualifying behaviors — pick the one that fits what actually happened at your table.
```

- [ ] **Step 2: Replace the "First Descent Read-Aloud" section in Stations.md with the following**

Replace from `## First Descent Read-Aloud (Use in Session 2)` through the blank line before `## The Main Hall` with:

```markdown
## First Descent Read-Aloud (Use in Session 2 — read in two parts)

**PART ONE — The Stairs:**

> "The stairs go down further than they should.
>
> This is not a figure of speech. Count them if you want — you have time. The alley above you is two stories deep at most. You are on step thirty-seven and still going. The city sounds — traffic, wind, the specific ambient noise of the world above — cut off completely on step fourteen. Not gradually. On step fourteen exactly, as though someone closed a door. After that: your own breathing. The iron railing under your hand is cold and real and slightly damp.
>
> The light changes on the way down. Street-level sodium orange. Then fluorescent. Then something greenish and sourceless that you cannot locate — it's not coming from any fixture you can see. It's just there, ambient, like the light inside a fish tank.
>
> By the time you reach the bottom, you are not sure how far underground you are. You are sure it should be impossible."

**PART TWO — The Hall (read when they reach the bottom):**

> "The space you step into is a vaulted hall — arched ceiling lost in greenish shadow somewhere high above, tile floors the color of old municipal bone. It shouldn't fit here. It is the size of a train station. Forty feet across, easy, and it extends in both directions further than you can see, curving gently out of sight like a runway.
>
> There is a transit map on the north wall. You look at it automatically, because maps orient you. It doesn't. The lines don't match anything — not the city above, not any city — and one of them is marked in red ink that looks newer than the rest. You find yourself looking for your street. It's not there. Nothing you recognize is there.
>
> There are people here.
>
> Some of them aren't.
>
> A figure in a business suit reads a newspaper at a bench. Their shoes are on backwards. They are reading what appears to be the Classifieds. A woman in a yellow coat is laughing at something her companion said; her companion has too many fingers. A teenager in a school uniform is asleep against a pillar, a backpack in their lap, and their shadow is pointing the wrong direction.
>
> Nobody looks at you. Not yet. This is a place with etiquette you don't know yet, and you can feel that getting it wrong would be immediately obvious. Like walking into a dinner party mid-conversation and not knowing anyone's name.
>
> In the far corner — before you have had time to take any of this in — a piece of old leather luggage shifts. Brass clasps, cracked leather. No visible eyes. The clasps are moving in a slow deliberate pattern, like morse code except it isn't morse code. It is looking at you. It has been looking at you since before you came down the stairs. It has been waiting."
```

- [ ] **Step 3: Commit**
```bash
git add "04-Locations/The-Subway/Overview.md" "04-Locations/The-Subway/Stations.md"
git commit -m "enhance: rewrite Subway first-entry as full WTF arrival sequence (two-part read-aloud)"
```

---

## Task 2: Populate Subway Mysteries File

**Problem:** `04-Locations/The-Subway/Mysteries.md` exists but contains only headers and placeholder bullets. It needs actual GM content for the four candidate truths, the qualifying criteria, and PTOLEMY's true function.

**Files:**
- Modify: `04-Locations/The-Subway/Mysteries.md`

- [ ] **Step 1: Replace the entire file contents with the following**

```markdown
---
type: mystery
status: open — campaign rule: do not resolve until players get close
---

# The Subway — Mysteries

**Campaign rule:** Nothing in this file resolves without an explicit GM canon update. The Subway is a living mystery, not a feature. Pick your preferred truth privately and play toward it — but keep all four alive until the players get close enough to force the question.

---

## The Central Question: Who Controls the Subway?

Four candidate truths. Choose one. Play all four as possible until the reveal.

### Option A — The Subway Is Alive
The infrastructure is the entity. The station itself perceives, selects, and protects. The transit map changes because it reflects the Subway's current state of awareness, not geography. PTOLEMY is the Subway's speaking apparatus — the most organized expression of a distributed intelligence. The "master" is the architecture.

**Implication:** You can't negotiate with it. You can only qualify. The crew qualified because the Subway perceived something in the Emmerich moment and made a decision the way a living system makes decisions — not consciously, but correctly.

**Reveal mechanic:** The map changes in front of a PC. A new line appears, going somewhere. PTOLEMY's clasps spell out coordinates, not words. The station itself is asking them to go somewhere.

### Option B — It Was Built and Then Abandoned
Something ancient built the Subway as a refuge and then left — or was forced out. The infrastructure still functions because the design was that good. The community that formed here is genuinely ungoverned. PTOLEMY predates everyone and is the last functional component of the original system. The ledger PTOLEMY keeps is the original purpose: logging who has shelter, what they've given up, what they owe the original builder.

**Implication:** The builder may be coming back. The Omen Clock is the return. What the crew finds at Omen 8 is not a monster — it's the thing that made this place and has been waiting to come home.

**Reveal mechanic:** PTOLEMY's ledger, if the crew ever reads it, has entries going back to a date that predates the city. The first entry is in a language no one alive speaks.

### Option C — Someone Hides In Plain Sight
One of the community members *is* the Subway's controlling intelligence — wearing a face, living a quiet life, maintaining access control through attention rather than mechanism. They have been doing this for longer than anyone else has been alive. The Twice-Born community knows this person. They do not know what this person is.

**Candidate:** The Crossroads Broker. He sits in the back booth. He has always been there. Every deal he makes requires him to understand, completely, what the person across from him actually wants — because what you actually want is the qualifying criterion for access. He tests everyone who comes down the stairs, whether they know it or not.

**Reveal mechanic:** A crew member cuts a deal with the Broker and then asks a question they shouldn't know to ask. The Broker's stillness before he answers lasts exactly one second too long. He says: "You've been figuring this out for a while." He does not deny it.

### Option D — The Subway Is All of Them
No master. No intelligence. The Subway is a collective manifestation — every entity that has ever needed refuge contributed something, and what was contributed accumulated into a space that could hold more. Access works because the Subway is, in some distributed sense, every member of its community making a judgment simultaneously. Apex Aegis can't find an entrance because the community collectively decided not to show them one.

**Implication:** The Subway can be destroyed by attrition. If enough members leave, die, or are taken, the space shrinks. The Subway Decay Clock is not just a narrative metaphor — it is the Subway literally losing mass.

**Reveal mechanic:** When the Subway Decay Clock hits 4, the Main Hall is noticeably smaller. When a beloved community member dies, a section of the transit map goes dark.

---

## The Qualifying Criterion — What Did the Crew Do?

The Subway opened access after the Emmerich score. The following behaviors are each sufficient, in isolation or combination. The GM picks which one fits what actually happened at the table.

| What happened | Why it qualified |
|---|---|
| The crew warned Emmerich instead of taking the job | Chose a person over a contract. The Subway perceived this as a capacity for that choice. |
| The crew took the job but felt the weight of it | The moral cost registered. Something about registering it, rather than dismissing it, was the signal. |
| A crew member interacted with Emmerich as a person, not a target | Called him by name. Asked a question that wasn't tactically necessary. |
| The crew returned the thimble after taking it | The rarest qualifying act. This one gets them immediate standing in the Subway community; PTOLEMY's first clasp movement is something that translates as recognition, not just awareness. |
| A crew member physically shielded Emmerich from Apex | The body as argument. The Subway doesn't care about ideology — it responds to action. |

**GM note:** Whatever the crew actually did, describe the entrance as if the Subway noticed that specific thing. If a player later asks "why could we suddenly see it?" — let PTOLEMY or the Crossroads Broker give them the answer in a way that reflects their actual session.

---

## PTOLEMY's Ledger — What Is It Tracking?

PTOLEMY tracks favors. Every favor given and owed. Every deal made. Every debt outstanding. This is the surface layer and it is completely accurate.

Underneath that, PTOLEMY is tracking something else.

**The GM's choice:**

- **Option A (The Subway is Alive):** PTOLEMY tracks probability weights. Every favor represents a data point about what someone is willing to give up vs. hold onto. PTOLEMY is forecasting something — who among the community will make a specific decision at a specific moment. The Omen is the event it's been forecasting for.
- **Option B (Built and Abandoned):** PTOLEMY tracks debts owed to the original builder. The favors it collects are payments toward those debts. Some accounts have been accumulating interest for centuries.
- **Option C (Broker as Master):** The Broker and PTOLEMY are the same system in different forms. PTOLEMY tracks who is in the Subway. The Broker tracks what they want. Together they maintain access control with perfect information.
- **Option D (Collective):** PTOLEMY is a memory archive. Every entry is a record of someone who needed the Subway and was given it. The ledger is the Subway's proof of itself — evidence that it exists, has always existed, and will continue to exist. PTOLEMY's true function is witnessing.

**What a crew member sees if they ever read it:** Their names are in there. Entry dated three days before they found the entrance. No notes — just the names. PTOLEMY, when asked, clicks its clasps once. This translates as "Yes."

---

## Hypotheses Raised in Play

*(Date-stamp each — useful for callbacks. Format: Session NN — who said it — what they said.)*

*(Empty — add as play generates them)*

---

## Scraps

*(Overheard fragments, things the crew noticed and didn't follow up on, things the GM dropped that haven't landed yet)*

*(Empty — add as play generates them)*

---

## Mimic Interference

The Mimic is actively working to advance the Subway Decay Clock from within. Some scraps the crew encounters in the Subway will be planted by the Understudied. Track suspected planted scraps separately.

**Known planted material:** Urban Legend 8 (The Tailor's Referral) — Mimic-authored job board posting designed to compromise a hidden Anchor fragment.
```

- [ ] **Step 2: Commit**
```bash
git add "04-Locations/The-Subway/Mysteries.md"
git commit -m "feat: populate Subway Mysteries with 4 candidate truths, qualifying criteria, and PTOLEMY ledger options"
```

---

## Task 3: Name and Detail The Vanished Firm

**Problem:** `02-Factions/Rival-Firms.md` has the Vanished Firm as a stub ("Ministry says they retired. Harlan says they didn't. Where it leads: an Apex Aegis black site.") with no name, no last job, no usable detail.

**Files:**
- Modify: `02-Factions/Rival-Firms.md`

- [ ] **Step 1: Replace the "The Unnamed Firm" section with the following**

Replace from `## The Unnamed Firm` to end of file with:

```markdown
## Vantage & Lowe *(Tier I — Disappeared)*

Two-person firm, now gone. Filed a Ministry retirement notice ninety-three days ago. Ministry processed it without follow-up. Harlan Okafor says they didn't retire — he had coffee with one of them two weeks before they disappeared.

**What they were:** Specialist biologicals firm. Emery Vantage (hunter, thirty years experience) and Dasha Lowe (handler/fixer, former Ministry archivist who knew which records to request and which to never mention). Meticulous. Ethical, by the industry's standards. Not the type to walk away mid-year.

**Their last job:** A Ministry contract for a Biological entity at a Docks cold storage facility. Routine by their file. They took it. They filed an initial assessment. They never filed a completion report.

**What the Ministry knows:** Their lair was vacated. Personal effects removed. No signs of violence. The Ministry closed the file. Retirement is the official position.

**What Harlan knows (and will share over coffee if asked carefully):** Emery called him two days before the disappearance. Said the Biological in the Docks wasn't what the contract described. Said the contract itself read wrong — phrasing he'd never seen in a Ministry envelope before. Said he thought someone had gotten to the routing system. He was going to make some calls. He didn't call back.

**What actually happened:** Apex Aegis wanted whatever was in the Docks facility. They couldn't get a Ministry contract because the entity didn't qualify under standard criteria. So they had one manufactured, routed through a compromised Ministry handler, and sent a firm with a clean record to do the extraction. When Vantage & Lowe figured out the contract was fabricated, Apex moved to contain the problem. Their lair was vacated under pressure. Where they are now is the question.

**The Apex black site:** A climate-controlled archive facility disguised as a private medical storage company in the Docks. The entity from the contract is there. So is the evidence of the manufactured job. So, probably, are Vantage and Lowe — in whatever condition Apex decides is acceptable.

**Hook:** This is Score 4 or 5 material. The crew hears a rumor, follows the thread, and finds something Apex doesn't want found. If they extract Vantage and/or Lowe, they gain the most experienced outside allies available — and make Apex into a committed enemy.

**Standing:** — *(firm is gone; if Vantage and/or Lowe are recovered, track their standing individually)*
```

- [ ] **Step 2: Commit**
```bash
git add "02-Factions/Rival-Firms.md"
git commit -m "feat: name and detail Vantage & Lowe — the vanished firm with full hook and Apex black site"
```

---

## Task 4: Create Casting Mask History (GM-Private)

**Problem:** The Mimic's history before Elias Thorne is blank. The ring from a previous face is mentioned but that face has no identity. Players will eventually want to know how long this has been happening and who got used before.

**Files:**
- Create: `03-NPCs/GM-Private/The-Casting-Mask.md`

- [ ] **Step 1: Create the file with the following content**

```markdown
---
type: gm-private
classification: GM-PRIVATE — DO NOT SHARE WITH PLAYERS
status: active
linked_npc: "03-NPCs/Active/Elias-Thorne.md"
---

# The Casting Mask — History & Previous Faces
## ⚠ GM-PRIVATE — DO NOT SHARE WITH PLAYERS

The Casting Mask is the Mimic's primary tool. Theatrical in construction — thin, designed to fit any face — wrong in ways that are difficult to articulate. It has been used long enough that the surface carries memory from every face it has worn. The Understudied sometimes reaches for memories that belong to previous faces and finds them. This is not a malfunction. It is accumulation.

---

## How the Mask Works

Contact with a living person for approximately seventy-two hours produces a complete copy — appearance, voice, mannerism, surface memory. The original person is not destroyed by the process. They are displaced: relocated, documented as having left voluntarily, occasionally simply gone.

The Understudied does not experience wearing a face as deception. It experiences it as becoming. After long periods in a single face, it is genuinely uncertain which convictions are its own and which it inherited.

---

## Previous Faces (Most Recent First)

### Face 3 — Elias Thorne *(Current — 11 years)*

Ministry field liaison. True Believer — the Understudied chose this face because Thorne's genuine conviction that the Ministry was right makes the performance sustainable. You can't fake sincerity for eleven years. You have to mean it.

**Status of original Thorne:** Gone. Relocated to a coastal property outside Ministry jurisdiction under a documented early retirement. He did not choose this. He does not have the resources to argue about it. He is alive, and he has been alive for eleven years, and he has not told anyone what happened because no one would believe him.

**Memory bleed:** The Understudied reaches for Thorne's memories and finds them. It has Thorne's password habits, his coffee preference, his opinions about Ministry internal politics. Occasionally it finds a memory that doesn't match what actually happened — the gap between what Thorne experienced and what the Understudied has been doing while wearing him.

---

### Face 2 — Mira Solano *(7 years — 18 to 11 years ago)*

Civilian. Journalist who covered municipal infrastructure. The Understudied wore her to maintain a watching brief on a city planning process that would have disrupted a Subway entrance location. The face was necessary for approximately eight months. The Understudied kept it for seven years.

**The ring:** Mira's ring. Her grandmother's. She wore it on her right hand. The Understudied kept wearing it after taking Thorne's face — habit, or the accumulation of seven years, or something harder to explain. It is slightly too loose on Thorne's hand. When the Understudied reaches for it and it isn't where it should be, what it's reaching for is Mira, not Thorne.

**Status of original Solano:** She went home one day and someone else was living her life. She is now known as someone who had a breakdown — quit journalism, moved cities, withdrew. She has been in the same city as the Understudied for three years without knowing it. She writes a local newsletter about urban gardening. She sometimes has a feeling she can't explain when she passes certain buildings.

---

### Face 1 — Corvin Ashby *(3 years — 21 to 18 years ago)*

Ministry archivist. Chosen for access to document routing systems. This is when the Understudied learned how Ministry contracts are manufactured — the same knowledge later used to compromise Vantage & Lowe's last job (see `02-Factions/Rival-Firms.md`).

**Status of original Ashby:** Deceased. Natural causes, seven years ago. The Understudied attended the funeral as Mira Solano. It brought flowers.

---

## What the Understudied Actually Wants

The Understudied is not purely an agent of chaos. Its goal is structural: advance the conditions under which the cover-up becomes impossible to maintain, so that the Twice-Born community and the human world are forced into open negotiation. The Subway Decay Clock is not an end — it is leverage.

The Understudied believes, genuinely, that the current arrangement — hidden supernatural, Ministry control, Apex extraction — is unsustainable and wrong. It is trying to end it. Its methods have involved eleven years of deception, three displaced lives, and one death. It does not experience these as contradictions.

**The reveal conversation:** When confronted, the Understudied does not lie. It explains its reasoning, clearly, with Thorne's warmth and conviction. Some of what it says is correct. The crew has to decide what to do with someone who caused real harm in pursuit of something that might actually be right.

---

## GM Notes — Using Previous Faces

- Mira Solano can appear in play before the Mimic reveal as a completely mundane character. She can even become a contact. The dramatic irony of the crew befriending the Understudied's previous face is available.
- Corvin Ashby's archived files are still in the Ministry system. They contain irregularities — routing anomalies that go back twenty years — that a sufficiently paranoid archivist might notice.
- Elias Thorne (the real one) is alive at a coastal property. If the crew ever goes looking for him post-reveal, he will tell them everything he knows. He has been trying to figure out who to tell for eleven years.
```

- [ ] **Step 2: Commit**
```bash
git add "03-NPCs/GM-Private/The-Casting-Mask.md"
git commit -m "feat: add Casting Mask history with three previous faces and Understudied motivation"
```

---

## Task 5: Add Ministry Internal Factions

**Problem:** The Ministry is flat — one agenda, one voice. By mid-game the crew needs factions within it to play against each other. Currently `02-Factions/The-Ministry.md` has Director Vance and Ministry Couriers and nothing else.

**Files:**
- Modify: `02-Factions/The-Ministry.md`

- [ ] **Step 1: Append the following to the end of The-Ministry.md**

```markdown

---

## Internal Factions

The Ministry is not monolithic. Three internal factions have divergent views on what the cover-up is actually for.

### The Oversight Desk *(Reformist)*

Belief: licensed firms should have more autonomy, existing Twice-Born should be registered and managed rather than extracted, and the Ministry's current methods create more exposure risk than they prevent.

**Key figure:** Deputy Director Alma Reyes. Mid-fifties. Sends the crew's contracts through channels that give them more time than standard. Has never said this aloud. If directly approached with evidence of Apex Aegis corruption, she will act — carefully, slowly, and in a way that protects her career first.

**Hook:** Reyes is the reason the crew's contracts are slightly better than they should be. She sees potential in firms that operate the way they do. She will never acknowledge this unless the crew forces the issue.

### The Bureau of Compliance *(Mainstream)*

Belief: the current system works. Enforce the rules. Extract or neutralize as contracted. Do not ask questions the paperwork doesn't require.

**Key figure:** Director Arthur Vance. The crew's nominal supervisor. Believes in procedure. Not cruel — procedural. If the crew follows the rules, he is not a problem. If they don't, he is a very slow, very thorough one.

### The Suppression Bureau *(Extremist)*

Belief: the Twice-Born are not a population to be managed — they are a contamination to be eliminated. The cover-up exists to protect humans, not to give monsters somewhere to hide. The licensed firm system is a mistake that Apex Aegis will eventually correct.

**Key figure:** Section Chief Dorian Kress. Never directly contacts field firms. Operates through budget line items, routing decisions, and manufactured contracts. Vantage & Lowe's last job was routed through Kress's office. He does not know the crew exists yet. When he notices them, it will be because they've done something he considers a problem.

**Hook:** Kress and Apex Aegis have a relationship neither party would admit to. They want compatible things for different reasons. The mid-game reveal that the crew's biggest institutional threat isn't Apex but a Ministry official working with Apex is the kind of escalation that recontextualizes everything that came before.
```

- [ ] **Step 2: Commit**
```bash
git add "02-Factions/The-Ministry.md"
git commit -m "feat: add Ministry internal factions — Oversight Desk, Compliance Bureau, Suppression Bureau"
```

---

## Task 6: Create Heirloom Degradation Patterns

**Problem:** The Campaign Bible references four heirloom degradation patterns and Session 0 tells the GM to privately assign one to each PC. These patterns aren't documented anywhere the GM can reference.

**Files:**
- Create: `00-Canon/Heirloom-Degradation-Patterns.md`

- [ ] **Step 1: Create the file with the following content**

```markdown
---
entity_type: Canon
purpose: "GM reference for PC Cursed Heirloom degradation. Assign one pattern per PC privately during Session 0 introductions."
---

# Heirloom Degradation Patterns

Every PC has a Cursed Heirloom — an object that anchors them to their life before the work. The heirloom is degrading. The pattern is GM-private. Symptoms manifest gradually, responding to the PC's choices.

**Assignment:** During Session 0, as each player describes their heirloom, privately select the pattern that fits the object and the character. Never tell the player which pattern you've assigned — only show them symptoms.

**Advancement:** Each pattern has four stages. Advance one stage per major arc, or when the PC does something that specifically stresses the heirloom's resonance (see individual patterns).

---

## Pattern 1 — The Fading

**The heirloom is forgetting what it is.**

The object is losing definition. Photos in a locket go grey. Text in a journal becomes harder to read. A piece of jewelry loses its distinguishing details — the engraving, the setting, the specific weight that made it unmistakable.

**Good for:** Objects that represent a person (photograph, letter, gift from someone loved). Works for PCs whose character arc involves losing connection to who they were before.

| Stage | Symptom |
|---|---|
| 1 | Details are slightly harder to make out in low light. The PC doesn't mention it yet. |
| 2 | The detail is gone in good light too. They can describe what used to be there. They remember it. |
| 3 | The object looks new — unmarked, unindividuated. It could belong to anyone. |
| 4 (Full) | The PC picks it up and cannot remember what made it theirs. The memory is not gone — but the connection between the object and the memory has broken. |

**Advancement trigger:** The PC chooses the job over a personal relationship, or fails to act to protect someone they love.

---

## Pattern 2 — The Persistence

**The heirloom is becoming more present, not less.**

The object refuses to stay out of the way. It turns up in pockets it wasn't placed in. It appears on surfaces where it wasn't left. It is in every photograph the crew takes, regardless of whether it was in frame. It is not haunted — it is insistent.

**Good for:** Objects the PC has complicated feelings about (inherited from someone difficult, acquired under circumstances they don't discuss, connected to something they're not proud of). Works for PCs who have something to reckon with.

| Stage | Symptom |
|---|---|
| 1 | The PC finds it in their left pocket. They're sure they put it in their right. |
| 2 | Someone else in the crew finds it somewhere it couldn't have been placed. |
| 3 | It appears in a photograph from before the PC joined the firm. |
| 4 (Full) | The PC leaves it behind deliberately — locks it in the vault, gives it to someone, throws it in the harbor — and finds it in their pocket the next morning. It is always warm. |

**Advancement trigger:** The PC avoids or suppresses something they need to address. The heirloom responds to avoidance.

---

## Pattern 3 — The Echo

**The heirloom is picking up signal.**

The object is Resonance-sensitive and becoming more so. A compass spins near supernatural events. A watch runs correctly except during Resonance activity, when it runs backward. A music box plays a tune that, if anyone could identify it, would be distressing.

**Good for:** Objects with mechanical or musical components. Works for PCs who are the crew's most perceptive member, or who are in danger of perceiving too much.

| Stage | Symptom |
|---|---|
| 1 | The object behaves oddly near strong Resonance. The PC notices but doesn't raise it. |
| 2 | The behavior is predictive — it responds before the Resonance event, not during. |
| 3 | Other crew members have noticed. The object is now a better Resonance detector than the Scanner Station, but using it costs the PC a point of Stress. |
| 4 (Full) | The object is broadcasting, not just receiving. Apex Aegis scanners can detect it from a block away. The PC has to choose: destroy it (losing their Anchor) or find a way to suppress it (Lead-Lined Vault, indefinitely). |

**Advancement trigger:** The PC pushes themselves beyond their limits on a job — marks Trauma, or takes a consequence they don't resist.

---

## Pattern 4 — The Weight

**The heirloom is getting heavier.**

Not metaphorically. The object is gaining mass. A ring that once spun freely is tight. A photograph that once slipped into a breast pocket now requires effort. A coin that used to flip easily sits in the hand like a stone.

**Good for:** Small, light objects (coins, rings, keys, small photographs). Works for PCs who are accumulating moral weight — making hard choices, compromising the values they started with.

| Stage | Symptom |
|---|---|
| 1 | Slightly heavy. The PC notices, says nothing. |
| 2 | Noticeably heavy. Other crew members can feel it if handed the object. "This is heavier than it looks." |
| 3 | Visibly wrong. The object sags pockets. The PC carries it in their hand sometimes instead of their pocket — easier that way. |
| 4 (Full) | The PC cannot carry it on their person anymore. It is not painful — it is simply too heavy to carry and walk. They leave it on the Post-Op table in the morning. They pick it up when they come home. If they die on a job, it will be on the table waiting. |

**Advancement trigger:** The PC makes a choice that compromises their pre-campaign self — takes a life, betrays an ally, destroys an Anchor they could have preserved.

---

## GM Notes

- **Never name the pattern to the player.** Only show them symptoms. Let them describe what their character notices.
- **Symptoms should emerge in narration, not as mechanics.** "When you search your jacket for the key, your hand closes around the coin first. It's heavier than you remember." Not: "Your heirloom advances to Stage 2."
- **The pattern can shift** if the PC's arc shifts significantly. Pattern 4 can become Pattern 1 if the PC finds something worth holding on to. Note the shift privately.
- **The heirloom at full degradation is not destroyed.** It becomes something else — a different kind of object with a different relationship to the PC. This is the end of one arc and the start of another.
```

- [ ] **Step 2: Commit**
```bash
git add "00-Canon/Heirloom-Degradation-Patterns.md"
git commit -m "feat: add four heirloom degradation patterns for GM Session 0 assignment"
```

---

## Self-Review

| Requirement | Task |
|---|---|
| Subway entrance WTF rewrite | Task 1 |
| Subway descent WTF rewrite | Task 1 |
| Subway Mysteries — 4 candidate truths with detail | Task 2 |
| Subway Mysteries — qualifying criterion table | Task 2 |
| PTOLEMY ledger purpose (4 options) | Task 2 |
| Vanished firm named (Vantage & Lowe) | Task 3 |
| Vanished firm last job + Apex connection | Task 3 |
| Vanished firm hook (Score 4-5) | Task 3 |
| Casting Mask history — 3 previous faces | Task 4 |
| Casting Mask — Mira Solano (the ring explained) | Task 4 |
| Casting Mask — Understudied's real goal | Task 4 |
| Ministry internal factions — 3 wings | Task 5 |
| Ministry — Suppression Bureau / Kress hook | Task 5 |
| Heirloom degradation — 4 patterns with stages | Task 6 |
| Heirloom — GM assignment notes | Task 6 |
