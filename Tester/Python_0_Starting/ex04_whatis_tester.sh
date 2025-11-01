# whatis.py
CMD="python whatis.py"
# Arguments à tester
args=("14" "-5" "" "0" "Hi!" "13 5")

# Affichage
for arg in "${args[@]}"
do
    echo "\$> $CMD $arg"
    eval $CMD $arg
    echo '$>'
done
