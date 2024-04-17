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



def pick_random_champ(role, min_win_rate, max_win_rate, min_play_rate, max_play_rate):
    # Load champion data from JSON file
    json_filename = f"data/{role}_data.json"
    with open(os.path.join(SCRIPT_DIR, json_filename), "r", encoding="utf-8") as json_file:
        champion_data_list = json.load(json_file)

    # Check if champion data is available
    if champion_data_list:
        # Define the maximum pick rate based on wacky_value

        eligible_champions = [champion for champion in champion_data_list
                               if float(champion["pick_rate"]) <= float(max_play_rate) and
                               float(champion["pick_rate"]) >= float(min_play_rate) and
                               float(champion["winrate"]) <= float(max_win_rate) and
                               float(champion["winrate"]) >= float(min_win_rate)]


        random_champion = random.choice(eligible_champions)

        random_champion['role'] = role
        return random_champion
    else:
        print("No champion data available for the specified role.")
        return None
