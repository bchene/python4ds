# Guide d'activation de l'autocomplétion dans Cursor

## ✅ Configuration effectuée

Le fichier `.vscode/settings.json` a été créé avec les paramètres nécessaires pour activer l'autocomplétion Python dans Cursor.

## 🚀 Comment utiliser l'autocomplétion

### 1. **Autocomplétion automatique**
Quand vous tapez du code, l'autocomplétion apparaît automatiquement. Par exemple :
```python
data['age'].
```
Après le point `.`, vous verrez une liste déroulante avec toutes les méthodes disponibles (`.value_counts()`, `.head()`, `.mean()`, etc.)

### 2. **Raccourcis clavier**
- **Tab** ou **Entrée** : Accepter la suggestion sélectionnée
- **Flèches ↑↓** : Naviguer dans la liste des suggestions
- **Ctrl+Espace** (ou **Cmd+Espace** sur Mac) : Forcer l'affichage des suggestions
- **Echap** : Fermer la liste des suggestions

### 3. **Exemple d'utilisation**
```python
import pandas as pd
data = pd.read_excel('Dataset/titanic.xls')

# Tapez "data['age']." et vous verrez :
# - value_counts()
# - head()
# - tail()
# - mean()
# - sum()
# - etc.
```

## 🔧 Vérifier que l'autocomplétion fonctionne

### 1. **Vérifier que Pylance est actif**
- En bas à droite de Cursor, vous devriez voir "Pylance" ou "Python"
- Si vous voyez "Jedi", changez pour Pylance :
  - `Cmd+Shift+P` (Mac) ou `Ctrl+Shift+P` (Windows/Linux)
  - Tapez "Python: Select Language Server"
  - Choisissez "Pylance"

### 2. **Sélectionner l'interpréteur Python**
- `Cmd+Shift+P` → "Python: Select Interpreter"
- Choisissez votre environnement Python (conda, venv, etc.)

### 3. **Recharger Cursor**
Si l'autocomplétion ne fonctionne pas immédiatement :
- `Cmd+Shift+P` → "Developer: Reload Window"
- Ou redémarrez Cursor complètement

## 📝 Paramètres importants activés

- ✅ **Pylance** comme language server (meilleur pour l'autocomplétion)
- ✅ **Suggestions automatiques** pendant la frappe
- ✅ **Autocomplétion des méthodes, fonctions, variables, classes**
- ✅ **Autocomplétion dans les notebooks Jupyter**
- ✅ **Indexation** pour une meilleure détection des méthodes

## 🐛 Dépannage

### L'autocomplétion ne fonctionne pas ?
1. Vérifiez que Pylance est installé et actif
2. Vérifiez que l'interpréteur Python est sélectionné
3. Rechargez la fenêtre Cursor
4. Vérifiez les logs : `Cmd+Shift+P` → "Python: Show Output" → Sélectionnez "Pylance"

### Les suggestions n'apparaissent pas après le point `.` ?
- Assurez-vous que le type de l'objet est correctement détecté
- Essayez de forcer avec `Ctrl+Espace` (ou `Cmd+Espace` sur Mac)
- Vérifiez que les bibliothèques (pandas, numpy, etc.) sont installées dans votre environnement Python

## 💡 Astuce

Pour voir la documentation d'une méthode directement dans l'éditeur :
- Survolez la méthode avec la souris
- Ou utilisez `Cmd+K Cmd+I` (Mac) / `Ctrl+K Ctrl+I` (Windows/Linux) pour afficher la documentation


