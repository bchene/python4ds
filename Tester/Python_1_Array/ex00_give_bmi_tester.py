from give_bmi import give_bmi, apply_limit


def test_bmi_function(
    height: list[int | float], weight: list[int | float], limit: int
) -> None:
    """Test the bmi functions with the given height and weight."""
    try:
        print(f"height = {height} - weight = {weight}")
        bmi = give_bmi(height, weight)
        print(f"give_bmi -> {bmi} {type(bmi)}")
        apply_limit_result = apply_limit(bmi, limit)
        print(f"apply_limit -> \
        {apply_limit_result} {type(apply_limit_result)}")
    except Exception as e:
        print(f"\033[91mAssertionError: {e}\033[0m")


def main():
    """Calculate the BMI of persons from a list of weights and heights."""
    try:
        print("TEST give_bmi.py:")
        print("--------------------------------")
        test_bmi_function("123", [4, 5, 6], 26)
        print("--------------------------------")
        test_bmi_function((1, 2, 3), [4, 5, 6], 26)
        print("--------------------------------")
        test_bmi_function([1, 2, 3], [4, 5], 26)
        print("--------------------------------")
        test_bmi_function([1, 2, 3], [4, 5, "a"], 26)
        print("--------------------------------")
        test_bmi_function([1, 2, 3], [4, 5, 0], 26)
        print("--------------------------------")
        test_bmi_function([1, 2, 3], [4, 5, "a"], 26)
        print("--------------------------------")
        test_bmi_function([1, 2, 3], [4, 5, 6], "26")
        print("--------------------------------")
        test_bmi_function([1, 2, 3], [4, 5, 6], -1)
        print("--------------------------------")
        test_bmi_function([2.71, 1.15], [165.3, 38.4], 26)
        print("--------------------------------")
    except Exception as e:
        print(f"\033[91mAssertionError: {e}\033[0m")
        exit(1)


if __name__ == "__main__":
    main()
