# Tableau des Codes Couleurs ANSI

## Codes de Couleurs de Texte (Foreground)

| Code | Couleur | Exemple |
|------|---------|---------|
| `\033[30m` | Noir (Black) | Noir |
| `\033[31m` | Rouge (Red) | Rouge |
| `\033[32m` | Vert (Green) | Vert |
| `\033[33m` | Jaune (Yellow) | Jaune |
| `\033[34m` | Bleu (Blue) | Bleu |
| `\033[35m` | Magenta | Magenta |
| `\033[36m` | Cyan | Cyan |
| `\033[37m` | Blanc (White) | Blanc |
| `\033[90m` | Gris foncé (Bright Black) | Gris foncé |
| `\033[91m` | Rouge clair (Bright Red) | Rouge clair |
| `\033[92m` | Vert clair (Bright Green) | Vert clair |
| `\033[93m` | Jaune clair (Bright Yellow) | Jaune clair |
| `\033[94m` | Bleu clair (Bright Blue) | Bleu clair |
| `\033[95m` | Magenta clair (Bright Magenta) | Magenta clair |
| `\033[96m` | Cyan clair (Bright Cyan) | Cyan clair |
| `\033[97m` | Blanc clair (Bright White) | Blanc clair |

## Codes de Couleurs d'Arrière-plan (Background)

| Code | Couleur | Exemple |
|------|---------|---------|
| `\033[40m` | Noir | Arrière-plan noir |
| `\033[41m` | Rouge | Arrière-plan rouge |
| `\033[42m` | Vert | Arrière-plan vert |
| `\033[43m` | Jaune | Arrière-plan jaune |
| `\033[44m` | Bleu | Arrière-plan bleu |
| `\033[45m` | Magenta | Arrière-plan magenta |
| `\033[46m` | Cyan | Arrière-plan cyan |
| `\033[47m` | Blanc | Arrière-plan blanc |
| `\033[100m` | Gris foncé | Arrière-plan gris foncé |
| `\033[101m` | Rouge clair | Arrière-plan rouge clair |
| `\033[102m` | Vert clair | Arrière-plan vert clair |
| `\033[103m` | Jaune clair | Arrière-plan jaune clair |
| `\033[104m` | Bleu clair | Arrière-plan bleu clair |
| `\033[105m` | Magenta clair | Arrière-plan magenta clair |
| `\033[106m` | Cyan clair | Arrière-plan cyan clair |
| `\033[107m` | Blanc clair | Arrière-plan blanc clair |

## Codes de Style

| Code | Style | Description |
|------|-------|-------------|
| `\033[0m` | Reset | Réinitialise tous les attributs (couleur normale) |
| `\033[1m` | Gras (Bold) | Texte en gras |
| `\033[2m` | Atténué (Dim) | Texte atténué |
| `\033[3m` | Italique | Texte en italique |
| `\033[4m` | Souligné (Underline) | Texte souligné |
| `\033[5m` | Clignotant (Blink) | Texte clignotant |
| `\033[7m` | Inversé (Reverse) | Inverse les couleurs |
| `\033[9m` | Barré (Strikethrough) | Texte barré |

## Combinaisons

Vous pouvez combiner plusieurs codes en les séparant par des points-virgules :

```python
# Texte rouge gras souligné
print("\033[1;4;31mTexte rouge gras souligné\033[0m")

# Texte vert sur fond jaune
print("\033[32;43mTexte vert sur fond jaune\033[0m")

# Texte blanc clair gras sur fond bleu
print("\033[1;97;104mTexte blanc clair gras sur fond bleu\033[0m")
```

## Exemples d'Utilisation

### En Python
```python
# Vert clair
print("\033[92m✓ Succès\033[0m")

# Rouge clair
print("\033[91m✗ Erreur\033[0m")

# Bleu clair
print("\033[94mℹ Information\033[0m")

# Jaune clair
print("\033[93m⚠ Avertissement\033[0m")
```

### En Bash
```bash
# Utiliser echo -e pour interpréter les codes
echo -e "\033[92m✓ Succès\033[0m"
echo -e "\033[91m✗ Erreur\033[0m"

# Ou utiliser printf (plus portable)
printf "\033[92m✓ Succès\033[0m\n"
printf "\033[91m✗ Erreur\033[0m\n"
```

## Notes Importantes

1. **Toujours réinitialiser** : Terminez toujours avec `\033[0m` pour réinitialiser les couleurs, sinon les couleurs continueront à s'appliquer.

2. **Dans Bash** : Utilisez `echo -e` ou `printf` pour interpréter les codes d'échappement. `echo` seul ne les interprétera pas.

3. **Portabilité** : Les codes ANSI fonctionnent sur la plupart des terminaux Unix/Linux/macOS. Pour Windows, vous devrez peut-être activer le support ANSI (Windows 10+ le supporte nativement).

4. **Détection du terminal** : Vous pouvez vérifier si le terminal supporte les couleurs avec `tput colors` dans bash.

