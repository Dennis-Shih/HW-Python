def calculator(number1, number2, operator):
	
	
	if (operator == '+'):
		print(number1+number2)
	elif (operator == '-'):
		print(number1-number2)
	elif (operator == '*'):
		print(number1*number2)
	elif (operator == '/'):
		print(number1/number2)
	elif (operator == '**'):
		print(number1**number2)
	else: return False
def input_output():
	shouldExit=False
	while not shouldExit:
		#firstnum=float(input("Enter the first number:"))
		#secondnum=float(input("Enter the second number:"))
		firstnum=input("Enter the first number:")
		secondnum=input("Enter the second number:")
		n1=float(firstnum)
		n2=float(secondnum)
		print(n1)
		print(n2)
		operator=input("Enter the operation:")
		print(operator)
		#calculator(firstnum,secondnum, operator)
		calculator(n1,n2, operator)
		wantToExit=input("Do you wish to exit?")
		if wantToExit=='y':
			shouldExit=True

#input_output()
