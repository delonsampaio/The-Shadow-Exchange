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

## Music (Lyria 3)

Gemini's music generation runs on **Lyria 3 Pro** (active on this account). Tracks up to 3 minutes, understands full song structure — verses, build, drop, resolution. Use this for everything: ambient loops, set-pieces, NPC themes, and session music.

### Prompt Structure

Every music prompt should include these four elements:

1. **Genre/Era** — e.g., Victorian Gothic, Industrial, Dark Ambient, Neoclassical
2. **Instrumentation/Texture** — e.g., cello, harpsichord, metallic clanks, ticking clocks, rain, dusty piano
3. **Mood/Tone** — e.g., melancholic, tense, stealthy, mysterious
4. **Tempo/Dynamics** — e.g., 60 BPM, slow build, sudden silence

Always start with `[Instrumental]` for background music to prevent vocals.

---

### Campaign Presets

**Loop note:** Presets marked *(loop)* are designed for scenes that run longer than 3 minutes. Add `seamless loop, no clear beginning or end, no melodic resolution, continuous ambient texture` to the prompt when generating. Lyria 3 will structure the track to restart without an audible seam.

**The Bookshop (Curios & Chronicles — downtime, crew planning)** *(loop)*
```
[Instrumental] Dark Victorian ambient, warm dusty piano, slow clock tick, rain on old glass, crackling vinyl static, muffled city sounds, melancholic and unhurried, 55 BPM, pure texture, no vocals, seamless loop, no clear beginning or end, no melodic resolution, continuous ambient texture.
```

**The Containment Suite (prep, examination, something in the cold drawer)** *(loop)*
```
[Instrumental] Cold industrial ambient, low fluorescent hum, deep sub-bass drone, metallic resonance, clinical and unsettling, surgical silence broken by distant mechanical noise, 40 BPM, no melody, pure texture, seamless loop, no clear beginning or end, no melodic resolution, continuous ambient texture.
```

**The Approach (stakeout, walking to the target, pre-engagement)**
```
[Instrumental] Dark Victorian ambient, rhythmic mechanical ticking, muffled footsteps, slow melancholic cello drone, tense suspenseful pace, solitary and focused, 60 BPM, pure texture, no vocals.
```

**The Score (active heist, things going loud, escape)**
```
[Instrumental] Industrial darkwave, heavy metallic percussion, clanking iron, distorted upright bass, frantic and aggressive tempo, dark warehouse energy, 120 BPM, no vocals.
```

**The Subway (first access, navigation, PTOLEMY encounter)**
```
[Instrumental] Ethereal dark ambient, hollow PA tone echo, distant train rumble, the sound of a crowd that isn't quite there, dissonant string pad, eerie and cavernous, 50 BPM, pure texture.
```

**The Supernatural (true form reveal, Anchor item moment, Omen manifestation)**
```
[Instrumental] Ethereal dark ambient, distant wordless choir pad, echoing cold stone texture, discordant violin, supernatural dread, hypnagogic pace, 45 BPM, no vocals.
```

**The Fairground Theater (exterior approach, theater basement)** *(loop)*
```
[Instrumental] Empty stage ambience, distant crowd echo barely audible, creaking wood, single piano note decaying slowly, the smell of old curtains in sound, melancholic and hollow, 50 BPM, seamless loop, no clear beginning or end, no melodic resolution, continuous ambient texture.
```

**Closing / Aftermath (end of score, downtime opens, something was left unresolved)**
```
[Instrumental] Sparse neoclassical, solo cello, unresolved harmonic — something that doesn't quite settle, quiet and weight-bearing, 48 BPM, no percussion, no resolution chord.
```

---

### Vocals (Use Sparingly)

For in-world moments only — a tavern, a radio broadcast, an NPC performing.

**Three ways to handle lyrics:**
- **Gemini writes everything** — describe the topic and tone, no lyrics provided. Gemini invents words that match.
- **Hint at the topic** — give a phrase or concept ("a song about a city that keeps no records") and Gemini writes to it.
- **Provide full or partial lyrics** — add `Lyrics: [your lines]` and Gemini sets them to music.

**Song structure:** You can specify segments explicitly — e.g., "15-second ambient intro, then verse at 0:15, chorus at 1:00, bridge at 1:45, outro fade at 2:30." Lyria 3 Pro follows this.

---

**The Scanner Station broadcast (the man who is never wrong about where)**
```
Lyria 3 Pro. 2-minute track. Low-fi AM radio quality, slight tape hiss. Structure: 10-second static crackle intro, then spoken-word male voice — calm, deliberate, slightly wrong in affect, too composed for what he's describing. He reads a street address and a time. No musical backing — just voice, static, and the occasional signal drift. Outro: the broadcast cuts mid-sentence, dead air, then static returns.
Topic: a man broadcasting on AM radio about the locations of things that haven't happened yet.
```

**Curios & Chronicles in-world radio (something playing in the shop)**
```
Lyria 3 Pro. 2.5-minute track. 1940s jazz standard. Structure: 8-bar piano intro, female vocalist enters at 0:20 — warm timbre, slightly melancholic, unhurried phrasing. Verse: a tired love song, the kind that belongs in a late-night diner. Chorus: the melody lifts slightly but doesn't resolve — it circles back. Bridge: piano solo, minimal, a little too slow. Outro: vocalist fades mid-phrase, piano alone for 10 seconds, then silence.
Topic: a woman singing about a city she can't leave and doesn't want to.
Small ensemble: piano, upright bass, brushed snare. No horns. No vibrato excess.
```

**The Fairground (a song from the theater's past — heard from backstage)**
```
Lyria 3 Pro. 90-second clip. Vaudeville era, slightly degraded as if played on a cracked wax cylinder. Female vocalist — bright, performative, slightly too cheerful for the words. The audience applause is there but feels wrong, like it's been recorded in an empty room. Structure: short intro, one full verse and chorus, applause, then silence.
Topic: a song about a magician who made things disappear and couldn't bring them back.
```

---

### Format from Claude During Sessions

When Claude generates a music cue during a session, it will output:

```
GM ONLY — MUSIC FOR TV SCREEN
Paste into Gemini music chat:

[prompt text]
```

Paste it into your Gemini music chat (separate from the session runner chat with Claude).

**On-the-fly two-prompt option:** For any unplanned scene, Claude can generate two variants:
- **Prompt A — Full Track (text only):** 2–3 minute structured track with explicit Intro/Verse/Outro timing. Start with `[Instrumental]` for background music (prevents unwanted vocals).
- **Prompt B — Image-Guided Clip:** Short atmospheric prompt designed to be sent alongside an image from `11-Visuals/_Saved-Images/` — Gemini reads the visual textures and translates them into sound. Include `[Instrumental]` here too unless you want vocals.

Ask for "two music prompts for [scene]" and Claude will output both.

---

## What Gemini Does NOT Do

- Run sessions or act as Co-GM
- Make mechanical rulings or advance clocks
- Narrate scenes or voice NPCs
- Update the GM dashboard

Claude handles all of the above.
