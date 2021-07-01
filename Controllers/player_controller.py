from pprint import pprint

from controller import Controller
from player_view import PlayerView


class PlayerController(Controller):
    def __init__(self, current_tournament=None):
        super().__init__()
        self.view = PlayerView()
        self.current_tournament = current_tournament

    @staticmethod
    def create_player(tournament):
        new_player_datas = PlayerView.create_new_player_form()
        tournament['players'].append(new_player_datas)
        pprint(tournament)
        return tournament
