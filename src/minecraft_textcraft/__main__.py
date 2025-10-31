from .colorize_ascii import colorize_ascii, Color
try:
    from .animate import animate_typewriter, animate_scroll, animate_wave, play_animation
    _ANIM_AVAILABLE = True
except Exception:
    _ANIM_AVAILABLE = False

import argparse
HELLO = """
█   █ █████ █     █     █████
█   █ █     █     █     █   █
█████ ████  █     █     █   █
█   █ █     █     █     █   █
█   █ █████ █████ █████ █████
"""


def main():
    p = argparse.ArgumentParser(add_help=False)
    p.add_argument("--effect", choices=["type", "scroll", "wave"])
    p.add_argument("--fps", type=int, default=12)
    p.add_argument("--color", default="RED")
    args, _ = p.parse_known_args()

    if not args.effect or not _ANIM_AVAILABLE:
        # 保持你原来的输出
        print(colorize_ascii(HELLO.strip("\n"), Color.RED))
        return

    # 有 --effect 时才播放动画
    color = Color.from_string(args.color)
    art = HELLO.strip("\n")
    if args.effect == "type":
        frames = animate_typewriter(art, color=color, cps=12)
    elif args.effect == "scroll":
        frames = animate_scroll(art, color=color, cols_per_frame=2, loops=2)
    else:  # wave
        frames = animate_wave(art, color=color, amplitude=2, period_cols=10, frames=36)
    play_animation(frames, fps=args.fps)



if __name__ == "__main__":
    main()
