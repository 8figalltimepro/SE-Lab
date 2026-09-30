import array
import math

import pygame

RATE = 44100


def _tone(start_freq, end_freq, ms, volume=0.4):
    count = int(RATE * ms / 1000)
    samples = array.array("h")
    phase = 0.0
    for i in range(count):
        freq = start_freq + (end_freq - start_freq) * i / count
        phase += 2 * math.pi * freq / RATE
        samples.append(int(32767 * volume * (1 - i / count) * math.sin(phase)))
    return pygame.mixer.Sound(buffer=samples.tobytes())


def load_sounds():
    try:
        return {
            "jump": _tone(420, 780, 90),
            "score": _tone(900, 1250, 70),
            "game_over": _tone(420, 90, 450),
        }
    except pygame.error:
        return {}
