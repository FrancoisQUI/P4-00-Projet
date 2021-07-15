from pprint import pprint

import inquirer

from Core.view import View
from player_view import PlayerView
from tournament import Tournament


class TournamentView(View):

    def __init__(self):
        super().__init__()

    @staticmethod
    def create_tournament_form():
        questions = [
            inquirer.Text('name',
                          message="The Tournament Name ? "),
            inquirer.Text('place',
                          message="Where is the tournament ? "),
            inquirer.Text('start_date',
                          message="When the tournament starts ? "
                                  "Must be a number : AAAAMMDD"),
            # TODO: Validate date format
            inquirer.Text('end_date',
                          message="When the tournament finish ? "
                                  "Must be a number : AAAAMMDD"),
            # TODO: Validate date format
            inquirer.Text('number_of_turns',
                          message="How many turns ? Default 8",
                          default=8),
            inquirer.List('time_control',
                          message="What kind of time control ? ",
                          choices=["Bullet", "Blitz", "Quick hit"],
                          default="Bullet"),
            inquirer.Text('description',
                          message="describe the tournament")
        ]

        return inquirer.prompt(questions)

    @staticmethod
    def select_tournament():
        tournaments = Tournament.get_list()
        tournaments_list = []
        for tournament in tournaments:
            try:
                tournaments_list.append(tournament['name'])
            except KeyError:
                pass
            # TODO: regarder pour faire un IF
        select = [inquirer.List('selected_tournament',
                                message='Choose a tournament',
                                choices=tournaments_list)]
        response = inquirer.prompt(select)
        return response['selected_tournament']

    @classmethod
    def manage_tournament_action(cls, current_tournament: Tournament):

        cls.clear()
        print("--------------------------")
        print("Current tournament : " +
              current_tournament.name)
        print("Current turn : " + str(len(current_tournament.turns_list)+1))
        if len(current_tournament.players) >= 2:
            print("Current players : ")
            for player in current_tournament.players:
                PlayerView.simple_player_description(player)
        else:
            print("Add players before compute the first turn")
        print("--------------------------")

        def get_choices(tournament: Tournament):
            choices = []
            if len(tournament.turns_list)+1 <= int(tournament.number_of_turns):
                if len(tournament.turns_list) == 0 and \
                        tournament.ongoing_turn is None:
                    choices.append('Add new player')
                    choices.append('Add existing player')
                if len(tournament.players) >= 2 and \
                        tournament.ongoing_turn is None and\
                        len(tournament.turns_list) == 0:
                    choices.append('Compute first turn')
                if len(tournament.turns_list) > 0 and \
                        tournament.ongoing_turn is None:
                    choices.append('Compute next turn')
                if tournament.ongoing_turn is not None:
                    choices.append('Enter turn scores')
            choices.append('Save Tournament')
            choices.append('Go Back')
            return choices

        actions = [
            inquirer.List('Action',
                          choices=get_choices(current_tournament))]

        response = inquirer.prompt(actions)

        return response["Action"]
