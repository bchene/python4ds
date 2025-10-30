# ft_filter.py
CMD="python ft_filter.py"

echo "filterstring.py 'Hello the World' 4"
python filterstring.py 'Hello the World' 4
# ['Hello', 'World']
echo ""

echo "filterstring.py 'Hello the World' 99"
python filterstring.py 'Hello the World' 99
# []
echo ""

echo "filterstring.py 3 'Hello the World'"
python filterstring.py 3 'Hello the World'
# AssertionError: the arguments are bad
echo ""

echo "filterstring.py"
python filterstring.py
# AssertionError: the arguments are bad
echo ""

echo "filterstring.py '' 5"
python filterstring.py '' 5
# []
echo ""