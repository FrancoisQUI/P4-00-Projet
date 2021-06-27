from Database import Database


class Model:
    def __init__(self):
        pass

    def save(self):
        db = Database()
        db.insert(self.__dict__)
