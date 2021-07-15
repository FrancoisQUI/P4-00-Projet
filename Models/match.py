from pprint import pprint

from model import Model
from player import Player


class Match(Model):

    def __init__(self, player_1: Player = None,
                 player_2: Player = None,):
        """
        :param player_1: Player
        :param player_2: Player
        """
        super().__init__()
        self.player_1: Player = player_1
        self.player_2: Player = player_2

    def serialized(self):
        serialized_data = {
            'player_1': self.player_1.serialized(),
            'player_2': self.player_2.serialized()
        }
        return serialized_data

    def deserialize_data(self, data):
        self.player_1 = Player()
        self.player_1.deserialize_player_data(data["player_1"])
        self.player_2 = Player()
        self.player_2.deserialize_player_data(data["player_2"])

    def to_tuple(self):
        return (
            [self.player_1.serialized(), self.player_2.serialized()],
            [self.player_1.score, self.player_2.score]
        )

    def set_scores(self, match_result):
        if match_result == self.player_1.name:
            self.player_1.score += 1
        elif match_result == self.player_2.name:
            self.player_2.score += 1
        else:
            self.player_1.score += .5
            self.player_2.score += .5
        pprint(self.__dict__)
