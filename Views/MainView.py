# Externals module
import inquirer
from colorama import init, Fore

# Python modules
from pprint import pprint

# Core imports
from Core.View import View

init()  # initialise colorama module


class MainView(View):
    def __init__(self, current_tournament=None):
        """

        :param current_tournament: None or Tournament
        """
        super().__init__()
        self.current_tournament = current_tournament
        self.question = [
            inquirer.List('action',
                          message='Que souhaitez vous faire ?',
                          choices=['Créer un nouveau tournois',
                                   'Sélectionner un tournois',
                                   'Gérer le tournois en cours',
                                   'Quitter'],
                          default='Quitter')

        ]

    def render(self):
        print(Fore.GREEN + "Bienvenue dans le gestionnaire de tournois")

        if self.current_tournament is not None:
            print(Fore.BLUE + "Tournois Actuel : ")
            pprint(self.current_tournament)

        action = inquirer.prompt(self.question)
        return action
