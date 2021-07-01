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
        response = inquirer.prompt(select)
        return response['selected_tournament']

    @classmethod
    def manage_tournament_action(cls, current_tournament):
        current_round = len(current_tournament['turns_list'])
        cls.clear()
        print("--------------------------")
        print("Current tournament : " +
              current_tournament['name'])
        if current_round > 0:
            print("Current Round : " +
                  str(current_round))
            # TODO: Show currents matches
        else:
            print("Add players before compute the first round")
        print("--------------------------")

        def get_choices(_current_round):
            choices = []
            if _current_round == 0:
                choices.append('Add player')
                choices.append('Compute first round')
            else:
                choices.append('Enter round scores')
                choices.append('Compute next round')
            choices.append('Go Back')
            return choices

        actions = [
            inquirer.List('Action',
                          choices=get_choices(current_round))]

        response = inquirer.prompt(actions)

        return response["Action"]
