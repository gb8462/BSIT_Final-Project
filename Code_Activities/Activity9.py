# Huge Thanks from Arglen
def act9():
    age = int(input("Enter your age: "))
    if age <= 1:
        print("You are a Toddler\n")
    elif age <= 8:
        print("You are a Pre-teen\n")
    elif age <= 14: 
        print("You are Teenager\n")
    elif age <= 19:
        print("You are in Early adulthood\n")
    elif age <= 32:
        print("You are in Mid adulthood\n")
    elif age <= 46:
        print("You are in Post adulthood\n")
    elif age >= 60:
        print("You are in your Senior\n")
    else:
        print("Invalid syntax\n")