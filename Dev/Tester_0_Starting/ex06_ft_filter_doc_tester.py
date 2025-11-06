import ft_filter as my
import io as io_string
from unittest.mock import patch

if __name__ == "__main__":
    captured_output1 = io_string.StringIO()
    with patch('sys.stdout', captured_output1):
        print(filter.__doc__)
        original = captured_output1.getvalue().strip()

    captured_output2 = io_string.StringIO()
    with patch('sys.stdout', captured_output2):
        print(my.ft_filter.__doc__)
        copy = captured_output2.getvalue().strip()

    print("\033[90mfilter.__doc__:\n\033[0m" + original)
    print("\033[90mft_filter.__doc__:\n\033[0m" + copy)
    if original == copy:
        print("\033[92m✓ Test passed\033[0m\n")
    else:
        print("\033[91m✗ Test failed\033[0m\n")
