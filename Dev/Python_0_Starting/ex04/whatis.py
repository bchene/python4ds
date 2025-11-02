import sys as system


def string_to_integer(s: str) -> int:
    """Check if a string represents a valid integer (positive or negative).

    Args:
        s: The string to check.

    Returns:
        int: The integer value of the string.

    Raises:
        AssertionError: If the argument is not a string or an integer.
    """
    assert isinstance(s, str), "argument is not a string"
    try:
        n = int(s)
        return n
    except ValueError:
        raise AssertionError("argument is not an integer")


def even_or_odd(n: int) -> int:
    """Print if the number is even or odd.

    Args:
        n : The number to check.

    Returns:
        int: 0 if the number is even, 1 if the number is odd.

    Raises:
        ValueError: If the argument is not an integer.
    """

    assert isinstance(n, int), "argument is not an integer"
    if n % 2 == 0:
        print("I'm Even.")
        return 0
    else:
        print("I'm Odd.")
        return 1


if __name__ == "__main__":
    try:
        if len(system.argv) < 2:
            exit(0)
        assert len(system.argv) == 2, "more than one argument is provided"
        even_or_odd(string_to_integer(system.argv[1]))
        exit(0)

    except AssertionError as e:
        print(f"AssertionError : {e}")
        exit(1)
    except Exception as e:
        print(f"Exception : {e}")
        exit(1)
