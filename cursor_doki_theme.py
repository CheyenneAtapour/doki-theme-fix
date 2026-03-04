import os
import sys

# =============================================================================
# CONFIGURATION - Change these to switch characters!
# =============================================================================

# Available characters (sticker_path, wallpaper_name):
CHARACTERS = {
    # === Re:Zero ===
    "echidna":          ("/reZero/echidna/dark/echidna_dark.png", "echidna_dark.png"),
    "rem":              ("/reZero/rem/rem.png", "rem.png"),
    "ram":              ("/reZero/ram/ram.png", "ram.png"),
    "emilia_dark":      ("/reZero/emilia/dark/emilia_dark.png", "emilia_dark.png"),
    "emilia_light":     ("/reZero/emilia/light/emilia_light.png", "emilia_light.png"),
    "beatrice":         ("/reZero/beatrice/beatrice.png", "beatrice.png"),
    
    # === Darling in the Franxx ===
    "zero_two_rose":    ("/franxx/zeroTwo/rose/zero_two_rose.png", "zero_two_rose.png"),
    "zero_two_obsidian": ("/franxx/zeroTwo/obsidian/zero_two_obsidian.png", "zero_two_obsidian.png"),
    "zero_two_sakura":  ("/franxx/zeroTwo/sakura/zero_two_sakura.png", "zero_two_sakura.png"),
    "zero_two_lily":    ("/franxx/zeroTwo/lily/zero_two_lily.png", "zero_two_lily.png"),
    "hiro":             ("/franxx/hiro/dark/hiro_dark.png", "hiro_dark.png"),
    
    # === DDLC (Literature Club) ===
    "monika_dark":      ("/literature/monika/dark/just_monika_dark.png", "just_monika_dark.png"),
    "monika_light":     ("/literature/monika/light/just_monika.png", "just_monika.png"),
    "yuri_dark":        ("/literature/yuri/dark/yuri_dark.png", "yuri_dark.png"),
    "yuri_light":       ("/literature/yuri/light/yuri.png", "yuri.png"),
    "natsuki_dark":     ("/literature/natsuki/dark/natsuki_dark.png", "natsuki_dark.png"),
    "natsuki_light":    ("/literature/natsuki/light/natsuki.png", "natsuki.png"),
    "sayori_dark":      ("/literature/sayori/dark/sayori_dark.png", "sayori_dark.png"),
    "sayori_light":     ("/literature/sayori/light/sayori.png", "sayori.png"),
    
    # === KonoSuba ===
    "megumin":          ("/konoSuba/megumin.png", "megumin.png"),
    "aqua":             ("/konoSuba/aqua/dark/aqua_dark.png", "aqua_dark.png"),
    "darkness_dark":    ("/konoSuba/darkness/dark/darkness_dark.png", "darkness_dark.png"),
    "darkness_light":   ("/konoSuba/darkness/light/darkness_light.png", "darkness_light.png"),
    
    # === Bunny Senpai ===
    "mai_dark":         ("/bunnySenpai/mai/dark/mai_dark.png", "mai_dark.png"),
    "mai_light":        ("/bunnySenpai/mai/light/mai_light.png", "mai_light.png"),
    
    # === Sword Art Online ===
    "asuna_dark":       ("/swordArtOnline/asuna/dark/asuna_dark.png", "asuna_dark.png"),
    "asuna_light":      ("/swordArtOnline/asuna/light/asuna_light.png", "asuna_light.png"),
    
    # === Kill la Kill ===
    "ryuko_dark":       ("/killLaKill/ryuko/dark/ryuko.png", "ryuko.png"),
    "ryuko_light":      ("/killLaKill/ryuko/light/ryuko_light.png", "ryuko_light.png"),
    "satsuki_dark":     ("/killLaKill/satsuki/dark/satsuki_dark.png", "satsuki_dark.png"),
    "satsuki_light":    ("/killLaKill/satsuki/light/satsuki_light.png", "satsuki_light.png"),
    
    # === Fate ===
    "rin":              ("/fate/rin/dark/rin_dark_v2.png", "rin_dark_v2.png"),
    "astolfo":          ("/fate/astolfo/dark/astolfo_dark.png", "astolfo_dark.png"),
    "ishtar_dark":      ("/fate/ishtar/dark/ishtar_dark.png", "ishtar_dark.png"),
    "ishtar_light":     ("/fate/ishtar/light/ishtar_light.png", "ishtar_light.png"),
    
    # === Code Geass ===
    "cc":               ("/codeGeass/cc/light/cc_light.png", "cc_light.png"),
    
    # === Dragon Maid ===
    "tohru":            ("/dragonMaid/tohru/light/tohru_light.png", "tohru_light.png"),
    "kanna":            ("/dragonMaid/kanna/dark/kanna_dark.png", "kanna_dark.png"),
    
    # === NekoPara ===
    "chocola":          ("/nekoPara/chocola/dark/chocola_dark.png", "chocola_dark.png"),
    "vanilla":          ("/nekoPara/vanilla/dark/vanilla_dark.png", "vanilla_dark.png"),
    "maple_dark":       ("/nekoPara/maple/dark/maple_dark.png", "maple_dark.png"),
    "maple_light":      ("/nekoPara/maple/light/maple_light.png", "maple_light.png"),
    "shigure":          ("/nekoPara/shigure/light/shigure_light.png", "shigure_light.png"),
    "azuki":            ("/nekoPara/azuki/dark/azuki_dark.png", "azuki_dark.png"),
    "coconut":          ("/nekoPara/coconut/dark/coconut_dark.png", "coconut_dark.png"),
    "cinnamon":         ("/nekoPara/cinnamon/dark/cinnamon_dark.png", "cinnamon_dark.png"),
    
    # === Quintessential Quintuplets ===
    "ichika":           ("/quintuplets/ichika/light/ichika_light.png", "ichika_light.png"),
    "nino":             ("/quintuplets/nino/dark/nino_dark.png", "nino_dark.png"),
    "miku_nakano":      ("/quintuplets/miku/dark/nakano_miku_dark.png", "nakano_miku_dark.png"),
    "yotsuba":          ("/quintuplets/yotsuba/dark/yotsuba_dark.png", "yotsuba_dark.png"),
    "itsuki":           ("/quintuplets/itsuki/light/itsuki_light.png", "itsuki_light.png"),
    
    # === Other ===
    "miku":             ("/miscellaneous/miku/miku.png", "miku.png"),
    "kurisu":           ("/steinsGate/kurisu/dark/kurisu_dark.png", "kurisu_dark.png"),
    "rias_crimson":     ("/highSchoolDxD/rias/dark/rias_dark.png", "rias_dark.png"),
    "rias_onyx":        ("/highSchoolDxD/rias/onyx/rias_onyx.png", "rias_onyx.png"),
    "raphtalia":        ("/shieldHero/raphtalia/dark/raphtalia_dark.png", "raphtalia_dark.png"),
    "konata":           ("/luckyStar/konata/dark/konata_dark.png", "konata_dark.png"),
    "senko":            ("/senkoSan/senko/light/senko_light.png", "senko_light.png"),
    "inori":            ("/guiltyCrown/inori/light/inori_light.png", "inori_light.png"),
    "nao":              ("/charlotte/nao/light/nao_light.png", "nao_light.png"),
    "ibuki_dark":       ("/danganronpa/ibuki/dark/ibuki_dark.png", "ibuki_dark.png"),
    "ibuki_light":      ("/danganronpa/ibuki/light/ibuki_light.png", "ibuki_light.png"),
    "nagatoro":         ("/dontToyWithMeMiss/nagatoro/dark/nagatoro_dark.png", "nagatoro_dark.png"),
    "yumeko":           ("/kakegurui/yumeko/dark/yumeko_dark.png", "yumeko_dark.png"),
    "rimuru":           ("/slime/rimuru/dark/rimuru_dark.png", "rimuru_dark.png"),
    "soma":             ("/shokugeki/soma/dark/soma_dark.png", "soma_dark.png"),
}

# >>> CHANGE THIS to switch characters! <<<
SELECTED_CHARACTER = "cc"

# Sticker opacity (0.0 = invisible, 1.0 = fully opaque)
STICKER_OPACITY = 0.4

# Wallpaper opacity
WALLPAPER_OPACITY = 0.5

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
/* {SELECTED_CHARACTER.upper()} Sticker */
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
