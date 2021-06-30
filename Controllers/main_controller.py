from Views.main_view import MainView
import sys

from Core.controller import Controller
from Controllers.tournament_controller import TournamentController


class MainController(Controller):

    def __init__(self, current_tournament=None):
        super().__init__()
        self.current_tournament = current_tournament
        self.logger.info("MainController constructor")
        self.view = MainView(current_tournament)
        self.view.clear()
        self.render = self.view.render()
        self.do_action(self.render["action"])

    def do_action(self, action):
        tournament = None

        if action == 'Quit Tournament Manager':
            print("Tournament manager closed")
            sys.exit()
        elif action == 'Manage current tournament':
            tournament = TournamentController.manage_tournament(self.current_tournament)
        elif action == 'Select current tournament':
            tournament = TournamentController.select_tournament()
        elif action == 'Create tournament':
            TournamentController.create_tournament()

        return MainController(current_tournament=tournament)
