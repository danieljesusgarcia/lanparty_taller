[app]

# Títol de l'aplicació
title = Semafor Interactiu

# Nom del paquet (únic per Google Play)
package.name = semaforinteractiu
package.domain = org.lanpartytaller

# Directori amb el codi font
source.dir = .
source.include_exts = py

# Versió de l'aplicació
version = 1.0

# Dependències Python
requirements = python3,kivy

# Orientació de la pantalla (portrait o landscape)
orientation = portrait

# No posar pantalla completa
fullscreen = 0

# Icona de l'aplicació (crea un fitxer icon.png de 512x512)
#icon.filename = %(source.dir)s/icon.png

# Permisos d'Android
android.permissions = INTERNET

# API d'Android
android.api = 31
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True

# Arxius a incloure
source.include_patterns = semafor_alumnes_kivy_solucio.py,interficie_semafor_kivy.py

[buildozer]

# Nivell de log (1 = debug, 2 = info)
log_level = 2

# Avisar si s'executa com a root
warn_on_root = 1
