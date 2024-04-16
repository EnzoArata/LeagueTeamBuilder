import random
import json
from lib.util import *

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



def pick_random_champ(role, wacky_value=0):
    # Load champion data from JSON file
    json_filename = f"data/{role}_data.json"
    with open(os.path.join(SCRIPT_DIR, json_filename), "r", encoding="utf-8") as json_file:
        champion_data_list = json.load(json_file)

    # Check if champion data is available
    if champion_data_list:
        # Define the maximum pick rate based on wacky_value
        if wacky_value != 0:
            max_pick_rate = max(10 - wacky_value / 10, 0.85)
            print(f"max pick rate: {max_pick_rate}")
            eligible_champions = [champion for champion in champion_data_list if float(champion["pick_rate"]) <= max_pick_rate]

        # Adjust the selection probability based on wacky_value
        if wacky_value > 0:
            for champion in eligible_champions:
                champion["pick_rate_weighted"] = (100 - wacky_value) / float(champion["pick_rate"])
            total_weight = sum(champion["pick_rate_weighted"] for champion in eligible_champions)
            probabilities = [champion["pick_rate_weighted"] / total_weight for champion in eligible_champions]
            random_champion = random.choices(eligible_champions, weights=probabilities)[0]
        else:
            random_champion = random.choice(champion_data_list)

        random_champion['role'] = role
        return random_champion
    else:
        print("No champion data available for the specified role.")
        return None
