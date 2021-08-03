from os import system, name
from abc import ABC
import re
import pandas as pd
from inquirer import errors


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
        input("press \"enter\" to continue")

    @staticmethod
    def validate_date_format(answer, current):
        if not re.match(
                "^(19[0-9]{2}|2[0-9]{3})-"
                "(0[1-9]|1[012])-"
                "([123]0|[012][1-9]|31)$",
                current):
            raise errors.ValidationError('',
                                         reason='Not valid format! '
                                                'example : 1982-05-28')
        return True

    @staticmethod
    def validate_rank_format(answer, current):
        if not re.match("^[0-9]{1,4}$", current):
            raise errors.ValidationError('',
                                         reason='Number between 1 to 9999')
        return True
