# minecraft-textcraft Demo Commands

## Quick Start
```bash
# Basic text rendering
python -m minecraft_textcraft "HELLO"

# With color
python -m minecraft_textcraft "HELLO" --color GREEN

# With command
python -m minecraft_textcraft 'GET \\sword NOW'

# With animation
python -m minecraft_textcraft "HELLO" --effect type
```

## Text Rendering
```bash
python -m minecraft_textcraft "HELLO"
python -m minecraft_textcraft "HELLO" --color GREEN
python -m minecraft_textcraft "HELLO" --color RED
python -m minecraft_textcraft "HELLO" --color BLUE
python -m minecraft_textcraft "HELLO" --color YELLOW
```

## Commands
```bash
# List all commands
python -m minecraft_textcraft --list

# List categories
python -m minecraft_textcraft --list-categories

# Get command ASCII art
python -m minecraft_textcraft --get sword
python -m minecraft_textcraft --get earth

# Command with color
python -m minecraft_textcraft --get sword --color GREEN
```

## Text with Commands
```bash
# Text + command + color
python -m minecraft_textcraft 'GET \\sword NOW' --color RED
```

## Animations
```bash
# Typewriter effect
python -m minecraft_textcraft "HELLO" --effect type --color GREEN

# Scroll effect
python -m minecraft_textcraft "HELLO" --effect scroll --color BLUE

# Wave effect
python -m minecraft_textcraft "HELLO" --effect wave --color YELLOW
```

## Full Features Demo
```bash
# Text + command + animation + color + custom FPS
python -m minecraft_textcraft 'GET \\sword NOW' --effect type --color GREEN --fps 20
python -m minecraft_textcraft 'HELLO \\sword' --effect scroll --color RED

```

## Options
- **Colors**: `RED`, `GREEN`, `BLUE`, `YELLOW`
- **Effects**: `type`, `scroll`, `wave`
- **FPS**: `10-30` (default: 12)

## Help
```bash
python -m minecraft_textcraft --help
```
