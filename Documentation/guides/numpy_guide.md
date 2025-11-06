# NumPy - Guide de référence rapide

> Pense-bête complet pour maîtriser NumPy - Bibliothèque fondamentale pour le calcul scientifique en Python

---

## Table des matières

1. [Installation et import](#installation-et-import)
2. [Création d'arrays](#création-darrays)
3. [Propriétés et attributs des arrays](#propriétés-et-attributs-des-arrays)
4. [Indexing et slicing](#indexing-et-slicing)
5. [Manipulation de shape](#manipulation-de-shape)
6. [Opérations mathématiques](#opérations-mathématiques)
7. [Opérations statistiques](#opérations-statistiques)
8. [Opérations booléennes et masking](#opérations-booléennes-et-masking)
9. [Broadcasting](#broadcasting)
10. [Manipulation d'images](#manipulation-dimages)
11. [Méthodes utiles supplémentaires](#méthodes-utiles-supplémentaires)

---

## Installation et import

```python
import numpy as np
```

**Convention standard** : importer NumPy avec l'alias `np` pour éviter de taper `numpy.` à chaque fois.

**Installation** :
```bash
pip install numpy
# ou avec conda
conda install numpy
```

---

## Création d'arrays

### Création d'arrays à partir de listes Python

```python
# Array 1D à partir d'une liste
a_list = [1, 2, 3, 4, 5, 6, 7]
z = np.array(a_list)
# Résultat : array([1, 2, 3, 4, 5, 6, 7])

# Array 2D à partir d'une liste de listes
b_list = [[9, 8, 7, 6, 5, 4, 3], [1, 2, 3, 4, 5, 6, 7]]
z = np.array(b_list)
# Résultat : array([[9, 8, 7, 6, 5, 4, 3],
#                   [1, 2, 3, 4, 5, 6, 7]])
```

### Arrays remplis de zéros

```python
# Array 1D avec 3 zéros
a = np.zeros(3)
# Résultat : array([0., 0., 0.])

# Array 1D avec 10 zéros
z = np.zeros(10)
# Résultat : array([0., 0., 0., ..., 0.])

# Array 2D (lignes, colonnes)
z = np.zeros((3, 4))
# Résultat : array([[0., 0., 0., 0.],
#                   [0., 0., 0., 0.],
#                   [0., 0., 0., 0.]])
```

**Schéma conceptuel :**
```
np.zeros(3)  →  [ 0    0    0 ]
                 └─────┬─────┘
                  3 éléments
```

### Arrays remplis de uns

```python
# Array 1D avec 10 uns
z = np.ones(10)
# Résultat : array([1., 1., 1., ..., 1.])

# Array 2D avec des uns
z = np.ones((2, 3))
# Résultat : array([[1., 1., 1.],
#                   [1., 1., 1.]])
```

### Arrays non initialisés (vide)

```python
# Array vide (valeurs aléatoires non initialisées)
z = np.empty(3)
# ⚠️ Attention : contient des valeurs "garbage" (mémoire non initialisée)
# Plus rapide que zeros() mais valeurs imprévisibles
```

**Schéma conceptuel :**
```
np.zeros()   →  Initialise à 0      (plus lent, sûr)
np.empty()   →  Pas d'initialisation (plus rapide, valeurs aléatoires)
np.ones()    →  Initialise à 1      (utile pour certains calculs)
```

### Array avec séquence linéaire

```python
# Génère 5 points équidistants entre 2 et 10 (inclus)
z = np.linspace(2, 10, 5)
# Résultat : array([ 2.,  4.,  6.,  8., 10.])
# Syntaxe : linspace(début, fin, nombre_de_points)
```

**Schéma visuel :**
```
linspace(2, 10, 5)

2 ────●────●────●────●────● 10
      2    4    6    8   10
      └────┬────┴────┴────┘
        5 points équidistants
```

### Array avec séquence arithmétique

```python
# Alternative à linspace : range avec pas
z = np.arange(0, 10, 2)
# Résultat : array([0, 2, 4, 6, 8])
# Syntaxe : arange(début, fin, pas)

# Équivalent à range() mais retourne un array
z = np.arange(10)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

**Différence entre linspace et arange :**
```
linspace(0, 10, 5)  → [0.,  2.5, 5.,  7.5, 10.]  (inclus la fin)
arange(0, 10, 2)    → [0, 2, 4, 6, 8]            (exclut la fin)
```

### Arrays avec valeurs aléatoires

```python
# Fixer la graine pour reproductibilité
np.random.seed(0)

# Entiers aléatoires entre 0 et 10 (exclu)
z1 = np.random.randint(10, size=(3, 4))
# Résultat : array([[5, 0, 3, 3],
#                   [7, 9, 3, 5],
#                   [2, 4, 7, 6]])

# Nombres décimaux aléatoires entre 0 et 1
z2 = np.random.random((3, 4))
# Résultat : array([[0.5488135 , 0.71518937, 0.60276338, ...],
#                   ...])

# Nombres aléatoires suivant une distribution normale
z3 = np.random.normal(0, 1, (3, 4))
# Paramètres : (moyenne, écart-type, shape)

# Autres distributions utiles :
z4 = np.random.uniform(0, 1, (3, 4))  # Distribution uniforme
z5 = np.random.randn(3, 4)            # Distribution normale standard (0, 1)
```

---

## Propriétés et attributs des arrays

### Type d'un array (ndarray)

```python
z = np.array([1, 2, 3])
type(z)
# Résultat : <class 'numpy.ndarray'>
# ndarray = n-dimensional array (array à n dimensions)
```

### Shape (dimensions)

```python
z = np.array([[9, 8, 7, 6, 5, 4, 3], [1, 2, 3, 4, 5, 6, 7]])
z.shape
# Résultat : (2, 7)  → 2 lignes, 7 colonnes

# Changer la shape directement (si compatible)
z = np.zeros(10)
z.shape = (10, 1)  # Transforme en colonne 10x1
# ou
z = z.reshape((10, 1))  # Méthode équivalente
```

**Schéma conceptuel :**
```
Array de shape (2, 7) :

┌────────────────────────┐
│  9  8  7  6  5  4  3   │ ← ligne 0 (index 0)
│  1  2  3  4  5  6  7   │ ← ligne 1 (index 1)
└────────────────────────┘
   ↑  ↑  ↑  ↑  ↑  ↑  ↑
 col0 col1 col2 col3 col4 col5 col6

2 lignes × 7 colonnes = 14 éléments
```

### Type des éléments (dtype)

```python
z = np.array([1, 2, 3])
z.dtype
# Résultat : dtype('int64')

z_float = np.array([1.0, 2.0, 3.0])
z_float.dtype
# Résultat : dtype('float64')

# Spécifier le dtype à la création
z = np.array([1, 2, 3], dtype=float)
# Résultat : array([1., 2., 3.])
```

### Taille totale (nombre d'éléments)

```python
z = np.array([[1, 2, 3], [4, 5, 6]])
z.size
# Résultat : 6  (2 × 3 = 6 éléments)
```

### Nombre de dimensions (ndim)

```python
z1d = np.array([1, 2, 3])
z1d.ndim
# Résultat : 1

z2d = np.array([[1, 2], [3, 4]])
z2d.ndim
# Résultat : 2
```

### Obtenir de l'aide (docstring)

```python
?z  # Dans Jupyter/IPython, affiche la documentation complète
# ou
help(z)
```

---

## Indexing et slicing

### Indexing 1D

```python
z = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
z[0]      # Premier élément : 1
z[-1]     # Dernier élément : 10
z[2:5]    # Slice : array([3, 4, 5]) (index 2 inclus, 5 exclu)
```

### Indexing 2D

```python
np.random.seed(0)
z1 = np.random.randint(10, size=(3, 4))
# Résultat : array([[5, 0, 3, 3],
#                   [7, 9, 3, 5],
#                   [2, 4, 7, 6]])

# Accès aux éléments
z1[0, 1]     # Ligne 0, colonne 1 : 0
z1[0][2]     # Syntaxe alternative : 3
z1[0, -1]    # Ligne 0, dernière colonne : 3

# Slicing de lignes
z1[0:2]      # Premières 2 lignes : array([[5, 0, 3, 3],
             #                             [7, 9, 3, 5]])

# Slicing complet
z1[0:2, 1:3] # Lignes 0-1, colonnes 1-2 : array([[0, 3],
             #                                     [9, 3]])
```

**Schéma d'indexing 2D :**
```
Array z1 (3×4) :

        col0  col1  col2  col3
ligne0   5     0     3     3     z1[0, 1] = 0
ligne1   7     9     3     5     z1[1, 2] = 3
ligne2   2     4     7     6     z1[2, 0] = 2

z1[0:2, 1:3] → colonnes 1-2 des lignes 0-1
```

### Slicing avancé avec pas (step)

```python
z = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

z[::2]      # Tous les 2 éléments : array([0, 2, 4, 6, 8])
z[1::2]     # À partir de 1, tous les 2 : array([1, 3, 5, 7, 9])
z[::-1]     # Inverser l'array : array([9, 8, 7, ..., 0])
z[5:1:-1]   # Rétrograde : array([5, 4, 3, 2])
```

**Syntaxe de slicing :**
```
array[début:fin:pas]
- début : inclus (défaut: début du array)
- fin   : exclu (défaut: fin du array)
- pas   : incrément (défaut: 1)
```

---

## Manipulation de shape

### Reshape (réorganisation des dimensions)

```python
z = np.arange(12)  # [0, 1, 2, ..., 11]
z.reshape(3, 4)    # Transforme en 3×4
# Résultat : array([[ 0,  1,  2,  3],
#                   [ 4,  5,  6,  7],
#                   [ 8,  9, 10, 11]])

# ⚠️ Le nombre d'éléments doit être compatible
# 12 éléments peut devenir (3, 4) ou (2, 6) ou (4, 3) etc.
```

### Flatten / Ravel (aplatir en 1D)

```python
z = np.array([[1, 2], [3, 4]])
z.flatten()  # Copie aplatie : array([1, 2, 3, 4])
z.ravel()    # Vue aplatie (pas de copie) : array([1, 2, 3, 4])
```

### Transpose (transposition)

```python
z = np.array([[1, 2, 3], [4, 5, 6]])
z.T          # Transpose : array([[1, 4],
             #                   [2, 5],
             #                   [3, 6]])
z.transpose()  # Méthode équivalente
```

**Schéma de transposition :**
```
Original (2×3) :          Transposé (3×2) :
┌───────────┐             ┌─────┐
│ 1  2  3   │      .T     │ 1 4 │
│ 4  5  6   │    ────→    │ 2 5 │
└───────────┘             │ 3 6 │
                          └─────┘
```

### Ajouter des dimensions

```python
z = np.array([1, 2, 3])
z[np.newaxis, :]    # Ajouter une dimension : shape (1, 3)
z[:, np.newaxis]    # Ajouter une colonne : shape (3, 1)
# ou plus simple :
np.expand_dims(z, 0)  # Shape (1, 3)
np.expand_dims(z, 1)  # Shape (3, 1)
```

---

## Opérations mathématiques

### Opérations élément par élément

```python
a_array = np.array([1, 2, 3, 4, 5])
b_array = np.array([6, 7, 8, 9, 10])

# Addition élément par élément
a_array + b_array
# Résultat : array([ 7,  9, 11, 13, 15])

# Soustraction
a_array - b_array
# Résultat : array([-5, -5, -5, -5, -5])

# Multiplication élément par élément
a_array * b_array
# Résultat : array([ 6, 14, 24, 36, 50])

# Division élément par élément
a_array / b_array
# Résultat : array([0.16666667, 0.28571429, 0.375, ...])

# Puissance
a_array ** 2
# Résultat : array([ 1,  4,  9, 16, 25])
```

### Opérations avec un scalaire (broadcasting)

```python
a_array = np.array([1, 2, 3, 4, 5])

a_array + 30
# Résultat : array([31, 32, 33, 34, 35])

a_array * 10
# Résultat : array([10, 20, 30, 40, 50])
```

### Produit matriciel (dot product)

```python
a_array = np.array([1, 2, 3, 4, 5])
b_array = np.array([6, 7, 8, 9, 10])

a_array @ b_array  # Produit scalaire : 1×6 + 2×7 + ... + 5×10 = 130
# ou
np.dot(a_array, b_array)  # Méthode équivalente
```

### Fonctions mathématiques universelles (ufunc)

```python
z = np.array([0, np.pi/2, np.pi])

np.sin(z)    # Sinus : array([0., 1., 0.])
np.cos(z)    # Cosinus
np.exp(z)    # Exponentielle
np.log(z)    # Logarithme naturel
np.sqrt(z)   # Racine carrée
np.abs(z)    # Valeur absolue
```

**Application sur une image :**
```python
from skimage import io
photo = io.imread('numpy_photo.jpeg')

# Appliquer une fonction mathématique à tous les pixels
photo_sin = np.sin(photo)
# ⚠️ Attention : les valeurs seront entre -1 et 1
```

---

## Opérations statistiques

### Fonctions de réduction

```python
# Exemple avec une image (array 3D)
photo = io.imread('numpy_photo.jpeg')

np.sum(photo)      # Somme de tous les éléments : 275190438
np.prod(photo)     # Produit de tous les éléments : 0 (dépassement)
np.mean(photo)     # Moyenne : 102.60642729306488
np.std(photo)      # Écart-type : 74.53745806863955
np.var(photo)      # Variance : 5555.8326553342
np.min(photo)      # Valeur minimale : 0
np.max(photo)      # Valeur maximale : 255
np.argmin(photo)   # Indice du minimum : 0
np.argmax(photo)   # Indice du maximum : 4674
```

### Réduction par axe (axis)

```python
z = np.array([[1, 2, 3], [4, 5, 6]])

np.sum(z, axis=0)  # Somme par colonne : array([5, 7, 9])
np.sum(z, axis=1)  # Somme par ligne : array([6, 15])

np.mean(z, axis=0) # Moyenne par colonne
np.mean(z, axis=1) # Moyenne par ligne
```

**Schéma de réduction par axe :**
```
Array (2×3) :          axis=0 (colonnes)    axis=1 (lignes)
┌───────────┐          ┌───────┐            ┌──────┐
│ 1  2  3   │  sum →   │ 5 7 9 │            │  6   │
│ 4  5  6   │          └───────┘            │ 15   │
└───────────┘                               └──────┘
```

### Tri

```python
x = np.array([3, 2, 1, 5, 4])
np.sort(x)          # Tri croissant : array([1, 2, 3, 4, 5])
x.sort()            # Tri en-place (modifie x)

# Indices de tri
np.argsort(x)       # array([2, 1, 0, 4, 3]) - indices qui donneraient le tri
```

---

## Opérations booléennes et masking

### Comparaisons (retournent des arrays booléens)

```python
z = np.array([1, 2, 3,  нескольких, 5, 6, 7, 8, 9, 10])

z < 3       # array([True, True, False, False, False, ...])
z > 3       # array([False, False, False, True, True, ...])
z == 5      # array([False, False, False, False, True, False, ...])
z != 0      # array([True, True, True, True, True, ...])
```

### Indexing booléen (masking)

```python
z = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Sélectionner uniquement les éléments > 3
z[z > 3]
# Résultat : array([4, 5, 6, 7, 8, 9, 10])

# Conditions multiples
z[(z > 3) & (z < 8)]  # ET logique : array([4, 5, 6, 7])
z[(z < 3) | (z > 8)]  # OU logique : array([1, 2, 9, 10])
z[~(z == 5)]          # NOT logique : tous sauf 5
```

**⚠️ Important :** Utiliser `&`, `|`, `~` au lieu de `and`, `or`, `not` avec NumPy.

### np.where (remplacement conditionnel)

```python
photo = io.imread('numpy_photo.jpeg')

# Remplace les valeurs > 100 par 255, sinon 0 (seuillage)
photo_masked = np.where(photo > 100, 255, 0)
# Syntaxe : np.where(condition, valeur_si_vrai, valeur_si_faux)

# Version plus complexe
result = np.where(z > 5, z * 2, z / 2)  # Double si > 5, divise par 2 sinon
```

**Schéma du masking :**
```
Original :          Condition :          Résultat :
[1, 2, 3, 4, 5]    [T, T, F, F, F]      [1, 2, _, _, _]
                                ↓
                     z[z > 3] = [4, 5]
```

### Any et All

```python
z = np.array([1, 2, 3, 4, 5])

np.any(z > 4)    # True si au moins un élément > 4 : True
np.all(z > 0)    # True si tous les éléments > 0 : True
```

---

## Broadcasting

Le broadcasting permet d'appliquer des opérations entre arrays de shapes différentes.

```python
# Exemple 1 : Array 1D + Scalar
a = np.array([1, 2, 3])
a + 10  # Broadcast : [11, 12, 13]

# Exemple 2 : Array 2D + Array 1D
a = np.array([[1, 2, 3], [4, 5, 6]])  # Shape (2, 3)
b = np.array([10, 20, 30])             # Shape (3,)
a + b  # Broadcast b sur chaque ligne de a
# Résultat : array([[11, 22, 33],
#                   [14, 25, 36]])

# Exemple 3 : Array 2D + Array colonne
a = np.array([[1, 2], [3, 4]])  # Shape (2, 2)
b = np.array([10, 20])           # Shape (2,)
b = b[:, np.newaxis]             # Shape (2, 1)
a + b  # Broadcast sur les colonnes
```

**Règles du broadcasting :**
1. Les dimensions de taille 1 sont "étendues" pour correspondre
2. La dimension manquante au début est ajoutée automatiquement
3. Les shapes doivent être compatibles

**Schéma du broadcasting :**
```
Array (3×1) + Array (1×4) = Array (3×4)

[10]        [1, 2, 3, 4]
[20]    +                = 
[30]       

┌─────────────┐
│ 11 12 13 14 │
│ 21 22 23 24 │
│ 31 32 33 34 │
└─────────────┘
```

---

## Manipulation d'images

Les images sont des arrays NumPy ! Une image RGB a typiquement la shape `(hauteur, largeur, 3)`.

### Charger une image

```python
from skimage import io
import matplotlib.pyplot as plt

photo = io.imread('numpy_photo.jpeg')
type(photo)    # <class 'numpy.ndarray'>
photo.shape    # Exemple : (500, 800, 3) pour une image 500×800 RGB
```

### Afficher une image

```python
plt.imshow(photo)
plt.show()
```

### Opérations de slicing sur images

```python
# Retourner verticalement (miroir haut/bas)
plt.imshow(photo[::-1])  # Inverse l'ordre des lignes

# Retourner horizontalement (miroir gauche/droite)
plt.imshow(photo[:, ::-1])  # Inverse l'ordre des colonnes

# Rogner (crop) : lignes 50-500, colonnes 800-1100
plt.imshow(photo[50:500, 800:1100])

# Sous-échantillonnage : 1 pixel sur 10 en hauteur, 1 sur 3 en largeur
plt.imshow(photo[::10, ::3])  # Réduit la résolution
```

**Schéma d'une image NumPy :**
```
Image RGB (500×800×3) :

photo[hauteur, largeur, canal]
         ↓        ↓       ↓
    ┌────────────┐
    │            │ ← ligne 0 (photo[0, :, :])
    │   Image    │ ← ligne 50
    │            │ ← ligne 500
    └────────────┘
       colonnes 0-800

Canaux : 0 = Rouge, 1 = Vert, 2 = Bleu
photo[:, :, 0] = canal rouge uniquement
```

### Transposition d'une image

```python
# Transposer le canal rouge
plt.imshow(photo[:,:,0].T)  # .T échange lignes et colonnes
```

---

## Méthodes utiles supplémentaires

### Copie vs Vue

```python
z = np.array([1, 2, 3, 4, 5])

# Vue (référence) - modifie l'original
z_view = z[:]
z_view[0] = 99
print(z)  # [99, 2, 3, 4, 5] ← z est modifié !

# Copie (indépendante)
z_copy = z.copy()
z_copy[0] = 100
print(z)  # [99, 2, 3, 4, 5] ← z non modifié
```

### Concatenation et stacking

```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

np.concatenate([a, b])  # array([1, 2, 3, 4, 5, 6])

# Stacking (ajouter une dimension)
np.stack([a, b])        # array([[1, 2, 3],
                        #        [4, 5, 6]])
np.vstack([a, b])       # Stack vertical (même résultat)
np.hstack([a, b])       # Stack horizontal : array([1, 2, 3, 4, 5, 6])
```

### Trouver des éléments

```python
z = np.array([1, 2, 3, 4, 5, 4, 3, 2, 1])

np.where(z == 3)        # Indices où z == 3 : (array([2, 6]),)
np.argwhere(z == 3)     # Indices compacts : array([[2], [6]])
np.nonzero(z > 3)       # Équivalent à np.where(z > 3)
```

### Opérations sur les axes

```python
z = np.array([[1, 2, 3], [4, 5, 6]])

# Ajouter une dimension
np.expand_dims(z, 0)     # Shape (1, 2, 3)
np.expand_dims(z, 1)     # Shape (2, 1, 3)

# Supprimer les dimensions de taille 1
z = np.array([[[1], [2], [3]]])
np.squeeze(z)            # array([1, 2, 3])

# Permuter les axes
z = np.ones((2, 3, 4))
z.swapaxes(0, 2)         # Échange l'axe 0 et 2 : shape (4, 3, 2)
```

### Opérations de base avancées

```python
z = np.array([1, 2, 3, 4, 5])

np.cumsum(z)    # Somme cumulative : array([1, 3, 6, 10, 15])
np.cumprod(z)   # Produit cumulative : array([1, 2, 6, 24, 120])
np.diff(z)      # Différences : array([1, 1, 1, 1])
np.gradient(z)  # Gradient (dérivée discrète)
```

### Opérations matricielles

```python
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

np.dot(a, b)         # Produit matriciel
a @ b                # Syntaxe moderne (produit matriciel)
np.matmul(a, b)      # Produit matriciel
np.linalg.inv(a)     # Inverse de la matrice
np.linalg.det(a)     # Déterminant
np.linalg.eig(a)     # Valeurs propres et vecteurs propres
```

### Utilitaires

```python
# Vérifier si un array est vide
z = np.array([])
z.size == 0          # True

# Remplacer certaines valeurs
z = np.array([1, 2, 3, np.nan, 5])
np.nan_to_num(z)     # Remplace NaN par 0

# Arrondir
z = np.array([1.7, 2.3, 3.8])
np.round(z)          # array([2., 2., 4.])
np.floor(z)          # array([1., 2., 3.]) - arrondi vers le bas
np.ceil(z)           # array([2., 3., 4.]) - arrondi vers le haut

# Clipping (limiter les valeurs)
z = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
np.clip(z, 3, 7)     # Limite entre 3 et 7 : array([3, 3, 3, 4, 5, 6, 7, 7, 7, 7])
```

### Opérations de comparaison avancées

```python
a = np.array([1, 2, 3])
b = np.array([1, 2, 4])

np.array_equal(a, b)     # False - comparaison exacte
np.allclose(a, b, atol=1) # True - comparaison avec tolérance
np.isclose(a, b)         # array([True, True, False])
```

### Séparation des arrays

```python
z = np.arange(12).reshape(3, 4)
# array([[ 0,  1,  2,  3],
#        [ 4,  5,  6,  7],
#        [ 8,  9, 10, 11]])

np.split(z, 3)           # Divise en 3 parties selon l'axe 0
np.split(z, 2, axis=1)   # Divise en 2 parties selon l'axe 1
np.vsplit(z, 3)          # Division verticale
np.hsplit(z, 2)          # Division horizontale
```

---

## Récapitulatif des conventions importantes

### Syntaxe de base

| Opération | Syntaxe |
|-----------|---------|
| Import | `import numpy as np` |
| Création 1D | `np.array([1, 2, 3])` |
| Création 2D | `np.array([[1, 2], [3, 4]])` |
| Zéros | `np.zeros(shape)` |
| Uns | `np.ones(shape)` |
| Séquences | `np.arange(début, fin, pas)` ou `np.linspace(début, fin, nb)` |

### Indexing

| Syntaxe | Description |
|---------|-------------|
| `z[0]` | Premier élément |
| `z[-1]` | Dernier élément |
| `z[1:5]` | Slice (indices 1 à 4) |
| `z[::2]` | Tous les 2 éléments |
| `z[::-1]` | Inverse |
| `z[condition]` | Indexing booléen |

### Opérations booléennes

| Opérateur NumPy | Équivalent Python |
|----------------|-------------------|
| `&` | `and` |
| `\|` | `or` |
| `~` | `not` |

### Axes

- `axis=0` : opération sur les lignes (résultat par colonne)
- `axis=1` : opération sur les colonnes (résultat par ligne)
- `axis=-1` : dernier axe

---

## Ressources supplémentaires

- **Documentation officielle** : https://numpy.org/doc/
- **Guide de référence** : https://numpy.org/doc/stable/reference/
- **Tutoriels** : https://numpy.org/doc/stable/user/

---

*Document créé pour servir de pense-bête NumPy - Mise à jour régulière recommandée*