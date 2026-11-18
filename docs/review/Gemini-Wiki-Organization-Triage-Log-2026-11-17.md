# Gemini Wiki Organization Review — Triage Log (2026-11-17)

Prompt: `Gemini-Wiki-Organization-Review-Prompt.md`. Response saved by the GM as `Gemini UI Triage Log.odt` (Downloads). Protocol: **Gemini suggests, Claude decides** (`Gemini-Triage-Protocol.md`).

**Verification done**
- 25 quoted passages `grep -F`-checked against the live site source: **all 25 exist** (no fabricated quotes this round).
- Every rules claim checked against the official SRD (bladesinthedark.com): action-roll, planning-engagement, resistance-armor, progress-clocks, effect, advancement.
- Local strict build (`mkdocs build --strict`) passes.

**Scores (Gemini):** Findability 7 · Redundancy 4 · Fit for veterans 6 · Completeness 7 · Navigation 7 · Tone 7.

## Applied
| Finding | Decision |
|---|---|
| GAP-1 Engagement Roll never explained | **Applied** (own wording, SRD-verified): six plans + detail, Load, dice modifiers, 6 / 4–5 / 1–3 / critical → position. In Rules → Core Loop. |
| GAP-2 bonus-die cap | **Applied** (SRD: one Assist die + one Push-or-Devil's-Bargain die). |
| GAP-3 Progress Clocks never defined | **Applied** (4/6/8 segments; Effect Limited 1 / Standard 2 / Great 3; danger clocks tick 1–3). New Rules section. |
| GAP-4 Armor | **Applied, but Gemini's text was WRONG** — it said Armor + Resistance stack on one hit. SRD: armor is *instead of* rolling to resist. Used SRD wording. Also added Armor + Progress clock to Glossary. |
| GAP-5 Character XP triggers | **Applied** (SRD triggers: playbook, beliefs/drives/heritage/background, Vice/Trauma; 1 XP, 2 if "a lot"). Downtime Guide → Advancement. |
| Duplicate 8-item "what to send" list (3–4 places) | **Applied**: Before Session 0 owns it; Character Creation and Session 0 Agenda now link to it; the duplicate list inside Before Session 0 removed (copy-paste block kept). |
| Home duplicates ("What kind of game", "Shape of a session") | **Applied**: replaced by a 3-line Tone paragraph; the loop now lives in Rules. |
| Tone (12 passages) | **Applied** (reworded or cut): Quick Start intro/"Don't worry about…", Home reassurance, Character Creation "Last notes", Before Session 0 "silly practice roll", Official Resources "great for beginners", Glossary header, Session 0 Agenda "no wrong crew build"/"No one is graded", Our Lair Practical Stuff, What-Kind-of-Game "Read this before…". |
| Terms: "skill" vs "action", "action group" vs attribute | **Applied.** |
| Nav: The World order, "Playbook Sheets" label | **Applied** (Our Lair first, What Kind of Game last; label "Playbook Sheets & Resources"). |
| Time estimates in progress bars `(5m)(45m)(5m)` | **Found by Claude** (grep missed "5m"): removed from all 3 pages. |
| Duplicate Resistance/Flashback bullets in Rules; Heat parenthetical in Downtime | **Applied** (cross-references). |
| Session 0 Agenda "What you leave with" | **Applied** (cut; "Session 1 begins the work" kept). |

## Not applied / decided against
| Finding | Reason |
|---|---|
| Retire FAQ (11 of 13 answers duplicate other pages) | **Applied (GM decision 2026-11-17).** FAQ page deleted, nav and links removed; the two unique answers (AI Co-GM + TV, missing a session) moved to Session 0 Agenda → Logistics. |
| Glossary: cut to 8 terms, alphabetize | **Rejected** — veterans new to Blades need those definitions; kept, only skill→action fixes + 2 additions. Alphabetizing skipped (several entries share a line). |
| "Delete What-Kind-of-Game lines 44–81" | **Rejected** — "The cover-up" / "What you are selling" carry unique tone guidance ("notice what you feel"). Kept. |
| Rename Cursed Family Heirloom → Cursed Heirloom | **Applied (GM decision 2026-11-17)** on the player site and in the GM repo (Core Instructions, Campaign Bible Appendix, Plot Threads, PC template, PC Character Creation Guide). Historical plan/log files left as written. |
| "Our-Lair: Twice-Born / damp manila envelope" rewrite | Not needed — the site already says "damp manila envelope" (Our Lair, Glossary). No new leak, no change. |
| teammate → crewmate | Skipped as trivial. |

## Do-not-change list (Gemini, accepted)
D&D comparison table on Home; playbook-to-D&D analogues in Character Creation; Rules action examples; copy-paste GM template; "ignore on the official sheet" section; in-world writing (Our Lair, Known Contacts, vignettes).
