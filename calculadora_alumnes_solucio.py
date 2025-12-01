"""
TALLER DE PROGRAMACIÓ - CALCULADORA (SOLUCIÓ)
==============================================
Aquest és el codi complet amb totes les tasques resoltes.
"""

from interficie_calculadora import crear_calculadora


# =============================================================================
# FUNCIONS MATEMÀTIQUES (SOLUCIÓ)
# =============================================================================

def sumar(num1, num2):
    """Funció per sumar dos números."""
    return num1 + num2


def restar(num1, num2):
    """Funció per restar dos números."""
    return num1 - num2


def multiplicar(num1, num2):
    """Funció per multiplicar dos números."""
    return num1 * num2


def dividir(num1, num2):
    """Funció per dividir dos números."""
    return num1 / num2


# =============================================================================
# INICI DEL PROGRAMA
# =============================================================================

if __name__ == "__main__":
    # Crear el diccionari amb les funcions
    funcions = {
        'sumar': sumar,
        'restar': restar,
        'multiplicar': multiplicar,
        'dividir': dividir
    }
    
    # Configuració opcional (exemple)
    config = {
        'titol': 'Calculadora - Solució',
        'autor': 'Professor'
    }
    
    # Crear i iniciar la calculadora
    calculadora = crear_calculadora(funcions, config)
    calculadora.iniciar()
