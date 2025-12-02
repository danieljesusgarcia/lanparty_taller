# 🚦 Taller de Programació - Semàfor Interactiu

## Descripció del Taller

Taller pràctic de programació per a alumnes de 4t ESO / Batxillerat tecnològic. Els alumnes aprenen a programar cridant mètodes visuals per controlar un semàfor interactiu amb interfície gràfica.

## 🎯 Objectius Didàctics

- Entendre el concepte d'objecte i mètode
- Aprendre a cridar mètodes amb paràmetres
- Crear seqüències d'accions temporitzades
- Veure resultats visuals immediats del codi
- Treballar amb comportaments interactius

## 📁 Contingut del Taller

### Fitxers per als Alumnes
- **`semafor_alumnes.py`**: Fitxer on programaran (6 funcions simples)
- **`interficie_semafor.py`**: Interfície gràfica (NO toquen)
- **`GUIA_ALUMNES_SEMAFOR.md`**: Guia pas a pas amb explicacions

### Fitxers per al Professor
- **`semafor_alumnes_solucio.py`**: Codi complet amb solucions
- **`README_SEMAFOR.md`**: Aquest fitxer

## ⏱️ Durada

- **Temps estimat**: 1 hora
- **Distribució**:
  - 10min: Introducció i conceptes bàsics
  - 30min: Tasques 1-4 (crides simples)
  - 15min: Tasques 5-6 (seqüències)
  - 5min: Testing i proves

## 🔧 Requisits Tècnics

### Software Necessari
- Python 3.7 o superior
- Tkinter (inclòs amb Python)

### Verificar Instal·lació
```bash
python3 --version
python3 -m tkinter
```

### Instal·lar Tkinter (si cal)
```bash
sudo apt-get install python3-tk
```

## 📋 Tasques del Taller

### Tasca 1: Activar Llum Verd
- **Dificultat**: ⭐
- **Conceptes**: cridar mètodes, paràmetres strings
- **Codi**: 1 línia
- **Temps**: 5 min

### Tasca 2: Activar Llum Groc
- **Dificultat**: ⭐
- **Conceptes**: repetició de patrons
- **Codi**: 1 línia
- **Temps**: 3 min

### Tasca 3: Activar Llum Vermell
- **Dificultat**: ⭐
- **Conceptes**: repetició de patrons
- **Codi**: 1 línia
- **Temps**: 3 min

### Tasca 4: Apagar Tots
- **Dificultat**: ⭐
- **Conceptes**: mètodes sense paràmetres
- **Codi**: 1 línia
- **Temps**: 3 min

### Tasca 5: Seqüència Normal
- **Dificultat**: ⭐⭐
- **Conceptes**: seqüències, temporització
- **Codi**: 7 línies
- **Temps**: 10 min

### Tasca 6: Mode Nocturn
- **Dificultat**: ⭐⭐
- **Conceptes**: paràmetres múltiples, animacions
- **Codi**: 1 línia
- **Temps**: 5 min

**TOTAL BÀSIC**: 6 funcions (~12 línies de codi efectiu)

---

## 🎮 Tasques Interactives (Opcionals)

Aquestes tasques introdueixen **interacció amb l'usuari** mitjançant diàlegs:

### Tasca I1: Seqüència amb Temps Personalitzat
- **Dificultat**: ⭐⭐⭐
- **Conceptes**: input d'usuari (números), variables, seqüències
- **Mètodes nous**: `demanar_numero()`
- **Codi**: 9 línies
- **Temps**: 10-15 min
- **Aprenen**: Com demanar informació a l'usuari i utilitzar-la

### Tasca I2: Parpelleig Personalitzat
- **Dificultat**: ⭐⭐⭐
- **Conceptes**: input d'usuari (text), validació
- **Mètodes nous**: `triar_color()`
- **Codi**: 3 línies
- **Temps**: 8-10 min
- **Aprenen**: Com validar opcions limitades

### Tasca I3: Missatge Personalitzat
- **Dificultat**: ⭐⭐
- **Conceptes**: input de text, interpolació de strings
- **Mètodes nous**: `demanar_text()`
- **Codi**: 3 línies
- **Temps**: 5-8 min
- **Aprenen**: Treballar amb text de l'usuari

**TOTAL AMB INTERACTIVES**: 9 funcions (~27 línies de codi efectiu)

## 🎓 Metodologia Docent

### Abans del Taller

1. **Preparació tècnica**:
   - Verificar Python i Tkinter en tots els ordinadors
   - Distribuir fitxers: `semafor_alumnes.py`, `interficie_semafor.py`, `GUIA_ALUMNES_SEMAFOR.md`
   - **Opcional**: Configurar sistema per enviar fitxers als alumnes (veure secció "📤 Compartir l'Aplicació")

2. **Introducció teòrica (10 min)**:
   - Què és un objecte? (exemple: comandament a distància)
   - Què és un mètode? (botons del comandament)
   - Mostrar el semàfor funcionant (`semafor_alumnes_solucio.py`)
   - Explicar que només han de cridar mètodes (zero lògica complexa)

### Durant el Taller

**Fase 1 - Crides Simples (Tasques 1-4)** [20 min]:
- Treballar tasca per tasca
- Fer que provin cada botó després de programar-lo
- Èmfasi: "Només has de cridar el mètode correcte"
- Resoldre dubtes col·lectivament

**Fase 2 - Seqüències (Tasques 5-6)** [15 min]:
- Introduir el concepte de "recepta" (pas a pas)
- Mostrar com `esperar()` crea pauses
- Deixar que experimentin amb temps diferents
- Fomentar creativitat

**Fase 3 - Interaccions (Tasques I1-I3)** [20-30 min] - *OPCIONAL*:
- Només per alumnes avançats o si hi ha temps extra
- Introduir el concepte de **diàleg** amb l'usuari
- Mostrar com un programa pot "preguntar" i "escoltar"
- Tasca I3 és la més senzilla (bon punt d'entrada)
- Tasques I1 i I2 requereixen més reflexió sobre variables
- Èmfasi: "El programa ara és **conversacional**"

**Fase 3 - Testing i Celebració** [5 min]:
- Provar tots els botons
- Cada alumne mostra la seva seqüència personalitzada (repte extra)
- Celebrar l'èxit! 🎉

### Després del Taller
- Proposar reptes extra
- Connectar amb DAM: objectes, mètodes → classes, POO

## 🎯 Connexió amb DAM

Aquest taller prepara per a conceptes clau de DAM:

| Concepte del Taller | Equivalent a DAM |
|---------------------|------------------|
| Objecte `semafor` | Instància d'una classe Java |
| Mètodes com `encendre_llum()` | Mètodes públics Java |
| Paràmetres (`"verd"`, `5`) | Arguments de mètodes |
| Seqüències d'accions | Lògica de mètodes |
| Interfície gràfica | JavaFX / Swing |

## 🚀 Reptes Extra

Per a alumnes que acabin abans:

### Repte 1: Seqüència Personalitzada (⭐⭐)
Crear una seqüència única amb parpellejos i pauses

### Repte 2: Mode Emergència (⭐⭐)
Parpelleig ràpid del vermell amb `interval=0.3`

### Repte 3: Test Complet (⭐⭐)
Provar cada llum individualment de forma automàtica

### Repte 4: Seqüència Inversa (⭐⭐)
VERMELL → GROC → VERD

### Repte 5: Show de Llums (⭐⭐⭐)
Combinar tots els mètodes per crear un espectacle visual

## 📊 Avaluació

### Criteris d'Avaluació
- ✅ Les 4 primeres tasques funcionen (crides simples)
- ✅ La seqüència normal funciona correctament
- ✅ El mode nocturn funciona
- ✅ Comprèn el concepte d'objecte i mètode

### Rúbrica (opcional)

**Sense tasques interactives:**
- **Excel·lent (9-10)**: Totes les 6 tasques + almenys 1 repte extra creatiu
- **Notable (7-8)**: Totes les 6 tasques completades i funcionant
- **Bé (6-7)**: Tasques 1-4 correctes + intent de tasca 5
- **Suficient (5-6)**: Almenys tasques 1-4 correctes

**Amb tasques interactives:**
- **Excel·lent (9-10)**: Totes 9 tasques (6 bàsiques + 3 interactives) funcionant
- **Notable (7-8)**: 6 tasques bàsiques + almenys 1 interactiva
- **Bé (6-7)**: Totes 6 tasques bàsiques correctes
- **Suficient (5-6)**: Almenys tasques 1-4 correctes

## 📤 Compartir l'Aplicació amb els Alumnes

Els alumnes poden emportar-se el seu treball a casa. Aquí tens diverses opcions:

### Opció 1: Comprimir els Fitxers (Més Senzill) ✅

**Crear un ZIP per cada alumne:**
```bash
# Crear carpeta amb els fitxers de l'alumne
mkdir semafor_alumne
cp semafor_alumnes.py interficie_semafor.py GUIA_ALUMNES_SEMAFOR.md semafor_alumne/

# Comprimir
zip -r semafor_alumne.zip semafor_alumne/
```

**Els alumnes necessitaran a casa:**
- Python 3.7+ instal·lat
- Tkinter (`sudo apt-get install python3-tk` a Linux)
- Descomprimir i executar: `python3 semafor_alumnes.py`

### Opció 2: Script Launcher (Recomanat)

**Crear un launcher executable:**
```bash
# Crear script
cat > executar_semafor.sh << 'EOF'
#!/bin/bash
cd "$(dirname "$0")"
python3 semafor_alumnes.py
EOF

# Donar permisos
chmod +x executar_semafor.sh
```

Ara poden executar amb doble clic a Linux!

### Opció 3: Enviar per Correu Electrònic 📧

**Preparar el paquet:**
```bash
# Comprimir tots els fitxers necessaris
zip -r semafor_taller.zip semafor_alumnes.py interficie_semafor.py GUIA_ALUMNES_SEMAFOR.md

# Enviar amb client de correu o adjuntar a email
```

**Plantilla d'email per als alumnes:**

```
Assumpte: 🚦 El teu Semàfor Interactiu del Taller

Hola [NOM],

Adjunt trobaràs el codi del semàfor que has programat avui al taller!

📦 Contingut del ZIP:
- semafor_alumnes.py (el teu codi!)
- interficie_semafor.py (la interfície gràfica)
- GUIA_ALUMNES_SEMAFOR.md (guia de referència)

🏠 Per executar-lo a casa:
1. Assegura't que tens Python 3.7+ instal·lat
2. Descomprimeix el fitxer
3. Obre una terminal a la carpeta
4. Executa: python3 semafor_alumnes.py

💡 Idees per continuar:
- Prova els reptes extra de la guia
- Crea noves seqüències personalitzades
- Mostra-ho a família i amics!

Bones pràctiques! 🚀

[PROFESSOR]
```

### Opció 4: Plataforma Educativa (Moodle/Classroom)

**Si tens plataforma educativa:**
1. Pujar el ZIP a la plataforma
2. Els alumnes el descarreguen directament
3. Pots afegir un fòrum per compartir seqüències creatives

### Opció 5: USB o Xarxa Local

**Copiar directament:**
```bash
# Copiar a USB de l'alumne
cp semafor_alumnes.py interficie_semafor.py GUIA_ALUMNES_SEMAFOR.md /media/usb/

# O compartir per xarxa local amb Python
python3 -m http.server 8000
# Els alumnes descarreguen des de: http://[IP_PROFESSOR]:8000
```

### 📝 Instruccions per als Alumnes (README a Casa)

Crea un fitxer `INSTRUCCIONS_CASA.txt`:

```
🚦 COM EXECUTAR EL TEU SEMÀFOR A CASA
====================================

1. INSTAL·LAR PYTHON (si no el tens):
   - Descarrega de: https://www.python.org/downloads/
   - Marca "Add Python to PATH" durant la instal·lació

2. VERIFICAR INSTAL·LACIÓ:
   python3 --version
   
3. EXECUTAR EL PROGRAMA:
   python3 semafor_alumnes.py

4. SI DONA ERROR DE TKINTER (Linux):
   sudo apt-get install python3-tk

5. CONTINUAR PROGRAMANT:
   - Obre semafor_alumnes.py amb qualsevol editor de text
   - Consulta GUIA_ALUMNES_SEMAFOR.md per idees
   - Prova els reptes extra!

Qualsevol dubte: [EMAIL_PROFESSOR]
```

### 🎁 Bonus: Certificat de Participació

Pots crear un certificat personalitzat:

```python
# certificat_generator.py
def crear_certificat(nom_alumne):
    return f"""
    ╔══════════════════════════════════════════╗
    ║     🏆 CERTIFICAT DE PARTICIPACIÓ 🏆    ║
    ╠══════════════════════════════════════════╣
    ║                                          ║
    ║   Certifiquem que {nom_alumne:^20}   ║
    ║   ha completat satisfactòriament el      ║
    ║   TALLER DE PROGRAMACIÓ:                 ║
    ║   🚦 Semàfor Interactiu amb Python       ║
    ║                                          ║
    ║   Data: Desembre 2025                    ║
    ║                                          ║
    ╚══════════════════════════════════════════╝
    """
```

## 🛠️ Resolució de Problemes

### Problema: Tkinter no funciona
**Solució Ubuntu**: 
```bash
sudo apt-get install python3-tk
```

### Problema: El botó no fa res
**Solució**: 
- Verificar que han substituït el `pass`
- Comprovar sintaxi de la crida al mètode

### Problema: Error "name 'semafor' is not defined"
**Solució**: La funció necessita el paràmetre `semafor`

### Problema: No s'encén cap llum
**Solució**: Revisar cometes i ortografia del color

## 📝 Notes per al Professor

- **Simplicitat**: Aquest taller és més simple que la calculadora (només crides de mètodes)
- **Visual**: Els resultats són immediats i molt visuals
- **Motivació**: Els semàfors són familiars i divertits de programar
- **Progressió**: De 1 línia (tasca 1) a 7 línies (tasca 5), fins a 9 línies (interactives)
- **Errors comuns**: Oblidar cometes en els colors, oblidar paràmetre `semafor`
- **Punt fort**: Zero lògica condicional complexa!
- **Tasques interactives**: Opcional, però ideal per introduir el concepte d'**entrada d'usuari**
- **Diàlegs**: Les funcions `demanar_numero()`, `demanar_text()` i `triar_color()` amaguen la complexitat de Tkinter
- **Ordre recomanat per interactives**: I3 (missatge) → I2 (parpelleig) → I1 (temps custom)
- **Temps total estimat**: 
  - Només bàsiques (6 tasques): 45-60 min
  - Amb interactives (9 tasques): 75-90 min
- **Creativitat**: La tasca 5 permet molta experimentació amb temps

## 💡 Consells Didàctics

### Per mantenir l'atenció:
- Mostrar resultats freqüentment
- Fer que cada alumne provi immediatament després de programar
- Celebrar cada èxit petit
- Fomentar que comparteixin seqüències personalitzades

### Per gestionar diferents velocitats:
- Els ràpids: reptes extra i seqüències creatives
- Els lents: ajuda personalitzada en tasques 1-4
- Treball en parelles: els que van ràpid ajuden companys

### Per connectar amb el món real:
- Explicar com funcionen els semàfors reals
- Mostrar aplicacions: semàfors intel·ligents, creuaments
- Connectar amb IoT i domòtica

## 📚 Recursos Addicionals

- [Python Docs oficial](https://docs.python.org/3/)
- [Tkinter Tutorial](https://docs.python.org/3/library/tkinter.html)
- Vídeos sobre programació visual

## 🎯 Objectius Pedagògics Assolits

Després d'aquest taller, els alumnes hauran:

1. ✅ Entès què és un objecte i com cridar els seus mètodes
2. ✅ Après a passar paràmetres a funcions
3. ✅ Creat seqüències d'accions temporitzades
4. ✅ Vist resultats visuals immediats del seu codi
5. ✅ Experimentat amb programació interactiva
6. ✅ Guanyat confiança per programar coses "de veritat"

## 📧 Suport

Per a dubtes o suggerències sobre aquest taller, contacta amb el creador del material.

---

**Versió**: 1.0  
**Data**: Desembre 2025  
**Llicència**: Material educatiu lliure

---

## 🆚 Comparativa amb el Taller de la Calculadora

| Aspecte | Calculadora | Semàfor |
|---------|-------------|---------|
| **Dificultat** | Mitjana | Fàcil |
| **Lògica** | Operadors matemàtics | Crides de mètodes |
| **Visual** | Resultats numèrics | Animacions i colors |
| **Conceptes** | Funcions, return | Objectes, mètodes |
| **Línies codi** | 4-7 | 12 (més línies, més simples) |
| **Motivació** | Útil | Divertit |
| **Recomanat per** | Aprendre funcions | Aprendre objectes |

**Recomanació**: Fer primer el Semàfor (més visual i motivador), després la Calculadora (més conceptual).
