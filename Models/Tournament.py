class Tournament:
    def __init__(self,
                 name,
                 place,
                 start_date,
                 end_date,
                 number_of_turns,
                 turns_list,
                 players,
                 time_control,
                 description):
        self.name = name
        self.place = place
        self.start_date = start_date
        self.end_date = end_date
        self.number_of_turns = number_of_turns
        self.turns_list = turns_list
        self.players = players
        self.time_control = time_control
        self.description = description
