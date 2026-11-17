#!/bin/bash
# fade-switch.sh — fade out, switch track in QuickTime Player, fade back in
# Usage: bash fade-switch.sh "path/to/track.mp3" [auto|loop|once]
# Stingers/one-shots (names containing sting, zoltar-opens, envelope-drops, the-pitch, s00-closing, ashby-approach) play ONCE; all other tracks loop.

NEW_TRACK="$1"
MODE="${2:-auto}"   # auto | loop | once   (auto: stingers/one-shots play once, everything else loops)
LOOP=true
case "$MODE" in
  once) LOOP=false ;;
  loop) LOOP=true ;;
  *) case "$(basename "$NEW_TRACK")" in
       *sting*|*zoltar-opens*|*envelope-drops*|*the-pitch*|*s00-closing*|*ashby-approach*) LOOP=false ;;
     esac ;;
esac
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
