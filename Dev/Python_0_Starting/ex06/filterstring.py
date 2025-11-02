import sys as system
import ft_filter as my


def main():
    """
    Output a list of words from the first argument (string) that have a
    length greater than the second argument (int).

    Args:
        system.argv: The arguments passed to the program.

    Raises:
        AssertionError: If the number of arguments is not 3 or
        the second argument is not an integer or the first
        argument is not a string.
        Exception: If the iterable is not iterable.
    """
    try:
        assert len(system.argv) == 3, \
            "Two arguments are required (string and integer)"
        assert isinstance(system.argv[1], str), \
            "first argument must be a string"
        assert isinstance(system.argv[2], str) and system.argv[2].isdigit(), \
            "second argument must be a positive integer (only digits)"

        word_list = [
            word for word in system.argv[1].split(" ") if word.isalnum()
        ]
        size = int(system.argv[2])

        print(my.ft_filter(lambda x: len(x) > size, word_list))
        exit(0)

    except AssertionError as e:
        print(f"AssertionError: {e}")
        exit(1)
    except Exception as e:
        print(f"Exception: {e}")
        exit(1)


if __name__ == "__main__":
    main()
