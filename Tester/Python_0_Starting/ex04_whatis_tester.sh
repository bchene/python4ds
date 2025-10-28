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

# Expected output:
# 
# $> python whatis.py 14
# I'm Even.
# $>
# $> python whatis.py -5
# I'm Odd.
# $>
# $> python whatis.py
# $>
# $> python whatis.py 0
# I'm Even.
# $>
# $> python whatis.py Hi!
# AssertionError: argument is not an integer
# $>
# $> python whatis.py 13 5
# AssertionError: more than one argument is provided
# $>
