#!/bin/bash
# Script pour lancer tous les tests Python_0_Starting

set +e  # Continuer même en cas d'erreur

BASE_DIR="$(cd "$(dirname "$0")" && pwd)"
DEV_DIR="$(cd "$BASE_DIR/../../Dev/Python_1_Array" && pwd)"

if [ $# -eq 0 ]; then
    for i in {0..5}; do
        ./py4ds_array_tester.sh $i
    done
    exit 0
fi

if [ $# -eq 1 ]; then
    EX_NUM=$1
    str1="                                                         "
    str2="     PYTHON FOR DATA SCIENCE - 1 ARRAY - EX0${EX_NUM} TESTER     "
    echo -e "\033[7;34m${str1}\n${str2}\n${str1}\033[0m"
    case "$EX_NUM" in
        0)
            cp "$DEV_DIR/ex00/give_bmi.py" .
            python ex00_give_bmi_tester.py
            rm give_bmi.py
            ;;
        1)
            cp "$DEV_DIR/ex01/array2D.py" .
            python ex01_slice_me_tester.py
            rm array2D.py
            ;;
        2)
            cp "$DEV_DIR/ex02/load_image.py" .
            python ex02_load_image_tester.py
            rm load_image.py
            ;;
        3)
            cp "$DEV_DIR/ex03/zoom.py" "$DEV_DIR/ex03/load_image.py" .
            python zoom.py
            rm zoom.py load_image.py
            ;;
        4)
            cp "$DEV_DIR/ex04/rotate.py" "$DEV_DIR/ex04/load_image.py" .
            python rotate.py
            rm rotate.py load_image.py
            ;;
        5)
            # TODO: Add the tester for the ex05
            cp "$DEV_DIR/ex05/pimp_image.py" "$DEV_DIR/ex05/load_image.py" .
            python ex05_pimp_image_tester.py
            rm pimp_image.py load_image.py
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