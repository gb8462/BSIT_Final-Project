def act17():
   elu = int(input("Enter a number: "))
   for x in range(1,11):
        for y in range(1, elu + 1):
            print(f"{x} x {y} = {x*y}", end="\t")
        print()