def ft_sqrt(n):
    """Calculate the square root of n using the exponentiation operator."""
    if n < 0:
        raise ValueError("Cannot calculate square root of a negative number")
    return n ** 0.5


def ft_mean(args) -> float:
    """Calculate the mean of a list of numbers."""
    return float(sum(args) / len(args))


def ft_median(args) -> float:
    """Calculate the median of a list of numbers."""
    sa = sorted(args)
    len_sa = len(sa)
    if len_sa % 2 == 0:
        return float(sa[len_sa // 2 - 1] + sa[len_sa // 2]) / 2
    else:
        return float(sa[len_sa // 2])


def ft_quartile(args) -> list[float]:
    """Calculate the quartile of a list of numbers."""
    sa = sorted(args)
    len_sa = len(sa)
    return [float(sa[len_sa // 4]), float(sa[len_sa * 3 // 4])]


def ft_var(args) -> float:
    """Calculate the variance of a list of numbers."""
    mean = ft_mean(args)
    var = 0.0
    for x in args:
        var += (x - mean) ** 2
    var = var / len(args)
    return var


def ft_std(args) -> float:
    """Calculate the standard deviation of a list of numbers."""
    return ft_sqrt(ft_var(args))


def ft_statistics(*args, **kwargs):
    """Calculate the statistics of a list of numbers."""

    STATISTICS_DICT = {
        "mean": ft_mean,
        "median": ft_median,
        "quartile": ft_quartile,
        "std": ft_std,
        "var": ft_var
    }

    for _, value in kwargs.items():
        if value in STATISTICS_DICT.keys():
            try:
                assert args, \
                    ("No arguments provided")
                assert all(isinstance(x, (int, float)) for x in args), \
                    ("The list contains non-numeric values")
                assert len(args) > 0, \
                    ("The list is empty")
                result = STATISTICS_DICT[value](args)
                print(f"{value} : {result}")

            except Exception as e:
                print(f"\033[31mError: {e}\033[0m")


ft_statistics(1, 42, 360, 11, 64, toto="mean", tutu="median", tata="quartile")
print("-----")
ft_statistics(5, 75, 450, 18, 597, 27474, 48575, hello="std", world="var")
print("-----")
ft_statistics(
    5, 75, 450, 18, 597, 27474, 48575, ejfhhe="heheh", ejdjdejn="kdekem")
print("-----")
ft_statistics(toto="mean", tutu="median", tata="quartile")

# EXPECTED OUTPUT
#
# mean : 95.6
# median : 42
# quartile : [11.0, 64.0]
# -----
# std : 17982.70124086944
# var : 323377543.9183673
# -----
# -----
# ERROR
# ERROR
# ERROR
