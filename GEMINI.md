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

**The Bookshop (Curios & Chronicles — downtime, crew planning)**
```
[Instrumental] Dark Victorian ambient, warm dusty piano, slow clock tick, rain on old glass, crackling vinyl static, muffled city sounds, melancholic and unhurried, 55 BPM, pure texture, no vocals.
```

**The Containment Suite (prep, examination, something in the cold drawer)**
```
[Instrumental] Cold industrial ambient, low fluorescent hum, deep sub-bass drone, metallic resonance, clinical and unsettling, surgical silence broken by distant mechanical noise, 40 BPM, no melody, pure texture.
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

**The Fairground Theater (exterior approach, theater basement)**
```
[Instrumental] Empty stage ambience, distant crowd echo barely audible, creaking wood, single piano note decaying slowly, the smell of old curtains in sound, melancholic and hollow, 50 BPM.
```

**Closing / Aftermath (end of score, downtime opens, something was left unresolved)**
```
[Instrumental] Sparse neoclassical, solo cello, unresolved harmonic — something that doesn't quite settle, quiet and weight-bearing, 48 BPM, no percussion, no resolution chord.
```

---

### Vocals (Use Sparingly)

For in-world moments only — a tavern, a radio broadcast, an NPC performing. Include `Lyrics:` if you want specific words; otherwise describe the topic and Gemini writes them.

**The Scanner Station broadcast (the man who is never wrong about where):**
```
Lyria 3 Pro. AM radio quality, male voice, slightly wrong — too calm for what he's describing, low-fi grain, occasional static break, monologue tone not song, speaking about a street address he shouldn't know.
```

**Curios & Chronicles in-world radio (something playing in the shop):**
```
Lyria 3 Pro. 1940s jazz standard, female vocalist, warm and slightly melancholic, small ensemble, the kind of song that belongs in a late-night diner, not sinister — just tired.
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

---

## What Gemini Does NOT Do

- Run sessions or act as Co-GM
- Make mechanical rulings or advance clocks
- Narrate scenes or voice NPCs
- Update the GM dashboard

Claude handles all of the above.
