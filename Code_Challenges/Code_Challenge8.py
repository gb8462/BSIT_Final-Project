def Code8():
    odd_count = 0
    even_count = 0
    total_sum = 0

    for i in range(1, 11):
        user_input = int(input(f"Enter number {i}: "))
        total_sum += user_input
        
        if user_input % 2 == 0:
            even_count += 2
        else:
            odd_count += 1

    print(f"\nThe total sum of the numbers you entered is: {total_sum}")
    print(f"Even numbers tally: {even_count}")
    print(f"Odd numbers tally: {odd_count}")
