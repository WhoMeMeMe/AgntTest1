"""ElevenLabs TTS for the channel's locked voice.

Usage: python3 tools/elevenlabs_tts.py <script.txt> <out.mp3> [voice_id] [model_id] [language]
Defaults are the locked channel voice (see claude_kit/skills/style-guide.md, section 7).
The API key is injected by the environment's network proxy; none is stored here.
"""
import sys

import httpx

VOICE = "TX3LPaxmHKxFdv7VOQHJ"  # "Liam", ElevenLabs built-in voice


def main() -> None:
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    script, out = sys.argv[1:3]
    voice = sys.argv[3] if len(sys.argv) > 3 else VOICE
    model = sys.argv[4] if len(sys.argv) > 4 else "eleven_v3"
    lang = sys.argv[5] if len(sys.argv) > 5 else "id"
    text = open(script, encoding="utf-8").read().strip()
    r = httpx.post(
        f"https://api.elevenlabs.io/v1/text-to-speech/{voice}",
        params={"output_format": "mp3_44100_128"},
        json={"text": text, "model_id": model, "language_code": lang},
        headers={"xi-api-key": "proxy-injected"},
        timeout=300,
    )
    if r.status_code != 200:
        sys.exit(f"{r.status_code}: {r.text[:400]}")
    open(out, "wb").write(r.content)
    print(f"wrote {out}: {len(text)} characters, {len(r.content)} bytes")


if __name__ == "__main__":
    main()
