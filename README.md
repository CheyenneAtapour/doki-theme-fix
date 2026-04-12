# Doki Theme Injector for Cursor & Antigravity

A cross-platform (Windows, macOS, Linux) Python script to seamlessly inject [Doki Theme](https://github.com/doki-theme) stickers and wallpapers into **Cursor** and **Antigravity** code editors.

## 🌟 Overview

Cursor and Antigravity are based on VS Code but often lack direct support for standard VS Code extension-based UI modifications due to strict Content Security Policies (CSP) and custom builds. This tool bypasses those limitations by directly modifying the internal `workbench.desktop.main.css` and `workbench.desktop.main.js` files to inject your favorite anime characters.

Originally built for macOS only, this fork has been completely rewritten to natively support Windows, macOS, and Linux without relying on OS-specific shell commands.

## ✨ Features

- **Cross-Platform Compatibility:** Automatically detects your OS and resolves the correct installation paths (`%LOCALAPPDATA%` on Windows, `/Applications` on macOS, `/opt` on Linux).
- **Decoupled Configuration (`config.py`):** Clean separation of concerns. You no longer need to edit the main injection scripts to change characters or opacities.
- **Custom Local Assets:** Easily use your own `.png` or `.webp` files by defining absolute paths. The script natively handles copying them into the editor's protected directory to bypass strict CSP blocks.
- **Native Network Requests:** Uses Python's native `urllib.request` for downloading remote assets, dropping the dependency on system `curl` or `powershell`.
- **macOS Gatekeeper Handling:** Automatically attempts to `codesign` the modified `.app` bundle on Darwin systems to prevent "App is damaged" errors.

---

## 🚀 Getting Started

### 1. Prerequisites
- **Python 3.6+** installed on your system.
- **Cursor** or **Antigravity** installed on your machine.

### 2. Installation
Clone the repository to your local machine:
```bash
git clone https://github.com/YOUR-USERNAME/doki-theme-fix-windows.git
cd doki-theme-fix-windows
```

### 3. Configuration Setup
Create your personal configuration file from the provided template. This file is ignored by git so your paths remain strictly local:
```bash
cp config.example.py config.py
```

Open `config.py` in your text editor. You can configure:
- `SELECTED_CHARACTER`: Choose from the built-in dictionary catalog (e.g., `"cc"`, `"rem"`, `"echidna"`) or set to `"custom"`.
- `STICKER_OPACITY` / `WALLPAPER_OPACITY`: Float values from `0.0` (invisible) to `1.0` (fully opaque).
- `CUSTOM_STICKER` / `CUSTOM_WALLPAPER`: If using `"custom"`, provide the absolute path to your local images. 
  *(Example for Windows: `"C:\\Users\\Name\\Pictures\\waifu.png"`).*

### 4. Injecting the Theme

Run the script corresponding to your code editor. 

**For Cursor:**
```bash
# Windows
python cursor_doki_theme.py

# macOS / Linux (Requires sudo to modify files in /Applications or /opt)
sudo python3 cursor_doki_theme.py
```

**For Antigravity:**
```bash
# Windows
python antigravity_doki_theme.py

# macOS / Linux
sudo python3 antigravity_doki_theme.py
```

Once the script finishes successfully, **completely restart your editor** to see the changes taking effect.

---

## 🔧 Troubleshooting

#### macOS: "The application is damaged and can't be opened."
macOS Gatekeeper blocks applications whose internal files have been modified. The script tries to fix this automatically by re-signing the app. If it fails, run it manually in your terminal:
```bash
sudo codesign --force --deep --sign - /Applications/Cursor.app
```
*(Replace `Cursor.app` with `Antigravity.app` if necessary).*

#### Error: "Could not find CSS file at..."
If you installed your editor in a non-standard location (e.g., a custom drive on Windows), the auto-detection will fail. You can bypass this by passing the absolute path to the `workbench.desktop.main.css` file as an argument:
```bash
python cursor_doki_theme.py "D:\CustomTools\Cursor\resources\app\out\vs\workbench\workbench.desktop.main.css"
```

#### Assets are not showing up / Broken images
This usually happens if the internal CSP (Content Security Policy) blocks the image URL. Ensure you are using the script properly so it copies the assets to the internal `workbench` directory and generates `vscode-file://vscode-app/` URIs.

---

## 🤝 Acknowledgements
Massive thanks to the original creator of this workaround for macOS. This fork expands upon their brilliant idea to bring the joy of Doki Theme to everyone, regardless of their operating system.
