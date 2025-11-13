import pandas as pd
import os as sys_os


def check_file_access_R_OK(filename: str) -> None:
    """
    Check if the file exists and is a file and is readable.
    """
    assert sys_os.path.exists(filename), \
        f"file '{filename}' doesn't exist"
    assert sys_os.path.isfile(filename), \
        f"file '{filename}' is not a file"
    assert sys_os.access(filename, sys_os.R_OK), \
        f"file '{filename}' is not readable"


def check_extension(filename: str, extension: str) -> None:
    """
    Check if the file has the given extension.
    """
    assert filename.endswith(extension), \
        f"file '{filename}' is not a {extension} file"


def read_csv_file(filename: str) -> pd.DataFrame:
    """
    Read the csv file into a pandas dataframe.
    """
    try:
        data = pd.read_csv(filename)
        if data is None:
            raise AssertionError(f"'{filename}' is not a readable csv file")
        return data
    except Exception:
        raise AssertionError(f"'{filename}' is not a readable csv file:")


def load(filename: str) -> pd.DataFrame | None:
    """
    Load the csv file into a pandas dataframe.
    """
    try:
        check_file_access_R_OK(filename)
        check_extension(filename, '.csv')
        data = read_csv_file(filename)
        print("Loading dataset of dimensions", data.shape)
        return data

    except AssertionError as e:
        print(f"\033[91mAssertionError: {e}\033[0m")
        return None
    except Exception as e:
        print(f"\033[91mError: {e}\033[0m")
        return None
