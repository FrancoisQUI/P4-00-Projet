from person import Person


class Player(Person):
    def __init__(self, first_name, name, birthdate, gender, rank: int):
        super().__init__(first_name, name, birthdate, gender)
        self.rank = rank
