# 🎓 TALLER DE PROGRAMACIÓ - CREA LA TEVA CALCULADORA

## 📋 Objectius del Taller

En aquest taller aprendràs:
- ✅ Què són les funcions i com crear-les
- ✅ Com treballar amb operacions matemàtiques
- ✅ Com es programa una interfície gràfica
- ✅ Gestió d'errors en programació

**Temps estimat**: 1-2 hores

---

## 🚀 Abans de Començar

### Requisits
- Python 3 instal·lat al teu ordinador
- Un editor de text (VS Code, PyCharm, o fins i tot Bloc de notes)
- Els fitxers del taller:
  - `calculadora_alumnes.py` (on programaràs tu)
  - `interficie_calculadora.py` (interfície gràfica, NO cal tocar)

### Comprovar que Python està instal·lat
Obre un terminal i escriu:
```bash
python3 --version
```

Hauries de veure algo com `Python 3.x.x`

### Instal·lar Tkinter (necessari per a la interfície gràfica)
```bash
sudo apt-get install python3-tk
```

---

## 📚 Conceptes Bàsics

### Què és una funció?
Una funció és com una "màquina" que:
1. Rep uns valors d'entrada (paràmetres)
2. Fa alguna cosa amb ells
3. Retorna un resultat

**Exemple**:
```python
def saludar(nom):
    return "Hola, " + nom

# Utilitzar la funció
missatge = saludar("Maria")
print(missatge)  # Mostra: Hola, Maria
```

### Operadors matemàtics en Python
- `+` → Suma
- `-` → Resta
- `*` → Multiplicació
- `/` → Divisió

---

## 🎯 TASCA 1: Funció Sumar

**Objectiu**: Fer que la calculadora pugui sumar dos números.

### Què has de fer:
1. Obre el fitxer `calculadora_alumnes.py`
2. Cerca la funció `sumar()` (línia ~22)
3. Substitueix el `pass` per una línia que retorni la suma

### Pistes:
- Has de retornar el resultat amb `return`
- Per sumar, utilitza l'operador `+`

### Solució:
```python
def sumar(num1, num2):
    return num1 + num2
```

### Prova-ho:
```python
# Afegeix aquestes línies al final del fitxer temporalment
print(sumar(5, 3))  # Ha de mostrar: 8
print(sumar(10, 20))  # Ha de mostrar: 30
```

---

## 🎯 TASCA 2: Funció Restar

**Objectiu**: Fer que la calculadora pugui restar dos números.

### Què has de fer:
Igual que la tasca 1, però ara amb la resta (`-`)

### Solució:
```python
def restar(num1, num2):
    return num1 - num2
```

### Prova-ho:
```python
print(restar(10, 3))  # Ha de mostrar: 7
print(restar(5, 8))   # Ha de mostrar: -3
```

---

## 🎯 TASCA 3: Funció Multiplicar

**Objectiu**: Fer que la calculadora pugui multiplicar dos números.

### Què has de fer:
Mateixa estructura, però amb multiplicació (`*`)

### Solució:
```python
def multiplicar(num1, num2):
    return num1 * num2
```

### Prova-ho:
```python
print(multiplicar(4, 5))   # Ha de mostrar: 20
print(multiplicar(7, 3))   # Ha de mostrar: 21
```

---

## 🎯 TASCA 4: Funció Dividir

**Objectiu**: Fer que la calculadora pugui dividir dos números.

### Què has de fer:
Utilitza l'operador de divisió (`/`)

### ⚠️ Atenció:
Què passa si algú intenta dividir entre 0? (Ho gestionarem a la TASCA 6)

### Solució:
```python
def dividir(num1, num2):
    return num1 / num2
```

### Prova-ho:
```python
print(dividir(10, 2))  # Ha de mostrar: 5.0
print(dividir(15, 3))  # Ha de mostrar: 5.0
```

---

## 🎯 TASCA 5: Executar la Calculadora

**Objectiu**: Veure la teva calculadora en funcionament!

### Què has de fer:
1. Guarda el fitxer `calculadora_alumnes.py`

2. Executa-la des del terminal:
   ```bash
   python3 calculadora_alumnes.py
   ```

3. **Opció alternativa**: Si vols provar les funcions abans d'executar la calculadora:
   - Descomenta les línies de la funció `provar_funcions()` al fitxer
   - Descomenta també `provar_funcions()` a la línia ~122
   - Executa el fitxer i veuràs els resultats de les teves funcions

### ✨ Si tot ha anat bé:
Hauria d'obrir-se una finestra amb la teva calculadora funcionant!

### 💡 Com funciona:
- Les teves funcions (sumar, restar, etc.) són passades a la interfície gràfica
- Quan cliques un botó d'operació, la calculadora crida la teva funció
- El fitxer `interficie_calculadora.py` s'encarrega de tota la part visual

---

## 🧪 Proves

Prova la teva calculadora amb aquestes operacions:

| Operació | Resultat Esperat |
|----------|------------------|
| 5 + 3    | 8                |
| 10 - 4   | 6                |
| 6 * 7    | 42               |
| 20 / 4   | 5                |
| 10 / 0   | Error!           |

---

## 🎓 Què has après?

✅ **Funcions**: Crear petits blocs de codi reutilitzables
✅ **Paràmetres i Return**: Com passen informació les funcions
✅ **Operadors**: Fer càlculs matemàtics en Python
✅ **Condicionals**: Prendre decisions (if/elif)
✅ **Gestió d'errors**: Evitar que el programa es trenqui
✅ **Interfícies gràfiques**: Crear aplicacions visuals

---

## 🚀 Reptes Extra (Opcionals)

Si has acabat abans de temps, prova aquests reptes:

### Repte 1: Personalitza la teva calculadora ⭐
**Objectiu**: Canviar colors, mides i títol de la calculadora

**Què has de fer**:
1. Al fitxer `calculadora_alumnes.py`, busca la funció `obtenir_configuracio()`
2. Descomenta les línies que vulguis modificar
3. Canvia els valors dels colors, mides o títol
4. Guarda i executa per veure els canvis!

**Exemples de colors**:
```python
config = {
    'titol': '🧮 La Meva Calc',
    'color_numeros': '#2980B9',  # Blau fosc
    'color_operacions': '#F39C12',  # Taronja
    'color_igual': '#16A085',  # Verd aigua
    'autor': 'El teu nom'
}
```

**Pista**: Pots trobar més colors a [htmlcolorcodes.com](https://htmlcolorcodes.com/)

### Repte 2: Tema fosc/clar
Crear dues configuracions diferents i canviar entre elles

### Repte 3: Mides personalitzades
Fer una calculadora més gran o més petita canviant `mida` i les fonts

### Repte 4: Compartir el teu disseny
Mostrar la teva calculadora personalitzada als companys!

---

## ❓ Problemes Comuns

### Error: "name 'tk' is not defined"
**Solució**: Assegura't que la línia `import tkinter as tk` està al principi del fitxer.

### Error: "invalid syntax"
**Solució**: Comprova que no hi ha `pass` on hauria d'haver codi.

### Error: "No module named 'interficie_calculadora'"
**Solució**: Assegura't que els dos fitxers (`calculadora_alumnes.py` i `interficie_calculadora.py`) estan a la mateixa carpeta.

### El botó "=" no fa res o mostra error
**Solució**: Revisa que les teves funcions retornen el resultat amb `return`.

---

## 📞 Suport

Si tens problemes:
1. Rellegeix la tasca amb calma
2. Comprova els exemples de solució
3. Pregunta al professor/a

---

## 🎉 Felicitats!

Has creat la teva primera aplicació amb interfície gràfica!

Això és només el principi. Amb Python i els conceptes que has après, podràs crear:
## 🎓 Què has après?

✅ **Funcions**: Crear petits blocs de codi reutilitzables
✅ **Paràmetres i Return**: Com passen informació les funcions
✅ **Operadors**: Fer càlculs matemàtics en Python
✅ **Imports**: Com utilitzar codi d'altres fitxers
✅ **Diccionaris**: Organitzar funcions i dades
✅ **Separació de concerns**: Interfície separada de la lògica