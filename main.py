from mode import confirm_question
from card import insert_card
from account import create_account
from database import Database


def main():

    db = Database()

    data = db.load_database()

    # welcome
    print("Hello, Nice to meet you!")

    # select mode
    mode = confirm_question("Do you own an account?")

    if mode:
        # Insert Card
        card_id = insert_card(db)
        user = db.get_user_from_id(card_id)
        if user is None:
            card_id = insert_card(db)
            user = db.get_user_from_id(card_id)
    else:
        user = create_account(len(db))
        data.append(user)
        db.save()

    # PIN number

    # Select Account

    # See Balance/Deposit/Withdraw

    # Exit Programs
    print("Thank you for using our service.")


if __name__ == "__main__":
    main()
