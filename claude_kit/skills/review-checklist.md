# Skill: review-checklist

Tensaikun: this is where a video actually gets good, and it is the step almost everyone skips. Claude can produce a whole video, but **someone still has to watch it**. You cannot see many mistakes by yourself; they show up when a person watches. Expect them, and put every repeating one into the skill.

He reviewed on a live preview so he did not pay full render time for every fix. We must not copy his Video Hub product. He also said pausing and writing timestamps works. **[ours]** For Higgsfield, review scripts and start-frames before spending motion credits.

---

## 1. When to review

| Gate | What you watch / read | Spend credits? |
|---|---|---|
| Gate 1 | Script + title | No |
| Gate 2 | Shot list + captions | No |
| Gate 3 | Start-frames (or a 20 s test) | Start-frames only |
| Gate 4 | Motion clips, then the assembly | Yes, in chunks |
| Gate 5 | Pre-export / pre-upload | Already spent; do not re-export until this passes |

Do not jump from Gate 1 to Gate 4.

## 2. How to take notes

For every issue, log:

```
#nn  timestamp  type (script / visual / audio / edit / fact)
Note: …
Suggested fix: shot N / prompt / skill rule
Repeating? yes/no (search LESSONS.md and known-mistakes.md)
```

Examples of the *kind* of notes he described (do not copy his film): "he's facing the wall"; "the tag covers his face"; trees spinning with the camera; people walking through furniture; labels covering each other. Translate those into our medium: morphing hands, baked-in text, wrong sky, hook that starts too late, captions longer than 5 words, SFX louder than the VO, character drift between shots.

Send the note list back in one batch when possible, then update previews / regenerate only the affected chunks.

## 3. Repeating notes → fix the system

If the same problem appears in a second shot or a second video:

1. Add a numbered rule to the relevant skill (`style-guide`, `script-writer`, `shot-planner`, `thumbnail`, or this file).
2. Add a row to `known-mistakes.md`.
3. Append a `LESSONS.md` entry that names the file you changed.
4. Then fix the current video.

Do not only patch the one clip and hope you remember next time. Tensaikun: a prompt is forgotten after one chat; a skill gets better with every video. Start a new session per video; the skill carries what matters.

## 4. Watch-list (every review)

**Picture**

- [ ] Hook is readable with the sound off in the first 3 seconds
- [ ] Strongest moment is at 0:00, not buried mid-video
- [ ] Look matches the style skill (cyan cyclorama or justified context; stylized-realistic 3D; no lime typography brand)
- [ ] No text, logos, or watermarks in the generated picture
- [ ] No copied characters or costumes
- [ ] Continuity: materials, wardrobe, sky, anatomy do not randomly change
- [ ] No morphing faces, melting hands, or objects clipping through each other
- [ ] Cuts land about every 2–3 s and still feel motivated

**Script / VO**

- [ ] 75–95 words, calm tone, not textbook, no CTA
- [ ] Facts checked, or fiction labeled
- [ ] Picture is timed to the words (if timestamps exist)

**Audio**

- [ ] VO is clearly above the bed music
- [ ] SFX are specific and not uniformly slamming the ceiling (his "too loud / all alike" warning)
- [ ] Loudness not obviously hotter than about −14 LUFS if you can measure

**Edit**

- [ ] Duration 28–35 s (hard cap 45)
- [ ] Captions 2–5 words, lower third, karaoke, added in the edit
- [ ] `DO NOT ATTEMPT` present if needed

## 5. Pre-render / pre-credit checklist

Run this in the chat (or write `videos/YYYY-MM-slug/PRE_RENDER.md`) **before** a batch of motion generations or a final export. If any item is no, stop.

- [ ] Script approved, 75–95 words, no CTA, facts checked
- [ ] Hook places the strongest moment at 0:00–0:03
- [ ] Shot list is 10–14 shots, 2–3 s each, captions 2–5 words
- [ ] Style skill + `LESSONS.md` + `known-mistakes.md` were read this session
- [ ] Every generate prompt includes the style prefix and forbids text/logos/watermarks
- [ ] Characters/objects are original
- [ ] Start-frames (or a 20 s test) were reviewed; open notes are resolved or accepted
- [ ] Repeating notes have already been written into a skill file
- [ ] This run's credit cost is stated
- [ ] Mas Hanief approved spending those credits, or he already set a standing budget for this video

Tensaikun also: do not "just render it" as a vague command; optimize for the machine you have; split long work into chunks so a late fix only redoes the chunks that changed. **[ours]** Same idea: regenerate only the bad shots.

## 6. Known review rules added from feedback

1. Never skip Gate 3 (start-frame review) to "save time."
2. (Add the next rule when a note repeats.)

