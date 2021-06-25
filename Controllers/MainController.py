from Views.MainView import MainView
import sys

from pprint import pprint
import logging

from Core.Controller import Controller




class MainController(Controller):
    logging.info("J'entre dans MainController")

    def __init__(self):
        logging.info("MainController constructor")
        self.view = MainView()
        self.view.clear()
        self.render = self.view.render()
        self.do_action(self.render["action"])

    @staticmethod
    def do_action(action):
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
            # TODO: Créer l'action "Créer" dans le TournamentController
            pass
