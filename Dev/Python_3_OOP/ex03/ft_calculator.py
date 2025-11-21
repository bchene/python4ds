class calculator:
    '''calculator class is able to do calculations of vectors with a scalar.'''

    def __init__(self, values: list[float]) -> None:
        '''calculator constructor : calculator(values: list[float]) -> None.'''
        self.values = values

    def __add__(self, object) -> None:
        '''calculator method __add__(self, object) -> list[float] : \
adds the values of the two vectors and prints the result.'''
        object = float(object)
        self.values = [x + object for x in self.values]
        print(self.values)

    def __mul__(self, object) -> None:
        '''calculator method __mul__(self, object) -> list[float] : \
multiplies the values of the two vectors and prints the result.'''
        object = float(object)
        self.values = [x * object for x in self.values]
        print(self.values)

    def __sub__(self, object) -> None:
        '''calculator method __sub__(self, object) -> list[float] : \
subtracts the values of the two vectors with a scalar and prints the result.'''
        object = float(object)
        self.values = [x - object for x in self.values]
        print(self.values)

    def __truediv__(self, object) -> None:
        '''calculator method __truediv__(self, object) -> list[float] : \
divides the values of the two vectors with a scalar and prints the result.'''
        object = float(object)
        if object == 0:
            raise ValueError("Cannot divide by zero")
        self.values = [x / object for x in self.values]
        print(self.values)
