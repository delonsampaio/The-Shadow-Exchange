// LIVE SCENE FILE — rewritten by the Co-GM during play. Read by 11-Visuals/Player-Screen.html every 1.5 s.
// EVERYTHING HERE IS SHOWN TO THE PLAYERS. No GM-secret information. Bump `rev` on every change.
//
// image      : path relative to 11-Visuals/  e.g. "_Saved-Images/location-curios-exterior.png"  (null = title card)
// caption    : lower-third title (location / NPC name); subcaption = optional italic line
// nowPlaying : track filename shown small bottom-right (cosmetic only — audio is played by fade-switch.sh)
// clocks     : PUBLIC clocks only — [{ name, total, cur, color }]   (never the Omen)
// card       : null | { style: "contract"|"newspaper"|"note"|"fortune"|"sign"|"recap", title, lines:[...], bullets:[...] }
//              ("recap" = session-start "Previously…": 1–2 short lines + max 2 bullets, from the PUBLIC player recap only. Keep every card to ~8 short lines — long cards spill.)
// crew       : null | { heat, coin, rep } — OPTIONAL small top-left strip of the three PUBLIC crew numbers. Show in free play / planning / downtime; set null when a score starts. Any other keys are ignored.
// banner     : null | "RUH-ROH?"   → big comic pop-up text for 2.6 s. Fires ONCE per (banner, bannerId). To re-fire the same text, increment bannerId; set banner back to null when done.
window.SCENE = {
  rev: 4,
  image: "_Saved-Images/location-curios-exterior.png",
  caption: "Curios & Chronicles",
  subcaption: "Old City · raining",
  nowPlaying: "music-bookshop-loop",
  clocks: [],
  card: null,
  crew: null,
  banner: null,
  bannerId: 0
};
