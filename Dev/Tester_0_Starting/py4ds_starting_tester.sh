#!/bin/bash
# Script pour lancer tous les tests Python_0_Starting

set +e  # Continuer même en cas d'erreur

BASE_DIR="$(cd "$(dirname "$0")" && pwd)"
DEV_DIR="$(cd "$BASE_DIR/../Python_0_Starting" && pwd)"

if [ $# -eq 0 ]; then
    for i in {0..9}; do
        ./py4ds_starting_tester.sh $i
    done
    exit 0
fi

if [ $# -eq 1 ]; then
    EX_NUM=$1
    echo -e "\033[96m==========================================================\033[0m"
    echo -e "\033[96mPYTHON FOR DATA SCIENCE - 0 STARTING - EX0${EX_NUM} TESTER\033[0m"
    echo -e "\033[96m==========================================================\033[0m"
    
    case "$EX_NUM" in
        0)
            cd "$DEV_DIR/ex00"
            python Hello.py | cat -e
            ;;
        1)
            cd "$DEV_DIR/ex01"
            python format_ft_time.py
            ;;
        2)
            cd "$DEV_DIR/ex02"
            cp "$BASE_DIR/ex02_find_ft_type_tester.py" .
            python ex02_find_ft_type_tester.py | cat -e
            rm ex02_find_ft_type_tester.py
            ;;
        3)
            cd "$DEV_DIR/ex03"
            cp "$BASE_DIR/ex03_NULL_not_found_tester.py" .
            python ex03_NULL_not_found_tester.py | cat -e
            rm ex03_NULL_not_found_tester.py
            ;;
        4)
            cd "$DEV_DIR/ex04"
            cp "$BASE_DIR/ex04_whatis_tester.sh" .
            bash ex04_whatis_tester.sh
            rm ex04_whatis_tester.sh
            ;;
        5)
            cd "$DEV_DIR/ex05"
            cp "$BASE_DIR/ex05_building_tester.py" .
            python ex05_building_tester.py
            rm ex05_building_tester.py
            ;;
        6)
            cd "$DEV_DIR/ex06"
            cp "$BASE_DIR/ex06_ft_filter_doc_tester.py" .
            python ex06_ft_filter_doc.py
            rm ex06_ft_filter_doc.py
            cp "$BASE_DIR/ex06_ft_filter_tester.sh" .
            bash ex06_ft_filter_tester.sh
            rm ex06_ft_filter_tester.sh
            ;;
        7)
            cd "$DEV_DIR/ex07"
            cp "$BASE_DIR/ex07_sos_tester.py" .
            python ex07_sos_tester.py
            rm ex07_sos_tester.py
            ;;
        8)
            cd "$DEV_DIR/ex08"
            cp "$BASE_DIR/ex08_Loading_tester.py" .
            python ex08_Loading_tester.py 2>&1 | head -10 || echo "⚠️ Ex08 nécessite terminal interactif"
            rm ex08_Loading_tester.py
            ;;
        9)
            cd "$BASE_DIR"
            ./ex09_full_test.sh
            ;;
        *)
            echo "❌ Erreur: Exercice invalide. Utilisez un nombre de 0 à 9."
            exit 1
            ;;
    esac
    
    exit 0
fi
echo "❌ Erreur argument: Utilisez un nombre de 0 à 9."
exit 1