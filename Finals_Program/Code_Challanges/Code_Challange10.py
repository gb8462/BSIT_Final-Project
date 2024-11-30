def code10():
    for r in range(1,7):
        for i in range(7,r, -1):
            print(" ",end="")
        for j in range(0, r):
            print("*", end="")
        for k in range(r,7, -1):
            print("*", end="")
        for l in range(0,r):
            print("*", end="")
        print()

    for t in range(1,7):
        for x in range(1,t + 1):
            print(" ", end="")
        for y in range(7,t, -1):
            print("*", end="")
        for y in range(7,t, -1):
            print("*", end="")    
        print()
