from datetime import datetime


class Person:
    """ Represent a person """

    def __init__(self,
                 first_name: str,
                 name: str,
                 birthdate: datetime,
                 gender: str):
        self.first_name = first_name
        self.name = name
        self.birthdate = birthdate
        self.genre = gender
