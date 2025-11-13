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
        raise ValueError(f"Invalid population string: {val}")


def show_life_expect_income_graph(
        life_expect_ds: pd.DataFrame,
        income_ds: pd.DataFrame,
        year_str: str,) -> None:
    """
    Show the life expectancy / income graph.
    """
    if (year_str not in life_expect_ds.columns or
            year_str not in income_ds.columns):
        raise AssertionError(f"Year {year_str} not found in both datasets")

    life_float = 0.0
    income_int = 0
    life_list = []
    income_list = []
    life_expect_indexed = life_expect_ds.set_index('country')
    income_indexed = income_ds.set_index('country')
    common_countries = (set(life_expect_ds['country']) &
                        set(income_ds['country']))

    for country in common_countries:
        try:
            life = life_expect_indexed.loc[country, year_str]
            income = income_indexed.loc[country, year_str]
        except KeyError:
            continue
        if pd.isna(life) or pd.isna(income):
            continue
        try:
            life_float = float(life)
            income_int = popstr_to_int(income)
        except ValueError:
            continue
        life_list.append(life_float)
        income_list.append(income_int)

    plt.scatter(income_list, life_list)
    plt.xlabel('Gross Domestic Product')
    plt.ylabel('Life Expectancy')
    plt.title(str(year_str))
    plt.xscale('log')
    plt.xticks([300, 1e3, 1e4], ['300', '1k', '10k'])
    plt.show()


def main() -> None:
    """
    Main function.
    """
    try:
        life_expect_ds = load("life_expectancy_years.csv")
        if life_expect_ds is None:
            exit(1)
        income_ds = load(
            "income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
        if income_ds is None:
            exit(1)

        show_life_expect_income_graph(life_expect_ds, income_ds, '1900')

    except Exception as e:
        print(f"\033[91mError: {e}\033[0m")
        exit(1)


if __name__ == "__main__":
    main()
