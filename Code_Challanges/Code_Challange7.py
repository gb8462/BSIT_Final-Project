def Code7():
    user = input("Please Enter your name: ")
    age = int(input("Please Enter your age: "))
    money = 500
    print("================================================================================")
    print("             ITEMS: (1).Hotdog (2).Chicken (3).Beef (4).Milk")
    print("================================================================================")
    
    print("your money is: ",money)
    print("choose from (1-4)")
    choice = input("Please choose which item would you like to buy: ")
    
    if choice == "1":
        num1 = input("Hotdog cost 50 would you like to buy it? (yes/no): ")
        if num1.lower() == "yes":
            if age >= 60:
                print("congrats you received a discount!")
                money += 20
            balance = money - 50
            print(balance)
            print(f"\nthank you for purchase {user}")
        elif num1 == "no":
            print("Thank you for visiting")
        else:
            print("Invalid input")
    elif choice == "2":
        num2 = input("Chcken Cost 100 would you like to buy it? (yes/no)")
        if num2.lower() == "yes":
            if age >= 60:
                print("congrats you received a discount!")
                money += 20
            balance = money - 100
            print(balance)
            print(f"\nthank you for purchase {user}")
        elif num2 == "no":
            print("Thank you for visiting")
        else:
            print("Invalid input")
    
    elif choice == "3":
        num3 = input("beef Cost 200 would you like to buy it? (yes/no)")
        if num3.lower() == "yes":
            if age >= 60:
                print("congrats you received a discount!")
                money += 20
            balance = money - 200
            print(balance)
            print(f"\nthank you for purchase {user}")
        elif num3 == "no":
            print("Thank you for visiting")    
        else:
            print("Invalid input")
    
    elif choice == "4":
        num4 = input("Milk Cost 30 would you like to buy it? (yes/no)")
        if num4.lower() == "yes":
            if age >= 60:
                print("congrats you received a discount!")
                money += 20
            balance = money - 30
            print(balance)
            print(f"\nthank you for purchase {user}")
        elif num4 == "no":
            print("Thank you for visiting")
        else:
            print("Invalid input")