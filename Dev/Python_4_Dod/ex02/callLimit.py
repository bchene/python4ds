
def callLimit(limit: int):
    '''Returns a function that limits the number of times \
a function can be called.'''
    count: int = 0

    def callLimiter(function):

        def limit_function(*args, **kwds):
            nonlocal count
            if count >= limit:
                print(f"Error: {function} called too many times")
                return None
            count += 1
            return function(*args, **kwds)
        return limit_function

    return callLimiter
