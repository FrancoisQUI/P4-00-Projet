from pprint import pprint, pformat

from match import Match
from model import Model
from player import Player
from round import Round


class Tournament(Model):
    _table_name = "Tournament"
    players = []

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
        self.turn_number = len(self.turns_list) + 1

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

    def compute_round(self):
        players_list = self.players
        _round = Round()
        _round_number = str(self.turn_number)
        _round.name = f"Round {str(_round_number)}"
        """ Add a fake player if there are odd players """
        if len(self.players) % 2 != 0:
            fake_player = Player(name="fake", first_name="fake", rank="0")
            players_list.append(fake_player.serialized())

        """ the first turn : matches are computed with the rank """
        if self.turn_number is 1:
            sorted_players = sorted(players_list, key=lambda x: x["rank"])
            middle = round(len(sorted_players)/2)
            lower_players = sorted_players[:middle]
            upper_players = sorted_players[(len(sorted_players) - middle):]
            for i in range(middle):
                _match = Match()
                _match.player_1 = upper_players[i]
                _match.player_2 = lower_players[i]
                _round.add_match(_match)
                pprint(_match.__dict__)
                pprint(_match.to_tuple())
            pprint(_round.__dict__, width=2)
        return _round


