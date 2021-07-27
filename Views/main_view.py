import inquirer
from colorama import init, Fore

from Core.variables_settings import VERSION
from Core.view import View
from Models.tournament import Tournament

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
        """
        app and current tournament informations
        """
        print(f"{Fore.GREEN}CTM: {Fore.LIGHTGREEN_EX}Chess Tournament Manager "
              f"--------- {Fore.LIGHTBLUE_EX}{VERSION : >10}")

        print(Fore.BLUE + "Current tournament ")
        if current_tournament is not None:
            print(Fore.RED + current_tournament.name)
        else:
            print(Fore.BLUE + "Select or create a tournament")

        """
        prompt question
        """
        choices = ['Create tournament']
        if len(Tournament.get_list()) != 0:
            choices.append('Select current tournament')
            choices.append('View data')
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
                                         'Active tournament turns',
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
