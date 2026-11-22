---
entity_type: Tracker
status: LIVE — the Co-GM appends one line per change during a real session; cleared at a **finished** session's close-out (Change-Propagation-Map §3); **kept across a Pause**. Never written in a mock.
purpose: "Survives a context reset and tells the end-of-session pass exactly which files to update."
---

# Live Ledger

Format: `S<N> · beat · what changed · files to touch after (from 00-Canon/Change-Propagation-Map.md)`

<!-- entries below this line; empty between sessions -->
