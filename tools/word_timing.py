"""Word-level timestamps for a voiceover file.

Usage: python3 tools/word_timing.py path/to/vo.wav [out.json]
Prints one word per line (start, end, word) and optionally writes JSON.
"""
import json
import sys

from faster_whisper import WhisperModel


def main() -> None:
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    model = WhisperModel("base.en", device="cpu", compute_type="int8")
    segments, _ = model.transcribe(sys.argv[1], word_timestamps=True)
    words = [
        {"start": round(w.start, 2), "end": round(w.end, 2), "word": w.word.strip()}
        for s in segments
        for w in s.words
    ]
    for w in words:
        print(f'{w["start"]:7.2f} {w["end"]:7.2f}  {w["word"]}')
    if len(sys.argv) > 2:
        with open(sys.argv[2], "w") as f:
            json.dump(words, f, indent=2)


if __name__ == "__main__":
    main()
