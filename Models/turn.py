from pprint import pprint

from match import Match
from model import Model


class Turn(Model):
    _table_name = "Turn"

    def __init__(self):
        super().__init__()
        # TODO : Ajouter une propriété de date de début
        #  et de fin
        self.name = None
        self.matches = []

    def serialized(self):
        serialized_matches = []

        for match in self.matches:
            serialized_matches.append(match.to_tuple())

        serialized_data = {
            'name': self.name,
            'matches': serialized_matches
        }
        return serialized_data

    def save_unique(self):
        table = self.get_table()
        table.truncate()
        table.insert(self.serialized())

    def add_match(self, match: Match):
        self.matches.append(match)

