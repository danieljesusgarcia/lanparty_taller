"""
TALLER DE PROGRAMACIÓ - SEMÀFOR INTERACTIU
===========================================
Aprèn programació controlant un semàfor!

OBJECTIU: Completar les funcions per fer funcionar el semàfor.

INSTRUCCIONS:
1. Completa les funcions de control (activar_verd, activar_groc, etc.)
2. Guarda el fitxer
3. Executa: python3 semafor_alumnes.py
4. Clica els botons per veure el teu semàfor en acció!
"""

from interficie_semafor import crear_semafor


# =============================================================================
# LES TEVES FUNCIONS - PROGRAMA AQUÍ!
# =============================================================================

def activar_verd(semafor):
    """
    TASCA 1: Activar el llum verd del semàfor
    
    Has de cridar el mètode que encén el llum verd.
    
    Pista: semafor.encendre_llum("color")
    
    Exemple:
        Quan l'usuari clica el botó "🟢 Verd", aquesta funció s'executa
        i el llum verd del semàfor s'encén (i els altres s'apaguen).
    """
    # ESCRIU EL TEU CODI AQUÍ (1 línia)
    
    pass  # Substitueix aquest 'pass' pel teu codi


def activar_groc(semafor):
    """
    TASCA 2: Activar el llum groc del semàfor
    
    Has de cridar el mètode que encén el llum groc.
    
    Pista: Utilitza el mateix mètode que a la tasca 1, però amb "groc"
    
    Exemple:
        Quan l'usuari clica el botó "🟡 Groc", el llum groc s'encén.
    """
    # ESCRIU EL TEU CODI AQUÍ (1 línia)
    pass


def activar_vermell(semafor):
    """
    TASCA 3: Activar el llum vermell del semàfor
    
    Has de cridar el mètode que encén el llum vermell.
    
    Pista: Utilitza el mateix mètode, però amb "vermell"
    
    Exemple:
        Quan l'usuari clica el botó "🔴 Vermell", el llum vermell s'encén.
    """
    # ESCRIU EL TEU CODI AQUÍ (1 línia)
    pass


def apagar_tots(semafor):
    """
    TASCA 4: Apagar tots els llums del semàfor
    
    Has de cridar el mètode que apaga tots els llums.
    
    Pista: semafor.apagar_tots()
    
    Exemple:
        Quan l'usuari clica "⚫ Apagar", tots els llums s'apaguen.
    """
    # ESCRIU EL TEU CODI AQUÍ (1 línia)
    pass


def sequencia_normal(semafor):
    """
    TASCA 5: Crear la seqüència normal d'un semàfor
    
    Has de fer que el semàfor faci la seqüència: VERD → GROC → VERMELL
    Amb pauses entre cada canvi.
    
    Mètodes que necessites:
    - semafor.encendre_llum("color")
    - semafor.esperar(segons)
    
    Exemple de codi:
        semafor.encendre_llum("verd")
        semafor.esperar(2)  # Espera 2 segons
        semafor.encendre_llum("groc")
        semafor.esperar(1)  # Espera 1 segon
        # TU ACABES LA SEQÜÈNCIA...
    
    Prova amb diferents temps d'espera!
    """
    # ESCRIU EL TEU CODI AQUÍ (6 línies aproximadament)
    pass


def mode_nocturn(semafor):
    """
    TASCA 6: Mode nocturn - El groc parpelleja
    
    De nit, molts semàfors fan parpallejar el llum groc per avisar.
    Has de fer que el llum groc parpellegi 5 vegades.
    
    Mètode que necessites:
    - semafor.parpallejar("color", vegades=5)
    
    Pista: El color ha de ser "groc" i ha de parpallejar 5 vegades
    
    Exemple:
        Quan l'usuari clica "🌙 Nocturn", el llum groc parpelleja.
    """
    # ESCRIU EL TEU CODI AQUÍ (1 línia)
    pass


# =============================================================================
# TASQUES EXTRA (Opcionals)
# =============================================================================

def sequencia_personalitzada(semafor):
    """
    TASCA EXTRA 1: Crea la teva pròpia seqüència!
    
    Combina els mètodes per crear una seqüència única:
    - Pots fer parpallejar diferents colors
    - Pots canviar els temps d'espera
    - Pots fer seqüències llargues
    
    Sigues creatiu!
    """
    # ESCRIU EL TEU CODI AQUÍ
    pass


def emergencia(semafor):
    """
    TASCA EXTRA 2: Mode emergència
    
    Fes que el llum vermell parpellegi ràpidament (interval curt).
    
    Pista: semafor.parpallejar("vermell", vegades=10, interval=0.3)
    """
    # ESCRIU EL TEU CODI AQUÍ
    pass


def test_complet(semafor):
    """
    TASCA EXTRA 3: Prova tots els llums
    
    Fes una seqüència que provi cada llum individualment:
    1. Encén verd, espera
    2. Encén groc, espera
    3. Encén vermell, espera
    4. Apaga tots
    """
    # ESCRIU EL TEU CODI AQUÍ
    pass


# =============================================================================
# TASQUES INTERACTIVES (Amb input de l'usuari)
# =============================================================================

def sequencia_amb_temps_personalitzat(semafor):
    """
    TASCA INTERACTIVA 1: Seqüència amb temps que tries tu!
    
    Demana a l'usuari quants segons vol que estigui cada llum encès
    i crea una seqüència personalitzada.
    
    Mètodes que necessites:
    - semafor.demanar_numero("pregunta", default=2, minim=1, maxim=10)
    - semafor.encendre_llum("color")
    - semafor.esperar(segons)
    
    Exemple de codi:
        segons_verd = semafor.demanar_numero("Quants segons en verd?", default=2)
        semafor.encendre_llum("verd")
        semafor.esperar(segons_verd)
        
        # Continua amb groc i vermell...
    """
    # ESCRIU EL TEU CODI AQUÍ
    pass


def parpelleig_personalitzat(semafor):
    """
    TASCA INTERACTIVA 2: Parpelleig amb opcions de l'usuari
    
    Demana a l'usuari:
    1. Quin color vol fer parpallejar
    2. Quantes vegades vol que parpellegi
    
    Mètodes que necessites:
    - semafor.triar_color()  # Retorna "verd", "groc" o "vermell"
    - semafor.demanar_numero("pregunta", default=3)
    - semafor.parpallejar(color, vegades)
    
    Exemple de codi:
        color = semafor.triar_color()
        vegades = semafor.demanar_numero("Quantes vegades?", default=3, minim=1, maxim=20)
        semafor.parpallejar(color, vegades)
    """
    # ESCRIU EL TEU CODI AQUÍ
    pass


def missatge_personalitzat(semafor):
    """
    TASCA INTERACTIVA 3: Mostra un missatge personalitzat
    
    Demana a l'usuari que escrigui un missatge i mostra'l a la pantalla
    mentre el semàfor fa una animació.
    
    Mètodes que necessites:
    - semafor.demanar_text("pregunta", default="")
    - semafor.mostrar_text("missatge")
    - semafor.parpallejar() o semafor.encendre_llum()
    
    Exemple de codi:
        missatge = semafor.demanar_text("Escriu un missatge:", default="Hola!")
        semafor.mostrar_text(missatge)
        semafor.parpallejar("verd", vegades=2)
    """
    # ESCRIU EL TEU CODI AQUÍ
    pass


# =============================================================================
# PROVES DE LES TEVES FUNCIONS (Opcional)
# =============================================================================

def provar_funcions():
    """
    Prova les teves funcions abans d'executar el semàfor.
    
    Això et permet veure si les funcions estan ben escrites
    sense haver d'obrir la interfície gràfica.
    """
    print("\n" + "="*60)
    print("PROVANT LES TEVES FUNCIONS...")
    print("="*60)
    
    # Simulem un objecte semàfor simple per proves
    class SemaforProva:
        def encendre_llum(self, color):
            print(f"  ✓ Llum {color} encès")
        
        def apagar_tots(self):
            print(f"  ✓ Tots els llums apagats")
        
        def esperar(self, segons):
            print(f"  ⏱ Esperant {segons} segons...")
        
        def parpallejar(self, color, vegades=3, interval=0.5):
            print(f"  ✨ Parpellejant {color} {vegades} vegades")
    
    semafor_prova = SemaforProva()
    
    print("\n→ Provant activar_verd():")
    try:
        activar_verd(semafor_prova)
    except:
        print("  ❌ Encara no implementada")
    
    print("\n→ Provant activar_groc():")
    try:
        activar_groc(semafor_prova)
    except:
        print("  ❌ Encara no implementada")
    
    print("\n→ Provant activar_vermell():")
    try:
        activar_vermell(semafor_prova)
    except:
        print("  ❌ Encara no implementada")
    
    print("\n→ Provant apagar_tots():")
    try:
        apagar_tots(semafor_prova)
    except:
        print("  ❌ Encara no implementada")
    
    print("\n→ Provant sequencia_normal():")
    try:
        sequencia_normal(semafor_prova)
    except:
        print("  ❌ Encara no implementada")
    
    print("\n" + "="*60)
    print("Si veus ✓ a tot, les teves funcions estan ben escrites!")
    print("="*60 + "\n")


# =============================================================================
# INICI DEL PROGRAMA
# =============================================================================

if __name__ == "__main__":
    print("""
╔════════════════════════════════════════════════════════════════╗
║           SEMÀFOR INTERACTIU - TALLER DE PROGRAMACIÓ          ║
╠════════════════════════════════════════════════════════════════╣
║                                                                ║
║  TASQUES A COMPLETAR:                                         ║
║                                                                ║
║  ✓ TASCA 1: Funció activar_verd()                            ║
║  ✓ TASCA 2: Funció activar_groc()                            ║
║  ✓ TASCA 3: Funció activar_vermell()                         ║
║  ✓ TASCA 4: Funció apagar_tots()                             ║
║  ✓ TASCA 5: Funció sequencia_normal()                        ║
║  ✓ TASCA 6: Funció mode_nocturn()                            ║
║                                                                ║
║  Quan hagis completat les tasques, guarda i executa!         ║
║                                                                ║
╚════════════════════════════════════════════════════════════════╝
    """)
    
    # Descomenta aquesta línia si vols provar les funcions primer:
    # provar_funcions()
    
    # Crear el diccionari amb les teves funcions
    funcions = {
        'activar_verd': activar_verd,
        'activar_groc': activar_groc,
        'activar_vermell': activar_vermell,
        'apagar_tots': apagar_tots,
        'sequencia_normal': sequencia_normal,
        'mode_nocturn': mode_nocturn,
        # Funcions interactives (amb input de l'usuari)
        'sequencia_amb_temps_personalitzat': sequencia_amb_temps_personalitzat,
        'parpelleig_personalitzat': parpelleig_personalitzat,
        'missatge_personalitzat': missatge_personalitzat,
    }
    
    # Crear i iniciar el semàfor
    semafor = crear_semafor(funcions)
    semafor.iniciar()
