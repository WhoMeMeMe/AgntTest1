"""Fish Audio TTS with an inline voice reference (no saved voice model needed).

Usage: python3 tools/fish_tts.py <script.txt> <out.mp3> <reference.wav> <reference transcript.txt> [speed]
The API key is injected by the environment's network proxy; none is stored here.
"""
import sys

import httpx
import ormsgpack


def main() -> None:
    if len(sys.argv) < 5:
        sys.exit(__doc__)
    script, out, ref_audio, ref_text = sys.argv[1:5]
    body = {
        "text": open(script, encoding="utf-8").read().strip(),
        "references": [{"audio": open(ref_audio, "rb").read(), "text": open(ref_text, encoding="utf-8").read().strip()}],
        "format": "mp3",
        "mp3_bitrate": 192,
        "normalize": True,
    }
    if len(sys.argv) > 5:
        body["prosody"] = {"speed": float(sys.argv[5]), "volume": 0}
    r = httpx.post(
        "https://api.fish.audio/v1/tts",
        content=ormsgpack.packb(body),
        headers={"authorization": "Bearer proxy-injected", "content-type": "application/msgpack", "model": "s1"},
        timeout=300,
    )
    if r.status_code != 200:
        sys.exit(f"{r.status_code}: {r.text[:400]}")
    open(out, "wb").write(r.content)
    print(f"wrote {out} ({len(r.content)} bytes)")


if __name__ == "__main__":
    main()
