# Gemini UI/UX Second-Pass Prompt (player website)

Paste the block into Gemini (local file access; paths are repo-relative to `The-Shadow-Exchange/`). Screenshots are in `docs/review/ui-screenshots/round2/` (taken 2026-11-17 from the **live** site: 5 pages × desktop 1440 and phone 500px — headless Chrome can't render below ~500px, so "phone" = 500px). Claude triages the result per `Gemini-Triage-Protocol.md` — **Gemini suggests, Claude decides**.

What changed since the first review (`Gemini-UI-Triage-Log-2026-11-16.md`): nav reordered, light-mode contrast fixed, 3-step progress bar + print stylesheet added, hero/Greta/cat images re-cropped (generator logo removed), grey Consequence photo on the FAQ, Session 0 time estimates removed.

````
ROLE
You are a senior product/UX designer specialising in onboarding documents for tabletop-RPG groups, with strong CSS and MkDocs Material skills. This is a SECOND PASS: a first review was done and fixes were applied. Be a skeptic: verify, don't assume.

WHAT TO LOOK AT
- Screenshots: docs/review/ui-screenshots/round2/*.png (home, Quick-Start, Before-Session-0, Session-0-Agenda, FAQ; each desktop + phone-500px).
- Live site (open it if you can; toggle light/dark with the moon icon and test at phone width): https://delonsampaio.github.io/The-Shadow-Exchange-Players/
- Source: ../The-Shadow-Exchange-Players/docs/stylesheets/extra.css, ../The-Shadow-Exchange-Players/mkdocs.yml, and the pages in ../The-Shadow-Exchange-Players/docs/.
- Previous round: docs/review/Gemini-UI-Triage-Log-2026-11-16.md (what was already fixed or rejected — do NOT re-raise rejected items unless you have new evidence).

THE READER
A 28-year-old who has played some D&D but never Blades in the Dark, reading on a phone the night before Session 0, wanting to know: what do I read, what do I do, what do I send the GM?

DO THIS
1. VERIFY the first round's fixes actually landed: nav order (Start Here steps 1→2→3), light-mode contrast (AA), the 3-step progress bar, mobile layout, tab label size, the print/Quick Start handout. For each: FIXED / PARTLY / NOT FIXED + evidence.
2. FIRST-TIME FLOW: from Home, can a nervous newcomer tell in 5 seconds what to do first? Count taps from Home to "Before Session 0". Is the 3-step path still the clearest thing on the page?
3. IMAGES: do the hero, FAQ cat photo (float-right on desktop, cropped banner on phone) and Greta photo look intentional and well-cropped now? Any awkward crops after the logo removal?
4. CONSISTENCY: headings, spacing, link colors, callouts and tables across the 5 pages — anything that looks like a different site?
5. PHONE: any horizontal scroll, tiny tap targets (< 44px), long tables that squeeze, sticky-header overlaps, or text that needs zoom.
6. Anything a first-timer would find confusing about the 5 top-level tabs (Home / Start Here / The Rules / The World / The Campaign) when the Campaign tab is still mostly empty before Session 1.

DELIVERABLES (in this order)
1. A one-paragraph VERDICT and a scorecard (Glanceability, First-time flow, Legibility, Mobile, Consistency, Style) each /10.
2. A severity-ranked table: Severity (BLOCKER/HIGH/MEDIUM/LOW) | Page + viewport | What the player experiences | Concrete fix (exact CSS or Markdown, ready to paste).
3. A "FIRST-ROUND FIX VERIFICATION" list (item → FIXED / PARTLY / NOT FIXED).
4. A short "Do not change" list of things that already work.

RULES
- Do NOT edit files. Report only.
- Give exact selectors/values for any CSS suggestion; verify they don't already exist in extra.css.
- Do not invent problems to look thorough; if a category is fine, say so.
- Do not suggest adding safety-tool / content-warning pages (the GM has decided against them).
````
