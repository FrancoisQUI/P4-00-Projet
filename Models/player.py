from datetime import date
from tinydb import where

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
        try:
            serialized_birthdate = self.birthdate.isoformat()
        except AttributeError:
            serialized_birthdate = None

        serialized_data = {
            'first_name': self.first_name,
            'name': self.name,
            'birthdate': serialized_birthdate,
            'gender': self.gender,
            'rank': self.rank,
            'score': self.score
        }

        return serialized_data

    def deserialize_player_data(self, player_data):
        self.first_name = player_data["first_name"]
        self.name = player_data["name"]
        try:
            self.birthdate = date.fromisoformat(str(player_data["birthdate"]))
        except (AttributeError, ValueError):
            self.birthdate = None
        self.gender = player_data["gender"]
        self.rank = int(player_data["rank"])
        try:
            self.score = int(player_data["score"])
        except KeyError:
            self.score = 0

    def save_new(self):
        table = self.get_table()
        table.insert(self.serialized())

    def update(self):
        table = self.get_table()
        obj_to_update = table.get(where("name") == self.name)
        table.update(self.serialized(),
                     doc_ids=[obj_to_update.doc_id])
