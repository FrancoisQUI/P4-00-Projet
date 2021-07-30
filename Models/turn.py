from datetime import datetime, date

from Core.model import Model
from Models.match import Match


class Turn(Model):
    _table_name = "Turn"

    def __init__(self):
        super().__init__()
        self.start_date = datetime.now()
        self.name = None
        self.matches = []
        self.end_date: [date, None] = None

    def serialized(self):

        if self is None:
            serialized_data = None

        else:
            serialized_matches = []
            for match in self.matches:
                serialized_matches.append(match.serialized())

            try:
                serialized_end_date = self.end_date.isoformat()
            except AttributeError:
                serialized_end_date = None

            serialized_data = {
                'name': self.name,
                'matches': serialized_matches,
                'start_date': self.start_date.isoformat(),
                'end_date': serialized_end_date
            }

        return serialized_data

    def deserialize_data(self, data):
        self.name = data["name"]
        if isinstance(self.start_date, date) is True:
            self.start_date = date.fromisoformat(str(data["start_date"]))
        else:
            self.start_date = None
        if isinstance(self.end_date, date) is True:
            self.end_date = date.fromisoformat(str(data["end_date"]))
        else:
            self.end_date = None
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
