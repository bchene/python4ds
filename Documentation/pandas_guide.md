# Pandas - Guide de référence rapide

> Pense-bête complet pour maîtriser Pandas - Bibliothèque fondamentale pour la manipulation et l'analyse de données en Python

---

## Table des matières

1. [Installation et import](#installation-et-import)
2. [Création de DataFrames et Series](#création-de-dataframes-et-series)
3. [Lecture et écriture de fichiers](#lecture-et-écriture-de-fichiers)
4. [Exploration des données](#exploration-des-données)
5. [Sélection et filtrage](#sélection-et-filtrage)
6. [Manipulation des données](#manipulation-des-données)
7. [Opérations sur les colonnes](#opérations-sur-les-colonnes)
8. [Gestion des valeurs manquantes](#gestion-des-valeurs-manquantes)
9. [Regroupement et agrégation](#regroupement-et-agrégation)
10. [Fusion et jointures](#fusion-et-jointures)
11. [Opérations temporelles](#opérations-temporelles)
12. [Méthodes utiles supplémentaires](#méthodes-utiles-supplémentaires)

---

## Installation et import

```python
import pandas as pd
import numpy as np
```

**Convention standard** : importer Pandas avec l'alias `pd` pour éviter de taper `pandas.` à chaque fois.

**Installation** :
```bash
pip install pandas
# ou avec conda
conda install pandas
```

---

## Création de DataFrames et Series

### Création d'un DataFrame à partir d'un dictionnaire

```python
# DataFrame à partir d'un dictionnaire
data = {
    'nom': ['Alice', 'Bob', 'Charlie', 'Diana'],
    'âge': [25, 30, 35, 28],
    'ville': ['Paris', 'Lyon', 'Marseille', 'Paris']
}
df = pd.DataFrame(data)
# Résultat :
#       nom  âge      ville
# 0   Alice   25      Paris
# 1     Bob   30       Lyon
# 2  Charlie   35  Marseille
# 3   Diana   28      Paris
```

**Schéma conceptuel :**
```
DataFrame = Tableau 2D avec colonnes nommées

┌─────────┬──────┬───────────┐
│   nom   │ âge  │   ville   │ ← Colonnes (columns)
├─────────┼──────┼───────────┤
│  Alice  │  25  │   Paris   │ ← Ligne 0 (index)
│   Bob   │  30  │   Lyon    │ ← Ligne 1
│ Charlie │  35  │ Marseille │ ← Ligne 2
│  Diana  │  28  │   Paris   │ ← Ligne 3
└─────────┴──────┴───────────┘
```

### Création d'un DataFrame à partir d'une liste de listes

```python
# DataFrame à partir d'une liste de listes
data = [
    ['Alice', 25, 'Paris'],
    ['Bob', 30, 'Lyon'],
    ['Charlie', 35, 'Marseille']
]
df = pd.DataFrame(data, columns=['nom', 'âge', 'ville'])
# Résultat :
#       nom  âge      ville
# 0   Alice   25      Paris
# 1     Bob   30       Lyon
# 2  Charlie   35  Marseille
```

### Création d'un DataFrame à partir d'un array NumPy

```python
import numpy as np

# Array NumPy
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
df = pd.DataFrame(arr, columns=['A', 'B', 'C'])
# Résultat :
#    A  B  C
# 0  1  2  3
# 1  4  5  6
# 2  7  8  9
```

### Création d'une Series

```python
# Series = colonne unique avec index
s = pd.Series([10, 20, 30, 40], index=['a', 'b', 'c', 'd'])
# Résultat :
# a    10
# b    20
# c    30
# d    40
# dtype: int64

# Series à partir d'un dictionnaire
s = pd.Series({'a': 10, 'b': 20, 'c': 30})
# Résultat :
# a    10
# b    20
# c    30
# dtype: int64
```

**Schéma conceptuel :**
```
Series = Array 1D avec index nommé

┌─────┬──────┐
│  a  │  10  │
│  b  │  20  │
│  c  │  30  │
│  d  │  40  │
└─────┴──────┘
Index  Valeur
```

### DataFrame vide avec colonnes spécifiées

```python
# DataFrame vide
df = pd.DataFrame(columns=['nom', 'âge', 'ville'])
# Résultat :
# Empty DataFrame
# Columns: [nom, âge, ville]
# Index: []
```

---

## Lecture et écriture de fichiers

### Lecture de fichiers CSV

```python
# Lecture d'un fichier CSV
df = pd.read_csv('data.csv')

# Avec options courantes
df = pd.read_csv('data.csv', 
                 sep=',',           # Séparateur
                 header=0,          # Ligne d'en-tête (0 = première ligne)
                 index_col=0,       # Colonne à utiliser comme index
                 encoding='utf-8',  # Encodage
                 na_values=['NA', 'N/A', ''])  # Valeurs à considérer comme NaN
```

**Exemple avec fichier réel :**
```python
# Lecture d'un fichier de données démographiques
df = pd.read_csv('population_total.csv')
print(df.head())  # Affiche les 5 premières lignes
```

### Écriture de fichiers CSV

```python
# Écriture dans un fichier CSV
df.to_csv('output.csv', index=False)  # index=False pour ne pas sauvegarder l'index

# Avec options
df.to_csv('output.csv', 
          index=False,
          sep=';',           # Séparateur personnalisé
          encoding='utf-8',  # Encodage
          na_rep='NA')       # Représentation des valeurs manquantes
```

### Lecture de fichiers Excel

```python
# Lecture d'un fichier Excel
df = pd.read_excel('data.xlsx', sheet_name='Sheet1')

# Lecture de plusieurs feuilles
excel_file = pd.ExcelFile('data.xlsx')
df1 = pd.read_excel(excel_file, sheet_name='Sheet1')
df2 = pd.read_excel(excel_file, sheet_name='Sheet2')
```

### Écriture de fichiers Excel

```python
# Écriture dans un fichier Excel
df.to_excel('output.xlsx', sheet_name='Data', index=False)

# Écriture de plusieurs DataFrames dans un même fichier
with pd.ExcelWriter('output.xlsx') as writer:
    df1.to_excel(writer, sheet_name='Sheet1', index=False)
    df2.to_excel(writer, sheet_name='Sheet2', index=False)
```

### Autres formats

```python
# JSON
df = pd.read_json('data.json')
df.to_json('output.json', orient='records')

# Parquet (format binaire efficace)
df = pd.read_parquet('data.parquet')
df.to_parquet('output.parquet')

# HTML
df = pd.read_html('https://example.com/table.html')[0]  # Retourne une liste de DataFrames
```

---

## Exploration des données

### Affichage des données

```python
# Afficher les premières lignes (par défaut 5)
df.head()
df.head(10)  # 10 premières lignes

# Afficher les dernières lignes
df.tail()
df.tail(10)  # 10 dernières lignes

# Afficher un échantillon aléatoire
df.sample(5)  # 5 lignes aléatoires
```

### Informations sur le DataFrame

```python
# Informations générales
df.info()
# Affiche : nombre de lignes, colonnes, types de données, mémoire utilisée

# Description statistique
df.describe()
# Affiche : count, mean, std, min, 25%, 50%, 75%, max pour les colonnes numériques

# Description pour toutes les colonnes (y compris catégorielles)
df.describe(include='all')

# Shape (dimensions)
df.shape  # (nombre_lignes, nombre_colonnes)

# Colonnes
df.columns  # Index des noms de colonnes

# Index
df.index  # Index des lignes

# Types de données
df.dtypes  # Type de chaque colonne
```

**Exemple de sortie `df.describe()` :**
```
       âge
count   4.000000
mean   29.500000
std     4.434712
min    25.000000
25%    26.500000
50%    29.000000
75%    32.500000
max    35.000000
```

### Valeurs uniques et comptage

```python
# Valeurs uniques dans une colonne
df['ville'].unique()
# Résultat : array(['Paris', 'Lyon', 'Marseille'], dtype=object)

# Nombre de valeurs uniques
df['ville'].nunique()  # 3

# Comptage des valeurs
df['ville'].value_counts()
# Résultat :
# Paris        2
# Lyon         1
# Marseille    1
# Name: ville, dtype: int64

# Comptage avec normalisation (pourcentages)
df['ville'].value_counts(normalize=True)
# Résultat :
# Paris        0.5
# Lyon         0.25
# Marseille    0.25
```

---

## Sélection et filtrage

### Sélection de colonnes

```python
# Sélection d'une colonne (retourne une Series)
df['nom']
df.nom  # Syntaxe alternative (si le nom de colonne est valide en Python)

# Sélection de plusieurs colonnes (retourne un DataFrame)
df[['nom', 'âge']]

# Sélection par position (iloc)
df.iloc[:, 0]        # Première colonne
df.iloc[:, 0:2]      # Colonnes 0 et 1
df.iloc[:, [0, 2]]   # Colonnes 0 et 2
```

### Sélection de lignes

```python
# Par index (loc)
df.loc[0]           # Première ligne (retourne une Series)
df.loc[0:2]         # Lignes 0, 1, 2 (inclus les deux bornes)
df.loc[[0, 2]]      # Lignes 0 et 2

# Par position (iloc)
df.iloc[0]          # Première ligne
df.iloc[0:3]        # Lignes 0, 1, 2 (3 exclu)
df.iloc[[0, 2]]     # Lignes 0 et 2

# Par index nommé
df.set_index('nom', inplace=True)
df.loc['Alice']     # Ligne avec index 'Alice'
```

**Schéma de sélection :**
```
DataFrame :
┌─────────┬──────┬───────────┐
│   nom   │ âge  │   ville   │
├─────────┼──────┼───────────┤
│  Alice  │  25  │   Paris   │ ← df.loc[0] ou df.iloc[0]
│   Bob   │  30  │   Lyon    │ ← df.loc[1] ou df.iloc[1]
│ Charlie │  35  │ Marseille │
│  Diana  │  28  │   Paris   │
└─────────┴──────┴───────────┘

df[['nom', 'âge']] → Colonnes 'nom' et 'âge'
df.loc[0:2] → Lignes 0, 1, 2
df.iloc[0:3] → Lignes 0, 1, 2 (3 exclu)
```

### Sélection combinée (lignes et colonnes)

```python
# Sélection de lignes et colonnes
df.loc[0:2, ['nom', 'âge']]      # Lignes 0-2, colonnes nom et âge
df.iloc[0:3, [0, 1]]              # Lignes 0-2, colonnes 0 et 1

# Condition sur une colonne
df.loc[df['âge'] > 25, ['nom', 'ville']]
```

### Filtrage avec conditions

```python
# Filtrage simple
df[df['âge'] > 25]
# Résultat : lignes où l'âge est supérieur à 25

# Conditions multiples (ET)
df[(df['âge'] > 25) & (df['ville'] == 'Paris')]
# ⚠️ Important : utiliser &, |, ~ au lieu de and, or, not

# Conditions multiples (OU)
df[(df['âge'] > 30) | (df['ville'] == 'Lyon')]

# Condition de négation
df[~(df['ville'] == 'Paris')]  # Toutes les villes sauf Paris

# Filtrage avec isin()
df[df['ville'].isin(['Paris', 'Lyon'])]

# Filtrage avec contains() (pour chaînes de caractères)
df[df['nom'].str.contains('Alice')]
```

**Exemple de filtrage :**
```python
# Données
df = pd.DataFrame({
    'nom': ['Alice', 'Bob', 'Charlie', 'Diana'],
    'âge': [25, 30, 35, 28],
    'ville': ['Paris', 'Lyon', 'Marseille', 'Paris']
})

# Personnes de plus de 25 ans à Paris
result = df[(df['âge'] > 25) & (df['ville'] == 'Paris')]
# Résultat :
#      nom  âge  ville
# 3  Diana   28  Paris
```

### Filtrage avec query()

```python
# Syntaxe alternative avec query()
df.query('âge > 25')
df.query('âge > 25 and ville == "Paris"')
df.query('âge > @seuil', local_dict={'seuil': 25})  # Variable externe
```

---

## Manipulation des données

### Ajout de colonnes

```python
# Ajout d'une colonne simple
df['nouvelle_colonne'] = 0
df['nouvelle_colonne'] = [1, 2, 3, 4]

# Ajout d'une colonne calculée
df['âge_doublé'] = df['âge'] * 2

# Ajout avec assign()
df = df.assign(nouvelle_colonne=df['âge'] * 2)

# Ajout conditionnel
df['catégorie'] = df['âge'].apply(lambda x: 'jeune' if x < 30 else 'adulte')
```

### Suppression de colonnes/lignes

```python
# Suppression de colonnes
df.drop('colonne', axis=1)           # Retourne un nouveau DataFrame
df.drop('colonne', axis=1, inplace=True)  # Modifie le DataFrame existant
df.drop(['col1', 'col2'], axis=1)    # Suppression multiple

# Suppression de lignes
df.drop(0)                           # Supprime la ligne d'index 0
df.drop([0, 2])                      # Supprime les lignes 0 et 2
df.drop(df[df['âge'] < 30].index)   # Supprime les lignes où âge < 30
```

### Renommage

```python
# Renommer des colonnes
df.rename(columns={'nom': 'name', 'âge': 'age'})

# Renommer l'index
df.rename(index={0: 'premier', 1: 'deuxième'})

# Renommer toutes les colonnes
df.columns = ['name', 'age', 'city']
```

### Réorganisation des colonnes

```python
# Réorganiser l'ordre des colonnes
df = df[['ville', 'nom', 'âge']]  # Nouvel ordre

# Réorganiser avec reindex()
df = df.reindex(columns=['ville', 'nom', 'âge'])
```

### Tri

```python
# Tri par une colonne
df.sort_values('âge')                    # Tri croissant
df.sort_values('âge', ascending=False)   # Tri décroissant

# Tri par plusieurs colonnes
df.sort_values(['ville', 'âge'])         # Tri par ville, puis par âge

# Tri par index
df.sort_index()

# Tri en place
df.sort_values('âge', inplace=True)
```

---

## Opérations sur les colonnes

### Opérations mathématiques

```python
# Opérations élément par élément
df['nouveau'] = df['col1'] + df['col2']
df['nouveau'] = df['col1'] * 2
df['nouveau'] = df['col1'] / df['col2']

# Fonctions mathématiques
df['sqrt'] = np.sqrt(df['col1'])
df['log'] = np.log(df['col1'])
df['exp'] = np.exp(df['col1'])
```

### Opérations sur les chaînes de caractères

```python
# Accès aux méthodes de chaînes via .str
df['nom'].str.upper()           # Mettre en majuscules
df['nom'].str.lower()           # Mettre en minuscules
df['nom'].str.capitalize()      # Première lettre en majuscule
df['nom'].str.len()             # Longueur de chaque chaîne
df['nom'].str.contains('Alice') # Contient 'Alice'
df['nom'].str.replace('Alice', 'Alicia')  # Remplacer
df['nom'].str.split(' ')        # Diviser par espace
df['nom'].str.strip()           # Supprimer espaces en début/fin
```

**Exemple :**
```python
df = pd.DataFrame({'nom': ['  Alice  ', 'Bob', 'Charlie']})
df['nom'] = df['nom'].str.strip().str.capitalize()
# Résultat :
#       nom
# 0   Alice
# 1     Bob
# 2  Charlie
```

### Opérations sur les dates

```python
# Conversion en datetime
df['date'] = pd.to_datetime(df['date_colonne'])

# Extraction de composants
df['année'] = df['date'].dt.year
df['mois'] = df['date'].dt.month
df['jour'] = df['date'].dt.day
df['jour_semaine'] = df['date'].dt.dayofweek  # 0 = lundi
df['nom_jour'] = df['date'].dt.day_name()

# Opérations sur les dates
df['date'] + pd.Timedelta(days=7)  # Ajouter 7 jours
df['date'] - pd.Timedelta(weeks=2)  # Soustraire 2 semaines
```

### Application de fonctions (apply)

```python
# Appliquer une fonction à une colonne
df['nouveau'] = df['col'].apply(lambda x: x * 2)

# Appliquer une fonction à chaque ligne
df['somme'] = df.apply(lambda row: row['col1'] + row['col2'], axis=1)

# Appliquer une fonction définie
def ma_fonction(x):
    return x * 2 if x > 10 else x

df['nouveau'] = df['col'].apply(ma_fonction)

# Appliquer à plusieurs colonnes
df[['col1', 'col2']] = df[['col1', 'col2']].apply(lambda x: x * 2)
```

---

## Gestion des valeurs manquantes

### Détection des valeurs manquantes

```python
# Vérifier les valeurs manquantes
df.isna()           # DataFrame booléen (True = valeur manquante)
df.isnull()         # Alias de isna()
df.notna()          # Inverse de isna()

# Compter les valeurs manquantes par colonne
df.isna().sum()

# Compter les valeurs manquantes totales
df.isna().sum().sum()

# Pourcentage de valeurs manquantes
df.isna().sum() / len(df) * 100
```

### Suppression des valeurs manquantes

```python
# Supprimer les lignes avec des valeurs manquantes
df.dropna()                    # Supprime toutes les lignes avec au moins un NaN
df.dropna(how='all')           # Supprime seulement si TOUTES les valeurs sont NaN
df.dropna(subset=['col1'])     # Supprime seulement si NaN dans 'col1'

# Supprimer les colonnes avec des valeurs manquantes
df.dropna(axis=1)              # Supprime les colonnes avec au moins un NaN
```

### Remplissage des valeurs manquantes

```python
# Remplir avec une valeur constante
df.fillna(0)                   # Remplacer tous les NaN par 0
df['col'].fillna('inconnu')    # Remplacer dans une colonne spécifique

# Remplir avec la moyenne/médiane/mode
df['col'].fillna(df['col'].mean())     # Moyenne
df['col'].fillna(df['col'].median())   # Médiane
df['col'].fillna(df['col'].mode()[0])  # Mode (plus fréquent)

# Remplir avec méthode forward fill / backward fill
df.fillna(method='ffill')      # Forward fill (remplit avec la valeur précédente)
df.fillna(method='bfill')      # Backward fill (remplit avec la valeur suivante)

# Remplir avec interpolation
df['col'].interpolate()        # Interpolation linéaire
```

**Exemple :**
```python
df = pd.DataFrame({
    'A': [1, 2, np.nan, 4, 5],
    'B': [np.nan, 2, 3, np.nan, 5]
})

# Avant :
#      A    B
# 0  1.0  NaN
# 1  2.0  2.0
# 2  NaN  3.0
# 3  4.0  NaN
# 4  5.0  5.0

df.fillna(df.mean())
# Après :
#      A    B
# 0  1.0  3.33
# 1  2.0  2.00
# 2  3.0  3.00
# 3  4.0  3.33
# 4  5.0  5.00
```

---

## Regroupement et agrégation

### Groupby de base

```python
# Grouper par une colonne
grouped = df.groupby('ville')

# Appliquer une fonction d'agrégation
df.groupby('ville')['âge'].mean()      # Moyenne d'âge par ville
df.groupby('ville')['âge'].sum()       # Somme
df.groupby('ville')['âge'].count()     # Nombre d'éléments
df.groupby('ville')['âge'].min()       # Minimum
df.groupby('ville')['âge'].max()       # Maximum
df.groupby('ville')['âge'].std()       # Écart-type
```

**Exemple :**
```python
df = pd.DataFrame({
    'ville': ['Paris', 'Paris', 'Lyon', 'Lyon', 'Marseille'],
    'âge': [25, 28, 30, 35, 40],
    'salaire': [3000, 3500, 4000, 4500, 5000]
})

# Moyenne d'âge par ville
df.groupby('ville')['âge'].mean()
# Résultat :
# ville
# Lyon         32.5
# Marseille    40.0
# Paris        26.5
# Name: âge, dtype: float64
```

### Agrégations multiples

```python
# Plusieurs fonctions d'agrégation
df.groupby('ville')['âge'].agg(['mean', 'min', 'max', 'count'])

# Agrégations différentes par colonne
df.groupby('ville').agg({
    'âge': 'mean',
    'salaire': ['sum', 'mean']
})

# Fonction personnalisée
df.groupby('ville')['âge'].agg(lambda x: x.max() - x.min())  # Écart
```

### Groupby avec plusieurs colonnes

```python
# Grouper par plusieurs colonnes
df.groupby(['ville', 'catégorie'])['âge'].mean()

# Résultat (MultiIndex) :
# ville      catégorie
# Lyon       adulte       32.5
# Marseille  adulte       40.0
# Paris      jeune        26.5
```

### Transform et apply

```python
# Transform : applique une fonction et retourne un DataFrame de même taille
df['âge_moyen_ville'] = df.groupby('ville')['âge'].transform('mean')

# Apply : applique une fonction personnalisée
def normaliser(group):
    return (group - group.mean()) / group.std()

df['âge_normalisé'] = df.groupby('ville')['âge'].apply(normaliser)
```

---

## Fusion et jointures

### Concaténation

```python
# Concaténation verticale (empiler des DataFrames)
df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
df2 = pd.DataFrame({'A': [5, 6], 'B': [7, 8]})
pd.concat([df1, df2], ignore_index=True)
# Résultat :
#    A  B
# 0  1  3
# 1  2  4
# 2  5  7
# 3  6  8

# Concaténation horizontale
pd.concat([df1, df2], axis=1)
```

### Merge (jointures SQL-like)

```python
# Merge interne (inner join) - intersection
df1 = pd.DataFrame({'id': [1, 2, 3], 'nom': ['A', 'B', 'C']})
df2 = pd.DataFrame({'id': [2, 3, 4], 'ville': ['X', 'Y', 'Z']})
pd.merge(df1, df2, on='id', how='inner')
# Résultat :
#    id nom ville
# 0   2   B     X
# 1   3   C     Y

# Merge externe (outer join) - union
pd.merge(df1, df2, on='id', how='outer')
# Résultat :
#    id nom ville
# 0   1   A   NaN
# 1   2   B     X
# 2   3   C     Y
# 3   4 NaN     Z

# Merge gauche (left join)
pd.merge(df1, df2, on='id', how='left')

# Merge droite (right join)
pd.merge(df1, df2, on='id', how='right')
```

**Schéma des jointures :**
```
df1:          df2:
id  nom       id  ville
1   A         2   X
2   B         3   Y
3   C         4   Z

INNER JOIN (how='inner') :
id  nom  ville
2   B    X
3   C    Y

LEFT JOIN (how='left') :
id  nom  ville
1   A    NaN
2   B    X
3   C    Y

OUTER JOIN (how='outer') :
id  nom  ville
1   A    NaN
2   B    X
3   C    Y
4   NaN  Z
```

### Merge avec colonnes différentes

```python
# Colonnes de jointure différentes
pd.merge(df1, df2, left_on='id1', right_on='id2')

# Merge sur l'index
pd.merge(df1, df2, left_index=True, right_index=True)
```

---

## Opérations temporelles

### Création de dates

```python
# Créer un range de dates
dates = pd.date_range('2023-01-01', '2023-12-31', freq='D')  # Quotidien
dates = pd.date_range('2023-01-01', periods=365, freq='D')

# Fréquences courantes
pd.date_range('2023-01-01', periods=12, freq='M')   # Mensuel
pd.date_range('2023-01-01', periods=4, freq='Q')    # Trimestriel
pd.date_range('2023-01-01', periods=2, freq='Y')    # Annuel
```

### Index temporel

```python
# Créer un DataFrame avec index temporel
df = pd.DataFrame({
    'valeur': [10, 20, 30, 40],
    'date': pd.date_range('2023-01-01', periods=4, freq='D')
})
df.set_index('date', inplace=True)

# Sélection par date
df.loc['2023-01-01']
df.loc['2023-01-01':'2023-01-03']  # Plage de dates
```

### Resampling (rééchantillonnage temporel)

```python
# Rééchantillonnage (ex: quotidien → mensuel)
df.resample('M').mean()      # Moyenne mensuelle
df.resample('W').sum()       # Somme hebdomadaire
df.resample('Q').max()       # Maximum trimestriel

# Exemple avec données réelles
df = pd.read_csv('income_per_person_gdppercapita_ppp_inflation_adjusted.csv', index_col=0)
df.index = pd.to_datetime(df.index)
df_monthly = df.resample('M').mean()  # Si les données sont quotidiennes
```

---

## Méthodes utiles supplémentaires

### Copie

```python
# Copie superficielle (shallow copy)
df_copy = df.copy()

# ⚠️ Attention : sans copy(), les modifications affectent l'original
df_view = df  # Ce n'est pas une copie !
```

### Réinitialisation de l'index

```python
# Réinitialiser l'index (0, 1, 2, ...)
df.reset_index(drop=True)  # drop=True supprime l'ancien index

# Réinitialiser avec conservation
df.reset_index()  # L'ancien index devient une colonne
```

### Pivot et melt

```python
# Pivot : transformer les lignes en colonnes
df = pd.DataFrame({
    'date': ['2023-01', '2023-01', '2023-02', '2023-02'],
    'ville': ['Paris', 'Lyon', 'Paris', 'Lyon'],
    'valeur': [10, 20, 15, 25]
})
df.pivot(index='date', columns='ville', values='valeur')
# Résultat :
# ville    Lyon  Paris
# date
# 2023-01    20     10
# 2023-02    25     15

# Melt : transformer les colonnes en lignes (inverse de pivot)
df.melt(id_vars=['date'], value_vars=['Paris', 'Lyon'], var_name='ville', value_name='valeur')
```

### Duplication

```python
# Trouver les lignes dupliquées
df.duplicated()              # True pour les lignes dupliquées
df.duplicated(subset=['col'])  # Duplication basée sur une colonne

# Supprimer les doublons
df.drop_duplicates()
df.drop_duplicates(subset=['col'], keep='first')  # Garder la première occurrence
```

### Exportation de données

```python
# CSV
df.to_csv('output.csv', index=False)

# Excel
df.to_excel('output.xlsx', index=False)

# JSON
df.to_json('output.json', orient='records')

# HTML (pour affichage web)
df.to_html('output.html', index=False)

# Parquet (format binaire efficace)
df.to_parquet('output.parquet')
```

### Méthodes de chaînes avancées

```python
# Extraction avec regex
df['col'].str.extract(r'(\d+)')  # Extraire les chiffres

# Concaténation
df['nom_complet'] = df['prénom'].str.cat(df['nom'], sep=' ')

# Vérification de patterns
df['col'].str.match(r'^[A-Z]')   # Commence par une majuscule
```

### Méthodes de séries temporelles

```python
# Décalage (shift)
df['valeur_lag1'] = df['valeur'].shift(1)  # Valeur précédente
df['valeur_lead1'] = df['valeur'].shift(-1)  # Valeur suivante

# Différence
df['diff'] = df['valeur'].diff()  # Différence avec la valeur précédente

# Pourcentage de changement
df['pct_change'] = df['valeur'].pct_change()  # Pourcentage de changement
```

### Méthodes de sélection conditionnelle avancées

```python
# where() : remplacer les valeurs qui ne satisfont pas la condition
df['col'].where(df['col'] > 0, 0)  # Remplace les valeurs <= 0 par 0

# mask() : inverse de where()
df['col'].mask(df['col'] > 0, 0)  # Remplace les valeurs > 0 par 0

# clip() : limiter les valeurs entre un min et un max
df['col'].clip(lower=0, upper=100)  # Limite entre 0 et 100
```

---

## Récapitulatif des conventions importantes

### Syntaxe de base

| Opération | Syntaxe |
|-----------|---------|
| Import | `import pandas as pd` |
| Création DataFrame | `pd.DataFrame(data, columns=[...])` |
| Création Series | `pd.Series([...], index=[...])` |
| Lecture CSV | `pd.read_csv('file.csv')` |
| Écriture CSV | `df.to_csv('file.csv', index=False)` |

### Sélection

| Syntaxe | Description |
|---------|-------------|
| `df['col']` | Sélection d'une colonne (Series) |
| `df[['col1', 'col2']]` | Sélection de plusieurs colonnes (DataFrame) |
| `df.loc[0]` | Sélection par index (inclus les bornes) |
| `df.iloc[0]` | Sélection par position (exclut la borne supérieure) |
| `df[df['col'] > 0]` | Filtrage conditionnel |

### Opérations booléennes

| Opérateur Pandas | Équivalent Python |
|------------------|-------------------|
| `&` | `and` |
| `\|` | `or` |
| `~` | `not` |

### Méthodes d'agrégation courantes

- `mean()`, `median()`, `std()`, `var()` : Statistiques
- `sum()`, `prod()`, `min()`, `max()` : Opérations
- `count()`, `nunique()` : Comptage
- `first()`, `last()` : Première/dernière valeur

---

## Ressources supplémentaires

- **Documentation officielle** : https://pandas.pydata.org/docs/
- **Guide de référence** : https://pandas.pydata.org/docs/reference/
- **Tutoriels** : https://pandas.pydata.org/docs/getting_started/

---

*Document créé pour servir de pense-bête Pandas - Mise à jour régulière recommandée*

