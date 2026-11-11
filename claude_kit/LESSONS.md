# LESSONS.md — running improvement log

**[ours]** This file is our formal version of Tensaikun's rule: when notes repeat, fix the **skill**, not only the video; a prompt is forgotten after one chat, a skill gets better with every video.

Claude: append an entry after every review session, failed generation, skill change, or published video. Newest entries at the **top**. Do not overwrite old entries. If you edit a skill, name the file and the heading.

Mas Hanief can also paste notes here in Indonesian. Claude should rewrite the stored lesson in clear English (and keep a one-line Indonesian summary if he wrote in Indonesian).

---

## How to log

Copy the block:

```
### YYYY-MM-DD — [video slug or "style-test"] — [review | ship | fail | skill-update]
- What happened:
- Timestamp / shot (if any):
- Repeating issue? (yes/no; if yes, first seen in):
- Skill file changed: [path + heading, or "none — one-off clip fix"]
- Rule added (quote the new numbered rule, or "none"):
- What we will do differently next time:
- Credits used this run (start-frames / motion / retries), if known:
```

---

## Known-mistakes index

The compact list of standing rules lives in `known-mistakes.md`. This file is the narrative. That file is the checklist you re-read at the start of a session.

---

## Entries

### 2026-11-11 — 2026-11-rice-cooker — review
- What happened: Director said the stock voices were "kurang Indonesia" and supplied his own 2-minute Indonesian narration as a voice reference (`videos/2026-11-rice-cooker/audio/reference/`). Saving a voice model on Fish Audio is refused for this account (limit 0/0), so the first 34 s of the reference is sent inline with each request (`tools/fish_tts.py`). Script rewritten in conversational Indonesian (`vo.txt`, 89 words). Export: `videos/_previews/2026-11-rice-cooker_2d_v3.mp4`, 37.9 s, -13.8 LUFS, true peak -1.4 dBFS; click SFX peak -12.5 dB vs VO peak -3.4 dB (9 dB under). Awaiting his ear on the voice.
- Timestamp / shot (if any): n/a
- Repeating issue?: no
- Skill file changed: none yet — language and script-register rules wait for his go
- Rule added: none
- What we will do differently next time: (1) Spell "gak", not "nggak", for TTS — transcription heard "negap" with the long spelling. (2) The cloned voice inherits the slow storytelling pace of the reference: 89 words ran 39 s; `speed 1.15` only brought it to 37 s, over the 28–35 s target. Either trim the script to ~75 words or give a faster reference. (3) Large inline references can fail with a 502; a 128 kbps MP3 reference (~550 KB) works. (4) Audio is checked by measurement and transcription only — the director must listen.
- Credits used this run: 0 Higgsfield; Fish Audio: 4 short samples + 2 full generations

### 2026-11-11 — 2026-11-rice-cooker — review
- What happened: Voice added with Fish Audio (director's choice). Two stock narrator voices generated from the approved script: "Toren" (28.1 s, used) and "Slax" (34.5 s, kept as an alternative) in `videos/2026-11-rice-cooker/audio/`. Word timing via `tools/align_vo.py`; captions and animation now follow the voice. Export: `videos/_previews/2026-11-rice-cooker_2d_v2.mp4`, 28.9 s, -13.7 LUFS, true peak -1.4 dBFS. Awaiting director notes.
- Timestamp / shot (if any): n/a
- Repeating issue?: no
- Skill file changed: none
- Rule added: none
- What we will do differently next time: (1) Do not pass the script as a Whisper prompt — it made the model skip most of the audio (14/83 words); without it 70/83 matched and the rest interpolate. (2) Use the multilingual `small` model with `language=id`; `base.en` is English-only. (3) Skip Fish Audio voices cloned from real public figures; pick stock narrator voices. (4) Fish Audio access goes through the environment's saved credential for `api.fish.audio`; never store a key in the repo. (5) "Toren" runs ~178 wpm on this script, faster than the kit's 150–160 target — director to judge.
- Credits used this run: 0 Higgsfield; 2 Fish Audio TTS generations (~500 characters each)

### 2026-11-11 — 2026-11-rice-cooker — review
- What happened: Director asked for a 2D version. Built a code-drawn 2D preview (HTML/SVG rendered frame by frame with `tools/render_html.js`, then FFmpeg): `videos/_previews/2026-11-rice-cooker_2d_v1.mp4`, 1080x1920, 30 fps, 33.6 s, 6 beats. Look follows `skills/style-guide.md` (cyan gradient, caption `#F7F6F5` / `#2B2628`). No VO yet: caption timing is estimated, audio is two click SFX only (peak -8.4 dB). Awaiting director notes.
- Timestamp / shot (if any): self-review fixed caption words overlapping on entry (scale pop replaced by an 18 px rise) and the temperature readout covering the lid (moved to top 120 px).
- Repeating issue?: no
- Skill file changed: none — one-off fixes
- Rule added: none
- What we will do differently next time: Deviations to settle with the director — (1) Indonesian VO/captions instead of the kit's English; (2) 2D flat look instead of stylized 3D; (3) a temperature readout is drawn in-picture (code-rendered text, not model-generated, so KM-001 does not strictly apply). If approved, write them into `skills/style-guide.md` and `skills/script-writer.md`.
- Credits used this run: 0 (no Higgsfield generation)

### 2026-11-11 — tools-setup — skill-update
- What happened: Installed word-timing (faster-whisper 1.2.1, `base.en` model) with the director's approval. Added `tools/word_timing.py` and `tools/requirements.txt`. Tested on a synthetic clip: 12 words, timestamps correct.
- Timestamp / shot (if any): n/a
- Repeating issue?: no
- Skill file changed: none
- Rule added: none
- What we will do differently next time: The cloud container is rebuilt per session, so run `pip install -r tools/requirements.txt` at the start of a session that needs VO timing. PyAV 19 breaks faster-whisper 1.2.1 (`metadata_errors` error); keep `av<17`.
- Credits used this run: 0

### 2026-11-11 — session-bootstrap — skill-update
- What happened: Kit installed in this repo (`claude_kit/`, root `CLAUDE.md` imports it; `videos/` and `tools/` created; analysis PDF stored in `docs/`). Tools found: ffmpeg 6.1.1, Python 3.13, Node 22, Higgsfield connector (plan max, 3,197.55 credits at check time). Whisper is NOT installed (needs approval to install). No footage generated.
- Timestamp / shot (if any): n/a
- Repeating issue?: no
- Skill file changed: none
- Rule added: none
- What we will do differently next time: OPEN DECISION for the director — `skills/style-guide.md` targets the cyan cyclorama (`#4DC0FF`), while the analysis PDF (ch. 12–13) advises not cloning that palette and offers an original ivory `#F3EDE0` / ink `#1A1916` / cobalt `#2F6BFF` pack, with text drawn inside frames (conflicts with KM-001). Settle this in the 20-second style test before any real Short. Indonesian summary: palet cyan vs gading-tinta-kobalt belum diputuskan.
- Credits used this run: 0

### 2026-11-11 — kit-bootstrap — skill-update
- What happened: Initial kit created from the Tensaikun analysis (`/workspace/zacd/video_x6Z/Analisa_x6ZjVTK8aI.md`) and the ZacD DNA doc (`/workspace/zacd/final/DNA_ZacD_FINAL.md`). No production video has been reviewed yet.
- Timestamp / shot (if any): n/a
- Repeating issue?: n/a
- Skill file changed: starter skills added under `skills/` (style-guide, script-writer, shot-planner, review-checklist, thumbnail)
- Rule added: none from footage — production rules in the skill files are from those two sources; anything marked **[ours]** is an adaptation, not a step invented as if Tensaikun said it
- What we will do differently next time: first real work should be a 20-second style test, start-frames only, then a lesson from Mas Hanief's notes
- Credits used this run: 0

