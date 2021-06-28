from pprint import pprint

from tinydb import TinyDB
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
        return TinyDB(DATABASE_FILENAME, sort_keys=True, indent=4, separators=(',', ': '))

    def save_new(self):
        db = self.set_db()
        table = db.table(self._table_name)
        table.insert(self.__dict__)
