from datetime import datetime


class Tournament:
    def __init__(self,
                 name: str,
                 place: str,
                 start_date: datetime,
                 end_date: datetime,
                 turns_list: dict,
                 time_control: str,
                 description: str,
                 players=None,
                 number_of_turns=8):

        if players is None:
            self.players = []
        else:
            self.players = players

        self.name = name
        self.place = place
        self.start_date = start_date
        self.end_date = end_date
        self.number_of_turns = number_of_turns
        self.turns_list = turns_list
        self.time_control = time_control
        self.description = description
