"""
Interfície Gràfica del Semàfor amb Kivy
========================================
Aquest fitxer conté la interfície gràfica del semàfor.
NO HAS DE MODIFICAR AQUEST FITXER!

Només programa a: semafor_alumnes_kivy.py
"""

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.graphics import Color, Ellipse, Rectangle
from kivy.clock import Clock
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
import time


class SemaforKivyGUI(BoxLayout):
    def __init__(self, funcions_alumne, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 20
        self.spacing = 15
        
        self.funcions_alumne = funcions_alumne
        
        # Estats dels llums
        self.llums = {
            'vermell': False,
            'groc': False,
            'verd': False
        }
        
        # Colors
        self.colors = {
            'vermell': (0.9, 0.1, 0.1, 1),
            'groc': (1, 0.9, 0.1, 1),
            'verd': (0.1, 0.8, 0.1, 1),
            'apagat': (0.2, 0.2, 0.2, 1)
        }
        
        # Crear interfície
        self._crear_titol()
        self._crear_semafor()
        self._crear_text_missatge()
        self._crear_botons()
        
    def _crear_titol(self):
        """Crear títol de l'aplicació"""
        titol = Label(
            text='🚦 Semàfor Interactiu - Versió Kivy',
            size_hint=(1, 0.1),
            font_size='24sp',
            bold=True
        )
        self.add_widget(titol)
    
    def _crear_semafor(self):
        """Crear el canvas del semàfor"""
        self.canvas_semafor = BoxLayout(
            size_hint=(1, 0.4),
            orientation='vertical',
            spacing=10,
            padding=20
        )
        
        # Contenidor per centrar el semàfor
        contenidor = BoxLayout(orientation='horizontal')
        contenidor.add_widget(Label())  # Espai esquerra
        
        # Columna del semàfor
        columna_semafor = BoxLayout(
            orientation='vertical',
            size_hint=(0.3, 1),
            spacing=15
        )
        
        # Crear els tres llums
        with columna_semafor.canvas.before:
            # Fons del semàfor
            Color(0.15, 0.15, 0.15, 1)
            self.fons_rect = Rectangle(pos=columna_semafor.pos, size=columna_semafor.size)
        
        columna_semafor.bind(pos=self._actualitzar_fons, size=self._actualitzar_fons)
        
        # Llums (s'afegiran després amb el canvas)
        self.llum_vermell_widget = BoxLayout(size_hint=(1, 0.3))
        self.llum_groc_widget = BoxLayout(size_hint=(1, 0.3))
        self.llum_verd_widget = BoxLayout(size_hint=(1, 0.3))
        
        columna_semafor.add_widget(self.llum_vermell_widget)
        columna_semafor.add_widget(self.llum_groc_widget)
        columna_semafor.add_widget(self.llum_verd_widget)
        
        # Dibuixar cercles inicials
        Clock.schedule_once(lambda dt: self._dibuixar_llums(), 0.1)
        
        contenidor.add_widget(columna_semafor)
        contenidor.add_widget(Label())  # Espai dreta
        
        self.canvas_semafor.add_widget(contenidor)
        self.add_widget(self.canvas_semafor)
    
    def _actualitzar_fons(self, instance, value):
        """Actualitzar posició del fons"""
        self.fons_rect.pos = instance.pos
        self.fons_rect.size = instance.size
    
    def _dibuixar_llums(self):
        """Dibuixar els cercles dels llums"""
        self._dibuixar_llum(self.llum_vermell_widget, 'vermell')
        self._dibuixar_llum(self.llum_groc_widget, 'groc')
        self._dibuixar_llum(self.llum_verd_widget, 'verd')
    
    def _dibuixar_llum(self, widget, color):
        """Dibuixar un cercle de llum"""
        widget.canvas.clear()
        with widget.canvas:
            # Color segons estat
            if self.llums[color]:
                Color(*self.colors[color])
            else:
                Color(*self.colors['apagat'])
            
            # Calcular posició centrada
            x = widget.center_x - 40
            y = widget.center_y - 40
            Ellipse(pos=(x, y), size=(80, 80))
    
    def _crear_text_missatge(self):
        """Crear àrea de missatges"""
        self.label_missatge = Label(
            text='Prem un botó per començar!',
            size_hint=(1, 0.08),
            font_size='16sp'
        )
        self.add_widget(self.label_missatge)
    
    def _crear_botons(self):
        """Crear tots els botons de control"""
        # Botons de llums individuals
        box_llums = BoxLayout(orientation='horizontal', size_hint=(1, 0.08), spacing=10)
        
        btn_verd = Button(
            text='🟢 VERD',
            background_color=(0.2, 0.8, 0.2, 1),
            on_press=lambda x: self._executar_funcio('activar_verd')
        )
        btn_groc = Button(
            text='🟡 GROC',
            background_color=(1, 0.9, 0.2, 1),
            on_press=lambda x: self._executar_funcio('activar_groc')
        )
        btn_vermell = Button(
            text='🔴 VERMELL',
            background_color=(0.9, 0.2, 0.2, 1),
            on_press=lambda x: self._executar_funcio('activar_vermell')
        )
        
        box_llums.add_widget(btn_verd)
        box_llums.add_widget(btn_groc)
        box_llums.add_widget(btn_vermell)
        self.add_widget(box_llums)
        
        # Botó apagar
        btn_apagar = Button(
            text='⚫ Apagar Tots',
            size_hint=(1, 0.08),
            background_color=(0.3, 0.3, 0.3, 1),
            on_press=lambda x: self._executar_funcio('apagar_tots')
        )
        self.add_widget(btn_apagar)
        
        # Botons de seqüències
        box_seq = BoxLayout(orientation='horizontal', size_hint=(1, 0.08), spacing=10)
        
        btn_normal = Button(
            text='🔄 Seqüència Normal',
            background_color=(0.2, 0.4, 0.8, 1),
            on_press=lambda x: self._executar_funcio('sequencia_normal')
        )
        btn_nocturn = Button(
            text='🌙 Mode Nocturn',
            background_color=(0.4, 0.2, 0.6, 1),
            on_press=lambda x: self._executar_funcio('mode_nocturn')
        )
        
        box_seq.add_widget(btn_normal)
        box_seq.add_widget(btn_nocturn)
        self.add_widget(box_seq)
        
        # Botons interactius
        box_inter = BoxLayout(orientation='horizontal', size_hint=(1, 0.08), spacing=10)
        
        btn_temps = Button(
            text='⏱️ Temps Custom',
            background_color=(0.6, 0.3, 0.8, 1),
            on_press=lambda x: self._executar_funcio('sequencia_amb_temps_personalitzat')
        )
        btn_parpelleig = Button(
            text='✨ Parpelleig Custom',
            background_color=(0.6, 0.3, 0.8, 1),
            on_press=lambda x: self._executar_funcio('parpelleig_personalitzat')
        )
        btn_missatge = Button(
            text='💬 Missatge',
            background_color=(0.6, 0.3, 0.8, 1),
            on_press=lambda x: self._executar_funcio('missatge_personalitzat')
        )
        
        box_inter.add_widget(btn_temps)
        box_inter.add_widget(btn_parpelleig)
        box_inter.add_widget(btn_missatge)
        self.add_widget(box_inter)
    
    def _executar_funcio(self, nom_funcio):
        """Executar una funció de l'alumne en un thread separat"""
        if nom_funcio in self.funcions_alumne:
            try:
                self.mostrar_text(f"Executant: {nom_funcio}...")
                # Executar en thread per no bloquejar la UI
                import threading
                
                semafor_ref = self
                funcio = self.funcions_alumne[nom_funcio]
                
                def executar():
                    error_msg = None
                    try:
                        funcio(semafor_ref)
                    except Exception as e:
                        error_msg = str(e)
                    
                    if error_msg:
                        Clock.schedule_once(lambda dt: semafor_ref.mostrar_text(f"❌ Error: {error_msg}"), 0)
                    else:
                        Clock.schedule_once(lambda dt: semafor_ref.mostrar_text(f"✓ {nom_funcio} completat!"), 0)
                
                thread = threading.Thread(target=executar)
                thread.daemon = True
                thread.start()
            except Exception as e:
                self.mostrar_text(f"❌ Error: {str(e)}")
        else:
            self.mostrar_text(f"⚠️ Funció '{nom_funcio}' no implementada")
    
    # ============================================
    # MÈTODES PER ALS ALUMNES
    # ============================================
    
    def encendre_llum(self, color):
        """
        Encén un llum del semàfor
        
        Args:
            color: "verd", "groc" o "vermell"
        """
        if color not in ['verd', 'groc', 'vermell']:
            Clock.schedule_once(lambda dt: self.mostrar_text(f"❌ Color '{color}' no vàlid. Usa: verd, groc o vermell"), 0)
            return
        
        def _encendre(dt):
            # Apagar tots primer
            self.llums = {k: False for k in self.llums}
            # Encendre el seleccionat
            self.llums[color] = True
            self._dibuixar_llums()
        
        Clock.schedule_once(_encendre, 0)
    
    def apagar_tots(self):
        """Apaga tots els llums"""
        def _apagar(dt):
            self.llums = {k: False for k in self.llums}
            self._dibuixar_llums()
        
        Clock.schedule_once(_apagar, 0)
    
    def parpallejar(self, color, vegades=3, interval=0.5):
        """
        Fa parpallejar un llum
        
        Args:
            color: "verd", "groc" o "vermell"
            vegades: quantes vegades parpellejar
            interval: segons entre cada parpelleig
        """
        def _parpelleig(dt):
            nonlocal comptador, encendre
            
            if comptador < vegades * 2:
                if encendre:
                    self.encendre_llum(color)
                else:
                    self.apagar_tots()
                encendre = not encendre
                comptador += 1
                Clock.schedule_once(_parpelleig, interval)
            else:
                self.apagar_tots()
        
        comptador = 0
        encendre = True
        _parpelleig(0)
    
    def esperar(self, segons):
        """
        Espera un temps determinat
        
        Args:
            segons: segons a esperar
        """
        time.sleep(segons)
    
    def mostrar_text(self, missatge):
        """
        Mostra un missatge a la pantalla
        
        Args:
            missatge: text a mostrar
        """
        def _mostrar(dt):
            self.label_missatge.text = missatge
        
        Clock.schedule_once(_mostrar, 0)
    
    def demanar_numero(self, pregunta, default=1, minim=1, maxim=10):
        """
        Demana un número a l'usuari
        
        Args:
            pregunta: pregunta a mostrar
            default: valor per defecte
            minim: valor mínim acceptat
            maxim: valor màxim acceptat
            
        Returns:
            int: número introduït per l'usuari
        """
        return self._mostrar_dialog_input(pregunta, str(default), 'numero', minim, maxim)
    
    def demanar_text(self, pregunta, default=""):
        """
        Demana text a l'usuari
        
        Args:
            pregunta: pregunta a mostrar
            default: text per defecte
            
        Returns:
            str: text introduït per l'usuari
        """
        return self._mostrar_dialog_input(pregunta, default, 'text')
    
    def triar_color(self):
        """
        Permet triar un color del semàfor
        
        Returns:
            str: "verd", "groc" o "vermell"
        """
        colors = ['verd', 'groc', 'vermell']
        return self._mostrar_dialog_opcions("Tria un color:", colors)
    
    def _mostrar_dialog_input(self, pregunta, default, tipus='text', minim=None, maxim=None):
        """Mostra un diàleg d'input"""
        import threading
        result = [default]
        event = threading.Event()
        
        def mostrar_popup(dt):
            content = BoxLayout(orientation='vertical', padding=10, spacing=10)
            content.add_widget(Label(text=pregunta))
            
            text_input = TextInput(
                text=str(default),
                multiline=False,
                size_hint=(1, 0.3)
            )
            content.add_widget(text_input)
            
            btn_box = BoxLayout(size_hint=(1, 0.3), spacing=10)
            
            popup = Popup(
                title='Input',
                content=content,
                size_hint=(0.8, 0.4),
                auto_dismiss=False
            )
            
            def on_ok(instance):
                valor = text_input.text
                if tipus == 'numero':
                    try:
                        num = int(valor)
                        if minim is not None and num < minim:
                            num = minim
                        if maxim is not None and num > maxim:
                            num = maxim
                        result[0] = num
                    except ValueError:
                        result[0] = default
                else:
                    result[0] = valor
                popup.dismiss()
                event.set()
            
            def on_cancel(instance):
                popup.dismiss()
                event.set()
            
            btn_ok = Button(text='OK', on_press=on_ok)
            btn_cancel = Button(text='Cancel·lar', on_press=on_cancel)
            
            btn_box.add_widget(btn_ok)
            btn_box.add_widget(btn_cancel)
            content.add_widget(btn_box)
            
            popup.open()
        
        Clock.schedule_once(mostrar_popup, 0)
        event.wait()  # Esperar fins que es tanqui el popup
        
        return result[0]
    
    def _mostrar_dialog_opcions(self, pregunta, opcions):
        """Mostra un diàleg amb opcions"""
        import threading
        result = [opcions[0]]
        event = threading.Event()
        
        def mostrar_popup(dt):
            content = BoxLayout(orientation='vertical', padding=10, spacing=10)
            content.add_widget(Label(text=pregunta, size_hint=(1, 0.3)))
            
            popup = Popup(
                title='Tria una opció',
                content=content,
                size_hint=(0.8, 0.5),
                auto_dismiss=False
            )
            
            def crear_callback(opcio):
                def callback(instance):
                    result[0] = opcio
                    popup.dismiss()
                    event.set()
                return callback
            
            for opcio in opcions:
                btn = Button(
                    text=opcio.upper(),
                    size_hint=(1, None),
                    height=50,
                    on_press=crear_callback(opcio)
                )
                content.add_widget(btn)
            
            popup.open()
        
        Clock.schedule_once(mostrar_popup, 0)
        event.wait()  # Esperar fins que es tanqui el popup
        
        return result[0]
        popup.open()
        
        # Esperar fins que es tanqui el popup
        while popup._window is not None:
            time.sleep(0.1)
        
        return result[0]


class SemaforApp(App):
    def __init__(self, funcions_alumne, **kwargs):
        super().__init__(**kwargs)
        self.funcions_alumne = funcions_alumne
    
    def build(self):
        self.title = '🚦 Semàfor Interactiu - Kivy'
        return SemaforKivyGUI(self.funcions_alumne)


def crear_semafor_kivy(funcions_alumne):
    """
    Crea i executa l'aplicació del semàfor
    
    Args:
        funcions_alumne: diccionari amb les funcions implementades
    """
    app = SemaforApp(funcions_alumne)
    app.run()
