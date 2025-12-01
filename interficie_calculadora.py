"""
INTERFÍCIE GRÀFICA DE LA CALCULADORA
======================================
Aquest fitxer conté tot el codi de la interfície gràfica.
NO CAL MODIFICAR RES D'AQUEST FITXER!

La teva feina està a calculadora_alumnes.py
"""

import tkinter as tk
from tkinter import messagebox


class CalculadoraGUI:
    """Classe que gestiona la interfície gràfica de la calculadora."""
    
    def __init__(self, funcions_calcul, config=None):
        """
        Inicialitza la interfície gràfica.
        
        Args:
            funcions_calcul: Diccionari amb les funcions de càlcul
                            {'sumar': funció, 'restar': funció, ...}
            config: Diccionari amb la configuració personalitzada (opcional)
        """
        self.funcions = funcions_calcul
        self.numero_guardat = None
        self.operacio_actual = None
        
        # Configuració per defecte
        self.config = {
            'titol': 'La Meva Calculadora',
            'mida': '450x550',
            'color_fons': '#2C3E50',
            'color_numeros': '#3498DB',
            'color_operacions': '#E67E22',
            'color_especial': '#E74C3C',
            'color_igual': '#27AE60',
            'mida_font_pantalla': 20,
            'mida_font_botons': 18,
            'autor': 'Python + Tkinter'
        }
        
        # Aplicar configuració personalitzada si existeix
        if config:
            self.config.update(config)
        
        # Crear la finestra
        self.finestra = tk.Tk()
        self.finestra.title(self.config['titol'])
        self.finestra.geometry(self.config['mida'])
        self.finestra.resizable(False, False)
        self.finestra.configure(bg=self.config['color_fons'])
        
        # Crear la pantalla
        self._crear_pantalla()
        
        # Crear els botons
        self._crear_botons()
        
        # Configurar el grid
        self._configurar_grid()
        
        # Informació al peu
        self._crear_peu()
    
    def _crear_pantalla(self):
        """Crea la pantalla on es mostren els números."""
        self.pantalla = tk.Entry(
            self.finestra,
            font=('Arial', self.config['mida_font_pantalla'], 'bold'),
            justify='right',
            bd=10,
            bg='#ECF0F1',
            fg='#2C3E50',
            width=15
        )
        self.pantalla.grid(row=0, column=0, columnspan=4, padx=15, pady=20, sticky='ew')
    
    def _crear_botons(self):
        """Crea tots els botons de la calculadora."""
        # Colors dels botons (personalitzables)
        COLOR_NUMERO = self.config['color_numeros']
        COLOR_OPERACIO = self.config['color_operacions']
        COLOR_ESPECIAL = self.config['color_especial']
        COLOR_IGUAL = self.config['color_igual']
        
        # Definició dels botons (fila, columna, text, color, amplada, acció)
        botons = [
            # Fila 1: Funcions especials
            (1, 0, 'C', COLOR_ESPECIAL, 2, self.esborrar),
            (1, 2, '/', COLOR_OPERACIO, 1, lambda: self.seleccionar_operacio('/')),
            (1, 3, '*', COLOR_OPERACIO, 1, lambda: self.seleccionar_operacio('*')),
            
            # Fila 2: Números 7-9
            (2, 0, '7', COLOR_NUMERO, 1, lambda: self.afegir_numero(7)),
            (2, 1, '8', COLOR_NUMERO, 1, lambda: self.afegir_numero(8)),
            (2, 2, '9', COLOR_NUMERO, 1, lambda: self.afegir_numero(9)),
            (2, 3, '-', COLOR_OPERACIO, 1, lambda: self.seleccionar_operacio('-')),
            
            # Fila 3: Números 4-6
            (3, 0, '4', COLOR_NUMERO, 1, lambda: self.afegir_numero(4)),
            (3, 1, '5', COLOR_NUMERO, 1, lambda: self.afegir_numero(5)),
            (3, 2, '6', COLOR_NUMERO, 1, lambda: self.afegir_numero(6)),
            (3, 3, '+', COLOR_OPERACIO, 1, lambda: self.seleccionar_operacio('+')),
            
            # Fila 4: Números 1-3
            (4, 0, '1', COLOR_NUMERO, 1, lambda: self.afegir_numero(1)),
            (4, 1, '2', COLOR_NUMERO, 1, lambda: self.afegir_numero(2)),
            (4, 2, '3', COLOR_NUMERO, 1, lambda: self.afegir_numero(3)),
            (4, 3, '=', COLOR_IGUAL, 1, self.calcular),
            
            # Fila 5: 0 i punt decimal
            (5, 0, '0', COLOR_NUMERO, 2, lambda: self.afegir_numero(0)),
            (5, 2, '.', COLOR_NUMERO, 1, lambda: self.afegir_numero('.')),
        ]
        
        # Crear tots els botons
        for fila, columna, text, color, amplada, comando in botons:
            boto = tk.Button(
                self.finestra,
                text=text,
                font=('Arial', self.config['mida_font_botons'], 'bold'),
                bg=color,
                fg='white',
                activebackground=color,
                activeforeground='white',
                bd=5,
                command=comando,
                cursor='hand2'
            )
            boto.grid(
                row=fila,
                column=columna,
                columnspan=amplada,
                padx=5,
                pady=5,
                sticky='nsew',
                ipadx=10,
                ipady=20
            )
    
    def _configurar_grid(self):
        """Configura que les columnes i files s'expandeixin."""
        for i in range(4):
            self.finestra.grid_columnconfigure(i, weight=1)
        for i in range(6):
            self.finestra.grid_rowconfigure(i, weight=1)
    
    def _crear_peu(self):
        """Crea la informació al peu de la finestra."""
        info_label = tk.Label(
            self.finestra,
            text=f"Taller de Programació | {self.config['autor']}",
            font=('Arial', 10),
            bg=self.config['color_fons'],
            fg='#95A5A6'
        )
        info_label.grid(row=6, column=0, columnspan=4, pady=10)
    
    # =========================================================================
    # MÈTODES D'INTERACCIÓ (utilitzen les funcions dels alumnes)
    # =========================================================================
    
    def afegir_numero(self, numero):
        """Afegeix un número o punt decimal a la pantalla."""
        actual = self.pantalla.get()
        self.pantalla.delete(0, tk.END)
        self.pantalla.insert(0, actual + str(numero))
    
    def esborrar(self):
        """Esborra tot el contingut de la pantalla."""
        self.pantalla.delete(0, tk.END)
        self.numero_guardat = None
        self.operacio_actual = None
    
    def seleccionar_operacio(self, operacio):
        """Guarda el primer número i l'operació seleccionada."""
        try:
            self.numero_guardat = float(self.pantalla.get())
            self.operacio_actual = operacio
            self.pantalla.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Error", "Introdueix un número vàlid primer!")
    
    def calcular(self):
        """Realitza el càlcul utilitzant les funcions dels alumnes."""
        try:
            # Obtenim el segon número
            num2 = float(self.pantalla.get())
            
            # Comprovem que hi ha una operació seleccionada
            if self.operacio_actual is None:
                messagebox.showwarning("Avís", "Selecciona una operació primer!")
                return
            
            # Cridem la funció corresponent
            resultat = None
            operacio_nom = ""
            resultat_esperat = None
            
            if self.operacio_actual == '+':
                resultat = self.funcions['sumar'](self.numero_guardat, num2)
                operacio_nom = "sumar"
                resultat_esperat = self.numero_guardat + num2
                
            elif self.operacio_actual == '-':
                resultat = self.funcions['restar'](self.numero_guardat, num2)
                operacio_nom = "restar"
                resultat_esperat = self.numero_guardat - num2
                
            elif self.operacio_actual == '*':
                resultat = self.funcions['multiplicar'](self.numero_guardat, num2)
                operacio_nom = "multiplicar"
                resultat_esperat = self.numero_guardat * num2
                
            elif self.operacio_actual == '/':
                # Comprovem divisió per zero
                if num2 == 0:
                    messagebox.showerror("Error", "No es pot dividir entre zero!")
                    self.esborrar()
                    return
                resultat = self.funcions['dividir'](self.numero_guardat, num2)
                operacio_nom = "dividir"
                resultat_esperat = self.numero_guardat / num2
            
            # Comprovem que la funció ha retornat alguna cosa
            if resultat is None:
                messagebox.showerror("Error", 
                    f"La funció '{operacio_nom}' no ha retornat cap resultat!\n\n"
                    "❌ Problema: Has oblidat posar 'return'\n\n"
                    f"💡 Solució: A la funció {operacio_nom}(), afegeix:\n"
                    f"   return num1 {self.operacio_actual} num2")
                self.esborrar()
                return
            
            # Comprovem que el resultat és correcte (amb tolerància per decimals)
            try:
                if abs(float(resultat) - float(resultat_esperat)) > 0.0001:
                    messagebox.showwarning("Resultat Incorrecte", 
                        f"⚠️ La funció '{operacio_nom}' no retorna el resultat correcte!\n\n"
                        f"Operació: {self.numero_guardat} {self.operacio_actual} {num2}\n"
                        f"El teu resultat: {resultat}\n"
                        f"Resultat esperat: {resultat_esperat}\n\n"
                        f"💡 Revisa la funció {operacio_nom}() i comprova que:\n"
                        f"   - Utilitzes l'operador correcte ({self.operacio_actual})\n"
                        f"   - Fas return del càlcul correcte")
                    self.esborrar()
                    return
            except (ValueError, TypeError):
                # Si no es pot convertir a número, deixar que el TypeError del final ho gestioni
                pass
            
            # Mostrem el resultat
            self.pantalla.delete(0, tk.END)
            self.pantalla.insert(0, str(resultat))
            
            # Reiniciem
            self.numero_guardat = None
            self.operacio_actual = None
            
        except ValueError:
            messagebox.showerror("Error", "Introdueix un número vàlid!")
        except TypeError as e:
            messagebox.showerror("Error", 
                f"Hi ha un problema amb les teves funcions:\n{str(e)}\n\n"
                "Assegura't que retornen un número!")
        except Exception as e:
            messagebox.showerror("Error", f"S'ha produït un error: {str(e)}")
    
    def iniciar(self):
        """Inicia la calculadora (mostra la finestra)."""
        print("\n" + "="*60)
        print("✓ Calculadora iniciada correctament!")
        print("="*60 + "\n")
        self.finestra.mainloop()


def crear_calculadora(funcions_calcul, config=None):
    """
    Crea i retorna una calculadora amb les funcions proporcionades.
    
    Args:
        funcions_calcul: Diccionari amb les funcions {'sumar': f, 'restar': f, ...}
        config: Diccionari opcional amb la configuració personalitzada
    
    Returns:
        CalculadoraGUI: La calculadora creada
    """
    return CalculadoraGUI(funcions_calcul, config)
