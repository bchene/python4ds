def count_in_list(lst: list, item_to_count: any) -> int:
    """Count the occurrences of an item in a list.

    Args:
        lst (list): The list to search in.
        item_to_count (any): The item to count.

    Returns:
        int: The number of times the item appears.

    Raises:
        TypeError: If the object is not a list or is not iterable.
        Exception: If an unexpected error occurs.

    """
    try:
        return sum(1 for item in lst if item == item_to_count)

    except TypeError as e:
        raise TypeError(f"the object provided is not a list or is not iterable. {e}")
    except Exception as e:
        raise Exception(f"an unexpected error occurred: {e}")
