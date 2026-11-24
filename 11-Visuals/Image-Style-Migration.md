---
entity_type: Task
status: OPEN — decided by the GM 2026-11-23: move all campaign images from photoreal to a cartoon style. **Style B (painted storybook noir) chosen 2026-11-23 after the Merton, Gerald and Merton-Surge tests (saved in `_Saved-Images/_style-tests/`); one interior test left (the bookshop, which doubles as the first real image).**
purpose: "One place for the plan, the order, the rules and the test prompts for the style change. Tick items off here."
---

# Image style migration: photoreal to cartoon

**Why (GM, 2026-11-23):** Gemini produces stylised characters more consistently than photoreal faces (the Broker/Thorne drift is the example), garbled text and hands matter less, and it is easier to repeat across 80 sessions.
**Risks to manage:** (1) dread: Merton, the Surge, Mabel's wraith and the Subway must still read as scary (Menace Rule), so the style must carry shadow and weight, not Saturday-morning brightness; (2) mixed styles clash on the TV, so we switch fully, session by session; (3) about 80 images exist (6 items, 26 locations, 7 maps, 33 NPCs, 9 wiki) plus the album covers.

## Phase 1: choose the style (the GM, about 30 minutes)
Run each test in Gemini and look at the results on the TV, not the laptop. Attach nothing for the first run.

**Style candidates** (paste the line at the start of the scene prompt):
- **A, graphic noir animation (recommended to try first):** *"Stylised animation illustration in a graphic-noir cartoon style: bold clean outlines, flat shapes with heavy black shadows, a limited palette of warm amber and cold teal, slightly exaggerated proportions, rainy night atmosphere, no photographic detail, no film grain."*
- **B, painted storybook noir:** *"Stylised painted illustration, gouache and ink, visible brushwork, thick dark outlines, slightly exaggerated faces and hands, moody amber and blue light, like a modern dark-fantasy comic. No photographic detail."*
- **C, mystery-cartoon (Scooby-style):** *"Classic mystery-cartoon style: clean outlines, flat bright colours, simple shading, expressive faces, with night-time colours. No photographic detail."* (Expect this to be too light for the dread scenes; it is here as the comparison.)

**Test scenes** (use the same scene for all three styles):
1. *Menace:* "A tired middle-aged security guard in a gray uniform stands in a basement corridor between rows of dented lockers, keys in one hand, caught half-way through turning into a large dog: his face and ears and hands are changing, his eyes are amber, the bare bulb above flickers. He looks apologetic, not aggressive."
2. *Comedy:* "A fawn English bulldog sits very upright on a tall stool in a dark theater basement, with two human hands where his front paws should be, clasped politely. He is delighted to see the viewer."
3. *Place:* "The inside of a struggling old bookshop at night, rain on the window, a grey cat asleep on the counter, a Zoltar fortune-teller machine glowing in a back corner."

**Pick when:** scene 1 still frightens, scene 2 still makes you laugh, and you would be happy to see scene 3 on the TV for ten minutes. Then tell me the style letter (or your edits to it).

## Phase 2: the Co-GM rewrites the prompts (after Phase 1)
- [x] Write the Image Style Guide (a new file in the 11-Visuals folder, named Image-Style-Guide): the chosen style block, the palette, the dread rule, and how to keep characters consistent (attach the anchor portrait every time).
- [x] Update `Pre-Campaign-Image-Prompts.md` (the 13 photographic style paragraphs replaced; done 2026-11-23), `Session-01-Redo-Prompts.md`, `Living-Map.md` (map prompts), and decide the album covers (`Album-Cover-Prompts.md`, probably keep).
- [x] Update `ASSET-TODO.md` so every image is listed as "to restyle" in the order below.

## Phase 3: regenerate, one image at a time (the GM pastes, the Co-GM picks and wires)
Keep the **same filenames** so no prep changes. (Historical: each old photoreal file was archived and later deleted, 2026-11-24.) Order:
1. **Anchor portraits first** for every recurring character (Thorne, Greta, Harlan, Gerald, Consequence, Merton, Bernard, Cosma, Aldric, Emmerich, Mabel, PTOLEMY, Stalls): ONE 3:2 portrait each (face, outfit and signature prop), saved in `_Saved-Images/_anchors/`, then attached as the reference for every later image of that character (a second full-outfit image only if needed). **Done:** Thorne (2026-11-23, mirrored so the ring is on his right hand), Greta (2026-11-23). Anchors are drawn from the written description, not from the old photoreal pictures.
2. **Session 0:** map, Curios exterior and interior, Zoltar, Containment Suite, Scanner Station, corkboard, Journal, Annex, Consequence (two).
3. **Session 1:** map, theater exterior, lobby, auditorium, Bernard, Gerald, locker, Merton (corridor, reveal, surge, chained), collar, Thorne, Greta.
4. **Sessions 2 and 3** images, then the wiki images in the players' repo.
5. **Redo the Crossroads Broker** with a clearly different face (already on the list).
For each image: check it against its read-aloud, check for stray text, and keep the dread scenes scary.

## Order update (2026-11-23)
Do the characters and images **session by session**, not all anchors up front. Session 0 and 1 first (Consequence uses the restyled bookshop interior as her reference; then Gerald, Merton, Bernard), then Session 2 and 3 cast. Characters who debut in Session 4 or later (Harlan, and others) get their anchor when their session is next.

## Progress (2026-11-24)
- **Session 0: all images restyled** (shop exterior and interior, Zoltar machine, Containment Suite, Scanner Station, corkboard, Journal, Annex, Consequence ×2). **Session 1: all restyled** (theater exterior, lobby, auditorium, Bernard, Gerald, locker, Merton ×4, Thorne, Greta). Optional left: `item-leather-collar` (Downtime only).
- **Maps are exempt:** the five city maps are already hand-inked on parchment (style B in spirit); redrawing risks geography drift. New maps stay in the parchment style.
- **Players' site:** `hero-curios.jpg` and `consequence.jpg` replaced with the restyled pictures (not yet committed).
- **Session 2 and Session 3: all restyled.** Still to do: Session 4+ images, wiki portraits and album covers later. The old photoreal archive was deleted on 2026-11-24.

## RESUME HERE (updated 2026-11-24)
**Say "continue the image migration" in a new session started in the `The-Shadow-Exchange` folder.** The Co-GM reads this file and `Image-Style-Guide.md`, then gives the next prompt below. Workflow per image: the GM pastes the prompt into Gemini (attachments named in the prompt), pastes the options back, the Co-GM picks one (checks the brief, stray text, spoilers, placement), saves it over the same filename (no archive of the old one is kept), updates `ASSET-TODO.md`, then writes the next prompt.
**Done so far (Session 2):** Emmerich, silver thimble, Drennick & Foss, Meridian street, Subway entrance, Subway main hall, PTOLEMY, Cosma, Aldric, Broker, pier exit (Session 2 done). Session 3 so far: Mabel living, Mabel wraith, Ashby exterior, Ashby interior (clock fixed to about 11:47, wall patch removed), Agnes, Grief Jars, knitting needle, Stalls (Session 3 done). Optional images done: leather collar, Emmerich's shop. Wiki portraits done: Greta, Consequence, Emmerich, Drennick, Foss, Cosma, Merton (human), Thorne, Bernard, Gerald, Mabel, Agnes, Aldric, Stalls (all via the API script, 2026-11-24).
**Every campaign image is now in the painted style (2026-11-24).** Done: Sessions 0 to 3 (all cued images), the optional collar and Emmerich's shop, all wiki portraits (Greta, Consequence, Emmerich, Drennick, Foss, Cosma, Merton human, Thorne, Bernard, Gerald, Mabel, Agnes, Aldric, Stalls, Harlan), and the Session 4+ set (Harlan's counter, the diner, the Wall of the Missing, Senna, Mara (face hidden), Dev & the Last Stop, Reyes, Vance, the Bookmobile, Officer Bram, Madame Quill, Wim, Ottilie). Made through `docs/tools/gemini_image.py` (Gemini API, direct REST call; `--size 2K` gives 2752x1536). The old photoreal archive and the unused alternates were deleted on 2026-11-24 (tracked originals remain in git history). **Left, none urgent:** (1) wiki portraits for the Broker, Ptolemy's luggage and Merton's true form wait for the story; (2) publish portraits to the players' site only through `Wiki-Update-Protocol.md`; (3) album covers decision; (4) new characters get an anchor portrait first. Music: `docs/tools/gemini_music.py` (Lyria) is being tested on the Session 3 cues.

## Rules while migrating
- Do not mix styles within a session: finish Session 0 and 1 before running another mock or a real session with new images.
- The spoiler rules still apply to the new images (no stray names, stamps or forms; Aldric not a broadcaster; no Omen).
- Players' site: keep the old hero images until the new ones exist, then swap through `Wiki-Update-Protocol.md`.
