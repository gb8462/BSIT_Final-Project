# Code Written by Arglen
# Huge Thanks Again :D
# Factorial stuff
def act13():
    number = int(input("Enter any number: "))
    factorial = 1
    for fact in range(number, 0, -1):
        factorial *= fact 
        rounded = round(factorial, 2)
    print(f"The factorial of {rounded}\n")