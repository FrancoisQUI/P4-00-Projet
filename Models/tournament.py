from model import Model


class Tournament(Model):
    _table_name = "Tournament"

    def __init__(self, name=None,
                 place=None,
                 start_date=None,
                 end_date=None,
                 number_of_turns=None,
                 time_control=None,
                 description=None):

        super().__init__()

        self.name = name
        self.place = place
        self.start_date = start_date
        self.end_date = end_date
        self.number_of_turns = number_of_turns
        self.time_control = time_control
        self.description = description
        self.players = []
        self.turns_list = []

    def unserialize_tournament_data(self, tournament_data):
        self.name = tournament_data["name"]
        self.place = tournament_data["place"]
        self.start_date = tournament_data["start_date"]
        self.end_date = tournament_data["end_date"]
        self.number_of_turns = tournament_data["number_of_turns"]
        self.time_control = tournament_data["time_control"]
        self.description = tournament_data["description"]

        try:
            self.players = tournament_data["players"]
        except KeyError:
            self.players = []

        try:
            self.turns_list = tournament_data["turns_list"]
        except KeyError:
            self.turns_list = []

    def serialised(self):
        serialized_data = {
            'name': self.name,
            'place': self.place,
            'start_date': self.start_date,
            'end_date': self.end_date,
            'number_of_turns': self.number_of_turns,
            'time_control': self.time_control,
            'description': self.description,
            'players': self.players,
            'turns_list': self.turns_list
        }
        return serialized_data
