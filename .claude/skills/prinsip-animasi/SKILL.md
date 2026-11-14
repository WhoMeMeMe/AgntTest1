---
name: prinsip-animasi
description: Use when animating any 2D character in code (SVG, canvas, Remotion, CSS) for this channel - walk, run, jump, sit, wave, emotions, talking. Applies the 12 basic principles of animation with concrete numbers, plus the measured motion spec for the "Gaya 3" coloured-outline stick-limb style. Trigger on "animasi", "gerakan", "12 prinsip", "jalan/lompat/duduk", "Gaya 3", "Studio Gaya 3".
---

# Prinsip Animasi (12 principles, in numbers)

Source: Ollie Johnston and Frank Thomas, *The Illusion of Life* (1981). This file turns
each principle into values that can be typed into code. Adjectives are not direction;
numbers are.

Working code that already implements everything below: `reference/studio-gaya3.html`
(a standalone page: procedural character, 5 views, actions, expressions, a "12 prinsip
animasi" switch). Read it before writing a new rig; extend it instead of starting over.

## 0. Before animating

1. Decide the mode. **Reference mode** (stiff, like the preschool series we studied) or
   **12-principles mode** (livelier). Never mix inside one action.
2. Build every action pose to pose: list key poses with a time, then pick the easing
   for each segment. Do not animate by adding sine waves to everything.
3. Screenshot the key poses (anticipation, extreme, contact, settle) and look at them
   before publishing. A pose that reads badly as a still will not read in motion.

## 1. The 12 principles as parameters

| # | Principle (ID) | What to do in code | Typical numbers |
|---|---|---|---|
| 1 | Squash and stretch (remas-regang) | Scale Y by `1+sq`, scale X by `1/sqrt(1+sq)` so volume stays constant. Pivot at the feet. | Crouch -0.14, launch +0.15, landing -0.16, walk +/-0.04, run +/-0.07. Above 0.2 the head turns into an egg. |
| 2 | Anticipation (ancang-ancang) | A small move in the opposite direction before the main move. | 0.12-0.25 s. Jump: crouch 0.22 s. Wave: arm dips 0.12 s. Sit: rise 7 px for 0.14 s. Surprise has none. |
| 3 | Staging (penataan) | One idea per shot, clear silhouette, limbs away from the body. | Arms rest about 20 degrees below horizontal so both read in every view. |
| 4 | Straight ahead vs pose to pose | Pose to pose for actions; straight-ahead only for loose secondary motion. | Keyframe list `[time, pose, easing]`. |
| 5 | Follow through and overlapping action (tindak lanjut) | Loose parts lag behind the root and overshoot. | Forearm phase lag 0.9 rad behind upper arm. Head lags body by 0.06 s, max 7 px. Arms keep rising while the body already falls. Pendulum settle: `exp(-2.6t)*cos(8t)`. |
| 6 | Slow in and slow out | Ease per segment. | `io` smoothstep for holds, `out` (1-(1-u)^2) rising against gravity, `in` (u^2) falling. |
| 7 | Arcs (lengkung) | Rotate limbs around joints; body path curves. | Walk: body highest when legs pass, lowest at contact, 6 px. |
| 8 | Secondary action (aksi tambahan) | A smaller action that supports the main one. | Walk: arms swing opposite to legs at 2/3 amplitude, head tilt 2.5 degrees. Blink every 1.6-4 s. |
| 9 | Timing (tempo) | Frame count is the emotion. | Surprise 0.07 s to extreme. Sad 0.9 s to pose. Stomp: lift 0.36 s, slam 0.07 s. |
| 10 | Exaggeration (melebih-lebihkan) | Push the extreme pose past the real one, then settle. | Overshoot 8-12% then return. Run lean 8 degrees. Tremble 13 Hz decaying over 0.6 s. |
| 11 | Solid drawing | Keep volume and attachment consistent in every view. | Limbs stay attached at the same body points; outline width constant. |
| 12 | Appeal (daya tarik) | Simple readable shapes, big head, clear face. | Head about 45% of height for children. |

## 2. Action recipes (12-principles mode)

Times in seconds. `y` negative is up. Angles: lift 0 = down, 90 = horizontal, 180 = up.

- **Walk** (cycle 0.8): leg swing +/-30 degrees straight legs; body `y = -6*cos^2(ph)`;
  squash +/-0.04; arms opposite to legs, lagging 0.55 rad; head tilt 2.5 degrees.
- **Run** (cycle 0.4): swing +/-48; `y = -13*cos^2`; lean 8; squash +/-0.07; arms pump.
- **Jump** (cycle 1.4): 0.00 stand, 0.22 crouch (y+10, sq-0.14, arms back),
  0.30 launch (sq+0.15), 0.52 apex (y-78, arms up 146, legs V 22), 0.74 falling
  (arms still up 152), 0.82 land (y+9, sq-0.16), 0.96 rebound (y-3, sq+0.06), 1.08 rest.
- **Sit on floor**: 0.14 rise, 0.40 impact (sq-0.12, arms fly up), 0.54 overshoot, 0.70 settle.
- **Wave**: 0.12 dip, 0.28 overshoot up (134), 0.36 settle (122), then forearm waves
  +/-26 with 0.9 rad lag, body counter-sways 2 degrees.
- **Happy bounce** (cycle 0.5): 30% ground squash -0.16, 70% air y-38, arms flap with lag.
- **Laugh, falling over**: 0.14 lean forward 7 degrees, 0.42 fall past -99, 0.54 settle -90,
  then limbs kick out of phase (1.3 rad apart) and the body pulses +/-0.06.
- **Sad**: 0.9 s ease into y+6, tilt 12, squash -0.07; arms drop and swing to rest.
- **Surprised**: 0.07 stretch (y-30, sq+0.16, arms 128), 0.20 squash, 0.32 settle, tremble.
- **Angry**: 0.3 inhale (sq+0.09), hands on hips, stomp loop 0.6 (lift slow, slam fast,
  squash -0.14 on impact, head shake).

## 3. Reference mode: measured from the preschool series (frame-by-frame, 25 fps)

Use these when the brief says "like the reference". We copy the *way of moving*, never
the characters (see project CLAUDE.md, section 2).

- **Walk**: one step 0.40 s (cycle 0.80 s). Legs are straight sticks, swing about 30
  degrees. Front foot tilts toe-up at contact, rear foot heel-up. Arms do not swing.
  Body bob is almost zero. The character translates every frame (on ones).
- **Jump**: no anticipation. Up and down in about 0.30 s. Legs open into an inverted V
  (about 24 degrees each), arms stay out, mouth is a small "o" in the air, then a laugh.
  Hold about 0.5 s on the ground before the next jump.
- **Talking**: body and head completely still. Only the mouth swaps shapes: big open,
  medium open, small round "o", closed smile. Each shape is held 2-3 frames (0.08-0.12 s).
- **Sitting**: on the floor, legs straight forward, shoe tips up, body leaning back
  about 12 degrees.
- **Rest pose**: arms straight out to the sides, about 20 degrees below horizontal.
- **Body**: stays frontal in every view; only the head turns. Both arms and both legs
  are always visible side by side.

## 4. Gaya 3 character build (original character, not a copy)

- **Director's shape brief (2026-11-14): cute, bell body, tiny stick legs.** Body is a wide
  bell about as wide as the head at the hem (half-width 56 at scale 1, 20 at the top, 88 tall).
  Legs are short thin sticks (12 + 12), 36 apart, never thick tubes; long trousers are an
  8 px stick in the trouser colour. Shoes are flat dark ovals 30 x 11 that both point the way
  the character faces. Eyes are small round whites (r 10.5) set high and close together
  (x +/-0.23, y -0.24 of the head radius) with small pupils (r 4.2) looking up.
- Outline: 5 px, colour = fill darkened to about 78%. Never black.
- Head: circle, radius 62 at scale 1. Body: bell shape 76 tall, 42 wide at top, 72 at hem.
- Limbs: 5 px lines without fill. Hands: three 8 px finger lines at -38, 0, +38 degrees.
- Feet: dark ellipses 10-16 wide, 6 tall. Cheeks: pink circles r 13, 80% opacity.
- Eyes: white ellipse r 10.5, outline 3.5, pupil r 4.4. Mouth: 5 px pink line.
- Hair is clipped to the head circle; the head outline under hair uses the hair's dark colour.

## 6. Mood layer (suasana hati): any action x any mood

Do not hand-animate "walk while sleepy" as a separate action. Keep three layers and
combine them: **action** (what the body does) x **mood** (how it does it) x **face/mouth**.
A mood changes tempo, arm carriage, head, body and face on top of any locomotion or
idle action (stand, walk, run, sit).

| Mood | Tempo | Arms | Head / body | Extra |
|---|---|---|---|---|
| Riang | x1.12 | open 74 degrees, swing x1.3 | head up 3 | small hop 3 px |
| Mengantuk | x0.58 | hang straight down (9 degrees out), swing x0.45 | head droops 13 and nods +/-6 every 2.6 s, lean 7, body 4 px lower | step x0.6; yawn every 5 s for 1.6 s with one hand to the mouth |
| Sedih | x0.70 | hang (11), swing x0.3 | head down 12, body 5 px lower, squash -0.06 | step x0.7 |
| Menangis | x0.75 | both hands to the face | head down 8 | shoulders sob every 0.5 s, tears fall |
| Marah | x1.25 | stiff, down and 18 degrees back, swing x0.5 | lean 7 forward | walk bob x1.6 (stomping) |
| Takut | x0.85 | pulled to the chest | lean 5 back | step x0.55, 12 Hz tremble |
| Malu | x0.80 | behind the back | head down 8, turned away 14 | step x0.65, bigger cheeks |
| Bangga | x0.90 | hands on hips | chest out (lean -6), head up 6 | hop 2 px |
| Lelah | x0.62 | dangle (7), swing x0.35 | lean 11, head down 9, body 6 px lower | panting squash every 0.9 s |
| Bosan | x0.80 | limp (14), swing x0.4 | head down 6 | half-closed eyes |

Faces available: netral, senang, tertawa, kedip, malu, bingung, bosan, mengantuk, menguap,
sedih, menangis, takut, kaget, marah, terpejam. Extra actions: menunjuk, tepuk tangan,
mengangguk, menggeleng (head yaw offset), tidak tahu (shrug), tidur.

## 6b. Series cast (director's own character sheets, 02-14)

`reference/studio-gaya3.html` holds the cast as data in `CAST` and draws them with the same
rig, so every action, mood and face works on every character. One entry = species parts +
outfit: `fur`, `line`, `limb`, `muzzle`, `ears` (kucing, kelinci, rusa, kerbau), `stripes`,
`spots`, `whisk`, `antler`, `horn`, `beak`, `hair`, `bun`, `hijab`, `hat` (peci, topi),
`glasses`, `kumis`, `bow`, `tail` (kucing, kadal, kerbau, rusa, ayam), `top` (colour, sleeve,
detail: dasi, batik, kancing, koko, kebaya, rompi, kerah, polos) and `bottom` (rok,
rokpanjang, celana, celanapendek, celemek, optional motif).

Cast: 02 Nisa, 03 Pak Arif, 04 Bu Rani (cats); 05 Kakek Hadi, 14 Bayu (deer); 06 Nenek Sari,
07 Pak Bima, 08 Bu Maya, 09 Lala (rabbits); 10 Pak Joko, 11 Tobi (lizards); 12 Kak Raka
(chick); 13 Pak Wawan (buffalo). Sheet 01 has not been supplied yet.

To add a character: add one `CAST` entry; do not write new drawing code unless the sheet
needs a part that does not exist yet. Adults use body factor 1.22; children 1.0; the head
radius stays the same so the head-to-body ratio matches the sheets.

## 6c. Keep it calm, and audit every frame (director feedback 2026-11-14)

The director rejected the first 12-principles pass as "wiggle parah". Principles are a
seasoning, not the dish. Ceilings that passed review:

- Squash/stretch: at most +/-0.08 on big moments (jump, land, surprise), +/-0.015 while
  walking, +/-0.03 running. Never above 0.1.
- Head lag at most 3 px. Head tilt sway at most 1.2 degrees in a walk.
- Arm swing in a walk at most 12 degrees. No whole-body tremble above 0.6 px.
- Idle and talking stay still. Mood layers add posture, not constant motion.

- **Feet stay on the ground.** For every grounded action the rig lowers the body until the
  lowest foot touches the ground line; only jump, happy bounce, surprise and run may lift
  off. Never bob the whole character including the feet ("ngawang").
- **Near ear in front.** When the head is turned (3/4 front, side) the ear nearer the camera
  is drawn in front of the head; in back views both ears stay behind it.

Before publishing, run the automated audit (`reference/audit.js`, Playwright): it steps
every action x mood at 25 fps for 6 s in both modes and every cast x action x view, and
reports NaN/undefined in the markup, thrown errors, per-frame pose jumps, and geometry
leaving the stage. Fast moves (run legs, jump launch) are expected in the jump list; a
value that pops with no fast move behind it is a glitch. Then read the frame sheets by eye.

## 7. Checklist before calling an animation done

- [ ] Mode chosen (reference or 12 principles) and stated to the director.
- [ ] Every action has anticipation, an extreme, and a settle (or a stated reason not to).
- [ ] Squash and stretch keeps volume (X compensates Y) and pivots at the feet.
- [ ] Something lags: head, forearm, hair, or arms.
- [ ] No linear moves except impacts.
- [ ] Key poses screenshotted in at least front, 3/4 and side; no limb leaves the stage.
- [ ] No console errors; every pose object is complete (missing limb arrays crash the draw).
- [ ] Said plainly what was verified by screenshot and what still needs the director's eye
      (timing feel cannot be judged from stills).
