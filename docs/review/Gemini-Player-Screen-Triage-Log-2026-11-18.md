# Gemini Player-Screen Review — Triage Log (2026-11-18)

Prompt: `Gemini-Player-Screen-Review-Prompt.md`. Protocol: **Gemini suggests, Claude decides**. Display facts supplied by the GM after the review: **75-inch TV, about 10 ft from the table** (Gemini re-ran its size maths for that; it upgraded legibility from 6/10 to ~7.5/10 and shrank the fix list).

**Verification done**
- Every file reference/value Gemini cited was checked against `Player-Screen.html`: clock label `1.5vh #a1a1aa`, now-playing `1.6vh #71717a` with no shadow, blank screen `#3f3f46/#52525b` with no fade, banner `white-space:nowrap`, silent clock redraw on every rev, unfilled slices `rgba(20,20,24,.78)`. **All accurate.**
- Two Gemini claims corrected: (1) the banner would clip at ~22 characters, not ">~12" (15vh Impact is ~7.5vh per character on a 178vh-wide screen); (2) its `.sheet{overflow:hidden}` fix would silently cut off text — rejected.
- Built in a scratchpad copy first and rendered at 1920×1080 in headless Chrome: main scene, recap card, blank screen, banner (long and short text), full Meridian scene with clocks/caption/label/banner. Pulse logic and the crew-strip key filter tested by driving `apply()` directly.

**Scores (Gemini):** Legibility 6→7.5 · Glanceability 7 · Pacing cost 9 · Spoiler safety 9 · Fit 8 · Consistency 9.

## Applied (`11-Visuals/Player-Screen.html`)
| Gemini finding | Decision |
|---|---|
| Clock label too small/dim (`1.5vh`) | **Applied:** `2vh`, bold, `#f4f4f5`, shadow. Dial stays `8vh` (fine at 75"/10 ft). |
| Unfilled clock slices vanish on dark scenes | **Applied:** `rgba(255,255,255,.16)` + a faint outer ring. |
| Now-playing too dim, no shadow, can collide with caption | **Applied:** `1.9vh`, `#a1a1aa`, shadow, `max-width:28vw` + ellipsis; caption narrowed to `62vw`. |
| Blank title screen near-invisible, snaps off | **Applied:** amber title, `#a1a1aa` sub-line, 1 s fade. |
| Caption/subcaption wash out over bright floors | **Applied:** stronger shadow, subcaption `#f4f4f5`. |
| Contract card Courier too thin | **Applied:** `2.7vh`, weight 600. |
| Banner can clip long phrases | **Applied:** `width:max-content; max-width:90vw; wrap; centered` (verified a 23-char phrase fits one line). |
| **BUILD** "Previously…" recap card | **Applied:** new card style `recap` with optional `bullets`; rule = populate **only from the public player recap**; cleared by the first beat. |
| **BUILD** clock-tick pulse (client-side, zero fields) | **Applied:** a clock whose `cur` rises pulses for 1.2 s; first load and unchanged clocks never pulse. |
| **MAYBE** nullable crew strip (Heat/Coin/Rep) | **Built, optional:** top-left, null by default, three keys only (extra keys ignored — tested). |

## Not applied
| Finding | Reason |
|---|---|
| Position/Effect tag | **SKIP** (Gemini + Claude): 1.5 s poll lag and a mid-beat write per roll; belongs on a printed table card. Claude's own suggestion — withdrawn. |
| "Where we are" objective line | **SKIP:** duplicates the subcaption, feels like a quest tracker, goes stale. |
| Roll outcome, Devil's-Bargain marker, turn cue, initiative, per-PC Stress/Harm, NPC list, permanent map | **Rejected** (clutter / sub-beat pacing / already on sheets). |
| `.sheet { overflow:hidden }` | **Rejected:** hides overflow text. Instead: keep cards to ~8 short lines (documented in `CoGM-Core-Instructions.md`). |

## Follow-up offered
Printed one-page **Position & Effect** table card for the table (the thing the Position/Effect tag was meant to teach).
