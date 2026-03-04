import os
import sys

# =============================================================================
# CONFIGURATION - Change these to switch characters!
# =============================================================================

# Available characters (sticker_path, wallpaper_name):
CHARACTERS = {
    "echidna":      ("/reZero/echidna/dark/echidna_dark.png", "echidna_dark.png"),
    "rem":          ("/reZero/rem/rem.png", "rem.png"),
    "emilia":       ("/reZero/emilia/dark/emilia_dark.png", "emilia_dark.png"),
    "ram":          ("/reZero/ram/ram.png", "ram.png"),
    "beatrice":     ("/reZero/beatrice/beatrice.png", "beatrice.png"),
    "zero_two":     ("/franxx/zeroTwo/rose/zero_two_rose.png", "zero_two_rose.png"),
    "zero_two_obsidian": ("/franxx/zeroTwo/obsidian/zero_two_obsidian.png", "zero_two_obsidian.png"),
    "monika":       ("/literature/monika/dark/just_monika_dark.png", "just_monika_dark.png"),
    "yuri":         ("/literature/yuri/dark/yuri_dark.png", "yuri_dark.png"),
    "natsuki":      ("/literature/natsuki/dark/natsuki_dark.png", "natsuki_dark.png"),
    "sayori":       ("/literature/sayori/dark/sayori_dark.png", "sayori_dark.png"),
    "megumin":      ("/konoSuba/megumin.png", "megumin.png"),
    "aqua":         ("/konoSuba/aqua/dark/aqua_dark.png", "aqua_dark.png"),
    "darkness":     ("/konoSuba/darkness/dark/darkness_dark.png", "darkness_dark.png"),
    "mai":          ("/bunnySenpai/mai/dark/mai_dark.png", "mai_dark.png"),
    "asuna":        ("/swordArtOnline/asuna/dark/asuna_dark.png", "asuna_dark.png"),
    "rias":         ("/highSchoolDxD/rias/dark/rias_dark.png", "rias_dark.png"),
    "kurisu":       ("/steinsGate/kurisu/dark/kurisu_dark.png", "kurisu_dark.png"),
    "miku":         ("/miscellaneous/miku/miku.png", "miku.png"),
    "tohru":        ("/dragonMaid/tohru/light/tohru_light.png", "tohru_light.png"),
    "kanna":        ("/dragonMaid/kanna/dark/kanna_dark.png", "kanna_dark.png"),
    "raphtalia":    ("/shieldHero/raphtalia/dark/raphtalia_dark.png", "raphtalia_dark.png"),
    "ryuko":        ("/killLaKill/ryuko/dark/ryuko.png", "ryuko.png"),
    "satsuki":      ("/killLaKill/satsuki/dark/satsuki_dark.png", "satsuki_dark.png"),
    "rin":          ("/fate/rin/dark/rin_dark_v2.png", "rin_dark_v2.png"),
    "astolfo":      ("/fate/astolfo/dark/astolfo_dark.png", "astolfo_dark.png"),
    "ishtar":       ("/fate/ishtar/dark/ishtar_dark.png", "ishtar_dark.png"),
    "konata":       ("/luckyStar/konata/dark/konata_dark.png", "konata_dark.png"),
    "taiga":        ("/toradora/taiga/dark/taiga_dark.png", "taiga_dark.png"),
}

# >>> CHANGE THIS to switch characters! <<<
SELECTED_CHARACTER = "echidna"

# Sticker opacity (0.0 = invisible, 1.0 = fully opaque)
STICKER_OPACITY = 0.4

# Wallpaper opacity
WALLPAPER_OPACITY = 0.15

# =============================================================================

# Get character paths
if SELECTED_CHARACTER not in CHARACTERS:
    print(f"Error: Unknown character '{SELECTED_CHARACTER}'")
    print(f"Available characters: {', '.join(sorted(CHARACTERS.keys()))}")
    sys.exit(1)

sticker_path, wallpaper_name = CHARACTERS[SELECTED_CHARACTER]

# Default path, but can be overridden by a command line argument
css_path = os.path.expanduser("/Applications/Cursor.app/Contents/Resources/app/out/vs/workbench/workbench.desktop.main.css")
if len(sys.argv) > 1:
    css_path = os.path.expanduser(sys.argv[1])

# Build URLs
wallpaper_url = f"https://doki.assets.unthrottled.io/backgrounds/wallpapers/transparent/{wallpaper_name}"
sticker_url = f"https://doki.assets.unthrottled.io/stickers/vscode{sticker_path}"

if not os.path.exists(css_path):
    print(f"Error: Could not find Cursor CSS file at {css_path}")
    print("Please make sure the path is correct.")
    sys.exit(1)

with open(css_path, "r", encoding="utf-8") as f:
    css_content = f.read()

# Remove existing wallpaper injection
wallpaper_start = "/* CUSTOM_CURSOR_BG_START */"
wallpaper_end = "/* CUSTOM_CURSOR_BG_END */"

if wallpaper_start in css_content and wallpaper_end in css_content:
    start_idx = css_content.find(wallpaper_start)
    end_idx = css_content.find(wallpaper_end) + len(wallpaper_end)
    css_content = css_content[:start_idx].rstrip() + "\n" + css_content[end_idx:].lstrip()

# Remove existing sticker injection
sticker_start = "/* CUSTOM_CURSOR_STICKER_START */"
sticker_end = "/* CUSTOM_CURSOR_STICKER_END */"

if sticker_start in css_content and sticker_end in css_content:
    start_idx = css_content.find(sticker_start)
    end_idx = css_content.find(sticker_end) + len(sticker_end)
    css_content = css_content[:start_idx].rstrip() + "\n" + css_content[end_idx:].lstrip()

# Wallpaper CSS (background overlay on editor)
wallpaper_css = f"""
{wallpaper_start}
/* Set the wallpaper directly on the editor container so it overlays everything else */
.monaco-workbench .part.editor > .content {{
    position: relative !important;
}}

.monaco-workbench .part.editor > .content::after {{
    content: '' !important;
    position: absolute !important;
    top: 0 !important;
    left: 0 !important;
    right: 0 !important;
    bottom: 0 !important;
    background-image: url('{wallpaper_url}') !important;
    background-position: right bottom !important;
    background-size: auto 100% !important;
    background-repeat: no-repeat !important;
    opacity: {WALLPAPER_OPACITY} !important;
    pointer-events: none !important;
    z-index: 9999 !important;
}}

/* Ensure the background image doesn't obscure the text */
.monaco-editor .view-lines {{
    z-index: 10000 !important;
    position: relative !important;
}}
.monaco-editor .current-line {{
    z-index: 10000 !important;
    position: relative !important;
}}
{wallpaper_end}
"""

# Sticker CSS (character sticker in corner)
sticker_css = f"""
{sticker_start}
/* Echidna Sticker */
body > .monaco-workbench > .monaco-grid-view > .monaco-grid-branch-node > .monaco-split-view2 > .split-view-container::after,
body > .monaco-workbench > .monaco-grid-view > .monaco-grid-branch-node > .monaco-split-view2 > .monaco-scrollable-element > .split-view-container::after {{
    content: '' !important;
    pointer-events: none !important;
    position: absolute !important;
    z-index: 100 !important;
    width: 100% !important;
    height: 100% !important;
    background-repeat: no-repeat !important;
    opacity: {STICKER_OPACITY} !important;
    background-image: url('{sticker_url}') !important;
    background-position: 100% 97% !important;
    background-size: auto 65% !important;
}}

/* Makes sure notification shows on top of sticker */
.monaco-workbench > .notifications-center,
.notifications-toasts {{
    z-index: 9002 !important;
}}

/* Glass pane effect for notifications */
.notification-toast {{
    backdrop-filter: blur(2px) !important;
}}
{sticker_end}
"""

with open(css_path, "w", encoding="utf-8") as f:
    f.write(css_content.strip() + "\n" + wallpaper_css + sticker_css)

print(f"Successfully injected {SELECTED_CHARACTER.upper()} wallpaper AND sticker into {css_path}!")
print(f"  - Sticker opacity: {STICKER_OPACITY}")
print(f"  - Wallpaper opacity: {WALLPAPER_OPACITY}")
print("Restart Cursor to see the changes.")
