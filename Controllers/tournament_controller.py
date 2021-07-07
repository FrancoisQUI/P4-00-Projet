import logging
from pprint import pprint

from Views.tournament_view import TournamentView
from Models.tournament import Tournament
from Core.controller import Controller
from player_controller import PlayerController


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
        tournament.unserialize_tournament_data(tournament_data)
        tournament.save_unique()
        return tournament.serialised()

    @classmethod
    def select_tournament(cls):
        tournaments = Tournament.get_list()
        tournament_name = TournamentView.select_tournament(tournaments)
        tournament_data = Tournament.find_one_by_name(
            tournament_name)
        tournament = Tournament()
        tournament.unserialize_tournament_data(tournament_data)
        return tournament.serialised()

    @classmethod
    def manage_tournament_action(cls, current_tournament):
        action = TournamentView.manage_tournament_action(current_tournament)
        if action == 'Add player':
            pprint(current_tournament)
            PlayerController.create_player(current_tournament)
            print(current_tournament)
        elif action == 'Compute first round':
            # TODO: Compute first round
            pass
        elif action == 'Enter round scores':
            # TODO: Enter round scores
            pass
        elif action == 'Compute next round':
            # TODO: Compute next round
            pass
        else:
            # TODO: Go back
            pass
        return current_tournament
