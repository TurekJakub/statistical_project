all_teams = {
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
    "Utah Mammoth",
    "Ottawa Senators",
    "Calgary Flames",
    "Edmonton Oilers",
    "Montreal Canadiens",
    "Vancouver Canucks",
    "Toronto Maple Leafs",
    "Winnipeg Jets",
}

canadian_teams = {
    "Ottawa Senators",
    "Calgary Flames",
    "Edmonton Oilers",
    "Montreal Canadiens",
    "Vancouver Canucks",
    "Toronto Maple Leafs",
    "Winnipeg Jets",
}

traditional_teams = {
    "Boston Bruins",
    "Chicago Blackhawks",
    "Detroit Red Wings",
    "Montreal Canadiens",
    "New York Rangers",
    "Toronto Maple Leafs",
    "Los Angeles Kings",
    "Philadelphia Flyers",
    "Pittsburgh Penguins",
    "St. Louis Blues",
}

low_taxation_teams = {
    "Carolina Hurricanes",
    "Dallas Stars",
    "Florida Panthers",
    "Vegas Golden Knights",
    "Nashville Predators",
    "Seattle Kraken",
    "Tampa Bay Lightning",
    "Colorado Avalanche",
    "Utah Mammoth",
    "Arizona Coyotes"
}

medium_taxation_teams = {
    "Boston Bruins",
    "Chicago Blackhawks",
    "Columbus Blue Jackets",
    "Detroit Red Wings",
    "Philadelphia Flyers",
    "Pittsburgh Penguins",
    "St. Louis Blues",
    "Washington Capitals",
    "New Jersey Devils",
    "New York Islanders",
    "Minnesota Wild",
    "Buffalo Sabres",
    "Atlanta Thrashers"
}

high_taxation_teams = {
    "Anaheim Ducks",
    "Calgary Flames",
    "Edmonton Oilers",
    "Los Angeles Kings",
    "Montreal Canadiens",
    "New York Rangers",
    "Ottawa Senators",
    "San Jose Sharks",
    "Toronto Maple Leafs",
    "Vancouver Canucks",
    "Winnipeg Jets",
}

# maps historical names of teams to their contemporary counterparts
rename_mapping = {
    "Utah Hockey Club": "Utah Mammoth",
    "Mighty Ducks of Anaheim": "Anaheim Ducks",
    "Phoenix Coyotes": "Arizona Coyotes",
}

def assign_origin(team_name):
    if not sanity_check_helper(team_name, "origin"):
        return "Unknown"

    if team_name in canadian_teams:
        return "Canada"

    return "USA"

def assign_tradition(team_name):
    if not sanity_check_helper(team_name, "tradition"):
        return "Unknown"
     
    if team_name in traditional_teams:
        return "Traditional"

    return "Expansion"

def assign_taxation_level(team_name):
    if not sanity_check_helper(team_name, "taxation level"):
        return "Unknown"

    if team_name in low_taxation_teams:
        return "Low"
    if team_name in medium_taxation_teams:
        return "Medium"
    if team_name in high_taxation_teams:
        return "High"

def sanity_check_helper(team_name: str, additional_err_message: str) -> bool:
    if team_name not in all_teams:
        print(
            f"warning: cannot assign {additional_err_message} to team: {team_name} - name does not match any team playing the league between 2005 and 2026"
        )
        return False
    
    return True

def assign_group_labels(data):
    data["Origin"] = data["Team"].apply(assign_origin)
    data["Tradition"] = data["Team"].apply(assign_tradition)
    data["Taxation"] = data["Team"].apply(assign_taxation_level)

def group_data_by(data, group_by_col: str, group_values: list[str], col_to_select: str = None) -> tuple :
    groups: list = []
    for val in group_values:
        data_group = data[data[group_by_col] == val]
        if col_to_select is None:
            groups.append(data_group)
        else:
            groups.append(data_group[col_to_select])

    return tuple(groups)