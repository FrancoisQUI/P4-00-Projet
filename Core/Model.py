from pprint import pprint

from tinydb import TinyDB, Query, where

import Tournament
from variables_settings import DATABASE_FILENAME


class Model:
    def __init__(self):
        self._table_name = self.set_table_name()

    def set_table_name(self):
        table_name = str(type(self))
        table_name = table_name[:-2]
        table_name = table_name[8:]
        table_name = table_name.replace("Models.", "")
        return table_name

    @staticmethod
    def set_db():
        return TinyDB(DATABASE_FILENAME, sort_keys=True, indent=2, separators=(',', ': '))

    def set_table(self, db):
        table = db.table(self._table_name)
        return table

    def set_db_and_table(self):
        db = self.set_db()
        table = self.set_table(db)
        return table

    def save_new(self):
        table = self.set_db_and_table()
        table.insert(self.__dict__)

    def get_list(self):
        table = self.set_db_and_table()
        all_data = table.all()
        return all_data

    def find_one_by_name(self, the_name):
        db = self.set_db()
        result = db.search(where("name") == the_name)
        return result
