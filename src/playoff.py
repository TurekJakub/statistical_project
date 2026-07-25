#!/usr/bin/env python3

import pandas

from utilities import perform_all_tests
from teams_division import rename_mapping


def prepare_playoff_dataset():
    df_list: list = []
    season = 2006

    while season <= 2026:
        dfs = pandas.read_html(f"./resources/playoffs/{season - 1}_{season}.html")

        df = dfs[16]
        # 2020 season is special due to covid-19 restrictions
        if season == 2020:
            df = dfs[25]

        # drop last row with league averages
        df = df.iloc[:-1]

        df["Team"] = df["Team"].replace(rename_mapping)
        df_list.append(df)
        season += 1

    dataset = pandas.concat(df_list, ignore_index=True)

    dataset["Performance"] = dataset["W"] // 4

    return dataset

def perform_playoff_tests():
    dataset = prepare_playoff_dataset()

    perform_all_tests(dataset, False)

if __name__ == "__main__":
    perform_playoff_tests()