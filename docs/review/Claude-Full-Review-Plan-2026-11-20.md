# Claude Full-Review Plan (three lanes) — prepared 2026-11-20, NOT yet launched

**Why:** most of this repo was written by Claude (Sonnet) and reviewed by Gemini. A second independent Claude read, after a lot of canon change in one day, should catch contradictions, leaks and design weak spots that neither of those passes saw.
**When:** after the Session 1 mock, before the first real Session 0. Launch only when the GM says so.
**Triage:** results come back to the main session and go through `Gemini-Triage-Protocol.md` rules (verify every file:line with grep; ADOPT / ADAPT / REJECT / ASK). Reviewers **report only**; they never edit files.

## Scope and rough cost (measured 2026-11-20)
| Lane | What | Files read | Size (≈ tokens, one read) | Model | Rough total cost* |
|---|---|---|---|---|---|
| 1. Continuity | Every canon decision vs every file; Run Sheet ↔ body sync; asset cues vs files on disk | whole repo (124 `.md`, excl. SRD/archive) — mostly grep-driven | ~230k | **Sonnet** | ~0.5–1M tokens |
| 2. Player-facing leak check | What players or the TV can see vs the GM-private secret list | 22 files (players' site, handouts, scene.js, Sessions 0–3 read-aloud/SAY) | ~60k | **Sonnet**, then Claude spot-checks | ~0.3–0.5M tokens |
| 3. Design critique | Season plan, Arc, Express Ending Kit, factions, NPCs, threads, Subway, clocks | 70 files | ~67k | **Opus** *(or Fable for the deepest read — costs more)* | ~0.4–0.9M tokens |
| **Total** |  |  |  |  | **≈ 1.2–2.4M tokens** |

\*Rough ranges, not measured: a subagent's total is its context re-read each turn, so it is several times the file size. For comparison, an earlier large review pass in another project cost about 2.6M. Cap each agent's final report (below) to keep the main session's context small.

## Rules every lane receives
- Report only. Do not edit, create or delete any file.
- Every claim needs `file:line` and a direct quote. No vague claims. Say "clean" where a category is clean.
- Do not propose safety-tool pages, GM acting or voices, or reintroducing anything listed under "Decided" below.
- **Decided (do not argue):** the GM never acts anything out (reads labelled NPC lines only); read-aloud is second person, present tense; one question per message with a setup line and a REACTION STOP; the Menace Rule (monsters are scary; comedy lives in the people); the city has no subway (water table about a storey down), the Subway is magical and appears with no fixed address, the Containment Suite is one floor deep, nobody boards a train before Arc IV; the campaign is 80 sessions in three seasons with one endgame (the Waking); the express-ending command is "wrap it N".
- Final report ≤ 1,500 words: a severity-ranked table (BLOCKER / HIGH / MEDIUM / LOW | file:line | quote | what goes wrong | exact fix), then a short "do not change" list.
- Do not reveal GM-private secrets in the report beyond a short label.

## Lane 1 prompt — Continuity (Sonnet)
```
You are auditing a tabletop-RPG campaign repository (The-Shadow-Exchange/) for continuity after many recent canon changes. Read docs/review/Canon-Change-Log-2026-11-20.md first, then 05-Sessions/Campaign-Arc.md, 05-Sessions/Season-1-Plan.md and 05-Sessions/Express-Ending-Kit.md. Then, for EACH canon decision in the change log and for each of the following, grep the whole repo (all *.md except 00-Canon/Blades-in-the-Dark-SRD.md, any _archive folder and docs/superpowers/) and list every place that contradicts it or is now stale:
 1. "subway" / "metro" / "train" / "transit" / "basement" / "sub-basement" / "cellar" / "underground" / "water" wording against the no-subway, one-floor-deep, appearing-Subway and no-boarding-before-Arc-IV decisions.
 2. Session numbers: the Thorne/Understudied unmasking is now Session 15 (was 12); the Away Job S16; the Offer S14; Vantage & Lowe S8–11; the Waking ~S78–80. Find every stale reference (Campaign-Arc, Truth Table, trigger rules, NPC and faction files, Foreshadowing, Plot-Threads, Active-Clocks).
 3. Clock values: Omen pacing (2/8 by S3, 3 at ~S11, 4 at S25, 6 end of Season 2, 7 ~S67, 8 only at the Waking), Subway Decay (6), Ministry Audit (4): find any file that gives a different schedule.
 4. Names and numbers: NPC names, Anchor items and dates, form numbers (Greta: Form 22-A, 31, 88-D), the coin code, rule counts (Wall of Rules: six rules, five hands + a sixth in red).
 5. Run Sheet ↔ body sync for 05-Sessions/Session-00-Prep.md to Session-03-Prep.md: every cue on the Run Sheet appears in its beat body and vice versa; every [IMAGE CUE]/[MUSIC CUE] filename exists in 11-Visuals/_Saved-Images or _Saved-Music, or is marked ❌ in 11-Visuals/ASSET-TODO.md.
Report per the rules.
```

## Lane 2 prompt — Player-facing leak check (Sonnet; Claude spot-checks)
```
You are checking what the PLAYERS can see against what must stay secret. Players see: ../The-Shadow-Exchange-Players/docs/*.md (their website), 11-Visuals/handouts/*.html, 11-Visuals/player-screen/scene.js and Player-Screen.html (the TV), and everything a GM reads aloud (🔊 READ ALOUD, 🗣 SAY, ❓ ASK, banners and card text) in 05-Sessions/Session-00-Prep.md to Session-03-Prep.md. Anything inside a 🔒 GM ONLY block is secret and is NOT a finding.
The secret list (do not repeat the secrets in your report; use labels): the Thorne/Understudied identity and the six-plus-three tells; the Casting Mask; the Architect; Section Chief Kress; that Stalls Holdings is an Apex shell; the cause of the Omen; the Subway's nature and its controller; Mara's corruption arc; Heirloom degradation patterns; the Spoilage/Detection/Decay clock names before they are introduced; Harlan's Wall photo meaning; anything from Sessions 4+.
Find every place a player could learn a secret early, plus: real brand names, text that tells the players an outcome before they act, and any read-aloud written in third person or past tense. Also run the rules in 00-Canon/Wiki-Update-Protocol.md (§ spoiler check) against the players' site.
Report per the rules.
```

## Lane 3 prompt — Design critique (Opus; Fable optional)
```
You are a senior designer of long-form story games (Blades in the Dark, Apocalypse World fronts, episodic TV structure). Read 05-Sessions/Campaign-Arc.md, Season-1-Plan.md, Express-Ending-Kit.md and Campaign-Current-State.md; 00-Canon/Campaign-Bible.md, Campaign-Bible-Appendix.md, Comedy-Playbook.md, Tone-and-Style.md, Mechanics-Teaching-Ladder.md; 02-Factions/, 03-NPCs/ (including GM-Private), 04-Locations/, 09-Threads/, 10-Generators/, 07-Clocks/, 08-Loot-and-Anchors/, 06-Scores/, 01-Crew/. The table: three experienced players new to Blades, weekly 2–3 hour sessions, 80 sessions in three seasons, one endgame.
Critique, with file:line and exact fixes:
 1. Pacing: where does a weekly table get too much, too little, or two big reveals in one session?
 2. Clue structure: for each major secret, are there at least three independent routes? Which secrets can a quiet or unlucky table miss?
 3. Twists and choices: which twists recolour what the players know, and which are random shocks? Do the six mid-arc climaxes and the Season 1 finale all offer a real choice with a real cost?
 4. Spotlight and agency: are the three PCs' heirloom, friend and rival threads used? Can the table reorder arcs without breaking the endgame?
 5. NPC mortality and churn: is any planned death unearned, any protected NPC overused, any new NPC redundant?
 6. Blades accuracy: check Tier, Rep, upgrade, Heat, Entanglement and advancement numbers in the plan against 00-Canon/Blades-in-the-Dark-SRD.md and flag any mismatch (do not flag intentional house rules marked as such).
 7. Tone: does the plan honour the Menace Rule (monsters are scary; comedy lives in the people), the dread budget and "laugh, then land"?
 8. The express-ending kit: does it work from every state, and is the state-to-ending table consistent with Campaign-Arc.md §6?
 9. What would you cut, what is missing, and what is the single biggest risk to this campaign finishing well?
Report per the rules, plus a ranked "top five changes" list.
```

## Launch (when the GM says so)
Say **"launch the review"** (all three lanes) or name lanes and models, for example "lane 3 only, with Fable". Lanes run in parallel and report back; results are triaged before anything changes.
