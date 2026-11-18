# Gemini Wiki Organization / Information-Architecture Review Prompt (player website)

Paste the block into Gemini (local file access; paths are repo-relative to `The-Shadow-Exchange/`, the player site source is `../The-Shadow-Exchange-Players/`). Claude triages the result per `Gemini-Triage-Protocol.md` — **Gemini suggests, Claude decides**, and every quote Gemini cites is `grep -F`-verified before anything is acted on (it has fabricated quotes before).

**Why now (2026-11-17):** the earlier reviews covered look/layout (two UI passes) and spoiler leaks. None looked at how the *information* is organized, and the audience was corrected: the three players are friends with 20+ years of tabletop RPG experience, new only to Blades in the Dark itself. Nervous-first-timer wording and all time estimates were just removed. This review checks whether the structure and content now fit that audience.

````
ROLE
You are an experienced tabletop-RPG game designer and technical writer who writes player-facing documentation (rulebook primers, session-zero packets, campaign wikis). You are reviewing the INFORMATION ARCHITECTURE and CONTENT of a small private campaign wiki. Be a skeptic and be specific.

THE READERS (this matters more than anything else)
Three friends who have played tabletop RPGs (mostly D&D-style games) for 20+ years. They are NOT nervous beginners and do not need reassurance or hand-holding. They have NOT played Blades in the Dark (a different system: action ratings, position & effect, stress, flashbacks, heat, downtime, a heist-planning loop). They will read this on a phone or laptop before Session 0, wanting to know: what is different from D&D, what do I need to decide, what do I send the GM. The GM wants the wiki short, scannable and respectful of their experience.

WHAT TO READ (all of it)
- ../The-Shadow-Exchange-Players/mkdocs.yml (the nav and page titles count)
- ../The-Shadow-Exchange-Players/docs/*.md (15 pages, about 11,000 words: Home, Quick Start, Character Creation Guide, Before Session 0, Official Resources, Rules and Mechanics, Downtime Guide, Glossary, FAQ, What Kind of Game, Our Lair, Known Contacts, Session 0 Agenda, Session Recaps, The Anchor Ledger)
- Previous reviews (do NOT re-raise what was already decided): docs/review/Gemini-UI-Triage-Log-2026-11-16.md, docs/review/Gemini-UI-Second-Pass-Triage-Log-2026-11-17.md, docs/review/Gemini-Spoiler-Triage-Log-2026-11-17.md
- Live site (open if you can): https://delonsampaio.github.io/The-Shadow-Exchange-Players/

DECISIONS ALREADY MADE (do not argue with these)
- No safety-tool or content-warning pages (the GM decided against them).
- No time estimates anywhere; no "nervous first-timer" tone.
- Session 0 happens before the campaign pages fill up; the Campaign tab (Session Recaps, Anchor Ledger) is intentionally near-empty until play starts.
- Spoiler discipline is handled separately; do not suggest adding GM secrets. Do not name any hidden campaign secret in your report.

DO THIS
1. MAP IT. In a table list each page: purpose in one line, word count (approximate), who it is for, and the single question it answers. Flag any page that answers no distinct question.
2. OVERLAP. Find content stated in more than one place (rules, character-creation steps, the 12 actions, stress/trauma, Heat/Downtime, the Anchor Ledger, "what to send the GM"). For each, say which page should own it and what the others should do (link, one-line summary, or delete). Quote the repeated sentences with page and line.
3. GAPS FOR THESE READERS. What would an experienced D&D player need that is missing or buried? Examples to consider (only raise if truly missing): a short "how Blades differs from D&D" section, the core loop (Free Play → Score → Downtime → Heat), what a Resistance roll is, how flashbacks replace planning, and what the GM expects them to do before Session 0. Rank by how much confusion it would prevent.
4. TOO MUCH. Which pages or sections are longer than these readers need? Give a concrete cut (which headings or paragraphs) and the word-count saving.
5. ORDER AND NAVIGATION. Judge the 5 top-level tabs (Home / Start Here / The Rules / The World / The Campaign) and the order of pages inside them. Is anything filed in the wrong tab (for example Glossary/FAQ under The Rules, Session 0 Agenda under The Campaign)? Is the 3-step "Start Here" path still the clearest route? Propose the final nav as a YAML block ready to paste into mkdocs.yml, and say what changes and why.
6. HOME PAGE. Does the Home page tell these readers what to do first, quickly? What would you remove or move?
7. TONE. Find sentences that still talk down to experienced players or reassure beginners (quote them with page and line) and give a one-line rewrite for each.
8. CONSISTENCY OF TERMS. Do pages use different names for the same thing (for example crew/team/firm, Anchor Item/Heirloom, Heat/Detection)? List the mismatches with the preferred term.

DELIVERABLES (in this order)
1. A one-paragraph VERDICT and a scorecard (Findability, Redundancy, Fit for veterans, Completeness, Navigation, Tone) each /10.
2. The page map table from step 1.
3. A severity-ranked table: Severity (HIGH/MEDIUM/LOW) | Page(s) + line | The problem (with a direct quote) | Concrete fix (exact replacement text or exact nav YAML, ready to paste).
4. The proposed nav as a YAML block.
5. A short "Do not change" list of things that already work.

RULES
- Do NOT edit files. Report only.
- Every finding needs file:line and a direct quote. No vague claims. Do not invent findings to look thorough; if a category is fine, say so plainly.
- Do not suggest safety-tool pages, time estimates, beginner reassurance, or anything that reveals campaign secrets.
- Do not quote from the GM-side repo (03-NPCs, 05-Sessions, 00-Canon); the only sources are the player site and the review logs listed above.
````
