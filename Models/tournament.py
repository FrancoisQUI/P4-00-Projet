from pprint import pprint, pformat

from tinydb import where

from match import Match
from model import Model
from player import Player
from turn import Turn


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
        self.ongoing_turn: Turn() = None

        self.turn_number = len(self.turns_list) + 1

    def deserialize_tournament_data(self, tournament_data):
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
            'turns_list': self.turns_list,
            'ongoing_turn': self.ongoing_turn.serialized()
        }
        return serialized_data

    def update(self):
        table = self.get_table()
        obj_to_update = table.get(where("name") == self.__dict__["name"])
        table.update(self.serialised(),
                     doc_ids=[obj_to_update.doc_id])

    def compute_round(self) -> Turn:
        players_list = self.players
        turn = Turn()
        turn.name = f"Round {str(self.turn_number)}"
        """ Add a fake player if there are odd players """
        if len(self.players) % 2 != 0:
            fake_player = Player(name="fake", first_name="fake", rank=0)
            players_list.append(fake_player.serialized())

        if self.turn_number is 1:
            """ the first turn : matches are computed with the rank """
            sorted_players = sorted(players_list, key=lambda x: x["rank"])

            pprint(sorted_players)
            middle = round(len(sorted_players)/2)
            lower_players = sorted_players[:middle]
            upper_players = sorted_players[(len(sorted_players) - middle):]
            for i in range(middle):
                _match = Match()
                _match.player_1 = upper_players[i]
                _match.player_2 = lower_players[i]
                turn.add_match(_match)
            self.ongoing_turn = turn
            return turn
        else:

            # TODO: Compute others rounds
            pass
            return turn

    def close_ongoing_turn(self):
        self.turns_list.append(self.ongoing_turn)
        self.ongoing_turn = None

