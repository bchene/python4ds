#!/bin/bash
# Script pour lancer tous les tests Python_0_Starting

set +e  # Continuer même en cas d'erreur

BASE_DIR="$(cd "$(dirname "$0")" && pwd)"
DEV_DIR="$(cd "$BASE_DIR/../Python_3_OOP/" && pwd)"

cp "$DEV_DIR/ex00/S1E9.py" S1E9.py
cp "$DEV_DIR/ex01/S1E7.py" S1E7.py
cp "$DEV_DIR/ex02/DiamondTrap.py" DiamondTrap.py
cp "$DEV_DIR/ex03/ft_calculator.py" ft_calculator.py

if [ $# -eq 0 ]; then
    for i in {0..5}; do
        ./py4ds_OOP_tester.sh $i
    done
    exit 0
fi

if [ $# -eq 1 ]; then
    EX_NUM=$1
    str1="                                                       "
    str2="     PYTHON FOR DATA SCIENCE - 2 OOP - EX0${EX_NUM} TESTER     "
    echo -e "\033[7;34m${str1}\n${str2}\n${str1}\033[0m"
    case "$EX_NUM" in
        0)
            python Python_3_OOP_ex00_tester.py
            ;;
        1)
            python Python_3_OOP_ex01_tester.py
            ;;
        2)
            python Python_3_OOP_ex02_tester.py
            ;;
        3)
            cp "$DEV_DIR/ex03/ft_calculator.py" ft_calculator.py
            python Python_3_OOP_ex03_tester.py
            rm ft_calculator.py
            ;;
        4)
            cp "$DEV_DIR/ex04/ft_calculator.py" ft_calculator.py
            python Python_3_OOP_ex04_tester.py
            rm ft_calculator.py
            ;;
        *)
            echo "❌ Erreur: Exercice invalide. Utilisez un nombre de 0 à 4."
            exit 1
            ;;
    esac
    
    echo ""
    echo "✅ TEST EX0${EX_NUM} TERMINÉ"
    exit 0
fi
echo "❌ Erreur argument: Utilisez un nombre de 0 à 9."
exit 1