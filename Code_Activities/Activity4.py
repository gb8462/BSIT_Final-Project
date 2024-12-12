def act4():
	print("========================================\n")
	num1 = eval(input("Number: "))
	num2 = eval(input("Number: "))
	op = input("Operators(+, -, /, x): ")

	if op == "+":
		print("Output:", num1 + num2)
	elif op == "-":
		print("Output:", num1 - num2)
	elif op == "/":
			print("Output:", num1 / num2)
	elif op == "x":
		print("Output:", num1 * num2)
	else:
		print("Invalid operator! \n\n")
	print("\n========================================")
