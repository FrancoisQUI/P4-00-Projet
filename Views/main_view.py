
from pprint import pprint

import inquirer
from colorama import init, Fore


from Core.view import View
from tournament import Tournament
from variables_settings import VERSION


init()  # initialise colorama module


class MainView(View):
    def __init__(self, current_tournament=None):
        """
        :param current_tournament: None or Tournament
        """
        super().__init__()
        self.current_tournament = current_tournament

    @staticmethod
    def select_main_action(current_tournament: Tournament = None) -> str:
        """
        Header
        :param current_tournament: Tournament
        :return: string
        """
        pprint(current_tournament)
        print(Fore.GREEN + "CTM: Chess Tournament Manager --------- " +
              Fore.CYAN + "Version : " + VERSION)

        print(Fore.BLUE + "Current tournament ")
        if current_tournament is not None:
            print(Fore.RED + current_tournament.name)
        else:
            print(Fore.BLUE + "Any")

        """
        prompt question
        """

        choices = ['Create tournament',
                   'Select current tournament',
                   'View data']
        if current_tournament is not None:
            choices.append('Manage current tournament')
        choices.append('Quit Tournament Manager')

        question = [inquirer.List('action',
                                  message='Choose an action',
                                  choices=choices,
                                  default='Quit Tournament Manager')]

        action = inquirer.prompt(question)
        action = action["action"]

        return action

    @classmethod
    def choose_data_to_view(cls, current_tournament: Tournament = None):
        choices = ['Tournaments List',
                   'All time players by name',
                   'All time players by rank']
        if current_tournament is not None:
            active_tournament_choices = ['Active tournament players by name',
                                         'Active tournament players by rank',
                                         'Active tournament played turns',
                                         'Active tournament played matches']
            choices += active_tournament_choices

        choices.append('Back')
        question = [inquirer.List('data_to_view',
                                  message='view data :',
                                  choices=choices,
                                  default='Tournaments List')]

        data_to_view = inquirer.prompt(question)
        data_to_view = data_to_view['data_to_view']

        return data_to_view
