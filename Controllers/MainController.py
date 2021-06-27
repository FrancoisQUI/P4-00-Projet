from Views.MainView import MainView
import sys

from Core.Controller import Controller
from Controllers.TournamentController import TournamentController


class MainController(Controller):

    def __init__(self):
        super().__init__()
        self.logger.info("MainController constructor")
        self.view = MainView()
        self.view.clear()
        self.render = self.view.render()
        self.do_action(self.render["action"])

    @staticmethod
    def do_action(action):
        next_action = None
        if action == "Quitter":
            print("Merci d'avoir utiliser mon logiciel")
            sys.exit()
        elif action == "Gérer le tournois en cours":
            print("Gérer un tournois")
            # TODO: Créer l'action "gérer" dans le TournamentController
            pass
        elif action == "Sélectionner un tournois":
            print("Sélectionner un tournois")
            # TODO: Créer l'action "Select" dans le TournamentController
            pass
        elif action == "Créer un nouveau tournois":
            print("Créer un tournois")
            next_action = TournamentController.create_tournament()

        return next_action
