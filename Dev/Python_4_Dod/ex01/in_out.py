def square(x: int | float) -> int | float:
    '''Returns the square of a number.'''
    return x ** 2


def pow(x: int | float) -> int | float:
    '''Returns the power of the number to the power of itself.'''
    return x ** x


def outer(x: int | float, function) -> object:
    '''Returns an object that when called returns the result \
of the function called on the last result.'''
    result: int | float = x

    def inner() -> float:
        '''Returns the result of the function called on the last result.'''
        nonlocal result
        result = function(result)
        return result
    return inner
