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
        action = TournamentView.manage_tournament_action(tournament)
        pprint(action)
        if action == 'Add new player':
            PlayerController.create_player(tournament)
        elif action == 'Add existing player':
            PlayerController.add_existing_player(tournament)
        elif action == 'Compute first round':
            tournament.compute_round()
            TurnController.set_scores(tournament.ongoing_turn)
            tournament.update()
        elif action == 'Enter round scores':
            # TODO: Enter round scores
            pass
        elif action == 'Compute next round':
            # TODO: Compute next round
            pass
        else:
            # TODO: Go back
            pass
        return tournament
