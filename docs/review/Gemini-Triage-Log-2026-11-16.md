# Gemini Second-Opinion — Triage Log (2026-11-16)

**Source:** `Downloads/Second-Opinion Campaign Review.rtf` (≈9,000 words). Every finding was verified against the files or the SRD before acting. **Gemini suggests; Claude decides.**

## Verified & ADOPTED
| Finding | Verified how | Fix |
|---|---|---|
| Wiki Character-Creation-Guide said **7 more dots** (BLOCKER) | read file | now: playbook's printed dots + **4** more |
| **Vice is one of the two free downtime activities**; extras cost **1 Coin or 1 Rep**; "pay coin or take Heat for lifestyle" isn't SRD | SRD lines 2136–2145 | fixed in S1/S2/S3, Cheat Sheet, Player-Reference, Running-Your-First-Score, Ladder, wiki |
| **Acquire Asset math was wrong** (6 = Tier +1, crit = +2; Tier 0 rolls 2d-take-lower; Parish Records was gated too hard) | SRD §Acquire asset | rewritten; assets re-quality'd; coin/friend routes added |
| **Desperate rolls earn XP** (never taught) | SRD l.883 | added to Ladder, Quick-Start, Player-Reference, Cheat Sheet |
| `fade-switch.sh` **looped every track** incl. stingers | read script | stingers/one-shots play once (auto by filename; `once`/`loop` override) |
| Player-Screen **re-fired banners and reset the image** on every update | read code | change-detection + `bannerId` |
| Session 3 sections **out of order** (Acquire Assets before the briefing; Pivot before Agnes) | `grep ^##` | reordered; Agnes now precedes the 🔴 Pivot, with an optional 🔴 coda |
| Session 2 Downtime and Tell-4 call sat **before the Subway** in the file | read | moved into the Closing Beat |
| PTOLEMY's S2 charges contained **jokes** (Subway first visit) | read | uncanny set; funny set moved to Session 3's second visit |
| Cosma: "**man** in the corner with the luggage" | read | fixed; her unprompted opening trimmed to two sentences |
| Cold Open prompts told Claude to restate **uncaught Thorne tells** | read | conditional: only if a player caught it |
| `[[What Kind of Game Is This]]` **dead wiki links** | filename check | `[[…|What-Kind-of-Game]]` |
| Leftovers: *Status of original Ashby*; *Mira/Tamsin*; *real Thorne "not retrievable"*; *Mabel known since 1994*; *"forty-year tenant"*; *Senna's 1943 card*; *Physick*; stale README/template/Tone paths | grep | all fixed |
| Tell 6 (ring) never appears in a scene | read | added to S1 Thorne entrance |
| Dashboard: standing capped at ±2; no Returned/Refused anchor status; PC names not editable | read code | ±3; +Returned/Refused; editable names |
| Public-Wiki lair stale; What-Kind-of-Game **spoiled Session 1** (collar + dog) | read | synced; replaced with non-spoiler examples |
| Contacts/Anchor-Ledger listed **Subway NPCs and Emmerich's thimble before they're known** | read | marked unlocked-later / cleared |
| Score-01-Merton stale (no Gerald/Surge) | read | updated |
| Session 0 Beat 4b **hardcoded "2 Stress"** | read | "6 minus your highest die" |
| Comedy: **bank-irony pause 1/5**; Consequence-on-staple repeat; "Buttons" too subtle; Kettle weak | audit | ATM-customer gag; Greta's REJECTED stamp; boutique cologne gag; Mabel's posture inspection |
| Surge gags landed straight after the tragic plea | audit | Gerald pulls **DO NOT PULL** lever as the transition |
| Reyes had no intro scene; Mara/Senna/Ghost Map vanished; Sessions 8–10 had no antagonist pressure | read Arc | scene + placements + Kress's squeeze |
| Missing prompts (Bernard, Harlan, Reyes, Vance, Bookmobile, 4 Subway regulars, 9 covers) | read | added |
| EC exchange rate conflict | read | 1 EC ≈ 1 Coin inside the Subway |
| Run Sheet beat numbering mismatch (S1); ❌ markers missing in scene bodies; stale asset notes | read | S1 table renumbered; **16 ❌ markers added**; notes fixed |
| Stale `GM-Dashboard.jsx` | exists | archived to `99-Workshop/` |
| Stings < Lyria's 30 s minimum | GEMINI.md | trim note added |

## ADAPTED (right problem, different fix)
- **Fourth Option (return the collar):** adopted the *mend* idea but as a **Tinker/Attune roll with graded outcomes**, with the Subway Workshop as the permanent fix hook (tied to the arc).
- **Gerald's hands:** adopted *permanent* (stronger identity) + Greta's **Form 47-B**.
- **Van:** adopted *owned from Session 0*; the Lair Upgrade now **armors** it.
- **Resistance in Session 0:** kept as **practice** (it's the best teacher), moved the Ladder's S1 entry to "reinforce"; fixed the hardcoded cost.
- **fade-switch:** auto-detect by filename rather than by `*loop*` only (several scene tracks should loop without "loop" in the name).
- **Arc "when players learn the Architect/Kress/Whisperer":** clarified the *name vs identity* and *hint vs proof* distinctions rather than moving dates.
- **Downtime block for Session 3:** adopted, adjusted for Vice-inside-two and Greta's "three-sleeve sweater."

## REJECTED / NOT NEEDED
- *"Replace Harlan with Greta in Contacts"* — Harlan stays (he's a wiki-established two-year contact); **Greta was added** alongside him.
- *"Move Entanglements to Session 2's Return Downtime"* — reordered inside Session 3 instead (after the briefing).
- *"Rename wiki collar example to a gargoyle with a union grievance"* — used a silver-locket example (no spoilers, no new gag competing with Gerald).
- *Comedy-Playbook "PTOLEMY (🟡)"* — **adopted** (it was a real error; fixed).

## Open (LOW — fix opportunistically)
- Session 0/2/3 Run Sheet "Trigger" column nuance vs inline/`go` in the body for 3–4 rows.
- `Run Sheet` omits `[PLAYER SCREEN]` banners/cards in the image column for S0–S3 (they're in the body).
- Possibly generate a **Session 2 Cold Open** and **Session 3 Cold Open** only after Session 1/2 are played (by design).
