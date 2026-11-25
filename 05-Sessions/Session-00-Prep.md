---
entity_type: Session
session_number: 0
title: "The Bookshop Existed Before You Did"
status: Prep
purpose: "Crew creation, table-culture reset, and opening montage. No heist."
runtime: "~2.5–3 hours"
---

# Session 0 — The Bookshop Existed Before You Did

**→ GM MOVE:** Players arrive with their PCs already made. Tonight is crew creation, table-culture reset, and the opening montage. **No heist tonight.**

> **Tone for tonight:** 🟡 warm and funny with a thread of unease. Let the table laugh in the first ten minutes — it teaches them this game is allowed to be funny. See `00-Canon/Comedy-Playbook.md`.

---

## RUN SHEET (read this first)

**Time budget (estimates; nothing is cut):** Pitch 5 → Introductions 25 → Crew creation + lair tour 65–80 *(3f alone 15–20; mock-0 report 2026-11-24)* → Friends/Rivals/Heirlooms 20 → **Trial Run 25** → Closing montage 15 → buffer 20 (≈ 3 h of play — on a slow night expect safe stop B or C; the mock, with its image and music pauses, ran 2 h 20 to 2 h 50, so plan a safe stop).
**Cold Open: none (Session 0).** **Safe stops:** **Nothing is cut:** every beat is played in full. If the evening runs out, stop at one of these **safe stops**: run the short **pause** (a "To be continued" TV card, one line of recap for next time, and a `Night-Log.md` row), and the next sitting opens with a "Previously" card. **Zoltar's card, the XP tally, the retrospective and the Faction Turn happen only when the session itself is finished.** **Never end a night on a Choice, a reveal or an Anchor decision.** **(A)** after Introductions (Beat 2) · **(B)** after the lair tour and crew creation (Beat 3f) · **(C)** after Friends, Rivals and Heirlooms (Beat 4) · then the Trial Run and the closing montage together.

| # | Beat | Trigger | 🎵 Music | 🖼 Image | 🎭 Comedy | Purpose |
|---|---|---|---|---|---|---|
| 1 | The Pitch | start | `music-s00-the-pitch` *(inline, before read-aloud; loops until Beat 2's song replaces it)* | — | — | Tone |
| 2 | Introductions | pitch ends | `music-bookshop-loop` | — | Banter seeds | Voices |
| 3a | Crew basics + the shop | "go" | `music-bookshop-loop` | `map-city-s00` ✅ *(city map)* → `location-curios-exterior` → `location-curios-interior` ✅ *(with the ATM read-aloud)* | **The ATM** | Cover |
| 3b | Zoltar opens | inline | `music-s00-zoltar-opens` *(inline — fire at "Zoltar" description)* | `location-zoltar-machine` ✅ *(on TV **during** the read-aloud — the closed machine)* → `location-containment-suite` *(the moment the wall slides open)* | **The Coin Code**; Zoltar judges | Reveal |
| 3c | Lair tour | wall opens | `music-containment-suite-loop` | — | **The Wall of Rules** | Onboarding |
| 3d | Scanner Station | "STOP HERE" | `music-vocal-scanner-station` *(vocal — GM OK'd firing it **inline, during** the read-aloud; it opens with ~10 s of static)* | `location-scanner-station` ✅ | — | Lore |
| 3e | Corkboard + Journal | switch back | `music-containment-suite-loop` → `music-bookshop-loop` *(switch on the closing "Upstairs: the Annex" line)* | `location-corkboard-wall` ✅ *(on TV for the read-aloud)* → `item-hunters-journal` ✅ *(the close-up, with the Journal paragraph)* → `location-annex` ✅ *(on "Upstairs: the Annex")* | — | Hooks |
| 3f | Upstairs: rep, abilities | return | `music-bookshop-loop` *(already playing)* | `location-annex` ✅ *(already on screen)* | — | Crew sheet |
| 4 | Friends, Rivals, Heirlooms | — | `music-bookshop-loop` | `location-annex` ✅ *(stays on screen)* | — | Seeds |
| 4b | **The Trial Run** | after Beat 4 | `music-bookshop-loop` | `npc-consequence-push` ✅ *(caption "Consequence"; stays up for the whole Trial Run; `npc-consequence.png`, asleep, is held for Beat 5)* | **Consequence knocks it over** | **Dice, Position, Effect, Stress, Resistance** |
| 5 | Closing montage | "go" | `music-s00-closing` *(no sting; no Zoltar voice)* | `npc-consequence` ✅ *(on the TV with the "Where is Consequence?" answer)* | Consequence; **Zoltar's card** | Promise |

**Asset status:** all required music and images exist ✅. No sting is used (the card needs no sound; the Zoltar voice was dropped, GM 2026-11-22). **Tonight the comedy runs on read-aloud text plus banners** (ATM, wrong Coin Code, Consequence).

### Tech checklist (before players arrive)
- [ ] Open `11-Visuals/GM-Dashboard.html` on the GM screen (F11). *(The Co-GM fills PC names, nicknames and table canon in live through the dashboard feed — see `Session-Boot.md` §2b.)*
- [ ] Open `11-Visuals/Player-Screen.html` on the shared TV (F11). It should show the title card. *(Co-GM updates `player-screen/scene.js` — see Core Instructions.)*
- [ ] Test `fade-switch.sh` with one track; confirm QuickTime Player is allowed to be controlled.
- [ ] Printed `Player-Reference.md` ×3 and `01-Crew/Hunter-Kit.md` ×3 (the kit list taught in Session 1); **Table Card** (`11-Visuals/handouts/Table-Card.pdf`) one per player + a spare — Position, Effect, Stress and Harm on one page; `GM-Cheat-Sheet.md` at your elbow.

---

## Pre-Session GM Checklist

> 🔒 **GM ONLY:**
>
> **Confirm players received (all via the campaign wiki):** What Kind of Game Is This · Our Lair · Known Contacts · Rules and Mechanics · Character Creation Guide · Downtime Guide · Session 0 Agenda.
>
> **GM prep:**
> - [ ] Read `00-Canon/GM-Rules-Reference.md`, `GM-Cheat-Sheet.md`, `Running-Your-First-Score.md`, `Comedy-Playbook.md`.
> - [ ] Skim `05-Sessions/Campaign-Arc.md` so you know where the threads go.
> - [ ] Note each PC's Vice, Friend, Rival, and **[Item: Cursed Heirloom]** as introduced.
> - [ ] Review `03-NPCs/Active/Elias-Thorne.md` — he appears in Session 1. The Mimic face is confirmed.
> - [ ] `04-Locations/Curios-and-Chronicles.md` open for the lair tour (it is the canon layout).
> - [ ] **City name:** (A) leave unnamed — "the city" — industrial-noir style; or (B) name it at the table and write it here: `__________`. Either is correct. Use consistently.
> - [ ] **Pronouns/GM voice in handouts:** keep neutral ("the GM").

---

## Beat 1 — The Pitch

**[MUSIC CUE: music-s00-the-pitch.mp3]** *(inline — start just before the read-aloud; it loops until Beat 2's music replaces it)*

> 🔊 **READ ALOUD:**
>
> "The world is exactly as it appears — if you're not looking closely. Governments function. Cities run. People go to work. And somewhere in the gap between a gas leak and a missing person report, something inhuman gets quietly erased from the record.
>
> That's the job. You are a small, underfunded monster-hunting firm. You take government contracts, you clean up the messes, and you make sure nobody sees what you saw. The Ministry calls you pest control. You let them.
>
> But you also keep what you find. Monster parts, supernatural items, things the Ministry says should be destroyed — you sell them instead, to a market the Ministry doesn't know exists. You are not the heroes the official story describes. You're something more interesting. Welcome to The Shadow Exchange."

---

## Beat 2 — PC Introductions, Round-Robin (25 min)

**[MUSIC CUE: music-bookshop-loop.mp3]** *(switch when the pitch read-aloud ends)*

🗣 **SAY** *(set it up):* *"Let's meet the crew. I'll ask each of you a few quick questions about your character, one player at a time. The other two: listen, react, and steal anything good."*

❓ **ASK PLAYER 1:** *"What's your character's name, and what do they look like — in one sentence?"* ⏸ **REACTION STOP.**
❓ **ASK THE SAME PLAYER:** *"What do you do in the bookshop on a normal day?"* ⏸ **REACTION STOP.**
❓ **ASK THE SAME PLAYER:** *"What is one thing your character carries that they wouldn't lend to anyone here?"* ⏸ **REACTION STOP.**
❓ **ASK THE SAME PLAYER:** *"What's your Vice, and who supplies it?"* ⏸ **REACTION STOP.** *(Stall menu once: a night-market cook · a bookie · a retired lighthouse keeper with a still. Write it down; Downtime uses it.)*

**→ GM MOVE:** If an answer stalls, offer the stall menu (one try); the introductions get the time they need.

🎭 **COMEDY SEED (🟡) — after EACH introduction, one nickname question.** Ask the next player about the one who just introduced themselves: Player 2 names Player 1's nickname, Player 3 names Player 2's, and **Player 1 names Player 3's** (don't skip this last one). Use a different lead-in each time:
❓ **ASK THE NEXT PLAYER:** *(a)* "What does the crew call [Name] behind their back, the nickname they pretend not to hear?" · *(b)* "[Name] has been called something in this shop for two years that they hate. What is it?" · *(c)* "What name does the crew use for [Name] when something goes wrong?" ⏸ **REACTION STOP.** Log it on the dashboard (Gags → PC nicknames); it comes back all campaign.

> 🔒 **GM ONLY:** Write down each PC's "thing they wouldn't lend" (often the Heirloom) and one unexpected detail they invented. Also read each player's **playbook** off the sheet they hold and log it with a `pc` op (action dots are asked at the Trial Run).

**→ GM MOVE:** After all three introductions, *before* the lair tour:

🗣 **SAY** *(set it up):* *"You've shared this building for two years. Let's talk about how that started."*
❓ **ASK THE TABLE:** *"How did the three of you end up working together?"* ⏸ **REACTION STOP.** 🔒 **If they stall (once):** a HELP WANTED card nobody remembers putting up · a mutual friend who vanished and left the lease · a pest-control contract that arrived addressed to all three of you.

🗣 **SAY** *(then):* *"There's one more thing nobody can explain: nobody remembers who signed the lease on this building."*
❓ **ASK THE TABLE:** *"What's your theory about who signed it?"* ⏸ **REACTION STOP.**

> 🔒 **GM ONLY:** Two years is canon. The lease is an Architect hook — **do not resolve it.** Whatever theories the table offers, write them down and confirm nothing. If they stall, offer: *signed in 1931 by a long-dead branch manager* · *the building signed it itself* · *nobody did; you simply kept being here.*

---

## Beat 3 — Crew Creation (50 min)

### Crew Type and Name
- **Crew type:** Hunters. **Crew name:** Curios & Chronicles (canonical — this is the front).

### 3a — The Shop

**[IMAGE CUE: map-city-s00.png]** ✅ *(caption "Your City"; the city map with the lair labelled. Show it first; the shop exterior replaces it when you read PART 1. Play it in full; it carries the no-subway line.)*

🗣 **SAY** *(set it up — the city they work in; one short line each, pause between)*:
> "This is your city. Your shop is the dot in **Old City**: wet brick and old paper, the walled old town in the west.
> **The Meridian**, across the river: glass towers, shopping, cameras on every corner.
> **The Fairground District**: theaters and late nights. Nobody asks questions at 2 a.m.
> **The Docks**: salt, rust and warehouses.
> **The Overhang**: houses and flats stacked up the cliff, where the neighbors report everything.
> And the river runs through all of it."

🗣 **SAY** *(the Session 2 seed — on its own, plainly, then move on)*: *"You get around by car, bike, taxi, bus or the elevated train. Nobody ever built a subway here: dig down more than a single floor in this city and you hit water."*
❓ **ASK THE TABLE:** *"Which district does the firm try to avoid on a job — and what happened there once?"* ⏸ **REACTION STOP.** *(If nobody answers after the stall menu: **the Meridian** — the cameras.)*
> 🔒 **GM ONLY:** Whatever they invent is canon — log it on the dashboard (Gags → City). *If they stall, offer:* **the Meridian** — a cover story got a Ministry clerk's mother in trouble · **the Overhang** — a witness filmed the van · **the Docks** — someone lost a shoe to the harbor. Do **not** let them place the Subway, the Architect or any reserved NPC here. *(The no-subway / water line is a deliberate seed for Session 2 — say it plainly and move on; do not explain it. If they ask where the elevated train is on the map: it runs along the outer ring road and is not drawn. If they notice the lair is eleven steps down: that is exactly one floor, and the lair's runes keep the water out.)*

**[IMAGE CUE: location-curios-exterior.png]** *(caption "Curios & Chronicles"; on TV before the read-aloud — first entry to the location)*

> 🔊 **READ ALOUD — PART 1:**
>
> "Let's look at your home. A narrow, three-story brick building squeezed between two glass-and-steel towers the city let through the old wall, like a relic of a forgotten century. It shouldn't exist. This is **Curios & Chronicles**.
>
> To any passerby: a struggling bookstore. Vanilla, old parchment, floor wax. A rotary phone. A half-knitted sweater. A sleeping cat named **Consequence**. It makes twenty dollars a day on purpose. That's the point.
>
> It used to be a savings bank."

**[IMAGE CUE: location-curios-interior.png]** ✅ *(caption "The Shop"; on the TV with the ATM read-aloud: the shop floor at night, the cat asleep on the counter, the Zoltar booth in the corner)*
> 🎭 **COMEDY BEAT — The ATM (🟢)** — *read it, don't act it:*
>
> 🔊 **READ ALOUD:**
> "On a quiet, rainy evening, the bell over the shop door jingles. A customer pokes their head in and squints at the old marble counter. 'Is the ATM still working?' they ask.
>
> The customer stares at the three of you. The silence goes on a very long time. The customer swallows.
>
> Slowly, without breaking eye contact, the customer takes a two-dollar bookmark from the rack, pays for it, and backs out of the shop. The bell jingles again."
>
> ❓ **ASK THE TABLE:** *"The customer is clearly terrified. Which of you gave them the scariest look, and what was it?"*
>
> ⏸ **REACTION STOP — next part depends on:** who the table says gave the scariest look, and what the look was (or if nobody does, you name one). Wait for their answer.
>
> 🗣 **SAY** *(only after their answer, plainly, then wait for the groans):* *"It used to be a bank. It makes twenty dollars a day."* **[PLAYER SCREEN: banner "NO WITHDRAWALS"]** *(fire it on the punchline; clear it after)*

> 🗣 **SAY** *(in passing; Sessions 1 and 3 assume the crew has the van):* *"Out back in the alley is your van — a retired bookmobile with 'C&C MOBILE LIBRARY — ASK ABOUT OUR LATE FEES' painted on the side. It starts on the second try."*
> 🔒 **GM ONLY:** Session 1 already assumes the crew drives it (the Lair Upgrade later *armors* it). Don't expand on it.

**→ GM MOVE:** That's the shop. Next: the back corner — **3b, Zoltar and the Coin Code.**

### 3b — Zoltar Opens

**[MUSIC CUE: music-s00-zoltar-opens.mp3]** *(inline — fire now, before reading; let it establish a beat)*

**[IMAGE CUE: location-zoltar-machine.png]** *(caption "Zoltar"; on TV now — fire with the Zoltar music, before the read-aloud)* ✅

> 🔊 **READ ALOUD — PART 2a (read while the Zoltar music plays; stop at the dash):**
>
> "In the back corner, near the Occult & Folklore section, behind a stack of moldering atlases, stands an old **Zoltar machine** — a glass-fronted booth the size of a phone box. Inside: a robed automaton with a painted beard, a turban, brass hands resting on a velvet pedestal where a deck of fortune cards used to be. One bent card is still stuck to the velvet; the lamp on top glows anyway, and nobody knows why. The rest of the cards are long gone. The machine has been unplugged at the wall for decades. It opens for one thing only: the right coins, in the right order — a code that only the people in this building know —"

> 🎭 **COMEDY BEAT — The Coin Code (🟢 — the table invents canon):**
>
> ❓ **ASK THE TABLE #1:** *"To open Zoltar, your crew drops coins in the slot in a secret order — for example, 'three nickels, then a quarter.' What is yours? Tell me which coins, one after another."*
>
> ⏸ **REACTION STOP — next part depends on:** the coins they name. Wait for their answer.
>
> 🔒 **GM ONLY:** Whatever they invent is canon (*two quarters, a dime, and a lie*). **Write it on the dashboard (Gags → Zoltar coin code).** Have them say it out loud, coin by coin.

> 🗣 **SAY** *(after their answer — set up the next step)*: *"Now let's open it. Zoltar is fussy about the order."*
> ❓ **ASK THE TABLE #2:** *"Who puts the coins in — and do they get it right the first time, or fumble it?"*
>
> ⏸ **REACTION STOP — next part depends on:** who does it, and whether they get it right.
> → *If they fumble it:* read the **wrong-code** paragraph below (Zoltar judges them), then let them try again.
> → *If they get it right (or nobody volunteers — pick the player who talked least and say* *"Let's see it done right — go on"*)*:* read Part 2b.
>
> 🔊 **READ ALOUD — IF THEY GET IT WRONG** *(a bad coin, a wrong order, or a fumble — it is funnier if it happens once):*
>
> *(Fill the bracket from the table's own canon: **[the wrong order]** = the mistake they described.)*
>
> "The coins go into the slot, one after another — **[the wrong order]**. Zoltar's glass eyes stay dark. With a small, sad whirr, his head turns one degree to the **right.** The wall does not move. Zoltar looks very disappointed in you." **[PLAYER SCREEN: banner "ZOLTAR JUDGES YOU"]**
>
> *(Let them try again.)*
>
> 🔊 **READ ALOUD — PART 2b** *(once they get it right):*
>
> *(Fill the bracket: **[the code]** = the coins and extras the table named, e.g. "say please".)*
>
> "The coins go into the slot, one after another — **[the code, in the table's order, including any spoken word]**. Zoltar's glass eyes flicker once, green; his head turns one degree to the left; and the wall behind him slides back with the heavy pneumatic hiss of a train door."

**→ GM MOVE: STOP.** Then swap the image.

**[IMAGE CUE: location-containment-suite.png]** *(caption "The Containment Suite"; **paired with the music cue just below: fire both on ONE "go"** — the wall has opened; the TV has been showing `location-zoltar-machine.png` until this moment. The Zoltar image is generated — never show the lair before the wall opens)*

### 3c — The Containment Suite

**[MUSIC CUE: music-containment-suite-loop.mp3]** *(fires together with the Containment Suite image above, on the same "go" — runs for the lair tour)*

> 🔊 **READ ALOUD — PART 3 (the stair and the room; stop before the Scanner Station):**
>
> "Eleven iron steps down. The pneumatic door seals behind you and the bookshop is gone. Vanilla and old parchment, replaced by something colder — a chemical tang, the sort of clean you only smell in dental offices and morgues. Fluorescent panels click on overhead, one by one.
>
> Along the far wall, a bank of stainless steel drawers, each one inscribed with thin silver runes. Pull one open and the cold air that spills out is sharp enough to fog. Things that should be spoiling don't. The runes are why. This is where the perishables stay perishable for as long as you need them — months, sometimes, when the wall is closed."

❓ **ASK THE TABLE** *(stop reading here; one quick answer)*: *"What's the first thing each of you does every morning when you come down these steps?"* ⏸ **REACTION STOP.**

> 🔊 **READ ALOUD — PART 3, continued (the vault and the table):**
>
> "Beside the drawers, set into the brick: the old bank vault door, heavy as a small car, lined with lead, a row of small mirrors sunk flush into the front face. When it's closed and sealed, what's inside goes quiet — stops humming, stops calling, stops being on the kind of map the Ministry's scanners read. You have tested this. They drive past the building. They find nothing. The mirrors are not for looking at.
>
> Centered under the brightest light: a zinc-topped surgical table with leather straps bolted to the corners. The zinc is scratched in patterns that suggest something was very interested in getting up. The straps have stains that didn't quite come out. This is where you open things, put them back together, or coax them into giving up what's inside them. Some jobs take an hour. Some take a week."

> 🗣 **SAY** *(Anchors, once: the hunters' first rule; about 20 seconds)*: *"One thing everyone in this building knows. Every monster that passes as human is tied to one personal object, its **Anchor**: a locket, a collar, a keepsake. Take the Anchor and the disguise starts to fail, in hours, not days. Every Anchor belongs to somebody, and what you do with it is what this job is."*

> 🗣 **SAY** *(the three kinds of loot, once; about 25 seconds)*: *"Three kinds of loot, and you'll meet all of them. **Biologicals** are perishable monster parts; keep them cold. **Relics** are cursed objects that never stop humming; that's what the vault is for. And **Anchors**, which you just heard about. You can sell a Biological or a Relic, use one once on a job, or trade it; an Anchor is never for sale."*

> 🎭 **COMEDY BEAT — The Wall of Rules (🟡/🟢):**
>
> 🔊 **READ ALOUD** *(read it straight, as writing on a wall — no voice needed)*:
> "By the stairs, six rules are written on the wall: five in black marker, in five tired hands, and one in red. You've read them every day for two years.
>
> One. Nobody says 'basement.'
> Two. Cold things go in the cold place. Today.
> Three. If it hums, it goes in the vault.
> Four. If it sings, it goes in the vault, and you leave.
> Five. Do not feed Consequence from the evidence.
> Six, in red ink, in a sixth hand: Do not trust anything that offers you tea.
>
> No one has ever admitted to writing Rule Six."
>
> ❓ **ASK THE TABLE:** *"Which of these rules exists because of something one of you did — and what did you do?"*
> ⏸ **REACTION STOP — next part depends on:** which rules they claim. Log them on the dashboard.
>
> 🔒 **GM ONLY — PURPOSE:** Rule Six is a plant: the tea contract that comes due at Mabel Ashby's house (Session 3) and the building's unexplained history. Nobody confesses; never explain it.
> 🔒 **GM ONLY:** Nobody confesses to Rule Six — keep it unexplained. *If they stall, offer:* **Rule One** — someone said "basement" to a customer · **Rule Two** — someone left something in a coat for a weekend · **Rule Five** — someone fed the cat something that turned out to be evidence.

**→ GM MOVE: STOP HERE.** Then fire the scanner music.

### 3d — The Scanner Station

**[IMAGE CUE: location-scanner-station.png]** ✅ *(caption "The Scanner Station"; on the TV for the read-aloud)*

**[MUSIC CUE: music-vocal-scanner-station.mp3]** *(inline — fire it as the read-aloud begins; the voice is part of the scene and the track opens with ~10 s of static. GM decision 2026-11-18)*

> 🔊 **READ ALOUD — PART 4 (Scanner Station only):**
>
> "Half-buried in cabling against the side wall, the Scanner Station — three modified shortwave radios on a rolling cart, each tuned to a different government frequency. They intercept Ministry bounty traffic before the public list updates, which is how you sometimes know who's about to be hunted before whoever's hunting them does. Beside them sits a fourth unit, older than the rest, with a single green lamp that has not been off in two years: the Resonance detector. It reaches about two blocks. There is a soft wash of static at all hours. You stopped hearing it months ago. It is always there."

❓ **ASK THE TABLE** *(stop reading here; one quick answer)*: *"Whose job is it to check that green lamp every morning, and what do they say when it's still on?"* ⏸ **REACTION STOP.**

> 🔊 **READ ALOUD — PART 4, continued (the AM voice):**
>
> "On clear nights, between the official broadcasts, you can pick up a signal that sounds like it comes from very far away — you have never been able to triangulate it. A man broadcasts on AM without a call sign. His voice is flat, unhurried, slightly too close to the microphone — the voice of someone who has been talking for a long time and expects to keep talking. He reports locations. Not addresses — coordinates, landmarks, the kind of description that tells you where something is without naming what the something is. He is wrong about the cause. He is wrong about the history. He is never wrong about where. You have driven to three of his locations. You found something at all three. You have not been able to reach him to ask how he knows."

> 🔒 **GM ONLY — PURPOSE:** the AM voice is **Aldric Voss**'s broadcast (he meets the crew in Session 2 only if they go to his workshop doorway). Never identify him tonight.

**→ GM MOVE: STOP HERE.** Switch music.

### 3e — The Corkboard and the Journal

**[IMAGE CUE: location-corkboard-wall.png]** ✅ *(caption "The Corkboard"; on the TV for the read-aloud)* · **[IMAGE CUE: item-hunters-journal.png]** ✅ *(fire it at the pause before the Journal paragraph; it replaces the corkboard picture. 🔒 The one red line is scribbled over: its words are unreadable on the TV and only come through when the crew studies the page, at S4.)*

**[MUSIC CUE: music-containment-suite-loop.mp3]** *(switch back)*

> 🔊 **READ ALOUD — PART 5:**
>
> "On the back wall, a corkboard pinned with polaroids. Each one annotated in red marker — a date, a name, a cause of death that is not the cause of death the Ministry filed. Every hunt that has happened in this building's life is on that wall. Look at it before a job involving anything you have already faced; there is always something pinned there that makes the next one easier. An old instant camera hangs from a nail beside the board, a half-used film pack tucked behind it. The earliest photo is older than one of you. None of you put it there.
>
> ⏸ **PAUSE — "go" for the Journal paragraph.** **[IMAGE CUE: item-hunters-journal.png]** *(inline: fire it first, then read on)*
>
> And near the surgical table, on a reading stand: an old leather-bound journal. Half the handwriting in it is yours. Half of it isn't. When you open it before a hunt, the people who came before you are still helping — some in pencil, some in pen, one of them in red ink, four years ago, in handwriting none of you recognize."

> 🔒 **GM ONLY:** The Trophy Wall and the Journal each give **+1d Study** vs. a monster type they've already hunted. The red-ink entry is the **Architect** thread (a Long-Term Project can chase it). **Do not** say "Spoilage Clock" or "Detection Clock" — those words don't exist for the players yet.

> 🗣 **SAY** *(set it up first):* *"The newest polaroids on that board are yours. The last one is only three weeks old."*
>
> ❓ **ASK THE TABLE:** *"Who took that last photo — and what was in it?"*
>
> ⏸ **REACTION STOP — next part depends on:** what monster they name and who took the photo. Wait for their answer.
>
> 🔒 **GM ONLY:** Whatever monster they name is now a type the **Trophy Wall covers (+1d Study against it)** — log it on the dashboard (Gags → Trophy Wall). Only a **named monster type** counts. **Camera rule:** the old instant camera on the nail by the board is a free (italic, no Load) Hunter Kit item; after the **first hunt of a new monster type**, someone photographs it and pins the polaroid, and from then on the crew has +1d Study against that type. Note each new type in the crew file's Trophy Wall list (Merton, a Barghest, is the first after Session 1). It also seeds Beat 3f's "prior history" question. If the table stalls, offer three: *a ghoul in a florist's crawl space · something in a drainage tunnel that looked like a wet coat · a "ghost" that turned out to be a very loud pipe.*

**→ GM MOVE:** Close the tour:

**[MUSIC CUE: music-bookshop-loop.mp3]** *(inline — fire it with the line below; the tour is over)*
**[IMAGE CUE: location-annex.png]** ✅ *(caption "The Annex"; fire it with the line below: the kettle, three armchairs, the whiteboard)*
🗣 **SAY:** *"Upstairs: the Annex — a kettle, three armchairs, and a whiteboard of banned words. And the Lofts: bunks for whoever stays too late."*
> 🔒 **GM ONLY — if anyone asks what the banned words are:** hunters' superstitions, written in several hands: *"basement" · "it's probably nothing" · "let's split up" · "what's the worst that could happen".* Or ask them to add one; it's a running joke, not a rule.
❓ **ASK THE TABLE:** *"Each of you: name one thing on the shelf in your corner."* ⏸ **REACTION STOP.**
> 🔒 **GM ONLY:** These shelf objects are heirloom seeds — note them, but the Heirlooms themselves come in Beat 4.

### 3f — Reputation, Abilities, Upgrades

*(Music and image are already running from the end of 3e: `music-bookshop-loop` and `location-annex`. No change here.)*

🗣 **SAY** *(set it up):* *"Back upstairs, with the kettle on. The firm has a reputation in the small circle that knows you at all, and a few trade secrets. Let's write them down."*

🗣 **SAY** *"How the underworld sees the firm."* ❓ **ASK THE TABLE:** *"Pick the firm's reputation: Ambitious, Brutal, Daring, Honorable, Professional, Savvy, Subtle or Strange, or name your own."* ⏸ **REACTION STOP.** 🔒 **GM ONLY:** the SRD list. It is a flavour label and a crew-XP cue ("build or bolster the firm's reputation"), **not** the Rep number (Rep starts at 0). Log it on the dashboard (Gags → Crew).

❓ **ASK THE TABLE:** *"Besides the one in that last photo, what other kinds of monsters has the firm dealt with? Spirits? Things that look human? Something else?"* ⏸ **REACTION STOP.**

> 🔒 **GM ONLY:** Their answers become your seed pool for what they've already done (and which monster types the Trophy Wall already covers). If they say "things that look human", keep it for later: 🗣 **SAY** *"Good. Noted."* It does **not** add a Trophy Wall type or any +1d.

### Crew Abilities and Upgrades
> 🔒 **GM ONLY:** Read options from `00-Canon/GM-Rules-Reference.md` Part 4. Do not paraphrase or invent.

The crew starts with the lair fixtures above and **Double Bookkeeping** *(custom: roll Sway after a Ministry bounty to keep one minor item)*.
> 🔒 **GM ONLY:** 6 clean · 4–5 they keep it and a secret clock ticks · 1–3 they surrender it and it ticks. **Never name or show that clock tonight.** *(Anyone without a special ability takes the first on their playbook, the SRD default.)*
 Pick **one more** ability:

| Ability | Effect | Best for |
|---|---|---|
| **Deadly** | Each PC adds +1 action rating to Hunt, Prowl, or Skirmish (max 3) | Field efficiency |
| **Anointed** | +1d to resist supernatural threats; +1d to recover from supernatural harm | Survival — *recommended* |
| **Forged in the Fire** | Each PC +1d on all resistance rolls | Broad durability |
| **Death Veil** | No extra Heat when killing is involved | Lethal, clean ops |
| **No Traces** | Rep on quiet jobs; +1 Rep at zero Heat | Low-heat reputation |
| **Synchronized** | Multiple 6s in group actions = critical | Teamwork |
| **Pack Rats** | +1d to acquire assets | Gear & black-market access |
| **Accord** | Treat up to three faction statuses at +3 as turf | Mid-game pick |

> 🗣 **SAY** *(1 — what they already have):* *"Your firm already has one trick: **Double Bookkeeping**. After a Ministry job, you can quietly keep one small item off the books. We'll see how it works when it comes up. Now pick **one more** ability."*
>
> 🗣 **SAY** *(2)*: *"Don't worry about words like 'resist' or 'critical' yet; we'll test them in a few minutes, and you can swap this after Session 1."*
> 🗣 **SAY** *(3 — the menu; one option per line: what you get, and who it suits)*:
> "**Deadly** — each of you gets +1 on Hunt, Prowl or Skirmish. *Good if you want to be better in the field.*
> **Anointed** — extra dice to resist supernatural threats and to recover from supernatural harm. *Recommended — good if you worry about surviving what you hunt.*
> **Forged in the Fire** — extra dice whenever you resist anything. *Good if you want everyone tougher.*
> **Death Veil** — killing no longer draws extra attention. *Good for a lethal, quiet crew.*
> **No Traces** — quiet jobs earn you reputation. *Good if you want to stay under the radar.*
> **Synchronized** — when you act together, two or more 6s count as a critical. *Good for a tight team.*
> **Pack Rats** — extra dice to get hold of gear and black-market goods. *Good if you like having the right tool.*
> **Accord** — the territory of three friendly factions counts as turf you can work in. *Good for a well-connected crew.*"
>
> ❓ **ASK THE TABLE:** *"Which one?"* ⏸ **REACTION STOP — next part depends on:** their pick.
> → **If Deadly:** 🗣 **SAY** *"Each of you picks one: Hunt, Prowl or Skirmish. That one gets +1."* ❓ **ASK EACH PLAYER:** *"Which one?"* ⏸ **REACTION STOP.**
> → **Any other pick:** nothing more to ask; 🗣 **SAY** *"Good. That's yours."*

> 🔒 **GM ONLY:** if they ask what you recommend, it's **Anointed** (the menu says so); don't read this line aloud.

> 🗣 **SAY** *(the upgrade menu — read it as written; one option per line)*:
> "Next: your firm gets **two improvements**. Pick two different ones, and tell me which comes first.
> **Training** — you all learn faster. When you train between jobs, you advance faster. *Good if you want to grow quickly.*
> **Quality** — one kind of gear is better made, so it works better when you use it. You'd pick the kind: fake badges and papers, tools, weapons, or occult implements. *Good if you like good equipment.*
> **Secure Lair** — the Containment Suite gets better locks, alarms and traps, so intruders — the Ministry included — have a much harder time getting in. *Good if you worry about who might walk in.*
> **Workshop** — a proper workbench in the lair for long projects: tinkering, brewing, researching. You can work on them without leaving the shop. *Good if you want to work on things at home.*"
>
> ❓ **ASK THE TABLE:** *"Which two improvements does the firm take, and which one comes first?"*
>
> 🔒 **GM ONLY:** the order matters: the **first** pick pleases a faction, the **second** annoys one (table below). Ask each pick's follow-up in turn; if they take **Quality and Training**, ask the Quality question, then the Training question.
>
> ⏸ **REACTION STOP — next part depends on which upgrades they pick:**
> → **Quality:** 🗣 **SAY** *"Which kind of gear gets better?"* ❓ **ASK:** *"Fake badges and papers, tools, weapons, or occult implements?"* ⏸ **REACTION STOP.**
> → **Training:** 🗣 **SAY** *"Training works on one thing at a time."* ❓ **ASK:** *"What does the firm train: Insight (thinking and noticing), Prowess (fighting and moving), Resolve (willpower; we use these three words in a few minutes), or each character's own playbook?"* ⏸ **REACTION STOP.**
> → **Secure Lair:** nothing more to ask. 🗣 **SAY** *"Good. The new locks go in this week."*
> → **Workshop:** nothing more to ask. 🗣 **SAY** *"Good. The back room gets a proper bench."*
>
> 🔒 **GM ONLY — FACTION REACTIONS (SRD; record privately, do not announce):** the two upgrades change two factions: one **pleased** (**+1 status**; the +2 for 1 Coin is not available at 0 Coin) and one **annoyed** (**−2 status**; the −1 for 1 Coin is not available at 0 Coin). Use only the weak rival firms for the annoyed side, so no main faction starts hostile. Pleased from the **first** pick, annoyed from the **second**: *Training* → pleased Hunter Underground / annoyed Castellan Retrieval · *Quality* → pleased Meridian Group / annoyed Harrow & Sons · *Secure Lair* → pleased Hunter Underground / annoyed Castellan Retrieval · *Workshop* → pleased Harrow & Sons / annoyed Castellan Retrieval. Log both on the dashboard now (Gags → Firm standings); write them into `02-Factions/Faction-Tracker.md` **after** the session (Boot §2b). **Floor −2 (house rule):** reductions may stack, but no firm starts below **−2**; if a reduction (upgrade, hunting ground or favourite contact) would take a firm below −2, skip it. **Most likely path:** Quality as the *second* pick (Harrow & Sons −2) plus the Old City hunting ground (Harrow & Sons −1) → Harrow is already at −2, so the hunting-ground −1 is **skipped**; say nothing, just don't mark it. Keep a running list of every firm's standing on the dashboard (Gags → Firm standings). *(The Containment Suite fixtures they just toured are the crew's two-plus starting upgrades: Cold Storage Locker, Lead-Lined Vault, Post-Op Table, Scanner Station, Trophy Wall, Hunter's Journal.)*
>
> 🗣 **SAY** *(hunting grounds, SRD; every crew has them)*: *"Last thing about the firm: every crew has a **hunting ground**, a small corner of the city it works most. Yours is where the shop is: **Old City**, unless you'd rather pick the Docks or the Fairground."* ❓ **ASK THE TABLE:** *"Old City, the Docks, or the Fairground?"* *(leave out any district the table said the firm avoids in 3a)* ⏸ **REACTION STOP.** *(If nobody answers: Old City.)* 🔒 **SRD costs, said to yourself:** the district's faction notices: **−1 status** with it (Old City: Harrow & Sons · the Docks: Castellan Retrieval · the Fairground: Meridian Group), since there is no Coin to pay them off. **Preferred operation type: Extraction** (retrieving an Anchor, Relic or Biological): +1d to gather information on such a target in the hunting grounds, and a free extra downtime activity toward that operation.
>
> 🗣 **SAY** *(what the firm is, said once)*: *"So that you know: the firm starts small and broke on purpose. **Tier 0**, a **weak hold**, and **0 Coin**. Every job changes that."*

---

## Beat 4 — Friends, Rivals, and Heirlooms (20 min)

> 🗣 **SAY** *(set it up first):* *"Every one of you has a life outside this building: someone who'd help you without being asked, someone who'd like to see you fail, and one thing you carry from before. I'm going to ask about each, one at a time. These people will turn up in the story later, so give me names — we won't play them tonight."*
>
> 🔒 **GM ONLY — read this BEFORE the three questions** (names the players may not use as a Friend or Rival, and what to say):
> - **Director Vance / Deputy Director Reyes / Section Chief Kress** → *"That one's above your pay grade for now. Pick someone at your own level."*
> - **Elias Thorne** (pre-cast as the Mimic face) → *"Thorne is a Ministry name that will come up later — pick someone outside the Ministry for now."*
> - **Anyone from the Subway** (PTOLEMY, Cosma Linden, Aldric Voss, Senna Calder, the Crossroads Broker), **Emmerich, Mabel, Agnes, Renwick Stalls, Merton, Gerald, Mara Halliday** → *"They're not yours yet — pick someone else."*
> - **Greta Fenn** → allowed as a joke: *"You've been mailing her forms for two years — she's never met you."*
> - **Harlan Okafor** → allowed as a **Friend** (it deepens his Session 4 debut); as a Rival: *"Harlan works as a friend, or not at all. Pick someone else as the rival."*
> - **Before accepting any invented name** (friend, rival, shop, street), grep `03-NPCs/NPC-Index.md`, bench and standby rows included (Fitch Ambrose, Yardley Pike…); on a collision ask *"a different name?"*

❓ **ASK THE TABLE #1 — Friends:** *"First, a friend: someone who'd help you without being asked. One sentence each — who are they?"*
🔒 **GM ONLY — if someone stalls (offer once):** a pawnbroker who owes you · a night nurse · your landlady.
⏸ **REACTION STOP — next part depends on:** who each player names (check the list above before accepting).

❓ **ASK THE TABLE — the firm's favourite contact** *(SRD, once all three Friends are named)*: *"Which of the three Friends is the firm's closest ally, the one it would call at 3 a.m.?"* ⏸ **REACTION STOP.**
🔒 **GM ONLY:** **+1 status** with that contact's faction. **Most Friends are civilians**, so use the firm of the district they live or work in: **Old City → Harrow & Sons · the Docks → Castellan Retrieval · the Meridian or the Fairground → Meridian Group · a fellow hunter, or anywhere else → Hunter Underground.** Then **−1 status** with a rival firm **other than** the one the upgrades or the hunting ground already marked (the SRD's +2/−2 is optional; floor −2: see 3f). If every rival firm is already marked, put it on the one with the mildest mark, never below −2, or skip it: never the Ministry, Apex or the Twice-Born. Log both on the dashboard now (Gags → Firm standings); the Faction-Tracker is written after the session.

❓ **ASK THE TABLE #2 — Rivals:** *"Now a rival: someone who wants what you have, or would be glad to see you fail. One sentence each — who are they?"*
🔒 **GM ONLY — Rival stall menu (offer once, only if someone stalls):** a firm that lost a contract to you · an old partner who left on bad terms · a collector who wants what you keep.
⏸ **REACTION STOP — next part depends on:** who each player names (check the list above before accepting).

🗣 **SAY** *(before the third question):* *"Your Heirloom is the one thing you carry that you probably should have left behind."*

❓ **ASK THE TABLE #3 — Heirlooms:** *"One sentence each: where did it come from, and why should you have left it behind?"* *(If the earlier "thing you wouldn't lend" is already the object, name it for them.)* 🔒 **Stall menu (once):** a medal that isn't yours · a pocket watch that stopped · a book with a name torn out. **If a player passes:** 🗣 **SAY** *"Then it's the thing you wouldn't lend. We'll find out why."* Use the object from Beat 2 and do not ask again.
⏸ **REACTION STOP — next part depends on:** each player's answer. Then pick each pattern privately.

> 🔒 **GM ONLY:** For each Heirloom, privately choose a degradation pattern (`00-Canon/Heirloom-Degradation-Patterns.md`).

---

## Beat 4b — The Trial Run (25 min — *the first roll anyone at this table has ever made in Blades*)

> 🔒 **GM ONLY:** The players have **never played Blades.** Do one **low-stakes practice roll** so Session 1 isn't a cold start. Teach only: **dice, Position, Effect, Stress, Resistance.** (See `00-Canon/Mechanics-Teaching-Ladder.md`, cards 1–4 and 6.) **Do not** mention anything else (one clause on Trauma is allowed in the Stress line; no Trauma tables).

**[IMAGE CUE: npc-consequence-push.png]** ✅ *(caption "Consequence"; she is mid-push on the Journal. It stays up for the whole Trial Run and the banner pops over it. The sleeping picture `npc-consequence.png` is held for Beat 5.)*
> 🗣 **SAY:** *"Downstairs, the shop floor. Afternoon."*
> 🔊 **READ ALOUD:**
> "A customer is about to walk in — you can see the shape of them at the front window. And Consequence, from the counter, with the slow deliberation of a creature who has never once regretted anything, pushes the **Hunter's Journal** — left on the counter after this morning's stock-take — off the edge with one paw. It hits the floor. It falls open. It is open to a page that says, in a hand that is not yours, **DO NOT SHELVE THIS WHERE CUSTOMERS CAN SEE.** You have about ninety seconds."

> 🎭 **COMEDY BEAT (🟢):** **[PLAYER SCREEN: banner "CONSEQUENCE!"]**
> 🔊 **READ ALOUD:** "Consequence stares at the nearest one of you. She does not apologize."

**→ GM MOVE:** *Hand out the printed **Table Cards** now — "This is the whole game on one page."*

❓ **ASK THE TABLE:** *"Someone needs to get that journal back out of sight before the customer reads it. What do you do?"* 🔒 **Menu if they freeze (offer once):** 🗣 *"You could (a) grab it fast, (b) hide it under something, (c) distract the customer."* ⏸ **REACTION STOP — next part depends on:** who acts and how.

**Then teach, in this order, about 30 seconds each:**

1. 🗣 **SAY** *(name the action)*: *"That's **[Finesse / Prowl / Sway]** — the action you're using."*
2. 🗣 **SAY** *(Position and Effect)*: *"Position is how exposed you are. This one is **Risky** — if you miss, it costs you something. Effect is how much you get done. This is **Standard** — a clean save."*
3. 🗣 **SAY** *(the dice)*: *"You roll as many dice as your rating in that action, and you look at the **highest** one. If your rating is zero, you roll two dice and take the **lowest**."* ❓ **ASK THE PLAYER:** *"How many dice is that: how many dots do you have in that action? Roll them. What's the highest?"* ⏸ **REACTION STOP.**
4. **The result** — read only the branch that matches:
   - **6:** 🔊 *"Clean. The journal is back under the counter, the page is turned, and the customer wanders in and asks about cat books."*
   - **4–5:** 🔊 *"You do it, **but** there's a cost: the customer glances at the page as you tuck it away. 'Is that a recipe?'"*
   - *(then, after any result)* 🗣 **SAY** *(Effect, one line)*: *"That was **Standard** effect: you got it done. With **Great** effect you'd also have turned the page to something boring; with **Limited** you'd only have got it off the counter."*
   - **1–3:** 🔊 *"The customer reads the page: 'DO NOT SHELVE THIS WHERE CUSTOMERS CAN SEE.' They laugh. 'Great marketing.' They buy the book — the only book you've sold all day. Consequence is very pleased."*
5. **Resistance** *(decide to resist FIRST, roll the resistance dice AFTER — you can't roll and then choose; offer it on a 4–5 or a 1–3):*
   - 🗣 **SAY:** *"You can **resist** that cost. You decide to resist **before** you roll the resistance dice — no peeking first."*
   - ❓ **ASK THE PLAYER:** *"Do you want to resist — yes or no?"* ⏸ **REACTION STOP.**
   - → **If yes:** 🗣 **SAY** *"Then roll the attribute that fits what you're resisting — Insight for what you notice and cover, Prowess for physical strain, Resolve for willpower. Here it's **Insight**: you're covering for what the customer saw. Insight is four actions: Hunt, Study, Survey and Tinker. Count how many of those four have at least one dot; roll that many dice (zero: roll two, take the lowest). Tell me the highest."* ⏸ **REACTION STOP** — then step 6 works out the cost.
   - → **If no:** 🗣 **SAY** *"Fair. You take the cost as it is."* Still read step 6, as *what resisting would have cost if they had rolled a die*, then let the next player try.
   - → **If the roll was a 6 (nothing to resist):** 🗣 **SAY** *"On a 6 there's nothing to resist — but here's how it works if there had been one."* Then read step 6 as an example.
6. 🗣 **SAY** *(Stress — the cost)*: *"The cost is **6 minus your highest die** — so a 5 costs you 1 Stress, and a 6 is free. Stress is your reserve of willpower. Fill all nine boxes and you take a **Trauma**, a lasting scar; we'll cover that if it ever happens. That's it. That's the whole game. We'll do this for real next time."*

❓ **CHECK FOR UNDERSTANDING** *(one question, not a quiz):* *"What would you have done differently if the customer were two minutes away?"* ⏸ **REACTION STOP.**
> 🔒 **GM ONLY:** *This practice Stress clears before Session 1.* Invite the other two to make one quick roll each (Assist is taught in S2: do not offer it): **(1)** the customer asks about cat books (Sway); **(2)** Consequence goes for the till (Finesse). 🗣 **SAY** *"Erase that Stress; it was practice."* If they say "gone slower", they've understood Position. If someone asks to **help** another's roll: 🗣 **SAY** *"Good instinct. Helping is a real move and we use it in Session 2. Tonight it's one roll each."* **Mark on the dashboard (Mechanics Taught): dice and Position *understood* (state 2); Effect, Stress, Resistance *introduced* (state 1).**

---

## Beat 5 — Closing Montage (10–15 min)

**[MUSIC CUE: music-s00-closing.mp3]** *(inline — fire it with the "Closing time" line; it runs through the questions)*

> 🎭 **COMEDY BEAT — Where is Consequence? (🟢):**
>
> 🗣 **SAY** *(set it up first):* *"Closing time. Consequence has settled down for the night — and as always, she's picked the single most inconvenient spot in the building."*
>
> ❓ **ASK A PLAYER:** *"Where is Consequence asleep?"*
>
> ⏸ **REACTION STOP — next part depends on:** their answer. Then 🗣 **SAY** *"…and she is not moving."* and make it the worst possible place (evidence, an open first-aid kit, a contract). Put their answer into the read-aloud below.
>
> 🔒 **GM ONLY:** She has never once been helpful. She has never once been removed.

**[IMAGE CUE: npc-consequence.png]** ✅ *(show it ONLY if the answer is the counter, a stack of papers, or the default; the picture shows her asleep on an old catalog by a rainy window. For any other spot, `image: null` with caption "Closing Time".)*
> 🔊 **READ ALOUD:**
>
> "It's late. The shop is closed. Consequence the cat is asleep on **[wherever the table said she is — make it the worst possible place; if nobody answered, use: the counter, on top of a 1962 mail-order catalog that has no business being there]**. The rotary phone has not rung. The kettle is cooling. From the back room, behind the Zoltar machine, the Scanner Station is humming on its own frequency — a quiet wash of static that you stopped noticing months ago.
>
> Tonight there is no envelope on the counter. Tomorrow there will be."

> 🔊 **READ ALOUD (the card):**
> "In the back corner, Zoltar's slot gives a small, apologetic *clunk.* A card drops into the tray. It is warm. **YOU WILL SOON RECEIVE AN ENVELOPE. IT WILL NOT BE GOOD NEWS. IT WILL BE DAMP.**"
> **[PLAYER SCREEN: card style `fortune`, title "ZOLTAR SAYS"]** *(leave it up through the card read-aloud; clear it, `card:null`, before the four questions)*
> 🔒 **GM ONLY — audio:** show the card; no sound. **No voice line** (dropped, GM 2026-11-22).

> 🗣 **SAY** *(explain why before asking anything):* *"Before we wrap up, I'd like to ask each of you one question. There are no wrong answers. What you tell me is how I'll know what you want from this campaign, and I'll build around it."*
>
> **Player 1** — 🗣 **SAY** *"I want to know what keeps your character coming back to this job."* then ❓ **ASK** *"Why is your character still doing this work?"* ⏸
>
> **Player 2** — 🗣 **SAY** *"Every good story has something to lose."* then ❓ **ASK** *"What is your character most afraid will happen here?"* ⏸
>
> **Player 3** — 🗣 **SAY** *"Last one for your character: what they are like when nobody is watching."* then ❓ **ASK** *"What does your character do when no one else is in the bookshop?"* ⏸
>
> **The whole table** *(this one is for you, not your characters)* — ❓ **ASK** *"What do you want me, as the GM, to make sure I do in this campaign?"* ⏸
>
> *(One question per message: ask, stop, wait for the answer in chat, then the next.)*

> 🔒 **GM ONLY:** Log all four answers verbatim on the dashboard now (Gags → Table promises); copy them into `05-Sessions/Campaign-Current-State.md` → *Table Promises* **after** the session (Boot §2b). They are the contract you have with each player. Offer an example if someone stalls (a one-line answer is fine).

---

## If they zig (Session 0)
🔒 **GM ONLY — likely improvisation, with ready lines:**
- *They open the vault or drawers:* 🗣 **SAY** *"Three sealed tins from old jobs. Nothing hums tonight."*
- *They try to triangulate the AM voice:* 🗣 **SAY** *"The signal only comes on clear nights. It's raining."*
- *They plug Zoltar in:* 🗣 **SAY** *"Nothing happens. The lamp was already on."*
- *They push for something the prep never covers:* call for no roll before the Trial Run; say *"Good question. Hold it for Session 1."*

## After Session 0 — Between This and Session 1

- Update each PC file in `01-Crew/PCs/` with anything that emerged.
- Update `01-Crew/Crew-Sheet.md` — reputation, hunting grounds (asked at Crew Abilities), ability, **both** upgrades and the two faction reactions, the **coin code**, the **nicknames**.
- Update `01-Crew/Contacts.md` — Friend and Rival NPCs.
- Copy the four closing answers into `Campaign-Current-State.md` → *Table Promises*; list the firms' starting standings in `02-Factions/Faction-Tracker.md`; add any Trophy Wall type named in 3e (Gags → Trophy Wall) and the favourite contact to the crew file.
- Write the confirmed PC names, nicknames and table canon into `GM-Dashboard.html` (INIT_PCS / INIT_GAGS), bump `SAVE_VERSION`, and reset `dashboard-feed/feed.js`.
- Co-GM generates **Session 1's Cold Open** (see Core Instructions).
