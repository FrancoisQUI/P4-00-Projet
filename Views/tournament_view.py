# Externals module
import inquirer


# Python modules
from pprint import pprint
import logging

# Core imports
from Core.view import View
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
                          # TODO: Vérifier la traduction de "coup rapide" pour les échecs
                          default="Bullet"),
            inquirer.Text('description',
                          message="describe the tournament")
        ]

        return inquirer.prompt(questions)

    @staticmethod
    def select_tournament(tournaments):
        tournaments_list = []
        for tournament in tournaments:
            tournaments_list.append(tournament['name'])
        select = [inquirer.List('selected_tournament',
                                message='Choose a tournament',
                                choices=tournaments_list)]
        return inquirer.prompt(select)

    @staticmethod
    def manage_tournament(current_tournament):
        pass

