# Opus Re-audit — files changed since the beat audit (2026-11-21)

**Scope:** the 31 files in `git diff --name-only HEAD` (including the four promoted catalogs), read against Session-Boot, House-Rules, the triage log, Season-1-Plan, Campaign-Arc, the S0–S3 preps and the players' site (`../The-Shadow-Exchange-Players`, grep only). `scene.js` and `feed.js` were not opened. `consistency_check.py` prints **CLEAN**, but it cannot see the logic errors below. **Report only.**

**Clean on re-check:** the players' site has none of the renamed names (Iron-Bell, Amber Room, Pelham, #1147, 112 steps, 47-B(ii)) and no GM secrets. No live file still says Foundry Gym, Lantern Room, Bramley, "Bus #114", "114-step" or "Mimic-hive". The new File-Index and Change-Propagation-Map links resolve. The Decay ≤ 3 and Omen 5 ≈ S41 settings agree across Season-1-Plan:31, Active-Clocks, the Calendar, the Secrets schedule and the Anchor catalog.

---

## BLOCKER
None.

## HIGH

**H1. House-Rules gets the Entanglement dice wrong for Wanted 0 (the file ranks second in priority).**
`00-Canon/House-Rules.md:16` says "(Wanted 0 = 1 die, and so on)". The SRD, `07-Clocks/Heat-and-Entanglements.md` §2 and `Session-Boot.md:172` all say: Wanted 0 → roll **two dice and keep the lowest**; otherwise roll dice equal to Wanted. Every Entanglement in Season 1 will be rolled at Wanted 0. Because House-Rules outranks Heat-and-Entanglements, a fresh Co-GM will use one die and give harsher results than the SRD.
**Fix:** replace that parenthesis with "(dice = Wanted level; at Wanted 0 roll two dice and keep the lowest)". Add `Wanted 0 = 1 die :: SRD: two dice, keep the lowest` to `docs/tools/stale-phrases.txt`.

**H2. The Session 3 prep still puts Form 44-C on the table in S3, which breaks "Audit is GM-secret until S4".**
`05-Sessions/Session-03-Prep.md:62` says: "If [Clock: The Ministry Audit] is active, Greta Fenn arrives before the briefing with Form 44-C (Ongoing Premises Review)…" The new canon contradicts this: `Running-Gags-and-Forms-Register.md:50` (44-C is **S4+**), `Clocks-Calendar.md:18,47`, `Secrets-and-Reveals-Schedule.md:45` (#28) and `Active-Clocks.md`. The same prep's line 150 says "GM-secret until S4". If the crew used Double Bookkeeping in S1, the Co-GM follows line 62 and shows the players the Audit clock one session early.
**Fix:** rewrite line 62 as: "**Audit Check (🔒 GM ONLY):** if the Audit ticked, change nothing on screen; Greta visits only about the square footage. Form 44-C waits for S4." (This file is outside the diff, but the promoted catalogs created the conflict.)

**H3. The Forms Register says the Subway's first visit is in S3. It is in S2.**
`00-Canon/Running-Gags-and-Forms-Register.md:30` says "S3 first Subway visit (never S2)". The first descent happens in S2 (`Session-02-Prep.md:6,13,370,404`; Boot §4.5 "the first visit (Session 2)"). S3 is the *second* visit, and the regulars wait for it (`Subway-Regulars.md:4`). A Co-GM reading the register could skip the S2 Subway or treat S3 as the protected first visit.
**Fix:** "S3, the second Subway visit (regulars never appear on the S2 first descent)". In `03-NPCs/NPC-Index.md:34`, change "S3+ (never S2)" to "S3+ (second visit; never on the S2 first visit)".

**H4. The Bestiary #19 rename puts a Fairground monster in a Meridian venue that is already defined.**
`10-Generators/Bestiary.md:332` now reads "The Wager-Goblin of the Iron-Bell Gym". Line 334 says "**The Fairground District**", and line 336 says "a Fairground boxing/wrestling gym… elderly coach… slated to become a luxury juice bar". But the Iron-Bell Gym is `Venues-Bank.md:63` #24: **Meridian**, a third-floor loft above a garage, run by Dante Morales, with Castellan's Twice-Born hunter as a regular (the MA5 clue). Running #19 there merges two Anchor plots and can expose the S21 Castellan secret (Secrets #24) early.
**Fix:** give #19 its own Fairground gym, e.g. "The Wager-Goblin of the Brass-Bell Boxing Club (Fairground)". Add a note: "not the Meridian Iron-Bell Gym (Venues #24)". Add `Wager-Goblin of the Iron-Bell Gym` to stale-phrases.

**H5. The form numbers do not strictly rise in session order.**
(a) `Running-Gags-and-Forms-Register.md:71` puts **146** at "Ep 10". Episode 10 is the S9 option (`Clocks-Calendar.md:40` "Ep 10 option: Kress's routing"), which comes before **142-D** (S11, line 67), 143-K (S12) and 144-H/145-A (S16). The list at line 78 (…145-A, 146…) is therefore only true if Episode 10 runs after S16.
(b) `10-Generators/Improv-Kit.md:66` still says "continue the series after 47-B, 88-D and 91-C", and its gags use **104-F (l.67), 117-C (l.73), 129-M (l.78)**, all below 140-A. A Co-GM asked for "a Greta gag" at S8 would read Form 104-F after 141-J (S6), so the number goes backwards. `Improv-Kit.md:30` rumour "Form 140-A" has no session either.
**Fix:** (a) renumber Ep 10 to **141-B** (any session S6–S10), or say "146: only if Episode 10 runs after S16; otherwise use 141-B". (b) Change the §4 header to "Improv forms: take the **next free number above the last one used** (see the Register); 104-F / 117-C / 129-M are S1–S5 only." Add a "last number used" line to the Register for the Live Ledger.

## MEDIUM

**M1. A resolved Calendar flag still carries the proposal that would break the Decay cap.**
`07-Clocks/Clocks-Calendar.md:73` says "RESOLVED… Decay holds at 3", then keeps "*PROPOSAL:* make the S15 truce's +1 happen offscreen in S16–18…". A Co-GM could apply that +1, contradicting row 15 (l.45) and Season-1-Plan:31.
**Fix:** delete everything after "(Was: S15 truce + S28 overload = Decay 4 at S28.)" and add "The truce suspends the licence; the overload costs Twice-Born Favor −1."

**M2. The Register still points at the d8 card table it says was cut.**
`Running-Gags-and-Forms-Register.md:17` (Zoltar's cards) says "S4+ from the d8 table (map below)… never repeat a d8 card inside one arc". Line 35 says the d8 map was cut and the deck is the only source.
**Fix:** "S4+ from `00-Canon/Zoltar-Card-Deck.md` (one card per session, by mid arc)"; "never repeat a deck card inside one arc".

**M3. The Ministry Liaison complication contradicts the Casting Mask.**
`10-Generators/Resonance-Complications.md:21` says "the clerk is one more face of the single Mimic entity (Anchor Cover Rule applies)". The Mimic is the Understudied, who wears **Thorne's** face until S15 (`_Dictionary.md:33`). The Mask has had three faces in 21 years (Anchor catalog row 9), and it is a **Relic, not an Anchor**. A second, simultaneous face breaks the S15 reveal's logic and the tells.
**Fix:** "🔒 GM ONLY: the clerk is mundane; the report is compromised because it routes through Thorne's desk (the Understudied). Never name it on screen."

**M4. The Black Cabinet sequencing note cannot be followed.**
`10-Generators/Bestiary.md:586` says "Black Cabinet first, Quarter-Drop only at Omen 3+". The Black Cabinet is "Season 2, pick 8" (l.584). Omen 3 arrives around S11, and the Quarter-Drop LINE 0 is gated only by Omen 3+ (`Venues-Bank.md:16,74`), so the Quarter-Drop usually comes first.
**Fix:** "Quarter-Drop's LINE 0 screen (Omen 3+, Season 1) comes first; the Black Cabinet (Season 2) must not reuse the LINE 0 image in the same arc."

**M5. A Zoltar card pre-empts Thorne tell 8.**
`00-Canon/Zoltar-Card-Deck.md:38` reads "*TWO HANDS SIGNED THE SAME NAME.*" That *is* tell 8 ("two Thornes on paper", `Campaign-Arc.md:91`, S12–13). The Venues gate forbids showing the signature mismatch before Tell 8. Mid-Arc 3 cards may play from S12.
**Fix:** add "*(only after Tell 8 has landed; log as tell 8, not a new tell)*" to card 3.

**M6. The Secrets schedule files Foss's S12 payoff under S14.**
`09-Threads/Secrets-and-Reveals-Schedule.md:63` (S14 row) carries the Foss note. The S12 row (l.61) has no mention of it, and a Co-GM prepping S12 scans that row.
**Fix:** move "Foss: 'For the record — I was right.' (beets payoff)" into the S12 row and delete it from S14.

**M7. The Downtime project shows the Audit clock to players before S4.**
`01-Crew/Downtime-Menu.md:21` "Pay the Ministry audit down" has no gate. Downtime runs from S1, so the players can pick it from the menu in S1–S3.
**Fix:** add "*(S4+ only; the Audit clock is GM-secret before S4)*".

## LOW

- **L1.** `11-Visuals/Living-Map.md:54` puts Agnes's house "next door to Ashby House" and pins it in `s03`. `03-NPCs/Active/Agnes-Pell.md:5` says "across from Mabel", and `Living-Map.md:29` shows that `s03` has only Eastern Pier and Ashby House. **Fix:** "across the street from Ashby House"; set the map column to "when first named (not on `s03`)".
- **L2.** `03-NPCs/Active/Zoltar-and-Consequence.md:20–21`: the retired d8 table now has 7 entries (1–6, 8). **Fix:** add "(d8: on a 7, reroll)" or renumber it as a d7 list.
- **L3.** `07-Clocks/Heat-and-Entanglements.md` (Audit-ticks line) counts "Show of Force by a Ministry sweep" as a Ministry row; `Session-03-Prep.md:150` leaves it out. **Fix:** add "Show of Force (Ministry sweep)" to S3 l.150.
- **L4.** `10-Generators/Improv-Kit.md:90` says "before that, Renwick Stalls' shop is the offer". Stalls has no shop; he makes a phone "investment opportunity" (S3) and is unmasked at S4. **Fix:** "before that, Stalls Holdings' 'investment opportunity' (S3–S7) is the offer".
- **L5.** `01-Crew/Downtime-Menu.md:14`: the project gives a cohort, but the text also says a cohort "costs two crew upgrades". It is unclear whether finishing the project pays that cost. **Fix:** "finishing the clock fields the cohort *and* takes the two crew-upgrade slots".
- **L6.** `docs/review/draft-content/02-NPC-Bench.md:50` and `03-Improv-Kit.md:21` still say "The Lantern Room" and are labelled "DRAFT", not superseded. The consistency checker skips `docs/review`. **Fix:** set their status to "SUPERSEDED by `03-NPCs/NPC-Bench.md` / `10-Generators/Improv-Kit.md`; do not use", as was done for draft 07.
- **L7.** `docs/review/Gemini-Content-Bank-Cross-Check-Prompt.md:15` still names the drafts by their old `docs/review/draft-content/05…09` paths. It is harmless as a record, but a re-run would point Gemini at files that no longer exist. **Fix:** add a note: "05/06/08/09 now live at their promoted paths".
- **L8.** `Running-Gags-and-Forms-Register.md:73` (147-B "Basement, Second", S22 elevator to Basement Two) runs close to the "nothing below one storey" lock. **Fix:** add "(impossible/Resonant: the elevator shows a button for a floor that is not there; nothing is dug)".

---

## What a fresh Co-GM would get wrong
1. Roll one Entanglement die at Wanted 0 (H1).
2. Show Form 44-C in S3 (H2).
3. Treat S3 as the first Subway visit (H3).
4. Run the Wager-Goblin inside the Castellan hunter's gym (H4).
5. Hand out Form 104-F after 141-J (H5).

**Counts:** BLOCKER 0 · HIGH 5 · MEDIUM 7 · LOW 8 (total 20).
