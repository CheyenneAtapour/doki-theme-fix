#!/bin/bash
set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
APP_WORKBENCH="/Applications/Antigravity IDE.app/Contents/Resources/app/out/vs/workbench"

echo "Running theme injection script..."
sudo python3 "$SCRIPT_DIR/antigravity_doki_theme.py"

echo ""
echo "Copying local assets into app bundle..."
sudo cp "$SCRIPT_DIR/orchis.png"         "$APP_WORKBENCH/doki_wallpaper.png"
sudo cp "$SCRIPT_DIR/Orchis_leader.webp" "$APP_WORKBENCH/doki_sticker.png"
echo "Assets copied."

echo ""
echo "Done! Restart Antigravity IDE to see the changes."
