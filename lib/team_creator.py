import random
import json
from lib.util import *

PLAYERS = ["enzo", "steven", "eric", "rudy", "zack",
           "matt", "gibby", "sohail", "koby", "jason"]
RANKS = [5,2,1,3,5,6,7,12,1.2]

ROLES = ["top", "jg", "mid", "bot", "sup"]

TEAM_1 = []
TEAM_2 = []

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

def form_random_teams(players, ranks):
    # Pair each player with their rank
    paired = list(zip(players, ranks))
    
    # Shuffle to introduce randomness
    random.shuffle(paired)

    # Sort by rank (descending) to distribute higher ranked players evenly
    paired.sort(key=lambda x: x[1], reverse=True)

    team1, team2 = [], []
    team1_rank, team2_rank = 0, 0

    for player, rank in paired:
        # Stop adding if both teams are full
        if len(team1) >= 5 and len(team2) >= 5:
            break

        # Prefer the team with fewer total rank, with randomness
        if (team1_rank < team2_rank and len(team1) < 5) or len(team2) >= 5:
            if random.random() < 0.7:
                team1.append(player)
                team1_rank += rank
            elif len(team2) < 5:
                team2.append(player)
                team2_rank += rank
        else:
            if random.random() < 0.7:
                team2.append(player)
                team2_rank += rank
            elif len(team1) < 5:
                team1.append(player)
                team1_rank += rank

    print(f"Team 1 (Total Rank: {team1_rank}): {team1}")
    print(f"Team 2 (Total Rank: {team2_rank}): {team2}")

    return team1, team2


def form_arena_teams(players=PLAYERS):
    random.shuffle(players)
    random.shuffle(players)
    random.shuffle(players)

    return players

def assign_champions(team1, team2):
    team1_with_champs = {}
    team2_with_champs = {}
    for count, player in enumerate(team1):
        team1_with_champs[player] = pick_random_champ(ROLES[count])
    for count, player in enumerate(team2):
        team2_with_champs[player] = pick_random_champ(ROLES[count])
    return team1_with_champs, team2_with_champs



def pick_random_champ(role, min_win_rate, max_win_rate, min_play_rate, max_play_rate, blind_pick, team, current_champ):
    # Load champion data from JSON file
    json_filename = f"data/{role}_data.json"
    with open(os.path.join(SCRIPT_DIR, json_filename), "r", encoding="utf-8") as json_file:
        champion_data_list = json.load(json_file)

    if current_champ != "-":
        if team == 1:
            TEAM_1.remove(current_champ)
        else:
            TEAM_2.remove(current_champ)

    # Check if champion data is available
    if champion_data_list:
        # Define the maximum pick rate based on wacky_value
        if role == "arena":
            eligible_champions = [champion for champion in champion_data_list
                                if float(champion["winrate"]) <= float(max_win_rate) and
                                float(champion["winrate"]) >= float(min_win_rate)]
        else:
            eligible_champions = [champion for champion in champion_data_list
                                if float(champion["pick_rate"]) <= float(max_play_rate) and
                                float(champion["pick_rate"]) >= float(min_play_rate) and
                                float(champion["winrate"]) <= float(max_win_rate) and
                                float(champion["winrate"]) >= float(min_win_rate)]
            
        eligible_champions = [champ for champ in eligible_champions if champ['name'] != current_champ]

        if blind_pick.get():
            print("Blind Pick enabled")
            if team == 1:
                eligible_champions = [champ for champ in eligible_champions if champ['name'] not in TEAM_1]
            else:
                eligible_champions = [champ for champ in eligible_champions if champ['name'] not in TEAM_2]
        else:
            eligible_champions = [champ for champ in eligible_champions if champ['name'] not in TEAM_1]
            eligible_champions = [champ for champ in eligible_champions if champ['name'] not in TEAM_2]

        random_champion = random.choice(eligible_champions)

        random_champion['role'] = role
        if team == 1:
            TEAM_1.append(random_champion['name'])
        else:
            TEAM_2.append(random_champion['name'])
        print(TEAM_1)
        print(TEAM_2)
        return random_champion
    else:
        print("No champion data available for the specified role.")
        return None
