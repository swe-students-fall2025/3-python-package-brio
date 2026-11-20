# Recreate Textcraft typewriter, scroll and wave

Every animation frame comes from the package’s actual rendering and animation functions, exported to GIF with Pillow. This is program output, not a mock terminal effect.

Run from the repository root in a separate Python 3.11+ environment:

~~~bash
python -m venv .venv-demo
source .venv-demo/bin/activate
python -m pip install -r scripts/demo-requirements.txt
python scripts/render_demo.py
~~~

Output: docs/media/textcraft-workflow.gif. On Windows, activate with .venv-demo/Scripts/activate.

The script imports render, animate_typewriter, animate_scroll and animate_wave directly from this checkout’s src/ directory. It draws the returned text frames with a monospace font; no GPU or browser is required.

Team/source attribution remains in the main README and original project files. The demo adds presentation assets, not new product functionality.
