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
- [ ] `location-merton-locker.png` (optional; Session 1 beat 5, the emotional centre; prompt in `Pre-Campaign-Image-Prompts.md` → *Merton's Locker*; until then the TV shows the caption "Locker 7").
- [ ] `item-hunters-journal.png` close-up (optional; the corkboard image covers it).
- [ ] `location-curios-interior.png` (optional; the shop floor: ATM gag, S1 Beat 1 and Downtime, every recap; prompt in `Pre-Campaign-Image-Prompts.md` → *The Shop Floor*; until then a caption).
- [ ] `location-annex.png` (optional; the upstairs room for Session 0 beat 3f and every downtime scene; prompt in `11-Visuals/Pre-Campaign-Image-Prompts.md` → *The Annex*; until then the TV shows the title card with the caption "The Annex").
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
- [x] *(done 2026-11-21; report `Opus-Beat-Audit-Report-2026-11-21.md`)* **Opus beat-by-beat audit of Sessions 0–3** (plan and ready prompt: `docs/review/Opus-Beat-Audit-Plan.md`; run after the Session 1 mock; GM approves the cost first).
- [x] *(done 2026-11-21; `Gemini-Regression-Triage-Log-2026-11-21.md`)* **Regression check** of the fixed Sessions 0–3 — `docs/review/Gemini-Regression-Check-Prompt.md` (drafted 2026-11-21; run it next).
- [x] **Bestiary slips** (the Anchor Cover Rule for all 40 entries): run 2026-11-21 and applied to `10-Generators/Bestiary.md`; raw result in `docs/review/Gemini-Bestiary-Slips-Raw-2026-11-21.txt`.
- [x] *(done 2026-11-21; `Gemini-Content-Bank-Triage-Log-2026-11-21.md`)* **Content-bank cross-check** (NPC bench, Improv Kit, Venues Bank, Gazetteer, Bestiary, Zoltar deck, procedures, and the five draft catalogs) — `docs/review/Gemini-Content-Bank-Cross-Check-Prompt.md` (drafted 2026-11-21; run it next).
- [x] *(done 2026-11-21; `Opus-Gap-Items-Audit-2026-11-21.md`, 30 findings fixed)* **Opus final audit of the gap-item files**
- [x] *(done 2026-11-21; report `Opus-Reaudit-Report-2026-11-21.md`, 20 findings fixed)* **Opus (or higher) re-audit of the files changed since the beat audit** (verify the ~100 fixes did not break anything): run after the content-bank cross-check; no per-token cost (monthly plan).

- [x] *(done 2026-11-21; `Gemini-Regression-2-Triage-Log-2026-11-21.md`)* **Gemini regression check #2** — `docs/review/Gemini-Regression-Check-2-Prompt.md`; paste the block into Gemini and bring the result back for triage.
- [ ] **Listen once to `music-vocal-scanner-station`** for any Subway or Aldric Voss detail (its prompt asks for "locations of things that haven't happened yet"). Found by the S0 simulation.
- [ ] **Make `location-curios-interior`** (S0 names it but no beat cues it until it exists).

## Parked ideas (not started; revisit when the GM asks)
- **End-of-night transcript** (GM, 2026-11-21): record the night, transcribe with a free tool that can tell voices apart (e.g. WhisperX with speaker labels, Buzz, or MacWhisper's free tier; get the friends' OK first), then hand the transcript to the Co-GM at close-out to mine for table-invented canon (names, nicknames, Friends, Rivals, Heirlooms, cover stories), exact quotes for the recap, and the Night Log. A live feed was considered and set aside (side talk, several voices, theories leaking into canon).

## Decisions waiting on you
- [ ] Review the draft content in `docs/review/draft-content/` when the Opus agents finish (NPC bench, improv kit, gaps and rules, catalogs).
- [ ] Any NPC deaths you want to lock in beyond the defaults in `05-Sessions/Season-1-Plan.md` §4.
