# 🍄 Desktop Mario

A **stress-relief mini-game** that lives on your Windows desktop as a transparent overlay.

> People work continuously and get stressed. Desktop Mario gives you a quick fun break — right on your desktop. Press **Ctrl+Alt+M** anytime to play!

![Platforms](https://img.shields.io/badge/platform-Windows%20%7C%20Linux-blue)
![Python](https://img.shields.io/badge/python-3.10%2B-green)
![License](https://img.shields.io/badge/license-MIT-orange)

## ✨ Features

- **Desktop overlay** — plays right on top of your work, with transparent background support where available
- **Ctrl+Alt+M** hotkey to instantly show/hide the game
- **System tray icon** — runs silently in background, right-click to show/hide or quit
- **Classic SMB mechanics** inspired by the original NES Super Mario Bros:
  - Run (Shift), jump (Space, hold for higher!), arrow keys to move
  - Goombas, Koopas (green + red), Bob-ombs with explosions
  - Shell kick mechanics — stomp, kick, chain kills
  - Mushroom power-up — grow big!
  - Pipes, pits, bricks, ?-blocks, coins, staircases
  - Score system with popups
- **Lightweight** — pure Python + tkinter, no heavy game engine

## 🎮 Controls

| Key | Action |
|-----|--------|
| ← → | Move left/right |
| Space | Jump (hold longer = higher) |
| Shift | Run faster |
| Ctrl+Alt+M | Show/Hide game |
| ESC | Hide game |

## 📦 Installation

### Windows Installer
Download the latest `DesktopMario_Setup.exe` from [Releases](https://github.com/bxf1001g/desktop_mario/releases) and run it.

Options during install:
- Create desktop shortcut
- Start with Windows (runs in background)

### Run from Source (uv)
```bash
git clone https://github.com/bxf1001g/desktop_mario.git
cd desktop_mario
uv sync
uv run desktop-mario-overlay
```

Other Python entry points:
```bash
uv run desktop-hearts-overlay
uv run desktop-mario-screensaver
```

## 🔨 Build

### Build Go executable (recommended)
```bash
# Build for the current platform
go build -o desktop_mario ./cmd/desktop_mario

# Cross-compile for Windows
GOOS=windows GOARCH=amd64 go build -ldflags "-H windowsgui" -o DesktopMario.exe ./cmd/desktop_mario
```

Logs are written to `desktop_mario.log` next to the executable.

### Run Legacy Script Entry Points
```bash
python mario_enhanced.py
python desktop_hearts.py
python desktop_screensaver.py
```

### Build Python .exe (legacy, Windows)
```bash
pip install pyinstaller pystray Pillow
python -m PyInstaller --onefile --windowed --name DesktopMario --hidden-import pystray --hidden-import pystray._win32 --hidden-import PIL mario_enhanced.py
```

### Build Installer (requires Inno Setup)
```bash
iscc installer.iss
```

## 💡 Why?

Continuous work leads to stress and burnout. Sometimes you just need a 2-minute break doing something fun. Desktop Mario is always one hotkey away — no need to open a browser or launch a separate app.

## ☕ Support

If you enjoy Desktop Mario, consider buying me a coffee!

[![Donate](https://img.shields.io/badge/Donate-PayPal-blue.svg)](https://www.paypal.com/paypalme/bhanu1001)

## 🎨 Credits

Sprite assets by **[webfussel](https://webfussel.itch.io/more-bit-8-bit-mario)** — *More-bit 8-bit Mario* (itch.io). Thank you for the amazing SMAS-style sprites!

## 🐧 Linux Notes

- The Python overlays now run on Linux using the same entry points via `uv`.
- Window transparency behavior depends on your window manager/compositor.
- Global idle-time detection in `desktop-mario-screensaver` is Windows-only; on Linux, the screensaver starts immediately and exits on input.

## 📄 License

MIT License — see [LICENSE](LICENSE) for details.
