# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 15:31:44 2024

@author: laksh
"""

import json
from data_extraction import values

stadiums = [
    "Perth Stadium",
    "Melbourne Cricket Ground",
    "Adelaide Oval",
    "Brisbane Cricket Ground",
    "Sydney Cricket Ground"
]

stadium_stats = {stadium: {"batters": {}, "bowlers": {}} for stadium in stadiums}
teams = ["India", "Australia"]

for file in values:
    with open('tests_json\\' + file + '.json', 'r') as file:
        file_json = json.load(file)

        venue = file_json['info']['venue']
        if venue not in stadiums:
            continue

        for team in teams:
            if team in file_json['info']['players']:
                players = file_json['info']['players'][team]

                # Initialize all players for batters and bowlers
                for player in players:
                    if player not in stadium_stats[venue]["batters"]:
                        stadium_stats[venue]["batters"][player] = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 'out': 0}
                    if player not in stadium_stats[venue]["bowlers"]:
                        stadium_stats[venue]["bowlers"][player] = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0, 'out': 0}

            for inning in file_json['innings']:
                if inning['team'] == team:
                    for over in inning['overs']:
                        for delivery in over['deliveries']:
                            run = delivery['runs']['batter']
                            extra = delivery['runs']['extras']

                            batsman = delivery['batter']
                            bowler = delivery['bowler']

                            # Ensure batsman is initialized
                            if batsman not in stadium_stats[venue]["batters"]:
                                stadium_stats[venue]["batters"][batsman] = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 'out': 0}

                            # Ensure bowler is initialized
                            if bowler not in stadium_stats[venue]["bowlers"]:
                                stadium_stats[venue]["bowlers"][bowler] = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0, 'out': 0}

                            stadium_stats[venue]["batters"][batsman][run] += 1
                            stadium_stats[venue]["bowlers"][bowler][run] += extra + 1

                            if 'wickets' in delivery:
                                for wicket in delivery['wickets']:
                                    player_out = wicket['player_out']
                                    stadium_stats[venue]["batters"][player_out]['out'] += 1
                                    if wicket['kind'] != 'run out':
                                        stadium_stats[venue]["bowlers"][bowler]['out'] += 1

#print(stadium_stats)

