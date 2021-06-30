from Views.main_view import MainView
import sys

from Core.controller import Controller
from Controllers.TournamentController import TournamentController


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

        if action == "Quitter":
            print("Merci d'avoir utiliser mon logiciel")
            sys.exit()
        elif action == "Gérer le tournois en cours":
            print("Gérer un tournois")
            TournamentController.manage_tournament(self.current_tournament)
            pass
        elif action == "Sélectionner un tournois":
            print("Sélectionner un tournois")
            tournament = TournamentController.select_tournament()
        elif action == "Créer un nouveau tournois":
            print("Créer un tournois")
            TournamentController.create_tournament()

        return MainController(current_tournament=tournament)
