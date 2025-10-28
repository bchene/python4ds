import sys as system


def even_or_odd(n):
    """Print if the number is even or odd.

    Args:
        n : The number to check.

    Returns:
        int: 0 if the number is even, 1 if the number is odd.

    Raises:
        ValueError: If the argument is not an integer.
    
    """
    try:
        n = int(n)
    except ValueError:
        raise ValueError("argument is not an integer")
    if n % 2 == 0:
        print("I'm Even.")
        return 0
    else:
        print("I'm Odd.")
        return 1


if __name__ == "__main__":
    try:
        if len(system.argv) > 2:
            raise ValueError("more than one argument is provided")
        if len(system.argv) == 2:
            even_or_odd(system.argv[1])
        exit(0)
    
    except Exception as e:
        print(f"AssertionError: {e}")
        exit(1)

