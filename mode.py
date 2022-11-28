def select_mode():

    mode = input("\nDo you own an account?(Y / N)\n=> ")

    if mode == "y" or mode == "Y":
        return True
    elif mode == "n" or mode == "N":
        return False
    else:
        print("[Warning] Please choose Y or N.")
        select_mode()
