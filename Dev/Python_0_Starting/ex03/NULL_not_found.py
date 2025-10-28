def NULL_not_found(obj) -> int:
    # None
    if obj is None:
        print(f"Nothing: None {type(obj)}")
        return 0
    # NaN
    elif isinstance(obj, float) and obj != obj:
        print(f"Cheese: nan {type(obj)}")
        return 0
    # False
    elif obj is False:
        print(f"Fake: False {type(obj)}")
        return 0
    # 0
    elif (
        (isinstance(obj, int) and obj == 0)
        or (isinstance(obj, float) and obj == 0.0)
        or (isinstance(obj, complex) and obj == 0j)
    ):
        print(f"Zero: 0 {type(obj)}")
        return 0
    # Empty string, list, dict, tuple and set
    elif not obj:
        print(f"Empty: {type(obj)}")
        return 0
    # Type not found
    else:
        print("Type not found")
        return 1
