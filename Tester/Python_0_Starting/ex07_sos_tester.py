from sos import textToMorseString

if __name__ == "__main__":

    testList = [
        ["HELLO", ".... . .-.. .-.. ---", None],
        ["HELLO WORLD", ".... . .-.. .-.. --- / .-- --- .-. .-.. -..", None],
        ["SOS", "... --- ...", None],
        [None, None, "argument must be a string"],
        ["", "", None],  # Chaîne vide retourne une chaîne vide
        ["HellU$$ $$ Worldu$$", None,
         "argument must be a string of alphanumeric characters or spaces"],
        ["1234567890",
         ".---- ..--- ...-- ....- ..... -.... --... ---.. ----. -----", None],
        ["!@#$%^&*()", None,
         "argument must be a string of alphanumeric characters or spaces"],
    ]

    for test in testList:
        input_val, expected_result, expected_error = test
        print(f"\033[90mpython sos.py {input_val}\033[0m")

        try:
            result = textToMorseString(input_val)
            if expected_error is None:
                # Test de succès attendu
                if result == expected_result:
                    print(result)
                    print("\033[92m✓ Test passed\033[0m")
                else:
                    print(result)
                    print("\033[91m✗ Test failed\033[0m")
                    print(f"\033[90mExpected: {expected_result}\033[0m")
                    print(f"\033[90mGot: {result}\033[0m")
            else:
                # Une erreur était attendue mais la fonction a réussi
                print(result)
                print("\033[91m✗ Test failed\033[0m")
                print(f"\033[90mExpected error: {expected_error}\033[0m")
                print(f"\033[90mGot result instead: {result}\033[0m")
        except AssertionError as e:
            error_msg = str(e)
            if expected_error is not None:
                # Une erreur était attendue
                if expected_error in error_msg:
                    print(f"AssertionError: {error_msg}")
                    print("\033[92m✓ Test passed\033[0m")
                else:
                    print(f"AssertionError: {error_msg}")
                    print("\033[91m✗ Test failed\033[0m")
                    print(f"\033[90mExpected error: {expected_error}\033[0m")
                    print(f"\033[90mGot error: {error_msg}\033[0m")
            else:
                # Une erreur s'est produite mais ce n'était pas attendu
                print(f"AssertionError: {error_msg}")
                print("\033[91m✗ Test failed\033[0m")
                print(f"\033[90mExpected result: {expected_result}\033[0m")
        print()
