def Code13():
    for r in range(1, 8):
        for i in range(8, r, -1):
            print(" ", end="")
        for j in range(r - 1, 1, -1):
            print(j, end="")
        for k in range(1, r):
            print(k, end="")
        print()

    for t in range(6, 1, -1):
        for x in range(8, t, -1):
            print(" ", end="")
        for y in range(t - 1, 1, -1):
            print(y, end="")
        for z in range(1, t):
            print(z, end="")
        print()