#!/bin/bash
# Script complet pour tester l'exercice 09 (ft_package)

PROJECT_DIR="../../Dev/Python_0_Starting/ex09"
TESTER_DIR="$(pwd)"

echo "========================================="
echo "TEST COMPLET - EXERCICE 09 (ft_package)"
echo "========================================="
echo ""

# 1. Aller dans le dossier du projet
cd "$PROJECT_DIR"
echo "📂 Étape 1: Arrivée dans le projet"
echo "Dossier: $(pwd)"
echo ""

# 2. Nettoyer les anciens builds
echo "🧹 Étape 2: Nettoyage des anciens builds"
rm -rf dist build *.egg-info src/ft_package.egg-info 2>/dev/null || true
echo "✅ Nettoyé"
echo ""

# 3. Build le package
echo "🔨 Étape 3: Build du package"
if python -m build; then
    echo "✅ Build réussi"
else
    echo "❌ Build échoué"
    exit 1
fi
echo ""

# 4. Lister les fichiers créés
echo "📦 Étape 4: Fichiers créés"
ls -lh dist/
echo ""

# 5. Désinstaller l'ancien package si existant
echo "🗑️  Étape 5: Désinstallation de l'ancien package"
pip uninstall -y ft_package >/dev/null 2>&1 || true
echo "✅ Package désinstallé (ou non installé)"
echo ""

# 6. Installer le nouveau package
echo "📥 Étape 6: Installation du package"
if pip install ./dist/ft_package-0.0.1-py3-none-any.whl; then
    echo "✅ Package installé"
else
    echo "❌ Installation échouée"
    exit 1
fi
echo ""

# 7. Vérifier avec pip list
echo "📋 Étape 7: Vérification avec pip list"
pip list | grep ft_package
echo ""

# 8. Afficher pip show
echo "📊 Étape 8: pip show ft_package"
pip show ft_package
echo ""

# 9. Lancer le tester Python
echo "🧪 Étape 9: Lancement de ex09_ft_package_tester.py"
cd "$TESTER_DIR"
# stdout de ex09_ft_package_tester.py
output=$(python ex09_ft_package_tester.py 2>&1)
expected_output="2
0"
echo -e "\033[90mSortie obtenue:\033[0m"
echo "$output"
if [ "$output" = "$expected_output" ]; then
    echo -e "\033[92m✓ Test passed\033[0m"
else
    echo -e "\033[91m✗ Test failed\033[0m"
    echo -e "\033[90mSortie attendue:\033[0m"
    echo "$expected_output"
fi
echo ""
