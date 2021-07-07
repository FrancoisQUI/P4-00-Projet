from pprint import pprint

from controller import Controller
from player import Player
from player_view import PlayerView
from tournament import Tournament


class PlayerController(Controller):
    def __init__(self, current_tournament=None):
        super().__init__()
        self.view = PlayerView()
        self.current_tournament = current_tournament

    @staticmethod
    def create_player(tournament_data):
        tournament = Tournament()
        tournament.unserialize_tournament_data(tournament_data)
        add_player = True
        while add_player is True:
            new_player_data = PlayerView.create_new_player_form()
            player = Player()
            player.unserialize_player_data(new_player_data)
            player.save_new()
            tournament.players.append(player.__dict__)
            add_player = PlayerView.add_more_player_question()
        tournament.update()

        return tournament.serialised()
