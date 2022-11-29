from config import *
from database import Database


class PinNumberFormatValidator:
    def notice(self):
        print(f"\nPlease make PIN NUMBER {PIN_NUMBER_LENGTH} digits.")

    def is_vaild(self, pin_number):
        if not pin_number.isdigit():
            print("Please enter numbers only.")
            return False
        if len(pin_number) != PIN_NUMBER_LENGTH:
            self.notice()
            return False
        return True


class CardNumberFormatValidator:
    def notice(self):
        print(
            f"\nPlease make CARD NUMBER a minimum of {MIN_CARD_NUMBER_LENGTH} digits. (Recommand - Your Phone Number)"
        )

    def is_vaild(self, card_number):
        if not card_number.isdigit():
            print("Please enter numbers only.")
            return False
        if len(card_number) < MIN_CARD_NUMBER_LENGTH:
            self.notice()
            return False

        db = Database()
        data = db.load_database()
        for user in data:
            if user.user_id == card_number:
                print("It's already a registered.")
                return False

        return True
