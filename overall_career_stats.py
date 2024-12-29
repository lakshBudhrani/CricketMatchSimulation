# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 18:53:55 2024

@author: laksh
"""

import json
from data_extraction import values

players_dict_batter = {}
players_dict_bowler = {}
teams = ["India", "Australia"]

for file in values:
    with open('tests_json\\' + file + '.json', 'r') as file:
        file_json = json.load(file)

        for team in teams:
            if team in file_json['info']['players']:
                players = file_json['info']['players'][team]

                for player in players:
                    if player not in players_dict_batter:
                        players_dict_batter[player] = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 'out': 0}

                for inning in file_json['innings']:
                    if inning['team'] == team:
                        for over in inning['overs']:
                            for delivery in over['deliveries']:
                                run = delivery['runs']['batter']
                                extra = delivery['runs']['extras']
                                
                                bowler = delivery['bowler']
                                if bowler not in players_dict_bowler:
                                    players_dict_bowler[bowler] = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0, 'out': 0}

                                players_dict_batter[delivery['batter']][run] += 1
                                players_dict_bowler[delivery['bowler']][run] += extra + 1

                                if 'wickets' in delivery:
                                    for wicket in delivery['wickets']:
                                        player_out = wicket['player_out']
                                        players_dict_batter[player_out]['out'] += 1
                                    for wicket in delivery['wickets']:
                                        if wicket['kind'] != 'run out':
                                            players_dict_bowler[bowler]['out'] += 1
