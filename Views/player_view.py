from pprint import pprint

import inquirer

from player import Player
from view import View


class PlayerView(View):
    def __init__(self, current_tournament=None):
        super().__init__()
        self.current_tournament = current_tournament

    @staticmethod
    def create_new_player_form():
        questions = [
            inquirer.Text('first_name', message='First Name'),
            inquirer.Text('name', message='Name'),
            inquirer.Text('birthdate', message='Birthdate (AAAAMMDD)'),
            inquirer.List('gender',
                          choices=['M', 'F', '?']),
            inquirer.Text('rank', message='Rank')
        ]

        return inquirer.prompt(questions)

    @classmethod
    def add_more_player_question(cls):
        question = [
            inquirer.List('Add Player',
                          message='Add one more player ?',
                          choices=['yes', 'no'])
        ]

        response = inquirer.prompt(question)

        if response['Add Player'] == 'yes':
            return True
        else:
            return False

    @staticmethod
    def select_existing_player():
        existing_players_list = Player.get_list()
        player_choice_list = []

        for player in existing_players_list:
            player_instance = Player()
            player_instance.deserialize_player_data(player)
            player_choice_list.append(player_instance.__dict__)

        checkboxes = [
            inquirer.Checkbox('players',
                              message="Select player to add "
                                      "(Many if necessary)",
                              choices=player_choice_list)
        ]

        response = inquirer.prompt(checkboxes)

        return response['players']
