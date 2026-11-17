---
entity_type: Review_Log
last_updated: 2026-11-17
purpose: "Triage of Gemini's GM-Dashboard UI/UX review (Gemini suggests, Claude decides)."
---

# Gemini Dashboard UI Triage — 2026-11-17

| Gemini finding | Verified? | Decision |
|---|---|---|
| Batched feed ops render oldest-first; green "latest" line is the wrong op | ✅ real | **Fixed** — batch reversed (newest on top) |
| Stale `feedseq` silently drops ops after `feed.js` is reset | ✅ real | **Fixed** — if max seq < stored seq, reset to 0 |
| `reset saved state` re-ingests whatever is in `feed.js` | ✅ real | **Fixed** — records current max seq before reload |
| Panels below the 1080p fold; inactive clocks eat space | ✅ real | **Fixed** — compact spacing; Gags/Anchors/Tells/Taught now a 4-up row; factions 2×2 under clocks; Position strip moved right; 0/N clocks dimmed, near-full clocks amber, full red |
| Stress pips: no numbers, 1.28:1 empty contrast, no danger colour | ✅ real | **Fixed** — numbered, 7–9 red, count pulses at ≥7 |
| Dim label contrast (FRIEND/RIVAL/HEIRLOOM/role/×/footer) | ✅ real | **Fixed** — moved to -300/-400/-500 shades |
| 12 px −/+ targets | ✅ real | **Fixed** — 24 px buttons (crew, factions); clocks gained −/+ |
| Privacy: Omen, Heirloom pattern/stage, Thorne Tells on view | ✅ real | **Added** — one-key **P** veil (blurs those + secret feed lines; hover to peek) |
| Flash the changed widget | good idea | **Added** — 3.5 s amber ring on crew stat / clock / PC / faction / tell / gag / taught |
| Always show Co-GM feed box + "Last:" heartbeat | ✅ | **Added** |
| Copy-snapshot button | good idea | **Added** (footer) — Session-Boot §6 points to it |
| **Gemini's Position/Effect pills** | ⚠ partly wrong | **Rewrote from the SRD** instead. (My *old* table was also wrong: it said Controlled failures cause "no harm" and listed "Success: Standard" as a Position result.) Strip now matches SRD text; Desperate roll = +1 XP; Effect shown as separate. |
| CDN scripts blank the screen offline | ✅ real, already on TODO | **Deferred** — vendor React/Tailwind/Babel locally if you want offline play |

Verified by rendering at 1920×1080 in headless Chrome (screenshots kept outside the repo — they contain mock-session names).
