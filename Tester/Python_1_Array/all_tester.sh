#!/bin/bash
# Script pour lancer tous les tests Python_0_Starting

set +e  # Continuer même en cas d'erreur

BASE_DIR="$(cd "$(dirname "$0")" && pwd)"
DEV_DIR="$(cd "$BASE_DIR/../../Dev/Python_1_Array" && pwd)"

if [ $# -eq 1 ]; then
    EX_NUM=$1
    echo "========================================================"
    echo "PYTHON FOR DATA SCIENCE - 1 ARRAY - EX0${EX_NUM} TESTER"
    echo "========================================================"
    echo ""
    
    case "$EX_NUM" in
        0)
            cd "$DEV_DIR/ex00"
            cp "$BASE_DIR/ex00_give_bmi_tester.py" .
            python ex00_give_bmi_tester.py | cat -e
            rm ex00_give_bmi_tester.py
            ;;
        1)
            # TODO: Add the tester for the ex01
            ;;
        2)
            # TODO: Add the tester for the ex02
            ;;
        3)
            # TODO: Add the tester for the ex03
            ;;
        4)
            # TODO: Add the tester for the ex04
            ;;
        5)
            # TODO: Add the tester for the ex05
            ;;
        *)
            echo "❌ Erreur: Exercice invalide. Utilisez un nombre de 0 à 9."
            exit 1
            ;;
    esac
    
    echo ""
    echo "✅ TEST EX0${EX_NUM} TERMINÉ"
    exit 0
fi
echo "❌ Erreur argument: Utilisez un nombre de 0 à 9."
exit 1