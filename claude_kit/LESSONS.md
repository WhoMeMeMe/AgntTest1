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

