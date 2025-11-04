import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """
    Takes as parameters a 2D array, prints the shape of a 2D array and returns
    a truncated version based on the provided start and end arguments.

    Args:
        family: 2D array (list of lists)
        start: start index (can be negative, like numpy slicing)
        end: end index (can be negative, like numpy slicing)

    Returns:
        truncated version of the array as a list

    Raises:
        AssertionError: If the family is not a 2D array.
        AssertionError: If the start is not an integer.
        AssertionError: If the end is not an integer.
    """
    assert isinstance(family, list), "family must be a 2D Array (ndim >= 2)"
    assert len(family) > 0, "family must be a 2D Array (ndim >= 2)"
    for item in family:
        assert isinstance(item, list), "family must be a 2D Array (ndim >= 2)"
    assert isinstance(start, int), "start must be an integer"
    assert isinstance(end, int), "end must be an integer"

    np_family = np.array(family)
    assert np_family.ndim >= 2, "family must be a 2D Array (ndim >= 2)"
    print(np_family.shape)
    return np_family[start:end].tolist()
