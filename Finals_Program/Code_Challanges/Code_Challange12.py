def Code12():
    for i in range(0, 10):
        for j in range(10, i, -1):
            print(" ", end="")
        for k in range(i + 1):
            print("*", end=" ")
        print()

    for a in range(7):
        print("       * * * *")