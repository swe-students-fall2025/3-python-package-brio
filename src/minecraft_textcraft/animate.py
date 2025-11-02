# src/minecraft_textcraft/animate.py
from typing import Generator, Iterable, Optional
from .colorize_ascii import colorize_ascii, Color

def _normalize(ascii_art: str) -> list[str]:
    lines = ascii_art.splitlines()
    if not lines:
        return []
    width = max(len(ln) for ln in lines)
    return [ln.ljust(width) for ln in lines]

def animate_typewriter(
    ascii_art: str,
    color: Optional[Color] = None,
    cps: int = 10,  # characters per second
) -> Generator[str, None, None]:
    lines = _normalize(ascii_art)
    if not lines:
        yield ""
        return
    width = len(lines[0])
    # speed: 12 fps 
    step = max(1, int(round(cps / 12)))
    shown = 0
    while shown <= width:
        frame = "\n".join(ln[:shown] for ln in lines)
        yield colorize_ascii(frame, color) if color else frame
        shown += step
    full = "\n".join(lines)
    yield colorize_ascii(full, color) if color else full

def animate_scroll(
    ascii_art: str,
    color: Optional[Color] = None,
    cols_per_frame: int = 1,
    loops: int = 1,
) -> Generator[str, None, None]:
    lines = _normalize(ascii_art)
    if not lines:
        yield ""
        return
    cols_per_frame = max(1, int(cols_per_frame))
    width = len(lines[0])
    pad = " " * cols_per_frame
    padded = [pad + ln + pad for ln in lines]   # width = width + 2*cols
    total_w = width + 2 * cols_per_frame

    def colorize_if_needed(s: str) -> str:
        return colorize_ascii(s, color) if color else s

    def one_loop() -> Generator[str, None, None]:
        for start in range(0, total_w):
            frame_cols = [row[start:start + cols_per_frame] for row in padded]
            yield colorize_if_needed("\n".join(frame_cols))

    loops = max(1, int(loops))
    for _ in range(loops):
        yield from one_loop()
    

def animate_wave(
    ascii_art: str,
    color: Optional[Color] = None,
    amplitude: int = 2,
    period_cols: int = 10,
    frames: int = 24,
) -> Generator[str, None, None]:
  
    import math
    base = _normalize(ascii_art)
    if not base:
        yield ""
        return
    h = len(base)
    w = len(base[0])
    pad = amplitude + 1
    for t in range(max(1, frames)):
        canvas_h = h + 2 * pad
        canvas = [[" "] * w for _ in range(canvas_h)]
        for r in range(h):
            for c, ch in enumerate(base[r]):
                phase = 2 * math.pi * (c / max(1, period_cols)) + 2 * math.pi * (t / max(1, frames))
                offset = int(round(amplitude * math.sin(phase)))
                rr = r + pad + offset
                if 0 <= rr < canvas_h:
                    canvas[rr][c] = ch
        frame = "\n".join("".join(row) for row in canvas)
        yield colorize_ascii(frame, color) if color else frame

def play_animation(frames: Iterable[str], fps: int = 12) -> None:
    import time
    if fps <= 0:
        fps = 12
    delay = 1.0 / fps
    for f in frames:
        print("\033[2J\033[H", end="")  # clear screen + cursor home
        print(f)
        time.sleep(delay)
