# Player-Facing Spoiler Check — 2026-11-22 (Opus, report only)

Scope: the four channels players see or hear (the site, the TV, READ ALOUD/SAY, handouts and TV images) for S0–S3, the Zoltar deck to S28, against CLAUDE.md, `09-Threads/Secrets-and-Reveals-Schedule.md` and `Campaign-Arc.md` §5. Every item was checked against the exact line or by looking at the image. Nothing else was edited.

## BLOCKER

**B1. The GM repo is public on GitHub.** *Channel: site / repo.* `gh api repos/delonsampaio/The-Shadow-Exchange` returns `"private": false, "visibility": "public"` (last push 2026-11-22). Its `09-Threads/Secrets-and-Reveals-Schedule.md` and `03-NPCs/GM-Private/` are on `main`. The players' site is on the same account (`delonsampaio.github.io/The-Shadow-Exchange-Players`), so one click on the owner's profile shows the repo. `MAINTAINING.md:58` already calls it "the private campaign repo". *Touches:* every secret. *Fix:* now, run `gh repo edit delonsampaio/The-Shadow-Exchange --visibility private --accept-visibility-change-consequences`. Then check Insights → Traffic for outside views or clones. Forks: 0. Pages: none.

**B2. In S2, Aldric says he is the AM host.** *Channel: SAY.* `Session-02-Prep.md:450`: *"That's me. Has been for sixty years. I'm better now."* This line plays if a PC asks about the AM broadcasts. The image `npc-aldric-voss.png` (a radio workshop with reel-to-reel decks) and the S0 Scanner Station read-aloud (`S00:242`) practically invite that question. *Touches:* Secret #15 (reveal window S9–S25; Aldric's voice only after S9), and it contradicts `S00:244` ("Never identify him"). *Fix:* replace the line with 🗣 *"Lot of people listen to the radio."* and then silence. Keep the confession for the S9 Radio Signal.

## HIGH

**H1. The Crossroads Broker has Elias Thorne's face.** *Channel: TV image.* The faces in `npc-crossroads-broker.png` and `npc-elias-thorne.png` match: same nose, ears, hairline and closed-lip smile. The Broker looks like Thorne about 15 years older. Both go on the TV in S1–S2, and the S2 street beat puts Thorne back in the players' minds that same night. Experienced players will read it as "the same face in two places", which points straight at a face-taker (the Mimic) or links Thorne to the Subway. No prompt asks for the resemblance (grep for "resembl" or "same face" finds only Greta's references). *Fix:* regenerate the Broker with a clearly different face (age, build, hair, features). Add "must not resemble npc-elias-thorne" to the prompt.

**H2. Thorne's S1 debrief is overloaded, and the S1 Zoltar card states Tell 1 again.** *Channel: READ ALOUD and TV card.* In one beat:
- `S01:417` READ ALOUD: "thumbs a plain silver ring … slightly too loose". This breaks the Run Sheet rule at `S01:35` ("the ring, Tell 6, is worn, never pointed out").
- `:419` Tell 1 (he uses a PC's first name).
- `:425` Tell 2 (he mentions the basement).
- `:432` Gerald whines and hides behind the crew.
- `:526–527` the card **A MAN WHO KNOWS YOUR NAME HAS NEVER BEEN TOLD IT.**

The prep (`:528`) expects the players to read the card as being about Merton, but Merton never used anyone's name, so it can only point at Thorne. The card also counts as a Zoltar Thorne-tell, so a Mid-Arc 3 card on top of it breaks the deck's "at most one before S15" cap. *Touches:* Secret #1 and the tells. These are deliberate plants, but together they are too strong for S1. *Fix:* cut "— slightly too loose" from `:417`. Move this card to the Mid-Arc 3 slot as that arc's single Thorne card, and give S1 a General card (e.g. #3) or a new non-Thorne line. Keep Tells 1 and 2 and Gerald.

**H3. The printed S0 handouts give away the S1 and S2 Anchors.** *Channel: handouts.* Both files are printed and handed out at S0 (`S00:43`):
- `01-Crew/Hunter-Kit.md:15`: "Binding and mending Anchors (the Session 1 collar)".
- `00-Canon/Player-Reference.md:136`: "a thimble from a daughter, a leather collar from a first dog".

This spoils the S1 locker reveal, the Fourth Option ("mend it") and the S2 target before the envelopes arrive. *Fix:* in Hunter-Kit, change the line to "Binding and mending Anchors; stitching a ward shut". In Player-Reference, change it to "a pocket watch from a husband, a locket from a sister". Reprint both.

## MEDIUM

**M1. The word "audit" before S4.** *Channel: SAY and site.* `S02:269` has Foss say aloud: "Flagging Curios & Chronicles for a **compliance audit**". The site's `What-Kind-of-Game.md:63` says "A Ministry internal audit is more dangerous than a creature." *Touches:* Secret #28 (the Audit clock is GM-secret until S4). *Fix:* change `S02:269` to "for a compliance review". On the site, change it to "A Ministry inspection is more dangerous than a creature."

**M2. The narrator points at Thorne's tells.** *Channel: READ ALOUD.* These lines tell the players that a tell has just happened:
- `S02:142` "as though he had been told to expect you"
- `S02:146` "He looks for slightly too long."
- `S02:561` "silent for exactly one second too long"
- `S03:434` "silent for one second"

*Touches:* the rule against anything that tells players a tell exists. *Fix:* report only the fact. At `:142`, end the sentence at "nearest of you." At `:146`, write "He looks up at the gold leaf … then back at you." Delete the two silence lines and go straight to "The line clicks off."

**M3. The Mid-Arc 3 card mix can't follow the cap.** *Channel: TV card.* In `Zoltar-Card-Deck.md`, #1 (`:36`), #3 (`:38`) and #4 (`:39`) are all Thorne tells. #3 ("TWO HANDS SIGNED THE SAME NAME") nearly says there are two Thornes, and its note ("log it as tell 8, not a new tell") leaves it unclear whether it counts against the "at most one before S15" cap (`:11`). The arc has four sessions but only one non-Thorne card. *Fix:* state at `:11` that the cap includes S1's card and #3. Mark #1 and #4 "S15 only (after the unmasking)". Add two neutral Mid-Arc 3 cards.

**M4. General cards can slip in extra Thorne tells.** *Channel: TV card.* General #2 (`:17`, "…HAS A SECOND PAIR OF SHOES") hints at a second face. General #5 (`:20`, "BEWARE OF A MAN WHO OFFERS TO HELP") echoes Thorne's offer at `S02:151`. Both can play in any session, outside the cap. *Fix:* tag #2 "not before S15". Tag #5 "counts as the arc's Thorne card".

**M5. Gaps in the automated sweep.** *Channel: site.* `docs/tools/spoiler-words.txt` is missing Kress, Aldric / "AM host", "audit" (before S4), Pryce, Tamsin / Solano, Waking, hinge, and GM paths (`GM-Private`, `0[0-9]-[A-Z]`). Check E in `consistency_check.py` scans only `PLAYERS/docs/**/*.md`: not `mkdocs.yml`, and not the root `README.md`, `CLAUDE.md` or `MAINTAINING.md`. Also, the `Line 0` rule will block a valid post-S2 recap: the players read the sign (`S02:323`, and it is visible in `location-subway-entrance.png`). *Fix:* add those words. Scan the root `.md` files and `mkdocs.yml`. Narrow the rule to `Line 0.{0,40}(Waking|platform|board)`.

## LOW

- **L1.** *TV image:* in `location-corkboard-wall.png`, both pages of the open Journal are entirely in red ink. The read-aloud (`S00:258`) says "one of them in red ink", so the image overplays the Architect thread. *Fix:* regenerate with mostly pencil and pen and one red entry.
- **L2.** *TV image:* the transit map in `location-subway-main-hall.png` has red lines. The read-aloud (`S02:371`) mentions only one faint pencil line, and `:383` says the red Decay ink starts in S6. *Fix:* treat the red as an ordinary line colour or regenerate. Never describe it.
- **L3.** *TV image:* `item-leather-collar.png` sits on the Containment Suite's zinc table under a surgical lamp, but S1 Beat 7 (`S01:384`) takes place in the theater basement. *Fix:* show it only in Downtime, or use a caption only.
- **L4.** *TV image:* the mantel clock in `location-ashby-interior.png` does not read 11:47, contradicting `S03:205`. *Fix:* skip this optional image or regenerate it.
- **L5.** *TV card:* `S03:116` "LAST RECORDED HABITATION: 1991" is the year Thomas died, so it is a soft clue toward Option B. Acceptable as a deliberate plant. Keep it if intended.
- **L6.** *READ ALOUD:* the punchline at `S03:253` ("'For your blood sugar.'") comes before the ASK at `:255`, which uses the same punchline. Delete it from `:253`. This is a formatting bug, not a secret.
- **L7.** *Public repo:* the players' repo `CLAUDE.md:5` names `../The-Shadow-Exchange/00-Canon/Wiki-Update-Protocol.md`, which points readers to the GM repo by name. *Fix:* use the wording from `MAINTAINING.md:58` ("the GM's private notes").
- **L8.** *Handout:* `Player-Reference.md:161` "Cold Storage Locker (pauses biological spoilage)" sits close to S1's rule not to mention spoilage before S4 (`S01:391`). *Fix:* "keeps things cold".

## Verified clean

- **Site (`../The-Shadow-Exchange-Players`):** all 15 pages under `docs/` and `mkdocs.yml` (nav, site name). The secret-word grep finds only "audit" (M1). The site shows the AM voice, the red ink, Rule 6 and the lease theory, all deliberate and known to players per the schedule (#9, #13, #15, #25). No GM paths. Assets: `hero-curios.jpg`, `consequence.jpg`, `logo.svg` and `favicon.svg` have neutral names and contents, and no page uses an `<img>` or alt text. Git history (15 commits) has no secret words. `site/` is gitignored.
- **TV text, S0–S3:** contract cards (`S01:104`, `S02:109`, `S03:116`), banners (CONSEQUENCE!, DO NOT PULL, RUH-ROH?, BOO?), captions (The Annex, Consequence, Closing Time, Locker 7, Merton, The stage, The alley, Downtime, The basement stairs, Elias Thorne, Emmerich & Daughter, The Ashby House, Thorne's call), the Detection / Surge / Subdue clocks, and the S0, S2 and S3 fortune cards. The smudged "E." stamp stays in 🔒 only (`S02:111`).
- **Zoltar deck, Mid-Arcs 1, 2 and 4–6 and Reserve:** no secret is stated.
- **READ ALOUD / SAY:** no Mimic, Architect, Kress, Stalls = Apex, Omen name, Decay or Audit clock in spoken text. "Stalls Holdings" (`S03:137`) and "LINE 0 — ETHEREAL EXPRESS" (`S02:323`) are planned plants. S0's Kress redirect (`S00:376`) is GM-only, and players cannot name Kress anyway.
- **Table Card (`11-Visuals/handouts/Table-Card.html`):** rules only.
- **Images checked (35):** all three city maps (the pins are public places, no Subway entrance), the exterior, Zoltar, the Suite (the vault mirrors show no faces), Scanner Station, Consequence, theater, auditorium, Bernard, Gerald, Merton (true form), Thorne (ring shown, not emphasised), Greta, Meridian street, Emmerich, thimble, Drennick & Foss, Subway entrance, PTOLEMY, Cosma, pier, the Ashby exterior, Mabel (living and wraith), jars, Agnes, needle, Stalls. No stray names, stamps or forms.

**Counts:** BLOCKER 2 · HIGH 3 · MEDIUM 5 · LOW 8.
