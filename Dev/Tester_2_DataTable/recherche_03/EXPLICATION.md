# Explication détaillée du programme `projection_life_correlation.py`

Ce document explique en détail le fonctionnement du programme qui analyse la corrélation entre l'espérance de vie et le niveau de vie (PIB par habitant) des pays.

---

## 📋 Table des matières

1. [Chargement des données avec Pandas](#1-chargement-des-données-avec-pandas)
2. [Les DataFrames Pandas](#2-les-dataframes-pandas)
3. [L'affichage du scatter plot](#3-laffichage-du-scatter-plot)
4. [La fonction de corrélation](#4-la-fonction-de-corrélation)

---

## 1. Chargement des données avec Pandas

### 1.1 La fonction `load()`

```python
life_expect_ds = load("life_expectancy_years.csv")
income_ds = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
```

La fonction `load()` (importée depuis `ex00.load_csv`) charge un fichier CSV et le convertit en **DataFrame Pandas**.

### 1.2 Qu'est-ce qu'un fichier CSV ?

Un fichier CSV (Comma-Separated Values) est un format de fichier texte où :
- Chaque ligne représente une **ligne de données**
- Les colonnes sont séparées par des **virgules** (ou points-virgules)
- La première ligne contient généralement les **noms des colonnes** (en-têtes)

**Exemple de structure CSV :**
```
country,1800,1801,1802,...
Afghanistan,28.2,28.2,28.2,...
Albania,35.4,35.4,35.4,...
...
```

### 1.3 Comment Pandas lit un CSV

Quand vous appelez `pd.read_csv("fichier.csv")` (utilisé dans la fonction `load()`), Pandas :
1. **Ouvre le fichier** et lit son contenu
2. **Identifie automatiquement** les colonnes (première ligne = en-têtes)
3. **Crée un DataFrame** avec :
   - Les noms de colonnes comme en-têtes
   - Chaque ligne du CSV devient une ligne du DataFrame
   - Les valeurs sont automatiquement typées (nombres, textes, etc.)

**Résultat :** Un objet DataFrame prêt à être manipulé en Python !

---

## 2. Les DataFrames Pandas

### 2.1 Qu'est-ce qu'un DataFrame ?

Un **DataFrame** est une structure de données bidimensionnelle (comme un tableau Excel) qui contient :
- **Des lignes** : chaque ligne représente un enregistrement (ex: un pays)
- **Des colonnes** : chaque colonne représente une variable (ex: année, espérance de vie)
- **Un index** : numéro ou label identifiant chaque ligne (par défaut : 0, 1, 2, ...)

**Représentation visuelle :**

```
         country    1800    1801    1802    ...
0    Afghanistan    28.2    28.2    28.2    ...
1        Albania    35.4    35.4    35.4    ...
2        Algeria    28.8    28.8    28.8    ...
...
```

### 2.2 Accéder aux données d'un DataFrame

#### A. Accéder à une colonne

```python
# Méthode 1 : notation avec crochets (comme un dictionnaire)
df['country']          # Retourne une Series (colonne complète)
df['1800']             # Retourne la colonne de l'année 1800

# Méthode 2 : notation avec point (si le nom de colonne est valide)
df.country             # Équivalent à df['country']
```

**Exemple :**
```python
life_expect_ds['country']  # Tous les noms de pays
life_expect_ds['1900']     # Toutes les espérances de vie en 1900
```

#### B. Accéder à une ligne spécifique

```python
# Par index numérique
df.iloc[0]             # Première ligne (index 0)
df.iloc[5]             # Sixième ligne (index 5)

# Par label d'index (si l'index a été modifié)
df.loc['France']       # Ligne avec l'index 'France'
```

#### C. Accéder à une valeur spécifique (ligne + colonne)

```python
# Méthode 1 : iloc (index numérique)
df.iloc[0, 1]          # Ligne 0, colonne 1
df.iloc[5, 2]          # Ligne 5, colonne 2

# Méthode 2 : loc (label d'index)
df.loc['France', '1900']  # Valeur pour France en 1900
```

### 2.3 Modifier l'index : `set_index()`

```python
life_expect_indexed = life_expect_ds.set_index('country')
```

**Avant `set_index('country')` :**
```
         country    1800    1801    ...
0    Afghanistan    28.2    28.2    ...
1        Albania    35.4    35.4    ...
```

**Après `set_index('country')` :**
```
                 1800    1801    ...
country                          
Afghanistan     28.2    28.2    ...
Albania         35.4    35.4    ...
```

**Pourquoi utiliser `set_index()` ?**
- Permet d'accéder aux lignes par **nom de pays** au lieu d'un numéro
- Plus lisible : `df.loc['France', '1900']` au lieu de `df.iloc[42, 1]`
- Plus sûr : le nom du pays ne change pas même si l'ordre des lignes change

### 2.4 Accès avec `.loc[]` dans le programme

```python
life = life_expect_indexed.loc[country, year_str]
income = income_indexed.loc[country, year_str]
```

**Explication :**
- `life_expect_indexed.loc[country, year_str]` :
  - Cherche la **ligne** avec l'index = `country` (ex: "France")
  - Cherche la **colonne** avec le nom = `year_str` (ex: "1900")
  - Retourne la **valeur** à l'intersection

**Exemple concret :**
```python
# Si country = "France" et year_str = "1900"
life = life_expect_indexed.loc["France", "1900"]
# Retourne : 45.3 (espérance de vie de la France en 1900)
```

### 2.5 Filtrer les données : trouver les pays communs

```python
common_countries = (set(life_expect_ds['country']) &
                    set(income_ds['country']))
```

**Explication :**
1. `life_expect_ds['country']` : récupère tous les pays du premier DataFrame
2. `set(...)` : convertit en ensemble (set) pour les opérations d'intersection
3. `&` : opérateur d'**intersection** (pays présents dans les deux DataFrames)
4. Résultat : un ensemble contenant uniquement les pays présents dans **les deux** fichiers

**Pourquoi c'est important ?**
- Pour calculer la corrélation, il faut que chaque pays ait **à la fois** :
  - Une valeur d'espérance de vie
  - Une valeur de revenu
- On ne peut analyser que les pays présents dans les deux datasets

---

## 3. L'affichage du scatter plot

### 3.1 Qu'est-ce qu'un scatter plot ?

Un **scatter plot** (nuage de points) est un graphique qui affiche des points dans un espace 2D :
- **Axe X (abscisse)** : variable indépendante (revenu/PIB)
- **Axe Y (ordonnée)** : variable dépendante (espérance de vie)
- **Chaque point** : représente un pays avec ses deux valeurs

### 3.2 Création des listes de données

```python
life_list = []      # Liste pour stocker les espérances de vie
income_list = []    # Liste pour stocker les revenus

for country in common_countries:
    # ... extraction des valeurs ...
    life_list.append(life_float)
    income_list.append(income_int)
```

**Processus :**
1. On itère sur chaque pays commun
2. On extrait les valeurs pour ce pays et cette année
3. On ajoute ces valeurs aux listes correspondantes
4. **Important** : l'ordre est préservé → `life_list[i]` et `income_list[i]` correspondent au même pays

### 3.3 Affichage avec `plt.scatter()`

```python
plt.scatter(income_list, life_list)
```

**Paramètres :**
- `income_list` : valeurs pour l'axe X (revenu)
- `life_list` : valeurs pour l'axe Y (espérance de vie)

**Résultat :** Un nuage de points où chaque point = un pays

### 3.4 Configuration de l'axe logarithmique

```python
plt.xscale('log')
plt.xticks([300, 1e3, 1e4], ['300', '1k', '10k'])
```

**Pourquoi une échelle logarithmique ?**
- Les revenus varient énormément : de 300$ à 10 000$+
- Sur une échelle linéaire, les pays pauvres seraient tous regroupés à gauche
- L'échelle **logarithmique** permet de mieux visualiser les différences à toutes les échelles

**Comment ça marche ?**
- Au lieu de placer les valeurs à leur position réelle (300, 1000, 10000)
- On place les valeurs à la position de leur **logarithme** (log10(300), log10(1000), log10(10000))
- Résultat : les distances sont proportionnelles aux **ratios** plutôt qu'aux différences

**Exemple :**
- Sur échelle linéaire : distance entre 1000 et 2000 = distance entre 9000 et 10000
- Sur échelle log : distance entre 1000 et 2000 = distance entre 5000 et 10000 (même ratio ×2)

---

## 4. La fonction de corrélation

### 4.1 Vue d'ensemble

La fonction `correlation_curve()` calcule et affiche une **droite de régression linéaire** qui représente la tendance générale entre revenu et espérance de vie.

**Objectif :** Répondre à la question : "Quelle est la relation mathématique entre le revenu et l'espérance de vie ?"

### 4.2 Théorie : La régression linéaire

#### A. Qu'est-ce qu'une régression linéaire ?

Une régression linéaire cherche à trouver la **meilleure droite** qui passe "au plus près" de tous les points.

**Équation d'une droite :**
```
y = a × x + b
```

Où :
- `a` = **pente** (slope) : indique si y augmente ou diminue avec x
- `b` = **ordonnée à l'origine** (intercept) : valeur de y quand x = 0

#### B. La méthode des moindres carrés

Pour trouver la "meilleure" droite, on utilise la **méthode des moindres carrés** :
1. On calcule la distance verticale entre chaque point et la droite
2. On élève ces distances au carré (pour éviter les négatifs)
3. On trouve la droite qui **minimise la somme de ces carrés**

**Formule mathématique :**

Pour une droite `y = ax + b`, les coefficients sont :

```
a = Σ(xi - x̄)(yi - ȳ) / Σ(xi - x̄)²
b = ȳ - a × x̄
```

Où :
- `xi`, `yi` = valeurs individuelles
- `x̄`, `ȳ` = moyennes de x et y
- `Σ` = somme

### 4.3 Pratique : Implémentation avec NumPy

#### Étape 1 : Conversion en arrays NumPy

```python
income_array = np.array(income_list)
life_array = np.array(life_list)
```

**Pourquoi NumPy ?**
- Les arrays NumPy sont **optimisés** pour les calculs mathématiques
- Opérations vectorielles **beaucoup plus rapides** que les boucles Python
- Fonctions mathématiques intégrées (log, polyfit, etc.)

#### Étape 2 : Transformation logarithmique

```python
log_income = np.log10(income_array)
```

**Pourquoi `log10()` ?**
- L'axe X est en échelle logarithmique
- Pour la régression, on doit travailler avec les **valeurs logarithmiques**
- `log10(1000) = 3`, `log10(10000) = 4`, etc.

**Exemple :**
```python
income = [300, 1000, 5000, 10000]
log_income = [2.48, 3.0, 3.70, 4.0]  # log10 de chaque valeur
```

#### Étape 3 : Calcul de la régression avec `np.polyfit()`

```python
coeffs = np.polyfit(log_income, life_array, deg=1)
```

**Paramètres :**
- `log_income` : valeurs X (revenus en log)
- `life_array` : valeurs Y (espérances de vie)
- `deg=1` : degré du polynôme (1 = droite linéaire)

**Retour :**
- `coeffs[0]` = pente `a` de la droite
- `coeffs[1]` = ordonnée à l'origine `b`

**Exemple de résultat :**
```python
coeffs = [15.2, -10.5]
# Signifie : y = 15.2 × log10(x) - 10.5
```

**Ce que fait `np.polyfit()` en interne :**
1. Calcule les moyennes de x et y
2. Calcule les écarts à la moyenne
3. Applique les formules mathématiques de la régression
4. Retourne les coefficients optimaux

#### Étape 4 : Génération des points pour la courbe

```python
x_trend = np.logspace(
    np.log10(income_array.min()),
    np.log10(income_array.max()),
    100
)
```

**`np.logspace()` :**
- Génère 100 valeurs **réparties logarithmiquement** entre min et max
- Équivalent à : `10^logspace(log10(min), log10(max), 100)`

**Exemple :**
```python
# Si min = 300, max = 10000
x_trend = [300, 350, 400, ..., 8000, 9000, 10000]
# 100 valeurs réparties de manière logarithmique
```

**Pourquoi 100 points ?**
- Pour avoir une courbe **lisse** lors de l'affichage
- Plus de points = meilleure qualité visuelle

#### Étape 5 : Calcul des valeurs Y de la droite

```python
y_trend = coeffs[0] * np.log10(x_trend) + coeffs[1]
```

**Application de la formule :**
- Pour chaque valeur `x` dans `x_trend`
- On calcule `y = a × log10(x) + b`
- Résultat : 100 points (x, y) qui forment la droite de régression

**Exemple :**
```python
# Si coeffs = [15.2, -10.5] et x_trend[0] = 300
y_trend[0] = 15.2 × log10(300) + (-10.5)
           = 15.2 × 2.48 - 10.5
           = 27.2
```

### 4.4 Le coefficient de détermination R²

#### A. Qu'est-ce que R² ?

Le **coefficient de détermination R²** mesure la **qualité** de la corrélation :
- **R² = 1** : corrélation parfaite (tous les points sont sur la droite)
- **R² = 0** : aucune corrélation linéaire
- **R² proche de 1** : forte corrélation (la droite explique bien les données)

**Interprétation :**
- R² = 0.85 signifie que **85% de la variance** de l'espérance de vie est expliquée par le revenu
- Les 15% restants sont dus à d'autres facteurs (santé, éducation, etc.)

#### B. Calcul de R²

```python
# 1. Prédire les valeurs Y pour tous les points
y_pred = coeffs[0] * log_income + coeffs[1]

# 2. Calculer la somme des carrés résiduels (erreurs)
ss_res = np.sum((life_array - y_pred) ** 2)

# 3. Calculer la somme totale des carrés (variance totale)
ss_tot = np.sum((life_array - np.mean(life_array)) ** 2)

# 4. Calculer R²
r_squared = 1 - (ss_res / ss_tot)
```

**Explication détaillée :**

**Étape 1 : Prédictions**
```python
y_pred = coeffs[0] * log_income + coeffs[1]
```
- Pour chaque pays, on calcule la valeur **prédite** par la droite
- Exemple : si un pays a un revenu de 1000, la droite prédit une espérance de vie de 35 ans

**Étape 2 : Erreurs résiduelles (ss_res)**
```python
ss_res = np.sum((life_array - y_pred) ** 2)
```
- `life_array - y_pred` : différence entre valeur **réelle** et valeur **prédite**
- On élève au carré pour éviter les négatifs
- `np.sum()` : somme de toutes ces erreurs
- **Plus ss_res est petit, meilleure est la corrélation**

**Étape 3 : Variance totale (ss_tot)**
```python
ss_tot = np.sum((life_array - np.mean(life_array)) ** 2)
```
- `np.mean(life_array)` : moyenne de toutes les espérances de vie
- `life_array - mean` : écart de chaque valeur à la moyenne
- `np.sum()` : somme des carrés de ces écarts
- **Mesure la variabilité totale** des données

**Étape 4 : Calcul final**
```python
r_squared = 1 - (ss_res / ss_tot)
```
- Si `ss_res = 0` (erreurs nulles) → R² = 1 (corrélation parfaite)
- Si `ss_res = ss_tot` (erreurs = variance totale) → R² = 0 (pas de corrélation)

**Formule mathématique :**
```
R² = 1 - (SS_res / SS_tot)

Où :
SS_res = Σ(yi - ŷi)²    (somme des carrés résiduels)
SS_tot = Σ(yi - ȳ)²     (somme totale des carrés)
```

### 4.5 Affichage de la courbe

```python
plt.plot(x_trend, y_trend, 'r--', linewidth=2,
         label=f'Tendance (R² = {r_squared:.3f})')
plt.legend()
```

**Paramètres de `plt.plot()` :**
- `x_trend, y_trend` : coordonnées des points de la droite
- `'r--'` : style de ligne (rouge, pointillée)
- `linewidth=2` : épaisseur de la ligne
- `label=...` : texte de la légende avec R² arrondi à 3 décimales

**Résultat visuel :**
- Une ligne rouge pointillée qui traverse le nuage de points
- La légende affiche "Tendance (R² = 0.852)" par exemple

---

## 📊 Résumé du flux de données

```
1. Chargement CSV → DataFrame Pandas
   ↓
2. Extraction des données (pays communs, année spécifique)
   ↓
3. Conversion en listes Python
   ↓
4. Affichage scatter plot (nuage de points)
   ↓
5. Calcul régression linéaire (NumPy)
   ↓
6. Calcul R² (qualité de corrélation)
   ↓
7. Affichage courbe de tendance
```

---

## 🔍 Points clés à retenir

1. **DataFrame** = tableau de données avec lignes et colonnes
2. **`.loc[]`** = accès par label (nom de pays, nom de colonne)
3. **Scatter plot** = visualisation de la relation entre 2 variables
4. **Régression linéaire** = trouver la meilleure droite qui résume les données
5. **R²** = mesure de qualité (0 = pas de corrélation, 1 = corrélation parfaite)
6. **Échelle logarithmique** = utile pour visualiser des données avec de grandes variations

---

## 📚 Ressources pour aller plus loin

- **Pandas** : [Documentation officielle](https://pandas.pydata.org/docs/)
- **NumPy** : [Documentation officielle](https://numpy.org/doc/)
- **Matplotlib** : [Documentation officielle](https://matplotlib.org/stable/contents.html)
- **Régression linéaire** : Cours de statistiques sur les moindres carrés
- **R²** : Coefficient de détermination en statistiques

