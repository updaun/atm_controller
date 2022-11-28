from mode import select_mode


def main():

    # welcome
    print("Hello, Nice to meet you!")

    # select mode
    mode = select_mode()

    if mode:
        # Insert Card
        insert_card()

    # PIN number

    # Select Account

    # See Balance/Deposit/Withdraw

    # Exit Programs
    print("Thank you for using our service.")


if __name__ == "__main__":
    main()
