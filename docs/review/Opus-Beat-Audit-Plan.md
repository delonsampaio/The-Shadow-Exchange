# Opus Beat-by-Beat Audit — Plan (Sessions 0–3)

**Status:** READY TO RUN, not launched (cost: roughly 200k tokens, like the runtime review; the GM approves first). **When:** after the Session 1 mock finishes (so its findings are in the log). **After it:** Claude triages and fixes, then drafts the Gemini regression-check prompt.
**Why:** the 2026-11-21 mock of Sessions 0–1 found 25 defects that earlier static reviews missed, almost all of them *classes* of defect that probably recur in Sessions 2–3 and in later preps. Source list: `Mock-Audit-Log-2026-11-21.md`.

## Scope
`05-Sessions/Session-00-Prep.md` … `Session-03-Prep.md`, read beat by beat against: the Run Sheet, `Session-Boot.md` (§2–§5), `House-Rules.md`, `CoGM-Core-Instructions.md` (TV policy), `Mechanics-Teaching-Ladder.md`, `01-Crew/Hunter-Kit.md`, `10-Generators/Three-Layer-Monster.md` (Anchor Cover Rule), `Comedy-Playbook.md` (Menace Rule), the NPC files in each roster, and the images/music named (read the image files; compare each picture to the read-aloud it accompanies).

## The ten defect classes to hunt (each found at least once in the mock)
| # | Class | What to check | Mock examples |
|---|---|---|---|
| A | **TV state** | Every beat says what the TV shows; no stale image or card; cues on "go", never early; an image arrives with its read-aloud (a *reveal* image arrives with the reveal line, not before) | corkboard left up (1), card early (3), auditorium image after text (12), Gerald image would spoil the flip (13) |
| B | **Labelling** | Every spoken line is 🔊 READ ALOUD or 🗣 SAY; every comedy beat has narration labelled; the Cold Open is READ ALOUD in full | unlabelled comedy lines (2), Cold Open bullets (4) |
| C | **Narrated PC actions** | No read-aloud narrates what the players do, say or show; the table acts, then the NPC reacts | Bernard "looks at your cover story" (11) |
| D | **Missing "before" state** | Every reveal has the state the players saw before it (a human before the monster) | Merton as the man (16) |
| E | **First-appearance explanations** | Every mechanic and every public clock has a one-line explanation at its first appearance; max 4 lessons per session | Detection and Surge clocks (19), clocks as a tutorial (Ladder 17) |
| F | **Established items** | Everything a PC uses was shown, packed (kit/Load) or a Flashback | rune-thread (24), Load (25) |
| G | **Branches assuming a choice** | A line that depends on an earlier choice has a variant for every branch (no Gland, no collar taken, etc.) | Thorne's "gland" line (22) |
| H | **Lethal paths** | Every encounter has a "they fight to kill" block (clock, harm, consequences) | Merton's Subdue clock (20) |
| I | **Image ↔ text match** | The picture matches the read-aloud (pose, props, who holds what); mismatches are fixed in the text or logged as an image TODO | Merton true form (15), collar crack (21) |
| J | **Stall help** | Every planning/choice question has stall prompts (examples, a default pick); no blank page | Engagement Roll details (8) |
Also: **K** dashboard ids exist for everything the prep tells the Co-GM to log (7) · **L** canon (no subway, Decay ≤ 3 in S1, Anchor Cover Rule stated for every disguised entity, Menace Rule) · **M** `Bestiary.md`: every entry states its Anchor, where it is kept and how the cover slips without it.

## Method
1. Read `Mock-Audit-Log-2026-11-21.md` first (the 25 findings and the open TODOs).
2. For each session, one beat at a time: apply classes A–L, quoting the line (file:line) and the fix.
3. **Report only.** Write one file, `docs/review/Opus-Beat-Audit-Report-<date>.md`; touch nothing else; do not read or edit `scene.js` / `feed.js` (mock state).
4. Output: ≤ 2,500 words; BLOCKER / HIGH / MEDIUM / LOW with file:line, what a fresh Co-GM would do wrong, and an exact fix; then a count of findings per class and per session.

## Ready-to-run prompt (hand to an Opus subagent)
> You are a senior reviewer of a live-run tabletop campaign. REPORT ONLY. Read `docs/review/Opus-Beat-Audit-Plan.md` and `docs/review/Mock-Audit-Log-2026-11-21.md` in the repo `/Users/delonsampaio/Desktop/VSCode Workspaces/The-Shadow-Exchange`. Then audit `05-Sessions/Session-00-Prep.md` through `Session-03-Prep.md` beat by beat against defect classes A–M in the plan, reading the images and NPC files they cite. Verify every claim by reading the line. Write exactly one file, `docs/review/Opus-Beat-Audit-Report-2026-11-21.md`, in the plan's format. Do not edit any other file. Finish with a summary of under 200 words naming the path and the top five findings.

## After the audit
- Claude verifies each finding against the files, fixes what is clear, asks the GM only for real design choices, and re-runs `python3 -I docs/tools/consistency_check.py`.
- Then: the Gemini regression-check prompt (drafted by Claude), and optionally a mock of Sessions 2 and 3 using the same checklist.
- Open TODOs that the audit should close: clock first-appearance lines for S2/S3 (Audit clock); reconcile the Audit clock vs the Ladder's "S4+"; the optional images (`location-annex`, `location-merton-locker`, `npc-merton-reveal`).
