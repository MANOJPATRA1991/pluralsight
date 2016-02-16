#!/usr/bin/env python
# -*- coding: utf-8 -*-

score_names = ["Love", "Fifteen", "Thirty", "Forty"]


def tennis_score(player1_points, player2_points):
    if player1_points == player2_points:
        if player1_points >= 3:
            return "Deuce"
        else:
            return "{0}-All".format(score_names[player1_points])
    elif min(player1_points, player2_points) >= 3 and \
            abs(player1_points - player2_points) == 1:
        advantage = (
            "1"
            if player1_points > player2_points
            else "2"
        )
        return "Advantage Player {0}".format(advantage)
    elif max(player1_points, player2_points) >= 4 and \
            abs(player1_points - player2_points) >= 2:
        winner = (
            "1"
            if player1_points > player2_points
            else "2"
        )
        return "Win for Player {0}".format(winner)
    else:
        return "{0}-{1}".format(
            score_names[player1_points],
            score_names[player2_points]
        )
