def card_number_filter(number):
    filtered_number = number[:4]
    filtered_number += "*" * (len(number) - 8)
    filtered_number += number[-4:]
    return filtered_number
