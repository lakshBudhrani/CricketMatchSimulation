# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 21:10:04 2024

@author: laksh
"""

from pprint import pprint
from info_extraction import stadium_stats, stadiums

# Team members for India and Australia
ind_players = [
    "RG Sharma",
    "YBK Jaiswal",
    "V Kohli",
    "Shubman Gill",
    "KL Rahul",
    "RR Pant",
    "RA Jadeja",
    "Washington Sundar",
    "R Ashwin",
    "Mohammed Siraj",
    "JJ Bumrah"
]

aus_players = [
    "UT Khawaja",
    "M Labuschagne",
    "SPD Smith",
    "TM Head",
    "MR Marsh",
    "AT Carey",
    "PJ Cummins",
    "MA Starc",
    "SM Boland",
    "NM Lyon",
    "JR Hazlewood"
]

# Initialize dictionaries to hold the probability distributions for each player at each stadium
ind_players_prob_dist = {stadium: {} for stadium in stadiums}
aus_players_prob_dist = {stadium: {} for stadium in stadiums}

# Initialize dictionaries to hold the number of balls faced by each player at each stadium
ind_players_balls_faced = {stadium: {} for stadium in stadiums}
aus_players_balls_faced = {stadium: {} for stadium in stadiums}

def initialize_prob_dist_and_balls(players, players_prob_dist, players_balls_faced):
    """Initialize the probability distribution and balls faced dictionaries for the players."""
    for stadium in stadiums:
        for player in players:
            players_prob_dist[stadium][player] = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 'out': 0}
            players_balls_faced[stadium][player] = 0

def calculate_probabilities_and_balls(players, players_prob_dist, players_balls_faced):
    """Calculate the probability distributions and count balls faced for the players."""
    batter_keys = [0, 1, 2, 3, 4, 5, 6, 7, 8, 'out']
    for stadium in stadiums:
        for player in players:
            if player in stadium_stats[stadium]['batters']:  # Check if the player has stats
                total_runs = sum(stadium_stats[stadium]['batters'][player].values())
                if total_runs > 0:  # Ensure that the sum of statistics is not zero
                    for batter_key in batter_keys:
                        prob = stadium_stats[stadium]['batters'][player][batter_key] / total_runs
                        players_prob_dist[stadium][player][batter_key] = prob
                # Count the number of balls faced
                players_balls_faced[stadium][player] = sum(stadium_stats[stadium]['batters'][player].values())

# Initialize probability distributions and balls faced
initialize_prob_dist_and_balls(ind_players, ind_players_prob_dist, ind_players_balls_faced)
initialize_prob_dist_and_balls(aus_players, aus_players_prob_dist, aus_players_balls_faced)

# Calculate probabilities and balls faced
calculate_probabilities_and_balls(ind_players, ind_players_prob_dist, ind_players_balls_faced)
calculate_probabilities_and_balls(aus_players, aus_players_prob_dist, aus_players_balls_faced)

# # Pretty print the probability distributions and balls faced
# print("Indian Players' Probability Distributions:")
# pprint(ind_players_prob_dist)
# print("Indian Players' Balls Faced:")
# pprint(ind_players_balls_faced)

# print("\nAustralian Players' Probability Distributions:")
# pprint(aus_players_prob_dist)
# print("Australian Players' Balls Faced:")
# pprint(aus_players_balls_faced)
