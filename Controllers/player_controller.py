from Core.controller import Controller

from Models.player import Player
from Models.tournament import Tournament

from Views.player_view import PlayerView


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

    @classmethod
    def view_players_by(cls, sorted_by):
        players_list = Player.get_list()
        PlayerView.view_list(players_list, sorted_by)

    @staticmethod
    def edit_player_rank():
        player_data_to_edit = PlayerView.select_unique_player()
        player = Player()
        player.deserialize_player_data(player_data_to_edit)
        player.rank = int(PlayerView.edit_player_rank())
        player.update()
