#!/usr/bin/env python3

import pandas

from utilities import perform_all_tests
from teams_division import rename_mapping
from regular import prepare_single_regular_season


def prepare_playoff_dataset():
    df_list: list = []
    season = 2006

    while season <= 2026:
        dfs = pandas.read_html(f"./resources/playoffs/{season - 1}_{season}.html")

        playoff_df = dfs[16]
        # 2020 season is special due to covid-19 restrictions
        if season == 2020:
            playoff_df = dfs[25]

        # drop last row with league averages
        playoff_df = playoff_df.iloc[:-1]

        playoff_df["Team"] = playoff_df["Team"].replace(rename_mapping)

        # load corresponding regular season to take all teams into the account
        regular_df = prepare_single_regular_season(season - 1)
        season_teams = regular_df[["Team"]].copy()

        team_series = regular_df["Team"]
       
        season_teams = pandas.DataFrame({"Team": team_series.values})

        all_teams_df = pandas.merge(
            season_teams, playoff_df[["Team", "W"]], on="Team", how="left"
        )

        df_list.append(all_teams_df)
        season += 1

    dataset = pandas.concat(df_list, ignore_index=True)

    # ensure that all teams that got eliminated before playoffs has zero points
    dataset["W"] = dataset["W"].fillna(-1)
    dataset["Performance"] = (dataset["W"] // 4) + 1

    return dataset

def perform_playoff_tests():
    dataset = prepare_playoff_dataset()

    perform_all_tests(dataset, False)

if __name__ == "__main__":
    perform_playoff_tests()
