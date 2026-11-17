---
entity_type: Review_Log
last_updated: 2026-11-17
purpose: "Triage of Gemini's second-pass UI/UX review of the player site (Gemini suggests, Claude decides)."
---

# Gemini UI Second-Pass Triage — 2026-11-17

Every claim was checked against the source and screenshots; fixes were verified in a **local strict build** (`mkdocs build --strict`, Material 9.7.7) and re-screenshotted (copy icon checked over `http://127.0.0.1`, because `file://` doesn't inject Material's copy button).
This time Gemini's file/line references were accurate — but two of its fixes were wrong or unneeded (below).

| Gemini finding | Verified? | Decision |
|---|---|---|
| **HIGH** — lists/lines collapse into run-on paragraphs (Session-0-Agenda "Bring/Required"; Quick-Start "12 actions") | ✅ real (no blank line before lists). My scan found the same pattern in 5 more spots. | **Fixed** in Session-0-Agenda ×2, Character-Creation-Guide ×3, Downtime-Guide, Rules-and-Mechanics; Quick-Start 12 actions now one paragraph each. |
| MEDIUM — nested checklist renders **a–h** above the 1–8 template | ✅ real (`ul ol`, not `ol ol`; confirmed in screenshot) | **Fixed** — `.md-typeset ol ol, .md-typeset ul ol { list-style-type: decimal }`. Now 1–8. |
| MEDIUM — copy icon nearly invisible | ✅ real (live screenshot: faint grey square) — **but Gemini's selector was wrong**: Material 9.7 names the button `.md-code__button`, not `.md-clipboard`, so its CSS would have done nothing | **Fixed with the right selector** (both names covered): amber, always visible, blue on hover. Verified by screenshot. |
| MEDIUM — Light-mode hero kicker/CTA go brown on the dark hero | ✅ real (`.hero` missing from the "stays dark in both modes" rule; CTA uses `var(--se-amber)`) | **Fixed** — added `[data-md-color-scheme="default"] .hero`. Verified with a forced light-mode render. |
| MEDIUM — pills `~34px` tall; pill says `40m` but text says `45 minutes` | ✅ both real | **Fixed** — pills `min-height: 2.2rem` (44px at Material's 20px rem); pills now say `45m` on all 3 pages (Gemini suggested changing the text to 40; kept the more conservative 45). |
| LOW — Session 0 Agenda has no closing next-step box | ✅ | **Added** a short closing box linking Our Lair / Known Contacts / What Kind of Game. |
| LOW — move Session 0 Agenda under *Start Here*; hide the empty Campaign tab | opinion | **Declined** — would break the 1→2→3 step bar numbering; the Campaign tab fills after Session 1. |
| LOW — Greta banner crops her head on phones (`object-position: center 25%`) | ❌ not supported: the image is 1.84:1 and the phone banner box is 1.82:1, so almost nothing is cropped | **Rejected.** |

Not changed (Gemini's "do not change" list agreed): hero composition, FAQ cat photo, typography, 2-column tables, onboarding tone.
