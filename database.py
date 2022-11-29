import os
import pickle
from config import *
from utils import card_number_filter
from account import create_account


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

    def get_card_list(self):
        print()
        if len(self.db) > 0:
            for idx, data in enumerate(self.db):
                filtered_data = card_number_filter(data.user_id)
                print(f"{idx+1}. {filtered_data}")
            select_index = input("\nChoose Your card\n=> ")
            if int(select_index) < 1:
                print("Please insert number upper then 1.")
                self.get_card_list()
            if not select_index.isdigit():
                print("Please insert number only")
                self.get_card_list()
            if int(select_index) <= len(self.db):
                return self.db[int(select_index) - 1].user_id
            else:
                return None
        else:
            print("There is no registered account.\nPlease make your account.")
            user = create_account(len(self.db))
            self.db.append(user)
            self.save()

    def get_user_from_id(self, card_id):

        for data in self.db:
            if data.user_id == card_id:
                return data
        else:
            print("Could not find your Account.")
            return None

    def save(self):
        with open(DATABASE["DATABASE_DIR"], "wb") as f:
            pickle.dump(self.db, f)

    def __len__(self):
        return len(self.db)


db = Database()
data = db.load_database()
print(data)
