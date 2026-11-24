// LIVE DASHBOARD FEED — append-only. Written by the Co-GM through push.sh; read by GM-Dashboard.html every 2 s.
// Do NOT hand-edit. Each line below the header is one op with a unique, increasing seq; the dashboard applies each seq once.
// Reset to just the next line (and bump SAVE_VERSION in GM-Dashboard.html) at end of session.
window.DASH_FEED = { ops: [] };
