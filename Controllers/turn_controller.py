from pprint import pprint

from controller import Controller
from match_view import MatchView
from turn import Turn


class TurnController(Controller):
    def __init__(self, turn: Turn):
        super().__init__()
        self.turn = turn

    @classmethod
    def set_scores(cls, turn):
        for match in turn.matches:
            match_result = MatchView.register_match_score_action(match)
            match.set_scores(match_result["Winner"])
        pass
