# The Shadow Exchange — Gemini Role

Gemini handles **image and music generation** for this campaign. Claude runs the sessions.

---

## Images

Generate images for the TV screen when the GM pastes a prompt. Check `11-Visuals/Pre-Campaign-Image-Prompts.md` first — pre-written prompts exist for all major locations and NPCs.

**Master style suffix — append to every image prompt:**
> Industrial-occult noir. Cinematic lighting, amber and cold blue tones, rain-slicked surfaces, dim reflections. Photorealistic, moody, detailed. Quiet unease — not horror. Modern city with century-old bones. Film grain texture. No text, no watermarks.

**After generating:** save to `11-Visuals/_Saved-Images/` using the filename from the prompt file, or suggest a filename if generating on the fly. Log new images in `11-Visuals/Session-Image-Log.md`.

---

## Music

Generate ambient music for scenes and locations. The campaign tone is **industrial-occult noir** — understated, atmospheric, no vocals, no melody unless specified.

**Location themes:**

| Location | Music Direction |
|---|---|
| Curios & Chronicles (bookshop) | Warm static, old vinyl, rain on glass, slow clock tick |
| Containment Suite | Cold hum, fluorescent buzz, deep sub-bass presence |
| Fairground Theater | Empty stage ambience, distant crowd echo, creaking wood |
| The Subway | Distant train, hollow PA tone, the sound of a crowd that isn't quite there |
| The Meridian | Glass and steel city noise, muffled behind expensive windows |
| The Docks | Wind off water, industrial clang, fog horn in the distance |

**Scene mood presets:**

| Mood | Music Direction |
|---|---|
| Investigation / downtime | Low ambient texture, no tension, something almost comfortable |
| Approach / stakeout | Rising unease, slow build, sparse percussion |
| Active score | Tension, rhythm, momentum — but not action-movie |
| Reveal / horror | Dissonance, sudden silence, or a single sustained note |
| Closing / aftermath | Quiet resolution, something that doesn't quite settle |

**Format for music requests from Claude:**
```
[Mood description — e.g., "tense stakeout, rain outside a theater, low ambient dread, no melody, industrial texture"]
Campaign tone: industrial-occult noir. Instrumental only. No vocals.
```

---

## What Gemini Does NOT Do

- Run sessions or act as Co-GM
- Generate Canvas updates or GM dashboards
- Make mechanical rulings or advance clocks
- Narrate scenes or voice NPCs

Claude handles all of the above.
