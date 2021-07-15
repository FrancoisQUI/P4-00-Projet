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
    def create_player(tournament: Tournament):
        add_player = True
        while add_player is True:
            new_player_data = PlayerView.create_new_player_form()
            player = Player()
            player.deserialize_player_data(new_player_data)
            player.save_new()
            tournament.add_player(new_player_data)
            add_player = PlayerView.add_more_player_question()
        return tournament

    @classmethod
    def add_existing_player(cls, tournament: Tournament):
        players = PlayerView.select_existing_player(tournament)
        tournament.players = []
        for player in players:
            tournament.add_player(player)
