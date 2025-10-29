# Guide complet : Création d'un package Python

## Table des matières
1. [Structure du projet](#1-structure-du-projet)
2. [Configuration du package](#2-configuration-du-package)
3. [Création du code](#3-création-du-code)
4. [Build du package](#4-build-du-package)
5. [Installation du package](#5-installation-du-package)
6. [Utilisation du package](#6-utilisation-du-package)

---

## 1. Structure du projet

### Arborescence recommandée

```
ft_package_project/
├── src/
│   └── ft_package/
│       ├── __init__.py
│       └── ft_count.py
├── LICENSE.txt
├── pyproject.toml
└── README.md
```

### Explication de chaque élément

- **`src/`** : Dossier contenant les sources du package
- **`src/ft_package/`** : Nom du package (doit correspondre à celui dans `pyproject.toml`)
- **`__init__.py`** : Fichier qui transforme le dossier en module Python et expose les fonctions publiques
- **`ft_count.py`** : Module contenant les fonctions du package
- **`LICENSE.txt`** : Fichier de licence (MIT, Apache, etc.)
- **`pyproject.toml`** : Configuration moderne du package (remplace `setup.py`)
- **`README.md`** : Documentation du package

---

## 2. Configuration du package

### 2.1 Créer `pyproject.toml`

Ce fichier définit les métadonnées et la configuration du package.

```toml
[build-system]
requires = ["setuptools>=61.0"]
build-backend = "setuptools.build_meta"

[project]
name = "ft_package"
version = "0.0.1"
description = "A sample test package"
authors = [
  { name="votre_nom", email="votre_email@example.com" },
]
license = { text="MIT" }
readme = "README.md"
classifiers = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
]
requires-python = ">=3.10"

[project.urls]
"Home-page" = "https://github.com/votre_nom/ft_package"

[tool.setuptools.packages.find]
where = ["src"]
```

### 2.2 Points importants

- **`name`** : Nom du package (visible avec `pip list`)
- **`version`** : Version du package (suivre semantic versioning)
- **`description`** : Brève description
- **`authors`** : Liste des auteurs avec nom et email
- **`license`** : Licence du projet
- **`readme`** : Fichier Markdown de documentation
- **`classifiers`** : Tags pour PyPI
- **`requires-python`** : Version Python minimale
- **`"Home-page"`** : ⚠️ **Doit être une URL valide, pas du markdown !**
- **`[tool.setuptools.packages.find]`** : Indique où trouver les packages (dans `src/`)

---

## 3. Création du code

### 3.1 Créer `src/ft_package/__init__.py`

Ce fichier expose les fonctions publiques du package.

```python
"""ft_package: A sample test package."""

# Import des fonctions depuis les modules
from .ft_count import count_in_list

# Liste des fonctions publiques
__all__ = ["count_in_list"]
```

### 3.2 Créer `src/ft_package/ft_count.py`

Module contenant la logique du package.

```python
def count_in_list(lst: list, item_to_count: any) -> int:
    """Count the occurrences of an item in a list.

    Args:
        lst (list): The list to search in.
        item_to_count (any): The item to count.

    Returns:
        int: The number of times the item appears.

    Raises:
        TypeError: If the object is not a list or is not iterable.
        Exception: If an unexpected error occurs.
    """
    try:
        return sum(1 for item in lst if item == item_to_count)
    except TypeError as e:
        raise TypeError(f"the object provided is not a list or is not iterable. {e}")
    except Exception as e:
        raise Exception(f"an unexpected error occurred: {e}")
```

### 3.3 Créer `LICENSE.txt`

Licence du projet (exemple MIT) :

```
MIT License

Copyright (c) 2024 Your Name

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction...

(Contenu complet de la licence MIT)
```

---

## 4. Build du package

### 4.1 Prérequis

Installer les outils nécessaires :

```bash
pip install build
```

### 4.2 Génération des fichiers de distribution

Dans le répertoire `ft_package_project`, exécuter :

```bash
python -m build
```

### 4.3 Fichiers générés

Cette commande crée le dossier `dist/` contenant :

- **`ft_package-0.0.1.tar.gz`** : Archive source
- **`ft_package-0.0.1-py3-none-any.whl`** : Wheel (format moderne)

---

## 5. Installation du package

### 5.1 Installer depuis les fichiers de build

Deux méthodes possibles :

**Méthode 1 - Fichier tar.gz :**
```bash
pip install ./dist/ft_package-0.0.1.tar.gz
```

**Méthode 2 - Fichier wheel (recommandé) :**
```bash
pip install ./dist/ft_package-0.0.1-py3-none-any.whl
```

### 5.2 Vérifier l'installation

```bash
pip show -v ft_package
```

Sortie attendue :
```
Name: ft_package
Version: 0.0.1
Summary: A sample test package
Home-page: https://github.com/bchene/ft_package
Author: bchene
Author-email: bchene@example.com
License: MIT
Location: /path/to/site-packages
Requires:
Required-by:
Metadata-Version: 2.1
Installer: pip
Classifiers:
Entry-points:
```

### 5.3 Désinstaller le package

```bash
pip uninstall ft_package
```

---

## 6. Utilisation du package

### 6.1 Importer et utiliser dans un script

```python
from ft_package import count_in_list

# Exemples d'utilisation
print(count_in_list(["toto", "tata", "toto"], "toto"))  # Output: 2
print(count_in_list(["toto", "tata", "toto"], "tutu"))   # Output: 0
```

### 6.2 Créer un fichier de test

**`tester.py` :**
```python
from ft_package import count_in_list

print(count_in_list(["toto", "tata", "toto"], "toto"))
print(count_in_list(["toto", "tata", "toto"], "tutu"))
```

**Exécution :**
```bash
python tester.py
```

**Sortie attendue :**
```
2
0
```

### 6.3 Tests unitaires

Créer `tests/test_ft_package.py` :

```python
from ft_package import count_in_list

def test_count_in_list():
    assert count_in_list(["a", "b", "a"], "a") == 2
    assert count_in_list(["a", "b", "a"], "c") == 0
    assert count_in_list([], "a") == 0

if __name__ == "__main__":
    test_count_in_list()
    print("All tests passed!")
```

---

## 7. Checklist de création d'un package

- [ ] Créer la structure de dossiers (`src/nom_du_package/`)
- [ ] Créer `__init__.py` avec les exports publics
- [ ] Créer les modules Python (`.py`)
- [ ] Créer `pyproject.toml` avec configuration correcte
- [ ] Créer `LICENSE.txt`
- [ ] Créer `README.md`
- [ ] Vérifier que l'URL est valide (pas de markdown)
- [ ] Vérifier que `description` est utilisé (pas `summary`)
- [ ] Vérifier que le nom du dossier correspond à `name` dans `pyproject.toml`
- [ ] Exécuter `python -m build`
- [ ] Vérifier que `dist/` contient les fichiers
- [ ] Tester l'installation avec `pip install`
- [ ] Tester l'utilisation avec un script de test
- [ ] Vérifier avec `pip show`

---

## 8. Résumé des commandes

```bash
# 1. Créer la structure
mkdir -p src/ft_package
touch src/ft_package/__init__.py src/ft_package/ft_count.py

# 2. Configurer le package
# Éditer pyproject.toml, LICENSE.txt, README.md

# 3. Installer les outils
pip install build

# 4. Build le package
python -m build

# 5. Installer le package
pip install ./dist/ft_package-0.0.1-py3-none-any.whl

# 6. Vérifier l'installation
pip show ft_package

# 7. Tester
python tester.py
```

---

## 9. Conseils et bonnes pratiques

1. **Nommage** : Utiliser des noms en minuscules avec underscores
2. **Versioning** : Suivre le semantic versioning (MAJOR.MINOR.PATCH)
3. **Documentation** : Ajouter des docstrings à toutes les fonctions
4. **Tests** : Créer des tests unitaires pour vérifier le fonctionnement
5. **Git** : Ajouter `.gitignore` pour ignorer `dist/`, `build/`, `*.egg-info/`
6. **Distribution** : Créer un dépôt GitHub/GitLab pour la distribution publique

---

## 10. Structure finale recommandée

```
ft_package_project/
├── .gitignore
├── LICENSE.txt
├── pyproject.toml
├── README.md
├── src/
│   └── ft_package/
│       ├── __init__.py
│       └── ft_count.py
├── tests/
│   └── test_ft_package.py
├── dist/                    # Généré par build
├── build/                    # Généré par build
└── *.egg-info/              # Généré par build
```

---

## Conclusion

Ce guide vous permet de créer un package Python professionnel de A à Z. Le processus peut être résumé en 4 étapes :

1. **Créer** la structure et le code
2. **Configurer** avec `pyproject.toml`
3. **Builder** avec `python -m build`
4. **Installer** et **utiliser** avec `pip install`

Pour plus d'informations, consultez [Python Packaging Guide](https://packaging.python.org/en/latest/).

