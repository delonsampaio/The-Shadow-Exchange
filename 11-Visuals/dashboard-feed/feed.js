// LIVE DASHBOARD FEED — append-only. Written by the Co-GM through push.sh; read by GM-Dashboard.html every 2 s.
// Do NOT hand-edit. Each line below the header is one op with a unique, increasing seq; the dashboard applies each seq once.
// Reset to just the next line (and bump SAVE_VERSION in GM-Dashboard.html) at end of session.
window.DASH_FEED = { ops: [] };
DASH_FEED.ops.push({"seq": 1, "op": "scene", "beat": "1", "title": "The Pitch", "next": "Beat 2 — PC Introductions (music-bookshop-loop)", "note": "MOCK S0 — Now: Beat 1, The Pitch"});
DASH_FEED.ops.push({"seq": 2, "op": "scene", "beat": "2", "title": "PC Introductions", "next": "Beat 3a — Crew basics + the shop (map-city-s00)", "note": "MOCK S0 — Now: Beat 2, round-robin introductions"});
DASH_FEED.ops.push({"seq": 3, "op": "pc", "pc": 1, "name": "Ottoline Brack", "role": "Cutter", "note": "[MOCK-INVENTED] PC1 Ottoline Brack, Cutter"});
DASH_FEED.ops.push({"seq": 4, "op": "pc", "pc": 2, "name": "Rufus Penwright", "role": "Slide", "note": "[MOCK-INVENTED] PC2 Rufus Penwright, Slide"});
DASH_FEED.ops.push({"seq": 5, "op": "pc", "pc": 3, "name": "Linnea Sorrel", "role": "Lurk", "note": "[MOCK-INVENTED] PC3 Linnea Sorrel, Lurk"});
DASH_FEED.ops.push({"seq": 6, "op": "pcinfo", "pc": 1, "vice": "Gambling", "purveyor": "a bookie who works out of a laundromat", "note": "Ottoline: Gambling, laundromat bookie"});
DASH_FEED.ops.push({"seq": 7, "op": "pcinfo", "pc": 2, "vice": "Luxury", "purveyor": "a night-market cook (one perfect plum a week)", "note": "Rufus: Luxury, night-market cook"});
DASH_FEED.ops.push({"seq": 8, "op": "pcinfo", "pc": 3, "vice": "Stupor", "purveyor": "a retired lighthouse keeper with a still", "note": "Linnea: Stupor, lighthouse keeper"});
DASH_FEED.ops.push({"seq": 9, "op": "gag", "id": "nick", "note": "Ottoline = \"Door Prize\" (shoulders every door) · Rufus = \"Receipts\" (keeps every one) · Linnea = \"Silent Night\" (vanishes when it goes wrong)", "note2": "", "label": "PC nicknames"});
DASH_FEED.ops.push({"seq": 10, "op": "gag", "id": "lease", "note": "Rufus: the building signed it itself, and the three of them are the clause · Linnea: nobody signed; the building just kept them", "label": "Lease theories"});
DASH_FEED.ops.push({"seq": 11, "op": "scene", "beat": "2", "title": "PC Introductions (done)", "next": "Beat 3a — Crew basics + the shop (map-city-s00)", "note": "MOCK S0 — Beat 2 complete (players invented)"});
DASH_FEED.ops.push({"seq": 12, "op": "scene", "beat": "3a", "title": "Crew basics + the shop: city map", "next": "Shop exterior → interior (ATM)", "note": "MOCK S0 — Now: Beat 3a, the city map"});
DASH_FEED.ops.push({"seq": 13, "op": "scene", "beat": "3a", "title": "The Shop: exterior", "next": "Interior + ATM comedy beat", "note": "MOCK S0 — Now: Beat 3a, shop exterior (no district answer logged)"});
