# Externals module
import inquirer
from colorama import init

# Core imports
from Core.View import View

init()  # initialise colorama module


class MainView(View):
    def __init__(self):
        super().__init__()
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
        print("Bienvenue dans le gestionnaire de tournois")
        action = inquirer.prompt(self.question)
        return action
