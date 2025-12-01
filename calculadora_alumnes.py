"""
TALLER DE PROGRAMACIÓ - CALCULADORA
=====================================
Aprèn programació creant la teva pròpia calculadora!

OBJECTIU: Completar les funcions per fer funcionar la calculadora.

INSTRUCCIONS:
1. Completa les funcions matemàtiques (sumar, restar, multiplicar, dividir)
2. Guarda el fitxer
3. Executa: python3 calculadora_alumnes.py
4. Prova la teva calculadora!
"""

from interficie_calculadora import crear_calculadora


# =============================================================================
# LES TEVES FUNCIONS - PROGRAMA AQUÍ!
# =============================================================================

def sumar(num1, num2):
    """
    Funció per sumar dos números.
    
    TASCA 1: Retorna la suma de num1 i num2
    Pista: utilitza l'operador +
    
    Exemple:
        sumar(5, 3) ha de retornar 8
        sumar(10, 20) ha de retornar 30
    """
    # ESCRIU EL TEU CODI AQUÍ (1 línia)
    pass  # Substitueix aquest 'pass' pel teu codi


def restar(num1, num2):
    """
    Funció per restar dos números.
    
    TASCA 2: Retorna la resta de num1 menys num2
    Pista: utilitza l'operador -
    
    Exemple:
        restar(10, 3) ha de retornar 7
        restar(5, 8) ha de retornar -3
    """
    # ESCRIU EL TEU CODI AQUÍ (1 línia)
    pass


def multiplicar(num1, num2):
    """
    Funció per multiplicar dos números.
    
    TASCA 3: Retorna la multiplicació de num1 per num2
    Pista: utilitza l'operador *
    
    Exemple:
        multiplicar(4, 5) ha de retornar 20
        multiplicar(7, 3) ha de retornar 21
    """
    # ESCRIU EL TEU CODI AQUÍ (1 línia)
    pass


def dividir(num1, num2):
    """
    Funció per dividir dos números.
    
    TASCA 4: Retorna la divisió de num1 entre num2
    Pista: utilitza l'operador /
    
    Exemple:
        dividir(10, 2) ha de retornar 5.0
        dividir(15, 3) ha de retornar 5.0
    
    NOTA: No et preocupis per la divisió per zero,
          la interfície ja ho gestiona!
    """
    # ESCRIU EL TEU CODI AQUÍ (1 línia)
    pass


# =============================================================================
# PROVES DE LES TEVES FUNCIONS (Opcional)
# =============================================================================

def provar_funcions():
    """
    Prova les teves funcions abans d'executar la calculadora.
    Descomenta les línies per provar-les!
    """
    print("\n" + "="*60)
    print("PROVANT LES TEVES FUNCIONS...")
    print("="*60)
    
    # Descomenta aquestes línies per provar les funcions:
    
    # print(f"sumar(5, 3) = {sumar(5, 3)}")  # Ha de ser 8
    # print(f"restar(10, 3) = {restar(10, 3)}")  # Ha de ser 7
    # print(f"multiplicar(4, 5) = {multiplicar(4, 5)}")  # Ha de ser 20
    # print(f"dividir(10, 2) = {dividir(10, 2)}")  # Ha de ser 5.0
    
    print("\n✓ Si tots els resultats són correctes, pots executar la calculadora!")
    print("="*60 + "\n")


# =============================================================================
# CONFIGURACIÓ DE LA CALCULADORA (TASCA EXTRA - Opcional)
# =============================================================================

def obtenir_configuracio():
    """
    TASCA 5 (OPCIONAL): Personalitza l'aparença de la teva calculadora!
    
    Pots canviar els colors, mides i el títol de la calculadora.
    Descomenta i modifica els valors que vulguis canviar.
    
    Colors disponibles (format hexadecimal):
    - Blaus: '#3498DB', '#2980B9', '#5DADE2'
    - Verds: '#27AE60', '#2ECC71', '#16A085'
    - Vermells: '#E74C3C', '#C0392B', '#E67E22'
    - Grisos: '#34495E', '#2C3E50', '#95A5A6'
    - Grocs: '#F39C12', '#F1C40F'
    - Morats: '#9B59B6', '#8E44AD'
    
    Pots trobar més colors a: https://htmlcolorcodes.com/
    """
    config = {
        # Descomenta i modifica el que vulguis canviar:
        
        # 'titol': 'La Meva Calculadora Pro',
        # 'mida': '500x600',  # amplada x alçada
        # 'color_fons': '#34495E',  # Color de fons de la finestra
        # 'color_numeros': '#2980B9',  # Color dels botons de números
        # 'color_operacions': '#F39C12',  # Color dels botons d'operacions
        # 'color_especial': '#C0392B',  # Color del botó Clear
        # 'color_igual': '#16A085',  # Color del botó =
        # 'mida_font_pantalla': 22,  # Mida de la font de la pantalla
        # 'mida_font_botons': 20,  # Mida de la font dels botons
        # 'autor': 'El meu nom',  # El teu nom per posar al peu
    }
    
    return config


# =============================================================================
# INICI DEL PROGRAMA
# =============================================================================

if __name__ == "__main__":
    print("""
╔════════════════════════════════════════════════════════════════╗
║           CALCULADORA - TALLER DE PROGRAMACIÓ                  ║
╠════════════════════════════════════════════════════════════════╣
║                                                                ║
║  TASQUES A COMPLETAR:                                         ║
║                                                                ║
║  ✓ TASCA 1: Funció sumar()                                    ║
║  ✓ TASCA 2: Funció restar()                                   ║
║  ✓ TASCA 3: Funció multiplicar()                              ║
║  ✓ TASCA 4: Funció dividir()                                  ║
║                                                                ║
║  Quan hagis completat les tasques, guarda i executa!         ║
║                                                                ║
╚════════════════════════════════════════════════════════════════╝
    """)
    
    # Descomenta aquesta línia si vols provar les funcions primer:
    # provar_funcions()
    
    # Crear el diccionari amb les teves funcions
    funcions = {
        'sumar': sumar,
        'restar': restar,
        'multiplicar': multiplicar,
        'dividir': dividir
    }
    
    # Crear i iniciar la calculadora
    calculadora = crear_calculadora(funcions)
    calculadora.iniciar()
