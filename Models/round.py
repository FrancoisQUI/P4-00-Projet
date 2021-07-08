from match import Match
from model import Model


class Round(Model):
    _table_name = "Round"

    def __init__(self):
        super().__init__()
        self.name = None
        self.matches = []

    def add_match(self, match: Match):
        self.matches.append(match)
