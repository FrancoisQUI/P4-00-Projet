from pprint import pprint

import inquirer

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
