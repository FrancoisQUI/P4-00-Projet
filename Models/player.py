from person import Person


class Player(Person):
    def __init__(self, player_data=None):
        super().__init__()
        if player_data is not None:
            self.first_name = player_data['first_name']
            self.name = player_data['name']
            self.birthdate = player_data['birthdate']
            self.gender = player_data['gender']
            self.rank = player_data['rank']
