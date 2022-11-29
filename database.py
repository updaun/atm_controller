import os
import pickle
from config import *


class Database:
    def __init__(self):
        self.db = []

    def load_database(self):
        if os.path.exists("db.pickle"):
            with open(DATABASE["DATABASE_DIR"], "rb") as f:
                self.db = pickle.load(f)
        else:
            with open(DATABASE["DATABASE_DIR"], "wb") as f:
                pickle.dump(self.db, f)
        return self.db

    def save(self):
        with open(DATABASE["DATABASE_DIR"], "wb") as f:
            pickle.dump(self.db, f)

    def __len__(self):
        return len(self.db)


# db = Database()
# data = db.load_database()
# print(data)
