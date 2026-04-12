"""
antigravity_doki_theme.py
--------------------------
Injects a Doki-theme sticker (and optional wallpaper) into Antigravity.
Works on both Windows and macOS!

Usage:
    python antigravity_doki_theme.py

Edit config.py to change the character, paths, and opacities.
Pass the path to workbench.desktop.main.css as an argument to override
the default Antigravity install location.
"""

import os
import sys
import subprocess
import shutil
import tempfile
import platform
import urllib.request

# ---------------------------------------------------------------------------
# Load user configuration
# ---------------------------------------------------------------------------
try:
    import config as cfg
except ImportError:
    print("Error: config.py not found. Please create it from the example.")
    sys.exit(1)

SELECTED_CHARACTER = getattr(cfg, "SELECTED_CHARACTER", "rem")
CUSTOM_STICKER     = getattr(cfg, "CUSTOM_STICKER",     None)
CUSTOM_WALLPAPER   = getattr(cfg, "CUSTOM_WALLPAPER",   None)
STICKER_OPACITY    = getattr(cfg, "STICKER_OPACITY",    0.3)
WALLPAPER_OPACITY  = getattr(cfg, "WALLPAPER_OPACITY",  0.45)
STICKER_WIDTH      = getattr(cfg, "STICKER_WIDTH",      350)

# ---------------------------------------------------------------------------
# Built-in character catalogue  (sticker_subpath, wallpaper_filename)
# ---------------------------------------------------------------------------
CHARACTERS = {
    # === Re:Zero ===
    "echidna":          ("/reZero/echidna/dark/echidna_dark.png",         "echidna_dark.png"),
    "rem":              ("/reZero/rem/rem.png",                            "rem.png"),
    "ram":              ("/reZero/ram/ram.png",                            "ram.png"),
    "emilia_dark":      ("/reZero/emilia/dark/emilia_dark.png",           "emilia_dark.png"),
    "emilia_light":     ("/reZero/emilia/light/emilia_light.png",         "emilia_light.png"),
    "beatrice":         ("/reZero/beatrice/beatrice.png",                  "beatrice.png"),
    # === DDLC ===
    "monika_dark":      ("/literature/monika/dark/just_monika_dark.png",  "just_monika_dark.png"),
    "monika_light":     ("/literature/monika/light/just_monika.png",      "just_monika.png"),
    "yuri_dark":        ("/literature/yuri/dark/yuri_dark.png",           "yuri_dark.png"),
    "yuri_light":       ("/literature/yuri/light/yuri.png",               "yuri.png"),
    "natsuki_dark":     ("/literature/natsuki/dark/natsuki_dark.png",     "natsuki_dark.png"),
    "natsuki_light":    ("/literature/natsuki/light/natsuki.png",         "natsuki.png"),
    "sayori_dark":      ("/literature/sayori/dark/sayori_dark.png",       "sayori_dark.png"),
    "sayori_light":     ("/literature/sayori/light/sayori.png",           "sayori.png"),
    # === KonoSuba ===
    "megumin":          ("/konoSuba/megumin.png",                          "megumin.png"),
    "aqua":             ("/konoSuba/aqua/dark/aqua_dark.png",             "aqua_dark.png"),
    "darkness_dark":    ("/konoSuba/darkness/dark/darkness_dark.png",     "darkness_dark.png"),
    "darkness_light":   ("/konoSuba/darkness/light/darkness_light.png",   "darkness_light.png"),
    # === Bunny Senpai ===
    "mai_dark":         ("/bunnySenpai/mai/dark/mai_dark.png",            "mai_dark.png"),
    "mai_light":        ("/bunnySenpai/mai/light/mai_light.png",          "mai_light.png"),
    # === Sword Art Online ===
    "asuna_dark":       ("/swordArtOnline/asuna/dark/asuna_dark.png",     "asuna_dark.png"),
    "asuna_light":      ("/swordArtOnline/asuna/light/asuna_light.png",   "asuna_light.png"),
    # === Kill la Kill ===
    "ryuko_dark":       ("/killLaKill/ryuko/dark/ryuko.png",              "ryuko.png"),
    "ryuko_light":      ("/killLaKill/ryuko/light/ryuko_light.png",       "ryuko_light.png"),
    "satsuki_dark":     ("/killLaKill/satsuki/dark/satsuki_dark.png",     "satsuki_dark.png"),
    "satsuki_light":    ("/killLaKill/satsuki/light/satsuki_light.png",   "satsuki_light.png"),
    # === Fate ===
    "rin":              ("/fate/rin/dark/rin_dark_v2.png",                "rin_dark_v2.png"),
    "astolfo":          ("/fate/astolfo/dark/astolfo_dark.png",           "astolfo_dark.png"),
    "ishtar_dark":      ("/fate/ishtar/dark/ishtar_dark.png",             "ishtar_dark.png"),
    "ishtar_light":     ("/fate/ishtar/light/ishtar_light.png",           "ishtar_light.png"),
    # === Code Geass ===
    "cc":               ("/codeGeass/cc/light/cc_light.png",              "cc_light.png"),
    # === Dragon Maid ===
    "tohru":            ("/dragonMaid/tohru/light/tohru_light.png",       "tohru_light.png"),
    "kanna":            ("/dragonMaid/kanna/dark/kanna_dark.png",         "kanna_dark.png"),
    # === NekoPara ===
    "chocola":          ("/nekoPara/chocola/dark/chocola_dark.png",       "chocola_dark.png"),
    "vanilla":          ("/nekoPara/vanilla/dark/vanilla_dark.png",       "vanilla_dark.png"),
    "maple_dark":       ("/nekoPara/maple/dark/maple_dark.png",           "maple_dark.png"),
    "maple_light":      ("/nekoPara/maple/light/maple_light.png",         "maple_light.png"),
    "shigure":          ("/nekoPara/shigure/light/shigure_light.png",     "shigure_light.png"),
    "azuki":            ("/nekoPara/azuki/dark/azuki_dark.png",           "azuki_dark.png"),
    "coconut":          ("/nekoPara/coconut/dark/coconut_dark.png",       "coconut_dark.png"),
    "cinnamon":         ("/nekoPara/cinnamon/dark/cinnamon_dark.png",     "cinnamon_dark.png"),
    # === Quintessential Quintuplets ===
    "ichika":           ("/quintuplets/ichika/light/ichika_light.png",    "ichika_light.png"),
    "nino":             ("/quintuplets/nino/dark/nino_dark.png",          "nino_dark.png"),
    "miku_nakano":      ("/quintuplets/miku/dark/nakano_miku_dark.png",   "nakano_miku_dark.png"),
    "yotsuba":          ("/quintuplets/yotsuba/dark/yotsuba_dark.png",    "yotsuba_dark.png"),
    "itsuki":           ("/quintuplets/itsuki/light/itsuki_light.png",    "itsuki_light.png"),
    # === Chuunibyou ===
    "rikka":            ("/chuunibyou/rikka/dark/rikka_dark.png",         "rikka_dark.png"),
    # === Monogatari ===
    "tsubasa":          ("/monogatari/hanekawa/dark/hanekawa_dark.png",   "hanekawa_dark.png"),
    # === Other ===
    "miku":             ("/miscellaneous/miku/miku.png",                   "miku.png"),
    "kurisu":           ("/steinsGate/kurisu/dark/kurisu_dark.png",       "kurisu_dark.png"),
    "rias_crimson":     ("/highSchoolDxD/rias/dark/rias_dark.png",        "rias_dark.png"),
    "rias_onyx":        ("/highSchoolDxD/rias/onyx/rias_onyx.png",        "rias_onyx.png"),
    "raphtalia":        ("/shieldHero/raphtalia/dark/raphtalia_dark.png", "raphtalia_dark.png"),
    "konata":           ("/luckyStar/konata/dark/konata_dark.png",        "konata_dark.png"),
    "senko":            ("/senkoSan/senko/light/senko_light.png",         "senko_light.png"),
    "inori":            ("/guiltyCrown/inori/light/inori_light.png",      "inori_light.png"),
    "nao":              ("/charlotte/nao/light/nao_light.png",            "nao_light.png"),
    "ibuki_dark":       ("/danganronpa/ibuki/dark/ibuki_dark.png",        "ibuki_dark.png"),
    "ibuki_light":      ("/danganronpa/ibuki/light/ibuki_light.png",      "ibuki_light.png"),
    "nagatoro":         ("/dontToyWithMeMiss/nagatoro/dark/nagatoro_dark.png", "nagatoro_dark.png"),
    "yumeko":           ("/kakegurui/yumeko/dark/yumeko_dark.png",        "yumeko_dark.png"),
    "rimuru":           ("/slime/rimuru/dark/rimuru_dark.png",            "rimuru_dark.png"),
    "soma":             ("/shokugeki/soma/dark/soma_dark.png",            "soma_dark.png"),
}

# ---------------------------------------------------------------------------
# Resolve sticker / wallpaper sources
# ---------------------------------------------------------------------------

def _is_absolute(p):
    return p and (os.path.isabs(p) or (len(p) > 1 and p[1] == ":"))


if SELECTED_CHARACTER == "custom":
    # Custom mode: user provides raw file paths in config.py
    if not CUSTOM_STICKER and not CUSTOM_WALLPAPER:
        print("Error: SELECTED_CHARACTER is 'custom' but both CUSTOM_STICKER "
              "and CUSTOM_WALLPAPER are None in config.py.")
        sys.exit(1)
    src_sticker_local   = CUSTOM_STICKER    # absolute path or None
    src_wallpaper_local = CUSTOM_WALLPAPER  # absolute path or None
    src_sticker_url     = None
    src_wallpaper_url   = None
    label = "Custom"
else:
    if SELECTED_CHARACTER not in CHARACTERS:
        print(f"Error: Unknown character '{SELECTED_CHARACTER}'")
        print(f"Available characters: {', '.join(sorted(CHARACTERS.keys()))}")
        print("Or set SELECTED_CHARACTER = 'custom' and provide paths in config.py")
        sys.exit(1)
    sticker_sub, wallpaper_file = CHARACTERS[SELECTED_CHARACTER]
    src_sticker_local   = None
    src_wallpaper_local = None
    src_sticker_url     = f"https://doki.assets.unthrottled.io/stickers/vscode{sticker_sub}"
    src_wallpaper_url   = f"https://doki.assets.unthrottled.io/backgrounds/wallpapers/transparent/{wallpaper_file}"
    label = SELECTED_CHARACTER.capitalize()

USE_WALLPAPER = (src_wallpaper_local is not None) or (src_wallpaper_url is not None)

# ---------------------------------------------------------------------------
# Locate Antigravity workbench directory
# ---------------------------------------------------------------------------
def _find_antigravity_dir():
    if platform.system() == "Windows":
        return os.path.join(os.environ.get("LOCALAPPDATA", ""), "Programs", "Antigravity", "resources", "app", "out", "vs", "workbench")
    elif platform.system() == "Darwin":
        return "/Applications/Antigravity.app/Contents/Resources/app/out/vs/workbench"
    else:
        return "/opt/Antigravity/resources/app/out/vs/workbench" # Reasonable default for Linux

default_app_dir = _find_antigravity_dir()

if len(sys.argv) > 1:
    app_dir = os.path.dirname(os.path.expanduser(sys.argv[1]))
else:
    app_dir = default_app_dir

css_path = os.path.join(app_dir, "workbench.desktop.main.css")
js_path  = os.path.join(app_dir, "workbench.desktop.main.js")

if not os.path.exists(css_path) or not os.path.exists(js_path):
    print(f"Error: Could not find Antigravity workbench files at:\n  {app_dir}")
    print("Make sure Antigravity is installed, or pass the CSS path as an argument.")
    sys.exit(1)

# Destination inside the Antigravity install (always the same filenames)
dest_wallpaper = os.path.join(app_dir, "doki_wallpaper.png")
dest_sticker   = os.path.join(app_dir, "doki_sticker.png")

# ---------------------------------------------------------------------------
# Download helper (Cross-Platform)
# ---------------------------------------------------------------------------
def download(url, dest):
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as response, open(dest, 'wb') as out_file:
        shutil.copyfileobj(response, out_file)

# ---------------------------------------------------------------------------
# Copy / download assets into the Antigravity directory
# ---------------------------------------------------------------------------
print(f"Setting up {label} assets...")

# -- Sticker --
if src_sticker_local:
    if not os.path.exists(src_sticker_local):
        print(f"Error: Custom sticker not found: {src_sticker_local}")
        sys.exit(1)
    shutil.copy2(src_sticker_local, dest_sticker)
    print(f"  [OK] Sticker (local)  -> {dest_sticker}")
elif src_sticker_url:
    tmp = os.path.join(tempfile.gettempdir(), "doki_sticker_tmp.png")
    print("  downloading sticker...")
    download(src_sticker_url, tmp)
    shutil.copy2(tmp, dest_sticker)
    print(f"  [OK] Sticker (remote) -> {dest_sticker}")

# -- Wallpaper --
if USE_WALLPAPER:
    if src_wallpaper_local:
        if not os.path.exists(src_wallpaper_local):
            print(f"Error: Custom wallpaper not found: {src_wallpaper_local}")
            sys.exit(1)
        shutil.copy2(src_wallpaper_local, dest_wallpaper)
        print(f"  [OK] Wallpaper (local)  -> {dest_wallpaper}")
    elif src_wallpaper_url:
        tmp = os.path.join(tempfile.gettempdir(), "doki_wallpaper_tmp.png")
        print("  downloading wallpaper...")
        download(src_wallpaper_url, tmp)
        shutil.copy2(tmp, dest_wallpaper)
        print(f"  [OK] Wallpaper (remote) -> {dest_wallpaper}")
else:
    print("  [--] Wallpaper disabled")

# ---------------------------------------------------------------------------
# Build vscode-file:// URL 
# ---------------------------------------------------------------------------
def to_vscode_url(abs_path):
    fwd = abs_path.replace("\\", "/")
    if not fwd.startswith("/"):
        fwd = "/" + fwd          # C:/... -> /C:/...
    return f"vscode-file://vscode-app{fwd}"

sticker_url_local   = to_vscode_url(dest_sticker)
wallpaper_url_local = to_vscode_url(dest_wallpaper) if USE_WALLPAPER else None

# ---------------------------------------------------------------------------
# Inject CSS background wallpaper
# ---------------------------------------------------------------------------
with open(css_path, "r", encoding="utf-8") as f:
    css = f.read()

M_START = "/* CUSTOM_ANTIGRAVITY_BG_START */"
M_END   = "/* CUSTOM_ANTIGRAVITY_BG_END */"

# Always remove previous injection first
if M_START in css and M_END in css:
    i = css.find(M_START)
    j = css.find(M_END) + len(M_END)
    css = css[:i].rstrip() + "\n" + css[j:].lstrip()

if USE_WALLPAPER:
    css += f"""
{M_START}
/* --- DOKI WALLPAPER --- */
.monaco-workbench .part.editor {{
    background-image: url('{wallpaper_url_local}') !important;
    background-position: right bottom !important;
    background-size: auto 100% !important;
    background-repeat: no-repeat !important;
}}
.monaco-workbench .part.editor > .content,
.monaco-workbench .part.editor > .content .split-view-container,
.monaco-workbench .part.editor > .content .split-view-view,
.monaco-workbench .part.editor > .content .editor-group-container,
.monaco-workbench .part.editor > .content .editor-container,
.monaco-workbench .part.editor > .content .editor-instance,
.monaco-workbench .part.editor > .content .monaco-editor,
.monaco-workbench .part.editor > .content .overflow-guard,
.monaco-workbench .part.editor > .content .margin,
.monaco-workbench .part.editor > .content .monaco-scrollable-element,
.monaco-workbench .part.editor > .content .lines-content,
.monaco-workbench .part.editor > .content .view-lines,
.monaco-workbench .part.editor > .content .minimap,
.monaco-workbench .part.editor > .content .editor-scrollable {{
    background-color: transparent !important;
    background-image: none !important;
}}
.monaco-workbench .part.editor > .content .monaco-editor-background {{
    background-color: rgba(0, 0, 0, {1.0 - WALLPAPER_OPACITY:.2f}) !important;
}}
{M_END}
"""
    print("[OK] Wallpaper CSS injected.")
else:
    print("[--] Wallpaper CSS skipped.")

with open(css_path, "w", encoding="utf-8") as f:
    f.write(css.strip() + "\n")

# ---------------------------------------------------------------------------
# Inject JS sticker
# ---------------------------------------------------------------------------
with open(js_path, "r", encoding="utf-8") as f:
    js = f.read()

JS_START = "/* CUSTOM_ANTIGRAVITY_STICKER_START */"
JS_END   = "/* CUSTOM_ANTIGRAVITY_STICKER_END */"

if JS_START in js and JS_END in js:
    i = js.find(JS_START)
    j = js.find(JS_END) + len(JS_END)
    js = js[:i].rstrip() + "\n" + js[j:].lstrip()

js += f"""
{JS_START}
setTimeout(function() {{
    const prev = document.getElementById("doki_sticker_injected");
    if (prev) prev.remove();

    const img = document.createElement("img");
    img.id            = "doki_sticker_injected";
    img.src           = "{sticker_url_local}";
    img.style.cssText = [
        "position:fixed",
        "bottom:20px",
        "right:20px",
        "width:{STICKER_WIDTH}px",
        "height:auto",
        "opacity:{STICKER_OPACITY}",
        "pointer-events:none",
        "z-index:9998"
    ].join(";");
    document.body.appendChild(img);
    console.log("[Doki] Sticker injected: {label}");
}}, 3000);
{JS_END}
"""

with open(js_path, "w", encoding="utf-8") as f:
    f.write(js.strip() + "\n")

print("[OK] Sticker JS injected.")
print()
print(f"Done! Character: {label}")
print(f"  Sticker opacity  : {STICKER_OPACITY}")
print(f"  Wallpaper opacity: {WALLPAPER_OPACITY}")
print()

# -------- RE-SIGN THE APP (macOS Gatekeeper) --------
if platform.system() == "Darwin":
    app_bundle = "/Applications/Antigravity.app"
    if os.path.isdir(app_bundle):
        print("Re-signing Antigravity.app to satisfy macOS Gatekeeper...")
        result = subprocess.run(
            ["codesign", "--force", "--deep", "--sign", "-", app_bundle],
            capture_output=True, text=True
        )
        if result.returncode == 0:
            print("Re-signed successfully!")
        else:
            print(f"Warning: codesign failed (exit {result.returncode}): {result.stderr.strip()}")
            print("You may need to run: codesign --force --deep --sign - /Applications/Antigravity.app")

print("Restart Antigravity to see the changes.")
