from tinydb import TinyDB, Query, queries
from Core.variables_settings import DATABASE_FILENAME


class Database:
    def __init__(self):
        self.db = TinyDB(DATABASE_FILENAME)

    def insert(self, data):
        insert = self.db.insert(data)
        return insert
