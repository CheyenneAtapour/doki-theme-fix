# config.example.py
# Rename this file to config.py and customize your settings.

# =============================================================================
# CONFIGURATION - Change these to switch characters!
# =============================================================================
# You can use built-in character names (e.g., 'echidna', 'rem', 'cc', etc.)
# Or use 'custom' to specify your own local images below.

SELECTED_CHARACTER = "cc"

# Sticker and Wallpaper Opacity
# (0.0 = completely transparent/invisible, 1.0 = fully opaque)
STICKER_OPACITY = 0.4
WALLPAPER_OPACITY = 0.5
STICKER_WIDTH = 350

# =============================================================================
# CUSTOM LOCAL ASSETS (Optional)
# =============================================================================
# Only used if SELECTED_CHARACTER = "custom". 
# Set absolute paths to your local image files.
# If you don't want a wallpaper, set CUSTOM_WALLPAPER = None.
CUSTOM_STICKER = None      # e.g., "/path/to/my_sticker.png" or "C:\\images\\sticker.png"
CUSTOM_WALLPAPER = None    # e.g., "/path/to/my_wallpaper.png" or "C:\\images\\wallpaper.png"
