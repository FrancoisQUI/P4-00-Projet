from model import Model


class Tournament(Model):
    _table_name = "Tournament"

    def __init__(self, tournament_data=None):
        """
        Describe a tournament

        :param tournament_data: must be a dict like this example :
                {'description': 'Test',
                'end_date': '20211010',
                'name': 'Test',
                'number_of_turns': '8',
                'place': 'Nowhere',
                'start_date': '20211010',
                'time_control': 'Blitz'}
        """
        super().__init__()
        if tournament_data is not None:
            self.name = tournament_data["name"]
            self.place = tournament_data["place"]
            self.start_date = tournament_data["start_date"]
            self.end_date = tournament_data["end_date"]
            self.number_of_turns = tournament_data["number_of_turns"]
            self.time_control = tournament_data["time_control"]
            self.description = tournament_data["description"]
            self.players = []
            self.turns_list = []



