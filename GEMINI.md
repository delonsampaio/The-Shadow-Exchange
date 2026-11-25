# The Shadow Exchange — Gemini Role

Gemini handles **image and music generation** for this campaign. Claude runs the sessions.

---

## Images

**Since 2026-11-24 the Co-GM generates images itself through the Gemini API** (`docs/tools/gemini_image.py`; key in `~/.config/shadow-exchange/gemini_api_key`, never in a repo; run it with `~/.config/shadow-exchange/venv/bin/python`). Workflow (GM's rule, 2026-11-24): make ONE image per prompt (the cheaper Flash model by default; `--size 2K` for TV scenes), look at it, and only if it is not good enough redo it with the higher Pro model (`--models pro`). Save the keeper over the same filename and update the progress files. **No stings (GM, 2026-11-24): never generate or offer short stings or foley; a cue for a missing sting is simply skipped and the beat is carried by the banner or the read-aloud.** Music: one track per cue with the full-length model by default (`gemini_music.py`; the clip model is fixed at 30 seconds, so use it only for short loops), redo with `--model pro` only if needed. Only generate when the GM asks; during a live session only under `00-Canon/Session-Boot.md` §2c (on the GM's "make it", one quick image, checked before it goes on the TV; no live music), and say the rough cost first for batches of more than a handful (about $0.13 per Pro image, $0.07 to $0.10 per Flash). The hand-paste route (below) still works if the API is unavailable.

Generate images for the TV screen when the GM pastes a prompt, or when the Co-GM runs one. Check `11-Visuals/Pre-Campaign-Image-Prompts.md` first — pre-written prompts exist for all major locations and NPCs.

**Master style suffix — append to every image prompt:**
> **Master style (changed 2026-11-23): painted storybook noir.** Start every image prompt with the style block in `11-Visuals/Image-Style-Guide.md`: *Stylised painted illustration, gouache and ink, visible brushwork, thick dark outlines, slightly exaggerated faces and hands, moody amber and blue light, like a modern dark-fantasy comic. No photographic detail.* End with: *No readable text except the exact words given. No watermark.*

**Five rules for every image prompt:**
1. **Structural order:** Subject & Composition → Lighting & Environmental Atmosphere → Texture, Color & Subtext → Exclusion
2. **No buzzwords:** Do not use "photorealistic," "hyperrealistic," or "8K." Describe physical tactile details instead — *visible wood grain, dust motes, micro-scratched metal*
3. **Cinematic lighting:** Describe how light *behaves* — *fractured neon reflections on wet asphalt, volumetric fog diffusing a streetlamp, cold blue light bleeding under a door*
4. **Narrative subtext:** One emotional directive — *quiet domestic loneliness, gritty institutional coldness, grief worn smooth*
5. **Exact negative anchor:** End every prompt with exactly: `Clean composition, no text, no watermarks, no signatures.`

**After generating:** save to `11-Visuals/_Saved-Images/` using the filename from the prompt file, or suggest a filename if generating on the fly. Log new images in `11-Visuals/Session-Image-Log.md`.

**Image-to-music shortcut:** Any saved image from `11-Visuals/_Saved-Images/` can be uploaded directly into Gemini music chat to generate a matching track — Gemini reads the mood and setting from the image. Useful for location themes and NPC scenes.

---

## Music (Lyria 3 Pro)

Gemini's music generation runs on **Lyria 3 Pro** (active on this account). Tracks 30 seconds to 3 minutes, understands full song structure — Intro, Verse, Chorus, Bridge, Outro.

**All prompts are in `11-Visuals/Music-Prompts.md`** — campaign presets, session-specific cues, and vocal tracks.
**Save generated tracks to `11-Visuals/_Saved-Music/`** using the filename listed in the prompt file.

### Prompt Structure

Every instrumental prompt should define:

1. **Genre, Era, and Sonic Vibe** — e.g., Dark Victorian ambient, Cold industrial, Ethereal dark ambient
2. **Tempo and Key** — exact BPM + key and mode (e.g., 55 BPM, D minor / B Phrygian / atonal)
3. **Instrumentation Roles** — Lead instrument vs. Support instruments listed separately
4. **Production Texture** — e.g., analog tape warmth, dry clinical room, cavernous cathedral reverb, warehouse acoustic
5. **Time-Stamped Structure** — Intro, Build, Climax, Outro with timestamps (e.g., "Cello enters at 0:20, drops at 1:30")

Always start with `[Instrumental]` for background music to prevent vocals.

**Loop tracks:** For scenes that run longer than 3 minutes, add `seamless loop, no clear beginning or end, no melodic resolution, continuous ambient texture`. Presets marked *(loop)* in `Music-Prompts.md` already include this.

**Vocal tracks** require three additional elements:
- **Vocal Profile** — gender, age tone, range, e.g., "smoky female mezzo-soprano, warm and slightly melancholic"
- **Delivery Style** — phrasing, vibrato, cadence, e.g., "behind-the-beat timing, straight tone, minimal vibrato"
- **Mix Placement** — where the voice sits, e.g., "dry mono AM radio compression" or "warm front-of-mix, small club ambience"

**Lyrics:** Gemini writes everything (describe topic/tone), hint at a topic ("a song about a city that keeps no records"), or supply full/partial lyrics with `Lyrics: [your lines]`. Use `[Verse]`, `[Chorus]`, `[Bridge]` tags for structure.

**Song structure:** Specify segments explicitly with timestamps — e.g., "Vocalist enters at 0:20, chorus at 1:00, piano solo bridge at 1:45, outro fade at 2:20." Lyria 3 Pro follows this.

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
