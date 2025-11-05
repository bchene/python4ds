# Comprendre les Arrays NumPy pour les Images

NumPy est la bibliothèque fondamentale pour le calcul scientifique en Python. Son objet principal est le `numpy.ndarray` (un *n-dimensional array*), qui est une grille de valeurs, toutes du même type.

Pour les images, c'est parfait :
* Une image en **niveaux de gris** est un *array* 2D : `(hauteur, largeur)`
* Une image en **couleur (RGB)** est un *array* 3D : `(hauteur, largeur, 3)` (3 *channels* : Rouge, Vert, Bleu).
* Une image en **couleur (RGBA)** est un *array* 3D : `(hauteur, largeur, 4)` (avec un *channel* Alpha pour la transparence).



## 1. Matrices : Inspection et Conversion

L'inspection (vérifier la forme) et la conversion (changer la forme ou le type) sont les opérations de base.

### Attributs d'inspection clés

Les attributs (on y accède avec `.`) vous renseignent sur votre *array*.

| Attribut | Description | Exemple |
| --- | --- | --- |
| **`.shape`** | Le plus important. Un *tuple* indiquant la taille de chaque dimension. | `(480, 640, 3)` (une image de 640x480 RGB) |
| **`.dtype`** | Le type de données (`data type`) des éléments. | `uint8` (entier 0-255, standard pour les images) ou `float64` (pour les calculs) |
| **`.ndim`** | Le nombre de dimensions (*axes*). | `3` pour une image couleur, `2` pour du N&B. |
| **`.size`** | Le nombre total d'éléments (pixels * channels). | `480 * 640 * 3 = 921600` |

### Fonctions de conversion clés

| Fonction | Description | Exemple |
| --- | --- | --- |
| **`np.reshape()`** | Change la forme de l'*array* sans changer ses données. | `img_1d = img.reshape((480 * 640 * 3))` (Aplatir l'image) |
| **`.astype()`** | Convertit l'*array* dans un nouveau type. | `img_float = img.astype(np.float64)` (Pour faire des calculs précis) |
| **`np.array()`** | Convertit une liste Python standard en *array* NumPy. | `arr = np.array([[1, 2], [3, 4]])` |

---

## 2. Le Slicing (Découpage)

Le *slicing* est la manière de sélectionner des parties d'un *array*. C'est la partie la plus puissante de NumPy.

La syntaxe de base pour une dimension est : `[start:stop:step]`
* `start` : L'index de début (inclus). Si omis, commence à 0.
* `stop` : L'index de fin (**exclu**). Si omis, va jusqu'à la fin.
* `step` : Le "pas" (saut). Si omis, vaut 1.



Pour les images (3D), on applique cette syntaxe à chaque dimension, séparée par des virgules :
`image[ slice_hauteur, slice_largeur, slice_channels ]`

### Exemples de Slicing

Imaginons une image `img` de forme `(100, 200, 3)` (100 pixels de haut, 200 de large, 3 canaux).

* **`img[:, :, :]`**
    * Signification : "Prendre tout." C'est une copie de l'image.

* **`img[10:20, 30:50, :]`**
    * Signification : "Prendre les lignes 10 à 19, les colonnes 30 à 49, et tous les canaux."
    * Résultat : Un "crop" (rognage) de l'image.

* **`img[:, :, 0]`**
    * Signification : "Prendre toutes les lignes, toutes les colonnes, mais **uniquement** le canal d'index 0 (Rouge)."
    * Résultat : Une *array* 2D contenant seulement le canal rouge.

* **`img[::2, ::2, :]`**
    * Signification : "Prendre 1 pixel sur 2 en hauteur, 1 pixel sur 2 en largeur."
    * Résultat : Réduire la taille de l'image de moitié (sous-échantillonnage).

### Le cas `[::-1]` (Inversion)

Le `step` négatif (comme `-1`) inverse l'ordre.

* **`img[::-1, :, :]`** ou **`img[::-1]`** (les `:, :` sont implicites)
    * Signification : "Inverser l'ordre des lignes (axe 0)."
    * Résultat : Un **retournement vertical** de l'image (la tête en bas).

* **`img[:, ::-1, :]`**
    * Signification : "Inverser l'ordre des colonnes (axe 1)."
    * Résultat : Un **retournement horizontal** de l'image (effet miroir).

* **`img[:, :, ::-1]`**
    * Signification : "Inverser l'ordre des canaux."
    * Résultat : L'image passe de **RGB à BGR**. Très utile pour des bibliothèques comme OpenCV qui utilisent BGR par défaut.

---

## 3. Fonctions NumPy Utiles

Voici une liste des fonctions et attributs les plus utilisés, classés par thème.

### Thème 1 : Création d'Arrays

* **NOM**
    `np.array`
* **Prototype**
    `np.array(object, dtype=None)`
* **Description**
    Crée un *array* à partir d'une liste (ou objet similaire).
* **Exemple**
    ```python
    a = np.array([[1, 2], [3, 4]])
    # Résultat:
    # [[1 2]
    #  [3 4]]
    ```

* **NOM**
    `np.zeros` / `np.ones`
* **Prototype**
    `np.zeros(shape, dtype=float)`
* **Description**
    Crée un *array* rempli de 0 (ou de 1) de la forme (`shape`) donnée.
* **Exemple**
    ```python
    black_img = np.zeros((100, 100, 3), dtype=np.uint8)
    # Résultat: Une image noire de 100x100
    ```

* **NOM**
    `np.arange`
* **Prototype**
    `np.arange(start, stop, step)`
* **Description**
    Comme la fonction `range()` de Python, mais crée un *array* NumPy.
* **Exemple**
    ```python
    a = np.arange(0, 10, 2)
    # Résultat: [0 2 4 6 8]
    ```

### Thème 2 : Manipulation et Transformation

* **NOM**
    `.reshape` (Méthode) ou `np.reshape` (Fonction)
* **Prototype**
    `array.reshape(new_shape)`
* **Description**
    Change la forme d'un *array* sans changer les données.
* **Exemple**
    ```python
    a = np.arange(6) # [0 1 2 3 4 5]
    b = a.reshape((2, 3))
    # Résultat:
    # [[0 1 2]
    #  [3 4 5]]
    ```

* **NOM**
    `.T` (Attribut)
* **Prototype**
    `array.T`
* **Description**
    La **Transposée** de l'*array*. Inverse les axes (les lignes deviennent des colonnes).
* **Exemple**
    ```python
    a = np.array([[1, 2], [3, 4]])
    # [[1 2]
    #  [3 4]]
    print(a.T)
    # Résultat:
    # [[1 3]
    #  [2 4]]
    ```

* **NOM**
    `np.concatenate`
* **Prototype**
    `np.concatenate((a1, a2, ...), axis=0)`
* **Description**
    Assemble des *arrays* le long d'un axe existant.
* **Exemple**
    ```python
    # Pour des images (axis=1 : horizontalement)
    img_a = np.zeros((100, 50, 3))
    img_b = np.ones((100, 50, 3))
    combined = np.concatenate((img_a, img_b), axis=1)
    # Résultat: Une image de (100, 100, 3)
    ```

* **NOM**
    `np.stack` / `np.dstack`
* **Prototype**
    `np.stack((a1, a2, ...), axis=0)`
* **Description**
    Assemble des *arrays* le long d'un **nouvel** axe. `np.dstack` est un raccourci pour empiler sur le 3ème axe (utile pour combiner des canaux N&B en une image couleur).
* **Exemple**
    ```python
    r = np.zeros((100, 100)) # Canal Rouge
    g = np.zeros((100, 100)) # Canal Vert
    b = np.ones((100, 100))  # Canal Bleu (rempli de 1)
    img = np.dstack((r, g, b))
    # Résultat: Une image "bleue" de (100, 100, 3)
    ```

### Thème 3 : Opérations Mathématiques et Statistiques

**Note importante sur l'argument `axis` :**
Presque toutes ces fonctions acceptent un argument `axis`.
* `axis=0` : Calcule sur les **lignes**.
* `axis=1` : Calcule sur les **colonnes**.
* `axis=None` (défaut) : Calcule sur **tous** les éléments (renvoie un seul nombre).

* **NOM**
    `np.sum`
* **Prototype**
    `np.sum(array, axis=None)`
* **Description**
    Somme des éléments de l'*array*.
* **Exemple**
    ```python
    a = np.array([[1, 2], [3, 4]])
    print(np.sum(a)) # Résultat: 10
    print(np.sum(a, axis=0)) # Résultat: [4 6] (1+3 et 2+4)
    ```

* **NOM**
    `np.mean`
* **Prototype**
    `np.mean(array, axis=None)`
* **Description**
    Moyenne arithmétique des éléments.
* **Exemple**
    ```python
    # Obtenir la "couleur moyenne" d'une image
    img = np.array(...) # Forme (H, L, 3)
    mean_color = np.mean(img, axis=(0, 1))
    # Résultat: [moyenne_R, moyenne_G, moyenne_B]
    ```

* **NOM**
    `np.max` / `np.min`
* **Prototype**
    `np.max(array, axis=None)`
* **Description**
    Renvoie la valeur maximale (ou minimale) de l'*array*.
* **Exemple**
    ```python
    # Normaliser une image (la mettre entre 0.0 et 1.0)
    img_float = img.astype(np.float64)
    img_norm = img_float / np.max(img_float)
    ```

* **NOM**
    `np.std` / `np.var`
* **Prototype**
    `np.std(array, axis=None)`
* **Description**
    Calcule l'écart-type (*standard deviation*) ou la variance.
* **Exemple**
    ```python
    # Trouver le contraste d'une image N&B
    gray_img = np.array(...) # Forme (H, L)
    contraste = np.std(gray_img)
    # Résultat: Un nombre (si bas, l'image est "plate")
    ```

* **NOM**
    `np.clip`
* **Prototype**
    `np.clip(array, a_min, a_max)`
* **Description**
    "Écrête" les valeurs : tout ce qui est < `a_min` devient `a_min`, tout ce qui est > `a_max` devient `a_max`.
* **Exemple**
    ```python
    # Garder les pixels entre 0 et 255 après une opération
    img_brighter = img * 1.5 # Peut dépasser 255
    img_safe = np.clip(img_brighter, 0, 255)
    ```
