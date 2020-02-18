"""
Draft Sport Python
Player Order By Enumeration
author: hugh@blinkybeach.com
"""
from enum import Enum


class OrderBy(Enum):

    PLAYER_NAME = 'player_name',
    AVERAGE_POINTS = 'average_points'
    POINTS_LAST_ROUND = 'points_last_round'
    TOTAL_SEASON_POINTS = 'total_season_points'
