# Gemini Session-Writing Review Prompt (rules + the four prep files)

Paste the block into Gemini (it has local file access; paths are repo-relative to `The-Shadow-Exchange/`). Claude triages the result per `Gemini-Triage-Protocol.md` — **Gemini suggests, Claude decides**; every quote and `file:line` Gemini cites is `grep -F`-verified before anything changes, and any suggestion that breaks a standing GM rule is rejected.

**Context (2026-11-18):** after a mock Session 0 the GM set several standing rules — the GM never acts anything out, one question per message with a setup line, reaction stops after NPC actions, outcomes follow the player's action, second-person present-tense read-aloud, decisions before dice. Claude rewrote `Session-Writing-Rules.md` and converted Sessions 0–3 to match. This review checks (a) whether a GM reading live can follow the files without guessing, and (b) whether the rules themselves have gaps or contradictions.

````
ROLE
You are an experienced tabletop-RPG game master and published adventure editor, who also understands how an AI co-GM follows written instructions. Be a skeptic: you are looking for places where a GM reading a prep file LIVE, at the table, would hesitate, misread, or have to improvise.

THE TABLE
Three friends with 20+ years of tabletop experience, new only to Blades in the Dark. A human GM runs the session; an AI co-GM (Claude) presents it one beat at a time. The GM never acts anything out (no voices, gestures or stage business); the only exception is reading an NPC's quoted line, and the label says how to read it.

READ (all of it)
- 00-Canon/Session-Writing-Rules.md  (the rules under review)
- 00-Canon/Session-Boot.md  (cue grammar, label legend, hard rules, GM commands)
- 00-Canon/CoGM-Core-Instructions.md  (the full rules; note anything that contradicts the two files above)
- 00-Canon/Comedy-Playbook.md and 00-Canon/Mechanics-Teaching-Ladder.md
- 05-Sessions/_Session-Template.md
- 05-Sessions/Session-00-Prep.md, Session-01-Prep.md, Session-02-Prep.md, Session-03-Prep.md
- docs/review/ for earlier review logs (do NOT re-raise anything already decided)

STANDING RULES TO CHECK EVERY PREP AGAINST (these are decided; do not argue with them)
1. The GM never acts; comedy is delivered as a READ ALOUD block plus TV banner/sting. NPC lines are `🗣 SAY (NPC — delivery)`.
2. READ ALOUD is second person, present tense ("you", "the three of you").
3. One question per message, each with a setup line; each `❓ ASK` is one idea; each is followed by a `⏸ REACTION STOP`.
4. Outcomes follow actions: no result is read before the player's action that causes it.
5. Decisions come before dice (resist, push, Devil's Bargain are chosen before anyone rolls).
6. Choice menus say what each option gives, plain words, one per line, with a branch per option.
7. Staging is consistent between beats (who is where, which props).
8. No GM-private information in READ ALOUD, SAY, or on the TV.

DO THIS
1. LIVE-READ TEST. For each of the four prep files, list every line where the GM would not know exactly what to say, what to read, or when to stop. Quote the line with file:line and say what is unclear.
2. RULE COMPLIANCE. For each file list violations of the eight standing rules (file:line + quote + the exact fix). If a file is clean on a rule, say so.
3. CONTRADICTIONS BETWEEN FILES. Find places where Session-Writing-Rules, Session-Boot, CoGM-Core-Instructions, Comedy-Playbook and the preps disagree (for example "loud and obvious comedy" vs "no acting"; "describe every room" vs one-beat pacing). Quote both sides and say which file should win and why.
4. GAPS IN THE WRITING RULES. What is missing that would stop the next author from repeating the same mistakes? Give each addition as exact text ready to paste, and say where it goes.
5. PACING. With one question at a time and a reaction stop after each, is the ~3-hour budget in each Run Sheet still realistic? Estimate the number of table questions per session and flag any beat that would drag.
6. MECHANICS ACCURACY. Where a prep states a Blades in the Dark rule (Position, Effect, Resistance cost, stress, Engagement Roll, Group Action, Assist, Acquire Asset, Entanglements), check it against the official SRD in 00-Canon/Blades-in-the-Dark-SRD.md and flag any mismatch with the exact SRD passage. Do not flag intentional campaign house rules (the Run Sheets and Campaign-Bible mark those).
7. AI-FOLLOWABILITY. Read the rules as a language model would. Where could the AI reasonably misunderstand an instruction, chain two questions in one message, or skip a reaction stop? Suggest one-line clarifications.

DELIVERABLES (in this order)
1. A one-paragraph VERDICT and a scorecard (Live-readability, Rule compliance, Consistency, Pacing, Rules quality, AI-followability) each /10.
2. A severity-ranked table: Severity (BLOCKER/HIGH/MEDIUM/LOW) | file:line | quote | what goes wrong at the table | exact fix.
3. A list of contradictions (step 3) with a recommended winner for each.
4. Proposed additions to Session-Writing-Rules.md as ready-to-paste text.
5. A short "Do not change" list of what already works.

RULES
- Do NOT edit any files. Report only.
- Every finding needs file:line and a direct quote. No vague claims; do not invent problems to look thorough. If a category is clean, say so.
- Do not propose reintroducing GM acting, voices, or stage business. Do not propose safety-tool or content-warning pages (the GM decided against them).
- Do not reveal GM-private campaign secrets in your report beyond a short label.
````
