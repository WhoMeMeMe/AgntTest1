"""Synthesize a quiet, varied sound-effect stem from a cue list.

Usage: python3 tools/sfx.py <events.json> <duration seconds> <out.wav>
events.json: [[kind, start, end-or-null], ...]. Every cue kind has its own sound and its
own peak level, all well under the voice (rule: SFX peak at least 3 dB below VO peak).
"""
import json
import sys
import wave

import numpy as np

SR = 48000
rng = np.random.default_rng(7)
PEAK_DB = {"click": -13, "thunk": -15, "ding": -17, "pop": -19, "ping": -19, "boing": -20,
           "whoosh": -21, "swish": -22, "tick": -23, "stretch": -24, "bubbles": -27, "hiss": -31}


def tone(f, d, decay):
    t = np.arange(int(d * SR)) / SR
    return np.sin(2 * np.pi * f * t) * np.exp(-decay * t)


def sweep(f0, f1, d):
    t = np.arange(int(d * SR)) / SR
    f = f0 + (f1 - f0) * t / d
    return np.sin(2 * np.pi * np.cumsum(f) / SR)


def noise(d, lo, hi):
    n = int(d * SR)
    spec = np.fft.rfft(rng.standard_normal(n))
    freq = np.fft.rfftfreq(n, 1 / SR)
    spec[(freq < lo) | (freq > hi)] = 0
    return np.fft.irfft(spec, n)


def hann(x):
    return x * np.hanning(len(x))


def make(kind, dur):
    if kind == "click":
        n = int(0.012 * SR)
        snap = np.pad(noise(0.012, 1500, 7000) * np.linspace(1, 0, n), (0, int(0.2 * SR)))
        body = np.pad(tone(240, 0.2, 38), (n, 0))
        return snap + body[: len(snap)]
    if kind == "thunk":
        return tone(105, 0.22, 22) + 0.3 * np.pad(noise(0.01, 300, 2000), (0, int(0.21 * SR)))
    if kind == "ding":
        return tone(1760, 1.6, 3.2) + 0.45 * tone(2637, 1.6, 4.5) + 0.2 * tone(3520, 1.6, 6)
    if kind == "pop":
        d = 0.09
        return sweep(620, 190, d) * np.exp(-28 * np.arange(int(d * SR)) / SR)
    if kind == "ping":
        return tone(1320, 0.5, 9) + 0.3 * tone(1980, 0.5, 13)
    if kind == "boing":
        d = 0.4
        t = np.arange(int(d * SR)) / SR
        f = 300 - 110 * t / d + 22 * np.sin(2 * np.pi * 13 * t)
        return np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-6 * t)
    if kind == "whoosh":
        return hann(noise(0.42, 250, 2600))
    if kind == "swish":
        return hann(noise(0.16, 2500, 9000))
    if kind == "tick":
        return tone(2100, 0.03, 120)
    if kind == "stretch":
        return hann(sweep(190, 430, dur)) * 0.8
    if kind == "hiss":
        x = noise(dur, 3500, 11000)
        fade = np.minimum(1, np.minimum(np.arange(len(x)), np.arange(len(x))[::-1]) / (0.6 * SR))
        return x * fade
    if kind == "bubbles":
        x = np.zeros(int(dur * SR))
        t = 0.0
        while t < dur - 0.1:
            d = rng.uniform(0.03, 0.07)
            b = hann(sweep(rng.uniform(350, 650), rng.uniform(750, 1100), d)) * rng.uniform(0.4, 1)
            i = int(t * SR)
            x[i:i + len(b)] += b[: len(x) - i]
            t += rng.uniform(0.07, 0.3)
        fade = np.minimum(1, np.minimum(np.arange(len(x)), np.arange(len(x))[::-1]) / (0.8 * SR))
        return x * fade
    raise ValueError(kind)


def main():
    events, total, out = json.load(open(sys.argv[1])), float(sys.argv[2]), sys.argv[3]
    mix = np.zeros(int(total * SR) + SR)
    for kind, start, end in events:
        x = np.asarray(make(kind, (end - start) if end else 0), dtype=float)
        x = x / np.max(np.abs(x)) * 10 ** (PEAK_DB[kind] / 20)
        i = int(start * SR)
        mix[i:i + len(x)] += x[: len(mix) - i]
    mix = mix[: int(total * SR)]
    with wave.open(out, "wb") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR)
        w.writeframes((np.clip(mix, -1, 1) * 32767).astype("<i2").tobytes())
    print(f"{len(events)} cues, stem peak {20 * np.log10(np.max(np.abs(mix))):.1f} dBFS")


if __name__ == "__main__":
    main()
