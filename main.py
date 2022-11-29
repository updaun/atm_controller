from card import insert_card
from account import check_pin_number
from database import Database
import time


def main():

    db = Database()

    data = db.load_database()

    # welcome
    print("\nHello, Nice to meet you! Welcome to our ATM Service.")

    # Insert Card
    card_id = insert_card(db)
    if card_id is None:
        main()
        return None
    user = db.get_user_from_id(card_id)

    # Check PIN number
    auth_check = check_pin_number(user)

    if auth_check is None:
        main()
        return None

    if auth_check:
        # See Balance/Deposit/Withdraw
        while True:
            mode = input(
                "\nPlease select the service you want.\n1. Check Balance\t2. Deposit\n3. Withdraw\t\t4. Exit\n=> "
            )
            # Exit
            if mode == "4":
                break

            # Check Balance
            elif mode == "1":
                print("The balance in your account is\n")
                print(f"{user.get_balance()} dollar")

            # Deposit
            elif mode == "2":
                user.deposit()
                db.save()

            # Withdraw
            elif mode == "3":
                user.withdraw()
                db.save()

    else:
        print("Due to PIN Number error, Move to Main Screen.")
        print("3", sep="")
        time.sleep(1)
        print("2", sep="")
        time.sleep(1)
        print("1", sep="")
        time.sleep(1)
        print()
        main()

    # Exit Programs
    print("*" * 80)
    print("\nThank you for using our service.\nPlease receive your card.\n")
    print("*" * 80)
    main()


if __name__ == "__main__":
    main()
