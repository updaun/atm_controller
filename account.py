import sys
from password import pwinput
from mode import confirm_question
from validate import PinNumberFormatValidator, CardNumberFormatValidator


class UserAccount:

    """Account Object Definition"""

    def __init__(self, id, user_id, pin_number=None, balance=0):
        self.id = id
        self.user_id = user_id
        self.pin_number = pin_number
        self.balance = balance

    def set_pin_number(self, pin_number):
        validator = PinNumberFormatValidator()
        if validator.is_vaild(pin_number):
            self.pin_number = pin_number

    def get_balance(self):
        return self.balance

    def deposit(self):
        amount = input("Please enter the amount you want to deposit.(dollar)\n=> ")
        if not amount.isdigit():
            print("Please insert digits only.")
            return self.deposit()
        if int(amount) <= 0:
            print(f"{amount} Unable to deposit. Please insert amount upper than zero.")
            return self.deposit()
        self.balance += int(amount)
        print("You have been successfully deposited.")
        print("The balance after deposit is\n")
        print(f"{self.balance} dollar")

    def withdraw(self):
        amount = input("Please enter the amount you want to withdraw.(dollar)\n=> ")
        if not amount.isdigit():
            print("Please insert digits only.")
            return self.withdraw()
        if int(amount) <= 0:
            print(f"{amount} Unable to withdraw. Please insert amount upper than zero.")
            return self.withdraw()
        if int(amount) > self.balance:
            print("\nAccount balance is insufficient.")
            print(f"The withdrawable amount is {self.balance} dollar\n")
            return self.withdraw()
        self.balance -= int(amount)
        print("You have been successfully withdrawn.")
        print("The balance after withdrawal is\n")
        print(f"{self.balance} dollar")

    def __str__(self):
        id_index = len(self.user_id)
        return self.user_id[:4] + "*" * (id_index - 4)


def make_new_card_number(db):
    validator = CardNumberFormatValidator()
    validator.notice()
    input_card_number = input("\nPlease Make new CARD number : ")
    if not db.check_unique(input_card_number):
        return make_new_card_number(db)
    if validator.is_vaild(input_card_number):
        confirm = confirm_question("Do you confirm card number?")
        if confirm is None:
            return None
        if not confirm:
            return make_new_card_number(db)
        return input_card_number
    else:
        if input_card_number.lower() == "exit":
            return None
        return make_new_card_number(db)


def make_new_pin_number():
    validator = PinNumberFormatValidator()
    validator.notice()
    input_pin_number = pwinput(
        prompt="\nPlease Make new PIN number. If you want to exit, Please Enter [exit]\n=> ",
        mask="*",
    )
    if validator.is_vaild(input_pin_number):
        confirm_pin_number = pwinput(
            prompt="Please Confirm PIN number. If you want to exit, Please Enter [exit]\n=> ",
            mask="*",
        )
        if input_pin_number != confirm_pin_number:
            print("The password you entered does not match.\n")
            make_new_pin_number()
        else:
            print("PIN Number set Successfully.")
            return confirm_pin_number
    else:
        if input_pin_number.lower() == "exit":
            return None
        make_new_pin_number()


def create_account(db):
    db_index = len(db)
    card_id = make_new_card_number(db)
    if card_id is None:
        return None
    set_pin_number = make_new_pin_number()
    if set_pin_number is None:
        return None
    account = UserAccount(id=db_index + 1, user_id=card_id, pin_number=set_pin_number)
    return account


def get_user(db, card_id):
    for data in db:
        if data.user_id == card_id:
            return data
    else:
        print("This is a missing number.")
        return None


def check_pin_number(user):
    print("\nStart Authentication.")
    pin_number = pwinput(
        prompt="\nPlease Enter your PIN number. If you want to exit, Please Enter [exit]\n=> ",
        mask="*",
    )
    if pin_number.lower() == "exit":
        return None
    if pin_number == user.pin_number:
        print("\nAuthentication Success")
        return True
    else:
        print("\nPIN Number Error - Authentication failed")
        return False
