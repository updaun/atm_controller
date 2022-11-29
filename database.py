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
            card = input("\nChoose Your card(index or card number)\n=> ")
            if len(card) >= MIN_CARD_NUMBER_LENGTH:
                if self.check_user_id(card):
                    return card
                else:
                    return self.get_card_list()
            if int(card) < 1:
                print("Please insert number upper then 1.")
                return self.get_card_list()
            if not card.isdigit():
                print("Please insert number only")
                return self.get_card_list()
            if int(card) <= len(self.db):
                return self.db[int(card) - 1].user_id
            else:
                return None
        else:
            print("There is no registered account.\nPlease make your account.")
            user = create_account(len(self.db))
            self.db.append(user)
            self.save()

    def check_user_id(self, card_id):
        for data in self.db:
            if data.user_id == card_id:
                return True
        else:
            return False

    def get_user_from_id(self, card_id):
        for data in self.db:
            if data.user_id == card_id:
                return data
        else:
            print("Could not find your Account.")
            return None

    def check_unique(self, card_number):
        for user in self.db:
            if user.user_id == card_number:
                print("It's already a registered.")
                return False
        else:
            return True

    def save(self):
        with open(DATABASE["DATABASE_DIR"], "wb") as f:
            pickle.dump(self.db, f)

    def __len__(self):
        return len(self.db)
