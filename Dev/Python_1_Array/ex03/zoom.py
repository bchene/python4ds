import load_image as li
import matplotlib.pyplot as plt
import numpy as np


def crop_image(
    image: np.array,
    x: int,
    y: int,
    size_x: int,
    size_y: int,
    zoom_factor: int
) -> np.array:
    """
    Crops and zooms an image.

    Args:
        image: the image to crop
        x: the offset x
        y: the offset y
        size_x: the size x
        size_y: the size y
        zoom_factor: the zoom factor
    Returns:
        the cropped image
    Raises:
        AssertionError: If the image is not a numpy array.
        AssertionError: If the image is not at least 2D array.
        AssertionError: If x and y are not non-negative.
        AssertionError: If size_x and size_y are not positive.
        AssertionError: If x + size_x or y + size_y are outside image bounds.
        AssertionError: If zoom_factor is not >= 1.
    """

    assert isinstance(image, np.ndarray), "image must be a numpy array"
    assert image.ndim >= 2, "image must be at least 2D array"
    height = image.shape[0]
    width = image.shape[1]
    assert x >= 0 and y >= 0, "x and y must be non-negative"
    assert size_x > 0 and size_y > 0, "size_x and size_y must be positive"
    assert x + size_x <= width and y + size_y <= height, \
        "x + size_x and y + size_y must be within image bounds"
    assert zoom_factor >= 1, "zoom_factor must be >= 1"

    # crop the image
    cropped = image[y: y + size_y: zoom_factor, x: x + size_x: zoom_factor]
    return cropped


def display_image(image: np.array):
    """
    displays an image in grayscale or color.
    """
    if image.ndim == 2 or (image.ndim == 3 and image.shape[2] == 1):
        plt.imshow(image, cmap='gray')
    else:
        plt.imshow(image)
    plt.show()


def main():
    try:
        # load_image
        image = li.ft_load("animal.jpeg")
        # crop_image
        image = crop_image(image, 450, 100, 400, 400, 1)
        # RGB > grayscale (red only channel (0) ))
        image = image[:, :, 0]
        # print the shape and the image
        print(f"New shape after slicing: {image.shape}")
        print(image)
        # display the image in grayscale or color
        display_image(image)

    except AssertionError as e:
        print(f"AssertionError: {e}")
        exit(1)
    except Exception as e:
        print(f"Exception: {e}")
        exit(1)


if __name__ == "__main__":
    main()
