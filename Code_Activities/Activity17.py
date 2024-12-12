def act17():
   ragud = int(input("Enter a number: "))
   for x in range(1,11):
        for y in range(1, ragud + 1):
            print(f"{x} x {y} = {x*y}", end="\t")
        print()