# Guide : Data Oriented Design en Python

Ce guide explique les concepts de **Data Oriented Design** en Python, incluant les **closures**, le mot-clé `nonlocal`, les **décorateurs**, les **wrappers** et les **dataclasses**.

---

## 📋 Table des matières

1. [Vue d'ensemble](#1-vue-densemble)
2. [Le mot-clé `nonlocal`](#2-le-mot-clé-nonlocal)
3. [Exemple 1 : Fonction `outer`](#3-exemple-1-fonction-outer)
4. [Exemple 2 : Décorateur `callLimit`](#4-exemple-2-décorateur-calllimit)
5. [Les décorateurs Python](#5-les-décorateurs-python)
6. [Les Wrappers](#6-les-wrappers)
7. [Les Dataclasses](#7-les-dataclasses)
8. [Comparaison avec `global`](#8-comparaison-avec-global)

---

## 1. Vue d'ensemble

### Qu'est-ce que le Data Oriented Design ?

Le **Data Oriented Design** (DOD) est un paradigme de programmation qui met l'accent sur la **structure des données** plutôt que sur le comportement. En Python, cela se traduit par l'utilisation de structures de données simples et efficaces.

### Concepts abordés

- **Closures** : Fonctions qui capturent et mémorisent des variables
- **`nonlocal`** : Modification de variables du scope parent
- **Décorateurs** : Modification du comportement des fonctions
- **Wrappers** : Enveloppement de fonctions
- **Dataclasses** : Classes orientées données avec génération automatique de code

---

## 2. Le mot-clé `nonlocal`

### Problème sans `nonlocal`

```python
def outer():
    count = 0
    
    def inner():
        count += 1  # ❌ Erreur : UnboundLocalError
        return count
    return inner
```

**Erreur :** `UnboundLocalError: local variable 'count' referenced before assignment`

**Pourquoi ?** Python voit `count += 1` et pense que `count` est une variable locale, mais elle n'existe pas encore.

### Solution avec `nonlocal`

```python
def outer():
    count = 0
    
    def inner():
        nonlocal count  # ✅ Dit à Python : "count vient du scope parent"
        count += 1
        return count
    return inner
```

**`nonlocal` indique :**
- "Je veux modifier la variable `count` du scope parent"
- "Ne crée pas une nouvelle variable locale"
- "Utilise celle qui existe déjà dans `outer`"

### Schéma simplifié

```
outer() {
    count = 0          ← Variable dans outer
    
    inner() {
        nonlocal count ← Référence à count de outer
        count += 1     ← Modifie count de outer
    }
}
```

---

## 3. Exemple 1 : Fonction `outer`

### Code

```python
def outer(x: int | float, function) -> object:
    result = x

    def inner() -> float:
        nonlocal result
        result = function(result)
        return result
    return inner
```

### Fonctionnement

**Étape 1 : Création**
```python
my_counter = outer(5, square)  # square(x) = x²
```
- `outer` crée `result = 5` et définit `inner`
- Retourne la fonction `inner` (avec mémoire de `result` et `function`)

**Étape 2 : Appels**
```python
print(my_counter())  # 25  (square(5))
print(my_counter())  # 625  (square(25))
print(my_counter())  # 390625  (square(625))
```

### Schéma de flux

```
outer(5, square)
  ↓
Crée: result=5, function=square
  ↓
Retourne inner (avec mémoire)
  ↓
Appel 1: inner() → square(5) = 25, result=25
Appel 2: inner() → square(25) = 625, result=625
Appel 3: inner() → square(625) = 390625, result=390625
```

---

## 4. Exemple 2 : Décorateur `callLimit`

### Code

```python
def callLimit(limit: int):
    '''Returns a function that limits the number of times
    a function can be called.'''
    count: int = 0

    def callLimiter(function):
        def limit_function(*args, **kwds):
            nonlocal count
            if count >= limit:
                print(f"Error: {function} called too many times")
                return None
            count += 1
            return function(*args, **kwds)
        return limit_function

    return callLimiter
```

### Fonctionnement

**Structure à 3 niveaux :**
1. `callLimit(limit)` → Retourne `callLimiter`
2. `callLimiter(function)` → Retourne `limit_function`
3. `limit_function(*args, **kwds)` → Exécute la fonction originale

**Variables capturées :**
- `count` : Compteur de nombre d'appels (modifié avec `nonlocal`)
- `limit` : Limite maximale d'appels
- `function` : Fonction originale à limiter

### Utilisation avec décorateur

```python
@callLimit(3)
def f():
    print("f()")

f()  # f()
f()  # f()
f()  # f()
f()  # Error: <function f> called too many times
```

---

## 5. Les décorateurs Python

### Qu'est-ce qu'un décorateur ?

Un **décorateur** est une fonction qui prend une fonction en paramètre et retourne une nouvelle fonction modifiée.

### Syntaxe avec `@`

```python
@callLimit(3)
def f():
    print("f()")
```

**Équivalent à :**
```python
def f():
    print("f()")

f = callLimit(3)(f)  # Applique le décorateur manuellement
```

### Décorateurs à paramètres

```python
@callLimit(3)  # ← Paramètre du décorateur
def f():
    pass
```

**Structure :**
- `callLimit` est une **factory de décorateurs**
- Elle retourne un décorateur (`callLimiter`)
- Le décorateur retourne une fonction modifiée (`limit_function`)

---

## 6. Les Wrappers

### Qu'est-ce qu'un Wrapper ?

Un **wrapper** (enveloppeur) est une fonction qui "enveloppe" une autre fonction pour ajouter des fonctionnalités supplémentaires sans modifier le code original.

### Wrapper dans un décorateur

```python
def my_decorator(func):
    def wrapper(*args, **kwargs):  # ← C'est le wrapper
        print("Avant")
        result = func(*args, **kwargs)  # Appelle la fonction originale
        print("Après")
        return result
    return wrapper
```

### Préservation des métadonnées avec `functools.wraps`

```python
from functools import wraps

def my_decorator(func):
    @wraps(func)  # ← Préserve les métadonnées
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper
```

---

## 7. Les Dataclasses

### Qu'est-ce qu'une dataclass ?

Une **dataclass** est un décorateur Python qui génère automatiquement des méthodes spéciales (`__init__`, `__repr__`, `__eq__`, etc.) pour une classe orientée données.

### Code étudié

```python
from dataclasses import dataclass, field

@dataclass
class Student:
    '''Student dataclass.'''
    name: str = field(default="unknown_name")
    surname: str = field(default="unknown_surname")
    active: bool = field(default=True)
    login: str = field(init=False)
    id: str = field(init=False)

    def __post_init__(self):
        self.login = f"{self.name.lower()}.{self.surname.lower()}"
        self.id = generate_id()
```

### Fonctionnement détaillé

#### Le décorateur `@dataclass`

Le décorateur `@dataclass` génère automatiquement :
- `__init__()` : Constructeur avec tous les champs
- `__repr__()` : Représentation lisible de l'objet
- `__eq__()` : Comparaison d'égalité basée sur les champs
- `__hash__()` : Hash basé sur les champs (si `frozen=True`)

#### La fonction `field()`

`field()` permet de configurer les champs de la dataclass :

**Paramètres importants :**
- `default` : Valeur par défaut du champ
- `init=False` : Le champ n'est pas dans `__init__()` (doit être initialisé ailleurs)
- `repr=True` : Inclure le champ dans `__repr__()`
- `compare=True` : Inclure le champ dans `__eq__()`

#### Explication ligne par ligne

```python
name: str = field(default="unknown_name")
```
- **`name: str`** : Annotation de type (le champ est une chaîne)
- **`field(default="unknown_name")`** : Valeur par défaut si non fournie

```python
login: str = field(init=False)
```
- **`init=False`** : Le champ `login` n'est **pas** un paramètre de `__init__()`
- Il doit être initialisé dans `__post_init__()` ou ailleurs

```python
def __post_init__(self):
    self.login = f"{self.name.lower()}.{self.surname.lower()}"
    self.id = generate_id()
```
- **`__post_init__()`** : Méthode appelée **après** `__init__()`
- Permet d'initialiser les champs avec `init=False`
- Utilise les valeurs des autres champs pour calculer de nouvelles valeurs

### Schéma du processus d'initialisation

```
Student(name="Edward", surname="agle")
  ↓
1. @dataclass génère __init__()
   → __init__(self, name="Edward", surname="agle", active=True)
   → Initialise: self.name, self.surname, self.active
  ↓
2. __init__() appelle __post_init__()
  ↓
3. __post_init__() s'exécute
   → self.login = "edward.agle"
   → self.id = generate_id()  # Ex: "qawxdtanefwqjbw"
  ↓
4. Objet Student créé avec tous les champs
```

### Exemples d'utilisation

#### Exemple 1 : Création avec tous les paramètres

```python
student = Student(name="Edward", surname="agle")
print(student)
# Student(name='Edward', surname='agle', active=True, 
#         login='edward.agle', id='qawxdtanefwqjbw')
```

**Ce qui se passe :**
- `name` et `surname` sont fournis
- `active` prend la valeur par défaut `True`
- `__post_init__()` calcule `login` et `id`

#### Exemple 2 : Création avec un seul paramètre

```python
student = Student(name="ba")
print(student)
# Student(name='ba', surname='unknown_surname', active=True,
#         login='ba.unknown_surname', id='hduhjdgugezquka')
```

**Ce qui se passe :**
- Seul `name` est fourni
- `surname` prend la valeur par défaut `"unknown_surname"`
- `active` prend la valeur par défaut `True`
- `__post_init__()` calcule `login` avec les valeurs par défaut

#### Exemple 3 : Création sans paramètres

```python
student = Student()
print(student)
# Student(name='unknown_name', surname='unknown_surname', active=True,
#         login='unknown_name.unknown_surname', id='rknfwlufxiwjzic')
```

**Ce qui se passe :**
- Tous les champs prennent leurs valeurs par défaut
- `__post_init__()` calcule `login` et `id`

#### Exemple 4 : Création avec tous les paramètres explicites

```python
student = Student(name="perso", surname="one", active=False)
print(student)
# Student(name='perso', surname='one', active=False,
#         login='perso.one', id='txikczvpedceccz')
```

### Comparaison : Classe normale vs Dataclass

**Classe normale (sans dataclass) :**
```python
class Student:
    def __init__(self, name="unknown_name", surname="unknown_surname", active=True):
        self.name = name
        self.surname = surname
        self.active = active
        self.login = f"{name.lower()}.{surname.lower()}"
        self.id = generate_id()
    
    def __repr__(self):
        return f"Student(name='{self.name}', surname='{self.surname}', ...)"
    
    def __eq__(self, other):
        if not isinstance(other, Student):
            return False
        return (self.name, self.surname, self.active) == \
               (other.name, other.surname, other.active)
```

**Avec dataclass :**
```python
@dataclass
class Student:
    name: str = field(default="unknown_name")
    surname: str = field(default="unknown_surname")
    active: bool = field(default=True)
    login: str = field(init=False)
    id: str = field(init=False)
    
    def __post_init__(self):
        self.login = f"{self.name.lower()}.{self.surname.lower()}"
        self.id = generate_id()
```

**Avantages de la dataclass :**
- ✅ Moins de code à écrire
- ✅ `__init__()`, `__repr__()`, `__eq__()` générés automatiquement
- ✅ Code plus lisible et maintenable
- ✅ Type hints intégrés

### Cas d'usage des dataclasses

- **Structures de données** : Représenter des données simples
- **Configuration** : Stocker des paramètres de configuration
- **DTO (Data Transfer Objects)** : Transférer des données entre couches
- **Records** : Enregistrements avec champs fixes
- **Points de données** : Coordonnées, mesures, etc.

### Bonnes pratiques avec dataclasses

✅ **Utilisez des type hints** pour tous les champs  
✅ **Utilisez `field()`** pour des valeurs par défaut complexes  
✅ **Utilisez `__post_init__()`** pour l'initialisation dérivée  
✅ **Documentez** les champs avec des docstrings  

❌ **N'utilisez pas** de valeurs mutables comme valeurs par défaut  
❌ **Ne créez pas** de logique métier complexe dans `__post_init__()`  

---

## 8. Comparaison avec `global`

### `nonlocal` vs `global`

| Caractéristique | `nonlocal` | `global` |
|----------------|------------|----------|
| **Scope cible** | Scope parent (fonction englobante) | Scope global (module) |
| **Portée** | Limité à la hiérarchie de fonctions | Accès au niveau module |
| **Usage** | Variables dans des fonctions imbriquées | Variables au niveau module |

### Exemple de différence

```python
count_global = 0  # Variable globale

def outer():
    count_local = 0  # Variable dans outer
    
    def inner():
        nonlocal count_local  # Modifie count_local de outer
        global count_global   # Modifie count_global du module
        count_local += 1
        count_global += 1
        return count_local, count_global
    return inner

func = outer()
print(func())  # (1, 1)
print(func())  # (2, 2)
```

---

## 📚 Résumé

### Points clés

1. **Closure** : Fonction interne qui capture des variables de son environnement
2. **`nonlocal`** : Permet de modifier une variable du scope parent (pas global)
3. **Décorateurs** : Fonctions qui modifient d'autres fonctions
4. **Wrappers** : Fonctions qui enveloppent d'autres fonctions pour ajouter des fonctionnalités
5. **Dataclasses** : Classes orientées données avec génération automatique de code
6. **État persistant** : Les closures maintiennent l'état entre les appels

### Cas d'usage

- **Compteurs** : Maintenir un compteur entre appels
- **Limiteurs** : Limiter le nombre d'appels d'une fonction
- **Mémorisation** : Se souvenir de résultats précédents
- **Logging** : Enregistrer les appels de fonction
- **Validation** : Vérifier les paramètres avant exécution
- **Structures de données** : Représenter des données simples et complexes

### Bonnes pratiques

✅ **Utilisez `nonlocal`** pour modifier des variables du scope parent  
✅ **Utilisez des closures** pour créer des fonctions avec état  
✅ **Utilisez des décorateurs** pour modifier le comportement de fonctions  
✅ **Utilisez `functools.wraps`** pour préserver les métadonnées dans les wrappers  
✅ **Utilisez des dataclasses** pour des structures de données simples  
✅ **Documentez** clairement le comportement  

❌ **Évitez** d'utiliser `global` à la place de `nonlocal`  
❌ **Ne créez pas** trop de niveaux d'imbrication (complexité)  
❌ **N'oubliez pas** `@wraps` dans vos wrappers pour préserver les métadonnées  
❌ **N'utilisez pas** de valeurs mutables comme valeurs par défaut dans les dataclasses  

---

## 🔍 Pour aller plus loin

- **Documentation Python** : [PEP 3104 - Access to Names in Outer Scopes](https://peps.python.org/pep-3104/)
- **Décorateurs** : [PEP 318 - Decorators for Functions and Methods](https://peps.python.org/pep-0318/)
- **Dataclasses** : [PEP 557 - Data Classes](https://peps.python.org/pep-0557/)
- **Closures** : Concept de programmation fonctionnelle
- **Functools** : Module avec des décorateurs utiles (`@lru_cache`, `@wraps`)

