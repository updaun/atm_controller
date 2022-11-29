def confirm_question(message):
    confirm = input(f"\n{message} (Y/N)\n=> ")

    if confirm == "y" or confirm == "Y":
        return True
    elif confirm == "n" or confirm == "N":
        return False
    else:
        print("\nPlease choose Y or N.")
        confirm_question(message)
