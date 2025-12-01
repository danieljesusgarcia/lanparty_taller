"""
EXEMPLE DE CALCULADORA PERSONALITZADA
======================================
Aquest fitxer mostra com personalitzar completament la calculadora.
"""

from interficie_calculadora import crear_calculadora


# =============================================================================
# FUNCIONS MATEMÀTIQUES
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
    
    # Configuració personalitzada (tema fosc/modern)
    config = {
        'titol': '🔢 Calculadora Pro',
        'mida': '480x580',
        'color_fons': '#1a1a2e',
        'color_numeros': '#0f3460',
        'color_operacions': '#e94560',
        'color_especial': '#533483',
        'color_igual': '#16213e',
        'mida_font_pantalla': 22,
        'mida_font_botons': 20,
        'autor': 'Tema Fosc per l\'alumne X'
    }
    
    # Crear i iniciar la calculadora
    calculadora = crear_calculadora(funcions, config)
    calculadora.iniciar()
