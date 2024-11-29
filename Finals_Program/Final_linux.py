import os

from Code_Challanges import (Code_Challange1,Code_Challange2,Code_Challange3,Code_Challange4,Code_Challange5)

def clean():
    os.system('clear')

def Code_challanges():
    print("\n=================================")
    print("======== Code Challanges ========")
    print("=================================\n")
    
    def menu():
        print("==============================")
        print("============ Menu ============")
        print("==============================\n")
        print("[exit]. Exit Code Challanges")
        print("[menu]. Code Challanges Menu\n")
        print("Please Enter the number of your Choices")
        print("=============================")
        print("[1]. Code Challange 1")
        print("[2]. Code Challange 2")
        print("[3]. Code Challange 3")
        print("[4]. Code Challange 4")
        print("[5]. Code Challange 5")
        print("=============================")
    
    while True:        
        usr = input("please type menu to view [menu] : ")
        clean()
        
        if usr == "1":
            print("OUTPUT: \n")
            Code_Challange1.Code_one()

        elif usr == "2":
            print("OUTPUT: \n")
            Code_Challange2.Code_two()

        elif usr == "3":
            print("OUTPUT: \n")
            Code_Challange3.Code_three()
        
        elif usr == "4":
            print("OUTPUT: \n")
            Code_Challange4.Code_four()
        
        elif usr == "5":
            print("OUTPUT: \n")
            Code_Challange5.Code_five()

        elif usr.lower() == "menu":
            menu()
        
        elif usr.lower() == "exit":
            return
        
        else:
            print("INVALID INPUT!")

def School_Activities():
    print("\n===================================")
    print("===== No School Activities yet=====")
    print("===================================\n")
    input("Please Press enter to exit ")
    clean()

def personal_project():
    print("\n==================================")
    print("===== No Personal Project yet=====")
    print("==================================\n")
    input("Please Press enter to exit ")
    clean()

def main():
    while True:
        print("=============================")
        print("===== Compiled Projects =====")
        print("=============================")
        print("[1]. Personal Projects")
        print("[2]. School Activities")
        print("[3]. School Code Challanges")
        print("=============================\n")
        usr = input("please enter a number from [1-3] : ")
        clean()
        if usr == "1":
            Code_challanges()
        elif usr == "2":
            School_Activities()
        elif usr == "3":
            personal_project()
        else:
            print("INVALID INPUT! EXITING!")
            exit()
main()