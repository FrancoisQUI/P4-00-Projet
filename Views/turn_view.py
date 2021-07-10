from pprint import pprint

import inquirer

from turn import Turn
from view import View


class TurnView(View):
    def __init__(self):
        super().__init__()

    @classmethod
    def set_scores_action(cls, turn: Turn):
        matches_result = []
        for match in turn.matches:
            """
            :var match: Match
            """
            choices = [str(match.player_1["name"]),
                       str(match.player_2["name"]),
                       "Draw"]
            question = [
                inquirer.List('Winner',
                              message='Who win the match ?',
                              choices=choices)
            ]
            response = inquirer.prompt(question)
            matches_result.append([match, response])
        return matches_result

