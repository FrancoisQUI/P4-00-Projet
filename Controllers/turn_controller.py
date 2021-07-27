from Models.turn import Turn
from Views.match_view import MatchView
from Core.controller import Controller


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
