def act19():
    while True:
        name = input("Are You Happy? (yes/ no): ")
        if name.lower() == "yes":
            print("I See Good For you!")
            break
        elif name.lower() == "no":
            print("Okay Comeback when your happy\n")
            break
        else:
            print("Invalid input exiting")
            break