# Gemini Player-Screen (TV) Review Prompt

Paste the block into Gemini (local file access; paths are repo-relative to `The-Shadow-Exchange/`). Claude triages the result per `Gemini-Triage-Protocol.md` — **Gemini suggests, Claude decides**; every quote or file reference Gemini gives is verified (`grep -F`) before anything is built, and any suggestion that would show GM-private information on the TV is rejected on sight.

Context (2026-11-18): the Player Screen currently shows only a scene image, a lower-third caption + subcaption, public clocks, document cards, a comedy banner and a small now-playing label. The GM and Claude want to know whether to add a few helpers for a table of experienced tabletop players who are new to Blades in the Dark. Candidate additions (Claude's suggestions, to be challenged): (1) a Position/Effect tag shown for a few seconds when a roll is called, (2) a small crew strip for the public numbers Heat / Coin / Rep, (3) a "Previously…" recap card at session start, (4) a one-line "Where we are" objective caption. Candidates Claude suggests NOT adding: per-player Stress/Harm, an initiative tracker, a permanent map.

````
ROLE
You are a senior UI/UX designer who specialises in "second-screen" displays for tabletop role-playing groups (a shared TV in a living room, read from 2-4 metres away, glanced at between conversation). You also understand tabletop RPG pacing. Be a skeptic: a good table display adds almost nothing and gets out of the way.

THE SETUP
- A group of three players (all 20+ years of tabletop RPG experience, new only to Blades in the Dark) plays in a living room. A GM runs the game; an AI co-GM (Claude) updates the TV by rewriting a small JavaScript file during play (one update per story beat; each update costs the GM a short pause, so every extra field has a real cost).
- The TV is a 16:9 display showing a full-screen browser page, read by the whole table from a sofa.

WHAT TO READ
- 11-Visuals/Player-Screen.html (the page: layout, fonts, sizes in vh/vw, animations)
- 11-Visuals/player-screen/scene.js (the live state object and the field documentation at its top)
- 00-Canon/CoGM-Core-Instructions.md, section "Player Screen — Live TV Protocol" and "Dual-Screen Setup" (when each field is used)
- 00-Canon/Session-Boot.md (how cues are fired during play; one beat then stop)
- Two or three of the table images in 11-Visuals/_Saved-Images/ (for example location-curios-exterior.png, npc-greta-fenn.png, location-subway-main-hall.png) so you understand the visual style.
Do NOT read the GM-private campaign files (03-NPCs, 05-Sessions, 00-Canon/Campaign-Arc.md). Everything on this TV is visible to the players, so nothing secret can ever appear on it.

DO THIS
1. REVIEW WHAT EXISTS. For each current element (image, caption + subcaption, public clocks, document cards in five styles, comedy banner, now-playing label, blank title screen): is it legible at 3 m on a 1080p TV? Quote the actual values from the file (font sizes, positions) and judge them. Flag anything too small, too low-contrast, or at risk of burn-in or overlap with another element.
2. JUDGE THE CANDIDATES. For each of the four candidate additions above: recommend BUILD / MAYBE / SKIP, with one sentence of reasoning, and say what it would cost the GM in pacing. Consider that a Position/Effect tag appears several times a session.
3. DESIGN THE ONES YOU RECOMMEND. For each BUILD/MAYBE item give: where it sits on the screen (in vh/vw terms, not overlapping the caption at bottom-left, the clocks at top-right or the now-playing label at bottom-right), size, colour from the existing palette (amber caption, red/other clock colours, dark overlay), how long it stays, how it animates in and out, and the exact new fields it needs in the SCENE object (name, type, example value). Keep it to the smallest possible change.
4. WHAT'S MISSING. Is there anything else genuinely useful for THIS table that I have not listed, for a group of experienced players learning Blades? Examples to consider only if justified: a "your turn" cue, a visible roll outcome (6 / 4-5 / 1-3), a "Devil's Bargain on offer" marker, a persistent public-NPC name list. Reject anything that adds clutter.
5. PACING AND RISK. Which of your recommendations would make the TV update more often than once per beat? Which would be easy to forget or leave stale on screen?
6. SPOILER SAFETY. For every recommendation, say how it could accidentally leak GM-private information (for example a clock that shows the secret Omen) and the one-line rule that prevents it.

DELIVERABLES (in this order)
1. A one-paragraph VERDICT and a scorecard (Legibility at distance, Glanceability, Pacing cost, Spoiler safety, Fit for this table, Visual consistency) each /10.
2. A table of the existing elements: element | legibility verdict at 3 m | concrete fix (exact CSS value if any).
3. A table of the candidates: candidate | BUILD/MAYBE/SKIP | reason | pacing cost.
4. Design specs for each recommended item, including the exact new SCENE fields and a sample value.
5. A short "Do not add" list.
6. A short "Do not change" list of things on the screen that already work.

RULES
- Do NOT edit files. Report only.
- Every claim about the current screen needs a file and line from Player-Screen.html or scene.js. No vague statements.
- Do not invent problems to look thorough; if an element is fine, say so.
- Never suggest showing GM-private information, hidden clocks, NPC secrets or "true forms" on the TV.
- Do not suggest adding safety-tool or content-warning screens (the GM has decided against them).
````
