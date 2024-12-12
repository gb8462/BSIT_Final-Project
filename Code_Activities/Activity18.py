def act18():
    ragud = int(input("Enter a number: "))
    for a in range(1,5):
        for x in range(1,ragud +1 ):
            for y in range(1, a + 1):
                print("*", end= " ")

            for z in range(5, a, -1):
                print(" ", end=" ")
        print()