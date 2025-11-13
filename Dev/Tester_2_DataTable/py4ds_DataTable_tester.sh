#!/bin/bash
# Script pour lancer tous les tests Python_0_Starting

set +e  # Continuer même en cas d'erreur

BASE_DIR="$(cd "$(dirname "$0")" && pwd)"
DEV_DIR="$(cd "$BASE_DIR/../Python_2_DataTable" && pwd)"

if [ ! -d "ex00" ]; then
    mkdir ex00
fi
cp "$DEV_DIR/ex00/load_csv.py" ex00/load_csv.py

if [ $# -eq 0 ]; then
    for i in {0..3}; do
        ./py4ds_DataTable_tester.sh $i
    done
    exit 0
fi

if [ $# -eq 1 ]; then
    EX_NUM=$1
    str1="                                                              "
    str2="     PYTHON FOR DATA SCIENCE - 2 DATA TABLE - EX0${EX_NUM} TESTER     "
    echo -e "\033[7;34m${str1}\n${str2}\n${str1}\033[0m"
    case "$EX_NUM" in
        0)
            cp "$DEV_DIR/ex00/load_csv.py" .
            python ex00_load_csv_tester.py
            rm load_csv.py
            ;;
        1)
            cp "$DEV_DIR/ex01/aff_life.py" .
            cp data_files/life_expectancy_years.csv .
            python aff_life.py
            rm aff_life.py life_expectancy_years.csv
            ;;
        2)
            cp "$DEV_DIR/ex02/aff_pop.py" .
            cp data_files/population_total.csv .
            python aff_pop.py
            rm aff_pop.py population_total.csv
            ;;
        3)
            cp "$DEV_DIR/ex03/projection_life.py" .
            cp data_files/life_expectancy_years.csv .
            cp data_files/income_per_person_gdppercapita_ppp_inflation_adjusted.csv .
            python projection_life.py
            rm projection_life.py life_expectancy_years.csv income_per_person_gdppercapita_ppp_inflation_adjusted.csv
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