import inquirer

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
