def confirm_question(message):
    confirm = input(f"\n{message} (Y/N)\n=> ").lower()

    if confirm == "exit":
        return None

    if confirm == "y" or confirm == "yes":
        return True
    elif confirm == "n" or confirm == "no":
        return False
    else:
        print("\nPlease choose Y or N.")
        return confirm_question(message)
