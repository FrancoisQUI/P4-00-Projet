import logging
from pprint import pprint

from Views.tournament_view import TournamentView
from Models.tournament import Tournament
from Core.controller import Controller
from player_controller import PlayerController
from turn_controller import TurnController


class TournamentController(Controller):

    def __init__(self):
        super().__init__()
        self.view = TournamentView()
        self.view.clear()
        self.logger.info("TournamentController constructor")

    @staticmethod
    def create_tournament():
        tournament_data = TournamentView.create_tournament_form()
        tournament = Tournament()
        tournament.deserialize_tournament_data(tournament_data)
        tournament.save_new()
        return tournament

    @classmethod
    def select_tournament(cls):
        tournament_name = TournamentView.select_tournament()
        tournament_data = Tournament.find_one_by_name(
            tournament_name)
        tournament = Tournament()
        tournament.deserialize_tournament_data(tournament_data)
        return tournament

    @classmethod
    def manage_tournament_action(cls, tournament: Tournament):
        pprint(tournament.__dict__)
        action = TournamentView.manage_tournament_action(tournament)
        if action == 'Add new player':
            PlayerController.create_player(tournament)
        elif action == 'Add existing player':
            PlayerController.add_existing_player(tournament)
        elif action == 'Compute first turn':
            tournament.compute_round()
        elif action == 'Enter turn scores':
            TurnController.set_scores(tournament.ongoing_turn)
            tournament.close_ongoing_turn()
        elif action == 'Compute next turn':
            tournament.compute_round()
        elif action == 'Save Tournament':
            pprint(tournament)
            tournament.update()
        else:
            pass
        return tournament
