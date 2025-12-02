# 📱 Versió Kivy del Semàfor - Per Android

## 🎯 Què és aquesta versió?

Aquesta és una versió **avançada** del taller del semàfor que:
- ✅ Funciona a **desktop** (Linux/Windows/Mac)
- ✅ Es pot convertir en **APK per Android**
- ✅ Utilitza **Kivy** en lloc de Tkinter
- ✅ Manté la **mateixa estructura didàctica**

## ⚠️ Recomanacions

**Aquesta versió NO és per al taller principal**. Utilitza-la:
- Com a **bonus** per alumnes avançats
- Per ensenyar **desenvolupament mòbil**
- Com a projecte de **continuació** després del taller Tkinter

**Per al taller presencial, usa la versió Tkinter** (més senzilla i fàcil de debugar).

## 📋 Requisits

### Per Desktop
```bash
# Instal·lar Kivy
pip install kivy

# Verificar instal·lació
python3 -c "import kivy; print(kivy.__version__)"
```

### Per Android (més avançat)
Necessites:
- Linux (Ubuntu recomanat)
- Buildozer (`pip install buildozer`)
- Dependències del sistema (Java, Android SDK, etc.)

## 🚀 Execució Desktop

```bash
# Executar versió alumnes
python3 semafor_alumnes_kivy.py

# Executar solució completa
python3 semafor_alumnes_kivy_solucio.py
```

## 📱 Generar APK per Android

### 1. Instal·lar Buildozer

```bash
pip install buildozer
sudo apt-get install -y python3-pip build-essential git \
    libffi-dev libssl-dev libjpeg-dev zlib1g-dev
```

### 2. Crear buildozer.spec

```bash
buildozer init
```

### 3. Editar buildozer.spec

Edita el fitxer generat:

```ini
[app]
title = Semàfor Interactiu
package.name = semaforinteractiu
package.domain = org.taller

source.dir = .
source.include_exts = py

version = 1.0

requirements = python3,kivy

orientation = portrait
fullscreen = 0

android.permissions = INTERNET

android.api = 31
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1
```

### 4. Construir APK

```bash
# Primera vegada (pot trigar 30-60 minuts!)
buildozer -v android debug

# L'APK estarà a: bin/semaforinteractiu-1.0-debug.apk
```

### 5. Instal·lar a Android

```bash
# Connecta el telèfon per USB i activa "Depuració USB"
buildozer android deploy run

# O manualment:
adb install bin/semaforinteractiu-1.0-debug.apk
```

## 📁 Fitxers de la Versió Kivy

- `semafor_alumnes_kivy.py` - Fitxer per als alumnes
- `interficie_semafor_kivy.py` - Interfície gràfica Kivy
- `semafor_alumnes_kivy_solucio.py` - Solució completa
- `README_KIVY.md` - Aquest fitxer
- `buildozer.spec` - Configuració per generar APK (crear amb `buildozer init`)

## 🎓 Diferències amb la Versió Tkinter

| Aspecte | Tkinter | Kivy |
|---------|---------|------|
| **Plataforma** | Desktop | Desktop + Mòbil |
| **Instal·lació** | Inclosa amb Python | `pip install kivy` |
| **Complexitat** | Senzilla | Mitjana |
| **APK Android** | ❌ No | ✅ Sí |
| **Depuració** | Fàcil | Mitjana |
| **Recomanat per** | Taller inicial | Bonus avançat |

## 🛠️ Resolució de Problemes

### Error: "ModuleNotFoundError: No module named 'kivy'"
```bash
pip install kivy
```

### Error en buildozer (Android)
```bash
# Netejar i recompilar
buildozer android clean
buildozer -v android debug
```

### L'app es tanca a Android
- Revisa els logs: `buildozer android logcat`
- Assegura't que totes les dependències estan a `requirements`

### Diàlegs no funcionen bé
Els diàlegs de Kivy són més bàsics que els de Tkinter. Poden semblar menys "nadius".

## 💡 Consells per Alumnes Avançats

### 1. Personalitza l'Estil
```python
# A interficie_semafor_kivy.py, modifica colors:
self.colors = {
    'vermell': (1, 0, 0, 1),  # R, G, B, Alpha
    'groc': (1, 1, 0, 1),
    'verd': (0, 1, 0, 1),
}
```

### 2. Afegeix Sons
```python
# Instal·la: pip install kivy-garden
# garden install audio

from kivy.core.audio import SoundLoader
sound = SoundLoader.load('beep.wav')
sound.play()
```

### 3. Crea Noves Funcions
Segueix el mateix patró que les existents!

### 4. Canvia la Icona de l'App
Afegeix a `buildozer.spec`:
```ini
icon.filename = %(source.dir)s/icon.png
```

## 📚 Recursos Addicionals

- [Documentació oficial Kivy](https://kivy.org/doc/stable/)
- [Buildozer GitHub](https://github.com/kivy/buildozer)
- [Kivy Tutorial](https://kivy.org/doc/stable/tutorials/firstwidget.html)
- [Packaging per Android](https://kivy.org/doc/stable/guide/packaging-android.html)

## 🎯 Objectius d'Aprenentatge (Versió Kivy)

Amb aquesta versió avançada, els alumnes aprenen:

1. ✅ **Multi-plataforma**: El mateix codi funciona a desktop i mòbil
2. ✅ **Frameworks**: Com utilitzar una biblioteca gràfica externa
3. ✅ **Packaging**: Com crear aplicacions distribuïbles (APK)
4. ✅ **Adaptabilitat**: Com adaptar conceptes de Tkinter a Kivy
5. ✅ **Cicle complet**: Des del codi fins a l'app instal·lable

## 🚀 Següents Passos

Després de completar aquesta versió:

1. **Publica l'app** a Google Play (necessita compte desenvolupador)
2. **Afegeix funcionalitats**: sensors del mòbil, geolocalització, etc.
3. **Crea altres apps**: Calculadora, jocs, utilitats
4. **Aprèn altres frameworks**: Flutter, React Native, etc.

## ⏱️ Temps Estimat

- **Programació de funcions**: Igual que versió Tkinter (45-90 min)
- **Instal·lació Kivy**: 10-15 min
- **Primera compilació APK**: 30-60 min (només primera vegada!)
- **Compilacions posteriors**: 5-10 min

## 📧 Suport

Per dubtes sobre:
- **Kivy**: [Fòrum oficial](https://groups.google.com/g/kivy-users)
- **Buildozer**: [Issues GitHub](https://github.com/kivy/buildozer/issues)
- **Aquest taller**: Contacta el professor

---

**Versió**: 1.0  
**Data**: Desembre 2025  
**Requisits**: Python 3.7+, Kivy 2.0+

**Nota Important**: Generar APKs requereix temps i paciència. La primera compilació pot trigar molt. És normal! ⏳
