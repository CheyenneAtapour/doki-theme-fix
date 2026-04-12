# =============================================================================
#  DOKI THEME - USER CONFIGURATION
#  Edit this file to personalize your theme. Don't touch the other scripts.
# =============================================================================

# ----------------------------------------------------------------------------
# OPTION A: Use a built-in Doki character
# Set SELECTED_CHARACTER to any of the names in the CHARACTERS list below.
# Set CUSTOM_STICKER and CUSTOM_WALLPAPER to None when using a built-in.
# ----------------------------------------------------------------------------
#
#   "echidna", "rem", "ram", "emilia_dark", "emilia_light", "beatrice",
#   "monika_dark", "monika_light", "yuri_dark", "yuri_light",
#   "natsuki_dark", "natsuki_light", "sayori_dark", "sayori_light",
#   "megumin", "aqua", "darkness_dark", "darkness_light",
#   "mai_dark", "mai_light",
#   "asuna_dark", "asuna_light",
#   "ryuko_dark", "ryuko_light", "satsuki_dark", "satsuki_light",
#   "rin", "astolfo", "ishtar_dark", "ishtar_light",
#   "cc", "tohru", "kanna",
#   "chocola", "vanilla", "maple_dark", "maple_light",
#   "shigure", "azuki", "coconut", "cinnamon",
#   "ichika", "nino", "miku_nakano", "yotsuba", "itsuki",
#   "rikka", "tsubasa",
#   "miku", "kurisu", "rias_crimson", "rias_onyx", "raphtalia",
#   "konata", "senko", "inori", "nao",
#   "ibuki_dark", "ibuki_light", "nagatoro", "yumeko", "rimuru", "soma",
#
# (Cursor only also has: "zero_two_rose", "zero_two_obsidian",
#   "zero_two_sakura", "zero_two_lily", "hiro")

SELECTED_CHARACTER = "custom"

# ----------------------------------------------------------------------------
# OPTION B: Use custom local image files
# Set SELECTED_CHARACTER = "custom" and fill in the paths below.
# Use None to disable the wallpaper or sticker individually.
# Paths can be Windows (C:\...) or forward-slash style.
#
# Example:
#   CUSTOM_STICKER   = r"C:\Users\YourName\Pictures\my_sticker.png"
#   CUSTOM_WALLPAPER = r"C:\Users\YourName\Pictures\my_wallpaper.png"
#   CUSTOM_WALLPAPER = None   # <- disables wallpaper, keeps sticker only
# ----------------------------------------------------------------------------

CUSTOM_STICKER   = r"C:\Users\acalderon\Pictures\anzu.png"
CUSTOM_WALLPAPER = None   # No wallpaper, sticker only


# ----------------------------------------------------------------------------
# APPEARANCE
# ----------------------------------------------------------------------------

# Sticker size (pixels wide, height is automatic)
STICKER_WIDTH     = 200

# Sticker opacity: 0.0 = fully invisible, 1.0 = fully opaque
STICKER_OPACITY = 0.3

# Wallpaper opacity: 0.0 = fully invisible, 1.0 = fully opaque
# (Only relevant when a wallpaper is set)
WALLPAPER_OPACITY = 0.45
