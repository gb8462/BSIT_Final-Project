def act7():
    miner = input("Enter you name: ")
    mined = input("Did you mine gold today (yes/no) : ")
    gold = 0
    if mined.lower() == "yes":
        gold += 1
        print(f" Your total mined today is {gold} gold\n")
    elif mined.lower() == "no":
        print(f" You havent mined a gold today\n")
    else:
        print("Invalid error\n")
