---
entity_type: Procedure
status: ADOPTED 2026-11-20
purpose: "The GM-side routine for the week between sessions, so a weekly 2–3 hour game never starts cold."
---

# Weekly Prep Checklist

## Day after a **finished** session (15 min)
*(After a Pause, nothing here runs except checking that the Night Log row and the Live Ledger are saved; the next sitting starts with "continue session N".)*
- [ ] Say **"end session"** to the Co-GM if it was not run; check the end-of-session checklist in `Session-Boot.md` §6 ran (the ritual, the dashboard feed, the recap).
- [ ] Ask the Co-GM for the **Faction Turn** (`02-Factions/Faction-Turn-Procedure.md`) and the **next lead** from the Score Catalog, using the table's "more of / less of".
- [ ] Publish the recap and update the players' site (`Wiki-Update-Protocol.md`); strict build passes; **say "push" only when you want it live.**

- [ ] **Nothing stale:** the Co-GM ran `Change-Propagation-Map.md` and `python3 -I docs/tools/consistency_check.py` printed CLEAN (ask it to run the check again if unsure).

## Four days before (the prep file)
- [ ] The next session's prep file exists, written to `Session-Writing-Rules.md` (one or two sessions ahead; Season Plan row).
- [ ] **Asset check:** every image and music file in the Run Sheet exists (`11-Visuals/ASSET-TODO.md`, `docs/Manual-Work-Queue.md`). Generate what's missing now, not at the table.
- [ ] Zoltar card chosen (`00-Canon/Zoltar-Card-Deck.md`) and, if you like, printed.

## Two days before
- [ ] Message the players: "Who is coming Thursday? Anything you want to do in downtime?" If someone is out, note House Rules (absent player).
- [ ] Print any handout the session needs.

## On the night (10 min before)
- [ ] Open `GM-Dashboard.html` and `Player-Screen.html` on the TV; confirm the title card.
- [ ] Say **"start session N"** (a new session) or **"continue session N"** (after a Pause); the Co-GM boots from `Campaign-Current-State.md`.
- [ ] If there's no prep: run `05-Sessions/Evergreen-Episodes.md`.

## Monthly
- [ ] Refresh the **Living Finale Envelope** (`Express-Ending-Kit.md` §6) after every mid-arc climax.
- [ ] Check the Score Catalog §E dread budget over the last ten sessions.
- [ ] **Repo size:** run `du -sh .git` in the campaign repo (it was ~1.0 GB on 2026-11-20; GitHub recommends staying under 1 GB and asks for a trim around 5 GB). Media (images, music, covers) is deliberately kept in git for now. **Trigger to act: at about 1.5 GB**, tell the Co-GM to move new media to Google Drive (git-ignore `_Saved-Images`, `_Saved-Music`, `_Album-Covers`; back them up with Drive for desktop). Note: git-ignoring stops *growth*; shrinking existing history needs a history rewrite, which is the GM's call.
