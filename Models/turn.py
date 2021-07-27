from datetime import datetime

from Core.model import Model
from Models.match import Match


class Turn(Model):
    _table_name = "Turn"

    def __init__(self):
        super().__init__()
        self.start_date = datetime.now()
        self.name = None
        self.matches = []
        self.end_date = None

    def serialized(self):
        if self is None:
            serialized_data = None

        else:
            serialized_matches = []
            for match in self.matches:
                serialized_matches.append(match.serialized())

            serialized_data = {
                'name': self.name,
                'matches': serialized_matches,
                'start_date': self.start_date,
                'end_date': self.end_date
            }

        return serialized_data

    def deserialize_data(self, data):
        self.name = data["name"]
        self.start_date = datetime.date(data["start_date"])
        self.end_date = datetime.date(data["end_date"])
        self.matches = []
        for match in data["matches"]:
            unique_match = Match()
            unique_match.deserialize_data(match)
            self.matches.append(unique_match)

    def save_unique(self):
        table = self.get_table()
        table.truncate()
        table.insert(self.serialized())

    def add_match(self, match: Match):
        self.matches.append(match)

    def set_end_date(self, date):
        self.end_date = date
