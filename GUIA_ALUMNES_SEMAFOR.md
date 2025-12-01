# 🚦 TALLER DE PROGRAMACIÓ - SEMÀFOR INTERACTIU

## 📋 Objectius del Taller

En aquest taller aprendràs:
- ✅ Cridar mètodes d'objectes
- ✅ Passar paràmetres a funcions
- ✅ Crear seqüències d'accions
- ✅ Veure resultats visuals immediats
- ✅ Programar comportaments interactius

**Temps estimat**: 1 hora

---

## 🚀 Abans de Començar

### Requisits
- Python 3 instal·lat al teu ordinador
- Tkinter instal·lat (normalment ve amb Python)
- Els fitxers:
  - `semafor_alumnes.py` (on programaràs tu)
  - `interficie_semafor.py` (interfície gràfica, NO cal tocar)

### Comprovar que Python està instal·lat
Obre un terminal i escriu:
```bash
python3 --version
```

### Instal·lar Tkinter (si cal)
```bash
sudo apt-get install python3-tk
```

---

## 📚 Conceptes Bàsics

### Què és un objecte?
Un objecte és com una "màquina" que té botons (mètodes) que pots prémer.

**Exemple**:
```python
# El semàfor és un objecte
# Té mètodes que pots cridar:
semafor.encendre_llum("verd")  # Premem el botó "encendre verd"
```

### Mètodes disponibles del semàfor

El teu semàfor té aquests "botons" que pots utilitzar:

| Mètode | Què fa | Exemple |
|--------|--------|---------|
| `encendre_llum("color")` | Encén un llum | `semafor.encendre_llum("verd")` |
| `apagar_tots()` | Apaga tots els llums | `semafor.apagar_tots()` |
| `parpallejar("color", vegades)` | Fa parpallejar un llum | `semafor.parpallejar("groc", vegades=5)` |
| `esperar(segons)` | Fa una pausa | `semafor.esperar(2)` |
| `mostrar_text("missatge")` | Mostra un text | `semafor.mostrar_text("Hola!")` |

---

## 🎯 TASCA 1: Activar el Llum Verd

**Objectiu**: Fer que el botó "🟢 Verd" encengui el llum verd.

### Què has de fer:
1. Obre el fitxer `semafor_alumnes.py`
2. Cerca la funció `activar_verd()` (línia ~23)
3. Substitueix el `pass` per la crida al mètode

### Pistes:
- Has de cridar el mètode `encendre_llum`
- El paràmetre ha de ser `"verd"`

### Solució:
```python
def activar_verd(semafor):
    semafor.encendre_llum("verd")
```

### Prova-ho:
1. Guarda el fitxer
2. Executa: `python3 semafor_alumnes.py`
3. Clica el botó "🟢 Verd"
4. El llum verd s'hauria d'encendre!

---

## 🎯 TASCA 2: Activar el Llum Groc

**Objectiu**: Fer que el botó "🟡 Groc" encengui el llum groc.

### Què has de fer:
Igual que la tasca 1, però amb el color "groc"

### Solució:
```python
def activar_groc(semafor):
    semafor.encendre_llum("groc")
```

---

## 🎯 TASCA 3: Activar el Llum Vermell

**Objectiu**: Fer que el botó "🔴 Vermell" encengui el llum vermell.

### Solució:
```python
def activar_vermell(semafor):
    semafor.encendre_llum("vermell")
```

---

## 🎯 TASCA 4: Apagar Tots els Llums

**Objectiu**: Fer que el botó "⚫ Apagar" apagui tots els llums.

### Què has de fer:
Cridar el mètode `apagar_tots()` (sense paràmetres)

### Solució:
```python
def apagar_tots(semafor):
    semafor.apagar_tots()
```

---

## 🎯 TASCA 5: Seqüència Normal del Semàfor

**Objectiu**: Crear la seqüència típica d'un semàfor: VERD → GROC → VERMELL

### Què has de fer:
1. Encendre el llum verd
2. Esperar 2 segons
3. Encendre el llum groc
4. Esperar 1 segon
5. Encendre el llum vermell
6. Esperar 2 segons
7. Apagar tots els llums

### Pistes:
- Necessites cridar `encendre_llum()` 3 vegades (amb colors diferents)
- Necessites cridar `esperar()` després de cada canvi
- Al final, crida `apagar_tots()`

### Solució:
```python
def sequencia_normal(semafor):
    semafor.encendre_llum("verd")
    semafor.esperar(2)
    semafor.encendre_llum("groc")
    semafor.esperar(1)
    semafor.encendre_llum("vermell")
    semafor.esperar(2)
    semafor.apagar_tots()
```

### Prova-ho:
Clica el botó "🔄 Seqüència" i veuràs el semàfor canviar automàticament!

---

## 🎯 TASCA 6: Mode Nocturn

**Objectiu**: Fer que el llum groc parpellegi (com els semàfors de nit).

### Què has de fer:
Cridar el mètode `parpallejar` amb:
- Color: "groc"
- Vegades: 5

### Pistes:
```python
semafor.parpallejar("color", vegades=número)
```

### Solució:
```python
def mode_nocturn(semafor):
    semafor.parpallejar("groc", vegades=5)
```

### Prova-ho:
Clica el botó "🌙 Nocturn" i veuràs el llum groc parpallejar!

---

## 🧪 Proves

Comprova que tot funciona correctament:

| Botó | Resultat Esperat |
|------|------------------|
| 🟢 Verd | El llum verd s'encén |
| 🟡 Groc | El llum groc s'encén |
| 🔴 Vermell | El llum vermell s'encén |
| ⚫ Apagar | Tots els llums s'apaguen |
| 🔄 Seqüència | Verd → Groc → Vermell automàticament |
| 🌙 Nocturn | El groc parpelleja 5 vegades |

---

## 🎓 Què has après?

✅ **Cridar mètodes**: Utilitzar funcions d'un objecte
✅ **Paràmetres**: Passar informació als mètodes (colors, números)
✅ **Seqüències**: Combinar múltiples accions
✅ **Temporització**: Fer pauses amb `esperar()`
✅ **Interacció visual**: Veure resultats immediats

---

## 🎮 TASQUES INTERACTIVES (Amb Input de l'Usuari)

Aquestes tasques són més avançades i utilitzen **diàlegs** per demanar informació a l'usuari!

### Tasca Interactiva 1: Seqüència amb Temps Personalitzat ⭐⭐⭐

**Objectiu**: Crear una seqüència on l'usuari tria quants segons vol cada llum.

**Nous mètodes que aprendràs**:
- `semafor.demanar_numero("pregunta", default=2, minim=1, maxim=10)` - Mostra un diàleg per demanar un número

**Què has de fer**:
1. Demanar quants segons vol el verd
2. Demanar quants segons vol el groc
3. Demanar quants segons vol el vermell
4. Fer la seqüència amb aquests temps

**Solució**:
```python
def sequencia_amb_temps_personalitzat(semafor):
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
```

**Prova-ho**: Clica el botó "⏱️ Temps Custom" i tria els teus temps!

---

### Tasca Interactiva 2: Parpelleig Personalitzat ⭐⭐⭐

**Objectiu**: L'usuari tria el color i quantes vegades vol que parpellegi.

**Nous mètodes**:
- `semafor.triar_color()` - Mostra un diàleg per triar color (retorna "verd", "groc" o "vermell")

**Solució**:
```python
def parpelleig_personalitzat(semafor):
    color = semafor.triar_color()
    vegades = semafor.demanar_numero("Quantes vegades?", default=3, minim=1, maxim=20)
    semafor.parpallejar(color, vegades=vegades)
```

**Prova-ho**: Clica "✨ Parpelleig Custom"

---

### Tasca Interactiva 3: Missatge Personalitzat ⭐⭐

**Objectiu**: Mostra un missatge que escriu l'usuari amb una animació.

**Nous mètodes**:
- `semafor.demanar_text("pregunta", default="")` - Mostra un diàleg per escriure text

**Solució**:
```python
def missatge_personalitzat(semafor):
    missatge = semafor.demanar_text("Escriu un missatge:", default="Hola!")
    semafor.mostrar_text(f"💬 {missatge}")
    semafor.parpallejar("verd", vegades=2, interval=0.3)
```

**Prova-ho**: Clica "💬 Missatge"

---

## 🚀 Reptes Extra (Opcionals)

Si has acabat abans de temps, prova aquests reptes:

### Repte 1: Seqüència Personalitzada ⭐⭐
Crea la teva pròpia seqüència de llums!

**Idees**:
- Fer que tots els llums parpellegin un per un
- Crear una seqüència llarga amb diferents temps
- Fer un "show de llums"

**Exemple**:
```python
def sequencia_personalitzada(semafor):
    semafor.parpallejar("verd", vegades=2)
    semafor.esperar(0.5)
    semafor.parpallejar("groc", vegades=2)
    semafor.esperar(0.5)
    semafor.parpallejar("vermell", vegades=2)
```

### Repte 2: Mode Emergència ⭐⭐
Fes que el llum vermell parpellegi ràpidament

**Pista**: Usa `interval=0.3` per fer-ho més ràpid
```python
semafor.parpallejar("vermell", vegades=10, interval=0.3)
```

### Repte 3: Test Complet ⭐
Prova cada llum individualment amb pauses

### Repte 4: Seqüència a l'Inversa ⭐⭐
Fes la seqüència: VERMELL → GROC → VERD

---

## ❓ Problemes Comuns

### Error: "name 'semafor' is not defined"
**Solució**: Assegura't que la funció té el paràmetre `semafor`:
```python
def activar_verd(semafor):  # ← Important!
```

### El botó no fa res
**Solució**: 
1. Comprova que has substituït el `pass`
2. Verifica que has escrit bé el nom del color

### Error: "invalid syntax"
**Solució**: Comprova les cometes i parèntesis:
```python
semafor.encendre_llum("verd")  # ← Cometes i parèntesis correctes
```

### No es veu el semàfor
**Solució**: Verifica que Tkinter està instal·lat:
```bash
python3 -m tkinter
```

---

## 📞 Suport

Si tens problemes:
1. Revisa l'error a la consola
2. Comprova els exemples de solució
3. Prova la funció `provar_funcions()` (descomenta-la)
4. Pregunta al professor/a

---

## 🎉 Felicitats!

Has creat el teu primer semàfor interactiu!

Amb el que has après, pots programar:
- Semàfors per a creuaments
- Sistemes de llums intel·ligents
- Animacions i efectes visuals
- I molt més!

**Segueix practicant! 💪**

---

## 💡 Consells Finals

- **Experimenta**: Canvia els temps d'espera, colors, etc.
- **Combina**: Crea seqüències complexes
- **Comparteix**: Mostra la teva seqüència personalitzada als companys
- **Pregunta**: No tinguis por de preguntar si tens dubtes

El més important és **aprendre divertint-te**! 🎮
