from pprint import pprint

from Views.main_view import MainView
import sys

from Core.controller import Controller
from Controllers.tournament_controller import TournamentController


class MainController(Controller):

    def __init__(self, current_tournament=None):
        super().__init__()
        self.current_tournament = current_tournament
        self.view = MainView(current_tournament)
        self.view.clear()
        action = MainView.select_main_action(self.current_tournament)
        self.do_action(action)

    def do_action(self, action):
        if action == 'Quit Tournament Manager':
            print("Tournament manager closed")
            sys.exit()
        elif action == 'Manage current tournament':
            self.current_tournament = TournamentController.\
                manage_tournament_action(self.current_tournament)
        elif action == 'Select current tournament':
            self.current_tournament = TournamentController.\
                select_tournament()
        elif action == 'Create tournament':
            TournamentController.create_tournament()
        elif action == 'View data':
            self.view_data_action(self.current_tournament)
        return MainController(self.current_tournament)

    @staticmethod
    def view_data_action(current_tournament=None):
        data_to_view = MainView.choose_data_to_view(current_tournament)
        if data_to_view == 'Tournaments List':
            pass
        elif data_to_view == 'All time players by name':
            pass
        elif data_to_view == 'All time players by rank':
            pass
        elif data_to_view == 'Active tournament players by name':
            pass
        elif data_to_view == 'Active tournament players by rank':
            pass
        elif data_to_view == 'Active tournament played turns':
            pass
        elif data_to_view == 'Active tournament played matches':
            pass
        else:
            pass
        return MainController(current_tournament)
