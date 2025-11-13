import sys as system
from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd
system.path.insert(0, str(Path(__file__).parent.parent))
from ex00.load_csv import load  # noqa: E402


def show_country_life_expt_graph(
        data: pd.DataFrame,
        country: str) -> None:
    """
    Show the life expectancy of a country by year.
    """
    country_data = data[data['country'] == country]
    if country_data.empty:
        raise AssertionError(f"{country} not found in dataset")

    plt.plot(country_data.columns[1:], country_data.iloc[0, 1:])

    plt.xlabel('Year')
    plt.ylabel('Life expectancy')
    plt.title(f'{country} Life expectancy Projections')
    plt.grid(False)
    plt.xticks(country_data.columns[1::40])
    plt.show()


def main() -> None:
    """
    Main function.
    """
    try:
        data = load("life_expectancy_years.csv")
        if data is None:
            exit(1)

        show_country_life_expt_graph(data, 'France')

    except Exception as e:
        print(f"\033[91mError: {e}\033[0m")
        exit(1)


if __name__ == "__main__":
    main()
