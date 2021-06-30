import inquirer

from Core.view import View


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
    def select_tournament(tournaments):
        tournaments_list = []
        for tournament in tournaments:
            try:
                tournaments_list.append(tournament['name'])
            except KeyError:
                pass
        select = [inquirer.List('selected_tournament',
                                message='Choose a tournament',
                                choices=tournaments_list)]
        return inquirer.prompt(select)

    @staticmethod
    def manage_tournament_action(current_tournament):
        actions = [
            inquirer.List('Action',
                          choices=['Add player',
                                   'Compute First round'])
        ]

        return inquirer.prompt(actions)
