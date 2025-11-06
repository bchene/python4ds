# Configuration des imports Python dans VS Code

Ce document explique comment résoudre les warnings jaunes "Impossible de résoudre l'importation" dans VS Code.

## Problème

VS Code/Pylance affiche des warnings jaunes pour les imports qui ne peuvent pas être résolus, même si le code fonctionne correctement lors de l'exécution. Cela arrive souvent avec :
- Des imports relatifs entre dossiers (`Dev/`, `Tester/`)
- Des modules locaux dans le même dossier
- Des imports qui dépendent du répertoire de travail

## Solution

Trois fichiers de configuration ont été créés pour résoudre ce problème :

### 1. `.vscode/settings.json`
Configuration VS Code pour Pylance :
- Définit les chemins supplémentaires (`extraPaths`) pour résoudre les imports
- Désactive les avertissements pour les imports manquants
- Configure le formatage automatique

### 2. `pyrightconfig.json`
Configuration Pyright (utilisé par Pylance) :
- Même configuration que `settings.json` mais dans un format standard
- Utilisé par d'autres outils d'analyse Python

### 3. `pyproject.toml` (mis à jour)
Ajout de la section `[tool.pyright]` :
- Configuration supplémentaire pour Pyright
- Compatible avec les autres outils Python modernes

## Après modification

1. **Recharger VS Code** :
   - `Cmd+Shift+P` (Mac) ou `Ctrl+Shift+P` (Windows/Linux)
   - Tapez "Developer: Reload Window"
   - Ou redémarrez VS Code complètement

2. **Vérifier l'interpréteur Python** :
   - `Cmd+Shift+P` → "Python: Select Interpreter"
   - Choisissez l'interpréteur de votre environnement (conda, venv, etc.)

3. **Vérifier que Pylance est actif** :
   - En bas à droite de VS Code, vous devriez voir "Pylance" ou "Python"
   - Si vous voyez "Jedi", changez pour Pylance dans les paramètres

## Fichiers créés

```
Python for datascience/
├── .vscode/
│   ├── settings.json          # Configuration VS Code
│   └── README.md              # Documentation
├── pyrightconfig.json         # Configuration Pyright
├── pyproject.toml             # Configuration Python (mis à jour)
└── requirements.txt           # Dépendances Python
```

## Personnalisation

Si vous avez besoin d'ajouter d'autres chemins :

1. **Dans `.vscode/settings.json`** :
   ```json
   "python.analysis.extraPaths": [
       "${workspaceFolder}/votre/nouveau/chemin"
   ]
   ```

2. **Dans `pyrightconfig.json`** :
   ```json
   "extraPaths": [
       "votre/nouveau/chemin"
   ]
   ```

3. **Dans `pyproject.toml`** :
   ```toml
   [tool.pyright]
   extraPaths = [
       "votre/nouveau/chemin"
   ]
   ```

## Notes importantes

- Les warnings d'imports sont **désactivés** car le code fonctionne correctement lors de l'exécution
- Les chemins sont configurés pour tous les dossiers `Dev/` et `Tester/`
- Les imports relatifs fonctionnent toujours lors de l'exécution depuis le bon répertoire
- Cette configuration n'affecte pas l'exécution du code, seulement l'affichage dans VS Code

## Dépannage

Si les warnings persistent après rechargement :

1. Vérifiez que Pylance est bien l'analyseur actif (pas Jedi)
2. Vérifiez que l'interpréteur Python est correctement sélectionné
3. Vérifiez les logs Pylance : `Cmd+Shift+P` → "Python: Show Output" → Sélectionnez "Pylance"
4. Essayez de redémarrer complètement VS Code

