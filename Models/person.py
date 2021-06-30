from datetime import datetime

from model import Model


class Person(Model):
    """ Represent a person """
    def __init__(self, first_name: str, name: str, birthdate: datetime, gender: str):
        super().__init__()
        self.first_name = first_name
        self.name = name
        self.birthdate = birthdate
        self.genre = gender
