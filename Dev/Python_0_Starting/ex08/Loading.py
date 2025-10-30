import os as my_os


def ft_tqdm(lst: range) -> None:
    """Display a progress bar while iterating through the range."""
    total = len(lst)
    try:
        bar_length = (
            my_os.get_terminal_size().columns
            - (34 + 2 * len(str(abs(total))))
        )
    except OSError:
        bar_length = 30

    for i, item in enumerate(lst):
        percentage = int((i + 1) / total * 100)
        filled = int(bar_length * (i + 1) / total)
        # █████████████████
        bar = "█" * filled + " " * (bar_length - filled)
        # 50%|█████████████████                | 166/333
        print(f"\r{percentage}%|{bar}| {i + 1}/{total}", end="", flush=True)
        yield item
    print()
