import os

from Code_Challenges import (
    Code_Challenge1, Code_Challenge2, Code_Challenge3, Code_Challenge4,
    Code_Challenge5, Code_Challenge6, Code_Challenge7, Code_Challenge8,
    Code_Challenge9, Code_Challenge10, Code_Challenge11, Code_Challenge12,
    Code_Challenge13, Code_Challenge14, Code_Challenge15, Code_Challenge16
)
from Code_Activities import (
    Activity1, Activity2, Activity3, Activity4, Activity5, Activity6, Activity7, Activity8,
    Activity9, Activity10, Activity11, Activity12, Activity13, Activity14, Activity15, Activity16,
    Activity17, Activity18, Activity19, Activity20, Activity21, Activity22, Activity23, Activity24, Activity25
)

def clean():
    os.system('clear')

def main():
    while True:
        print("=============================")
        print("===== Compiled Projects =====")
        print("=============================")
        print("[0]. Exit Program")
        print("[1]. School Code Challanges")
        print("[2]. School Activities")
        print("[3]. Personal Projects")
        print("=============================\n")
        usr = input("please enter a number from [1-3] : ")
        clean()
        if usr == "1":
            Code_challenges()
        elif usr == "2":
            School_Activities()
        elif usr == "3":
            personal_project()
        elif usr == "0":
            print("Thank you for browsing my compiled programs")
            exit()
        else:
            print("INVALID INPUT! Try Again")

def Code_challenges():
    def menu():
        print("==================================================")
        print("====================== Menu ======================")
        print("==================================================")
        print("Please Enter the number of your choice")
        print("==========================================================")
        print("[1]. Code Challange 1 \t[11]. Code Challange 11")
        print("[2]. Code Challange 2 \t[12]. Code Challange 12")
        print("[3]. Code Challange 3 \t[13]. Code Challange 13")
        print("[4]. Code Challange 4 \t[14]. Code Challange 14")
        print("[5]. Code Challange 5 \t[15]. Code Challange 15")
        print("[6]. Code Challange 6 \t[16]. Code Challange 16")
        print("[7]. Code Challange 7")
        print("[8]. Code Challange 8")
        print("[9]. Code Challange 9")
        print("[10]. Code Challange 10")
        print("==========================================================")

    while True:        
        print("\n=================================")
        print("======== Code Challanges ========")
        print("=================================\n")
        print("[exit]. Exit Code Challanges")
        print("[menu]. Code Challanges Menu\n")
        usr = input("please type [menu] to view Choices : ")
        clean()
        
        if usr == "1":
            print("OUTPUT:")
            Code_Challenge1.Code1()

        elif usr == "2":
            print("OUTPUT:")
            Code_Challenge2.Code2()

        elif usr == "3":
            print("OUTPUT:")
            Code_Challenge3.Code3()
        
        elif usr == "4":
            print("OUTPUT:")
            Code_Challenge4.Code4()
        
        elif usr == "5":
            print("OUTPUT:")
            Code_Challenge5.Code5()

        elif usr == "6":
            print("OUTPUT:")
            Code_Challenge6.Code6()

        elif usr == "7":
            print("OUTPUT:")
            Code_Challenge7.Code7()
        
        elif usr == "8":
            print("OUTPUT:")
            Code_Challenge8.Code8()
        
        elif usr == "9":
            print("OUTPUT:")
            Code_Challenge9.Code9()

        elif usr == "10":
            print("OUTPUT:")
            Code_Challenge10.Code10()
        
        elif usr == "11":
            print("OUTPUT:")
            Code_Challenge11.Code11()
        
        elif usr == "12":
            print("OUTPUT:")
            Code_Challenge12.Code12()
        
        elif usr == "13":
            print("OUTPUT:")
            Code_Challenge13.Code13()
        
        elif usr == "14":
            print("OUTPUT:")
            Code_Challenge14.Code14()
        
        elif usr == "15":
            print("OUTPUT:")
            Code_Challenge15.Code15()

        elif usr == "16":
            print("OUTPUT:")
            Code_Challenge16.Code16()

        elif usr.lower() == "menu":
            menu()
        
        elif usr.lower() == "exit":
            return
        
        else:
            print("INVALID INPUT!")

def School_Activities():
    print("\n===================================")
    print("======== School Activities ========")
    print("===================================\n")
    def Menu():
        print("==================================================")
        print("====================== Menu ======================")
        print("==================================================")
        print("Please Enter the number of your choice")
        print("==========================================================")
        print("[1]. Activity 1 \t[14]. Activity 14")
        print("[2]. Activity 2 \t[15]. Activity 15")
        print("[3]. Activity 3 \t[16]. Activity 16")
        print("[4]. Activity 4 \t[17]. Activity 17")
        print("[5]. Activity 5 \t[18]. Activity 18")
        print("[6]. Activity 6 \t[19]. Activity 19")
        print("[7]. Activity 7 \t[20]. Activity 20")
        print("[8]. Activity 8 \t[21]. Activity 21")
        print("[9]. Activity 9 \t[22]. Activity 22")
        print("[10]. Activity 10 \t[23]. Activity 23")
        print("[11]. Activity 11 \t[24]. Activity 24")
        print("[12]. Activity 12 \t[25]. Activity 25")
        print("[13]. Activity 13")
        print("==========================================================")

    while True:
        print("\n=================================")
        print("========= Code Activities =========")
        print("===================================\n")
        print("[exit]. Exit Code Activities")
        print("[menu]. Code Activities Menu\n")
        usr = input("please type [menu] to view Choices : ")
        clean()

        if usr == "1":
            print("OUTPUT:")
            Activity1.act1()
        elif usr == "2":
            print("OUTPUT:")
            Activity2.act2()
        elif usr == "3":
            print("OUTPUT:")
            Activity3.act3()
        elif usr == "4":
            print("OUTPUT:")
            Activity4.act4()
        elif usr == "5":
            print("OUTPUT:")
            Activity5.act5()
        elif usr == "6":
            print("OUTPUT:")
            Activity6.act6()
        elif usr == "7":
            print("OUTPUT:")
            Activity7.act7()
        elif usr == "8":
            print("OUTPUT:")
            Activity8.act8()
        elif usr == "9":
            print("OUTPUT:")
            Activity9.act9()
        elif usr == "10":
            print("OUTPUT:")
            Activity10.act10()
        elif usr == "11":
            print("OUTPUT:")
            Activity11.act11()
        elif usr == "12":
            print("OUTPUT:")
            Activity12.act12()
        elif usr == "13":
            print("OUTPUT:")
            Activity13.act13()
        elif usr == "14":
            print("OUTPUT:")
            Activity14.act14()
        elif usr == "15":
            print("OUTPUT:")
            Activity15.act15()
        elif usr == "16":
            print("OUTPUT:")
            Activity16.act16()
        elif usr == "17":
            print("OUTPUT:")
            Activity17.act17()
        elif usr == "18":
            print("OUTPUT:")
            Activity18.act18()
        elif usr == "19":
            print("OUTPUT:")
            Activity19.act19()
        elif usr == "20":
            print("OUTPUT:")
            Activity20.act20()
        elif usr == "21":
            print("OUTPUT:")
            Activity21.act21()
        elif usr == "22":
            print("OUTPUT:")
            Activity22.act22()
        elif usr == "23":
            print("OUTPUT:")
            Activity23.act23()
        elif usr == "24":
            print("OUTPUT:")
            Activity24.act24()
        elif usr == "25":
            print("OUTPUT:")
            Activity25.act25()
        elif usr.lower() == "menu":
            Menu()
        elif usr.lower() == "exit":
            print("Exiting...")
            return
        else:
            print("INVALID INPUT!")

def personal_project():
    print("\n==================================")
    print("===== No Personal Project yet=====")
    print("==================================\n")
    input("Please Press enter to exit ")
    clean()

main()