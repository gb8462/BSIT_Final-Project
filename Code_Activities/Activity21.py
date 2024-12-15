def act21():
    tuloy = True
    nameno = 0
    while tuloy == True:
        name = input("Enter a name: ")
        

        if name.lower()=="stop":
            print("Okay tama na\n")
            print(f"You have entered a total of {nameno} names!")
            break

        else:
            print("type 'stop' if you want to terminate the program\n")
            nameno += 1
            continue
