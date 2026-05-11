# The Shadow Exchange — Gemini Role

Gemini handles **image and music generation** for this campaign. Claude runs the sessions.

---

## Images

Generate images for the TV screen when the GM pastes a prompt. Check `11-Visuals/Pre-Campaign-Image-Prompts.md` first — pre-written prompts exist for all major locations and NPCs.

**Master style suffix — append to every image prompt:**
> Industrial-occult noir. Cinematic lighting, amber and cold blue tones, rain-slicked surfaces, dim reflections. Photorealistic, moody, detailed. Quiet unease — not horror. Modern city with century-old bones. Film grain texture. No text, no watermarks.

**After generating:** save to `11-Visuals/_Saved-Images/` using the filename from the prompt file, or suggest a filename if generating on the fly. Log new images in `11-Visuals/Session-Image-Log.md`.

**Image-to-music shortcut:** Any saved image from `11-Visuals/_Saved-Images/` can be uploaded directly into Gemini music chat to generate a matching track — Gemini reads the mood and setting from the image. Useful for location themes and NPC scenes.

---

## Music (Lyria 3 Pro)

Gemini's music generation runs on **Lyria 3 Pro** (active on this account). Tracks 30 seconds to 3 minutes, understands full song structure — Intro, Verse, Chorus, Bridge, Outro.

**All prompts are in `11-Visuals/Music-Prompts.md`** — campaign presets, session-specific cues, and vocal tracks.
**Save generated tracks to `11-Visuals/_Saved-Music/`** using the filename listed in the prompt file.

### Prompt Structure

Every music prompt should include these four elements:

1. **Genre/Era** — e.g., Victorian Gothic, Industrial, Dark Ambient, Neoclassical
2. **Instrumentation/Texture** — e.g., cello, harpsichord, metallic clanks, ticking clocks, rain, dusty piano
3. **Mood/Tone** — e.g., melancholic, tense, stealthy, mysterious
4. **Tempo/Dynamics** — e.g., 60 BPM, slow build, sudden silence

Always start with `[Instrumental]` for background music to prevent vocals.

**Lyrics (vocal tracks only):** Three options — Gemini writes everything (describe topic/tone), hint at a topic ("a song about a city that keeps no records"), or supply full/partial lyrics with `Lyrics: [your lines]`.

**Song structure:** Specify segments explicitly — e.g., "15-second ambient intro, verse at 0:15, chorus at 1:00, outro fade at 2:30." Lyria 3 Pro follows this.

**Loop tracks:** For scenes that run longer than 3 minutes, add `seamless loop, no clear beginning or end, no melodic resolution, continuous ambient texture` to the prompt. Presets marked *(loop)* in `Music-Prompts.md` already include this.

---

### Format from Claude During Sessions

When Claude generates a music cue during a session, it will output:

```
GM ONLY — MUSIC FOR TV SCREEN
Paste into Gemini music chat:

[prompt text]
```

Paste it into your Gemini music chat (separate from the session runner chat with Claude).

**On-the-fly two-prompt option:** Ask Claude for "two music prompts for [scene]":
- **Prompt A — Full Track (text only):** 2–3 minute structured track with Intro/Verse/Outro timing. Start with `[Instrumental]` for background music.
- **Prompt B — Image-Guided Clip:** Short prompt to send alongside an image from `11-Visuals/_Saved-Images/`. Include `[Instrumental]` unless you want vocals.

---

## What Gemini Does NOT Do

- Run sessions or act as Co-GM
- Make mechanical rulings or advance clocks
- Narrate scenes or voice NPCs
- Update the GM dashboard

Claude handles all of the above.
