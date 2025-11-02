import sys as system


def is_punctuation(c: str) -> bool:
    """Check if a character is a punctuation mark.

Args:
    c: The character to check.

Returns:
    bool: True if the character is a punctuation mark, False otherwise.
    """
    if not isinstance(c, str) or len(c) != 1:
        return False
    return c in r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""


def textStatistics(text):
    """
Print the statistics of the text.

Args:
    text: The text to count.

Returns:
    None

Raises:
    AssertionError: If the text is not a string.
    """
    assert isinstance(text, str), "text must be a string"
    upper_count = sum(1 for c in text if c.isupper())
    lower_count = sum(1 for c in text if c.islower())
    punct_count = sum(1 for c in text if is_punctuation(c))
    space_count = sum(1 for c in text if c.isspace())
    digit_count = sum(1 for c in text if c.isdigit())
    print(f"The text contains {len(text)} characters:")
    print(f"{upper_count} upper letters")
    print(f"{lower_count} lower letters")
    print(f"{punct_count} punctuation marks")
    print(f"{space_count} spaces")
    print(f"{digit_count} digits")


def main():
    """
Get the statistics of the first argument text.
If no argument is provided, ask the user for a text.

Args:
    system.argv: The arguments passed to the program.

Raises:
    AssertionError: If the number of arguments is greater than 1.
    Exception: If the input is not a string.
    """
    try:
        assert len(system.argv) <= 2, \
            "too many arguments, maximum is 1"
        assert len(system.argv) == 2 and isinstance(system.argv[0], str), \
            "argument must be a string"

        s = ""
        if len(system.argv) == 2:
            s = system.argv[1]
        else:
            while s == "":
                s = input("Enter a text: ")

        textStatistics(s)
        exit(0)

    except AssertionError as e:
        print(f"AssertionError: {e}")
        exit(1)
    except Exception as e:
        print(f"Exception: {e}")
        exit(1)


if __name__ == "__main__":
    main()
