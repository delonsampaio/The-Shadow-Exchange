# Gemini Spoiler-Check Prompt (player site vs GM secrets)

Paste the block into Gemini (it has local file access; paths are repo-relative to `The-Shadow-Exchange/`; the player site source is `../The-Shadow-Exchange-Players/`). Claude triages the result per `Gemini-Triage-Protocol.md` — **Gemini suggests, Claude decides** (verify every flag against the source; many "leaks" are things players are *meant* to know).

Mechanical pre-check already done by Claude (2026-11-17): whole-word search of the live site **and all 8 commits of git history** for Understudied / Mimic / Casting Mask / Architect / Kress / Stalls / Barghest / Wraith / Thorne / Omen — **zero hits**. This prompt is for the *subtle* leaks a keyword search can't find.

````
ROLE
You are a ruthless, adversarial spoiler-checker. Imagine you are one of three players in a Blades in the Dark campaign called "The Shadow Exchange". You are smart, curious, and you will read every page of the player website before Session 0 — and you will try to work out the GM's secrets from it. Also play the GM who built the secrets and wants to know exactly what a sharp reader could learn.

THE PLAYER SITE (read ALL of it)
../The-Shadow-Exchange-Players/docs/*.md, ../The-Shadow-Exchange-Players/mkdocs.yml (page titles and nav labels count!), ../The-Shadow-Exchange-Players/docs/stylesheets/extra.css (comments only), and look at the three images in ../The-Shadow-Exchange-Players/docs/assets/ (hero-curios.jpg, consequence.jpg, greta-fenn.jpg) plus any alt text / captions / file names that reference them.

THE GM SECRETS (read these first; they are the answer key — NEVER copy secret details into your report beyond a short label such as "Secret: Thorne")
- 00-Canon/Wiki-Update-Protocol.md  (the "never publish" list)
- 05-Sessions/Campaign-Arc.md  (truth table, trigger rules, endgame)
- 03-NPCs/Active/*.md  (every "GM-private" / "GM ONLY" line)
- 04-Locations/The-Subway/Overview.md and Living-Subway.md  (what the Subway is; why the crew can see it)
- 00-Canon/Heirloom-Degradation-Patterns.md  (never named to players)
- 05-Sessions/Session-00-Prep.md … Session-03-Prep.md  (every "🔒 GM ONLY" block)
- 00-Canon/Campaign-Bible-Appendix.md

WHAT PLAYERS ARE *ALLOWED* TO KNOW (do NOT flag these)
The premise and tone; the firm "Curios & Chronicles" and its bookshop front; the Ministry as license-holder; Apex Aegis as a rival private firm; the Twice-Born as a concept; Resonance; Anchor Items and the Anchor Ledger; the crew's lair rooms and the six Wall of Rules (but not the Rule 6 backstory); Gerald/Merton/Thorne/etc. are NOT yet known and must not appear. The Subway must not be named or described before Session 2.

DO THREE PASSES
1. LITERAL LEAKS — a secret stated outright, or any named NPC/location/object the players have not met.
2. INFERENCE LEAKS — could a clever player combine two or three innocent statements and deduce a secret? (Example of the kind of thing I mean: a Ministry description that is oddly specific about "not monolithic", paired with an NPC blurb.) Say exactly which sentences combine.
3. SIGNAL LEAKS — tone, emphasis, an odd choice of detail, an image that contains a clue (e.g. a silhouette in a window), a page title or nav label, an alt text, a quote on the Home page, a rule that tells players to do something that would wreck a planned reveal.

SPECIFIC QUESTIONS I NEED ANSWERED
a) Docs/Our-Lair.md names "Director Vance" as the crew's direct supervisor and says the Ministry is "not as monolithic as they present themselves." Session-00-Prep lists Vance among "too senior / GM-private" NPCs. Is naming him (and that phrase) a leak, a hint, or fine? Recommend keep / soften / remove.
b) docs/assets/greta-fenn.jpg shows a dark shape in a broken window behind Greta. Does it give away a monster, a Session 1 target, or anything else? Keep / crop / replace.
c) Does anything on the Home page or in the FAQ promise or imply a twist, a betrayer, or an "ally who isn't"?
d) Does any page tell players to build a character/Friend/Rival that collides with a reserved NPC?

DELIVERABLES (in this order)
1. A one-paragraph VERDICT: safe to publish as is / minor fixes / must fix.
2. A table of findings, most severe first: Severity (BLOCKER = reveals a secret outright; HIGH = a sharp reader can deduce one; MEDIUM = a hint or tone leak; LOW = nitpick) | Where (file:line, or image name) | The exact quote | Which secret (label only) | Why it leaks | Suggested rewrite or removal.
3. A list of pages you read and judged CLEAN (so I know what was covered).
4. Any false-positive risks: things that look like leaks but you believe players are meant to know — and why.

RULES
- Do NOT edit any files. Report only.
- Do not flag things on the allowed list.
- Be specific: file:line and a direct quote for every finding. No vague "might be a spoiler".
- If you find nothing in a category, say so plainly; do not invent findings to look thorough.
````
