# Mock 0 report (2026-11-24): triage and what was done

Source: the GM's Session 0 mock findings report (no blockers; 10 medium, the rest low). Every item was checked against the files before acting. Session 1 prep was not touched (mock 1 may be running).

## Fixed in `05-Sessions/Session-00-Prep.md`
| # | Finding | Fix |
|---|---|---|
| 1 | 3a city SAY too long; subway seed buried | Split into one short line per district (river and the cliff Overhang added to match the map); the no-subway / water line is now its own SAY |
| 2 | 3b "You push a specific coin…" narrates the players | Now "It opens for one thing only: the right coins, in the right order — a code only the people in this building know —" |
| 3 | 3d "another state" ambiguous | Now "a signal that sounds like it comes from very far away" |
| 4 | 3f three "SAY (first)" lines and two "last" | Duplicate swap line removed; labels now (1), (2), (3); upgrades start "Next:" |
| 5 | 3f unlabelled "Recommendation" line, conflicts with the menu | Now a GM-only line: if asked, Anointed |
| 6 | ASK + pause inside READ ALOUD quotes (3c, 3d) | Read-aloud closed before the question; a "continued" READ ALOUD block follows |
| 7 | Beat 4 layout (nested ask, menu order, redirect list last) | Rebuilt: reserved names and redirects first; Friends → favourite contact → Rivals (stall menu after the ask) → Heirlooms |
| 8 | Beat 5 double labels | "Player N — SAY … then ASK …" |
| 9 | 3f upgrade order matters but the table isn't told | Ask "which two, and which one comes first?"; GM note on the order and on asking both follow-ups for Quality + Training |
| 10 | Favourite contact: civilians have no faction | Default by district: Old City → Harrow & Sons · the Docks → Castellan Retrieval · the Meridian or Fairground → Meridian Group · a hunter or anywhere else → Hunter Underground (**GM may change**) |
| 11 | Beat 2 nickname for Player 3 easy to miss | Moved out of the quote block; spells out who names whom, including Player 1 naming Player 3 |
| 12 | 4b resist: attribute actions not on hand | SAY lists Insight's four actions; the Table Card now lists all three attributes' actions (PDF rebuilt, still one page) |
| 13 | 4b 4–5 has two costs; Prowess doesn't fit a torn page | One cost (the customer's glance); resist with Insight |
| 14 | 4b Effect never changes anything | One SAY after the result shows Limited / Standard / Great |
| 15 | 3a district question has no fallback | "If nobody answers: the Meridian — the cameras" |
| 16 | 3f floor rule silently cancels the hunting-ground cost | Explicit "most likely path" note (Quality second + Old City → skip the −1) |
| 17 | Beat 5 Zoltar card: when to clear | Clear it (`card:null`) before the four questions |
| 18 | Beats 4/5 write files during play | Now: dashboard (and Live Ledger) during play; Faction-Tracker and Campaign-Current-State after the session (Boot §2b) |
| 19 | Paired cues split across two "go"s (3b/3c) | The suite image and its music are marked as one "go"; Boot §2 says a paired cue is one change, in a mock too; the Co-GM's mock note was corrected |
| 20 | Most image cues have no caption | Captions added to every Session 0 image cue (the corkboard is "The Corkboard") |
| 21 | Annex image shows four bunks vs "three bunks" | Line now "bunks for whoever stays too late" |
| 22 | Timing: Beat 3 runs 65–80 min, 3f 15–20 | Run Sheet time budget updated (≈ 3 h; expect safe stop B or C on a slow night) |
| — | (GM question during triage) "banned words" undefined | GM-only examples added under the Annex line |

## Fixed in other files
- `00-Canon/Session-Boot.md`: stings no longer taught (SFX and VOICE rows marked dropped; Zoltar card has no sound; audio palette and "sound not saved" lines replaced; comedy = read-aloud + banner); paired cue = one change; a `gag` op replaces its note, so send the full running text. The 25 % vs 4 % dip question is moot (no stings).
- `11-Visuals/handouts/Table-Card.html` / `.pdf`: resist line lists the actions in each attribute.

## Images redone (painted style, Gemini API)
| Image | Problem | Now |
|---|---|---|
| `location-zoltar-machine` | garbled spine lettering; box not velvet | blank spines; velvet cushion |
| `location-curios-interior` | Zoltar booth by the front door, in full view | booth only a dim glimpse at the end of the aisle in the back corner; blank spines |
| `npc-consequence-push` | booth by the door; evening light vs "Afternoon" | grey afternoon daylight, customer at the window, no booth in view |
| `item-hunters-journal` | prompt words readable; a "TICKET" bookmark (a Gemini artifact, not a planted clue) | squiggle-only handwriting, plain ribbon, red line scribbled out |
| `location-containment-suite` | long concrete stair; no Wall of Rules | short iron stair; six unreadable lines (five black, one red) by the stairs |
| `location-curios-exterior` | not clearly three storeys; nothing says "bank" | three storeys; "SAVINGS BANK" carved in the stone. Players' site hero image updated; strict build passes |

## Left as is (with reason)
- `map-city-s00`: the shop dot sits a little above its label; readable and accepted. The river and the Overhang now match the SAY.
- 3d: `music-vocal-scanner-station` overlaps the read-aloud about the same voice; the GM approved this on 2026-11-18. Say if it should fire after the read-aloud instead.
