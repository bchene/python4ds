def all_thing_is_obj(obj) -> int:
    # List
    if isinstance(obj, list):
        print(f"List : {type(obj)}")
    # Tuple
    elif isinstance(obj, tuple):
        print(f"Tuple : {type(obj)}")
    # Set
    elif isinstance(obj, set):
        print(f"Set : {type(obj)}")
    # Dict
    elif isinstance(obj, dict):
        print(f"Dict : {type(obj)}")
    # String
    elif isinstance(obj, str):
        print(f"{obj} is in the kitchen : {type(obj)}")
    # Type not found
    else:
        print("Type not found")
    return 42
