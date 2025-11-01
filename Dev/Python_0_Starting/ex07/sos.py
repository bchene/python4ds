import sys as system


def charToMorseString(char):
    """Convert a character to its Morse Code string.

    Args:
        char: The character to convert.

    Returns:
        The Morse Code string.

    Raises:
        AssertionError: If the character is not a single alphanumeric \
        character or a space.
    """

    NESTED_MORSE = {
        " ": "/ ",
        "A": ".- ",
        "B": "-... ",
        "C": "-.-. ",
        "D": "-.. ",
        "E": ". ",
        "F": "..-. ",
        "G": "--. ",
        "H": ".... ",
        "I": ".. ",
        "J": ".--- ",
        "K": "-.- ",
        "L": ".-.. ",
        "M": "-- ",
        "N": "-. ",
        "O": "--- ",
        "P": ".--. ",
        "Q": "--.- ",
        "R": ".-. ",
        "S": "... ",
        "T": "- ",
        "U": "..- ",
        "V": "...- ",
        "W": ".-- ",
        "X": "-..- ",
        "Y": "-.-- ",
        "Z": "--.. ",
        "1": ".---- ",
        "2": "..--- ",
        "3": "...-- ",
        "4": "....- ",
        "5": "..... ",
        "6": "-.... ",
        "7": "--... ",
        "8": "---.. ",
        "9": "----. ",
        "0": "----- ",
    }
    assert (
        isinstance(char, str)
        and (char.isalnum() or char == " ")
        and len(char) == 1
    ), "argument must be a string of alphanumeric characters or spaces"

    return NESTED_MORSE.get(char.upper(), "")


def textToMorseString(text):
    """Encode a text into Morse Code string.

    Args:
        text: The text to encode.

    Returns:
        The Morse Code string.

    Raises:
        AssertionError: If the text is not a string.
    """
    assert isinstance(text, str), "argument must be a string"
    morse_string = ""
    for char in text:
        morse_string += charToMorseString(char)
    return morse_string.removesuffix(" ")


def main():
    """Encode a string into Morse Code."""
    try:
        assert len(system.argv) == 2, "1 argument is required"
        print(textToMorseString(system.argv[1]))
        exit(0)
    except AssertionError as e:
        print(f"AssertionError: {e}")
        exit(1)
    except Exception as e:
        print(f"Exception: {e}")


if __name__ == "__main__":
    main()
