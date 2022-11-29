from pwinput import pwinput
from mode import confirm_question
from validate import PinNumberFormatValidator, CardNumberFormatValidator


class UserAccount:

    """Account Object Definition"""

    def __init__(self, id, user_id, pin_number=None, balance=0):
        self.id = id
        self.user_id = user_id
        self.pin_number = pin_number
        self.balence = balance

    def get_balance(self):
        return self.balance

    def set_pin_number(self, pin_number):
        validator = PinNumberFormatValidator()
        if validator.is_vaild(pin_number):
            self.pin_number = pin_number

    def __str__(self):
        id_index = len(self.user_id)
        return self.user_id[:4] + "*" * (id_index - 4)


def make_new_card_number():
    validator = CardNumberFormatValidator()
    validator.notice()
    input_card_number = input("\nPlease Make new CARD number : ")
    if validator.is_vaild(input_card_number):
        confirm = confirm_question("Do you confirm card number?")
        if not confirm:
            make_new_card_number()
        return input_card_number
    else:
        make_new_pin_number()


def make_new_pin_number():
    validator = PinNumberFormatValidator()
    validator.notice()
    input_pin_number = pwinput(prompt="\nPlease Make new PIN number : ", mask="*")
    if validator.is_vaild(input_pin_number):
        confirm_pin_number = pwinput(prompt="Please Confirm PIN number : ", mask="*")
        if input_pin_number != confirm_pin_number:
            print("The password you entered does not match.\n")
            make_new_pin_number()
        else:
            print("PIN Number set Successfully.")
            return confirm_pin_number
    else:
        make_new_pin_number()


def create_account(db_index):

    card_id = make_new_card_number()

    set_pin_number = make_new_pin_number()

    account = UserAccount(id=db_index + 1, user_id=card_id, pin_number=set_pin_number)

    return account


def get_user(db, card_id):
    for data in db:
        if data.user_id == card_id:
            return data
    else:
        print("This is a missing number.")
        return None
