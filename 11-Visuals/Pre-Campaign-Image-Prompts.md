---
entity_type: Generator
name: "Pre-Campaign Image Prompts"
purpose: "Ready-to-paste prompts for Gemini image generation. Generate before Session 0 for player handouts and GM reference."
image_style: "Industrial-occult noir — fractured amber and cold blue, film grain, quiet unease"
---

# Pre-Campaign Image Prompts

Generate these before Session 0. Save outputs to `11-Visuals/_Saved-Images/`.

---

## How image generation behaves — field notes *(from Gemini, 2026-11-17; **verify by testing** — Gemini flagged parts as uncertain and has invented details before)*
**Adopted (they match problems we actually had):**
- **Consistency:** re-attach the **anchor image(s) every time**, even in the same chat — a chat only holds a face for ~1–2 turns, then drifts (this caused the Merton mismatch). Best: 2–3 references of one character (face close-up + full outfit), not one.
- **Left/right:** never "his right hand" (ambiguous). Say *"on the left side of the image frame, the hand holding the pencil."* (Cause of Thorne's ring on the wrong hand.)
- **Counting:** avoid exact counts above 3; describe items by position/state instead.
- **Targeted edits:** the app has no mask tool. Draw a red circle on the source and destination (e.g. both hands), re-upload, and say *"move the ring from the left circle to the right circle, remove both circles."* Otherwise it regenerates the whole image.
- **Short signs:** quote the exact words in CAPS, give the font and surface, **one sign per image**. Ampersands can blend into flourishes (ours worked).
- **Aspect ratio:** the Gemini *app* has no ratio control — state "16:9" / "3:2" in the prompt. If you edit with a 3:2 portrait attached, it may force 3:2; attach a blank 16:9 rectangle and say "use Image 2 only as the canvas size."
- **Seeds:** none in the app. To keep a *look*, attach a favorite image as a **style anchor** ("use Image 1 only for colour, grain and lighting").
**To test, only if needed:**
- **Borders / edge scratches:** words like "noir", "vintage", "film grain" pull in the look of scanned prints, and **negative phrasing ("no scratches") can summon what it names**. If a border returns, try a suffix variant: replace "Visible film grain" with "Subtle film grain" and end with *"Full-bleed, edge-to-edge clean digital frame."* (A/B it on a prompt that produced a border.) Don't change a suffix that is working.
- **Corner sparkle logo:** a visible mark on consumer-app images; developer endpoints (API / AI Studio) carry only the invisible SynthID mark. Our recent images are clean — **note which surface produced them and keep using it.** The invisible mark is always present. Prefer generating clean over cropping.

---

## Master Style Suffix

**Append this to the end of every prompt for visual consistency:**

> *Industrial-occult noir. Fractured amber and cold blue light sources cutting across rain-slicked surfaces — wet asphalt and glass fragmenting every light source into scattered reflections. Visible film grain, aged surface textures, micro-details on worn materials. A modern city built on century-old bones. Quiet unease — not horror. The world looks ordinary until the light hits it wrong. Clean composition, no text, no watermarks, no signatures.*

---

## Locations

### Curios & Chronicles — Exterior
Save as: `location-curios-exterior.png`

```
A narrow three-story brick building pressed between two glass-and-steel skyscrapers, viewed from across a rain-soaked sidewalk at night. A faded hand-painted sign above the door reads "CURIOS & CHRONICLES" in aged serif lettering — some letters slightly more faded than others. A cat silhouette resting on the counter inside, visible through the dusty single-pane window. The building occupies its footprint like an act of stubbornness — the towers lean slightly away from it.
A single warm amber lamp glows from inside the shop — the only warm light source on the block. Cold blue LED overflow from the flanking skyscrapers illuminates the facade from both sides. Rain fractures both light sources across the wet pavement below, creating layered amber and blue reflections.
Worn brick with century-old mortar lines, dust on the inside surface of the glass, the amber interior warmth against cold blue exterior — visible film grain across the entire frame. Quiet defiance. A building that decided not to update itself and has been winning that argument for a hundred years.
Clean composition, no text, no watermarks, no signatures.
```

---

### Curios & Chronicles — Containment Suite
Save as: `location-containment-suite.png`

```
A clinical underground room centered on a zinc-topped surgical table with heavy leather restraint straps bolted to each corner. Along the far wall, a bank of stainless steel drawers with thin engraved markings on each face. A massive lead-lined vault door with a row of small mirrors flush in the front face occupies the left wall. Original stone foundation visible at the base of the walls behind modern fixtures.
Harsh overhead fluorescent panels — the kind that render color incorrectly and make everything look post-mortem. Cold white light with no warmth. Near the drawer bank, a faint cold vapor where the temperature differential meets the room air — a barely visible fog at knee height.
Zinc surface scratched in irregular patterns that suggest intention, leather straps stained and softened with repeated use, clinical stainless steel with no fingerprints. Pale cold color palette — whites, grays, and the dull silver of metal. Institutional coldness. A room designed to contain things that resist containment.
Clean composition, no text, no watermarks, no signatures.
```

---

### The Subway — Main Hall
Save as: `location-subway-main-hall-v2.png` *(v1 = `location-subway-main-hall.png`, the shadow-monster version — keep as an alternate)*

```
A vast vaulted underground transit hall in a wide 16:9 composition, the size of a train station, with a cracked Art Deco tiled arched ceiling disappearing into green shadow high above, and a floor of pale old-bone-colored tile. The hall curves gently out of sight in both directions like a runway. A hand-drawn transit map hangs on the far wall, with one line marked in newer, brighter red ink. A mixed crowd of commuters in coats and suits walks and waits, all with eyes down, no one looking at the camera or at each other. Hidden among them, quiet details that are wrong: a man in a suit on a bench reading a newspaper with his shoes on backwards; a woman in a bright yellow coat laughing with her companion, whose hand has too many fingers; a teenager in a school uniform asleep against a pillar with a backpack in his lap, his shadow stretching in the opposite direction from every other shadow in the hall. In the far corner, almost lost in the shadows, a stack of old leather luggage with brass clasps, shown small. In the distance, one dim lit stall with a striped awning, and a back booth deep in shadow.
Light is a cold, greenish ambient glow with no visible source, like the light inside a fish tank, evenly lying across the tile and the people with no fixtures in sight. A faint wash of green on every surface. Very few warm lights at all, perhaps one dim amber lamp over the distant stall. The people cast shadows that don't quite agree.
Cracked tile with original gold leaf in the arches, worn stone floor with paths worn by thousands of feet, wet-looking reflections on the floor, long-ago painted station lettering too faded to read. Eerie bureaucratic normalcy: a place that has always existed and does not require acknowledgment. Keep the lower-left of the frame clear of important detail, with only floor and legs.
Clean composition, no text, no watermarks, no signatures.
```

---

### The Meridian — Emmerich's Shop
Save as: `location-emmerichs-shop.png`  *(v2 2026-11-18 — 16:9, exact sign text, suffix included)*

```
A 16:9 wide cinematic night shot of a narrow old stone building on a wet city street, seen from the pavement looking up at its second-floor window, which glows amber. A gold-leaf sign painted on the window glass reads "EMMERICH & DAUGHTER" in a classic serif, with nothing else written on it. The lettering has aged unevenly: "EMMERICH" is bright and recently touched up, while "& DAUGHTER" is faded and flaking almost to nothing. Through the rain-streaked glass a single elderly man, a warm silhouette, is bent over a worktable and does not look up.
Warm amber light from one desk lamp inside casts the man as a silhouette against the window. The street below is lit by cold blue LED streetlamps. Rain on the glass breaks the amber light into small elongated reflections on the wet pavement.
Old gold-leaf paint on glass with uneven aging, a single-pane window with interior condensation, stone facade with wrought-iron window details, a closed shop on the ground floor below. Amber against cold blue: the warmth of work happening long after reasonable hours.
Industrial-occult noir. Fractured amber and cold blue light sources cutting across rain-slicked surfaces — wet asphalt and glass fragmenting every light source into scattered reflections. Visible film grain, aged surface textures, micro-details on worn materials. A modern city built on century-old bones. Quiet unease — not horror. The world looks ordinary until the light hits it wrong. Clean composition, no text, no watermarks, no signatures.
```

---

### Fairground District — Theater Exterior
Save as: `location-fairground-theater.png`

```
An old theater marquee filling the upper frame on a rain-soaked street at night — the marquee reads "THE FAIRGROUND GRAND" in corroded brass lettering, some neon tubes still active, some dark. A side door propped open with a brick at street level, slightly ajar. Below street level, a single fluorescent light visible through a narrow basement window — barely brighter than the surrounding dark, creating a thin cold strip at ground level.
The active neon marquee tubes cast fractured magenta and amber reflections across the wet pavement below, multiplied in the puddles. Cold blue from the surrounding street. The basement fluorescent creates a separate cold ground-level light source. Rain catching and multiplying every source.
Corroded brass lettering with green oxidation in the recesses, worn theater facade brick with layered old poster remnants, oil-slicked wet pavement showing the building's reflection distorted. Melancholic history with something still operating in its basement. A building with more below ground than above.
Clean composition, no text, no watermarks, no signatures.
```

---

## NPCs

### Merton — Human Form
Save as: `npc-merton-human.png`

```
An older man in a pressed security uniform, three-quarter frame, seated alone in a theater basement break room. Both hands wrapped around a thermos, completely still — the stillness of someone who has held this exact position for hours. A keychain barely visible at his belt — a small photograph behind yellowed plastic, too small to read.
A single overhead fluorescent tube — one end flickering slightly — providing harsh top-down light that leaves the upper face partially in shadow. His eyes catch the light at the wrong angle, producing a faint amber reflection that should not be there from a fluorescent source.
Pressed uniform with eleven years of careful maintenance visible in the creases, weathered hands with prominent knuckles wrapped around the thermos, worn break room chair with foam visible at one corner. The expression of someone exhausted by a vigil they cannot explain and cannot stop. Grief worn smooth by repetition.
Clean composition, no text, no watermarks, no signatures.
```

---

### Merton — True Form (Barghest)

> **Generate Merton — Human Form first. Upload that image as a reference when generating this one.**

Save as: `npc-merton-true-form.png`

```
A large figure seated on a concrete floor with its back against the basement wall — taller than a man even seated, limbs elongated, the security uniform torn at every seam where the body beneath has changed. The face is clearly not human: an elongated canine muzzle and jaw pushing forward from a human skull, the skull narrower at the temples and longer front-to-back than a person's — the proportions of a large hound, not a man. Thick neck, deep-set eyes beneath a narrowed brow, coarse black fur covering most of the face and neck. Both hands cradling an old leather dog collar in its lap, head bowed over it. Camera at eye level or slightly above — not a low angle. Not facing camera.
A single overhead industrial fluorescent light casting top-down light across the bowed head and broad shoulders. Eyes directed downward toward the collar — not visible, not glowing. Cold blue tinge on the far basement wall. The leather collar catches a point of reflected light from the concrete floor below.
Torn uniform fabric split at the shoulders and chest, coarse black fur with visible individual hairs where the fabric has given way, worn leather collar with a brass buckle the only bright point in the frame. The posture is collapsed inward — the weight of something that has stopped fighting. No aggression, no threat. A creature sitting with something it has held onto for two hundred years. Grief readable through posture alone.
Clean composition, no text, no watermarks, no signatures.
```

---

### Emmerich — wiki portrait FIRST (anchor), then table scene *(v2 2026-11-18)*
**Step 1 — wiki portrait.** Attach `location-emmerichs-shop.png` so he matches the man in the lit window. Save as `wiki-emmerich.png`. Publish only after the crew has met him.
```
A 3:2 landscape waist-up portrait of Emmerich, an elderly tailor, subject centered with the head about one-third from the top, facing the viewer in a calm three-quarter turn, against a plain softly-lit dark workshop wall. He is the same man as the elderly tailor seen at the worktable in the attached image: mid-seventies, short thinning white hair combed straight back, a deeply lined face, steady pale-grey eyes, no glasses. He wears a white shirt with the sleeves neatly rolled to the forearm, a dark waistcoat, and a yellow cloth tape measure draped around his neck. His expression is patient and attentive, not smiling, the look of a man who has finished a great many last orders.
Soft warm amber light from the left on his face, a faint cool blue rim light on the right shoulder from a rain-streaked window out of frame.
Fine wool waistcoat fabric, rolled linen cuffs, the tape measure's worn numerals, deep skin texture. Nothing happening behind him.
Industrial-occult noir. Fractured amber and cold blue light sources cutting across rain-slicked surfaces — wet asphalt and glass fragmenting every light source into scattered reflections. Visible film grain, aged surface textures, micro-details on worn materials. A modern city built on century-old bones. Quiet unease — not horror. The world looks ordinary until the light hits it wrong. Clean composition, no text, no watermarks, no signatures.
```
**Step 2 — table scene (same chat, re-attach the portrait). Save as `npc-emmerich.png`.**
```
A 16:9 cinematic medium shot of the man in the attached portrait, Emmerich, at his tailor's worktable. Both hands rest on dark wool cloth, measuring it with practiced precision; a silver thimble is on the index finger of his right hand, which is in the foreground of the image's right half. The posture of someone who has done this task ten thousand times with no loss of attention. He does not look up.
A single amber desk lamp to his left; the pool of light ends sharply at the table edge. A rain-streaked window behind him lets in diffuse cold blue light from the street, rimming his right shoulder and the back of his head.
Fine fabric under precise hands, the silver thimble catching a small curved amber reflection, a worn worktable with old pin marks and chalk at the edges, shears with aged wooden handles.
Industrial-occult noir. Fractured amber and cold blue light sources cutting across rain-slicked surfaces — wet asphalt and glass fragmenting every light source into scattered reflections. Visible film grain, aged surface textures, micro-details on worn materials. A modern city built on century-old bones. Quiet unease — not horror. The world looks ordinary until the light hits it wrong. Clean composition, no text, no watermarks, no signatures.
```

---

### Elias Thorne (Ministry Liaison / Mimic Face)
Save as: `npc-elias-thorne.png`

```
A trim man in a charcoal field coat on a rain-slicked city street at night, facing camera in a slight three-quarter angle. Perfect posture. Open, earnest expression — the expression of someone genuinely pleased to see you. A plain silver ring on his right hand, slightly too large for the finger wearing it.
An amber streetlamp positioned above and slightly behind him — warm light on the top of his shoulders and the back of his coat collar. His face lit primarily by diffuse upward reflection from the wet pavement below — an unusual, subtly wrong direction for a light source to come from. The combination produces warmth that arrives from the wrong angle.
Fine charcoal field coat with practiced collar and precise button spacing, rain catching on his shoulders, the silver ring catching the streetlamp as the only bright point on his hands, wet pavement reflecting an elongated and slightly distorted version of him below. Warmth with an unidentifiable wrongness underneath it. The feeling of someone who already knows your name.
Clean composition, no text, no watermarks, no signatures.
```

---

### PTOLEMY *(v2 2026-11-18 — 16:9, suffix included; attach `location-subway-main-hall.png` so the hall matches)*
Save as: `npc-ptolemy.png`

```
A 16:9 cinematic wide shot of a stack of three mismatched old leather travel cases in a corner of the underground transit hall shown in the attached image, with the largest case at the bottom and the smallest on top, filling the lower left of the frame. The brass clasps on the top case are latched in a deliberate pattern, each one angled with intention, like a sentence. Far behind them, commuters cross the hall and every one of them is facing away from the luggage.
Greenish fluorescent overhead light from the transit hall, institutional and unflattering. The light seems to reach the luggage reluctantly, leaving a small pool of relative shadow around the cases. The brass clasps catch the green light as dull warm points.
Aged leather with faded travel labels from cities that are not on current maps, brass clasps with deliberate patina: green in the recesses, polished where fingers have touched them, visible leather micro-texture. Ancient intelligence in a mundane container, in this corner longer than the station has existed and intending to stay.
Industrial-occult noir. Fractured amber and cold blue light sources cutting across rain-slicked surfaces — wet asphalt and glass fragmenting every light source into scattered reflections. Visible film grain, aged surface textures, micro-details on worn materials. A modern city built on century-old bones. Quiet unease — not horror. The world looks ordinary until the light hits it wrong. Clean composition, no text, no watermarks, no signatures.
```

---

### Mara Halliday (The Innocent)
Save as: `npc-mara-halliday.png`

```
A young woman in a worn canvas jacket pausing at a rain-slicked street corner at night, three-quarter frame. A canvas bag over one shoulder. A small notebook open in her hand, not being written in — she is looking at something just outside the right edge of the frame with an expression that is calculating, not frightened.
Amber streetlamp from the left creating warm sidelight on her face and the open notebook page. Rain on her jacket shoulders. The street behind her receding in cold blue and reflective wet pavement. Her expression is clearly lit — this is the moment a pattern clicks into place.
Worn canvas jacket with fieldwork stains at the elbows and cuffs, notebook pages with dense small handwriting visible at the edges but not readable, damp hair, the posture of someone who has just found the thread and is deciding whether to pull it. Curiosity that has just become something more dangerous than curiosity.
Clean composition, no text, no watermarks, no signatures.
```

---

### Aldric Voss (Twice-Born — The Technician)
Save as: `npc-aldric-voss.png`

```
An older man in a worn corduroy jacket seated in a radio station control room, facing slightly away from camera at three-quarter angle. Headphones on. The room behind him filled with reel-to-reel equipment and analog consoles with hand-labeled tape strips — nothing updated since the 1970s. One hand resting lightly on a fader.
Amber instrument indicator lights across the console — many small warm points of light in an otherwise dim room. A single overhead incandescent bulb. The VU meters on the reel-to-reel lit in amber and red, needles moving. His face lit primarily by the ambient glow of the equipment.
Worn corduroy at the elbows, analog knobs with faded marker tape labels, reel-to-reel tape in motion with visible tape path, the accumulated weight of equipment that has been continuously running. The expression of someone who has been listening to the same warning for sixty years and has not found a reason to stop. Tired, permanent vigilance.
Clean composition, no text, no watermarks, no signatures.
```

---

### Senna Calder (Twice-Born — The Librarian)
Save as: `npc-senna-calder.png`

```
An older woman in a mended cardigan seated among floor-to-ceiling filing boxes in a dimly lit underground archive. Both hands holding separate documents simultaneously, cross-referencing without marking either — the efficiency of someone who has done this specific task ten thousand times. Reading glasses worn but not appearing to be used for vision.
A single portable desk lamp on the table beside her — warm but narrow pool of light that ends sharply. The filing boxes extend into shadow in all directions. Her face half-lit by the lamp, half by reflected light bouncing off the documents in her hands.
Cardigan repaired in at least three places with slightly mismatched thread, aged document paper with yellowing edges, filing boxes with handwritten labels in multiple different handwriting styles spanning decades, the deliberate organization of a space made navigable entirely by memory. Custodial purpose. A life organized around information that cannot be made public.
Clean composition, no text, no watermarks, no signatures.
```

---

### Cosma Linden (Twice-Born — The Teacher) — wiki portrait FIRST (anchor), then table scene *(v2 2026-11-18)*
**Step 1 — wiki portrait.** Save as `wiki-cosma-linden.png`. Publish only after the crew has met her (S2).
```
A 3:2 landscape waist-up portrait of Cosma Linden, a woman in her late sixties, subject centered with the head about one-third from the top, facing the viewer in a calm three-quarter turn, against a plain softly-lit dark wall. Grey-streaked dark hair pinned loosely up with a pencil, a warm, weathered, kind face with laugh lines and steady dark eyes, no glasses. She wears a long wool coat in muted plum-brown with deep patch pockets that bulge visibly with whatever is inside them, and a soft grey scarf. Her expression is patient and fully present, the look of someone who has explained frightening things to frightened people for decades.
Soft warm light from the left on her face, a faint cool green rim light on the right shoulder. Nothing happening behind her.
Wool coat texture, pockets pulled out of shape by their contents, fine lines on her hands, a faint pencil smudge on one knuckle. Nothing else in the frame.
Industrial-occult noir. Fractured amber and cold blue light sources cutting across rain-slicked surfaces — wet asphalt and glass fragmenting every light source into scattered reflections. Visible film grain, aged surface textures, micro-details on worn materials. A modern city built on century-old bones. Quiet unease — not horror. The world looks ordinary until the light hits it wrong. Clean composition, no text, no watermarks, no signatures.
```
**Step 2 — table scene (same chat, re-attach the portrait; attach `location-subway-main-hall.png` too). Save as `npc-cosma-linden.png`.**
```
A 16:9 cinematic medium shot of the woman in the attached portrait, Cosma Linden, seated at a folding table in the underground transit hall shown in the second attached image, talking to someone across the table who is just out of frame on the left. Her hands are mid-gesture over the table, arranging something invisible on its bare surface, a habit she does not notice. Her coat pockets bulge with their contents. There are more empty folding chairs around the table than there should be.
Greenish fluorescent light from the hall overhead makes every skin tone slightly wrong. A warmer light from an indeterminate source near the table is just enough to make her expression readable: patient, focused, fully present.
Coat pockets distorted by what is in them, hands mid-gesture over a bare table, the posture of someone who has spent decades explaining frightening things and has never found a shorter route to clarity. The kindness of someone who knows exactly how serious it is.
Industrial-occult noir. Fractured amber and cold blue light sources cutting across rain-slicked surfaces — wet asphalt and glass fragmenting every light source into scattered reflections. Visible film grain, aged surface textures, micro-details on worn materials. A modern city built on century-old bones. Quiet unease — not horror. The world looks ordinary until the light hits it wrong. Clean composition, no text, no watermarks, no signatures.
```

---

### Greta Fenn — Ministry Field Compliance Officer
Save as: `npc-greta-fenn.png` *(table/TV image — Sessions 1–3, where Greta is in person at the bookshop. **Same Gemini chat as the wiki portrait; the portrait is already in the conversation, so the prompt refers to it instead of re-describing her.**)*

```
Using the woman in the portrait above as the exact character — identical face, hair, glasses, red pen, badge and coat — create a wide 16:9 scene of her inside a cozy cluttered second-hand bookshop at night. She stands at the old marble counter writing on a form on her clipboard without looking down at it; she is looking calmly straight at the viewer, mid-sentence, unbothered. A stack of Ministry forms sits on the counter with a red rubber stamp beside it, and a large grey cat sleeps on top of the forms. A brass lamp glows beside her. Behind her, a shelf of old books and a rain-streaked window with a cold blue city night.
Warm amber from the brass lamp on the right, cold blue spill from the rainy window on the left, a soft amber rim along her coat. Her face lit clearly and evenly.
Forms with ruled boxes (no legible text), a red stamp with a worn wooden handle, grey cat fur, old marble counter with coffee rings. The expression of someone who has already filed the supernatural under the appropriate section.
Clean composition, no text, no watermarks, no signatures.
```

---

### Consequence — The Bookshop Cat
Save as: `npc-consequence.png` *(v1 = orange tabby on the desk — keep as `npc-consequence-desk.png`; canon says Consequence is LARGE and GREY)*

```
A very large, solid grey cat, round and heavy, sleeping on a cluttered old wooden bookshop counter, filling the middle of a wide 16:9 composition. She is draped over a stack of old paperwork — a manila folder, a 1962 department-store catalog and a government notice — with one paw hanging off the edge and one ear half-turned. A small tag on her collar catches the light but its lettering is too small to read. She has the profound indifference of an animal that has never once been moved by anything. Behind her, a rain-streaked shop window shows a cold blue city night. A brass reading lamp on the counter lights her from the side.
Warm amber from the brass lamp on the right, cold blue spill from the rainy window behind her. Fur edged with amber light, soft shadow under her belly.
Dense grey fur with subtle darker tabby striping and a slightly lighter chest, a notched ear, long whiskers catching the lamp, a worn red collar with a brass tag. Paper edges curled and yellow, a coffee ring, rain beading on the glass behind. Warm, comic, completely unbothered. The only creature in the building who has never reacted to anything.
Clean composition, no text, no watermarks, no signatures.
```

---

### The Crossroads Broker
Save as: `npc-crossroads-broker.png`

```
A man in a gray suit and narrow tie seated alone in a back booth of an underground hall, facing camera. A drink on the table in front of him — untouched, condensation forming on the glass. He is looking up and slightly to the left, toward someone approaching. His expression is the expression of someone who knows how this conversation ends, has had it before, and has no impatience about it.
A single light source above the booth — warm, focused, like a booth lamp. The hall behind him darker and less defined, figures at distance. His face fully and evenly lit — no shadows obscuring his expression. The untouched drink reflects the booth light on its surface.
Gray suit with the slight sheen of fabric that has held its press for forty years, a narrow tie of a period that has passed, the condensation ring beginning on the table from the drink, hands resting flat — not clasped, not tense. Calm authority that predates the room. A man who arrived before the concept of this meeting existed.
Clean composition, no text, no watermarks, no signatures.
```

---

## Anchor Items & Relics

### The Leather Dog Collar (Merton's Anchor)
Save as: `item-leather-collar.png`

```
A weathered leather dog collar laid flat on a dark wet surface — extreme close-up, the collar filling most of the frame. A single brass buckle. The leather surface fills the composition from edge to edge, the buckle positioned at the right third.
A single directional light source from the left — casting a deep shadow to the right that renders every surface variation in the leather as distinct. The brass buckle catches the light as a single bright point against the surrounding dark.
Leather worn smooth at the adjustment holes from two centuries of repeated buckling and unbuckling, stitching intact in a way that suggests the material itself has refused to degrade, brass buckle with green oxidation settled into the engraving recesses, the surface texture of old leather — not cracked, just compressed and dense with age. An object that belongs to someone and has never stopped. Quiet persistence across two hundred years.
Clean composition, no text, no watermarks, no signatures.
```

---

### The Silver Thimble (Emmerich's Anchor) *(v2 2026-11-18 — 16:9, suffix included; attach `npc-emmerich.png` so the lamp and worktable match)*
Save as: `item-silver-thimble.png`

```
A 16:9 extreme close-up of a single small silver thimble standing upright on a worn wooden tailor's worktable, centered in the frame, the only object in the shot. The worktable surface fills the frame to the edges, its grain and wear visible in low-angle light. It is the same worktable and the same amber lamp as in the attached image.
One amber lamp from the left makes a curved band of reflection along the thimble's upper rim, with deep warm shadow falling to the right. The wood grain is sharp in the low light, showing wear patterns and old pin marks.
The silver is covered in micro-scratches from decades of use, the dimpled grip pattern catching the amber light in dozens of small points; old wood with chalk residue and a few pin punctures at the frame edge. An object kept with great care by someone who no longer needs to keep it. Nothing else on the table.
Industrial-occult noir. Fractured amber and cold blue light sources cutting across rain-slicked surfaces — wet asphalt and glass fragmenting every light source into scattered reflections. Visible film grain, aged surface textures, micro-details on worn materials. A modern city built on century-old bones. Quiet unease — not horror. The world looks ordinary until the light hits it wrong. Clean composition, no text, no watermarks, no signatures.
```

---

### The Casting Mask (Mimic's Relic — GM Only)
Save as: `item-casting-mask-GM-PRIVATE.png`

```
A theatrical mask on a completely dark background, centered, slight upward angle — as if the mask is resting on a surface below frame. Designed to fit any face: the features are precise but composite, suggesting many faces rather than one. The eye hollows are empty.
A single narrow overhead light source illuminating the upper surface of the mask — the forehead, cheekbones, and upper lip — and leaving the eye hollows in total shadow. No fill light of any kind. The contrast between the lit surface and the dark eye sockets is total.
The surface material is wrong in a way that is difficult to name — too smooth in some areas, micro-textured in others, as if it has been worn to a different consistency than its original material. The shadow in the eye sockets is darker than the surrounding dark. Worn to an indeterminate number of faces. Between museum artifact and wound. Something that has been used too many times to retain a single identity.
Clean composition, no text, no watermarks, no signatures.
```

---

## Maps

### City District Overview
Save as: `map-city-districts.png`

```
A hand-drawn city map filling the full frame — five districts labeled in clean serif type: Old City (narrow historic street grid), The Meridian (glass tower district), The Fairground District (theaters and entertainment), The Docks (industrial waterfront), The Overhang (dense residential). A small precise dot marking one location in Old City. The map drawn as if by someone who knows the city from the inside rather than from above.
Flat document lighting — as if photographed on a light table, slight amber warmth to the aged paper. Ink rendering dark and clear. Paper texture visible across the surface.
Aged paper with slight yellowing at the edges and fold lines, ink lines with varying weight suggesting the map was drawn in multiple sessions over time, muted amber and grey color palette with occasional cool blue for water features along the Docks edge. No compass rose — the city doesn't need one. A document that is official in format and personal in execution.
Clean composition, no text, no watermarks, no signatures.
```

---

## Session 3 — Tea and Consequences

### The Ashby House — Exterior
Save as: `location-ashby-exterior.png`

```
A late-Victorian townhouse on a residential street — three stories, managed ivy on the facade, curtains visible in the upper right window. Through the ground-floor front window, three clocks are just visible on the parlor walls and mantel, all showing the same time: 11:47. The front path is swept. A single teacup sits on the porch railing with nothing near it. The neighboring houses are ordinary. This one is slightly too still.
Late afternoon grey-cloud light, no direct sun, the street itself dim and flat — but the upper right window has a warm amber glow from inside that does not match the time of day. The light is on when it should not need to be.
Brick darkened by decades of city air, ivy trimmed rather than sprawling — tended by someone who cares about it. Curtains in the upper window catch light from inside in a way that suggests movement without showing any. Muted palette: grey stone, dark green ivy, amber window light as the only warmth. A house that looks lived-in but is not.
Clean composition, no text, no watermarks, no signatures.
```

---

### The Ashby House — Interior Parlor
Save as: `location-ashby-interior.png`

```
A Victorian parlor frozen in the mid-1980s. A mantelpiece clock stopped at 11:47. An armchair by the window with a knitting basket beside it — needles mid-row, work in progress, as if someone stepped away and will return. A tea tray on a side table with two cups, one used, one placed for a guest. Bookshelves along one wall.
Warm low interior light — a floor lamp in one corner, amber-toned, casting soft shadows. The stopped clock catches light on its glass face. Steam rises from the fresh teacup, backlit by the lamp.
Wallpaper with a subtle floral pattern that is slightly different at the edges of the frame than at the center — not dramatically, just enough to notice on second look. Heavy fabric textures — curtains, armchair upholstery, braided rug — all maintained and clean, nothing neglected. Amber and cream palette with occasional dark wood. The room has been kept as if someone intends to return.
Clean composition, no text, no watermarks, no signatures.
```

---

### Mrs. Mabel Ashby — Living Appearance
Save as: `npc-mabel-ashby-alive.png`

```
A woman in her seventies in a knitted cardigan, seated in a high-backed armchair. Hair pinned with a single thin silver needle. Her hands rest on knitting in her lap, needles paused. She is looking at something just past the camera — not at the viewer, at whoever is standing near the viewer. Her expression is the expression of a schoolteacher who has seen worse.
Warm interior light from a nearby floor lamp, catching the silver needle in her hair, one side of her face in soft amber light, the other in shadow.
The cardigan has the softness of years of wear. The needle in her hair is the sharpest, most precise object in the frame — silver against grey. Her posture is very straight. Muted warm tones: cream cardigan, grey hair, amber light. She looks like someone who owns the room, because she does.
Clean composition, no text, no watermarks, no signatures.
```

---

### Mrs. Mabel Ashby — True Form (Wraith)
Save as: `npc-mabel-ashby-wraith.png`

```
The same woman — same cardigan, same posture, same needle in her hair — rendered translucent. She stands beside the armchair rather than in it, slightly offset from where a person would stand. Her edges lose definition where light passes through her. She is looking at the needle in her hair, not at the camera. Her expression is the same. She is not frightening. She is just also this.
Cool grey-green light diffused from no visible source — the ambient light of a room that belongs to her. The silver needle still catches light despite her translucency, the sharpest element in the frame. The background shows through her at the edges — just enough, not more.
Translucency achieved through layered softness rather than absence — solid at center, fading at margins. Grey and cream palette gone cooler, the amber warmth of the living portrait replaced by a quieter silver-grey. The knitting basket still visible in the background, still mid-row. Nothing has changed except she is not entirely here.
Clean composition, no text, no watermarks, no signatures.
```

---

### Agnes Pell — The Neighbor
Save as: `npc-agnes-pell.png`

```
A woman in her late sixties on a front doorstep, holding a large ceramic soup tureen with both hands. She has brought her own ladle. She is looking at whoever opened the door with the expression of someone who has been bringing soup to this house for forty years and has decided not to revisit the details tonight. Her coat is sensible. Her hat is slightly wrong for the weather.
Flat overcast exterior light — a residential street in late afternoon with no sun. The tureen is warm and slightly steaming. Her face lit from above and softly from the tureen's reflective glaze.
A ceramic tureen with a domestic floral pattern, the ladle handle extending past the lid because she did not plan for the ladle carefully. Her expression is the expression of a woman who is staying until she has seen Mabel. The composition slightly close — she is in the doorway and does not require more room.
Clean composition, no text, no watermarks, no signatures.
```

---

### The Grief Jars
Save as: `item-grief-jars.png`

```
An open kitchen cabinet containing forty-three small glass jars in neat rows. Each jar sealed with dark wax and hand-labeled in careful small script. Front-row labels visible: "Tuesday, 1978." "Thomas's birthday, the good one." "The argument about the curtains — I was right." The jars are slightly warm — the light inside them has a faint amber quality that should not be possible in sealed glass.
Flat overhead kitchen light, functional and harsh, illuminating the cabinet clearly. The warm amber from inside the jars is its own source, cooler than the overhead, emanating from within.
Glass jars with the slight variation of handmade production. Wax seals in slightly different colors, applied at different times. Labels in consistent handwriting, applied carefully. The cabinet door itself labeled PRIVATE in capitals in the same hand, visible at the frame edge.
Clean composition, no text, no watermarks, no signatures.
```

---

### The Knitting Needle — Anchor Item
Save as: `item-mabel-knitting-needle.png`

```
A single thin silver knitting needle on a dark wood surface. A few strands of grey hair still clinging to it — not many, just enough. The needle is old and elegant: silver darkened with decades of handling, the point still precise. It is warm. The surface beneath it has the grain of wood that has been in a house for a long time.
A single narrow overhead light source, the needle lit clearly against the dark wood. The hair strands catch the light. Nothing else in the frame.
Silver with patina — not tarnished, darkened with use, the grip end worn smooth precisely where a hand held it for forty years. The hair strands are grey and fine. This is the kind of object that belonged to someone specifically.
Clean composition, no text, no watermarks, no signatures.
```

---

### The Subway — Schematic
Save as: `map-subway-schematic.png`

```
A transit map filling the full frame for a system called "Line 0" — lines that do not correspond to normal city geography, rendered in the visual language of an official transit authority. One line marked in red ink by hand, added after the original printing. Station names in small type: "Threshold," "The Still Point," "Last Platform," "Confluence," "The Mouth."
Flat document lighting with a slight greenish tint — as if the map has absorbed the light of the space it belongs to. Aged paper catching the light unevenly, slightly brighter at center, dimming toward the edges.
Printed lines with the precision of official cartography, the red handwritten addition slightly smeared — added in haste, or in poor light, or somewhere the pen didn't want to work. Paper with a greenish aging tint, the official printing fading at the edges. A document that is correct in format and wrong in content. The kind of map that looks authoritative until you try to use it to go somewhere.
Clean composition, no text, no watermarks, no signatures.
```


---

## Added in Review — Missing Key Images

*(All new. Use the Master Style Suffix. Save to `_Saved-Images/`.)*

### The Subway Entrance — the Railing in the Alley *(Session 2 — the big reveal)*
Save as: `location-subway-entrance.png`
```
A narrow city alley at dusk in a wide 16:9 composition, viewed from the street end looking toward a dead end of wet brick. Near the far end, a waist-high green-painted iron railing is set into the concrete and leads down a steep stairwell into darkness. Above the stairwell, a sign tiled in white ceramic, in the style of an old municipal subway station from the 1920s, reads "LINE 0 — ETHEREAL EXPRESS". In the middle distance, a businessman in a dark suit, seen from behind, walks at full stride with a phone to his ear straight through the railing and the sign, slightly translucent where the iron passes through him, completely unaware. The alley is otherwise empty and ordinary: a dumpster, a downspout, a puddle.
The only real light is a flat sodium-orange streetlamp behind the camera, lighting the brick and the wet concrete. The railing and the sign receive almost none of it. They look lit from within, with a cold, sourceless green on the tile that lights nothing around it. The green is faint and exact, not a glow or fog.
Cold-painted iron with tiny rust freckles, white tiles with hairline cracks and no manufacturer's mark, wet brick, a slick of orange reflections on the concrete. Green-white sign against orange dusk. A thing that should not be here, looking like it has always been.
Clean composition; the only legible text is the white-tile sign reading LINE 0 — ETHEREAL EXPRESS; no other text, no watermarks, no signatures.
```

### Gerald — The Bulldog With Human Hands *(Session 1 — comic reveal)*
Save as: `npc-gerald-dog.png`
```
A fawn English bulldog sitting very upright on a high wooden stool in a dim theater basement, looking straight at the camera with an expression of great goodwill; **two pale human hands** where his front paws should be, one raised in a polite wave, the other resting on his knee. A ghost-light bulb on a stand in the background.
Warm amber from the bare bulb on the left; cold blue spill from a stairwell on the right; gentle dust motes.
Folded skin on the bulldog's brow, careful human knuckles with a faint tan line at the wrist, scuffed stool, concrete, a hanging mop. The most sincere creature in the room. Comic and deeply sad at once.
Clean composition, no text, no watermarks, no signatures.
```

### Zoltar — The Machine *(Session 0, beat 3b — on the TV during the read-aloud)*
Save as: `location-zoltar-machine.png`
```
A tall, floor-standing fortune-teller booth, roughly seven feet high and about the width of a phone box — taller than a grown man — shown full-length from its base to its carved pediment, standing flush against a plain plaster wall in the back corner of a dusty second-hand bookshop. Shot from a wide, slightly low angle at roughly standing eye level, pulled back far enough to show the wooden floorboards, the booth's heavy plinth base, and the full height of the wall above it. Behind the front glass: a robed automaton in a turban with a painted beard, seated, brass hands resting on a velvet pedestal where fortune cards used to lie, glass eyes facing the viewer. Below the glass, a hip-height panel with a narrow brass coin slot giving off a very thin green glow and an empty card tray. The wall behind the booth is smooth and seamless except for a faint vertical seam on either side of the booth, as if the whole wall could slide back. An unplugged power cord coils on the floor. Atlases are stacked beside it, small and ordinary against the booth's height, and a bookshelf with hand-lettered OCCULT and FOLKLORE labels stands to one side.
A single warm amber lamp from the bookshop behind the viewer, casting a soft pool on the glass and leaving the corners dark. A thin, steady line of green light along the coin slot — the only green in the frame. Dust motes drift in the amber light. Faint reflections of bookshelves ripple across the glass front.
Cracked and flaking paint on the automaton's cheeks, a hand-painted beard with individual strokes visible, brass fingers worn bright where hands once rested, sun-faded red velvet, thick dust on the glass with one clean finger-streak near the slot, curling old gold lettering on the booth's frame too worn to read. A fortune that has not been told yet. Wry, patient, slightly menacing — a machine that has been waiting to be asked.
Clean composition, no text, no watermarks, no signatures.
```

### Harlan's Diner — Exterior *(Session 4)*
Save as: `location-harlans-diner.png` *(Session 4 — the approach; no people)*
```
A wide 16:9 shot of a lone 24-hour roadside diner at night in steady rain, forty minutes from any city, with nothing around it but dark fields and a distant tree line. A chrome-trimmed silver railcar diner with a flat roof and a single half-lit neon sign reading HARLAN'S on the roof. Three battered pickup trucks and one motorcycle sit in the wet gravel lot, parked at careful angles. Warm yellow light spills from the windows with steam on the glass.
Warm yellow neon and window glow against cold blue rain-light, wet gravel reflecting both, a faint orange rim on the truck roofs. The glow is the only warmth for miles.
Chipped chrome, dented panels, a faded hunting-supply bumper sticker on one truck with no legible text, rain beading on the glass, a gravel lot pocked with puddles. A safe room that is not safe.
Clean composition; the only legible text is the neon sign reading HARLAN'S; no other text, no watermarks, no signatures.
```

Save as: `location-wall-of-the-missing.png` *(Session 4 reveal — the back wall of the diner; no people)*
```
A wide 16:9 shot of the back wall of a roadside diner covered floor to ceiling in a huge corkboard pinned with dozens of photographs of different people — hunters, in different decades, in work clothes and field gear — each photograph labeled with a small tag of case-number scribbles, with faded ribbons, pressed flowers and a few melted candle stubs on a shelf below. Most photographs are faded and curling. One photograph near the center is newer and sharper, with a short note beside it written in red ink in a hand unlike all the others. A single bare bulb hangs above, and a booth with a half-finished cup of coffee is in the foreground.
A single warm bulb from above, amber on the photographs, deep shadow in the corners, a thin cold blue line from the rainy window at the edge of the frame.
Yellowed photographs with curling corners, handwriting in pencil and pen layered over itself, pushpins of different ages, wax drips, a vinyl booth with a cracked seat. Quiet, reverent and slightly eerie; every face looking out is someone who did not come back.
Clean composition, no text, no watermarks, no signatures. (All handwriting is abstract scribble, no legible words; faces are indistinct and not detailed.)
```

### Renwick Stalls *(Session 3–4)*
Save as: `npc-renwick-stalls.png`
```
A nervous property developer in an expensive coat a size too large, holding two business cards in one hand, smiling a half-second too early; a pitch-deck folder under his arm; standing on a street of late-Victorian townhouses.
Cold overcast daylight; a warm window glow behind him in an old house.
Camel coat, new shoes that don't fit his stride, a tie slightly crooked. A man who has been told not to ask questions.
Clean composition, no text, no watermarks, no signatures.
```

### Drennick & Foss *(Session 2)* — three images, same chat, in this order *(v2 2026-11-18)*
Wiki portraits first (one per man; publish after the crew meets them), then the table scene with both portraits attached. No logos or lettering on their gear.

**1. `wiki-drennick.png`**
```
A 3:2 landscape waist-up portrait of Drennick, a tall, calm Apex Aegis peacekeeper in his mid-forties, subject centered with the head about one-third from the top, facing the viewer, against a plain softly-lit dark wall. Rain-pale skin, short dark hair combed neatly, a composed, unhurried expression with a hint of patient weariness, a small earpiece in his left ear. He wears a long dark wool coat with the collar turned up and holds a clipboard against his chest, one hand under it like a waiter holding a menu. Nothing written on the clipboard.
Soft cool blue light from the right, a faint warm amber rim light on the left side of his face.
Dark wool texture with fine beads of rain on the shoulders, the clipboard's worn clip, the curl of the earpiece wire. Nothing happening behind him.
Industrial-occult noir. Fractured amber and cold blue light sources cutting across rain-slicked surfaces — wet asphalt and glass fragmenting every light source into scattered reflections. Visible film grain, aged surface textures, micro-details on worn materials. A modern city built on century-old bones. Quiet unease — not horror. The world looks ordinary until the light hits it wrong. Clean composition, no text, no watermarks, no signatures.
```
**2. `wiki-foss.png`** *(v2 — v1 attached the Drennick portrait and Gemini copied his face. Start a NEW chat or do NOT attach Drennick; Foss must be a visibly different man: short, stocky, sandy buzz cut, ruddy, flat collar.)*
```
A 3:2 landscape waist-up portrait of Foss, a short, stocky, intense Apex Aegis peacekeeper in his late thirties, subject centered with the head about one-third from the top, facing the viewer, against a plain softly-lit dark wall. He is a completely different man from a tall pale slick-haired one: a broad square face with a heavy brow, a ruddy complexion, pale-blue narrowed eyes, a close-cropped sandy-blond buzz cut, a day of stubble, and a tightly clenched jaw. He is noticeably broad through the shoulders and a head shorter than the average man. He wears a long dark wool coat with the collar worn flat, and a small earpiece in the ear on the right side of the frame. He holds a clipboard flat against his chest with both hands, chin slightly lowered, like a charge sheet he is about to read aloud. Nothing written on the clipboard.
Soft cool blue light from the right, a faint warm amber rim light on the left side of his face.
Dark wool with fine beads of rain on the shoulders, white knuckles on the clipboard, the curl of the earpiece wire. Nothing happening behind him.
Industrial-occult noir. Fractured amber and cold blue light sources cutting across rain-slicked surfaces — wet asphalt and glass fragmenting every light source into scattered reflections. Visible film grain, aged surface textures, micro-details on worn materials. A modern city built on century-old bones. Quiet unease — not horror. The world looks ordinary until the light hits it wrong. Clean composition, no text, no watermarks, no signatures.
```
**3. `npc-drennick-foss.png`** *(attach both portraits and `location-meridian-street.png`)*
```
A 16:9 cinematic medium shot of the two men in the attached portraits walking along the rainy, upscale shopping street shown in the third attached image, mid-argument: Drennick, the tall, lean, calm one, holding his clipboard like a menu, and Foss, the shorter, broad, sandy-buzz-cut one, on his right, stabbing a pen toward the clipboard. Neither is looking at the people they are following, who are small and out of focus far down the pavement. A single smudged beet-red stain on Foss's cuff.
Cold blue streetlamp light and warm gold boutique windows behind them, wet pavement reflections.
Dark wool coats beaded with rain, matching clipboards, earpieces, one tall and lean and one shorter and broad, side by side. Dangerous and petty in equal measure.
Industrial-occult noir. Fractured amber and cold blue light sources cutting across rain-slicked surfaces — wet asphalt and glass fragmenting every light source into scattered reflections. Visible film grain, aged surface textures, micro-details on worn materials. A modern city built on century-old bones. Quiet unease — not horror. The world looks ordinary until the light hits it wrong. Clean composition, no text, no watermarks, no signatures.
```

### Dev & The Last Stop *(Session 3+, Subway)*
Save as: `npc-dev-last-stop.png`
```
A small café stall on a Subway platform: a barista in a green apron with a warm face making a drink for a customer with no visible mouth; shelves of mismatched mugs; a chalkboard that reads "WE'RE OUT OF THE CONCEPT OF OAT MILK."
Warm amber under a hanging bulb inside the stall; greenish sourceless Subway light on the platform behind.
Chipped mugs, steam, a hand-lettered chalkboard. A moment of kindness underground.
Clean composition, no text, no watermarks, no signatures.
```


---

## Added in Review (Round 2) — More Missing Prompts

### Bernard — The Theater Janitor *(Session 1)*
Save as: `npc-bernard-janitor.png`
```
A late-fifties theater janitor in a worn cardigan over a gray work shirt, standing half-inside a narrow backstage supply closet, holding a string mop across his chest like a rifle. Medium shot. One hand grips the closet doorknob, ready to pull it shut; his expression is a mix of profound dignity and a man who has decided that whatever he just saw is above his pay grade.
A single warm amber ghost-light bulb from the stage casts long shadows across worn red lobby carpet; cold blue fluorescent light spills from an open basement door behind him.
Threadbare carpet worn to the backing, a galvanized mop bucket on casters with soapy water catching the amber light, peeling backstage paint. Comic and tender at once.
Clean composition, no text, no watermarks, no signatures.
```

### Harlan Okafor *(Session 4)*
Save as: `npc-harlan-okafor.png` *(table/TV image — Session 4 debut. **Same Gemini chat as his wiki portrait**; the Wall of the Missing is its own image, shown later.)*
```
Using the man in the portrait above as the exact character — identical face, hair, beard, scar, apron and dish towel — create a wide 16:9 scene of him behind the counter of an old roadside diner at night in the rain, wiping a glass that is already clean, looking toward the front door and not at the viewer. A mug of coffee and a pie under a glass dome sit on the chrome-and-Formica counter, a coffee pot on the warmer behind him, a rain-streaked window with cold blue light. The wall behind him is plain and empty except for a menu board with no legible text — no corkboard, no photographs.
Warm yellow heat-lamp and tungsten glow over the counter against cold blue rain-light through the window; steam rising from the mug.
Chipped chrome, cracked red vinyl stools, steam on the glass, a counter worn pale where elbows have rested for decades. The only warm place for miles. A safe room that is not safe.
Clean composition, no text, no watermarks, no signatures.
```

### Deputy Director Alma Reyes *(Session 5)*
Save as: `npc-reyes.png`
```
A woman in her mid-fifties in a charcoal coat, standing at a bookshop shelf with a dry black umbrella and a manila folder, a capped pen held like a pointer; calm, intelligent, and very still.
Warm amber from the shop lamp on one side of her face; cold blue from the rainy window on the other.
Wool coat with a Ministry pin half-hidden by a scarf, an unmoving pen, damp shoulders. A person who has decided to be quietly dangerous in the right direction.
Clean composition, no text, no watermarks, no signatures.
```

### Director Arthur Vance *(Session 4+)*
Save as: `npc-vance.png`
```
A man in his sixties in a perfectly pressed gray suit sitting at a bare desk in a windowless office, reading a file while someone speaks to him; a single stamp and ink pad aligned with the edge of the blotter.
Flat cold fluorescent light overhead; a single amber desk lamp.
Pressed wool, a pen laid parallel to the folder, no photographs, no personal objects. Procedure as a personality.
Clean composition, no text, no watermarks, no signatures.
```

### The Bookmobile *(Session 0–1)*
Save as: `item-bookmobile.png`
```
A battered decommissioned bookmobile parked in a rainy alley behind the bookshop, hand-painted on the side in cracked cream letters: "C&C MOBILE LIBRARY — ASK ABOUT OUR LATE FEES"; one hubcap missing, a faded library-card decal on the windscreen.
Amber rear-door light from the shop spilling across wet cobbles; cold blue streetlight overhead.
Rust blooms on the wheel arch, faded paint, a dented fender, a book-return slot welded shut. A van that has outlasted four owners and will start on the second try.
Clean composition; the only legible text is the painted slogan on the side; no watermarks, no signatures.
```

### Subway Regulars *(Session 3+)*
Save as: `npc-officer-bram.png`
```
A stone gargoyle perched on a tiled pillar in a greenish-lit Subway hall wearing a small peaked cap, arms folded, an expression of weary formal disapproval; commuters pass beneath him without looking up.
Sourceless green light from above; warm amber from a nearby café stall.
Weathered stone with moss in the cracks, a tiny brass badge, the patience of three decades.
Clean composition, no text, no watermarks, no signatures.
```
Save as: `npc-madame-quill.png`
```
A theatrical woman in a velvet shawl behind a cluttered stall of glittering trinkets and "I ♥ LINE 0" magnets, holding up a snow globe that is snowing on a tiny Meridian; she is mid-pitch with arm outstretched.
Warm amber string lights over the stall; cold green Subway light behind.
Tarnished brass, velvet, tiny glass jars, a price tag in a looping hand. Gaudy, charming, slightly dangerous.
Clean composition, no text, no watermarks, no signatures.
```
Save as: `npc-wim-lost-and-found.png`
```
A soft-spoken clerk in a cardigan behind a long wooden counter stacked with lost things — umbrellas, a single glove, a lunch pail, glass jars each holding a small glowing something; he is holding up one jar and looking apologetic.
Warm amber from a desk lamp; cool green Subway light at the edges.
Brass counter bell, hand-lettered claim tags, dust, patience. A museum of everything anyone ever lost.
Clean composition, no text, no watermarks, no signatures.
```
Save as: `npc-ottilie-brand.png`
```
A sunny, reckless young hunter in a battered canvas jacket leaning on a Subway pillar and grinning, a pocket notebook (her scorecard) in one hand, a worn hunting knife and a sprig of dried herbs at her belt.
Warm amber from a café stall beside her; cold green Subway light behind.
Scuffed boots, a patch on her sleeve (a small brass lantern), an expression of happy competition. A person who keeps score and means it kindly.
Clean composition, no text, no watermarks, no signatures.
```

---

## Round 3 — Gap fill *(added 2026-11-17 audit)*

### The Fairground Grand — Auditorium & Ghost Light *(Session 1)*
Save as: `location-theater-auditorium.png`
```
The inside of a dark, shuttered old theater, viewed from the center aisle looking toward the stage. Rows of velvet seats fade into blackness. The stage is bare except for one bare bulb on a tall stand — a ghost light — standing alone at center stage. Stage left, a door painted the same black as the wall is propped open with a brick, a faint warm glow leaking up from a stairwell behind it.
The ghost light is the only real source: a small warm pool on the stage boards, everything beyond ten feet a rumor. Faint warm spill from the open stairwell door. Dust hanging in the air catches the bulb as slow drifting motes.
Faded red velvet seats with worn arms, gilded proscenium plaster flaking at the edges, rigging ropes disappearing into the dark overhead, scuffed stage boards with old spike-tape marks. Empty-room hush — a place where something happens at night. Mysterious with a hint of "someone is down there, and they're being very quiet about it."
Clean composition, no text, no watermarks, no signatures.
```

### The Meridian — Shopping District at Dusk *(Session 2 — the street and the Door Chase; v2 2026-11-18, attach `location-emmerichs-shop.png` so the tailor's window matches)*
Save as: `location-meridian-street.png`
```
A 16:9 cinematic wide shot of a busy upscale shopping street at blue-hour dusk, seen from the middle of the pavement. Boutique windows glow warm gold; a florist's buckets of flowers spill onto the damp pavement; on the far side of the street, a second-floor window with gold-leaf lettering reading "EMMERICH & DAUGHTER" glows amber, the same window as in the attached image. A revolving door at the left foreground is caught mid-spin with a faint blur of motion. Shoppers with bags walk past, none of them looking up.
Warm amber and gold from the shop windows against a cool blue dusk sky and cold blue LED streetlamps, with soft reflections on the damp pavement. The mood is polished and ordinary, a place where nobody would ever notice anything, with one detail slightly off: there are more doors along this street than the buildings could account for, such as a second revolving door beside the first and a plain door set between two shop windows.
Plate-glass shopfronts with brass trim, striped awnings, wrought-iron lamp posts, clean cobbles, window displays of tailored coats and perfume bottles. Upscale, inviting, faintly comic.
Industrial-occult noir. Fractured amber and cold blue light sources cutting across rain-slicked surfaces — wet asphalt and glass fragmenting every light source into scattered reflections. Visible film grain, aged surface textures, micro-details on worn materials. A modern city built on century-old bones. Quiet unease — not horror. The world looks ordinary until the light hits it wrong. Clean composition, no text, no watermarks, no signatures.
```

### The Pier — Where the Subway Lets You Out *(Session 2 exit; v2 2026-11-18)*
Save as: `location-pier-exit.png`
```
A 16:9 cinematic wide shot looking back along a weathered wooden pier from near its water end toward the land at early evening. At the far end of the planks, filling the right half of the frame, stands a plain brick wall with a faded painted advertisement of a cigarette pack on it, so weathered that no lettering can be read. The wall has no railing, no door and no sign, and it looks completely ordinary. On the left of the frame, across the harbor, the city skyline is a soft cutout against the sky. A single gull sits on a bollard in the foreground, and a tug is far out on the water.
Low violet-and-amber dusk light across the water, with cold blue shadows along the planks. The wall catches the last warm light.
Salt-stained pilings, wet planks with iron nail-heads, peeling brick with faded paint, drifting diesel haze over the water, a few lit windows across the harbor. Quiet, solitary, slightly eerie: the feeling of having just been somewhere impossible and being unable to prove it.
Industrial-occult noir. Fractured amber and cold blue light sources cutting across rain-slicked surfaces — wet asphalt and glass fragmenting every light source into scattered reflections. Visible film grain, aged surface textures, micro-details on worn materials. A modern city built on century-old bones. Quiet unease — not horror. The world looks ordinary until the light hits it wrong. Clean composition, no text, no watermarks, no signatures.
```

### The Hunters' Journal *(Session 0 — Containment Suite prop)*
Save as: `item-hunters-journal.png`
```
An old leather-bound journal lying open on a wooden reading stand beside a stainless-steel surgical table. Its pages are covered in overlapping handwriting from many hands — some in pencil, some in pen, margin notes crowded in between. One entry near the middle is written in red ink, a different hand from all the others, slanted and tidy, with a short line underlined twice.
Cool overhead surgical lamp light, flat and clinical, with a warmer reading-lamp glow pooled on the open pages. The steel table behind is out of focus, catching a thin line of reflection.
Cracked leather cover with a brass corner guard, thick yellowed pages with soft curled edges, coffee-ring stain on one corner, a ribbon bookmark, a ballpoint pen clipped to the spine. Layered, lived-in, passed down. The red ink is the only thing in the frame that doesn't belong, and it's the first thing the eye finds.
Clean composition, no text, no watermarks, no signatures. (Handwriting should be abstract scribble — do not render legible words.)
```

### The Scanner Station *(Session 0, beat 3d)*
Save as: `location-scanner-station.png`
```
A rolling metal cart half-buried in cabling against a brick wall in a cold underground workshop, carrying three modified shortwave radios with hand-wired knobs and strips of masking tape for labels. Beside them sits a fourth unit, older than the rest, with a single steady green lamp. A coffee mug and a spoon sit on the cart, a tangle of cables behind it. No person in frame.
Cool fluorescent light from above, flat and clinical, with the green lamp as the only saturated colour, throwing a soft green wash over the nearest radio dials and the brick. A faint amber glow from the radio dial displays.
Scuffed enamel, taped labels in marker, dust on the cable bundles, a coil of copper wire, a thin wash of visible static-like haze in the air around the green lamp. The feeling of a machine that has been listening for a long time and will keep listening. Mysterious and slightly lonely.
Clean composition, no text, no watermarks, no signatures.
```

### The Trophy Corkboard & the Hunters' Journal *(Session 0, beat 3e)*
Save as: `location-corkboard-wall.png`
```
A wide shot of a brick wall in a cold underground workshop covered by a huge cork board pinned with dozens of faded polaroid photographs, each with a scrap of paper annotated in red marker, connected here and there by red string. In the foreground, an old leather-bound journal lies open on a wooden reading stand beside a zinc-topped table. One page in the journal is written in a different, red ink.
Cool overhead fluorescent light on the wall, with a warmer reading-lamp glow on the journal in the foreground. The polaroids pick up small highlights. The red string and red marker are the only strong colour.
Yellowed polaroids with curling corners, pushpins of different ages, handwriting in pencil and pen layered over itself, a worn leather cover with a ribbon bookmark. Generations of work, shared. The earliest photos near the top are the faintest. Warm, lived-in, slightly eerie.
Clean composition, no text, no watermarks, no signatures. (All handwriting is abstract scribble, no legible words; the photographs show indistinct shapes, no clear faces.)
```

---

## Wiki Portraits *(rule: `00-Canon/Wiki-Update-Protocol.md` §3b — dedicated, spoiler-free, one per NPC)*
**Template:** `A 3:2 landscape waist-up portrait of [WHO], subject centered with the head about one-third from the top, facing the viewer or three-quarter turned, plain softly-lit [neutral setting], no props that carry plot, nothing happening behind them.` Then the usual 3 paragraphs, ending *Clean composition, no text, no watermarks, no signatures.* + the Master Style Suffix. Save as `wiki-<name>.png`.

### Greta Fenn — wiki portrait  *(generate FIRST — this fixes her face for every later image)*
**Consistency workflow:** generate this portrait until you love it. Then **stay in the same Gemini chat**, attach this portrait, and generate the bookshop scene below with *"Use this woman as the character reference — same face, hair, glasses, red pen and coat."* Re-attach the portrait for any later Greta image.
**Greta look block (reuse verbatim in every Greta prompt):** a woman in her mid-fifties with a neat, chin-length silver-grey bob with a side part; a long, lined, intelligent face with straight dark eyebrows and a firm, patient mouth; thin brass-rimmed reading glasses hanging on a black cord on her chest; a red pen tucked behind one ear; a Ministry badge on a lanyard with the photo and print too small to read; a heavy double-breasted Ministry-grey wool coat with wide notched lapels and dark buttons; a wooden clipboard.
Save as: `wiki-greta-fenn.png`
```
A 3:2 landscape waist-up portrait of a woman in her mid-fifties with a neat, chin-length silver-grey bob with a side part; a long, lined, intelligent face with straight dark eyebrows and a firm, patient mouth; thin brass-rimmed reading glasses hanging on a black cord on her chest; a red pen tucked behind one ear; a Ministry badge on a lanyard with the photo and print too small to read; a heavy double-breasted Ministry-grey wool coat with wide notched lapels and dark buttons; a wooden clipboard. She holds the clipboard against her chest with both hands and faces the viewer with the calm, slightly weary expression of someone who has found everything manageable. Subject centered, head about one-third from the top. Plain softly-lit pale institutional wall behind her, nothing else in frame, no props that carry plot.
Soft flat overcast-window light from the left, even on her face, gentle shadow on the right. No dramatic lighting.
Wool coat with a faint nap, the lanyard slightly twisted, a pen clipped to the clipboard, a faint crease between the eyebrows. Professional detachment as a complete worldview.
Clean composition, no text, no watermarks, no signatures.
```

### Harlan Okafor — wiki portrait  *(generate FIRST — it fixes his face; publish on the wiki only after he first appears, Session 4)*
**Consistency workflow:** keep this chat. After you love the portrait, make the diner-counter scene below in the **same chat** (portrait already in the conversation).
**Harlan look block:** a broad-shouldered man in his sixties with close-cropped grey hair and a short grey beard, deep lines around tired watchful eyes, a pale scar splitting his left eyebrow, forearms marked with old scars, a grease-stained apron over a rolled-sleeve flannel shirt, and a dish towel over one shoulder. *(Canon gives only "lived three lives, grease-stained apron"; I left ethnicity unspecified — add it here if you have one in mind, and the portrait will lock it in.)*
Save as: `wiki-harlan-okafor.png`
```
A 3:2 landscape waist-up portrait of a broad-shouldered man in his sixties with close-cropped grey hair and a short grey beard, deep lines around tired watchful eyes, a pale scar splitting his left eyebrow, forearms marked with old scars, a grease-stained apron over a rolled-sleeve flannel shirt, and a dish towel over one shoulder. His arms are folded loosely and he looks at the viewer with tired, watchful patience, as if he has just glanced at the door and decided you are probably fine. Subject centered, head about one-third from the top. Plain softly-lit warm cream wall behind him, nothing else in frame — no photographs, no corkboard, no counter, no props that carry plot.
Warm even tungsten light from the front-left, soft shadow on the right, a faint warm rim on the apron.
Faded flannel, apron stains, a dish towel with a worn hem, short grey stubble. A man who has lived three lives and kept the good parts of each.
Clean composition, no text, no watermarks, no signatures.
```

### Consequence — wiki portrait  *(cat anchor — generate in a chat where you attach the current grey `npc-consequence.png`)*
**Workflow:** attach `npc-consequence.png` (the large grey cat on the desk) and send the prompt below. Keep the resulting portrait as the reference for every later Consequence image, including fixing the cat in Greta's scene.
Save as: `wiki-consequence.png`
```
Using the cat in the attached image as the exact character — same large blue-grey tabby body and fur pattern, same notched ear, same worn red collar with a small brass tag — create a 3:2 landscape portrait of her sitting upright and facing the viewer with total indifference, centered, head about one-third from the top. Plain softly-lit warm wooden-counter-colored background, nothing else in frame — no paperwork, no lamp, no props that carry plot.
Soft warm lamp light from the right, gentle cool fill from the left, a thin amber rim along the fur.
Dense fur texture, long white whiskers catching the light, half-lidded amber eyes, one paw tucked beneath her. The only creature in the building who has never reacted to anything.
Clean composition, no text, no watermarks, no signatures.
```

