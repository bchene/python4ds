# <span style="color:#FFC300">Bibliothèques fondamentales python pour la data science</span>


* **NumPy** : C'est le **moteur** et la **matière première**. Il fournit les tableaux (`arrays`) rapides et les fonctions mathématiques.
* **Pandas** : C'est **l'atelier** ou la **feuille de calcul** (type Excel) pour les données. Il utilise NumPy sous le capot pour organiser les données dans des `DataFrames` faciles à manipuler.
* **Matplotlib** : C'est la **toile** et les **crayons**. C'est la bibliothèque de base, puissante mais parfois complexe, pour *dessiner* n'importe quel graphique.
* **Seaborn** : C'est le **kit de décoration de luxe**. Il est construit *sur* Matplotlib et vous permet de créer des graphiques statistiques magnifiques en très peu de lignes de code.

---

## 🔢 NumPy (Numerical Python)

**Description Globale :** C'est la fondation absolue du calcul scientifique en Python. NumPy fournit un objet essentiel : le `ndarray` (ou *array*). C'est un tableau (une matrice) N-dimensionnel ultra-rapide pour les opérations mathématiques. Pandas est construit *sur* NumPy.

**Votre cas d'utilisation : "Afficher des images" se fait avec NumPy. Une image est simplement un `array` 3D (hauteur, largeur, couleur).**



### Fonctionnalités Clés

* **`np.array([...])`** : Crée un `array` NumPy à partir d'une liste Python.
* **`array.shape`** : L'attribut le plus important. Donne la forme de la matrice (ex: `(480, 640, 3)` pour une image).
* **`array.dtype`** : Donne le type de données (ex: `uint8` pour les pixels, `float64` pour les calculs).
* **`array.reshape(...)`** : Modifie la forme de la matrice sans changer les données.
* **Slicing (`array[::, 0]` ...)** : Sélectionne des parties de la matrice (voir notre discussion précédente).
* **Vectorisation (ex: `array * 2`)** : Applique une opération à *tous* les éléments sans boucle `for` (c'est ce qui le rend rapide).
* **`np.zeros()` / `np.ones()`** : Crée des matrices remplies de 0 ou de 1.
* **`np.mean()` / `np.sum()` / `np.std()`** : Calcule la moyenne, la somme, l'écart-type (très rapide).

---

## 📊 Pandas

**Description Globale :** C'est votre couteau suisse pour la manipulation de données. Pandas est conçu pour lire, nettoyer, transformer et analyser des données tabulaires (comme des CSV ou des tables SQL). Ses deux objets principaux sont le `DataFrame` (un tableau à 2 dimensions, comme une feuille Excel) et la `Series` (une colonne de ce tableau).

**Votre cas d'utilisation : "Lire et vérifier des CSV" est la spécialité de Pandas.**



### Fonctionnalités Clés

* **`pd.read_csv("fichier.csv")`** : Lit un fichier CSV et le charge dans un `DataFrame`.
* **`df.head()` / `df.tail()`** : Affiche les 5 premières / dernières lignes pour inspecter les données.
* **`df.info()`** : Donne un résumé technique (types de données, valeurs manquantes).
* **`df.describe()`** : Fournit des statistiques rapides (moyenne, médiane, min, max...) sur les colonnes numériques.
* **`df['nom_colonne']`** : Sélectionne une colonne (une `Series`).
* **`df.loc[]` / `df.iloc[]`** : Sélectionne des lignes/colonnes par leur nom (`loc`) ou leur position d'index (`iloc`).
* **`df.dropna()` / `df.fillna()`** : Supprime ou remplit les valeurs manquantes (*missing values*).
* **`df.groupby("colonne")`** : Regroupe les données pour effectuer des agrégations (somme, moyenne...).
* **`df.plot()`** : Une interface simple pour créer des graphiques de base (utilise Matplotlib en arrière-plan).

---

## 📈 Matplotlib

**Description Globale :** C'est la bibliothèque "mère" de la visualisation de données (*data visualization* ou *dataviz*) en Python. Elle est extrêmement puissante et vous donne un contrôle total sur chaque aspect de votre graphique (la toile, les axes, les titres, les légendes...). Elle peut être complexe pour des graphiques avancés.

**Votre cas d'utilisation : C'est la bibliothèque qui *dessine* les `arrays` NumPy (images) et les `DataFrames` Pandas (graphiques).**

### Fonctionnalités Clés

* **`plt.figure()` / `plt.subplots()`** : Crée une "toile" et un ou plusieurs "axes" (zones de dessin).
* **`plt.plot(x, y)`** : Le graphique de base (lignes).
* **`plt.scatter(x, y)`** : Nuage de points (*scatter plot*).
* **`plt.bar(x, hauteur)`** : Diagramme en barres.
* **`plt.hist(donnees)`** : Histogramme (très utile pour voir la distribution).
* **`plt.imshow(array_image)`** : La fonction clé pour **afficher une image** (un `array` NumPy).
* **`plt.title()` / `plt.xlabel()` / `plt.legend()`** : Ajoute des étiquettes et une légende.
* **`plt.show()`** : Affiche le graphique final.

---

## ✨ Seaborn

**Description Globale :** Seaborn est une bibliothèque de *dataviz* statistique construite *sur* Matplotlib. Elle est conçue pour fonctionner parfaitement avec les `DataFrames` Pandas. Son but est de rendre des graphiques complexes (comme des *heatmaps* ou des régressions) très simples à créer et esthétiquement agréables par défaut.

**Votre cas d'utilisation : Quand vous voulez comprendre des relations dans vos données Pandas sans effort.**

### Fonctionnalités Clés

* **`sns.set_theme()`** : Change instantanément le style de *tous* vos graphiques Matplotlib/Seaborn.
* **`sns.scatterplot(data=df, x=..., y=..., hue=...)`** : Un nuage de points amélioré où la couleur (`hue`) peut représenter une 3e variable.
* **`sns.histplot(data=df, x=...)`** : Un histogramme amélioré.
* **`sns.boxplot()` / `sns.violinplot()`** : Visualise les distributions et les *outliers*.
* **`sns.heatmap(df.corr())`** : Une carte de chaleur. Parfait pour visualiser les corrélations.
* **`sns.pairplot(df)`** : Un graphique "magique" qui croise toutes les variables de votre `DataFrame` entre elles.
* **`sns.lmplot(data=df, x=..., y=...)`** : Affiche un nuage de points *plus* une ligne de régression linéaire.

---

## 🚀 Les Bibliothèques Essentielles à Ajouter

Vous avez raison, il en manque. Voici les deux ajouts les plus importants pour un débutant.

### 1. Scikit-learn (sklearn)

**Description Globale :** C'est la bibliothèque de référence pour le **Machine Learning**. Une fois vos données nettoyées avec Pandas et visualisées avec Seaborn, *sklearn* vous permet de *construire des modèles* (prédiction, classification, etc.). Elle est incroyablement bien conçue, cohérente et robuste.

#### Fonctionnalités Clés

* **`train_test_split()`** : La fonction la plus importante. Sépare vos données en un set d'entraînement (*train*) et un set de test.
* **`LinearRegression()` / `LogisticRegression()`** : Modèles de base pour la régression (prédire un nombre) et la classification (prédire une catégorie).
* **`KMeans()`** : Modèle de *clustering* (regrouper les données qui se ressemblent).
* **`model.fit(X_train, y_train)`** : La commande universelle pour **entraîner** n'importe quel modèle.
* **`model.predict(X_test)`** : La commande universelle pour **prédire** sur de nouvelles données.
* **`accuracy_score()` / `confusion_matrix()`** : Outils pour évaluer la performance de votre modèle.
* **`StandardScaler()`** : Un "pré-processeur" essentiel pour normaliser vos données avant de les donner au modèle.

### 2. Jupyter (Notebook / Lab)

**Description Globale :** Ce n'est pas une *bibliothèque* au sens strict, mais c'est **l'environnement de travail** (IDE) dans lequel tout ce qui précède s'exécute. C'est un "carnet de laboratoire" interactif qui vous permet de mélanger du code exécutable, des visualisations, des équations et du texte explicatif (Markdown) dans un seul document. C'est l'outil standard de la *data science*.

#### Fonctionnalités Clés

* **Cellules de code** : Permettent d'écrire et d'exécuter du code Python de manière interactive.
* **Cellules Markdown** : Permettent d'écrire du texte, de prendre des notes et de documenter votre analyse.
* **Sortie intégrée** : Les `DataFrames` Pandas, les graphiques Matplotlib et les résultats s'affichent directement sous la cellule de code.