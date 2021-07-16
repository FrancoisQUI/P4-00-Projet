
from pprint import pprint

from tinydb import TinyDB, where

from variables_settings import DATABASE_FILENAME


class Model:
    _table_name = None

    @classmethod
    def get_db(cls):
        return TinyDB(DATABASE_FILENAME,
                      sort_keys=True,
                      indent=2,
                      separators=(',', ': '))

    @classmethod
    def get_table(cls):
        db = cls.get_db()
        table = db.table(cls._table_name)
        return table

    def save_new(self):
        table = self.get_table()
        table.insert(self.__dict__)

    def save_unique(self):
        table = self.get_table()
        table.truncate()
        table.insert(self.__dict__)

    def update(self):
        table = self.get_table()
        obj_to_update = table.get(where("name") == self.__dict__["name"])
        table.update(self.__dict__,
                     doc_ids=[obj_to_update.doc_id])

    def get_id(self):
        table = self.get_table()
        _object = table.get(where("name") == self.__dict__["name"])
        print("get_id() object")
        pprint(_object)
        return _object.doc_id

    @classmethod
    def get_list(cls):
        table = cls.get_table()
        all_data = table.all()
        return all_data

    @classmethod
    def find_one_by_name(cls, the_name):
        table = cls.get_table()
        result = table.get(where("name") == the_name)
        return result
