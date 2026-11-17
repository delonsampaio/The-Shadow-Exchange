# How Claude Triages Gemini's Review

**Gemini suggests. Claude decides.** When the GM pastes Gemini's output (or says "apply Gemini's review"):

1. **Verify before believing — including every quote.** (2026-11-17: in the spoiler check Gemini cited **five quotes that exist nowhere** — not on the site, not in the repo, not in git history — and misquoted a Harlan distance. `grep -F` every quoted line before acting on it.) For each finding, open the cited file(s) and confirm it is real (Gemini can misread, hallucinate a contradiction, or flag something already fixed). Mark any finding that doesn't check out **REJECT — not reproducible.**
2. **Classify every item** — one line each, with a reason:
   - **ADOPT** — correct and improves the campaign; apply it.
   - **ADAPT** — right idea, wrong fix (e.g., conflicts with the tone, the Teaching Ladder, or a GM decision); apply a modified version.
   - **REJECT** — wrong, already fixed, out of scope, or conflicts with a **GM-made decision** (e.g., safety tools stay removed; Subway first visit has no jokes; no commits unasked).
   - **ASK** — a genuine design fork only the GM can decide; list the options with a recommendation.
3. **Protect the guardrails.** Never adopt a suggestion that: reveals GM-private info to players; adds jokes inside the Subway first visit or during an Anchor choice; adds more than ~4 new mechanics to a session; or breaks the cue grammar in `Session-Boot.md`.
4. **Apply the ADOPT/ADAPT items**, then re-run the checks (stale-term grep, link check, cue coverage).
5. **Report** to the GM: a table of *Gemini finding → decision → reason → files changed*, plus any ASK items. Keep it short.
6. **Don't commit or push** unless the GM asks.
