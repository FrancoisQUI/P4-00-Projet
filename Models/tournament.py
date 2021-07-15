from datetime import datetime
from pprint import pprint

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
        """ :param self.ongoing_turn: Turn or None"""
        self.ongoing_turn = None

    def deserialize_tournament_data(self, tournament_data):
        self.name = tournament_data["name"]
        self.place = tournament_data["place"]
        self.start_date = tournament_data["start_date"]
        self.end_date = tournament_data["end_date"]
        self.number_of_turns = tournament_data["number_of_turns"]
        self.time_control = tournament_data["time_control"]
        self.description = tournament_data["description"]

        try:
            for player_data in tournament_data["players"]:
                unique_player = Player()
                unique_player.deserialize_player_data(player_data)
                self.players.append(unique_player)
        except KeyError:
            self.players = []

        try:
            self.turns_list = []
            for turn in tournament_data["turns_list"]:
                unique_turn = Turn()
                unique_turn.deserialize_data(turn)
                self.turns_list.append(unique_turn)

        except KeyError:
            self.turns_list = []

    def serialized(self):
        serialized_turn_list = []
        for turn in self.turns_list:
            serialized_turn_list.append(turn.serialized())

        serialized_players = []
        for player in self.players:
            serialized_players.append(player.serialized())

        if self.ongoing_turn is None:
            serialized_ongoing_turn = None
        else:
            serialized_ongoing_turn = self.ongoing_turn.serialized()

        serialized_data = {
            'name': self.name,
            'place': self.place,
            'start_date': self.start_date,
            'end_date': self.end_date,
            'number_of_turns': self.number_of_turns,
            'time_control': self.time_control,
            'description': self.description,
            'players': serialized_players,
            'turns_list': serialized_turn_list,
            'ongoing_turn': serialized_ongoing_turn
        }
        return serialized_data

    def update(self):
        table = self.get_table()
        obj_to_update = table.get(where("name") == self.__dict__["name"])
        table.update(self.serialized(),
                     doc_ids=[obj_to_update.doc_id])

    def compute_round(self) -> Turn:
        turn = Turn()
        turn.name = f"Round {str(len(self.turns_list))}"

        if len(self.turns_list) == 0:
            """ Add a fake player if there are odd players """
            if len(self.players) % 2 != 0:
                fake_player = Player(name="fake", first_name="fake", rank=0)
                self.players.append(fake_player)
            """ the first turn : matches are computed with the rank """
            sorted_players = sorted(self.players, key=lambda x: x.rank)
            middle = round(len(sorted_players) / 2)
            upper_players = sorted_players[(len(sorted_players) - middle):]
            lower_players = sorted_players[:middle]
            for i in range(middle):
                match = Match()
                match.player_1 = upper_players[i]
                match.player_2 = lower_players[i]
                turn.add_match(match)
            self.ongoing_turn = turn

        else:
            sorted_players = sorted(self.players, key=lambda x: x.score)
            middle = round(len(sorted_players) / 2)
            for i in range(middle):
                match = Match()
                a = 0
                b = 1
                existing_match = False
                while existing_match is True:
                    existing_match = self.check_match_for_players(sorted_players[a],
                                                                  sorted_players[b])
                    b += 1
                match.player_1 = sorted_players[a]
                match.player_2 = sorted_players[b]
                sorted_players.remove(match.player_1)
                sorted_players.remove(match.player_2)
                turn.add_match(match)
            self.ongoing_turn = turn
        return turn

    def close_ongoing_turn(self):
        self.ongoing_turn.set_end_date(datetime.now())
        self.turns_list.append(self.ongoing_turn)
        self.ongoing_turn = None

    def add_player(self, player_data):
        new_player = Player()
        new_player.deserialize_player_data(player_data)
        self.players.append(new_player)

    def check_match_for_players(self, player_1, player_2) -> bool:
        for turn in self.turns_list:
            for match in turn.matches:
                """ :var match: Match """
                if player_1 == match.player_1 and \
                        player_2 == match.player_2 or \
                        player_2 == match.player_1 and \
                        player_1 == match.player_2:
                    return True
                else:
                    return False
