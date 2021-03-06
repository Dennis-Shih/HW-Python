"""Calculator that can do a number of math operations. If the 
        operator provided by the user is invalid (not +,-,*,**,/,or //)
        the calculator will not function."""
def calculator(number1, number2, operator):
	number1=float(number1)
	number2=float(number2)
	print(number1)
	print(number2)
	print(operator)
	result=0.0
	if (operator == '+'):
		print(number1+number2)
		return number1+number2
	elif (operator == '-'):
		print(number1-number2)
		return number1-number2
	elif (operator == '*'):
		print(number1*number2)
		return(number1*number2)
	elif (operator == '/'):
		print(number1/number2)
		return(number1/number2)
	elif (operator == '**'):
		print(number1**number2)
		return number1**number2
	elif (operator == '//'):
		print(number1//number2)
		return number1//number2
	else: return False

#takes input from the user and calls the calculator to carry out an operation
def input_output():
	shouldExit=False
	while not shouldExit:
		#firstnum=float(input("Enter the first number:"))
		#secondnum=float(input("Enter the second number:"))
		firstnum=input("Enter the first number:")
		secondnum=input("Enter the second number:")
		operator=input("Enter the operation:")
		calculator(firstnum,secondnum, operator)
		wantToExit=input("Do you wish to exit?")
		if wantToExit=='y':
			shouldExit=True

#input_output()
