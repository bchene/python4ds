import matplotlib.pyplot as plt
import numpy as np


def display_image(image: np.array):
    """
    displays an image in grayscale or color.
    """
    if image.ndim == 2 or (image.ndim == 3 and image.shape[2] == 1):
        plt.imshow(image, cmap='gray')
    else:
        plt.imshow(image)
    plt.show()


def check_image(array: np.array) -> None:
    """
    Check if the image is a numpy array.
    """
    assert isinstance(array, np.ndarray), "array must be a numpy array"
    assert array.size > 0, "array cannot be empty"
    assert array.ndim == 3, "array must be in RGB format"
    assert array.shape[2] == 3, "array must be in RGB format"
    return True


def ft_original(array) -> np.array:
    """Original image received"""
    check_image(array)
    display_image(array)


def ft_invert(array) -> np.array:
    """Inverts the color of the image received."""
    check_image(array)
    result = 255 - array[:, :, :]
    display_image(result)
    return result


def ft_red(array) -> np.array:
    """Red channel of the image received."""
    check_image(array)
    # copy and set all channels to 0
    result = array * 0
    # keep only red channel
    result[:, :, 0] = array[:, :, 0]
    display_image(result)
    return result


def ft_green(array) -> np.array:
    """Green channel of the image received."""
    check_image(array)
    # copy and set all channels to 0
    result = array - array
    # keep only green channel
    result[:, :, 1] = array[:, :, 1]
    display_image(result)
    return result


def ft_blue(array) -> np.array:
    """Blue channel of the image received."""
    check_image(array)
    # copy and set all channels to 0
    result = np.zeros_like(array)
    # keep only blue channel
    result[:, :, 2] = array[:, :, 2]
    display_image(result)
    return result


def ft_grey(array) -> np.array:
    """Greyscale of the image received."""
    check_image(array)
    # convert to grayscale: mean of all channels
    result = np.mean(array, axis=2)
    display_image(result)
    return result
