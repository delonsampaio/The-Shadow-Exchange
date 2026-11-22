# Gemini Spoiler Check #2 — everything the players will see or hear (before Session 0)

Paste the block into Gemini (it has local file access). Claude triages the result per `Gemini-Triage-Protocol.md`: **Gemini suggests, Claude verifies and decides.** Run it before the first real Session 0. A parallel Opus pass (`Opus-Player-Facing-Spoiler-Check-2026-11-22.md`) covers the same four channels; do not give Gemini that report, so the two checks stay independent.

````
ROLE
You are a careful spoiler auditor and an experienced GM. You can read local files (and images, if you can see them).

THE GAME
"The Shadow Exchange": Blades in the Dark with Supernatural/Scooby-Doo comedy and real dread. A human GM and three friends (20+ years of tabletop experience, new to Blades) play weekly with an AI Co-GM that shows images, cards and clocks on a shared TV, plays music, and gives the GM labelled text to read aloud: 🔊 READ ALOUD, 🗣 SAY (NPC lines), ❓ ASK, ⏸ REACTION STOP, 🔒 GM ONLY (never read aloud). The players have a website (the sibling folder ../The-Shadow-Exchange-Players, MkDocs, docs/). Content rule: anything goes (gore, violence, cursing); the ONLY hard line is nothing racist and nothing that mocks a culture or religion. Do not flag gore or swearing.

THE SECRETS THE PLAYERS MUST NOT LEARN EARLY
The Mimic / the Understudied, and that Elias Thorne is it (and the Casting Mask and its prior faces); the Architect and who it is; Section Chief Kress and his role (never named on screen before Session 7); that Renwick Stalls / Stalls Holdings is an Apex shell; what the Omen is; what the Subway is, who runs it, PTOLEMY's nature, the Broker, Line 0 and the Waking; the Ministry Audit clock before Session 4; any hint that Thorne's behaviours are "tells"; Aldric as the AM-radio host before Session 9 (and the line "It found the frequency" before Session 24); Decay values; hinge NPCs; GM-only stats. Deliberately planted subtle clues that appear in the plan are allowed: flag only clues that are too strong, too early, or overt.

READ (repo-relative; the players' site is ../The-Shadow-Exchange-Players/docs)
CLAUDE.md; 00-Canon/Session-Boot.md; 00-Canon/Wiki-Update-Protocol.md; 00-Canon/Zoltar-Card-Deck.md; 09-Threads/Secrets-and-Reveals-Schedule.md; 05-Sessions/Session-00-Prep.md, Session-01-Prep.md, Session-02-Prep.md, Session-03-Prep.md; every page in ../The-Shadow-Exchange-Players/docs and its mkdocs.yml; 11-Visuals/handouts; the images named in the four Run Sheets under 11-Visuals/_Saved-Images.

DO THIS (four channels)
1. THE PLAYERS' SITE: read every page. Flag any sentence, example, glossary entry, page title, nav label, image alt text or file name that gives away a secret or a clue too strong.
2. THE TV: list every PLAYER SCREEN card, caption, subcaption, banner and clock named in the four preps, and every Zoltar card for Sessions 4–28. Flag leaks and early reveals. Check the rule that at most one Thorne-tell card appears before Session 15.
3. WHAT THE PLAYERS HEAR: every 🔊 READ ALOUD and 🗣 SAY line in the four preps. Flag any that state a secret, narrate one, or sit inside a quote block while holding GM-only text.
4. WHAT THE PLAYERS SEE ON PAPER AND SCREEN: handouts and the images for Sessions 0–3: visible text, signs, stamps, forms, names, faces, clock times, props. Flag anything that gives a secret away or contradicts its read-aloud.

RANK each finding BLOCKER (a secret is overtly shown or said) / HIGH (a clue too strong or early) / MEDIUM / LOW, with the channel, file and line (or image name), the secret it touches, and a concrete fix. Then list what you checked and found clean.

RULES
- Do NOT edit any files. Report only.
- Quote the line or name the image. Never invent a quote, a line number or an image detail. If you are not sure, say "unverified".
- Do not flag a secret merely for existing in a GM-only 🔒 block or in a GM-only file: only what players see or hear.
````
