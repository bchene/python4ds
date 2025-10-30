def ft_filter(function, iterable):
    """\
Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true."""

    try:
        if function is None:
            # if function is None, get List of items that are not 'Falsy'
            return [item for item in iterable if item]
        else:
            # else, get List of items that are true according to the function.
            return [item for item in iterable if function(item)]

    # Handle the case where the iterable is not iterable
    except TypeError:
        raise TypeError(f"'{type(iterable).__name__}' object is not iterable")


print("--------------------------------")# A EFFACER
print(filter.__doc__)# A EFFACER
print("--------------------------------")# A EFFACER
print(ft_filter.__doc__)# A EFFACER
print("--------------------------------")# A EFFACER
