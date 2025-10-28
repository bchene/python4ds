import sys as system


def charToMorseString(char):
    """Convert a character to its Morse Code string."""
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
    if (
        not isinstance(char, str)
        or (not char.isalnum() and char != " ")
        or len(char) != 1
    ):
        raise TypeError("the arguments are bad")
    return NESTED_MORSE.get(char.upper(), "")


def textToMorseString(text):
    """Encode a text into Morse Code string."""
    morse_string = ""
    for char in text:
        morse_string += charToMorseString(char)
    return morse_string.removesuffix(" ")


def main():
    """Encode a string into Morse Code."""
    try:
        if len(system.argv) != 2:
            raise ValueError("the arguments are bad")
        if not all((c.isalnum() or c == " ") for c in system.argv[1]):
            raise ValueError("the arguments are bad")
        print(textToMorseString(system.argv[1]))
    except Exception as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()
