from building import textStatistics
from unittest import TestCase, TextTestRunner
from unittest.mock import patch
import io as io_string
import unittest as unittest_lib


def io_capture(function, *args, **kwargs) -> str:
    captured_output = io_string.StringIO()
    with patch("sys.stdout", captured_output):
        function(*args, **kwargs)
        return captured_output.getvalue().strip()


class TestTextStatistics(TestCase):
    # Test 1: Texte du sujet
    def test_subject_case(self):
        text1 = (
            "Python 3.0, released in 2008, was a major revision "
            "that is not completely backward compatible with earlier "
            "versions. Python 2 was discontinued with version 2.7.18 "
            "in 2020."
        )
        expected_result = (
            "The text contains 171 characters:\n"
            "2 upper letters\n"
            "121 lower letters\n"
            "7 punctuation marks\n"
            "26 spaces\n"
            "15 digits"
        )

        print("\033[90mSubject case :\n\033[0m" + text1)
        result = io_capture(textStatistics, text1)
        print("\033[90mResult :\n\033[0m" + result)
        try:
            self.assertEqual(result, expected_result)
            print("\033[92m✓ Test passed\033[0m\n")
        except AssertionError:
            print("\033[91m✗ Test failed\033[0m\n")
            raise

    # Test 2: Texte simple 'Hello World'
    def test_simple_text(self):
        text2 = "Hello World"
        expected_result = (
            "The text contains 11 characters:\n"
            "2 upper letters\n"
            "8 lower letters\n"
            "0 punctuation marks\n"
            "1 spaces\n"
            "0 digits"
        )

        print("\033[90mSimple text :\n\033[0m" + text2)
        result = io_capture(textStatistics, text2)
        print("\033[90mResult :\n\033[0m" + result)
        try:
            self.assertEqual(result, expected_result)
            print("\033[92m✓ Test passed\033[0m\n")
        except AssertionError:
            print("\033[91m✗ Test failed\033[0m\n")
            raise

    # Test 3: Texte complexe 'ABC abc 123 !@#'
    def test_complex_text(self):
        text3 = "ABC abc 123 !@#"
        expected_result = (
            "The text contains 15 characters:\n"
            "3 upper letters\n"
            "3 lower letters\n"
            "3 punctuation marks\n"
            "3 spaces\n"
            "3 digits"
        )

        print("\033[90mComplex text :\n\033[0m" + text3)
        result = io_capture(textStatistics, text3)
        print("\033[90mResult :\n\033[0m" + result)
        try:
            self.assertEqual(result, expected_result)
            print("\033[92m✓ Test passed\033[0m\n")
        except AssertionError:
            print("\033[91m✗ Test failed\033[0m\n")
            raise


if __name__ == "__main__":
    stream = io_string.StringIO()
    runner = TextTestRunner(stream=stream, verbosity=0)
    suite = unittest_lib.TestLoader().loadTestsFromTestCase(TestTextStatistics)
    result = runner.run(suite)
    if result.wasSuccessful():
        tests_count = result.testsRun
        print(
            f"\033[92m✓ Tous les tests ont réussi ({tests_count} tests)\033[0m"
        )
    else:
        failures = len(result.failures)
        errors = len(result.errors)
        print(f"\033[91m✗ {failures} échec(s), {errors} erreur(s)\033[0m")
