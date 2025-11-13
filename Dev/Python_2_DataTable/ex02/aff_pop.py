import sys as system
from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd
system.path.insert(0, str(Path(__file__).parent.parent))
from ex00.load_csv import load  # noqa: E402


def popstr_to_int(val: str) -> int:
    """
    Convert a population string with 'M' or 'k' to an integer.
    """
    coef = 1
    if pd.isna(val):
        return 0    # nan is 0
    try:
        numeric_val = float(val)
        return int(numeric_val)
    except (ValueError, TypeError):
        pass
    if not isinstance(val, str):
        return 0
    if len(val) > 1 and val[-1] == 'M':
        coef = 1e6
        val = val[:-1]
    if len(val) > 1 and val[-1] == 'k':
        coef = 1e3
        val = val[:-1]
    try:
        return int(float(val) * coef)
    except ValueError:
        return 0


def add_country_to_pop_graph(
        data: pd.DataFrame,
        country: str,
        color: str = 'blue'
        ) -> None:
    """
    Add a country to the population graph.
    """
    country_data = data[data['country'] == country]
    if country_data.empty or country_data is None:
        raise AssertionError(f"{country} not found in dataset")

    years = country_data.columns[1:-50]
    values_str = country_data.iloc[0, 1:-50]
    values_int = [popstr_to_int(val) for val in values_str]
    if (color):
        plt.plot(years, values_int, label=country, color=color)
    else:
        plt.plot(years, values_int, label=country)


def show_countries_pop_graph(
        data: pd.DataFrame,
        countries: list[str],
        colors: list[str]
        ) -> None:
    """
    Show the population of a list of countries by year.
    """
    for country, color in zip(countries, colors):
        add_country_to_pop_graph(data, country, color)
    plt.xlabel('Year')
    plt.ylabel('Population')
    plt.title('Population Projections')
    plt.grid(False)
    plt.xticks(data.columns[1:-50:40])
    plt.yticks([0, 20e6, 40e6, 60e6], ["", "20M", "40M", "60M"])
    plt.legend(countries, loc='lower right')
    plt.show()


def main() -> None:
    """
    Main function.
    """
    try:
        data = load("population_total.csv")
        if data is None:
            exit(1)
        show_countries_pop_graph(
            data, ['Belgium', 'France'], ['blue', 'green']
        )
    except AssertionError as e:
        print(f"\033[91mAssertionError: {e}\033[0m")
        exit(1)
    except Exception as e:
        print(f"\033[91mError: {e}\033[0m")
        exit(1)


if __name__ == "__main__":
    main()
