import inquirer
import pandas as pd

from match import Match
from view import View


class MatchView(View):
    def __init__(self):
        super().__init__()

    @classmethod
    def register_match_score_action(cls, match: Match):
        choices = [match.player_1.name, match.player_2.name, "draw"]
        question = [
            inquirer.List("Winner",
                          choices=choices,
                          message="Who win the match ?",
                          default="draw")
        ]

        response = inquirer.prompt(question)

        return response

    @classmethod
    def show_matches(cls, match_list: [Match]):
        match_list_data = []
        for match in match_list:
            """ :param match: Match"""
            unique_match = {"Player 1": match.player_1.name,
                            "Player 2": match.player_2.name,
                            "Winner": match.result,
                            "Turn": match.turn
                            }
            match_list_data.append(unique_match)

        show_list = pd.DataFrame(match_list_data)
        show_list = show_list.loc[show_list["Player 1"].str.lower().sort_values().index]
        return print(show_list)
