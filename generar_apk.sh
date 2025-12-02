#!/bin/bash
# Script per generar APK del Semàfor Kivy

echo "🚦 Generant APK del Semàfor Interactiu..."
echo ""
echo "⚠️  ADVERTÈNCIA: La primera compilació pot trigar 30-60 minuts!"
echo "    (descarrega i compila totes les dependències d'Android)"
echo ""
echo "📋 Requisits:"
echo "   - Ubuntu/Debian Linux"
echo "   - Mínim 10GB d'espai lliure"
echo "   - Connexió a Internet estable"
echo ""

read -p "Vols continuar? (s/n) " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Ss]$ ]]
then
    echo "❌ Cancel·lat."
    exit 1
fi

echo ""
echo "📦 Pas 1/3: Instal·lant Buildozer..."

# Instal·lar buildozer
pip install --upgrade buildozer

echo ""
echo "🔧 Pas 2/3: Instal·lant dependències del sistema..."

# Instal·lar dependències
sudo apt-get update
sudo apt-get install -y \
    git zip unzip openjdk-17-jdk python3-pip \
    autoconf libtool pkg-config \
    zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 \
    cmake libffi-dev libssl-dev \
    build-essential ccache

echo ""
echo "🏗️  Pas 3/3: Compilant APK..."
echo "    (això pot trigar molt de temps la primera vegada...)"
echo ""

# Compilar APK
buildozer -v android debug

if [ $? -eq 0 ]; then
    echo ""
    echo "✅ APK generat correctament!"
    echo ""
    echo "📱 Ubicació: bin/semaforinteractiu-1.0-debug.apk"
    echo ""
    echo "🔌 Per instal·lar al telèfon:"
    echo "   1. Connecta el telèfon per USB"
    echo "   2. Activa 'Depuració USB' a les opcions de desenvolupador"
    echo "   3. Executa: buildozer android deploy run"
    echo ""
    echo "   O envia'l per correu/WhatsApp i instal·la'l manualment"
    echo ""
else
    echo ""
    echo "❌ Error durant la compilació!"
    echo ""
    echo "💡 Consells:"
    echo "   - Revisa que tens prou espai al disc"
    echo "   - Comprova la connexió a Internet"
    echo "   - Mira els logs a .buildozer/logs/"
    echo ""
fi
