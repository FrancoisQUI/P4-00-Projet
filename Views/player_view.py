import inquirer
import pandas as pd

from Core.view import View
from Models.player import Player


class PlayerView(View):
    def __init__(self, current_tournament=None):
        super().__init__()
        self.current_tournament = current_tournament

    @classmethod
    def create_new_player_form(cls):

        questions = [
            inquirer.Text('first_name', message='First Name'),
            inquirer.Text('name', message='Name'),
            inquirer.Text('birthdate',
                          message='Birthdate (YYYY-MM-DD)',
                          validate=cls.validate_date_format),
            inquirer.List('gender',
                          choices=['M', 'F', '?']),
            inquirer.Text('rank', message='Rank',
                          validate=cls.validate_rank_format)
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
            selection = player_list["name"].str.lower().sort_values().index
            player_list = \
                player_list.loc[selection]
        elif sorted_by == "rank":
            player_list = player_list.sort_values(by="rank", ascending=False)

        return print(player_list)

    @staticmethod
    def select_unique_player():
        players = Player.get_list()
        player_list = []
        for player in players:
            player_list.append(player)

        question = [
            inquirer.List('player',
                          message='Choose a player to edit',
                          choices=player_list)
        ]
        response = inquirer.prompt(question)
        return response['player']

    @classmethod
    def edit_player_rank(cls):
        question = [
            inquirer.Text('rank', message='Rank',
                          validate=cls.validate_rank_format)
        ]

        response = inquirer.prompt(question)

        return response["rank"]
