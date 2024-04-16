import random
import json

PLAYERS = ["enzo", "steven", "eric", "rudy", "zack",
           "matt", "gibby", "sohail", "koby", "jason"]

ROLES = ["top", "jg", "mid", "bot", "sup"]

def form_random_teams(players=PLAYERS):
    team1 = []
    team2 = []
    random.shuffle(players)
    random.shuffle(players)
    random.shuffle(players)
    for count, item in enumerate(players):
        if count%2 == 0:
            team1.append(item)
        else:
            team2.append(item)

    return team1, team2


def assign_champions(team1, team2):
    team1_with_champs = {}
    team2_with_champs = {}
    for count, player in enumerate(team1):
        team1_with_champs[player] = pick_random_champ(ROLES[count])
    for count, player in enumerate(team2):
        team2_with_champs[player] = pick_random_champ(ROLES[count])
    return team1_with_champs, team2_with_champs


def pick_random_champ(role):
    # Load champion data from JSON file
    json_filename = f"data/{role}_data.json"
    with open(json_filename, "r", encoding="utf-8") as json_file:
        champion_data_list = json.load(json_file)

    # Check if champion data is available
    if champion_data_list:
        # Pick a random champion from the data
        random_champion = random.choice(champion_data_list)
        random_champion['role'] = role
        return random_champion
    else:
        print("No champion data available for the specified role.")
        return None
