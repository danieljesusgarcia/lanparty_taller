"""
TALLER DE PROGRAMACIÓ - SEMÀFOR INTERACTIU (SOLUCIÓ)
=====================================================
Aquest és el codi complet amb totes les tasques resoltes.
"""

from interficie_semafor import crear_semafor


# =============================================================================
# FUNCIONS DE CONTROL (SOLUCIÓ)
# =============================================================================

def activar_verd(semafor):
    """Activar el llum verd del semàfor."""
    semafor.encendre_llum("verd")


def activar_groc(semafor):
    """Activar el llum groc del semàfor."""
    semafor.encendre_llum("groc")


def activar_vermell(semafor):
    """Activar el llum vermell del semàfor."""
    semafor.encendre_llum("vermell")


def apagar_tots(semafor):
    """Apagar tots els llums del semàfor."""
    semafor.apagar_tots()


def sequencia_normal(semafor):
    """Crear la seqüència normal d'un semàfor: VERD → GROC → VERMELL"""
    semafor.encendre_llum("verd")
    semafor.esperar(2)
    semafor.encendre_llum("groc")
    semafor.esperar(1)
    semafor.encendre_llum("vermell")
    semafor.esperar(2)
    semafor.apagar_tots()


def mode_nocturn(semafor):
    """Mode nocturn - El groc parpelleja."""
    semafor.parpallejar("groc", vegades=5)


# =============================================================================
# TASQUES EXTRA (SOLUCIONS)
# =============================================================================

def sequencia_personalitzada(semafor):
    """Seqüència personalitzada amb efectes."""
    # Anem encenent cada llum amb parpelleig
    semafor.parpallejar("verd", vegades=2, interval=0.3)
    semafor.esperar(0.5)
    semafor.parpallejar("groc", vegades=2, interval=0.3)
    semafor.esperar(0.5)
    semafor.parpallejar("vermell", vegades=2, interval=0.3)
    semafor.apagar_tots()


def emergencia(semafor):
    """Mode emergència amb parpelleig ràpid."""
    semafor.parpallejar("vermell", vegades=10, interval=0.3)


def test_complet(semafor):
    """Prova tots els llums seqüencialment."""
    semafor.encendre_llum("verd")
    semafor.esperar(1)
    semafor.encendre_llum("groc")
    semafor.esperar(1)
    semafor.encendre_llum("vermell")
    semafor.esperar(1)
    semafor.apagar_tots()


# =============================================================================
# TASQUES INTERACTIVES (SOLUCIÓ)
# =============================================================================

def sequencia_amb_temps_personalitzat(semafor):
    """Seqüència amb temps personalitzats per l'usuari."""
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
    """Parpelleig amb color i vegades triats per l'usuari."""
    color = semafor.triar_color()
    vegades = semafor.demanar_numero("Quantes vegades vols que parpellegi?", default=3, minim=1, maxim=20)
    semafor.parpallejar(color, vegades=vegades)


def missatge_personalitzat(semafor):
    """Mostra un missatge personalitzat amb animació."""
    missatge = semafor.demanar_text("Escriu un missatge:", default="Hola!")
    semafor.mostrar_text(f"💬 {missatge}")
    semafor.parpallejar("verd", vegades=2, interval=0.3)
    semafor.mostrar_text(f"✓ Missatge mostrat: {missatge}")


# =============================================================================
# INICI DEL PROGRAMA
# =============================================================================

if __name__ == "__main__":
    # Crear el diccionari amb les funcions
    funcions = {
        'activar_verd': activar_verd,
        'activar_groc': activar_groc,
        'activar_vermell': activar_vermell,
        'apagar_tots': apagar_tots,
        'sequencia_normal': sequencia_normal,
        'mode_nocturn': mode_nocturn,
        # Funcions extra
        'sequencia_personalitzada': sequencia_personalitzada,
        'emergencia': emergencia,
        'test_complet': test_complet,
        # Funcions interactives
        'sequencia_amb_temps_personalitzat': sequencia_amb_temps_personalitzat,
        'parpelleig_personalitzat': parpelleig_personalitzat,
        'missatge_personalitzat': missatge_personalitzat,
    }
    
    # Crear i iniciar el semàfor
    semafor = crear_semafor(funcions)
    semafor.iniciar()
