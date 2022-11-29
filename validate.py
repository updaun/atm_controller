from config import *


class PinNumberFormatValidator:
    def notice(self):
        print(f"\nPlease make PIN NUMBER {PIN_NUMBER_LENGTH} digits.")

    def is_vaild(self, pin_number):
        if pin_number.lower() == "exit":
            return False
        else:
            if not pin_number.isdigit():
                print("*" * 80)
                print("\nPlease enter numbers only.\n")
                print("*" * 80)
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
        if card_number.lower() == "exit":
            return False
        else:
            if not card_number.isdigit():
                print("*" * 80)
                print("\nPlease enter numbers only.\n")
                print("*" * 80)
                return False
            if len(card_number) < MIN_CARD_NUMBER_LENGTH:
                self.notice()
                return False
            return True
