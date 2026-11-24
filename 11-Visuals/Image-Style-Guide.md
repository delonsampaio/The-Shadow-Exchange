---
entity_type: Guide
status: ADOPTED 2026-11-23 (GM: all campaign images move from photoreal to style B; see `Image-Style-Migration.md` for the plan and order)
purpose: "The one style every campaign image uses, how to paste it, and how to keep recurring characters looking the same."
---

# Image Style Guide: painted storybook noir (style B)

## How images are made now (2026-11-24)
The Co-GM runs `docs/tools/gemini_image.py` (Gemini API, Pro and Flash), views the candidates and picks. The GM no longer pastes. Output is 1264 px wide at `--size 1K` and about 2528 px at 2K, so use 2K for TV scenes and 1K for wiki portraits. Check pixel sizes when reference images are attached (the API sometimes ignores the size). All other rules below are unchanged.

## The style block (paste at the START of every image prompt)
```
Stylised painted illustration, gouache and ink, visible brushwork, thick dark outlines, slightly exaggerated faces and hands, moody amber and blue light, like a modern dark-fantasy comic. No photographic detail.
```
Then the scene. End every prompt with: *"No readable text except the exact words given. No watermark."*

## Rules
- **Dread still counts (Menace Rule).** Monsters and the Surge, the wraith, the Subway are dark and weighty: heavy shadow, low light, no bright flat colour. Comedy images (Gerald, Consequence, Bernard) may be warmer and funnier but keep the same linework.
- **Same style everywhere, never mixed within a session.** Do not drop the style block "because it's a map" or "because it's an item": maps and items use it too (maps as painted illustrated maps).
- **Faces and recurring characters:** make the **anchor portrait** first (a face close-up plus a full-outfit image), then **attach it to every later image** of that character and say "same character as the attached picture". Chats only hold a face for a turn or two.
- **When a character changes form (Merton, Mabel, Thorne's mask):** carry the costume, the badge and the *expression* from the anchor; expect the face to change with the form. Test: `_Saved-Images/_style-tests/styleB-merton-reveal.png` into `styleB-merton-surge.png`.
- **Handwriting and documents:** Gemini tends to write the prompt's own words into scribble. Say "handwriting drawn as wavy lines, not letters, with no words at all"; accept tiny gibberish if it is unreadable at TV distance, but never accept readable fragments on anything secret (the Journal's red entry).
- **Text:** at most one short sign per image, exact words in CAPS, on a named surface. Neon and signs through windows often garble: ask for "blank glowing neon, no lettering" unless the words matter.
- **Left and right:** say "on the left of the frame", not "his right hand".
- **Counting:** avoid exact numbers above 3.
- **Aspect ratio:** write "wide 16:9" for TV images, "3:2" for portraits. The Gemini app has no ratio control.
- **Edits:** no mask tool; draw a red circle on the picture to mark the spot, say what to change, and say "remove the circle". Or regenerate with the changes spelled out.
- **Proof (2026-11-23):** the theater exterior redone from scratch (no reference) is far more painted than the version made from a photoreal reference. Always include "it must look hand-painted, with visible brushstrokes and bold ink outlines, not like a filtered photograph".
- **Locations: describe from scratch, do not attach the photoreal picture.** The bookshop and the corridor (from description) came out genuinely painted; the theater exterior and lobby (from a photoreal reference) came out as the photo with ink outlines. Attach a photoreal picture only for a layout you must keep, never for a normal location.
- **Reference drift:** when a photoreal picture is attached as a layout reference, Gemini tends to copy it and give a filtered-photo look. Say "paint it clearly with heavier brushwork and thicker outlines than the reference" to push it back to style B.
- **No railings or descending stairwells in Meridian/city street pictures** (the Subway entrance in Session 2 is a railing in an alley; a similar railing elsewhere pre-empts it).
- **Spoilers still apply** (no stray names, stamps or forms; Aldric not a broadcaster; no Omen; Stalls not an Apex mark).

## Filenames and the archive
Keep the **same filename** so no prep changes. The old photoreal files were deleted on 2026-11-24; there is no archive folder.

## Done so far (style B)
- `location-curios-interior.png` (2026-11-23, the first real restyled image).
- `npc-elias-thorne.png` (2026-11-23, 16:9 from the anchor; the face held across scenes).
- `npc-consequence-push.png` (2026-11-23, S0 Trial Run, cat from the interior picture).
- Anchor portrait: `_anchors/anchor-greta-fenn.png` (Greta).
- Anchor portrait: `_anchors/anchor-elias-thorne.png` (Thorne). Remember the ring: it is on HIS right hand, the left of the frame when he faces us.
- `npc-gerald-dog.png` and `npc-merton-surge.png` adopted straight from the style tests (2026-11-23).
- The early style tests were deleted on 2026-11-24; the adopted ones are saved under their real names (Gerald, Merton surge).
