
import os
# BANK SIMULATION PROGRAM
# Create new account
# if account exists, deposit, withdraw, check balance -- function
# if deposit, enter amount, give Filipino denomination breakdown
# if withdraw, you cannot withdraw if balance is lower than withdraw amount
# deposit, ask how much? and show current balance
# continue to repeat the process until user opts out or exits the program, use while loop
# you will create a function that will break down a Filipino denomination and then print it
# Create a Python program that can create banking accounts, with the following information:
# initial deposit, name
# user can also deposit, withdraw, and every deposit program should be able to display the current balance
# program will only terminate if user choose to terminate the program

def clean():
    os.system('clear')

def Code16():
    denominations = [1000, 500, 200, 100, 50, 20, 10, 5, 1]

    accounts = {}

    def create_account(name, initial_deposit):
        if name in accounts:
            print(f"Account with name '{name}' already exists.")
        else:
            accounts[name] = initial_deposit
            print(f"Account created for '{name}' with an initial deposit of PHP {initial_deposit}.")

    def check_balance(name):
        if name in accounts:
            print(f"Current balance for '{name}': PHP {accounts[name]}")
        else:
            print("Account does not exist.")

    def denomination_breakdown(amount):
        print("Denomination breakdown:")
        for denom in denominations:
            count = amount // denom
            if count > 0:
                print(f"{denom} x {count}")
            amount %= denom

    def deposit(name, amount):
        if name in accounts:
            accounts[name] += amount
            print(f"Deposited PHP {amount} to '{name}'. New balance: PHP {accounts[name]}")
            denomination_breakdown(amount)
        else:
            print("Account does not exist.")

    def withdraw(name, amount):
        if name in accounts:
            if accounts[name] >= amount:
                accounts[name] -= amount
                print(f"Withdrew PHP {amount} from '{name}'. New balance: PHP {accounts[name]}")
            else:
                print("Insufficient balance!")
        else:
            print("Account does not exist.")

    def main():
        while True:
            print("\n--- BANK SIMULATION PROGRAM ---")
            print("1. Create Account")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Check Balance")
            print("5. Exit Program")

            choice = input("Choose an option: ")
            clean()

            if choice == "1":
                name = input("Enter account name: ")
                initial_deposit = eval(input("Enter initial deposit: "))
                clean()
                create_account(name, initial_deposit)
            elif choice == "2":
                name = input("Enter account name: ")
                amount = eval(input("Enter amount to deposit: "))
                clean()
                deposit(name, amount)
            elif choice == "3":
                name = input("Enter account name: ")
                amount = eval(input("Enter amount to withdraw: "))
                clean()
                withdraw(name, amount)
            elif choice == "4":
                name = input("Enter account name: ")
                clean()
                check_balance(name)
            elif choice == "5":
                print("Thank you for using the Bank Simulation Program. Goodbye!")
                clean()
                break
            else:
                print("Invalid choice. Please try again.")
    main()