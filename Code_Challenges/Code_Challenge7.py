def Code7():
    user = input("Please Enter your name: ")
    age = eval(input("Please Enter your age: "))
    money = 500
    while True:
        print("================================================================================")
        print("             ITEMS: (1).Hotdog (2).Chicken (3).Beef (4).Milk")
        print("================================================================================")
        print(f"Your money is: {money}")
        print("\nChoices (1-4)")
        print("\nType [exit] to exit program")
        choice = input("Please choose which item you would like to buy: ")

        if choice == "1":
            num1 = input("Hotdog costs 50. Would you like to buy it? (yes/no): ")
            if num1.lower() == "yes":
                if age >= 60:
                    print("Congrats! You received a discount!")
                    money += 20
                money -= 50 
                print(f"Remaining balance: {money}")
                print(f"\nThank you for your purchase, {user}!")
            elif num1.lower() == "no":
                print("Thank you for visiting.")
            else:
                print("Invalid input.")
        elif choice == "2":
            num2 = input("Chicken costs 100. Would you like to buy it? (yes/no): ")
            if num2.lower() == "yes":
                if age >= 60:
                    print("Congrats! You received a discount!")
                    money += 20
                money -= 100
                print(f"Remaining balance: {money}")
                print(f"\nThank you for your purchase, {user}!")
            elif num2.lower() == "no":
                print("Thank you for visiting.")
            else:
                print("Invalid input.")
        elif choice == "3":
            num3 = input("Beef costs 200. Would you like to buy it? (yes/no): ")
            if num3.lower() == "yes":
                if age >= 60:
                    print("Congrats! You received a discount!")
                    money += 20
                money -= 200
                print(f"Remaining balance: {money}")
                print(f"\nThank you for your purchase, {user}!")
            elif num3.lower() == "no":
                print("Thank you for visiting.")
            else:
                print("Invalid input.")
        elif choice == "4":
            num4 = input("Milk costs 30. Would you like to buy it? (yes/no): ")
            if num4.lower() == "yes":
                if age >= 60:
                    print("Congrats! You received a discount!")
                    money += 20
                money -= 30
                print(f"Remaining balance: {money}")
                print(f"\nThank you for your purchase, {user}!")
            elif num4.lower() == "no":
                print("Thank you for visiting.")
            else:
                print("Invalid input.")
        elif choice.lower() == "exit":
            print(f"Goodbye, {user}! Your remaining balance is {money}.")
            break
        else:
            print("Invalid choice. Please choose a valid option.")