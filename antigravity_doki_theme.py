import os
import sys
import urllib.request

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
    
    # === Chuunibyou ===
    "rikka":            ("/chuunibyou/rikka/dark/rikka_dark.png", "rikka_dark.png"),
    
    # === Monogatari ===
    "tsubasa":          ("/monogatari/hanekawa/dark/hanekawa_dark.png", "hanekawa_dark.png"),
    
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
    # === Custom ===
    "orchis":           ("file:///Users/cheyenneatapour/Documents/github/doki-theme-fix/Orchis_leader.webp", "file:///Users/cheyenneatapour/Documents/github/doki-theme-fix/orchis.png"),
    "luna":             ("file:///Users/cheyenneatapour/Documents/github/doki-theme-fix/Luna_leader.png", "file:///Users/cheyenneatapour/Documents/github/doki-theme-fix/Luna_wallpaper.png"),
}

# >>> CHANGE THIS to switch characters! <<<
SELECTED_CHARACTER = "orchis"

# Opacity (0.0 = invisible, 1.0 = fully opaque)
STICKER_OPACITY = 0.3
WALLPAPER_OPACITY = 0.45

# =============================================================================

if SELECTED_CHARACTER not in CHARACTERS:
    print(f"Error: Unknown character '{SELECTED_CHARACTER}'")
    print(f"Available characters: {', '.join(sorted(CHARACTERS.keys()))}")
    sys.exit(1)

sticker_path, wallpaper_name = CHARACTERS[SELECTED_CHARACTER]

# Default path for Antigravity, but can be overridden by a command line argument
app_dir = "/Applications/Antigravity.app/Contents/Resources/app/out/vs/workbench"
if len(sys.argv) > 1:
    app_dir = os.path.dirname(os.path.expanduser(sys.argv[1]))

css_path = os.path.join(app_dir, "workbench.desktop.main.css")
js_path = os.path.join(app_dir, "workbench.desktop.main.js")

if wallpaper_name.startswith("http") or wallpaper_name.startswith("file://"):
    wallpaper_url = wallpaper_name
else:
    wallpaper_url = f"https://doki.assets.unthrottled.io/backgrounds/wallpapers/transparent/{wallpaper_name}"

if sticker_path.startswith("http") or sticker_path.startswith("file://"):
    sticker_url = sticker_path
else:
    sticker_url = f"https://doki.assets.unthrottled.io/stickers/vscode{sticker_path}"

# We must download them locally because Antigravity's Strict Content Security Policy (CSP) blocks external images!
local_wallpaper_path = os.path.join(app_dir, "doki_wallpaper.png")
local_sticker_path = os.path.join(app_dir, "doki_sticker.png")

if not os.path.exists(css_path) or not os.path.exists(js_path):
    print(f"Error: Could not find Antigravity CSS/JS files at {app_dir}")
    print("Please make sure the path is correct.")
    sys.exit(1)

import subprocess
import shutil

if wallpaper_url.startswith("file://") and sticker_url.startswith("file://"):
    print(f"Using local {SELECTED_CHARACTER.capitalize()} assets...")
    # Strip the file:// prefix to get the absolute path on disk
    local_wallpaper_path_tmp = wallpaper_url.replace("file://", "")
    local_sticker_path_tmp = sticker_url.replace("file://", "")
    
    # Antigravity CSP blocks /Users/ paths! We must copy them to the protected /Applications directory.
    print("Assets are local! Please manually copy them to bypass CSP blocks:")
    print(f"  {local_wallpaper_path}")
    print(f"  {local_sticker_path}")
    
    # The CSS/JS MUST point to the /Applications/... directory for Antigravity to render them!
    local_wallpaper_css_url = f"vscode-file://vscode-app{local_wallpaper_path}"
    local_sticker_js_url = f"vscode-file://vscode-app{local_sticker_path}"
else:
    print(f"Downloading {SELECTED_CHARACTER.capitalize()} assets locally to bypass CSP...")
    try:
        # Use curl to download to /tmp first so we don't need sudo for the network request
        tmp_wallpaper = f"/tmp/doki_wallpaper_{SELECTED_CHARACTER}.png"
        tmp_sticker = f"/tmp/doki_sticker_{SELECTED_CHARACTER}.png"
        
        cmd_wallpaper = [
            "curl", "-sL", "-A", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36", 
            wallpaper_url, "-o", tmp_wallpaper
        ]
        subprocess.run(cmd_wallpaper, check=True)
        
        cmd_sticker = [
            "curl", "-sL", "-A", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36", 
            sticker_url, "-o", tmp_sticker
        ]
        subprocess.run(cmd_sticker, check=True)
        
        # Note: Copying to the protected /Applications directory requires sudo permissions
        # We leave that step to the user/runner script rather than hanging on subprocess prompts
        print("Assets downloaded to /tmp! Please manually copy them to:")
        print(f"  {local_wallpaper_path}")
        print(f"  {local_sticker_path}")
        
        # We must explicitly set variables for the subsequent CSS injection steps
        # to read /tmp rather than the missing /Applications location
        local_wallpaper_path_tmp = tmp_wallpaper
        local_sticker_path_tmp = tmp_sticker
        
        local_wallpaper_css_url = f"vscode-file://vscode-app{local_wallpaper_path_tmp}"
        local_sticker_js_url = f"vscode-file://vscode-app{local_sticker_path_tmp}"

    except Exception as e:
        print(f"Failed to download assets: {e}")
        sys.exit(1)

# -------- INJECT CSS BACKGROUND --------
with open(css_path, "r", encoding="utf-8") as f:
    css_content = f.read()

start_marker_css = "/* CUSTOM_ANTIGRAVITY_BG_START */"
end_marker_css = "/* CUSTOM_ANTIGRAVITY_BG_END */"

if start_marker_css in css_content and end_marker_css in css_content:
    start_idx = css_content.find(start_marker_css)
    end_idx = css_content.find(end_marker_css) + len(end_marker_css)
    css_content = css_content[:start_idx].rstrip() + "\n" + css_content[end_idx:].lstrip()

injected_css = f"""
{start_marker_css}
/* --- BACKGROUND WALLPAPER (minimal approach - no z-index hacks) --- */

/* Put the wallpaper on the outermost editor container */
.monaco-workbench .part.editor {{
    background-image: url('{local_wallpaper_css_url}') !important;
    background-position: right bottom !important;
    background-size: auto 100% !important;
    background-repeat: no-repeat !important;
}}

/* Force ALL inner editor layers to be transparent so the wallpaper shows through */
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

/* Dark tint on the editor background layer to dim the wallpaper and improve text readability */
.monaco-workbench .part.editor > .content .monaco-editor-background {{
    background-color: rgba(0, 0, 0, {1.0 - WALLPAPER_OPACITY}) !important;
}}
{end_marker_css}
"""

with open(css_path, "w", encoding="utf-8") as f:
    f.write(css_content.strip() + "\n" + injected_css)


# -------- INJECT JS STICKER --------
with open(js_path, "r", encoding="utf-8") as f:
    js_content = f.read()

start_marker_js = "/* CUSTOM_ANTIGRAVITY_STICKER_START */"
end_marker_js = "/* CUSTOM_ANTIGRAVITY_STICKER_END */"

if start_marker_js in js_content and end_marker_js in js_content:
    start_idx = js_content.find(start_marker_js)
    end_idx = js_content.find(end_marker_js) + len(end_marker_js)
    js_content = js_content[:start_idx].rstrip() + "\n" + js_content[end_idx:].lstrip()

injected_js = f"""
{start_marker_js}
// This script literally waits for the DOM to load and appends an img element floating on top of everything!
setTimeout(function() {{
    const doki_sticker = document.createElement("img");
    doki_sticker.id = "doki_sticker_injected";
    doki_sticker.src = "{local_sticker_js_url}";
    doki_sticker.style.position = "fixed";
    doki_sticker.style.bottom = "20px";
    doki_sticker.style.right = "20px";
    doki_sticker.style.width = "350px";
    doki_sticker.style.height = "auto";
    doki_sticker.style.opacity = "{STICKER_OPACITY}";
    doki_sticker.style.pointerEvents = "none";
    doki_sticker.style.zIndex = "9998"; // Place behind elevated UI elements

    // Remove old sticker if it exists from a previous injection that wasn't cleaned up by Antigravity reload
    const prev = document.getElementById("doki_sticker_injected");
    if (prev) {{
        prev.remove();
    }}
    document.body.appendChild(doki_sticker);
    console.log("Injected Doki sticker!");
}}, 3000);

// --- DOM INSPECTOR: MutationObserver to catch agent accept/reject buttons when they appear ---
(function() {{
    function getPath(el) {{
        const path = [];
        for (let depth = 0; depth < 15 && el && el !== document.body; depth++) {{
            let id = el.id ? "#" + el.id : "";
            let cls = el.className && typeof el.className === "string" ? "." + el.className.trim().split(/\\s+/).join(".") : "";
            path.unshift(el.tagName.toLowerCase() + id + cls);
            el = el.parentElement;
        }}
        return path.join(" > ");
    }}

    function logElement(label, el) {{
        const cs = window.getComputedStyle(el);
        console.log("[DOKI DEBUG] " + label + ": " + getPath(el)
            + " | text: " + (el.textContent || "").substring(0, 80).replace(/\\n/g, " ")
            + " | title: " + (el.title || "")
            + " | z-index: " + cs.zIndex
            + " | pointer-events: " + cs.pointerEvents
            + " | position: " + cs.position);
    }}

    // Watch for ANY new elements added to the editor area
    const observer = new MutationObserver(function(mutations) {{
        mutations.forEach(function(mutation) {{
            mutation.addedNodes.forEach(function(node) {{
                if (node.nodeType !== 1) return;
                // Log any element that looks like it could be accept/reject/agent related
                const html = node.outerHTML || "";
                const cls = node.className || "";
                const text = (node.textContent || "").toLowerCase();
                if (text.includes("accept") || text.includes("reject") || text.includes("discard")
                    || text.includes("apply") || text.includes("revert")
                    || cls.includes("diff") || cls.includes("inline")
                    || cls.includes("agent") || cls.includes("action")
                    || cls.includes("widget") || cls.includes("zone")
                    || cls.includes("review") || cls.includes("change")
                    || cls.includes("ghost") || cls.includes("suggest")) {{
                    logElement("NEW NODE", node);
                    // Also log interactive children
                    const kids = node.querySelectorAll("button, a, [role='button'], .action-label, .codicon");
                    kids.forEach(function(k) {{ logElement("  CHILD", k); }});
                }}
            }});
        }});
    }});
    observer.observe(document.body, {{ childList: true, subtree: true }});
    console.log("[DOKI DEBUG] MutationObserver installed - waiting for agent accept/reject buttons...");
}})();
{end_marker_js}
"""

with open(js_path, "w", encoding="utf-8") as f:
    f.write(js_content.strip() + "\n" + injected_js)


print(f"Successfully injected {SELECTED_CHARACTER.capitalize()} background CSS into {css_path}")
print(f"AND successfully injected {SELECTED_CHARACTER.capitalize()} sticker JS into {js_path}!")
print(f"  - Sticker opacity: {STICKER_OPACITY}")
print(f"  - Wallpaper opacity: {WALLPAPER_OPACITY}")

# -------- RE-SIGN THE APP (macOS Gatekeeper) --------
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

print("Please restart Antigravity to see the changes.")
