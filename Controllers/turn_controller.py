from controller import Controller
from turn import Turn
from turn_view import TurnView


class TurnController(Controller):
    def __init__(self, turn: Turn):
        super().__init__()
        self.turn = turn

    @classmethod
    def set_scores(cls, turn):
        scores_list = TurnView.set_scores_action(turn)
        turn.set_scores(scores_list)
        pass
