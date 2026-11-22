> **Note (2026-11-21):** drafts 05/06/08/09 were promoted and 07 retired after this prompt ran; see `Gemini-Content-Bank-Triage-Log-2026-11-21.md` for their new paths.

# Gemini Content-Bank Cross-Check Prompt

Paste the block into Gemini (it has local file access). Claude triages the result per `Gemini-Triage-Protocol.md`: **Gemini suggests, Claude verifies and decides.** The content bank (NPC bench, Improv Kit, Venues Bank, Gazetteer, Bestiary, Zoltar deck, procedures) was written by several different agents on 2026-11-20/21 and has not yet been read against itself or against the many canon changes that followed. The five catalogs in `docs/review/draft-content/` (05–09) were written before most of those changes.

````
ROLE
You are a continuity editor and campaign-bible auditor for a tabletop campaign. You can read local files.

THE CAMPAIGN (short)
"The Shadow Exchange": Blades in the Dark, industrial-occult noir with Supernatural/Scooby-Doo comedy and real dread (the Menace Rule: monsters stay scary; no jokes while a real threat is on screen). A human GM plus three friends (20+ years of TTRPG experience, new to Blades) play weekly with an AI Co-GM; about 80 sessions in three seasons. Content rule: anything goes (gore, violence, cursing); the ONLY hard line is nothing racist and nothing that mocks a culture or a religion. Do not flag gore or swearing.
CANON TO CHECK AGAINST: the city has NO subway system (high water table; nothing is dug deeper than one pumped cellar); the Subway is magical, ghostly and addressless, and no train can be boarded before Arc IV (one pass-by train at S28); Decay never exceeds 3 in Season 1; the Ministry Audit clock is GM-secret until S4; Load is taught in Session 1 with Flashback (kit: `01-Crew/Hunter-Kit.md`); Heat 9 gives +1 Wanted and clears Heat (SRD); the Anchor Cover Rule (`10-Generators/Three-Layer-Monster.md`); "wrap it N" early endings (`05-Sessions/Express-Ending-Kit.md`).

READ (repo-relative)
THE CONTENT BANK: 03-NPCs/NPC-Bench.md, 03-NPCs/NPC-Index.md, 10-Generators/Improv-Kit.md, 10-Generators/Bestiary.md, 10-Generators/Urban-Legends.md, 10-Generators/Resonance-Complications.md, 04-Locations/Venues-Bank.md, 04-Locations/Gazetteer.md, 00-Canon/Zoltar-Card-Deck.md, 05-Sessions/Evergreen-Episodes.md, 01-Crew/Downtime-Menu.md, 02-Factions/Faction-Turn-Procedure.md, 07-Clocks/Heat-and-Entanglements.md, 00-Canon/House-Rules.md.
THE DRAFTS: docs/review/draft-content/04-Content-Ideas.md and 05-Anchor-and-Heirloom-Catalog.md, 06-Secrets-and-Reveals-Schedule.md, 07-Locations-and-Sites-Catalog.md, 08-Running-Gags-and-Forms-Register.md, 09-Clocks-Calendar.md.
THE TRUTH: 05-Sessions/Season-1-Plan.md, Campaign-Arc.md, Express-Ending-Kit.md, 06-Scores/Score-Catalog.md, 04-Locations/City-Districts.md, 02-Factions/, 03-NPCs/Active, Twice-Born and GM-Private, 00-Canon/_Dictionary.md.
ALREADY FOUND AND FIXED (do not re-report): docs/review/Mock-Audit-Log-2026-11-21.md, Opus-Beat-Audit-Report-2026-11-21.md, Gemini-Regression-Triage-Log-2026-11-21.md.

DO THIS
1. NAME AND ROLE CLASHES: list every name used for two different things across the content bank and canon (NPCs, venues, streets, creatures, firms, forms), and every pair of entries that fill the same role (duplicates worth merging).
2. TIMELINE CONFLICTS: any session number, season, clock value, NPC death/arrival or Tell that disagrees with Season-1-Plan.md, Campaign-Arc.md or the Score Catalog.
3. THE FIVE DRAFT CATALOGS (05–09): for each row that is now stale or wrong given the canon above (Audit clock, Load, Decay cap, Heat/Wanted, no-subway, Anchor Cover Rule, changed Tells, the kit, the venues), say what changed and the corrected row. Say which catalogs are worth promoting to real files and which rows to cut.
4. LEAKS: anything a player could see or hear (Zoltar cards, street scenes, rumours, NPC SAY lines, venue looks, bestiary "Appears as") that gives away a GM-private truth (the Mimic/Understudied, the Architect, Kress, Stalls = Apex, what the Omen is, what the Subway is, Thorne's tells).
5. LIVE USABILITY: for each file, can an AI Co-GM use it at the table without improvising (labelled, triggers stated, no dead ends)? List what is missing.
6. TOP 10 GAPS: the ten most useful things still missing from the content bank, ranked, each with the file it should live in.
7. RANK every finding BLOCKER / HIGH / MEDIUM / LOW with file:line and a concrete fix.

DELIVERABLE: the ranked findings (one line each), then the catalog promotion advice, then the top-10 gaps.

RULES
- Do NOT edit any files. Report only.
- Quote the line you cite; never invent a quote, line number or rule; say "unverified" when unsure.
- Do not re-report anything in the three logs above.
- No safety-tool pages; the GM never acts anything out; keep everything runnable by a GM reading live with an AI Co-GM.
````
