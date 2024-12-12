def act5():
    temp = int(input("Enter temperature in Fahrenheit: "))
    cel = (temp - 32) * 5 / 9
    cel_r = round(cel, 2)
    print(f"\nThe conversion of  {temp} degrees Fahrenhet is {cel_r} degrees celsius.\n")