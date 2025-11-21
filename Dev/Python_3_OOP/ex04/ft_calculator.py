class calculator:
    '''calculator class is able to do calculations of 2 vectors.'''

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        '''calculator method dotproduct(list[float], list[float]) -> None: \
calculates the dot product of two vectors and prints the result \
without instantiating its class.'''
        res: float = 0
        for val1, val2 in zip(V1, V2):
            res += float(val1 * val2)
        print(f"Dot product is: {res}")

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        '''calculator method add_vec(list[float], list[float]) -> None: \
adds the values of the two vectors and prints the result \
without instantiating its class.'''
        res = [float(val1 + val2) for val1, val2 in zip(V1, V2)]
        print(f"Add Vector is: {res}")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        '''calculator method sous_vec(list[float], list[float]) -> None: \
subtracts the values of the two vectors and prints the result \
without instantiating its class.'''
        res = [float(val1 - val2) for val1, val2 in zip(V1, V2)]
        print(f"Sous Vector is: {res}")
