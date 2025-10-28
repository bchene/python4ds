import sys as system


def textStatistics(text):
    """Print the statistics of the text."""
    upper_count = sum(1 for c in text if c.isupper())
    lower_count = sum(1 for c in text if c.islower())
    punct_count = sum(1 for c in text if c in "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~")
    space_count = sum(1 for c in text if c.isspace())
    digit_count = sum(1 for c in text if c.isdigit())

    print(f"The text contains {len(text)} characters:")
    print(f"{upper_count} upper letters")
    print(f"{lower_count} lower letters")
    print(f"{punct_count} punctuation marks")
    print(f"{space_count} spaces")
    print(f"{digit_count} digits")


def main():
    """Get the statistics of the first argument text."""
    try:
        if len(system.argv) > 2:
            raise ValueError(
                "too many arguments (only one string argument is required)"
            )
        elif len(system.argv) < 2 or system.argv[1] == None or system.argv[1] == "":
            print("One string argument is required")
            exit(0)
        textStatistics(system.argv[1])
        exit(0)

    except Exception as e:
        print(f"AssertionError: {e}")
        exit(1)


if __name__ == "__main__":
    main()
