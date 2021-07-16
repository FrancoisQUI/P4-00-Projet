from pprint import pprint

import inquirer
import pandas as pd

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
    def select_existing_player(tournament=None):
        existing_players_list = Player.get_list()
        player_choice_list = []
        already_registered_players = []

        for player in existing_players_list:
            player_instance = Player()
            player_instance.deserialize_player_data(player)
            player_choice_list.append(player_instance.__dict__)

        for player in tournament.players:
            already_registered_players.append(player.__dict__)

        checkboxes = [
            inquirer.Checkbox('players',
                              message="Select player to add "
                                      "(Many if necessary)",
                              choices=player_choice_list,
                              default=already_registered_players)
        ]

        response = inquirer.prompt(checkboxes)

        return response['players']

    @staticmethod
    def name_player(player: Player):
        return f"| Name : {player.name} Firstname : {player.first_name} |"

    @staticmethod
    def simple_player_description(player: Player):
        return \
            print(f"| Name : {player.name} "
                  f"Firstname : {player.first_name} "
                  f"score: {player.score} |")

    @staticmethod
    def view_list(a_player_list, sorted_by=None):
        """

        :param a_player_list: list of Player
        :param sorted_by: must be a column name ("name", "first_name",
                                   "birthdate", "gender",
                                   "rank")
        :return: a print of the list in a Pandas dataframe
        """
        player_list = pd.DataFrame(a_player_list)
        player_list = player_list[["name", "first_name",
                                   "birthdate", "gender",
                                   "rank"]]
        if sorted_by == "first_name":
            player_list = player_list.loc[player_list["first_name"].str.lower().sort_values().index]
        if sorted_by == "rank":
            player_list = player_list.sort_values(by="rank", ascending=False)

        return print(player_list)
