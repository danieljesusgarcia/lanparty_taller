# 🎓 Taller de Programació - Calculadora amb Python

## Descripció del Taller

Taller pràctic de programació per a alumnes de 4t ESO / Batxillerat tecnològic sense coneixements previs de programació. Els alumnes aprendran conceptes bàsics de programació creant una calculadora funcional amb interfície gràfica.

## 🎯 Objectius Didàctics

- Entendre el concepte de funció
- Aprendre operadors matemàtics bàsics
- Treballar amb paràmetres i valors de retorn
- Introduir la gestió d'errors
- Crear una aplicació amb interfície gràfica
- Experimentar amb codi "real" professional

## 📁 Contingut del Taller

### Fitxers per als Alumnes
- **`calculadora_alumnes.py`**: Fitxer on programaran (4 funcions + configuració opcional)
- **`interficie_calculadora.py`**: Interfície gràfica (NO toquen)
- **`GUIA_ALUMNES.md`**: Guia pas a pas amb explicacions i solucions

### Fitxers per al Professor
- **`calculadora_alumnes_solucio.py`**: Codi complet amb totes les tasques resoltes
- **`calculadora_exemple_personalitzat.py`**: Exemple amb personalització completa (tema fosc)
- **`README.md`**: Aquest fitxer

## ⏱️ Durada

- **Temps estimat**: 1h - 1h 30min
- **Distribució**:
  - 15min: Introducció i configuració
  - 40min: Desenvolupament guiat (tasques 1-4)
  - 15min: Testing i proves
  - 20min: Reptes extra (opcionals)

**NOTA**: Amb la nova estructura (interfície separada), el taller és més curt i centrat.

## 🔧 Requisits Tècnics

### Software Necessari
- Python 3.7 o superior
- Editor de codi (recomanat: VS Code, PyCharm Community)
- Tkinter (ve inclòs amb Python)

### Verificar Instal·lació
```bash
python3 --version
python3 -m tkinter
## 📋 Tasques del Taller

### Tasca 1: Funció Sumar
- **Dificultat**: ⭐
- **Conceptes**: funcions, return, operador +
- **Temps**: 5-10 min

### Tasca 2: Funció Restar
- **Dificultat**: ⭐
- **Conceptes**: operador -
- **Temps**: 5 min

### Tasca 3: Funció Multiplicar
- **Dificultat**: ⭐
- **Conceptes**: operador *
- **Temps**: 5 min

### Tasca 4: Funció Dividir
- **Dificultat**: ⭐⭐
- **Conceptes**: operador /, divisió per zero (gestionat automàticament)
- **Temps**: 5-10 min

### Tasca 5: Executar l'Aplicació
- **Dificultat**: ⭐
- **Conceptes**: imports, execució
- **Temps**: 2 min

### Tasca Extra (Opcional): Personalitzar la Calculadora
- **Dificultat**: ⭐⭐
- **Conceptes**: diccionaris, configuració, colors hexadecimals
- **Temps**: 10-15 min
- **Què fan**: Canviar colors, mides, títol de la calculadora

**TOTAL**: 4 funcions a programar (4 línies de codi!) + executar + personalització opcional⭐
- **Conceptes**: comentaris, execució
- **Temps**: 5 min

## 🎓 Metodologia Docent

### Abans del Taller
1. Assegurar que tots els ordinadors tenen Python instal·lat
2. Distribuir els fitxers `calculadora_base.py` i `GUIA_ALUMNES.md`
3. Fer una breu introducció teòrica (10-15 min):
   - Què és Python i per què és útil
   - Concepte de funció amb exemples senzills
   - Mostrar la calculadora acabada

### Abans del Taller
1. Assegurar que tots els ordinadors tenen Python i Tkinter instal·lats:
   ```bash
   sudo apt-get install python3-tk
   ```
2. Distribuir els fitxers:
   - `calculadora_alumnes.py`
   - `interficie_calculadora.py`
   - `GUIA_ALUMNES.md`
3. Fer una breu introducció teòrica (10-15 min):
   - Què és Python i per què és útil
   - Concepte de funció amb exemples senzills
   - Mostrar la calculadora acabada (`calculadora_alumnes_solucio.py`)
   - Explicar que només han de programar 4 funcions!

### Durant el Taller
1. **Fase 1 - Funcions matemàtiques** (Tasques 1-4):
   - Treballar tasca per tasca
   - Opcional: Fer que provïn cada funció amb `provar_funcions()`
   - Resoldre dubtes col·lectivament
   - **Important**: Recordar que han de posar `return`!

2. **Fase 2 - Execució** (Tasca 5):
   - Executar la calculadora
   - Explicar breument com funciona l'import de funcions
   - Mostrar que les seves funcions "alimenten" la interfície

3. **Fase 3 - Testing i celebració**:
   - Provar totes les operacions
   - Provar divisió per zero (veure que està gestionat)
   - Celebrar l'èxit! 🎉
Aquest taller prepara per a conceptes clau de DAM:

| Concepte del Taller | Equivalent a DAM |
|---------------------|------------------|
| Funcions Python | Mètodes Java |
| Imports | Imports de classes Java |
| Diccionaris | Maps/HashMaps |
| Separació lògica/interfície | Patró MVC |
| Tkinter (classes) | JavaFX / Swing |
| Gestió d'errors | Try-catch exceptions |

## 🚀 Reptes Extra

Per a alumnes que acabin abans:

### Repte 1: Personalització Visual (⭐) **NOU!**
Utilitzar la funció `obtenir_configuracio()` per:
- Canviar colors dels botons
- Modificar el títol de la finestra
- Ajustar mides de fonts
- Posar el seu nom al peu

**Avantatge**: És el repte més accessible i motivador!

### Repte 2: Tema Fosc/Clar (⭐⭐)
Crear dues configuracions i alternar entre elles

### Repte 3: Concurs de Disseny (⭐⭐)
Fer que els alumnes comparteixin els seus dissenys personalitzats

### Repte 4: Calculadora Gegant/Mini (⭐⭐)
Experimentar amb mides extremes (200x300 o 800x900)

## 📊 Avaluació
### Criteris d'Avaluació
- ✅ Completa les 4 funcions matemàtiques
- ✅ Les funcions retornen valors correctes
- ✅ La calculadora s'executa sense errors
- ✅ Comprèn els conceptes bàsics explicats

### Rúbrica (opcional)
- **Excel·lent (9-10)**: Totes les tasques + almenys 1 repte extra + entén com funciona l'import
- **Notable (7-8)**: Totes les tasques completades i funcionant
- **Bé (6-7)**: Les 4 funcions fetes però amb petits errors
- **Suficient (5-6)**: Almenys 3 funcions correctes
- **Suficient (4-5)**: Tasques 1-4 completades

## 🛠️ Resolució de Problemes

### Problema: Python no està instal·lat
### Problema: L'alumne no sap què posar
**Solució**: Guiar-lo a la guia d'alumnes, hi ha exemples i solucions

### Problema: Error "No module named 'interficie_calculadora'"
**Solució**: Els dos fitxers han d'estar a la mateixa carpeta

## 📝 Notes per al Professor

- **Velocitat**: Alguns alumnes aniran més ràpid, tingues els reptes preparats
- **Errors comuns**: Oblidar el `return` (el més freqüent!)
- **Avantatge nova estructura**: Els alumnes NO poden trencar la interfície accidentalment
- **Avantatge nova estructura**: Els alumnes NO poden trencar la interfície accidentalment
- **Personalització**: La tasca de configuració és molt motivadora i visual!
- **Motivació**: Recordar constantment que estan creant "alguna cosa real"
- **Paciència**: Molts veuran codi per primera vegada, anar a poc a poc
- **Concepte clau**: Les funcions són "caixes negres" que la interfície utilitza
- **Creativitat**: Anima'ls a personalitzar colors - és la manera més divertida d'aprendre diccionaris

## 📝 Notes per al Professor

- **Velocitat**: Alguns alumnes aniran més ràpid, tingues els reptes preparats
- **Errors comuns**: Oblidar el `return`, no descomentar `mainloop()`
- **Motivació**: Recordar constantment que estan creant "alguna cosa real"
- **Paciència**: Molts veuran codi per primera vegada, anar a poc a poc

## 📚 Recursos Addicionals

- [Python Docs oficial](https://docs.python.org/3/)
- [Tkinter Tutorial](https://docs.python.org/3/library/tkinter.html)
- [Real Python - Tkinter](https://realpython.com/python-gui-tkinter/)

## 📧 Suport

Per a dubtes o suggerències sobre aquest taller, contacta amb el creador del material.

---

**Versió**: 1.0  
**Data**: Desembre 2025  
**Llicència**: Material educatiu lliure
