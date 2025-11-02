def ft_filter(function, iterable):
    """filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true."""

    try:
        if function is None:
            return [item for item in iterable if item]
        else:
            return [item for item in iterable if function(item)]

    except TypeError:
        raise AssertionError(
            f"'{type(iterable).__name__}' object is not iterable"
        )
    except Exception:
        raise AssertionError(
            f"'{type(function).__name__}' object is not callable"
        )
