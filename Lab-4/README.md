# Lab 4 - Vibe Coding: Endless Runner (Pygame)

**SRN:** PES1UG24CS703
**Assigned repo:** https://github.com/SETAPESU26/39_endless-runner
**Personal repo (this one):** https://github.com/8figalltimepro/39_endless-runner

## Deliverables

| Item | File |
| --- | --- |
| a. Gameplay video BEFORE the changes (broken behaviour visible) | `videos/before.mp4` |
| a. Gameplay video AFTER the changes (fixes + new features) | `videos/after.mp4` |
| a. Raw full-length captures (mp4 conversions of the original `.mov` recordings) | `videos/full_recording_before.mp4`, `videos/full_recording_after.mp4` |
| b. Updated code | `code/` (identical to the repo root) |
| c. Complete chat history exported as PDF | `chat_history.pdf` |

## What was broken, what was fixed

| Task | Before | After |
| --- | --- | --- |
| 1. Collision detection / speed ramp | Speed grew forever. Past ~55 px/frame one frame moved an obstacle further than the player's 30 px hitbox, so obstacles tunnelled straight through without registering a hit. | Collision is swept - `Obstacle.hits()` tests the whole path travelled during the frame - and the ramp is capped at `MAX_SPEED = 22` px/frame, which is below the width of any hitbox, so a hit can never be skipped. |
| 2. Game over condition | Printed `Game over! Final score: N` to the console, then froze with no UI and no way to continue. | A collision switches the engine to the `game_over` state: `GAME OVER` and `Final score: N` are drawn over the frozen scene and the game waits for input. |
| 3. Replay option | None - the process had to be killed. | The game over screen (and the start screen) offer `1 Easy`, `2 Medium`, `3 Hard`, `Q / Esc Quit`. Difficulty sets the starting speed and spawn interval. |
| 4. Sound feedback | None. | Jump, score and game-over tones are synthesised at runtime in `game/sound.py` (no asset files, no extra dependencies) and played on the matching event. |

## Difficulty presets

| Difficulty | Start speed | Spawn interval |
| --- | --- | --- |
| Easy | 5 px/frame | 95 frames |
| Medium | 6 px/frame | 70 frames |
| Hard | 9 px/frame | 48 frames |

## Run

```bash
pip install -r requirements.txt
python main.py
```

Controls: `Space` / `Up` / `W` jump, `1` / `2` / `3` pick difficulty, `Q` / `Esc` quit.
