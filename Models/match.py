from model import Model
from player import Player


class Match(Model):

    def __init__(self, player_1: Player = None,
                 player_2: Player = None,
                 player_1_score: int = 0,
                 player_2_score: int = 0):
        super().__init__()
        self.player_1 = player_1
        self.player_2 = player_2
        self.player_1_score = player_1_score
        self.player_2_score = player_2_score

    def to_tuple(self):
        return (
            [self.player_1, self.player_2],
            [self.player_1_score, self.player_2_score]
        )

