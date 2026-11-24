---
entity_type: Tracker
name: "Asset To-Do — Images & Music"
last_updated: 2026-11-24
purpose: "What is done and what is still open for images and music. Prompts live in Pre-Campaign-Image-Prompts.md / Music-Prompts.md / Album-Cover-Prompts.md; the tools and the style rules live in Image-Style-Migration.md and Image-Style-Guide.md."
---

# Asset To-Do — Images & Music

**Status (2026-11-24): everything cued in Sessions 0 to 3 exists.** All images are in the painted style (style B), all required music exists, and the Session 4+ NPC and prop images exist too. Images and music are now made by Claude through the Gemini API (`docs/tools/gemini_image.py`, `docs/tools/gemini_music.py`): one generation per prompt, redo with the higher model only if needed. **Stings and foley are dropped (GM, 2026-11-24).** Maps stay in the parchment style.

Legend: ☐ to do · ✅ done

## 🖼 IMAGES

### Done
- **Sessions 0 to 3:** every cued image (locations, NPCs, props, pier exit, Ashby house and its contents), plus the optional collar and Emmerich's shop.
- **Wiki portraits:** Greta, Consequence, Emmerich, Drennick, Foss, Cosma, Merton (human), Thorne, Bernard, Gerald, Mabel, Agnes, Aldric, Stalls, Harlan. They are held back from the players' site until the crew has met each character (`00-Canon/Wiki-Update-Protocol.md` §3b).
- **Session 2's optional wall map** `map-subway-schematic.png` (impossible network, one faint pencil line, no red ink; made 2026-11-24).
- **Session 4 and later:** Harlan at the counter, Harlan's diner, the Wall of the Missing, Senna, Mara (face hidden), Dev & the Last Stop, Reyes, Vance, the Bookmobile, Officer Bram, Madame Quill, Wim, Ottilie.
- **Anchor portraits** for recurring characters: `_Saved-Images/_anchors/`.

### Open
| ☐ | File | Notes |
|---|---|---|
| ☐ | `npc-elias-thorne-street.png`, `location-emmerichs-shop-day.png` | optional extras from Sessions 1 and 2 |
| ☐ | wiki portraits for the Broker, Ptolemy's luggage, Merton's true form | wait until the crew has seen them |
| ☐ | `item-casting-mask-GM-PRIVATE.png` | GM-only, never on the Player Screen; prompt exists |
| ☐ | images for the Fence, the Whisperer, the Ministry field office, the Docks, the Overhang playground | no prompts yet; ask the Co-GM when a session needs one |

## 🎵 MUSIC

### Done
- All music cued in Sessions 0 to 3, including `music-ashby-approach` and `music-ashby-interior` (made 2026-11-24).
- Already saved but not yet cued: `music-score.mp3` (alternate for the Surge or heist action) and `music-vocal-bookshop-radio.mp3` (AM-radio vocal for the Scanner Station or a Downtime vignette).

### Open
| ☐ | File | Cued in |
|---|---|---|
| ☐ | `music-road-rock.mp3` | van rides / end of a good score |
| ☐ | `music-harlans-diner.mp3` | S4 |

### ⚠ Vocal-under-narration risk
`music-vocal-fairground`, `music-vocal-scanner-station`, `music-vocal-bookshop-radio` all have **lyrics**. The Run Sheets say *fire after the read-aloud*, not under it. For an instrumental version, regenerate with `[Instrumental]`.

### Album covers (`_Album-Covers/`)
✅ All 28 covers are remade (2026-11-24) in the painted style, square 1024 px, with no star or watermark: one per track, including the covers for the not-yet-made `music-road-rock` and `music-harlans-diner`. The sting covers were dropped with the stings. Each cover follows its track's prompt in `Album-Cover-Prompts.md`.

---

## 🛠 Tech to-dos (not assets, but before Session 0)
- ☐ **Players' playbook sheets:** free PDFs are linked from the wiki's *Official Resources* page (verified; all load). Print or share the *Core Play Sheets* for the table.
- ✅ `GM-Dashboard.html` now loads **pinned local copies** of React, ReactDOM, Babel and Tailwind from `11-Visuals/vendor/` (2026-11-20) and works offline; if a library is missing it shows a message instead of a blank page. Open it once to confirm.
- ☐ Open `Player-Screen.html` on the TV; F11; confirm the title card; ask the Co-GM to update `scene.js` once to test a crossfade.
- ☐ Test `fade-switch.sh` once (QuickTime Player must be permitted to be controlled; macOS may prompt).
- ☐ Enter the three PC names into `GM-Dashboard.html` (`INIT_PCS`) and bump `SAVE_VERSION`.
- ☐ Windows paths in `CoGM-Core-Instructions.md` (`The Shadow Exchnage` misspelling, the OneDrive path) — only matter if you run from the Windows machine.
- ☐ Rotate the Gemini API key in Google AI Studio when the image and music work is finished (it was pasted into a chat).

### Living map (see `Living-Map.md` for rules and prompts)
| ☐ | File | Notes |
|---|---|---|
| ✅ | `map-city-s00.png` | C&C labelled — done 2026-11-20 |
| ✅ | `map-city-s01.png` | Fairground Grand pinned — done 2026-11-20 |
| ✅ | `map-city-s02.png` | Emmerich & Daughter pinned — done 2026-11-20 |
| ✅ | `map-city-s03.png` | Eastern Pier + Ashby House pinned — done 2026-11-20 |
| ✅ | `map-city-base.png` | new base map (2026-11-20); the old `map-city-districts*.png` are retired — also the fallback until the s00–s03 maps exist |
| ☐ | `map-region-s04.png` | regional map for Harlan's diner (first time outside the city) — prompt in `Living-Map.md` |
