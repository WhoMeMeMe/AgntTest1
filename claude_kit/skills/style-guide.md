# Skill: style-guide

**How everything we make should look.** The user prompt says *what* to make. This file says *how*. Read it before any script polish, shot plan, or Higgsfield prompt.

Numbers below are **production targets** from our ZacD DNA document (measured 11 Nov 2026, or taken from that formula). They are **not** an official Zack D. Films brand guide. Palette hex values are PIL measurements from research frames (often 360p) and may shift; use the gradient, not one rigid chip.

**[ours]** This skill is our channel's style bible, written in numbers as Tensaikun advised. Do not use his lime (`#D4FF3E`) or orange starburst, and do not use Zack watermarks or characters.

When a review note repeats, add a numbered rule at the bottom (see `known-mistakes.md`) and, if it is a look rule, add it here too.

---

## 1. Format

| Parameter | Value |
|---|---|
| Aspect | 9:16 vertical (1080×1920 target) |
| Duration | 28–35 s typical; never over 45 s |
| Shot count | 10–14 |
| Cut rhythm | about every 2–3 s |
| Frame rate (edit) | 30 fps is fine (research downloads were ~29.97/30) |

## 2. Render look

- Stylized-realistic **3D** educational short. Human proportions relatively natural. Faces, if any, read as CG characters — not chibi, not Unreal photoreal, not flat vector, not default stick figures.
- Skin: slightly glossy / plastic, visible pores, fine vellus hair, soft subsurface.
- Other materials must read clearly for a demo: wood, metal, glass, water, muscle, fabric.
- Lighting: soft diffused studio key from above-front, gentle contact shadows, background simpler than the subject.
- Gore, if any, is educational, controlled saturation, not horror.
- Shallow depth of field, uncluttered, **one dominant subject**.

**First tests (Tensaikun: start simple / start 2D before heavy 3D):** a 20-second test may be a single object on the cyclorama, even flatter than the final look, until consistency is proven. Finished channel videos still target the 3D look above.

## 3. Palette (working values)

Sky cyclorama gradient, top → mid → lower:

| Stop | Hex (approximate) |
|---|---|
| Top | `#5FBEFF` |
| Mid (signature) | `#4DC0FF` |
| Lower, lighter | `#A0DEFF` |
| Deeper variant (use sparingly) | `#4E9FD8` |

Other measured references (do not treat as a locked swatch book):

| Role | Hex (approximate) |
|---|---|
| Lit skin (example) | `#EEA785` |
| Arm skin (example) | `#E0BCA0` |
| Macro skin (example) | `#D4AC94` |
| Educational muscle | `#D01915` |
| Inflamed tissue | `#AC5554` |
| Caption fill | `#F7F6F5` (near white) |
| Caption edge / outline | `#2B2628` |

**Anatomical interiors:** playful-but-serious educational colors — saturated muscle red, high-chroma vein blue, cream bone/tendon. Still "a good toy that is serious," not surgical photo.

**Contextual backgrounds** (ocean, clinic, forest, interior) only when the story needs place or scale. For object/body demonstrations, use the plain cyan cyclorama.

**Forbidden palettes for this channel's brand:** Tensaikun acid lime `#D4FF3E` / `#C0E639` as a title system; his 8-point orange starburst.

## 4. Camera (numbers, not "cinematic")

Use these instead of mood words:

| Shot type | Camera |
|---|---|
| Hook (0–3 s) | Medium close-up, subject large and centered, **slow push-in ~1.5–2% per second**, 35mm-equivalent, slight high or eye-level |
| Myth / setup | Medium or CU, mostly locked or same slow push |
| Dive into the mechanism | Rapid camera dive / smash zoom through a surface into a cutaway |
| Inside the mechanism | Forward tracking or locked extreme macro |
| Twist / escalation | New angle or exploded view / layered slice |
| Payoff | Slow pull-out to medium, or gentle orbit hold |

- Mix static and moving shots. Do not float the camera without a reason.
- Transitions: clean cuts. The dive/zoom is the "door" into the inner world. No busy TikTok wipes, no lime circle wipes from the Tensaikun tutorial look.
- Lens language to put in prompts: `35mm-equivalent` for people/objects; macro for mechanism inserts. Do not say "cinematic lens" alone.

## 5. Captions (burned in at edit time, not in the 3D)

| Parameter | Value |
|---|---|
| Color | `#F7F6F5` |
| Outline / edge | thin dark, `#2B2628` |
| Type | Bold grotesque sans |
| Length | **2–5 words** per card (one short phrase is ok) |
| Placement | Lower third, centered, safe area |
| Style | Karaoke, follows the VO; not a paragraph; no background box |
| 3D renders | **No text, no captions, no logos, no watermarks, no UI** |

Dangerous topics may add a separate overlay: `DO NOT ATTEMPT`.

## 6. Characters and objects

- Original everyman or no face at all (hands, tools, cutaways are enough for many videos).
- If a person is needed, invent age, hair, and clothes. Write those details into the prompt every time for consistency, and record them here once a "house character" is approved.
- **Do not** describe "the Zack D. Films guy," navy-tee clones of their exact costume, or any character from Tensaikun's films.

House character (fill in after the first approved test; leave blank until then):

```
name: (none yet)
age:
hair:
clothes:
do not change without updating this block and LESSONS.md
```

## 7. Audio (picture style's companion)

- Calm male VO is the lead. Music stays low, under the voice.
- SFX should be specific (whoosh on the dive, material sounds) and **not** all the same loud hit. Tensaikun: AI SFX often come out too loud and too similar.
- **[ours]** Target integrated loudness near **-14 LUFS**; keep true peak out of the red (do not sit at 0 dBFS). If you can measure, measure.

## 8. Known look rules added from reviews

*(Append numbered rules here. Do not delete old ones; strike through if retired, and log in LESSONS.md.)*

1. Never bake captions or titles into Higgsfield start-frames.
2. Never add a channel watermark in the render.
3. If the sky comes out teal-green or grey, restate the hex gradient in the prompt and regenerate the start-frame; do not "fix it in the grade" as the first move.
4. (Add the next rule when a note repeats.)

