"""Align a known script to a voiceover and write per-word timestamps.

Usage: python3 tools/align_vo.py <vo audio> <script.txt> <out.js> [language] [model]
Whisper supplies the timing; the script supplies the spelling. Script words Whisper
missed are interpolated between their neighbours. Output: window.VO_WORDS / VO_END.
"""
import difflib
import json
import re
import sys

from faster_whisper import WhisperModel


def norm(w: str) -> str:
    return re.sub(r"[^a-z0-9]", "", w.lower())


def main() -> None:
    if len(sys.argv) < 4:
        sys.exit(__doc__)
    audio, script_path, out = sys.argv[1:4]
    lang = sys.argv[4] if len(sys.argv) > 4 else "id"
    model = WhisperModel(sys.argv[5] if len(sys.argv) > 5 else "small", device="cpu", compute_type="int8")
    script = open(script_path, encoding="utf-8").read().split()
    segments, _ = model.transcribe(audio, language=lang, word_timestamps=True, condition_on_previous_text=False)
    heard = [w for s in segments for w in s.words]
    sm = difflib.SequenceMatcher(None, [norm(w) for w in script], [norm(w.word) for w in heard], autojunk=False)
    times = [None] * len(script)
    for a, b, n in sm.get_matching_blocks():
        for k in range(n):
            times[a + k] = (heard[b + k].start, heard[b + k].end)
    matched = sum(t is not None for t in times)
    end = heard[-1].end
    i = 0
    while i < len(script):  # interpolate gaps
        if times[i] is None:
            j = i
            while j < len(script) and times[j] is None:
                j += 1
            t0 = times[i - 1][1] if i else 0.0
            t1 = times[j][0] if j < len(script) else end
            step = (t1 - t0) / (j - i)
            for k in range(i, j):
                times[k] = (t0 + step * (k - i), t0 + step * (k - i + 1))
            i = j
        else:
            i += 1
    words = [{"w": w, "start": round(s, 3), "end": round(e, 3)} for w, (s, e) in zip(script, times)]
    with open(out, "w", encoding="utf-8") as f:
        f.write("window.VO_WORDS = " + json.dumps(words, ensure_ascii=False) + ";\n")
        f.write(f"window.VO_END = {round(end, 3)};\n")
    print(f"{matched}/{len(script)} script words matched; VO ends at {end:.2f}s")
    print("heard:", " ".join(w.word.strip() for w in heard))


if __name__ == "__main__":
    main()
