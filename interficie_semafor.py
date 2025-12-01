"""
INTERFÍCIE GRÀFICA DEL SEMÀFOR
================================
Aquest fitxer conté tot el codi de la interfície gràfica del semàfor.
NO CAL MODIFICAR RES D'AQUEST FITXER!

La teva feina està a semafor_alumnes.py
"""

import tkinter as tk
from tkinter import Canvas
import time


class SemaforGUI:
    """Classe que gestiona la interfície gràfica del semàfor."""
    
    def __init__(self, funcions_control):
        """
        Inicialitza la interfície gràfica del semàfor.
        
        Args:
            funcions_control: Diccionari amb les funcions de control
                            {'activar_verd': funció, 'activar_groc': funció, ...}
        """
        self.funcions = funcions_control
        
        # Estats dels llums
        self.estat_llums = {
            'verd': False,
            'groc': False,
            'vermell': False
        }
        
        # Crear la finestra
        self.finestra = tk.Tk()
        self.finestra.title("🚦 Semàfor Interactiu")
        self.finestra.geometry("400x650")
        self.finestra.resizable(False, False)
        self.finestra.configure(bg='#2C3E50')
        
        # Crear el canvas per al semàfor
        self._crear_canvas()
        
        # Dibuixar el semàfor
        self._dibuixar_semafor()
        
        # Crear els botons de control
        self._crear_botons()
        
        # Crear etiqueta informativa
        self._crear_etiqueta()
    
    def _crear_canvas(self):
        """Crea el canvas on es dibuixarà el semàfor."""
        self.canvas = Canvas(
            self.finestra,
            width=350,
            height=400,
            bg='#34495E',
            highlightthickness=0
        )
        self.canvas.pack(pady=20, padx=25)
    
    def _dibuixar_semafor(self):
        """Dibuixa l'estructura del semàfor."""
        # Rectangle exterior (caixa del semàfor)
        self.canvas.create_rectangle(
            100, 50, 250, 350,
            fill='#2C3E50',
            outline='#1A252F',
            width=5
        )
        
        # Llum VERMELL (superior)
        self.llum_vermell = self.canvas.create_oval(
            125, 75, 225, 175,
            fill='#4A4A4A',
            outline='#2C3E50',
            width=3
        )
        
        # Llum GROC (mig)
        self.llum_groc = self.canvas.create_oval(
            125, 175, 225, 275,
            fill='#4A4A4A',
            outline='#2C3E50',
            width=3
        )
        
        # Llum VERD (inferior)
        self.llum_verd = self.canvas.create_oval(
            125, 275, 225, 375,
            fill='#4A4A4A',
            outline='#2C3E50',
            width=3
        )
        
        # Pal del semàfor
        self.canvas.create_rectangle(
            165, 350, 185, 400,
            fill='#2C3E50',
            outline='#1A252F',
            width=2
        )
    
    def _crear_botons(self):
        """Crea els botons de control."""
        # Frame per als botons
        frame_botons = tk.Frame(self.finestra, bg='#2C3E50')
        frame_botons.pack(pady=10)
        
        # Colors dels botons
        COLOR_VERMELL = '#E74C3C'
        COLOR_GROC = '#F39C12'
        COLOR_VERD = '#27AE60'
        COLOR_ESPECIAL = '#3498DB'
        COLOR_RESET = '#95A5A6'
        
        # Botons principals
        botons = [
            ("🔴 Vermell", COLOR_VERMELL, lambda: self._executar_funcio('activar_vermell')),
            ("🟡 Groc", COLOR_GROC, lambda: self._executar_funcio('activar_groc')),
            ("🟢 Verd", COLOR_VERD, lambda: self._executar_funcio('activar_verd')),
        ]
        
        for text, color, comando in botons:
            boto = tk.Button(
                frame_botons,
                text=text,
                font=('Arial', 12, 'bold'),
                bg=color,
                fg='white',
                activebackground=color,
                activeforeground='white',
                command=comando,
                width=12,
                height=2,
                cursor='hand2',
                relief='raised',
                bd=3
            )
            boto.pack(side='left', padx=5)
        
        # Frame per a botons secundaris
        frame_secundari = tk.Frame(self.finestra, bg='#2C3E50')
        frame_secundari.pack(pady=5)
        
        botons_secundaris = [
            ("⚫ Apagar", COLOR_RESET, lambda: self._executar_funcio('apagar_tots')),
            ("🔄 Seqüència", COLOR_ESPECIAL, lambda: self._executar_funcio('sequencia_normal')),
            ("🌙 Nocturn", COLOR_ESPECIAL, lambda: self._executar_funcio('mode_nocturn')),
        ]
        
        for text, color, comando in botons_secundaris:
            boto = tk.Button(
                frame_secundari,
                text=text,
                font=('Arial', 11, 'bold'),
                bg=color,
                fg='white',
                activebackground=color,
                activeforeground='white',
                command=comando,
                width=12,
                height=1,
                cursor='hand2',
                relief='raised',
                bd=3
            )
            boto.pack(side='left', padx=5)
    
    def _crear_etiqueta(self):
        """Crea l'etiqueta informativa."""
        self.etiqueta = tk.Label(
            self.finestra,
            text="Clica els botons per controlar el semàfor",
            font=('Arial', 11),
            bg='#2C3E50',
            fg='#ECF0F1',
            pady=10
        )
        self.etiqueta.pack()
    
    def _executar_funcio(self, nom_funcio):
        """Executa una funció dels alumnes i gestiona errors."""
        try:
            if nom_funcio in self.funcions:
                self.funcions[nom_funcio](self)
            else:
                self.mostrar_text(f"Funció '{nom_funcio}' no trobada!")
        except Exception as e:
            self.mostrar_text(f"Error: {str(e)}")
    
    # =========================================================================
    # MÈTODES QUE ELS ALUMNES PODEN CRIDAR
    # =========================================================================
    
    def encendre_llum(self, color):
        """
        Encén un llum del semàfor (apaga els altres).
        
        Args:
            color: "verd", "groc" o "vermell"
        """
        # Primer apaguem tots
        self.canvas.itemconfig(self.llum_verd, fill='#4A4A4A')
        self.canvas.itemconfig(self.llum_groc, fill='#4A4A4A')
        self.canvas.itemconfig(self.llum_vermell, fill='#4A4A4A')
        
        # Actualitzem estats
        self.estat_llums['verd'] = False
        self.estat_llums['groc'] = False
        self.estat_llums['vermell'] = False
        
        # Encendre el llum seleccionat
        if color == 'verd':
            self.canvas.itemconfig(self.llum_verd, fill='#2ECC71')
            self.estat_llums['verd'] = True
            self.mostrar_text("🟢 VERD: Pot passar!")
        elif color == 'groc':
            self.canvas.itemconfig(self.llum_groc, fill='#F1C40F')
            self.estat_llums['groc'] = True
            self.mostrar_text("🟡 GROC: Atenció!")
        elif color == 'vermell':
            self.canvas.itemconfig(self.llum_vermell, fill='#E74C3C')
            self.estat_llums['vermell'] = True
            self.mostrar_text("🔴 VERMELL: Atura't!")
        
        self.finestra.update()
    
    def apagar_tots(self):
        """Apaga tots els llums del semàfor."""
        self.canvas.itemconfig(self.llum_verd, fill='#4A4A4A')
        self.canvas.itemconfig(self.llum_groc, fill='#4A4A4A')
        self.canvas.itemconfig(self.llum_vermell, fill='#4A4A4A')
        
        self.estat_llums['verd'] = False
        self.estat_llums['groc'] = False
        self.estat_llums['vermell'] = False
        
        self.mostrar_text("⚫ Tots els llums apagats")
        self.finestra.update()
    
    def parpallejar(self, color, vegades=3, interval=0.5):
        """
        Fa parpallejar un llum.
        
        Args:
            color: "verd", "groc" o "vermell"
            vegades: Nombre de vegades que parpellejarà
            interval: Temps entre encendre i apagar (en segons)
        """
        for _ in range(vegades):
            self.encendre_llum(color)
            self.esperar(interval)
            self.apagar_tots()
            self.esperar(interval)
        
        self.mostrar_text(f"✨ Parpelleig {color} completat!")
    
    def esperar(self, segons):
        """
        Fa una pausa (espera).
        
        Args:
            segons: Temps a esperar en segons
        """
        self.finestra.update()
        time.sleep(segons)
    
    def mostrar_text(self, missatge):
        """
        Mostra un missatge a l'etiqueta informativa.
        
        Args:
            missatge: Text a mostrar
        """
        self.etiqueta.config(text=missatge)
        self.finestra.update()
    
    def encendre_dos_llums(self, color1, color2):
        """
        Encén dos llums alhora (mode especial).
        
        Args:
            color1: Primer color
            color2: Segon color
        """
        colors_map = {
            'verd': (self.llum_verd, '#2ECC71'),
            'groc': (self.llum_groc, '#F1C40F'),
            'vermell': (self.llum_vermell, '#E74C3C')
        }
        
        # Primer apaguem tots
        self.apagar_tots()
        
        # Encendre els dos llums
        if color1 in colors_map:
            llum, color_hex = colors_map[color1]
            self.canvas.itemconfig(llum, fill=color_hex)
            self.estat_llums[color1] = True
        
        if color2 in colors_map:
            llum, color_hex = colors_map[color2]
            self.canvas.itemconfig(llum, fill=color_hex)
            self.estat_llums[color2] = True
        
        self.mostrar_text(f"💡 Llums {color1} i {color2} encesos!")
        self.finestra.update()
    
    def iniciar(self):
        """Inicia el semàfor (mostra la finestra)."""
        print("\n" + "="*60)
        print("✓ Semàfor iniciat correctament!")
        print("="*60 + "\n")
        self.finestra.mainloop()


def crear_semafor(funcions_control):
    """
    Crea i retorna un semàfor amb les funcions de control proporcionades.
    
    Args:
        funcions_control: Diccionari amb les funcions de control
    
    Returns:
        SemaforGUI: El semàfor creat
    """
    return SemaforGUI(funcions_control)
