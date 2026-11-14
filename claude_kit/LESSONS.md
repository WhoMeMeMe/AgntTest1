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

### 2026-11-14 — gaya-3-animation — skill-update
- What happened: Built "Studio Gaya 3" (coloured-outline, stick-limb original character, 5 views, 11 actions, 7 expressions). Studied two reference videos frame by frame (25 fps) and measured walk, jump, talking and floor-sit. Director then asked for livelier motion, so a second motion set using the 12 principles of animation was added behind a switch.
- Timestamp / shot (if any): n/a
- Repeating issue?: yes — the director asked three times for motion to be "fixed" before numbers were measured from footage; guessing motion from memory was not accepted.
- Skill file changed: new Claude Code skill `.claude/skills/prinsip-animasi/SKILL.md` (12 principles as parameters, action recipes, measured reference spec, Gaya 3 build numbers, pre-publish checklist); working source kept in `.claude/skills/prinsip-animasi/reference/studio-gaya3.html`.
- Rule added: measure motion from the director's footage frame by frame before tuning; build actions pose to pose with anticipation, extreme and settle; screenshot key poses in 3 views before publishing; never copy the reference characters, only the way they move.
- What we will do differently next time: ask for short clips up front (upload in chat; a folder on the director's PC and large Drive videos are not reachable from a cloud session). Timing feel cannot be judged from stills, so say so and let the director watch.
- Credits used this run: 0

### 2026-11-11 — 2026-11-rice-cooker — skill-update
- What happened: Director approved the 15 s ElevenLabs sample "premade_liam" ("lumayan, lock aja") — voice locked. Full VO generated (`audio/vo_liam_v1.mp3`, 560 characters), tightened (`audio/vo_liam_v1_tight.wav`), picture re-timed, SFX rebuilt. Export `videos/_previews/2026-11-rice-cooker_2d_v5.mp4`: 40.0 s, -14.1 LUFS, true peak -1.4 dBFS, SFX stem peak -13.0 dBFS vs processed VO peak -3.1 dBFS.
- Timestamp / shot (if any): whole VO — raw read was 46.4 s for 89 words
- Repeating issue?: no (length first seen on the Fish clone, different cause)
- Skill file changed: `skills/script-writer.md` section 1 (Language, Narrator) and section 7 rules 4; `skills/style-guide.md` section 7; `CLAUDE.md` section 5.2 first bullet
- Rule added: "For a 28–35 s Short write 65–75 Indonesian words" and the locked voice/engine + VO processing chain
- What we will do differently next time: v5 runs 40 s, over the 28–35 s target but under the 45 s cap. To hit the target, trim this script to about 70 words and regenerate rather than speeding the voice further. A single-pass loudnorm left the mix at -16 LUFS until the VO was compressed first.
- Credits used this run: 0 Higgsfield; ElevenLabs 560 characters

### 2026-11-11 — 2026-11-rice-cooker — review
- What happened: Director asked to move the VO to ElevenLabs. Connected through the environment credential for `api.elevenlabs.io` (header `xi-api-key`). Account is on the free tier (about 6,200 of 10,000 characters left before this run). Library voices, including the three Indonesian ones already saved on the account (Jin, Andra, Mahaputra), return 402 "Free users cannot use library voices via the API". Only the built-in English voices work through the API; two 15 s Indonesian samples made with them (Liam, Will, model `eleven_v3`, `language_code: id`) in `videos/2026-11-rice-cooker/audio/samples_elevenlabs/`. Listed native Indonesian (locale id-ID) male library voices with preview links for the director to pick from.
- Timestamp / shot (if any): n/a
- Repeating issue?: no
- Skill file changed: none
- Rule added: none
- What we will do differently next time: Native Indonesian ElevenLabs voices need a paid plan for API use, or the director generates the file on the ElevenLabs site and uploads it. List endpoint: `/v1/shared-voices?language=id`, then keep only `locale` starting with `id` (the language filter alone returns mostly foreign voices).
- Credits used this run: 0 Higgsfield; ElevenLabs about 430 characters

### 2026-11-11 — 2026-11-rice-cooker — review
- What happened: Director's notes on v3: (1) "kurang Indonesia" — second time for the voice (first on the stock Fish voices, now on the Fish clone of his own reference); (2) no subtle sound effects. Added a coded SFX stem (`tools/sfx.py`, 21 cues, 12 distinct sounds: whoosh on cuts, pop, swish, ping, boing, bubbling, ticks, hiss, thunk, stretch, click, ding). Export `videos/_previews/2026-11-rice-cooker_2d_v4.mp4`: -13.8 LUFS, true peak -1.4 dBFS, SFX stem peak -13.0 dBFS vs VO peak -3.4 dBFS (9.6 dB under). Voice is unchanged in v4 and still open.
- Timestamp / shot (if any): whole VO
- Repeating issue? yes — "kurang Indonesia", first seen on v2 (stock voices)
- Skill file changed: `known-mistakes.md` KM-006; `skills/script-writer.md` section 7 rule 3
- Rule added: "Indonesian VO: never build a full video on a new voice. Send a 10-second sample of the engine + voice first and wait for the director's ear; a transcription match is not evidence that it sounds native."
- What we will do differently next time: Fish Audio s1 has now missed twice on Indonesian naturalness (stock and cloned). Ask which engine produced the director's reference narration and use that engine, or have him record the script. Higgsfield's speech presets are English-named voices with no listed Indonesian option.
- Credits used this run: 0

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

