from pprint import pprint
from colorama import Fore
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
            self.turns_list = tournament_data["turns_list"]
        except KeyError:
            self.turns_list = []

    def serialized(self):

        serialized_turn_list = []
        print(Fore.RED + "-----Turns list")
        pprint(self.turns_list)
        for turn in self.turns_list:
            for match in turn.matches:
                unique_turn = match.serialized()
                serialized_turn_list.append(unique_turn)

        serialized_players = []

        for player in self.players:
            serialized_players.append(player.serialized())

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
            'ongoing_turn': self.ongoing_turn.serialized()
        }
        print("------- Serialized tournament : ")
        pprint(serialized_data)
        return serialized_data

    def update(self):
        table = self.get_table()
        obj_to_update = table.get(where("name") == self.__dict__["name"])
        table.update(self.serialized(),
                     doc_ids=[obj_to_update.doc_id])

    def compute_round(self) -> Turn:
        players_list = self.players
        turn = Turn()
        turn.name = f"Round {str(len(self.turns_list))}"
        """ Add a fake player if there are odd players """
        if len(self.players) % 2 != 0:
            fake_player = Player(name="fake", first_name="fake", rank=0)
            players_list.append(fake_player)

        if len(self.turns_list) == 0:
            """ the first turn : matches are computed with the rank """
            sorted_players = sorted(players_list, key=lambda x: x.rank)

            pprint(sorted_players)
            middle = round(len(sorted_players)/2)
            lower_players = sorted_players[:middle]
            upper_players = sorted_players[(len(sorted_players) - middle):]
            for i in range(middle):
                match = Match()
                match.player_1 = upper_players[i]
                match.player_2 = lower_players[i]
                turn.add_match(match)
            self.ongoing_turn = turn

        else:
            print(Fore.GREEN + "It's me the next turn!!!")
            # TODO: Compute others rounds
        return turn

    def close_ongoing_turn(self):
        self.turns_list.append(self.ongoing_turn)
        self.ongoing_turn = None
        pprint(self.__dict__)

