# Manual Work Queue (things that need the GM's hands)

Updated 2026-11-20. Anything I recommend that only you can do (generate an image or audio, print, test hardware, run Gemini, push) goes here, in the order it is needed. Tick items off here; the detailed asset list is `11-Visuals/ASSET-TODO.md`.

**Map images:** none are needed before Session 0 or Session 1 — `map-city-s00` and `map-city-s01` exist and are cued. No new map images are being generated now (GM decision 2026-11-20); the map roadmap in `11-Visuals/Living-Map.md` is a planning list only.

## Before Session 0 (required)
- [ ] Print the Table Card (`11-Visuals/handouts/Table-Card.pdf`) ×4 (one per player + a spare), plus `Player-Reference.md` ×3 and keep `GM-Cheat-Sheet.md` at your elbow.
- [ ] Share the free playbook PDFs from the players' site (*Official Resources*); confirm the three players have read Quick Start and sent their 8 things.
- [ ] Open `GM-Dashboard.html` (F11) and `Player-Screen.html` on the TV (F11 on Windows; Cmd-Ctrl-F on a Mac). The Player Screen should show the title card. *(The dashboard's libraries are now vendored locally in `11-Visuals/vendor/`, so it works offline. Open it once to confirm.)*
- [ ] Test `fade-switch.sh` once (QuickTime Player must be allowed to be controlled; macOS may prompt).
- [ ] After the mock: reset `player-screen/scene.js` to the title card and `dashboard-feed/feed.js` to its header, and stop the music (the end-of-mock reset).
- [ ] Decide when to **push** (a large set of campaign and site changes is waiting; push only when you say "push").

## Optional before Session 0 (nice to have)
- [ ] A fairground street image for the Session 1 approach (prompt drafted in the chat; optional — the map and the theater image already cover it).
- [ ] `item-hunters-journal.png` close-up (optional; the corkboard image covers it).
- [ ] Zoltar and foley audio — **on hold** until video credits return (`Music-Prompts.md` §Z).

## Before Session 1
- [ ] Nothing required: all images and music exist.
- [ ] Optional stings (Veo, on hold): `music-sting-bernard-scream`, `music-sting-lever-trapdoor`, `music-sting-fortune-card`, the Zoltar S1 fortune.
- [ ] After Session 1: generate the wiki portraits for the NPCs the crew met (Thorne, Bernard, Gerald, and Merton once the collar's fate is known), then publish with the recap.

## Before Session 2
- [ ] Nothing required: images (incl. `map-city-s02`, Aldric, the Broker) and music exist.
- [ ] Optional: `map-subway-schematic.png` (prompt in `Pre-Campaign-Image-Prompts.md`), `music-sting-ptolemy-clasps`, `music-sting-rotary-phone` (Veo, on hold).

## Before Session 3
- [ ] **Required music (Lyria, not Veo):** `music-ashby-approach.mp3`, `music-ashby-interior.mp3`, and the `music-sting-boo` overlay (prompts in `Music-Prompts.md`). *These are the only required assets still missing for Sessions 0–3.*
- [ ] Images are done (`map-city-s03`, exterior, Mabel ×2, Agnes, jars; optional interior, needle, Stalls).

## Gemini second looks (run when you are ready; Claude triages the results)
- [x] **Bestiary** — `docs/review/Gemini-Bestiary-Ideas-Prompt.md` (run; raw result saved as `docs/review/Gemini-Bestiary-Raw-2026-11-20.txt`).
- [x] **Bestiary source check** (done 2026-11-20: all 40 links live; folklore details marked as adaptations) — `docs/review/Gemini-Bestiary-Source-Check-Prompt.md` (Gemini verified the 40 sources and the living-faith cautions).
- [x] **World atlas and venues** — `docs/review/Gemini-World-Atlas-Ideas-Prompt.md` (run 2026-11-20; built into `04-Locations/Venues-Bank.md` and `Gazetteer.md`).
- [ ] **Regression check** after the mock, once the preps are final (Claude will draft the prompt).
- [ ] A cross-check of the Opus content bank in `docs/review/draft-content/` once it is triaged.

## Decisions waiting on you
- [ ] Review the draft content in `docs/review/draft-content/` when the Opus agents finish (NPC bench, improv kit, gaps and rules, catalogs).
- [ ] Any NPC deaths you want to lock in beyond the defaults in `05-Sessions/Season-1-Plan.md` §4.
