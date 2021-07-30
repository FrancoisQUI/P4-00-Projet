import pandas as pd

from Models.turn import Turn
from Core.view import View


class TurnView(View):
    def __init__(self):
        super().__init__()

    @staticmethod
    def show_turn(turn: Turn):
        match_list_data = []
        for match in turn.matches:
            """ :param match: Match"""
            unique_match = {"Player 1": match.player_1.name,
                            "Player 2": match.player_2.name,
                            "Winner": match.result
                            }
            match_list_data.append(unique_match)

        match_list = pd.DataFrame(match_list_data)
        return print(match_list)
