# Gemini Dashboard UI/UX Review Prompt

Paste the block into Gemini (it reads the screenshots and the source locally). Claude triages the result per `Gemini-Triage-Protocol.md` — Gemini suggests, Claude decides.

````
ROLE
You are a senior UX/product designer who specializes in live-play tools for tabletop-RPG game masters (GM screens, VTT sidebars, status HUDs) and who is strong with Tailwind/React single-file apps. Review the layout, readability, and usability of a GM-only dashboard used DURING live sessions.

WHAT YOU'RE REVIEWING
- The dashboard source (local, repo-relative to The-Shadow-Exchange/): 11-Visuals/GM-Dashboard.html (React 18 + Tailwind + Babel from CDNs, one file, state in localStorage, no server)
- Its live feed: 11-Visuals/dashboard-feed/push.sh and feed.js (the AI Co-GM appends update ops; the dashboard polls every 2 s and shows a "Co-GM Updates · live" log and a "Now / Next" bar)
- Screenshots (repo-relative): docs/review/ui-screenshots/dashboard-1080p-visible.png (what the GM sees without scrolling on a 1920x1080 monitor) and docs/review/ui-screenshots/dashboard-full-page.png (the whole page)
- Context docs: 00-Canon/Session-Boot.md §2b (how the Co-GM updates it), 00-Canon/Mechanics-Teaching-Ladder.md (new players), 05-Sessions/Session-00-Prep.md and Session-01-Prep.md (what happens at the table)

CONTEXT
- The GM runs a Blades in the Dark campaign for 3 players who have never played Blades. The GM uses a GM monitor (1920x1080, 1–2 m away, dim room) showing this dashboard; a SEPARATE shared TV (never this screen) shows players the scene art. 
- An AI Co-GM (Claude) now keeps the dashboard UPDATED AUTOMATICALLY every beat. So the GM mostly READS it at a glance and only occasionally clicks (to correct or override). It must also hold GM-SECRET info (Omen clock, Thorne "tells" tracker, Heirloom degradation patterns) that must never be visible to players if someone glances at the GM screen.
- Tracked: crew Heat/Coin/Rep/Wanted/XP/Tier/Hold; per-PC Stress (9), Harm (3 slots), Trauma, XP, Vice, Heirloom+pattern, Friend, Rival; clocks (Detection, Surge, Spoilage, Subway Decay, Omen[secret], Audit, Corruption); NPC intel; faction standing (−3..+3); Anchor Ledger; GM-secret Thorne tells; running gags/table canon; "Mechanics taught" tracker; Now/Next beat bar; live Co-GM update log.
- Constraints: stay a single static HTML file (React/Tailwind via CDN; avoid new dependencies); changes must be implementable as JSX/Tailwind class changes; keep the feed protocol (window.DASH_FEED / push.sh) working; don't break localStorage persistence (SAVE_VERSION).

EVALUATE
1. GLANCEABILITY (the 3-second test, from 1–2 m in a dim room): what is the single most important thing and is it the most prominent? Can the GM see, without scrolling, the 6 things they need mid-scene (current beat + next cue, each PC's Stress/Harm, the active clocks, who just changed, public vs secret status, any alert)?
2. INFORMATION HIERARCHY & DENSITY: sizes, weights, grouping, whitespace, what's wasting space (large empty regions, oversized cards) vs. too cramped. The "Position / Effect quick ref" and "Mechanics taught" panels: are they worth their space and in the right place?
3. LEGIBILITY & CONTRAST: text sizes (there is a lot of small mono text), dim greys on near-black, WCAG AA contrast, colour semantics (red/amber/emerald/purple) and whether colour alone carries meaning; colour-blind safety of the stress/harm/clock fills.
4. CLOCK DESIGN: the circular clocks at the current size/placement; readability at distance; is "n/N" clear; should near-full clocks warn visually? Is the secret Omen clock appropriately signposted?
5. LIVE-FEED UX: is it obvious when the Co-GM changed something? (flash/highlight of changed fields, the update log size/placement, undo/override affordances, a "last updated" indicator, what happens if the feed stalls). Should the GM be able to pin/dismiss alerts?
6. PRIVACY: how to make it safe if a player glances at the GM screen (e.g., a one-key privacy blur of secret panels, collapsing secrets by default, calmer labelling of secret items).
7. INTERACTION: click target sizes for occasional manual corrections, hover-only affordances, keyboard shortcuts, accidental-click risk (e.g., stress pips, harm buttons, clock segments), mobile/tablet fallback (a GM on a tablet).
8. VISUAL STYLE: does it feel like a noir command console that suits "Industrial-occult noir"? Polish, consistency, anything garish or generic.
9. RESILIENCE: behaviour offline (CDN dependence), after refresh, with a stalled feed; performance.

DELIVERABLES (in this order)
1. Overall verdict + 1–10 scores for: Glanceability, Hierarchy, Legibility, Live-feed UX, Privacy, Interaction, Style, Resilience.
2. A severity-ranked table: [BLOCKER / HIGH / MEDIUM / LOW] | where (panel or file:line) | what the GM experiences | concrete fix as exact Tailwind/JSX (ready to paste).
3. "A better layout": a text wireframe (ASCII) of a 1920x1080 "cockpit" layout that keeps the 6 must-see items above the fold, with proposed column widths in Tailwind grid terms.
4. "5 quick wins" (≤10 minutes each) with paste-ready code.
5. "3 bigger ideas" (e.g., changed-field flash animation, privacy blur toggle with a hotkey, an alert bar for clocks about to fill, an end-of-session summary view that helps write the recap) with how to build each inside this single file.
6. "Do not change" list.

RULES
- Do not edit files; only report. If you can't open a screenshot or file, say so rather than guess.
- Judge as a GM at the table in a dim room, not as a designer at a desk. Prefer fewer high-impact changes. Anything that makes the live feed harder to trust is higher priority than anything that merely looks nicer.
- Keep each fix small and safe.
````
