import os
import sys

# Default path for Antigravity, but can be overridden by a command line argument
css_path = os.path.expanduser("/Applications/Antigravity.app/Contents/Resources/app/out/vs/workbench/workbench.desktop.main.css")
if len(sys.argv) > 1:
    css_path = os.path.expanduser(sys.argv[1])

wallpaper_url = "https://raw.githubusercontent.com/doki-theme/doki-theme-assets/master/backgrounds/wallpapers/transparent/echidna_dark.png"
sticker_url = "https://raw.githubusercontent.com/doki-theme/doki-theme-assets/master/stickers/echidna/dark_echidna.png"

if not os.path.exists(css_path):
    print(f"Error: Could not find Antigravity CSS file at {css_path}")
    print("Please make sure the path is correct.")
    sys.exit(1)

with open(css_path, "r", encoding="utf-8") as f:
    css_content = f.read()

start_marker = "/* CUSTOM_ANTIGRAVITY_BG_START */"
end_marker = "/* CUSTOM_ANTIGRAVITY_BG_END */"

if start_marker in css_content and end_marker in css_content:
    start_idx = css_content.find(start_marker)
    end_idx = css_content.find(end_marker) + len(end_marker)
    css_content = css_content[:start_idx].rstrip() + "\n" + css_content[end_idx:].lstrip()

injected_css = f"""
{start_marker}
/* --- BACKGROUND WALLPAPER --- */
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
    opacity: 0.15 !important;
    pointer-events: none !important;
    z-index: 9999 !important;
}}

/* --- DOKI STICKER --- */
/* Completely sidestep container clipping by making a full-screen invisible overlay layer */
html::after {{
    content: '' !important;
    position: fixed !important;
    top: 0 !important;
    left: 0 !important;
    width: 100vw !important;
    height: 100vh !important;
    background-image: url('{sticker_url}') !important;
    background-position: right 10px bottom 40px !important;  /* Offset slightly from the very edges */
    background-size: 350px 350px !important;
    background-repeat: no-repeat !important;
    opacity: 1.0 !important;
    pointer-events: none !important; /* Extremely important so you can still click things underneath */
    z-index: 2147483647 !important; /* Maximum possible CSS z-index value */
}}

/* Ensure the background image doesn't obscure the text */
.monaco-editor .view-lines,
.monaco-editor .current-line {{
    z-index: 10000 !important;
    position: relative !important;
}}

/* Set the wallpaper on the main container as a fallback */
.monaco-workbench .part.editor {{
    background-image: url('{wallpaper_url}') !important;
    background-position: right bottom !important;
    background-size: auto 100% !important;
    background-repeat: no-repeat !important;
}}

/* Force all inner editor layers to be transparent so the wallpaper shows through */
.monaco-workbench .part.editor > .content,
.monaco-workbench .part.editor > .content .editor-instance,
.monaco-workbench .part.editor > .content .monaco-editor,
.monaco-workbench .part.editor > .content .monaco-editor-background,
.monaco-workbench .part.editor > .content .margin {{
    background-color: transparent !important;
    background-image: none !important;
}}
{end_marker}
"""

with open(css_path, "w", encoding="utf-8") as f:
    f.write(css_content.strip() + "\n" + injected_css)

print(f"Successfully injected Echidna background AND sticker CSS into {css_path}!")
