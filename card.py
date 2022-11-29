from account import create_account


def insert_card(db):
    card_id = input(
        "\nPlease Insert your cards, Or Enter your card number.\nIf you want to create NEW account, Please Insert [ Y ] key\nIf you want to account list, Press ENTER\n=> "
    )
    if card_id == "":
        select_id = db.get_card_list()
        return select_id
    if card_id.isdigit():
        if db.check_user_id(card_id):
            return card_id
        else:
            print("\nCard number does not exist.")
            return insert_card(db)
    else:
        print("*" * 80)
        print("\nStart creating NEW account.")
        print("If you exit creating account, Please Enter [exit]\n")
        print("*" * 80)
        user = create_account(db)
        if user is not None:
            data = db.load_database()
            data.append(user)
            db.save()
            print("*" * 80)
            print("\nNew account has been created successfully.\n")
            print("*" * 80)
            return user.user_id
        else:
            return None
