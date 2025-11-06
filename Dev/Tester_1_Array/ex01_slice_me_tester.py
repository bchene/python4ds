from array2D import slice_me
from unittest import TestCase, TextTestRunner
from unittest.mock import patch
import io
import unittest


def capture_output(function, *args, **kwargs):
    """Capture la sortie stdout d'une fonction et retourne le résultat."""
    captured_output = io.StringIO()
    with patch("sys.stdout", captured_output):
        result = function(*args, **kwargs)
        output = captured_output.getvalue().strip()
    return result, output


class TestSliceMe(TestCase):
    """Tests pour la fonction slice_me."""

    def test_01_basic_slice(self):
        """Test 1: Cas basique avec start=0, end=2"""
        family = [[1.80, 78.4], [2.15, 102.7], [2.10, 98.5], [1.88, 75.2]]
        start = 0
        end = 2

        print(f"\033[2;34mTest 1 : slice_me({family}, {start}, {end})\033[0m")
        result, output = capture_output(slice_me, family, start, end)
        print(f"\033[0m{output}\033[0m")
        print(f"\033[0m{result}\033[0m")
        print("\033[92mOK\033[0m\n")

        expected = [[1.80, 78.4], [2.15, 102.7]]
        self.assertEqual(result, expected)
        self.assertEqual(output, "(4, 2)")

    def test_02_negative_end(self):
        """Test 2: Cas avec end négatif"""
        family = [[1.80, 78.4], [2.15, 102.7], [2.10, 98.5], [1.88, 75.2]]
        start = 1
        end = -2

        print(f"\033[2;34mTest 2 : slice_me({family}, {start}, {end})\033[0m")
        result, output = capture_output(slice_me, family, start, end)
        print(f"\033[0m{output}\033[0m")
        print(f"\033[0m{result}\033[0m")
        print("\033[92mOK\033[0m\n")

        expected = [[2.15, 102.7]]
        self.assertEqual(result, expected)
        self.assertEqual(output, "(4, 2)")

    def test_03_full_array(self):
        """Test 3: Slice du début à la fin"""
        family = [[1, 2], [3, 4], [5, 6]]
        start = 0
        end = 3

        print(f"\033[2;34mTest 3 : slice_me({family}, {start}, {end})\033[0m")
        result, output = capture_output(slice_me, family, start, end)
        print(f"\033[0m{output}\033[0m")
        print(f"\033[0m{result}\033[0m")
        print("\033[92mOK\033[0m\n")

        self.assertEqual(result, family)
        self.assertEqual(output, "(3, 2)")

    def test_04_negative_start(self):
        """Test 4: Slice avec start négatif"""
        family = [[1, 2], [3, 4], [5, 6], [7, 8]]
        start = -2
        end = 4

        print(f"\033[2;34mTest 4 : slice_me({family}, {start}, {end})\033[0m")
        result, output = capture_output(slice_me, family, start, end)
        print(f"\033[0m{output}\033[0m")
        print(f"\033[0m{result}\033[0m")
        print("\033[92mOK\033[0m\n")

        expected = [[5, 6], [7, 8]]
        self.assertEqual(result, expected)
        self.assertEqual(output, "(4, 2)")

    def test_05_both_negative(self):
        """Test 5: Slice avec start et end négatifs"""
        family = [[1, 2], [3, 4], [5, 6], [7, 8]]
        start = -3
        end = -1

        print(f"\033[2;34mTest 5 : slice_me({family}, {start}, {end})\033[0m")
        result, output = capture_output(slice_me, family, start, end)
        print(f"\033[0m{output}\033[0m")
        print(f"\033[0m{result}\033[0m")
        print("\033[92mOK\033[0m\n")

        expected = [[3, 4], [5, 6]]
        self.assertEqual(result, expected)
        self.assertEqual(output, "(4, 2)")

    def test_06_empty_slice_end_before_start(self):
        """Test 6: Slice vide (end < start)"""
        family = [[1, 2], [3, 4], [5, 6]]
        start = 2
        end = 1

        print(f"\033[2;34mTest 6 : slice_me({family}, {start}, {end})\033[0m")
        result, output = capture_output(slice_me, family, start, end)
        print(f"\033[0m{output}\033[0m")
        print(f"\033[0m{result}\033[0m")
        print("\033[92mOK\033[0m\n")

        self.assertEqual(result, [])
        self.assertEqual(output, "(3, 2)")

    def test_07_empty_slice_negative(self):
        """Test 7: Slice vide avec indices négatifs inversés"""
        family = [[1, 2], [3, 4], [5, 6]]
        start = -1
        end = -3

        print(f"\033[2;34mTest 7 : slice_me({family}, {start}, {end})\033[0m")
        result, output = capture_output(slice_me, family, start, end)
        print(f"\033[0m{output}\033[0m")
        print(f"\033[0m{result}\033[0m")
        print("\033[92mOK\033[0m\n")

        self.assertEqual(result, [])
        self.assertEqual(output, "(3, 2)")

    def test_08_single_element(self):
        """Test 8: Slice d'un seul élément"""
        family = [[1, 2], [3, 4], [5, 6]]
        start = 1
        end = 2

        print(f"\033[2;34mTest 8 : slice_me({family}, {start}, {end})\033[0m")
        result, output = capture_output(slice_me, family, start, end)
        print(f"\033[0m{output}\033[0m")
        print(f"\033[0m{result}\033[0m")
        print("\033[92mOK\033[0m\n")

        expected = [[3, 4]]
        self.assertEqual(result, expected)
        self.assertEqual(output, "(3, 2)")

    def test_09_out_of_bounds_end(self):
        """Test 9: end hors limites"""
        family = [[1, 2], [3, 4]]
        start = 0
        end = 10

        print(f"\033[2;34mTest 9 : slice_me({family}, {start}, {end})\033[0m")
        result, output = capture_output(slice_me, family, start, end)
        print(f"\033[0m{output}\033[0m")
        print(f"\033[0m{result}\033[0m")
        print("\033[92mOK\033[0m\n")

        self.assertEqual(result, family)
        self.assertEqual(output, "(2, 2)")

    def test_10_from_beginning(self):
        """Test 10: Slice depuis le début"""
        family = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        start = 0
        end = 2

        print(f"\033[2;34mTest 10 : slice_me({family}, {start}, {end})\033[0m")
        result, output = capture_output(slice_me, family, start, end)
        print(f"\033[0m{output}\033[0m")
        print(f"\033[0m{result}\033[0m")
        print("\033[92mOK\033[0m\n")

        expected = [[1, 2, 3], [4, 5, 6]]
        self.assertEqual(result, expected)
        self.assertEqual(output, "(3, 3)")

    def test_11_not_a_list(self):
        """Test 11: family n'est pas une liste"""
        family = "not a list"
        start = 0
        end = 2

        print(f"\033[2;34mTest 11 : slice_me({family}, {start}, {end})\033[0m")
        try:
            slice_me(family, start, end)
            self.fail("AssertionError should have been raised")
        except AssertionError as e:
            print(f"\033[91mAssertionError: {e}\033[0m")
            self.assertEqual(str(e), "family must be a 2D Array (ndim >= 2)")
            print("\033[92mOK\033[0m\n")

    def test_12_empty_list(self):
        """Test 12: family est une liste vide"""
        family = []
        start = 0
        end = 2

        print(f"\033[2;34mTest 12 : slice_me({family}, {start}, {end})\033[0m")
        try:
            slice_me(family, start, end)
            self.fail("AssertionError should have been raised")
        except AssertionError as e:
            print(f"\033[91mAssertionError: {e}\033[0m")
            self.assertEqual(str(e), "family must be a 2D Array (ndim >= 2)")
            print("\033[92mOK\033[0m\n")

    def test_13_not_2d_array(self):
        """Test 13: family n'est pas un 2D array (1D)"""
        family = [1, 2, 3, 4]
        start = 0
        end = 2

        print(f"\033[2;34mTest 13 : slice_me({family}, {start}, {end})\033[0m")
        try:
            slice_me(family, start, end)
            self.fail("AssertionError should have been raised")
        except AssertionError as e:
            print(f"\033[91mAssertionError: {e}\033[0m")
            self.assertEqual(str(e), "family must be a 2D Array (ndim >= 2)")
            print("\033[92mOK\033[0m\n")

    def test_14_start_not_int(self):
        """Test 14: start n'est pas un entier"""
        family = [[1, 2], [3, 4]]
        start = "0"
        end = 2

        print(f"\033[2;34mTest 14 : slice_me({family}, {start}, {end})\033[0m")
        try:
            slice_me(family, start, end)
            self.fail("AssertionError should have been raised")
        except AssertionError as e:
            print(f"\033[91mAssertionError: {e}\033[0m")
            self.assertEqual(str(e), "start must be an integer")
            print("\033[92mOK\033[0m\n")

    def test_15_end_not_int(self):
        """Test 15: end n'est pas un entier"""
        family = [[1, 2], [3, 4]]
        start = 0
        end = "2"

        print(f"\033[2;34mTest 15 : slice_me({family}, {start}, {end})\033[0m")
        try:
            slice_me(family, start, end)
            self.fail("AssertionError should have been raised")
        except AssertionError as e:
            print(f"\033[91mAssertionError: {e}\033[0m")
            self.assertEqual(str(e), "end must be an integer")
            print("\033[92mOK\033[0m\n")

    def test_16_mixed_list_not_2d(self):
        """Test 16: family contient des éléments non-listes"""
        family = [[1, 2], 3, [4, 5]]
        start = 0
        end = 2

        print(f"\033[2;34mTest 16 : slice_me({family}, {start}, {end})\033[0m")
        try:
            slice_me(family, start, end)
            self.fail("AssertionError should have been raised")
        except AssertionError as e:
            print(f"\033[91mAssertionError: {e}\033[0m")
            self.assertEqual(str(e), "family must be a 2D Array (ndim >= 2)")
            print("\033[92mOK\033[0m\n")


if __name__ == "__main__":
    stream = io.StringIO()
    runner = TextTestRunner(stream=stream, verbosity=0)
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSliceMe)
    result = runner.run(suite)
    if result.wasSuccessful():
        tests_count = result.testsRun
        print(f"\033[92m✓ Tous les tests sont réussi ({tests_count})\033[0m")
    else:
        failures = len(result.failures)
        errors = len(result.errors)
        print(f"\033[91m✗ {failures} échec(s), {errors} erreur(s)\033[0m")
