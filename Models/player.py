from datetime import datetime

from model import Model


class Player(Model):
    _table_name = "Player"

    def __init__(self, first_name=None,
                 name=None,
                 birthdate=None,
                 gender=None,
                 rank=None):
        self.first_name = first_name
        self.name = name
        self.birthdate = birthdate
        self.gender = gender
        self.rank = rank

    def serialized(self):
        serialized_data = {
            'first_name': self.first_name,
            'name': self.name,
            'birthdate': self.birthdate,
            'gender': self.gender,
            'rank': self.rank}
        return serialized_data

    def deserialize_player_data(self, player_data):
        self.first_name = player_data["first_name"]
        self.name = player_data["name"]
        self.birthdate = player_data["birthdate"]
        self.gender = player_data["gender"]
        self.rank = int(player_data["rank"])

