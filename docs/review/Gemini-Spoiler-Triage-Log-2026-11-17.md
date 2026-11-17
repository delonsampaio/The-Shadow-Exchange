---
entity_type: Review_Log
last_updated: 2026-11-17
purpose: "Triage of Gemini's spoiler check of the public player site (Gemini suggests, Claude decides)."
---

# Gemini Spoiler-Check Triage — 2026-11-17

**Claude's own mechanical pre-check (before Gemini):** whole-word search of the live site and all 8 commits of git history for the secret terms → zero hits.
**Gemini's verdict:** "safe after minor fixes (0 blockers, 1 high, 3 medium, 3 low)." **Claude's verdict after verification:** safe; four small edits made; the one HIGH was a canon gap, not a leak.

## ⚠ Gemini quoted text that does not exist
Five cited quotes were **not found** on the site, in the campaign repo, or in the site's git history (checked with `grep -F`): "Pay attention to who sends them. Notice that some of the jobs don't make sense" · "a grieving widow who happens to have too many teeth" · "Dogs with strong opinions about plot relevance" · "a two-minute walk from the shop" (the page says **forty minutes outside the city**) · "Jeren, a bluecoat archivist". Several line numbers were also wrong. Findings built on those quotes were rejected.

| Gemini finding | Verified? | Decision |
|---|---|---|
| **HIGH** — "a market the Ministry doesn't know exists" hints at the Subway | Quote is real, but it is the **Session 0 pitch read-aloud verbatim** (Home page). | **Keep.** The real gap: *who has the crew sold to before Session 2?* → **canon added** to `The-Subway/Overview.md` ("Before the First Visit": nervous middlemen + dead drops; the Fence's stall is the market's first real face). Also softened `Rules-and-Mechanics.md` "market vendor" → "someone who buys or sells quietly". |
| MEDIUM — "not as monolithic as they present themselves" telegraphs the Ministry's hidden factions | ✅ real (`Our-Lair.md:82`) | **Fixed** → "very good at not asking where things come from." |
| MEDIUM — "Pay attention to who sends them…" | ❌ **quote does not exist** | Rejected. (Real text at `Our-Lair.md:68` is neutral.) |
| MEDIUM — Friend/Rival step has no guardrail vs. reserved NPCs | ✅ real gap | **Fixed**, with canon-correct wording: Vance too senior; keep Ministry/Apex contacts at clerk level; Harlan OK as Friend, not Rival. (Gemini's draft would have banned Harlan as a Friend, which Session-00-Prep allows.) |
| MEDIUM — Harlan listed as a known contact vs. "debuts Session 4" | Partly (the diner is 40 min out, not 2) | **Kept on the site**; GM note added to `Harlan-Okafor.md`: public from S0, **on stage** S4, keep offstage until then. |
| LOW — "grieving widow … too many teeth" echoes Mabel | ❌ **quote does not exist** | Nothing to change. |
| LOW — repeated "sincere dog" joke defuses the Gerald reveal | Half real: `FAQ.md:36` said "a very sincere dog"; the `What-Kind-of-Game` quote doesn't exist | **Softened** FAQ → "a creature with strong opinions." |
| LOW — Greta photo shows a dark shape in the window | ✅ | **Keep** (reads as a gag; Gemini agreed). |
| "train door" simile in `Our-Lair.md:25` | optional | **Keep** — it is the Session 0 read-aloud. |
| Rule 6 / lease / red-ink page / AM radio / heirloom / Twice-Born XP | Gemini's own false-positive list | **Agreed — all intentional.** |

Net: 4 site edits (Our-Lair, Rules, FAQ, Character-Creation) + 2 canon notes (Subway Overview, Harlan card). Nothing committed yet.
