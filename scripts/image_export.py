from pathlib import Path
import json
from PIL import Image, ImageDraw, ImageFont

def font(size, mono=False):
    names = (['/System/Library/Fonts/Menlo.ttc', '/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf']
             if mono else ['/System/Library/Fonts/Supplemental/Arial.ttf',
                           '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'])
    for name in names:
        if Path(name).exists():
            return ImageFont.truetype(name, size)
    return ImageFont.load_default(size=size)

def save_gif(frames, durations, output):
    # One palette across all frames avoids color flicker between pages.
    samples = frames[::max(1, len(frames) // 20)]
    sheet = Image.new('RGB', (250 * 5, 200 * ((len(samples) + 4) // 5)))
    for i, frame in enumerate(samples):
        thumb = frame.copy()
        thumb.thumbnail((250, 200))
        sheet.paste(thumb, ((i % 5) * 250, (i // 5) * 200))
    palette = sheet.quantize(colors=256)
    images = [f.quantize(palette=palette, dither=Image.Dither.NONE) for f in frames]
    output.parent.mkdir(parents=True, exist_ok=True)
    images[0].save(output, save_all=True, append_images=images[1:],
                   duration=durations, loop=0, optimize=True, disposal=2)
    with Image.open(output) as check:
        info = {'file': output.name, 'size': list(check.size), 'frames': check.n_frames,
                'bytes': output.stat().st_size,
                'duration_ms': sum(durations)}
    print(json.dumps(info), flush=True)
