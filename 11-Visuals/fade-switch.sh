#!/bin/bash
# fade-switch.sh — fade out, switch track in QuickTime Player, fade back in
# Usage: bash fade-switch.sh "path/to/track.mp3"

NEW_TRACK="$1"
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
    set looping of document 1 to true
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
