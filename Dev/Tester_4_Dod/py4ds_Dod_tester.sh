#!/bin/bash
# Script pour lancer tous les tests Python_0_Starting

set +e  # Continuer même en cas d'erreur

BASE_DIR="$(cd "$(dirname "$0")" && pwd)"
DEV_DIR="$(cd "$BASE_DIR/../Python_4_Dod/" && pwd)"

if [ $# -eq 0 ]; then
    for i in {0..3}; do
        ./py4ds_Dod_tester.sh $i
    done
    exit 0
fi

if [ $# -eq 1 ]; then
    EX_NUM=$1
    str1="                                                       "
    str2="     PYTHON FOR DATA SCIENCE - 4 DOD - EX0${EX_NUM} TESTER     "
    echo -e "\033[7;34m${str1}\n${str2}\n${str1}\n\033[0m"

    case "$EX_NUM" in
        0)
            cp "$DEV_DIR/ex00/statistics.py" statistics.py
            python Python_4_Dod_ex00_tester.py
            rm statistics.py
            ;;
        1)
            cp "$DEV_DIR/ex00/statistics.py" statistics.py
            python Python_4_Dod_ex00_tester.py
            rm statistics.py
            ;;
        2)
            cp "$DEV_DIR/ex00/statistics.py" statistics.py
            python Python_4_Dod_ex00_tester.py
            rm statistics.py
            ;;
        3)
            cp "$DEV_DIR/ex00/statistics.py" statistics.py
            python Python_4_Dod_ex00_tester.py
            rm statistics.py
            ;;
        *)
            echo "❌ Erreur: Exercice invalide. Utilisez un nombre de 0 à 4."
            exit 1
            ;;
    esac

    echo ""
    exit 0
fi
echo "❌ Erreur argument: Utilisez un nombre de 0 à 9."
exit 1