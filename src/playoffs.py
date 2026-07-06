#!/usr/bin/env python3

import pandas

df_list: list = []
season = 2006

rename_mapping = {
    "Utah Hockey Club": "Utah Mammoth",
    "Mighty Ducks of Anaheim": "Anaheim Ducks",
    "Phoenix Coyotes": "Arizona Coyotes",
}
 
while season <= 2026:
    dfs = pandas.read_html(f"./resources/playoffs/{season-1}_{season}.html")

    df = dfs[16]
    # 2020 season is special due to covid-19 restrictions
    if season == 2020:
        df = dfs[25]
    
    # drop last row with league averages
    df = df.iloc[:-1]


    df['Team'] = df['Team'].replace(rename_mapping)
    df_list.append(df)
    season+=1

aggregated_df = pandas.concat(df_list, ignore_index=True)

aggregated_df['Performance'] = aggregated_df['W'] // 4

print(aggregated_df)