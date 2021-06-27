# Externals module
import inquirer
from colorama import init, Fore

# Python modules
from pprint import pprint
import logging

# Core imports
from Core.View import View


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
                          message="Witch Time Control Type ? ",
                          choices=["Bullet", "Blitz", "Quick hit"],
                          # TODO: Vérifier la traduction de "coup rapide" pour les echecs
                          default="Bullet"),
            inquirer.Text('description',
                          message="describe the tournament")
        ]

        return inquirer.prompt(questions)


