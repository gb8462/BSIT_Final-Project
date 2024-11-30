import os

from Code_Challanges import Code_Challange1
from Code_Challanges import Code_Challange2
from Code_Challanges import Code_Challange3
from Code_Challanges import Code_Challange4
from Code_Challanges import Code_Challange5
from Code_Challanges import Code_Challange6
from Code_Challanges import Code_Challange7
from Code_Challanges import Code_Challange8
from Code_Challanges import Code_Challange9
from Code_Challanges import Code_Challange10
from Code_Challanges import Code_Challange11
from Code_Challanges import Code_Challange12
from Code_Challanges import Code_Challange13
from Code_Challanges import Code_Challange14
from Code_Challanges import Code_Challange15
from Code_Challanges import Code_Challange16

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
        print("[6]. Code Challange 6")
        print("[7]. Code Challange 7")
        print("[8]. Code Challange 8")
        print("[9]. Code Challange 9")
        print("[10]. Code Challange 10")
        print("[11]. Code Challange 11")
        print("[12]. Code Challange 12")
        print("[13]. Code Challange 13")
        print("[14]. Code Challange 14")
        print("[15]. Code Challange 15")
        print("[16]. Code Challange 16")
        print("=============================")
    
    while True:        
        usr = input("please type menu to view [menu] : ")
        clean()
        
        if usr == "1":
            print("OUTPUT: \n")
            Code_Challange1.Code1()

        elif usr == "2":
            print("OUTPUT: \n")
            Code_Challange2.Code2()

        elif usr == "3":
            print("OUTPUT: \n")
            Code_Challange3.Code3()
        
        elif usr == "4":
            print("OUTPUT: \n")
            Code_Challange4.Code4()
        
        elif usr == "5":
            print("OUTPUT: \n")
            Code_Challange5.Code5()

        elif usr == "6":
            print("OUTPUT: \n")
            Code_Challange6.Code6()

        elif usr == "7":
            print("OUTPUT: \n")
            Code_Challange7.Code7()
        
        elif usr == "8":
            print("OUTPUT: \n")
            Code_Challange8.Code8()
        
        elif usr == "9":
            print("OUTPUT: \n")
            Code_Challange9.Code9()

        elif usr == "10":
            print("OUTPUT: \n")
            Code_Challange10.Code10()
        
        elif usr == "11":
            print("OUTPUT: \n")
            Code_Challange11.Code11()
        
        elif usr == "12":
            print("OUTPUT: \n")
            Code_Challange12.Code12()
        
        elif usr == "13":
            print("OUTPUT: \n")
            Code_Challange13.Code13()
        
        elif usr == "14":
            print("OUTPUT: \n")
            Code_Challange14.Code14()
        
        elif usr == "15":
            print("OUTPUT: \n")
            Code_Challange15.Code15()

        elif usr == "16":
            print("OUTPUT: \n")
            Code_Challange16.Code16()

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
        print("[1]. School Code Challanges")
        print("[2]. School Activities")
        print("[3]. Personal Projects")
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