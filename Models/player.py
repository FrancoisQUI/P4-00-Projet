from datetime import date, datetime

from Core.model import Model


class Player(Model):
    _table_name = "Player"

    def __init__(self, first_name=None,
                 name=None,
                 birthdate=None,
                 gender=None,
                 rank=None):
        self.score = 0
        self.first_name = first_name
        self.name = name
        self.birthdate: date = birthdate
        self.gender = gender
        self.rank = rank

    def serialized(self):
        serialized_data = {
            'first_name': self.first_name,
            'name': self.name,
            'birthdate': self.birthdate,
            'gender': self.gender,
            'rank': self.rank,
            'score': self.score}
        return serialized_data

    def deserialize_player_data(self, player_data):
        self.first_name = player_data["first_name"]
        self.name = player_data["name"]
        if type(player_data["birthdate"]) is not datetime.date:
            """ Support for non date format, remove this before swipe the DB"""
            self.birthdate = player_data["birthdate"]
        else:
            self.birthdate = datetime.date(player_data["birthdate"])
        self.gender = player_data["gender"]
        self.rank = int(player_data["rank"])
        try:
            self.score = int(player_data["score"])
        except KeyError:
            self.score = 0
