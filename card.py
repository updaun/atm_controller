from config import *


def insert_card(db):
    result = input(
        "\nPlease Insert your cards, Or Enter your card number.\nPress ENTER => "
    )
    if result == "":
        select_id = db.get_card_list()
        return select_id

    return None
