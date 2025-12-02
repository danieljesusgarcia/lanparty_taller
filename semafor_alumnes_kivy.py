"""
🚦 TALLER DE PROGRAMACIÓ - SEMÀFOR INTERACTIU (VERSIÓ KIVY)
============================================================

INSTRUCCIONS:
1. Completa les funcions més avall
2. NO modifiquis el fitxer interficie_semafor_kivy.py
3. Executa aquest fitxer per veure el resultat!

MÈTODES DISPONIBLES (crida'ls dins de les funcions):
- semafor.encendre_llum("verd")      → Encén el llum verd
- semafor.encendre_llum("groc")      → Encén el llum groc
- semafor.encendre_llum("vermell")   → Encén el llum vermell
- semafor.apagar_tots()              → Apaga tots els llums
- semafor.esperar(2)                 → Espera 2 segons
- semafor.parpallejar("verd", vegades=3, interval=0.5) → Fa parpallejar
- semafor.mostrar_text("Hola!")      → Mostra un missatge

MÈTODES INTERACTIUS:
- semafor.demanar_numero("Pregunta?", default=2, minim=1, maxim=10)
- semafor.demanar_text("Pregunta?", default="Hola")
- semafor.triar_color()              → Retorna "verd", "groc" o "vermell"
"""

# ============================================
# TASQUES BÀSIQUES
# ============================================

def activar_verd(semafor):
    """
    TASCA 1: Encén el llum verd
    
    Exemple:
        semafor.encendre_llum("verd")
    """
    pass  # ← Substitueix aquesta línia pel teu codi


def activar_groc(semafor):
    """
    TASCA 2: Encén el llum groc
    """
    pass  # ← Escriu el teu codi aquí


def activar_vermell(semafor):
    """
    TASCA 3: Encén el llum vermell
    """
    pass  # ← Escriu el teu codi aquí


def apagar_tots(semafor):
    """
    TASCA 4: Apaga tots els llums
    """
    pass  # ← Escriu el teu codi aquí


def sequencia_normal(semafor):
    """
    TASCA 5: Seqüència normal d'un semàfor
    
    Ordre: VERD (2s) → GROC (1s) → VERMELL (2s) → Apagar
    
    Exemple:
        semafor.encendre_llum("verd")
        semafor.esperar(2)
        semafor.encendre_llum("groc")
        ...
    """
    pass  # ← Escriu el teu codi aquí


def mode_nocturn(semafor):
    """
    TASCA 6: Mode nocturn - groc parpellejant
    
    Parpelleig del groc 5 vegades amb intervals de 0.5 segons
    
    Exemple:
        semafor.parpallejar("groc", vegades=5, interval=0.5)
    """
    pass  # ← Escriu el teu codi aquí


# ============================================
# TASQUES INTERACTIVES (OPCIONALS)
# ============================================

def sequencia_amb_temps_personalitzat(semafor):
    """
    TASCA I1: Seqüència amb temps que tria l'usuari
    
    1. Demana quants segons vol cada llum
    2. Executa la seqüència amb aquests temps
    
    Exemple:
        segons_verd = semafor.demanar_numero("Segons en verd?", default=2, minim=1, maxim=10)
        semafor.encendre_llum("verd")
        semafor.esperar(segons_verd)
        ...
    """
    pass  # ← Escriu el teu codi aquí


def parpelleig_personalitzat(semafor):
    """
    TASCA I2: Parpelleig del color que tria l'usuari
    
    1. L'usuari tria el color
    2. L'usuari tria quantes vegades
    3. Executa el parpelleig
    
    Exemple:
        color = semafor.triar_color()
        vegades = semafor.demanar_numero("Quantes vegades?", default=3)
        semafor.parpallejar(color, vegades=vegades)
    """
    pass  # ← Escriu el teu codi aquí


def missatge_personalitzat(semafor):
    """
    TASCA I3: Mostra un missatge personalitzat
    
    1. Demana un missatge a l'usuari
    2. Mostra'l amb una animació
    
    Exemple:
        missatge = semafor.demanar_text("Escriu un missatge:", default="Hola!")
        semafor.mostrar_text(f"💬 {missatge}")
        semafor.parpallejar("verd", vegades=2)
    """
    pass  # ← Escriu el teu codi aquí


# ============================================
# REGISTRE DE FUNCIONS (NO TOCAR!)
# ============================================

funcions = {
    'activar_verd': activar_verd,
    'activar_groc': activar_groc,
    'activar_vermell': activar_vermell,
    'apagar_tots': apagar_tots,
    'sequencia_normal': sequencia_normal,
    'mode_nocturn': mode_nocturn,
    'sequencia_amb_temps_personalitzat': sequencia_amb_temps_personalitzat,
    'parpelleig_personalitzat': parpelleig_personalitzat,
    'missatge_personalitzat': missatge_personalitzat,
}


# ============================================
# EXECUCIÓ DEL PROGRAMA (NO TOCAR!)
# ============================================

if __name__ == '__main__':
    from interficie_semafor_kivy import crear_semafor_kivy
    
    print("🚦 Iniciant Semàfor Interactiu (Kivy)...")
    print("📱 Aquesta versió també funciona a Android!")
    print("")
    
    crear_semafor_kivy(funcions)
