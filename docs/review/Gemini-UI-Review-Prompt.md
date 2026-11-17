# Gemini UI/UX Review Prompt (player website)

Paste the block into Gemini. It reads the screenshots in `docs/review/ui-screenshots/` and the source in `../The-Shadow-Exchange-Players/`; it can also open the live site. Claude triages the result per `Gemini-Triage-Protocol.md` — Gemini suggests, Claude decides.

````
ROLE
You are a senior product/UX designer who specializes in onboarding documents for tabletop-RPG groups, with strong CSS and MkDocs Material skills. Review the look, readability, and usability of a small public player website.

WHAT YOU'RE REVIEWING
- Live site (public): https://delonsampaio.github.io/The-Shadow-Exchange-Players/  (open it if you can browse; otherwise use the screenshots and source below)
- Source (local, sibling folder): ../The-Shadow-Exchange-Players/  — read mkdocs.yml, docs/stylesheets/extra.css, docs/index.md, and a few pages in docs/ (Quick-Start.md, Character-Creation-Guide.md, Before-Session-0.md, Our-Lair.md, FAQ.md, Glossary.md)
- Screenshots (local, repo-relative to The-Shadow-Exchange/): docs/review/ui-screenshots/ — home-desktop.png, home-phone-500px.png, quick-start-desktop.png, known-contacts-desktop.png
- Technology: static site, MkDocs Material 9, GitHub Pages, no server. Fixes MUST be implementable with CSS, mkdocs.yml, or Markdown/HTML in the docs (no custom backend; avoid custom JavaScript unless there's no alternative).

CONTEXT
- Audience: 3 adult players who have played D&D/Pathfinder but NEVER Blades in the Dark and are new to roleplaying. They will read this mostly on PHONES, the night before Session 0.
- Campaign tone: industrial-occult noir (rain-slick night, amber vs cold blue light, century-old brick) that is also openly FUNNY (think the TV show Supernatural plus a little Scooby-Doo). The design should feel atmospheric but never get in the way of reading.
- Goal of the site: a nervous first-timer can (1) understand the game in ~5 minutes, (2) build a character in ~45 minutes, and (3) know exactly what to send the GM — without getting lost.
- Constraints: GM-secret information must never appear; the site credits Blades in the Dark (CC BY 3.0) in the footer; the GM wants to keep things simple to maintain.

EVALUATE (use screenshots + source; note anything you could not verify)
1. FIRST-5-SECONDS TEST (Home): can a first-timer tell what this is, what to do first, and how long it takes? Is the primary action obvious?
2. VISUAL HIERARCHY & TYPOGRAPHY: headings (Oswald, uppercase), body (Inter), quotes (Lora italic). Sizes, weights, line length, line height, spacing. Is the amber used with restraint?
3. CONTRAST & ACCESSIBILITY: WCAG AA contrast for text, links, buttons, table headers, tab labels (small uppercase), in BOTH dark and light schemes; focus states; alt text; reliance on color alone; reduced-motion; font loading (Google Fonts @import).
4. MOBILE ERGONOMICS: tap-target sizes, header/title truncation, hero height, cards stacking, table readability (e.g., wide tables), floating "portrait" images, long pages and scroll depth, sticky elements.
5. NAVIGATION & INFORMATION ARCHITECTURE: top tabs (Start Here / The World / The Rules / The Campaign), sidebar, table of contents, search, "Next step" footers, previous/next links. Is the order right for a nervous beginner? Any dead ends?
6. TONE & BRAND FIT: does it feel noir AND welcoming/funny? Where does it feel generic Material, too grim, or cluttered? Use of imagery (hero image of the shop exterior; portrait of Greta Fenn; the cat Consequence).
7. PERFORMANCE: image weights (hero ~600 KB), fonts, anything that would feel slow on a phone.
8. CONSISTENCY & POLISH: spacing, borders, card/table styling, callouts, the Home page vs inner pages, light-mode appearance.

DELIVERABLES (in this order)
1. A one-paragraph overall verdict and a 1–10 score for: First-impression, Readability, Mobile, Accessibility, Navigation, Tone/brand, Polish.
2. A severity-ranked issue table: [BLOCKER / HIGH / MEDIUM / LOW] | location (page or file:line) | what a user experiences | concrete fix **as exact CSS, mkdocs.yml, or Markdown** (ready to paste).
3. "5 quick wins" (≤ 10 minutes each) with paste-ready code.
4. "3 bigger ideas" that would meaningfully improve the experience for first-timers (e.g., a 'Your first 50 minutes' progress path, a printable one-page cheat sheet, a visual 'how a roll works' diagram), each with a sketch of how to build it within MkDocs Material.
5. "Do not change" list: the things that already work well.
6. A short accessibility checklist the GM can re-run after each update.

RULES
- Do not edit any files; only report.
- Judge as a NEW player on a phone, not as a designer. If something needed explaining, that's a finding.
- If you cannot open the live site or an image, say so explicitly rather than guessing.
- Prefer fewer, higher-impact changes over a long list of nitpicks. Anything that makes reading harder is a higher priority than anything that merely looks nicer.
- Keep each fix small and safe; the site must keep building with `mkdocs build --strict`.
````
