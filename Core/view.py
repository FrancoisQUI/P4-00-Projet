from os import system, name
from abc import ABC

import pandas as pd


class View(ABC):
    def __init__(self):
        self.content = []
        self.clear()

    @staticmethod
    def clear():
        if name == "nt":
            clear = system('cls')
        else:
            clear = system('clear')
        return clear

    @staticmethod
    def wait_user_action():
        input("press a key to continue")

    @staticmethod
    def select_main_action():
        print("Le rendu de cette vue n'a pas encore été développé")

    @staticmethod
    def view_list(the_list):
        # Load the data in a data frame object
        df = pd.DataFrame(the_list)
        return print(df)
