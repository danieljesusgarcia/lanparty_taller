"""
🚦 SOLUCIÓ - TALLER DE PROGRAMACIÓ - SEMÀFOR KIVY
==================================================
Aquest fitxer conté les solucions de totes les tasques.
"""

def activar_verd(semafor):
    """TASCA 1: Encén el llum verd"""
    semafor.encendre_llum("verd")


def activar_groc(semafor):
    """TASCA 2: Encén el llum groc"""
    semafor.encendre_llum("groc")


def activar_vermell(semafor):
    """TASCA 3: Encén el llum vermell"""
    semafor.encendre_llum("vermell")


def apagar_tots(semafor):
    """TASCA 4: Apaga tots els llums"""
    semafor.apagar_tots()


def sequencia_normal(semafor):
    """TASCA 5: Seqüència normal d'un semàfor"""
    semafor.encendre_llum("verd")
    semafor.esperar(2)
    semafor.encendre_llum("groc")
    semafor.esperar(1)
    semafor.encendre_llum("vermell")
    semafor.esperar(2)
    semafor.apagar_tots()


def mode_nocturn(semafor):
    """TASCA 6: Mode nocturn - groc parpellejant"""
    semafor.parpallejar("groc", vegades=5, interval=0.5)


def sequencia_amb_temps_personalitzat(semafor):
    """TASCA I1: Seqüència amb temps personalitzat"""
    segons_verd = semafor.demanar_numero("Quants segons en verd?", default=2, minim=1, maxim=10)
    segons_groc = semafor.demanar_numero("Quants segons en groc?", default=1, minim=1, maxim=10)
    segons_vermell = semafor.demanar_numero("Quants segons en vermell?", default=2, minim=1, maxim=10)
    
    semafor.encendre_llum("verd")
    semafor.esperar(segons_verd)
    semafor.encendre_llum("groc")
    semafor.esperar(segons_groc)
    semafor.encendre_llum("vermell")
    semafor.esperar(segons_vermell)
    semafor.apagar_tots()


def parpelleig_personalitzat(semafor):
    """TASCA I2: Parpelleig personalitzat"""
    color = semafor.triar_color()
    vegades = semafor.demanar_numero("Quantes vegades?", default=3, minim=1, maxim=20)
    semafor.parpallejar(color, vegades=vegades)


def missatge_personalitzat(semafor):
    """TASCA I3: Missatge personalitzat"""
    missatge = semafor.demanar_text("Escriu un missatge:", default="Hola!")
    semafor.mostrar_text(f"💬 {missatge}")
    semafor.parpallejar("verd", vegades=2, interval=0.3)


# Registre de funcions
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

if __name__ == '__main__':
    from interficie_semafor_kivy import crear_semafor_kivy
    
    print("🚦 Iniciant Semàfor Interactiu (Kivy) - SOLUCIÓ")
    print("📱 Aquesta versió també funciona a Android!")
    print("")
    
    crear_semafor_kivy(funcions)
