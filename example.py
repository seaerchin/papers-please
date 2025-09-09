# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "pandas",
# ]
# ///


import pandas as pd


def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    unique = employee.unique()
