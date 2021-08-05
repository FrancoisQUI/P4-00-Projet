import re
import pandas as pd
import inquirer
from inquirer import errors

from Models.tournament import Tournament

from Views.match_view import MatchView
from Views.player_view import PlayerView

from Core.view import View


class TournamentView(View):

    def __init__(self):
        super().__init__()

    @classmethod
    def create_tournament_form(cls):
        def validate_number_of_turns(answer, current):
            if not re.match("^[0-9]{1,2}$",
                            current):
                raise errors.ValidationError('',
                                             reason='Must be a number '
                                                    'between 1 to 99')
            return True

        questions = [
            inquirer.Text('name',
                          message="The Tournament Name ? "),
            inquirer.Text('place',
                          message="Where is the tournament ? "),
            inquirer.Text('start_date',
                          message="When the tournament starts ? "
                                  "Must be a number : YYYY-MM-DD",
                          validate=cls.validate_date_format),
            inquirer.Text('end_date',
                          message="When the tournament finish ? "
                                  "Must be a number : YYYY-MM-DD",
                          validate=cls.validate_date_format),
            inquirer.Text('number_of_turns',
                          message="How many turns ? "
                                  "Default 8, min 1 - max 99",
                          default=8,
                          validate=validate_number_of_turns),
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

        if not tournaments:
            return None

        select = [
            inquirer.List('selected_tournament',
                          message='Choose a tournament',
                          choices=tournaments_list)]
        response = inquirer.prompt(select)
        return response['selected_tournament']

    @classmethod
    def manage_tournament_action(cls, current_tournament: Tournament):

        cls.clear()
        print("--------------------------")
        print(f"Current tournament : {current_tournament.name}")
        print("Current turn : " + str(len(current_tournament.turns_list)+1))
        if len(current_tournament.players) >= int(current_tournament.number_of_turns)*2-1:
            print("Current players : ")
            for player in current_tournament.players:
                PlayerView.simple_player_description(player)
        else:
            print("Add players before compute the first turn")
        if current_tournament.ongoing_turn is not None:
            MatchView.show_matches(current_tournament.ongoing_turn.matches)
        print("--------------------------")

        def get_choices(tournament: Tournament):
            choices = []
            if len(tournament.turns_list)+1 <= int(tournament.number_of_turns):
                if len(tournament.turns_list) == 0 and \
                        tournament.ongoing_turn is None:
                    choices.append('Add new player')
                    choices.append('Add existing player')
                if len(tournament.players) >= \
                        int(current_tournament.number_of_turns)*2-1 \
                        and tournament.ongoing_turn is None and\
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

    @staticmethod
    def view_list(the_list):
        # Load the data in a data frame object
        tournament_list = pd.DataFrame(the_list)
        tournament_list = tournament_list[["name", "description",
                                           "start_date", "end_date"]]

        return print(tournament_list)

    @classmethod
    def choose_active_tournament_turn(cls, current_tournament):
        choices = []
        for turn in current_tournament.turns_list:
            choices.append(turn.name)
        pass

        question = [
            inquirer.List('turn',
                          choices=choices,
                          message="Choose a turn")
        ]

        turn = inquirer.prompt(question)

        return turn['turn']
