[app]

# Application identity
title = Tic-Tac-Toe
package.name = tictactoe
package.domain = org.player
version = 1.0.0

# Source files
source.dir = .
source.include_exts = py,json,txt,png,jpg,jpeg,ttf
source.exclude_dirs = bin,tests,.git,.buildozer

# Pygame on Android uses the SDL2 bootstrap.
# If your installed python-for-android uses the classic pygame recipe,
# replace pygame-ce with pygame in this line.
requirements = python3,pygame-ce

# Phone UI
orientation = portrait
fullscreen = 1

# Modern Android devices
android.api = 35
android.minapi = 23
android.ndk = 27c
android.archs = arm64-v8a
android.accept_sdk_license = True

# Keep build output small and reproducible.
android.private_storage = True

# Optional: uncomment after adding an icon.png (512x512) to the project.
# icon.filename = %(source.dir)s/icon.png
