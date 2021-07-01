from pprint import pprint

from tinydb import TinyDB,  where

from variables_settings import DATABASE_FILENAME


class Model:
    _table_name = None

    @classmethod
    def get_db(cls):
        pprint(DATABASE_FILENAME)
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

    @classmethod
    def get_list(cls):
        table = cls.get_table()
        all_data = table.all()
        return all_data

    @classmethod
    def find_one_by_name(cls, the_name):
        table = cls.get_table()
        result = table.search(where("name") == the_name)
        return result
