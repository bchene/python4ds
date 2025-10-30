import sys as system


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
    punctuations = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
    punct_count = sum(1 for c in text if c in punctuations)
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
        AssertionError: If the number of arguments is not 0 or 1.
        Exception: If the input is not a string.
    """
    try:
        assert len(system.argv) <= 2, "at most one argument is allowed"

        if len(system.argv) == 2 and system.argv[1] != "":
            s = system.argv[1]
        else:
            # 0 argument ou argument vide -> demander un texte non vide
            s = ""
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
