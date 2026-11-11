# Skill: shot-planner

Turn an approved script into a shot list and **Higgsfield** prompts (start-frame + motion), 9:16. Read `skills/style-guide.md` first. The prompt says *what* happens in this shot. The style skill (and the prefix below) says *how*.

Tensaikun: more camera description in the script makes shot planning better; you may plan shots from the script, then re-time to the voice once Whisper (or equivalent) timestamps exist.

**[ours]** The prefix, shot count, and Higgsfield format are our channel's, adapted from the ZacD DNA production template — not Tensaikun's 16:9 typographic look, and not a copy of anyone's prompts word-for-word.

---

## 1. Shot math

| Parameter | Value |
|---|---|
| Count | 10–14 shots for a 28–35 s Short |
| Length on the timeline | about **2–3 s** each |
| Generation length | Generate about **5 s** of motion, then trim in the edit to 2–3 s |
| Aspect | 9:16 |
| Hook | Shot 1 is the strongest moment (0:00–0:03) |

If the VO timestamps are already available, align cuts to words, not to a rigid grid. You may insert a short pause if the mechanism needs a breath (Tensaikun).

## 2. Table to output every time

| # | Time | Camera / move | On screen | Caption (2–5 words) | SFX | Start-frame prompt | Motion prompt |
|---|---|---|---|---|---|---|---|
| 1 | 0:00–0:03 | slow push-in, MCU | … | … | … | (full prompt) | (full prompt) |

Also state: total shots, total estimated credits (start-frames + motion clips + planned retries), and whether this is a **20 s test** or a full Short.

## 3. Style prefix — paste at the start of every start-frame prompt

```
Stylized-realistic 3D educational short, vertical 9:16, slightly glossy plastic-looking human skin with visible pores and fine vellus hairs, soft diffused studio lighting with gentle contact shadows, plain seamless cyan-blue sky cyclorama backdrop (gradient from #5FBEFF at the top to #4DC0FF in the middle to #A0DEFF lower), shallow depth of field, uncluttered composition, one dominant subject, no text, no captions, no logos, no watermarks, no subtitles, no UI.
```

If the beat needs a real place (ocean, clinic, forest, room), replace the backdrop clause with:

```
contextual [environment], directional lighting, scene-appropriate warm/cool palette, subject still clearly readable against the background, vertical 9:16, no text, no captions, no logos, no watermarks, no subtitles, no UI.
```

Then add the shot-specific subject, action pose, and original character/object details.

## 4. Motion prefix — paste at the start of every motion prompt

```
Smooth educational 3D animation, vertical 9:16, 5-second shot, consistent materials and anatomy, no morphing faces, no text, no logos, no watermarks. Camera: [MOVE]. Action: [ACTION]. Lighting and backdrop remain consistent with the start frame.
```

Fill `[MOVE]` with exactly one of:

- slow push-in
- locked medium close-up
- rapid camera dive through the surface into a medical cutaway
- forward tracking inside the cutaway
- extreme macro, almost static
- slow pull-out to a medium payoff
- gentle orbit hold
- top-down scale shot

Prefer **start-frame first, then motion from that frame** (Start & End Frame when the tool allows). Do not use frames, stills, or clips from other channels as image references.

## 5. Planning rules

- One dominant subject per shot. If you need a comparison, a clean split or a cut is better than a crowded frame.
- Captions are for the **editor**, not the generator. Never ask Higgsfield to draw the title or the karaoke.
- Characters must match `style-guide.md` (or be faceless). Never "in the style of Zack D. Films" or Tensaikun's named scenes.
- After a weak hook in review, do not rebuild every scene. Write an **edit list**: what to cut, what to move to 0:00 (Tensaikun: a few lines that reorder the timeline).
- Budget **[ours]**: plan 1–2 motion attempts per shot, not an open-ended retry loop. Say the count before generating.

## 6. 20-second test mode (first sessions)

Tensaikun's first step: a short test, not a full film. In this mode:

- 40–60 word stub VO, or even a silent look test with 1–2 spoken lines
- 6–8 shots or fewer
- One subject, cyclorama, no complex multi-character continuity
- Stop after start-frames until Mas Hanief reviews, unless he explicitly wants motion on the test

## 7. Known planning rules added from reviews

1. If two adjacent shots share the same camera move and the same framing, combine or change one; the 2–3 s rhythm still needs a reason to cut.
2. (Add the next rule when a note repeats.)

