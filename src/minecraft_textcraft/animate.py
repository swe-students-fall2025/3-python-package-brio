# src/minecraft_textcraft/animate.py
from typing import Generator, Iterable, Optional
from .colorize_ascii import colorize_ascii, Color

def _normalize(ascii_art: str) -> list[str]:
    """把 ASCII 画对齐到等宽，便于做列切片/滚动。"""
    lines = ascii_art.splitlines()
    if not lines:
        return []
    width = max(len(ln) for ln in lines)
    return [ln.ljust(width) for ln in lines]

def animate_typewriter(
    ascii_art: str,
    color: Optional[Color] = None,
    cps: int = 10,  # characters per second（抽象单位；测试中只影响步长）
) -> Generator[str, None, None]:
    """
    打字机效果：逐列揭示。这里不sleep，测试友好；播放时用 play_animation 控制fps。
    """
    lines = _normalize(ascii_art)
    if not lines:
        yield ""
        return
    width = len(lines[0])
    # 约定按 12 fps 映射步长，避免太慢
    step = max(1, int(round(cps / 12)))
    shown = 0
    # 逐渐增加可见列
    while shown <= width:
        frame = "\n".join(ln[:shown] for ln in lines)
        yield colorize_ascii(frame, color) if color else frame
        shown += step
    # 收尾：完整一帧
    full = "\n".join(lines)
    yield colorize_ascii(full, color) if color else full

def animate_scroll(
    ascii_art: str,
    color: Optional[Color] = None,
    cols_per_frame: int = 1,
    loops: int = 1,
) -> Generator[str, None, None]:
    """
    横向跑马灯：每帧向左滚动若干列，可配置循环次数。
    """
    lines = _normalize(ascii_art)
    if not lines:
        yield ""
        return
    width = len(lines[0])
    gap = " " * 4  # 头尾间留空隙，视觉更好
    wrap_lines = [ln + gap + ln for ln in lines]
    span = len(wrap_lines[0])
    j = 0
    total_steps = span * max(1, loops)
    step = max(1, cols_per_frame)
    moved = 0
    while moved < total_steps:
        frame = "\n".join(wl[j:j+width] for wl in wrap_lines)
        yield colorize_ascii(frame, color) if color else frame
        j = (j + step) % span
        moved += step

def animate_wave(
    ascii_art: str,
    color: Optional[Color] = None,
    amplitude: int = 2,
    period_cols: int = 10,
    frames: int = 24,
) -> Generator[str, None, None]:
    """
    纵向波浪：按列做正弦偏移，生成固定帧数。
    """
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
    """
    在终端播放动画：清屏、回到光标原点、按fps延时打印。
    """
    import time
    if fps <= 0:
        fps = 12
    delay = 1.0 / fps
    for f in frames:
        print("\033[2J\033[H", end="")  # clear screen + cursor home
        print(f)
        time.sleep(delay)
