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
    def select_main_action():
        print("WIP")

    @staticmethod
    def view_list(the_list):
        # Load the data in a data frame object
        df = pd.DataFrame(the_list)
        return print(df)

    @staticmethod
    def wait_user_action():
        input("press a key to continue")
