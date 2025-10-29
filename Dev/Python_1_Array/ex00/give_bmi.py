import numpy as np


def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    """Calculate the BMI of persons from a list of weights and heights."""
    try:
        # Check if the arguments are valid.
        if not isinstance(height, list) or not isinstance(weight, list):
            raise ValueError("height and weight lists are required")
        if not all(isinstance(c, (float, int)) for c in height):
            raise ValueError("height lists must be lists of floats or integers")
        if not all(isinstance(c, (float, int)) for c in weight):
            raise ValueError("weight lists must be lists of floats or integers")
        if not all(c > 0 for c in weight) or not all(c > 0 for c in height):
            raise ValueError("height and weight lists must be positive")
        if len(weight) != len(height):
            raise ValueError("height and weight lists must have the same length")
        # Calculate the BMI of persons from a list of weights and heights.
        result = (np.array(weight) / (np.array(height) ** 2)).tolist()
        return result

    except ValueError as e:
        raise ValueError(f"the arguments are bad: {e}")


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """Apply a limit to the BMI of persons."""
    try:
        # Check if the arguments are valid.
        if not all(isinstance(c, (float, int)) for c in bmi):
            raise ValueError("bmi lists must be lists of floats or integers")
        if not all(c > 0 for c in bmi):
            raise ValueError("bmi lists must be positive")
        if not isinstance(limit, int) or limit < 0:
            raise ValueError("limit must be an positive integer")
        # Apply a limit to the BMI of persons.
        return (np.array(bmi) < limit).tolist()
    except ValueError as e:
        raise ValueError(f"the arguments are bad: {e}")
