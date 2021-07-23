from Views.main_view import MainView
import sys

from Core.controller import Controller
from Controllers.tournament_controller import TournamentController
from player_controller import PlayerController


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
            self.current_tournament = TournamentController. \
                manage_tournament_action(self.current_tournament)
        elif action == 'Select current tournament':
            self.current_tournament = TournamentController. \
                select_tournament()
        elif action == 'Create tournament':
            TournamentController.create_tournament()
        elif action == 'View data':
            self.view_data_action()
        return MainController(self.current_tournament)

    def view_data_action(self):
        data_to_view = MainView.choose_data_to_view(self.current_tournament)
        if data_to_view == 'Tournaments List':
            TournamentController.view_tournaments_list()
        elif data_to_view == 'All time players by name':
            PlayerController.view_players_by("first_name")
        elif data_to_view == 'All time players by rank':
            PlayerController.view_players_by("rank")
        elif data_to_view == 'Active tournament players by name':
            TournamentController.view_tournament_players_by(self.current_tournament, "first_name")
        elif data_to_view == 'Active tournament players by rank':
            TournamentController.view_tournament_players_by(self.current_tournament, "rank")
        elif data_to_view == 'Active tournament turns':
            TournamentController.view_tournament_turns(self.current_tournament)
        elif data_to_view == 'Active tournament played matches':
            TournamentController.view_tournament_matches(self.current_tournament)
        elif data_to_view == 'Back':
            pass
        else:
            pass
        self.view.wait_user_action()
        return MainController(self.current_tournament)
