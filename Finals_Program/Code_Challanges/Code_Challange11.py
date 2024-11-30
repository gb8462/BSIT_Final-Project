def code11():
    for r in range(1, 8):
        for i in range(8, r, -1):
            print(" ", end="")
        for j in range(1, r):
            print("*", end="")
        for k in range(0, r):
            print("*", end="")
        print()
    
    for t in range(0, 8):
        for x in range(1, t + 1):
            print(" ", end="")
        for y in range(t, 7):
            print("*", end="")
        for z in range(t, 8):
            print("*", end="")
        print()