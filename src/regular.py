#!/usr/bin/env python3

import pandas

from src.teams_division import rename_mapping
from src.utilities import perform_all_tests


def prepare_single_regular_season(start_year: int):
    df = pandas.read_html(f"./resources/regular/{start_year}_{start_year + 1}.xls")[0]

    # drop last row whit season averages that we are not interested in
    df = df.iloc[:-1]

    striped_name = (
        df.iloc[:, 1].astype(str).str.replace("*", "", regex=False).str.strip()
    )

    df["Team"] = striped_name.replace(rename_mapping)

    return df


def prepare_regular_season_dataset():
    df_list: list = []
    start_year = 2005

    while start_year < 2026:
        df_list.append(prepare_single_regular_season(start_year))
        start_year += 1

    dataset = pandas.concat(df_list, ignore_index=True)

    dataset["Performance"] = dataset.iloc[:, 7] / (dataset.iloc[:, 3] / 50)

    return dataset


def perform_regular_season_tests():
    dataset = prepare_regular_season_dataset()

    perform_all_tests(dataset, True)


if __name__ == "__main__":
    perform_regular_season_tests()
