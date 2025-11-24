def ft_sqrt(n: float) -> float:
    """Calculate the square root of n using ** 0.5."""
    if n < 0:
        raise ValueError("Cannot calculate square root of a negative number")
    return n ** 0.5


def ft_mean(args: list[float]) -> float:
    """Calculate the mean of a list of numbers."""
    return sum(args) / len(args)


def ft_median(args: list[float]) -> float:
    """Calculate the median of a list of numbers."""
    sa = sorted(args)
    len_sa = len(sa)
    if len_sa % 2 == 0:
        return (sa[len_sa // 2 - 1] + sa[len_sa // 2]) / 2
    else:
        return sa[len_sa // 2]


def ft_quartile(args: list[float]) -> list[float]:
    """Calculate the quartile of a list of numbers."""
    sa = sorted(args)
    len_sa = len(sa)
    return [float(sa[len_sa // 4]), float(sa[len_sa * 3 // 4])]


def ft_var(args: list[float]) -> float:
    """Calculate the variance of a list of numbers."""
    mean = ft_mean(args)
    var = 0.0
    for x in args:
        var += (x - mean) ** 2
    var /= len(args)
    return var


def ft_std(args) -> float:
    """Calculate the standard deviation of a list of numbers."""
    return ft_sqrt(ft_var(args))


def ft_statistics(*args, **kwargs):
    """Calculate the statistics of a list of numbers."""
    STATISTICS_FUNCTIONS = {
        "mean": ft_mean,
        "median": ft_median,
        "quartile": ft_quartile,
        "std": ft_std,
        "var": ft_var
    }
    for _, fn in kwargs.items():
        if fn in STATISTICS_FUNCTIONS.keys():
            try:
                assert len(args) > 0, \
                    ("The list is empty")
                assert all(isinstance(x, (int, float)) for x in args), \
                    ("The list contains non-numeric values")
                result = STATISTICS_FUNCTIONS[fn](args)
                print(f"{fn} : {result}")
            except Exception as e:
                print(f"\033[31mError in function {fn}: {e}\033[0m")
