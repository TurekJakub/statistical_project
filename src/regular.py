#!/usr/bin/env python3

import pandas
from scipy import stats

# maps historical names of teams to their contemporary counterparts 
rename_mapping = {
    "Utah Hockey Club": "Utah Mammoth",
    "Mighty Ducks of Anaheim": "Anaheim Ducks",
    "Phoenix Coyotes": "Arizona Coyotes",
}

df_list: list = []
start_year = 2005

while start_year < 2026:
    df = pandas.read_html(f"./resources/{start_year}_{start_year + 1}.xls")[0]

    # drop last row whit season averages that we are not interested in 
    df = df.iloc[:-1]

    striped_name =  df.iloc[:, 1].astype(str).str.replace("*", "", regex=False).str.strip()

    df.iloc[:, 1] = striped_name.replace(rename_mapping)

    df_list.append(df)
    start_year += 1

aggregated_df = pandas.concat(df_list, ignore_index=True)

canadian_teams = [
    "Ottawa Senators",
    "Calgary Flames",
    "Edmonton Oilers",
    "Montreal Canadiens",
    "Vancouver Canucks",
    "Toronto Maple Leafs",
    "Winnipeg Jets"
]

american_teams = [
    "Detroit Red Wings",
    "Carolina Hurricanes",
    "Dallas Stars",
    "Buffalo Sabres",
    "Nashville Predators",
    "Philadelphia Flyers",
    "New Jersey Devils",
    "New York Rangers",
    "San Jose Sharks",
    "Anaheim Ducks",
    "Colorado Avalanche",
    "Tampa Bay Lightning",
    "Atlanta Thrashers",
    "Los Angeles Kings",
    "Florida Panthers",
    "Minnesota Wild",
    "Arizona Coyotes",
    "New York Islanders",
    "Boston Bruins",
    "Columbus Blue Jackets",
    "Washington Capitals",
    "Chicago Blackhawks",
    "Pittsburgh Penguins",
    "St. Louis Blues",
    "Vegas Golden Knights",
    "Seattle Kraken",
    "Utah Mammoth"
]

aggregated_df['Performance'] = aggregated_df.iloc[:, 7] / (aggregated_df.iloc[:, 3] / 50)

def assign_origin(team_name):
    if team_name in canadian_teams:
        return 'Canada'
    elif team_name in american_teams:
        return 'USA'
    
    print("warning: team with unknown nation of origin - input data are probably corrupted")
    return 'Unknown'

aggregated_df['Origin'] = aggregated_df.iloc[:, 1].apply(assign_origin)

us_performance = aggregated_df[aggregated_df['Origin'] == 'US']['Performance']
ca_performance = aggregated_df[aggregated_df['Origin'] == 'CA']['Performance']


t_statistic, p_value = stats.ttest_ind(us_performance, ca_performance, equal_var=False)

print("=== US vs CA Results ===")
print(f"T-Statistic: {t_statistic:.4f}")
print(f"P-Value: {p_value:.4f}")
print("======================")
