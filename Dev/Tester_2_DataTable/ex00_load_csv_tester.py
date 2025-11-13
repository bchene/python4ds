from load_csv import load


def test_load_csv_function(filename: str) -> None:
    """Test the load_csv function with the given filename."""
    try:
        str = "\n\033[2;33m"
        str += f"filename = '{filename}'"
        if len(str) > 64:
            str = str[:64] + "..."
        elif len(str) < 64:
            str = str + " " * (64 - len(str))
        str += "\033[0m"
        print(str)

        data = load(filename)
        if data is None:
            print("-> None returned")
        else:
            print(data)

    except Exception as e:
        print(f"\033[91mAssertionError: {e}\033[0m")


def main():
    """Calculate the BMI of persons from a list of weights and heights."""
    try:
        test_load_csv_function("")
        test_load_csv_function("data_files/")
        test_load_csv_function("not_a_file")
        test_load_csv_function("ex00_load_csv_tester.py")
        test_load_csv_function("data_files/unreadable.csv")
        test_load_csv_function("data_files/life_expectancy_years.csv")
    except Exception as e:
        print(f"\033[91mAssertionError: {e}\033[0m")
        exit(1)


if __name__ == "__main__":
    main()
