# Opus Audit: Gap-Item Files (2026-11-21)

**Scope:** the nine new files, the Zoltar Season 2A–Waking sections, and the index edits, checked against Session-Boot, House-Rules, the SRD and the cited files. `consistency_check.py` prints **CLEAN** but cannot catch these. Re-audit H1–H5 are fixed; no form numbers were invented; the content rule is clean. **Report only.**

---

## BLOCKER

**B1. A teaching SAY line names the Mimic to the players.**
`00-Canon/Mechanics-Teaching-Ladder-S4-Plus.md:35` (card 21, read verbatim at S6): "It rises when the cover-up cracks: monsters leaking, exposure, **the Mimic's mischief**." The word "Mimic" is a GM secret (CLAUDE.md, Boot §4.2) and appears nowhere on the players' site (`spoiler-words.txt:3`).
**Fix:** "…monsters leaking, exposure, things the crew failed to contain." Also, line 35 ends "and the campaign ends". `Season-1-Plan.md:31` says Decay 6 "breaks the cover" and does not end the campaign. Change it to "At six the cover-up breaks."

## HIGH

**H1. Card 24 teaches the wrong way to lower Wanted.**
`Mechanics-Teaching-Ladder-S4-Plus.md:57`: CHECK "What do you do to lower it? *(Lie low, a favour, a bribe, or hand someone over.)*" The SRD (`Blades-in-the-Dark-SRD.md:1989`) and `Heat-and-Entanglements.md:10` say that **only incarceration** lowers Wanted. Lying low, favours and bribes lower Heat.
**Fix:** "*(Only one way: someone tied to the crew, or a framed enemy, is convicted. That gives Wanted −1 and clears Heat. Lying low and bribes only lower Heat.)*"

**H2. Card 22 gets crew advancement and the XP triggers wrong. It also contradicts the players' site.**
`Mechanics-Teaching-Ladder-S4-Plus.md:42` says "**8 XP buys a crew upgrade**" and lists XP sources as "triggers, Desperate rolls, and **one bonus**: beliefs…". The SRD (`:908`) and the players' `Downtime-Guide.md:56` both say a full crew track gives **a special ability or two upgrade boxes**. The SRD (`:885–889`) lists three end-of-session triggers, each worth 1 XP (2 if it happened a lot), and the third is struggling with vice or trauma. Desperate XP goes to the **attribute** track. Line 45 also says "keep it to three minutes", but in `End-of-Session-Ritual.md` the three minutes belong to the retrospective.
**Fix:** "…the crew's track, **8 XP**, gives a new crew special ability **or two upgrades**. End-of-session XP comes from three triggers, 1 each or 2 if it happened a lot: your playbook trigger; you expressed your beliefs, drives, heritage or background; you struggled with your vice or a trauma. A Desperate roll marks 1 XP in that action's attribute straight away." On line 45, delete "Keep it to three minutes".

**H3. The complication guide limits Resistance in a way that breaks House-Rules.**
`10-Generators/Entanglement-and-Complication-Cues.md:104`: "Offer a Resistance **only if harm is involved**." House-Rules §A ("Resistance", which ranks second) says the Co-GM offers it **after every consequence through Session 3**. The SRD lets players resist any consequence.
**Fix:** "Through S3 offer Resistance after every consequence (House-Rules A); from S4 the players call for it."

**H4. Two Wall names clash with bench NPCs.**
`03-NPCs/Wall-of-the-Missing-Roster.md:25` adds "Cal and Rudy **Brannigan**". **Holt Brannigan** is the Apex Cleaner lead (`NPC-Bench.md:124`, Venues #22). Line 26 adds "Dr. **Imogen** Frayne… in a lab coat", but **Dr. Imogen Halse** is the Apex research lead "in a lab coat" (`NPC-Bench.md:120`). The bench rule says to check names against the existing tables before inventing one.
**Fix:** rename them to **Cal and Rudy Mulvaney** and **Dr. Petra Frayne**. Update `NPC-Index.md:50` to match.

**H5. Hester Lyle, a standby, is used as a live NPC while Reyes is still active.**
`04-Locations/Sites-of-Interest/Old-City-Mercy.md:27` puts Hester in the S6 scene. `02-Factions/Ministry-Org-Chart.md:16,53` lists her as a usable "forgotten witness" face. But `NPC-Bench.md:10` says standbys "stay on the bench until the original NPC dies, leaves or is retired". Reyes is HINGE ONLY and alive through S27.
**Fix:** at Mercy:27, use an unnamed "Memory Remediation nurse (generic; not Hester)". At Org-Chart:53, write "a Remediation nurse (generic); Hester only if Reyes leaves".

## MEDIUM

**M1. The Season 1B cards contradict the Casting Mask.**
`03-NPCs/Season-1B-Cast-Cards.md:36` has Tamsin want "to understand why she **lost three years**". `The-Casting-Mask.md:35–41` says she was worn for **seven** years (the three years is how long she has lived in the same city since). Line 34 says the real Thorne "thought he had been 'retired'", but `Elias-Thorne.md:31` says he "has been trying to figure out who to tell for eleven years".
**Fix:** "…why she **lost seven years**". For Thorne: "**Secret:** he knows something took his life, but not what; nobody believed him."

**M2. The John Doe's "neutral" fragments point at particular Architect candidates.**
`Old-City-Mercy.md:35` gives three fragments: "A red pen" / "A ledger that kept writing after the page was full" / "Someone said: *sign here…*". A ledger points straight at Candidate B (PTOLEMY). A spoken offer rules out A (the Subway "cannot act directly", `The-Architect.md:26`). Yet the Architect must stay undecided until it is decided (Secrets #9).
**Fix:** replace the ledger fragment with "Red ink that was still wet years later". Replace the third with "A feeling of being *chosen*, like a name read off a list."

**M3. The Mercy choices contradict each other and use non-Blades rolls.**
`Old-City-Mercy.md:37`: "smuggle him to the Subway… **he never leaves the ward again**" contradicts itself. Line 34 asks for "a Fortune roll… *Mixed*… *Success*". Restoring his memory is the crew's action, so it needs a player's action roll. Blades has no "Mixed" result.
**Fix (37):** "…he is safe below; the Ministry loses his trail." **Fix (34):** "A player rolls Consort or Attune (Risky/Standard, or Controlled with the boat): 4–5 = a fragment and panic; 6 = what he saw."

**M4. A clipping renames the Fairground Hotel.**
`10-Generators/Urban-Legend-Clippings.md:19`: "THE **GRAND'S** FAMOUS NIGHT PORTER". Canon calls it the **Fairground Hotel** (`Urban-Legends.md:56`, `City-Districts.md:48`). "The Grand" is easy to confuse with the **Fairground Grand Theater**, Merton's venue.
**Fix:** "THE FAIRGROUND HOTEL'S FAMOUS NIGHT PORTER".

**M5. Wall photo #3 gives away Episode 4's plant.**
`Wall-of-the-Missing-Roster.md:20` puts the 1969 photo of Harlan's crew on the wall from S4. Episode 4's whole plant is finding "a 1969 photo of Harlan's lost crew" (`Season-1-Plan.md:112`). S4 is also already flagged as overloaded with five threads (Secrets §B, S4).
**Fix:** "#3: an **empty pin** with five ribbons; the photo turns up in Ep 4 *The Starlight*, then Harlan pins it. Gate: after Ep 4."

**M6. Two cue-grammar breaks in the Entanglement cues.**
(a) Line 58 marks Arrest "*No jokes*", but its read-aloud quip ("as many signatures… as people") and Greta's line at 60 ("which door has the better chairs") are jokes. She is also "not allowed in" yet speaks in the room. (b) Line 74 (Static Recall) says "the last **embarrassed** sentence one of you said", which assigns a feeling to a PC.
**Fix (a):** cut the signatures sentence. Change the SAY to "*(Greta — on the phone afterwards, quiet)*: 'I can't get you out. I can tell you who to call.'" **Fix (b):** "the last sentence one of you said aloud".

**M7. Kress's Squeeze clock does not match the Calendar and may never fill.**
`07-Clocks/Faction-Clocks.md:14` makes segment 1 "S7 Stalls exposed → Kress's letterhead". The letterhead is the crew finding Kress, not Kress noticing them. `Clocks-Calendar.md:37,42,46` ticks it at S6 (a Twice-Born protected), S11 (Artie freed) and resets it to 1 at S15. Segments 2–4 depend on crew choices, but the S12 freeze is a fixed spine beat.
**Fix:** use the Calendar's triggers and add "**S12 fills it regardless** (spine); S15 hand-over resets it to 1."

**M8. Index gaps: the procedures that run these files do not point to them.**
`Faction-Turn-Procedure.md` (Boot §5 "faction turn", `Session-Boot.md:180`) never names `Faction-Clocks.md`. `Heat-and-Entanglements.md` and Boot:172 ("roll the entanglement") never name the cue file. `Harlan-Okafor.md:36` never names the Wall roster. `Change-Propagation-Map.md` names none of the nine files, so an NPC death or a faction tick will not reach them.
**Fix:** add the following. Faction-Turn step 1: "…and `07-Clocks/Faction-Clocks.md`". Heat-and-Entanglements §2: "Read-aloud cues: `10-Generators/Entanglement-and-Complication-Cues.md`". Harlan:36: "Roster: `03-NPCs/Wall-of-the-Missing-Roster.md`". Change-Map: "NPC dies/leaves → Season-1B-Cast-Cards, Wall roster" and "faction clock tick → Faction-Clocks".

**M9. The Lethal-Path harm rule is an unlisted house rule.**
`05-Sessions/Lethal-Path-Quick-Table.md:15`: "**Level 4 = out**. Fatal harm only if the table accepts it." The SRD makes Level 4 catastrophic, permanent or fatal. House-Rules §A does not list this deviation, so by the priority line the SRD wins.
**Fix:** "Level 4 = catastrophic, permanent or fatal (SRD); offer Resistance first." Or, if the GM wants the softer rule, add it to House-Rules §A.

## LOW

- **L1.** `Lethal-Path-Quick-Table.md:29,33` (copying `Session-03-Prep.md:339`) says "a **Wanted check**". No such mechanic exists. **Fix:** "(Heat may reach 9 → Wanted +1)", in both files.
- **L2.** `Lethal-Path-Quick-Table.md:16`: Death Veil is a **crew special ability**, not a "playbook upgrade". Line 13 says to offer Resistance and "never skip it", but House-Rules says players call for it from S4. **Fix:** say "crew ability", and "Through S3 offer Resistance; from S4 remind once."
- **L3.** `Lethal-Path-Quick-Table.md:28`: Option B also opens through a jar (`Session-03-Prep.md:338`). **Fix:** "Parish Records, a jar, or a crit".
- **L4.** `Wall-of-the-Missing-Roster.md:20,30` puts stage directions ("*(wipes the counter)*") in the 🗣 SAY column. Line 33 has an empty "🔊 *a quiet moment*" with no text. **Fix:** turn the directions into a 🔊 line ("Harlan wipes the counter and says nothing.") and write the read-aloud for line 33.
- **L5.** `Wall-of-the-Missing-Roster.md:19`: "Pavel **Nowak**, Ministry cold-storage tech, brother of Tomasz **Wrona**". The surnames differ without explanation, and bench #11 has a private cold-storage *company*. `NPC-Index.md:50` says "All are missing hunters" (Pavel is not one; Harlan and Dasha are alive). **Fix:** "Pavel Wrona, a cold-storage loader"; in the index write "missing hunters and their people".
- **L6.** `Mechanics-Teaching-Ladder-S4-Plus.md:64` ("After S6: no new cards") conflicts with cards 23–24, which fire at first trauma or first Heat 9. The cards also lack the D&D bridge (Boot §4.8). Card 23 omits "fourth trauma = retire". **Fix:** "except cards 23–24 when first triggered"; add a bridge clause to each; add the retire line.
- **L7.** `Faction-Clocks.md:30`: "Never move a clock because the table is slow; use Faction Turn step 4" contradicts itself, because step 4 *is* the slow-table tick. **Fix:** "Outside the Faction Turn, never move a clock because the table is slow."
- **L8.** `Urban-Legend-Clippings.md:15`: the UL 3 body repeats the Tell ("stop at the same minute"), and per the Tell, kids don't play when adults watch. Line 18 (UL 6) repeats the Tell (the window). Line 14 labels UL 2 an "S9 option", but S9's options don't include it. **Fix:** cut the two Tell sentences; change the label to "flex job".
- **L9.** `Urban-Legend-Clippings.md:20`: UL 8 has no gate for "Emmerich alive" (Mini-Arc A). **Fix:** add "(only if Emmerich is alive; after S2)".
- **L10.** `Entanglement-and-Complication-Cues.md:82`: the Ministry Liaison note ("routes through Thorne's desk") is only true through S15. **Fix:** "S1–S15; from S16 the clerk is mundane." Line 33 ("Do you notice…?") and line 17 ("What does the neighbourhood do?") ask for perception or NPC choices; the SRD says Entanglements manifest fully. **Fix:** "What do you do about it?"
- **L11.** `Entanglement-and-Complication-Cues.md:48`: a 🗣 SAY for a written card. **Fix:** show it as a `note` card and read it as 🔊.
- **L12.** `Old-City-Mercy.md:33` asks two things in one ASK. **Fix:** "How do you get into Room 412?", then a separate ask.
- **L13.** `Zoltar-Card-Deck.md:86` ("Say nothing") conflicts with Boot §2a (fortune-card sting plus voice file). **Fix:** "Fire `music-sting-fortune-card` only; no voice line."
- **L14.** `Season-1B-Cast-Cards.md:24–26` files Valerie Crane under S12–15. A Co-GM at S12 may name her, but the S12 Regional Director is unnamed. Line 50's "one new name per session" breaks at S11 (Dasha and Artie together). **Fix:** move Crane to "Season 2"; add an S12 line: "the Regional Director: no name, no card"; write "…except a mid-arc climax".
- **L15.** `NPC-Index.md:46` still says "Planned (no file yet)" for the names that now have cards. Corvin Pryce and Councilman Pruitt have no card. **Fix:** "Planned (cards in Season-1B-Cast-Cards except Pryce, Pruitt)".

---

## What a fresh Co-GM would get wrong
Read "the Mimic" aloud (B1); say a bribe lowers Wanted (H1); sell a crew advance as one upgrade (H2); skip Resistance on non-harm complications (H3); mix up the duplicate Brannigans and Imogens (H4).

**Counts:** BLOCKER 1 · HIGH 5 · MEDIUM 9 · LOW 15 (total 30).
