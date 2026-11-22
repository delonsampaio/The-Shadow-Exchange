#!/bin/bash
# Render what the Player Screen (TV) would show for a given scene file, as a PNG.
# Usage: docs/tools/render_player_screen.sh <scene.js> <out.png> [workdir]
# Never touches 11-Visuals/player-screen/scene.js (mock state): it builds a scratch copy.
# If the scene names an image and the PNG comes out small (image not loaded yet), it retries with a longer wait.
set -uo pipefail
SCENE="$1"; OUT="$2"; WORK="${3:-${TMPDIR:-/tmp}/psr-$$}"
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"; V="$ROOT/11-Visuals"
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
rm -rf "$WORK"; mkdir -p "$WORK/player-screen"
sed 's#</head>#<style>*{transition:none!important;animation:none!important}</style></head>#' "$V/Player-Screen.html" > "$WORK/Player-Screen.html"
cp "$SCENE" "$WORK/player-screen/scene.js"
for d in _Saved-Images vendor; do [ -e "$V/$d" ] && ln -s "$V/$d" "$WORK/$d"; done
WANT_IMG=0; grep -Eq 'image:[[:space:]]*"[^"]+' "$SCENE" && WANT_IMG=1
for BUDGET in 15000 30000 60000; do
  "$CHROME" --headless=new --disable-gpu --hide-scrollbars --window-size=1600,900 --virtual-time-budget=$BUDGET --screenshot="$OUT" "file://$WORK/Player-Screen.html" >/dev/null 2>&1
  SIZE=$(stat -f%z "$OUT" 2>/dev/null || echo 0)
  if [ "$WANT_IMG" = 0 ] || [ "$SIZE" -gt 400000 ]; then break; fi
  echo "image not loaded yet (PNG $SIZE bytes); retrying with a longer wait" >&2
done
if [ "$WANT_IMG" = 1 ] && command -v python3 >/dev/null; then
  MEAN=$(python3 -c "from PIL import Image,ImageStat;im=Image.open('$OUT').convert('L').resize((200,112));print(int(ImageStat.Stat(im).mean[0]))" 2>/dev/null || echo 99)
  if [ "$MEAN" -lt 12 ]; then echo "WARNING: the frame is almost black (mean brightness $MEAN); the image probably had not faded in. Re-run." >&2; fi
fi
if [ "$WANT_IMG" = 1 ] && [ "$SIZE" -le 400000 ]; then echo "WARNING: the scene names an image but the PNG is small ($SIZE bytes); the file may be missing or not loaded. Check the path." >&2; fi
echo "$OUT"
