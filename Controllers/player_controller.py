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
            tournament.players.append(player.serialized())
            add_player = PlayerView.add_more_player_question()
        tournament.update()

        return tournament

    @classmethod
    def add_existing_player(cls, tournament: Tournament):
        players = PlayerView.select_existing_player()
        for player in players:
            new_player = Player()
            new_player.deserialize_player_data(player)
            tournament.players.append(player)
        tournament.update()

