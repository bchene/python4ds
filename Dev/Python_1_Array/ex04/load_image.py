import os as my_os
import numpy as np
import matplotlib.pyplot as plt


def ft_load(path: str) -> np.array:
    """
    loads an image, prints its format, and its pixels, content in RGB format.

    Args:
        path: path to the image

    Returns:
        array: array of the image

    Raises:
        AssertionError: If the file doesn't exist.
        AssertionError: If the file cannot be loaded.
        AssertionError: If the image is not a numpy array.
        AssertionError: If the image is empty.
        AssertionError: If the image is not in RGB format.
    """
    assert (
        isinstance(path, str)
        and my_os.path.exists(path)
        and my_os.path.isfile(path)
    ), f"file '{path}' doesn't exist"

    try:
        im_array = plt.imread(path)
    except Exception as e:
        raise AssertionError(f"plt.imread cannot load {path}: {e}") from e

    # check if the image is a none empty numpy array
    assert isinstance(im_array, np.ndarray), "image must be a numpy array"
    assert im_array.size > 0, "image cannot be empty"

    # check RGB format (3 dimensions (height, width, channels) and 3 color)
    assert im_array.ndim == 3, "image must be in RGB format (3 dimensions)"
    assert im_array.shape[2] == 3, \
        "image must be in RGB format (3 color channels)"

    print(f"The shape of image is: {im_array.shape}")
    print(im_array)
    return im_array
