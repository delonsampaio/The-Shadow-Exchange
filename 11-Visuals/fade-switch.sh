#!/bin/bash
# fade-switch.sh — fade out current track, switch, fade back in
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

# Switch track
killall afplay 2>/dev/null
while true; do afplay "$NEW_TRACK"; done &

# Fade in
for i in $(seq 0 "$STEPS"); do
    VOL=$(( CURRENT_VOL * i / STEPS ))
    osascript -e "set volume output volume $VOL"
    sleep "$INTERVAL"
done

# Restore original volume exactly
osascript -e "set volume output volume $CURRENT_VOL"
