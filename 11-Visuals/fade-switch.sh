#!/bin/bash
# fade-switch.sh — fade out, switch track in QuickTime Player, fade back in
# Usage: bash fade-switch.sh "path/to/track.mp3" [auto|loop|once]
# STINGS (name contains "sting": SFX, spoken lines, comic stings) OVERLAY the playing scene music — the loop is never interrupted.
# Every other track is a scene song: it LOOPS until the next fade-switch (replacing the previous track).

NEW_TRACK="$1"
MODE="${2:-auto}"   # auto | loop | once | overlay   (auto: stings overlay; every other track loops)

# --- OVERLAY: any file with "sting" in its name (SFX, spoken lines, comic stings) is laid OVER the
# scene music. The loop keeps playing (ramped down to ~4% while the sting plays so the two never clash, then ramped back up) — it is
# never stopped, so no "music back" is needed. If nothing is playing, the sting just plays alone.
IS_STING=false
case "$(basename "$NEW_TRACK")" in *sting*) IS_STING=true ;; esac
if [ "$MODE" = "overlay" ] || { [ "$MODE" = "auto" ] && [ "$IS_STING" = true ]; }; then
  (
    PREV=$(osascript -e 'tell application "System Events" to set r to (exists process "QuickTime Player")' -e 'if r then' -e 'tell application "QuickTime Player"' -e 'if (count of documents) > 0 then return audio volume of document 1' -e 'end tell' -e 'end if' -e 'return "none"' 2>/dev/null)
    if [ -n "$PREV" ] && [ "$PREV" != "none" ]; then
      # ramp the loop DOWN to ~4% (0.4 s), play the sting alone, ramp the loop back UP (1 s)
      for f in 0.7 0.4 0.2 0.04; do
        osascript -e "tell application \"QuickTime Player\" to set audio volume of document 1 to $(python3 -c "print(round($PREV*$f,3))")" 2>/dev/null
      done
      afplay "$NEW_TRACK"
      for f in 0.2 0.45 0.7 1.0; do
        osascript -e "tell application \"QuickTime Player\" to set audio volume of document 1 to $(python3 -c "print(round($PREV*$f,3))")" 2>/dev/null
        sleep 0.25
      done
    else
      afplay "$NEW_TRACK"
    fi
  ) >/dev/null 2>&1 &
  disown 2>/dev/null
  exit 0
fi
LOOP=true
[ "$MODE" = "once" ] && LOOP=false   # explicit override only; scene songs always loop
STEPS=8
INTERVAL=0.08

# Get current system volume
CURRENT_VOL=$(osascript -e "output volume of (get volume settings)")

# Fade out
for i in $(seq "$STEPS" -1 0); do
    VOL=$(( CURRENT_VOL * i / STEPS ))
    osascript -e "set volume output volume $VOL"
    sleep "$INTERVAL"
done

# Open new track in QuickTime Player (looping, minimized)
osascript << APPLESCRIPT
tell application "QuickTime Player"
    close every document
    open POSIX file "$NEW_TRACK"
    delay 1
    set looping of document 1 to $LOOP
    play document 1
    set miniaturized of window 1 to true
end tell
APPLESCRIPT

# Fade in
for i in $(seq 0 "$STEPS"); do
    VOL=$(( CURRENT_VOL * i / STEPS ))
    osascript -e "set volume output volume $VOL"
    sleep "$INTERVAL"
done

osascript -e "set volume output volume $CURRENT_VOL"
