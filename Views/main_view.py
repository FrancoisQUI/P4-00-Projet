# Externals module
import inquirer
from colorama import init, Fore

# Core imports
from Core.view import View
from variables_settings import VERSION

# Python modules

init()  # initialise colorama module


class MainView(View):
    def __init__(self, current_tournament=None):
        """

        :param current_tournament: None or Tournament
        """
        super().__init__()
        self.current_tournament = current_tournament

        def generate_choice_list(active_tournament=None):
            choices = ['Create tournament',
                       'Select current tournament',
                       'View data']
            if active_tournament is not None:
                choices.append('Manage current tournament')
            choices.append('Quit Tournament Manager')
            return choices

        self.question = [
            inquirer.List('action',
                          message='Choose an action',
                          choices=generate_choice_list(current_tournament),
                          default='Quit Tournament Manager')

        ]

    def render(self):
        print(Fore.GREEN + "CTM: Chess Tournament Manager --------- " +
              Fore.CYAN + "Version : " + VERSION)

        print(Fore.BLUE + "Current tournament ")
        if self.current_tournament is not None:
            print(Fore.RED + self.current_tournament.name)
        else:
            print(Fore.BLUE + "Any")

        action = inquirer.prompt(self.question)
        return action
