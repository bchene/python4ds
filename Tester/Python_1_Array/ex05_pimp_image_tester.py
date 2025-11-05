from load_image import ft_load
from pimp_image import \
    ft_original, ft_invert, ft_red, ft_green, ft_blue, ft_grey

array = ft_load("landscape.jpg")

ft_original(array)
print(ft_original.__doc__)

ft_invert(array)
print(ft_invert.__doc__)

ft_red(array)
print(ft_red.__doc__)

ft_green(array)
print(ft_green.__doc__)

ft_blue(array)
print(ft_blue.__doc__)

ft_grey(array)
print(ft_grey.__doc__)
