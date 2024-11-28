import os

def clean():
    os.system('cls')
def personal_project():
    print("\n==================================")
    print("===== No Personal Project yet=====")
    print("==================================\n")
    input("Please Press enter to exit ")
    clean()

def School_Activities():
    print("\n===================================")
    print("===== No School Activities yet=====")
    print("===================================\n")
    input("Please Press enter to exit ")
    clean()

def Code_challanges():
    print("\n================================")
    print("===== No Code Challange yet=====")
    print("================================\n")
    input("Please Press enter to exit ")
    clean()

def main():
    while True:
        print("=============================")
        print("===== Compiled Projects =====")
        print("=============================")
        print("[0]. Clear Terminal")
        print("[1]. Personal Projects")
        print("[2]. School Activities")
        print("[3]. School Code Challanges")
        print("=============================")
        usr = input("please enter a number from [0-3] : ")
        if usr == "0":
            clean()
        elif usr == "1":
            personal_project()
        elif usr == "2":
            School_Activities()
        elif usr == "3":
            Code_challanges()
        else:
            print("INVALID INPUT! EXITING!")
            exit()

main()
