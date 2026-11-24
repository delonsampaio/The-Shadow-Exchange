---
entity_type: Visual_Reference
purpose: "The city map is a LIVING map: one cumulative file per session, new pins added as the crew learns of places. Rules, pin ledger and Gemini prompts."
last_updated: 2026-11-20
---

# The Living Map

The TV shows the city map at the start of a trip (the approach to a score). It is **cumulative**: each session's map is the previous one plus the places the crew has learned about. The crew only ever sees places they have been to or been told about.

## Rules
1. **One file per session:** `map-city-s01.png`, `map-city-s02.png`, … Each is made by **editing the previous map** (attach it to Gemini; "change nothing else"). Never redraw from scratch after the base — the geography must not drift.
2. **A pin is added only when the crew knows the place** — they have been there, or an NPC has named it in play. Never pin: the Subway entrance, any GM-private site, anything from a future session, the Architect's places.
3. **Style:** earlier pins stay, re-inked in dark brown; **this session's new pins are red.** Labels are small hand-lettered serif, the same as the district names. No icons, no legend.
4. **Format:** 16:9. Exact label text as listed below. Real brand names are fine (private table); no compass rose. *(Gemini no longer stamps a corner sparkle, GM 2026-11-22; if an old image still shows one, crop it from the left/top so right-hand labels are not clipped and the result stays 16:9.)*
5. **Save** to `11-Visuals/_Saved-Images/`. Until the new file exists, the prep falls back to the previous map (or `map-city-base.png`).
6. **Every session, at the end:** add the next session's pins to the ledger below (from its prep), generate `map-city-s(N+1).png`, and name it in that prep's Run Sheet. The end-of-session checklist in `Session-Boot.md` §6 includes this step.
7. **Districts for each place** are in `04-Locations/City-Districts.md`; if a prep names a new location, say which district it is in.
8. **The elevated train** (the city's only rail) is not drawn on any city map. If a table asks, it runs along the outer ring road. If it ever matters, add a thin hand-inked line in a later map step.
9a. **Label size for TV and chat (checked 2026-11-21 on `map-city-s03.png`, which is legible at 1600 px on the TV and at 700 px in a chat):** every new label must be **at least as large as "ASHBY HOUSE"**; add **no more than about four new pins per session**; if a later map gets crowded, make a **zoom map** (the venue zoom maps in the placement plan) and do **not** shrink the labels.
9c. **Overview rule (GM, 2026-11-21): the city map is an overview, the zoom maps hold the detail.** Once the city map reaches about **15 labelled pins** (or earlier if it looks crowded), switch to this: the city map shows only the **permanent landmarks** (Curios & Chronicles, Harlan's diner area, and any other place the crew has made a base), **this session's new pins in red**, and **older pins as small brown X marks with no label**. Every place the crew has been keeps its full label on its **district zoom map** (`map-zoom-old-city.png`, `-meridian`, `-fairground`, `-docks`, `-overhang`), which is generated the first time the crew spends several scenes in that district and then updated the same way (edit the previous version, new pins red). Never shrink labels to fit; never redraw the base.
9b. **Sharing a map in a chat:** the full-size PNGs are about 7 MB. For a chat or message make a light copy: `sips -Z 1600 -s format jpeg -s formatOptions 80 11-Visuals/_Saved-Images/map-city-sNN.png --out /tmp/map-city-sNN-chat.jpg` (about 300–500 KB, still legible). Do not commit the copies.
9. **Outside the five districts? Make a new map.** Do not stretch the city map to hold it. Pick the type: **regional map** (the whole city as one small area, with the roads, towns and landmarks beyond it — for anywhere "out of the city"), **site map** (a street-level or floor-plan map of one place, when a score needs the layout), or **underground schematic** (the Subway has its own, `map-subway-schematic`, shown only per the Session 2 rules). Name it `map-region-sNN.png` / `map-site-<place>.png`, keep the same paper-and-ink style and the 16:9 rule, and add it to the ledger. A regional map is cumulative like the city map.

## Pin ledger (what each map shows)
| Map | New pins this session (red) | Pins carried (brown) | Added when |
|---|---|---|---|
| `map-city-base.png` (base, generated 2026-11-20) | Old City dot (unlabelled) | — | exists ✅ |
| `map-city-s00.png` ✅ | **Curios & Chronicles** (label on the dot) | — | S0, Beat 3a — the crew's home |
| `map-city-s01.png` ✅ | **The Fairground Grand** (Fairground District) | C&C | S1 approach (the crew knows the target) |
| `map-city-s02.png` ✅ | **Emmerich & Daughter** (The Meridian) | C&C · Fairground Grand | S2 job arrives |
| `map-city-s03.png` ✅ | **Eastern Pier** (The Docks) · **Ashby House** (The Overhang) | C&C · Fairground Grand · Emmerich & Daughter | S3 briefing / approach |
| `map-city-s04.png` | *(fill from the Session 4 prep)* | all above | S4 |

## Placement plan (decide positions BEFORE a session needs them)
A place's spot on the map is fixed **when it is first written into any prep or canon file**, not when the pin is drawn. Record it here the moment a location is named; the pin is only *drawn* when the crew learns the place (rule 2). Positions are described against what is already on the map so Gemini can find them.

| Place | District | Spot on the map (new base map, 2026-11-20) | First needed | Pinned from |
|---|---|---|---|---|
| Curios & Chronicles | Old City | the black dot in the central plaza of the walled circular core | S0 | `s00` |
| The Fairground Grand (theater) | Fairground | the large building on the east side of the ring of buildings — the one nearest the Meridian border, level with and to the left of the label "THE MERIDIAN" | S1 | `s01` |
| Emmerich & Daughter | Meridian | **as drawn in `s02`: the southern block row of the Meridian grid, just left of centre, above the warehouse row at the Docks edge** | S2 | `s02` |
| Eastern Pier (Subway exit) | Docks | **as drawn in `s03`:** the long diagonal pier on the right of the harbour, X near its upper end | S2 (end) | `s03` |
| Ashby House | Overhang | **as drawn in `s03`:** the upper terraces just right of the label "THE OVERHANG", near the river bend | S3 | `s03` |
| Ministry field office *(canon: six blocks east of C&C, plain door)* | Old City | just inside the east wall of the walled core, level with the dot | when first visited | — |
| Ministry scanner station *(above a coffee shop)* | Meridian | a block on the district's west edge, near the Fairground border | when first visited | — |
| Meridian Group HQ | Meridian | the tallest tower footprints in the middle of the grid | when first named | — |
| Fairground Hotel (Night Porter) | Fairground | the spired, castle-like building at the top of the ring | when first named | — |
| Cold storage / Ministry Bio-Containment | Docks | the row of long warehouse blocks along the quay at the top of the harbour | when first named | — |
| Overhang playground | Overhang | the open hillside patch at the top-left of the Overhang, beside the river bend | when first named | — |
| Municipal archive (burned) | Old City | the scorched block just inside the north wall of the walled core | when first named (S9 option) | — |
| Glass Building | Meridian | a mirrored tower footprint on the eastern side of the grid, next to the river | when first named (Mini-Arc C) | — |
| The Starlight (memory-siren lounge) | Fairground | a lit block on the inner side of the ring, away from the theater | when first named (Episode 4) | — |
| Pier 9 lockers | Docks | the ninth pier along the quay, south of the warehouse row | when first named (Episode 3) | — |
| Drainage tunnels, eastern pier | Docks | storm-drain outfalls beside the Eastern Pier (shallow, surface-level) | when first named (S9 option) | — |
| Empty Apartment (3rd floor) | Overhang | a terrace row on the lower hillside, near the playground | when first named (S5 option) | — |
| Agnes's house (12 Calloway St) | Overhang | across the street from Ashby House (14 Calloway St) on the upper terraces | S3 | when first named (not on `s03`) |
| Hospital (Old City Mercy), room 412 | Old City | an annex block outside the east wall (GM to confirm district) | when first named (S6) | — |
| Dead hunter's storage unit | Docks | a self-storage row at the inland edge of the Docks | when first named (S8) | — |
| The 11:47 bus route | citywide | **never pinned as a place** (a route): show only a bus-stop pin where it stops | when first named (Episode 1) | — |
| Harlan Okafor's diner | *(outside the five districts — "forty minutes out, city's edge")* | **regional map** `map-region-s04` (prompt below); the city is drawn small on it | S4 | `map-region-s04` |
| The Subway entrance, Architect sites, anything GM-private | — | **never pinned** — the Subway's entrances have no fixed address (they appear for whoever it chooses, wherever they are) | — | — |

**When writing a prep:** add every new location to this table (district + spot) *at that moment*, even if it will not be pinned for several sessions. **At the end of a session:** the pins for the next session come straight from the "Pinned from" column.

## Map roadmap (what to generate, and when)
**Planning list only — no new map images are being generated now (GM decision 2026-11-20); the world-building (names, venues, places) comes first.**

The city maps (`base`, `s00`–`s03`) are done. Everything below is generated **when first needed**, one at a time, in the same aged-paper-and-ink style, 16:9, with the Rules above. Each gets a Gemini prompt written from the placement plan when its trigger arrives.

| Map | What it shows | Trigger | Priority |
|---|---|---|---|
| `map-city-s04+` | the city map plus new pins (ledger above) | each session's prep | every session |
| **District zoom maps (5)** — Old City, The Meridian, The Fairground District, The Docks, The Overhang | street names, landmarks, the shops and venues players may visit (from `04-Locations/Venues-Bank.md` once written), the crew's walking routes | the first extended on-foot scene in that district | medium |
| `map-region-s04` | the city small on a regional map: roads, towns, the coast, Harlan's diner (prompt below) | Session 4 (Harlan's diner) | high |
| `map-transit-elevated` | the one elevated train line on the city map, with its stations | the first time a PC rides it or an NPC mentions it | low |
| **Site plans (floor plans)** — the lair (one floor, eleven steps down), the Fairground Grand (lobby, auditorium, basement, pump room), Mabel Ashby's house, Harlan's diner, the Apex Docks black site, the Meridian tailor block | where everything and everyone is, for chase, heist and infiltration scenes | the score that uses it | high for scores (draw 1–2 sessions ahead) |
| `map-subway-hall` + platforms | the Main Hall, Platforms 1–3, the Mezzanine, the turnstiles (a hand-drawn passenger guide; **never a true schematic** — the Subway does not obey physics) | the second Subway visit | medium |
| `map-subway-schematic` | the wrong transit map on the hall wall (prompt exists) | Session 2 optional | low |
| Out-of-town maps — the coast, an Away Job town, a motel and roadside | one small map each | the Away Job (S16) and later | low |
| Season 2/3 maps — a shrunken Subway, Past the Yellow Line, the Line 0 platform | what the story has changed | when the season starts | later |

**Naming:** every place a player may visit needs a name on the map (a shop, a bar, a library, an archive). Keep a running list in `04-Locations/Venues-Bank.md` (to be created from the Gemini and Opus results) so names stay consistent across maps, preps and the wiki.

## Gemini prompts
> **Style change 2026-11-23:** future map prompts use the painted-storybook style block from `Image-Style-Guide.md` (an illustrated painted map on aged paper). The existing maps stay photographic-parchment until they are restyled (see `Image-Style-Migration.md`).
Paste each into Gemini and attach the file named. (Gemini has local file access: you may instead give it the repo-relative path.) Generate in order; each uses the previous result.

### 0 — New base map — **DONE 2026-11-20** (`map-city-base.png`; the prompt that made it is in git history). The old map is retired. The unused alternative is in `99-Workshop/map-city-base-A-unused.png`.

### S0 — `map-city-s00.png` — **DONE 2026-11-20** ✅
Prompt that worked (second try; the first try's label was too small, ran into the wall, and added a stray bullet): attach `map-city-base.png`.
```
Using the attached city map as the exact reference, change nothing except one addition. Keep every street, district shape and district label exactly as they are.
Directly below the black dot in the middle of Old City, add a label in two centred lines, "CURIOS &" over "CHRONICLES", in the same black serif capitals as the district names. Make the lettering about half the height of the "OLD CITY" lettering, so it stays easy to read from across a room. Give it the same soft cream halo that sits behind the district names, so it stays legible over the streets. Do not add any other dots, bullets, lines, icons or marks, and do not move or change the black dot.
Keep the thin frame line. 16:9 landscape. No watermark, no logo, no signatures.
```
**Lessons for every pin step:** labels about half the height of the district names; two centred lines for long names; the cream halo; one mark only; "do not add any other dots, bullets or marks". Expect small street changes near the edit (Gemini redraws a little) — check the pinned building and the neighbouring labels each time.

### S1 — `map-city-s01.png` — **DONE 2026-11-20** ✅ *(pin label came out a little smaller than the S0 label; accepted)*
Attach `map-city-s00.png`.
```
Using the attached city map as the exact reference, change nothing except one addition. Keep every street, district shape and label exactly as they are, including "CURIOS & CHRONICLES".
In The Fairground District, on the large building on the east side of the ring of buildings (the one nearest the Meridian border, level with and to the left of the label "THE MERIDIAN"), add a clearly visible hand-inked RED X (about as tall as the letters of the label) and, beside it, the label "THE FAIRGROUND GRAND" in two centred lines ("THE FAIRGROUND" over "GRAND"), in black serif capitals about half the height of the district names, with the same soft cream halo as the district names.
Do not add any other dots, bullets, lines, icons, legend or marks, and do not change any other label.
Keep the thin frame line. 16:9 landscape. No watermark, no logo, no signatures.
```

### S2 — `map-city-s02.png` — **DONE 2026-11-20** ✅ *(the Emmerich X landed on the southern block row of the Meridian grid, near the Docks edge; accepted)*
Attach `map-city-s01.png`.
```
Using the attached city map as the exact reference, change nothing except the following. Keep every street, district shape and label exactly as they are.
1. Change the existing red X on the Fairground Grand building to dark brown ink, the same ink as the map's linework, so it looks older. Leave its label and "CURIOS & CHRONICLES" as they are.
2. In The Meridian, on an open block just below and slightly left of the label "THE MERIDIAN", add a new, clearly visible hand-inked RED X (about as tall as the letters of the label) and the label "EMMERICH &" over "DAUGHTER" in two centred lines, in black serif capitals about half the height of the district names, with the same soft cream halo.
Do not add any other dots, bullets, lines, icons, legend or marks, and do not change any other label.
Keep the thin frame line. 16:9 landscape. No watermark, no logo, no signatures.
```

### S3 — `map-city-s03.png` — **DONE 2026-11-20** ✅ *(second of two candidates chosen: fully brown old pins, larger new Xs)*
Attach `map-city-s02.png`.
```
Using the attached city map as the exact reference, change nothing except the following. Keep every street, district shape and label exactly as they are.
1. Change the existing red X for "EMMERICH & DAUGHTER" to dark brown ink, like the other earlier mark. Leave its label as it is.
2. In The Docks, on the long pier that runs diagonally down-right on the right side of the harbour, add a new, clearly visible hand-inked RED X and the label "EASTERN" over "PIER" in two centred lines, in black serif capitals about half the height of the district names, with the same soft cream halo.
3. In The Overhang, on one of the terraced rows to the right of the label "THE OVERHANG", along the cliff line, add a new, clearly visible hand-inked RED X and the label "ASHBY" over "HOUSE" in two centred lines, in black serif capitals about half the height of the district names, with the same soft cream halo.
Make each new red X about as tall as the letters of its label. Do not add any other dots, bullets, lines, icons, legend or marks, and do not change any other label.
Keep the thin frame line. 16:9 landscape. No watermark, no logo, no signatures.
```

### Regional map — `map-region-s04.png` *(first time the crew goes outside the city; Harlan's diner)*
Attach `map-city-s03.png` (or the latest city map).
```
Using the attached city map as a reference for the style only, draw a larger REGIONAL map in the same aged-cream-paper, dark-ink, hand-drawn style: the whole city shown as one small walled-looking cluster near the lower-left, with the surrounding countryside beyond it. Show a few main roads running out of the city, small hand-drawn villages, fields, a river or two, a rail line, hills drawn with hatching, and a distant coast at the top right in blue watercolor. Label only: the city as "The City" in the same serif lettering, and one small place on a road leaving the city to the east, drawn as a single tiny building by the roadside with a red X and the small hand-lettered label "Okafor's Diner". Nothing else is labelled.
The look of a map drawn by someone who knows the roads from driving them. Keep a thin frame line. 16:9 landscape. No compass rose, no legend, no watermark, no logo, no signatures.
```
*(Later regional maps: attach the previous regional map and say "change nothing except", as with the city map.)*

### S4 and later
Copy the S3 prompt, attach the previous map, and replace item 2 onward with the new pins from the ledger. Keep "change nothing except" and the exact labels.

---

## Maps needed (world-atlas pass, 2026-11-20 — planning only; no map images are generated until needed)
*All maps stay 16:9, aged-paper-and-ink style, no compass rose, no legend, generated one at a time only when triggered (Living-Map.md). **Never** pin Subway entrances, Architect sites, or GM-private sites on player maps.*

### A. Master Map Production Schedule

| Priority | Map File / Group | Category | What It Must Show | Trigger (When Needed) |
|---|---|---|---|---|
| **1 — Every Session** | `map-city-s04.png` … `s28+` | Cumulative City Map | Previous session's map with prior pins re-inked dark brown + new session pins in red (per `Living-Map.md` pin ledger). Never draw the Ring El here. | End of every session (prep for next session) |
| **2 — Immediate (High)** | `map-region-s04.png` | Regional Map | City small in lower-left, coast top-right, main roads, hatched hills, river, outer rail line, **Okafor's Diner** pinned red (cumulative for later out-of-town pins). | **Session 4** (Harlan's Diner debut) |
| **3 — High (Score Site Plans)** | `map-site-curios.png` | Site Floor Plan | Cutaway of C&C: Front Shop + Zoltar, 11 iron steps down to 1-floor Containment Suite (Vault, Cold Storage, Post-Op, Scanner, Trophy Wall), 2nd-floor Annex, 3rd-floor Lofts, Roof Hatch. | S1–S4 (for reference / S27 Siege of Old City) |
| **3 — High (Score Site Plans)** | `map-site-fairground-grand.png` | Site Floor Plan | Lobby, auditorium, backstage, basement (Locker 7), and sunken **pump room** (no second basement!), plus roof access for Bernard. | S1 (or callback score) |
| **3 — High (Score Site Plans)** | `map-site-ashby-house.png` | Site Floor Plan | 14 Calloway St (parlor, kitchen, stopped clocks, Grief Jars shelf, porch) + 12 Calloway St (Agnes) + Calloway Alley behind. | S3 (or Mini-Arc C callback) |
| **3 — High (Score Site Plans)** | `map-site-harlans-diner.png` | Site Floor Plan | Counter, grill, Wall of the Missing, privacy-hum back booth, kitchen rear door, gravel parking lot & tree line. | S4 / **S21** (*Closing Time* bottle episode) / ~S41 fire |
| **3 — High (Score Site Plans)** | `map-site-mercy-4f.png` | Site Floor Plan | Old City Mercy Hospital 4th floor, Room 412, nurse station, freight elevator, fire stairwell (for stealth extraction). | **Session 6** (*The John Doe*) |
| **3 — High (Score Site Plans)** | `map-site-apex-blacksite.png` | Site Floor Plan | Docks "private medical storage" shell: loading bay, freezer corridor, scanner calibration cage (Artie Bell), evidence room, harbor slip exit. | **Sessions 10–11** (*Extraction Under Salt*) |
| **3 — High (Score Site Plans)** | `map-site-emmerich-block.png` | Site Floor Plan | Emmerich & Daughter 2nd-floor tailor shop, boutique row street, Meridian Span canal bridge, alleys for Door Chase / Mini-Arc A. | S2 / Mini-Arc A |
| **4 — Medium (Subway Guide)** | `map-subway-hall.png` | Hand-Drawn Passenger Guide | Main Hall (north-wall red-ink map), PTOLEMY's corner, Platforms 1–3, Mezzanine (Job Board, moving Whisperer booth), Back Booth, Turnstiles, Line 0 Platform. **Impressionistic guide — never true physics.** | **Session 3+** (second Subway visit) |
| **4 — Medium (District Zooms)** | `map-zoom-old-city.png` (and 4 other districts — see Table B below) | 5 District Zoom Maps | Street names, bridges/landmarks, canon sites already learned, and the **12 Venue Bank places** for that district (unpinned until visited, or released as a neighborhood walking map). | First extended on-foot / free-play investigation in each district |
| **5 — Medium (S1B Site Plans)** | `map-site-meridian-hq.png`, `map-site-harrow-office.png`, `map-site-kress-rig.png` | Site Floor Plans | Meridian Group lobby/executive floor (S20), Harrow & Sons rowhouse (S23), and Kress's Resonance-rig site (S26–28). | Draw 1–2 sessions before S20, S23, S26 |
| **6 — Low (Transit & Optional)** | `map-transit-elevated.png` | Transit Diagram | Fold-out strip/ring diagram of **The Ring El** (8 outer-ring stations + bus transfers), explicitly styled as a separate municipal brochure so it stays OFF `map-city-*`. | First time a PC rides the Ring El or plans a transit escape |
| **6 — Low (Optional)** | `map-subway-schematic.png` | In-World Prop | The impossible, wrong transit map mounted on the Main Hall north wall (lines that match no city, one fresh red line). | S2 optional / when Decay rises |
| **6 — Low (Out-of-Town)** | `map-out-coastal-town.png`, `map-out-motel.png`, `map-out-quarry.png`, `map-out-lakehouse.png` | Away-Job Site Maps | Compact tactical sketches for S16 Coastal Town, Pine-Needle Motor Court, Siltwater Quarry, Heron Point Lake House, or Gull's Neck. | **Session 16** (Away Job) and later road trips |
| **7 — Later (Seasons 2–3)** | `map-subway-decay4.png`, `map-subway-yellow-line.png`, `map-subway-line0.png` | Endgame Evolved Maps | Visibly shrunken Main Hall & dark platforms (Decay 4, ~S41), tunnels Past the Yellow Line (~S67), and the Line 0 Platform when the first boardable train arrives (~S78–80). | Season 2 mid-finale (~S41) & Season 3 (~S67–80) |

---

### B. District Zoom Maps — 12 Venue Labels Each

*Each district zoom map also carries its canon landmarks once discovered (`Living-Map.md` rule 2) and its 5 Gazetteer streets/bridges.*

| District Zoom Map | 12 Venue Bank Labels (`INVENTED`) | Canon Pins Already in District (for reference) |
|---|---|---|
| **`map-zoom-old-city.png`** | 1. Evening Post Morgue · 2. Quintero's Key & Heel · 3. Bramwell Stationery · 4. St. Roch's Apothecary · 5. The Dripping Tap · 6. Gideon's Surplus · 7. Sable & Morrell Law · 8. Clockmaker's Lofts · 9. Sal's Chair & Shave · 10. Coach-House Garage · 11. Harrow & Sons · 12. Mina's 4 AM Oven | Curios & Chronicles (`s00`), Ministry Field Office, Municipal Archive (burned), Dog-Route Corner, Taxidermist, Old City Cemetery |
| **`map-zoom-meridian.png`** | 13. Canteen on 4th · 14. Varga Concierge · 15. Deeds & Zoning Annex · 16. Vermeer & Slate PR · 17. Helios Wellness · 18. Pulse Electronics · 19. Glass Conservatory · 20. Sterling Safe & Deposit · 21. The Roast & Ledger · 22. Halcyon Suites · 23. Oakhaven Horology · 24. The Iron-Bell Gym | Emmerich & Daughter (`s02`), Ministry Scanner Station, Meridian Group HQ, Glass Building, Meridian Public Library |
| **`map-zoom-fairground.png`** | 25. Spin Cycle 24 · 26. Red Curtain Diner · 27. Alibi Props · 28. The Velvet Box · 29. Dr. Halpern's Clinic · 30. Quarter-Drop Arcade · 31. Quick-Ink Printing · 32. The Green Room · 33. The Projector Room · 34. Madame Vera's Palmistry · 35. U-Lock Storage · 36. Stagehand Union 404 | Fairground Grand Theater (`s01`), Fairground Hotel, The Starlight, 3 After-Hours Clubs |
| **`map-zoom-docks.png`** | 37. Dr. Oduya's Harbor Vet · 38. Pike's Marine Pawn · 39. The Rust Bucket · 40. Harbor Cold-Chain · 41. Salty Pete's Bait · 42. Kerrigan Welding · 43. Salt Flats Wrecking · 44. Customs & Manifest · 45. *M.V. Albatross* Barge · 46. Gantry Coffee · 47. Pier 3 Radio · 48. St. Brendan's Mission | Eastern Pier (`s03`), Eastern Drainage Tunnels, Ministry Bio-Containment / Cold Storage, Pier 9 Lockers *(never pin Apex Black Site!)* |
| **`map-zoom-overhang.png`** | 49. Overhang Community Hall · 50. Hillside Hardware · 51. Terrace Pharmacy · 52. Calloway Auto & Tire · 53. The Overlook Diner · 54. The Watch Shed · 55. Gina's Dry Cleaning · 56. Post 88 Social Club · 57. Mrs. Alverez's Flat · 58. Nurse Hester's Parlor · 59. Tannery Row Newsstand · 60. Castellan Garage | Ashby House (`s03`), Agnes's House (12 Calloway), Calloway Alley, Overhang Playground, Empty Apartment |

---
