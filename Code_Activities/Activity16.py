def act16():
    for x in range(1, 6):
        for y in range(1, x + 1):
            print("  ",end="")
        for z in range(6, y, -1):
            print("^ ",end="")
        for a in range(6, x, -1):
            print("* ",end="")
        for b in range(1, x + 1):
            print(" ",end="")
        print("\n")
    print()